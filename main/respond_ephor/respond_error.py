import datetime
import json
import logging


from main.core.config import STATE, PATH, ACTION, FILTER, ERRORS, SPEC_ERROR
from main.request_ephor.request_to_server import RequestsServer
from main.respond_ephor.send_error import send_message


class RespondError(RequestsServer):
    '''
    Объект осуществляет получение и обработку данных 
    после GET-запроса на сервер в понятный читабельный вид.
    На выходе имеем данные по общим ошибкам в системе Эфор.
    Наследуется объект RequestServer
    '''
    def __init__(self):
        super().__init__()
        self.state = self.basic_request(
            path = PATH['state'],
            action = ACTION['read']
        )

    @property
    def get_params_automat_ERROR(self) -> list:
        '''
        Метод выбирает из полученных данных после GET-запроса без фильрации
        параметры, у которых на сервере параметр "automat_state" равен параметру
        STATE["error"], равный нулю (0). Таким образом мы получаем список данных
        с автоматами, которые находятся в ошибке.
        '''
        automats_ERROR = [param for param in self.state['data'] if param['automat_state'] == STATE['error']]
        return automats_ERROR

    @property
    def comparison_error_ids(self):
        '''
        Метод считывает идентификаторы (id) автоматов из файла "errors_id.json" 
        и сравнивает их с идетификаторами, которые берёт из нового списка
        обработанных данных метода "get_params_automat_ERROR". Если файла
        "errors_id.json" нет, то он просто возвращает список метода
        "get_params_automat_ERRORS". Если файл имеется, тогда при наличии
        новых идентификаторов из нового списка - возвращается список с данными,
        имеющие новые идетификаторы.
        '''
        try:
            with open(
                file = 'main/respond_ephor/ids_errors/errors_id.json',
                mode = 'r'
            ) as file:
                old_ids = json.load(file)
            comparison_list = [automat for automat in self.get_params_automat_ERROR if automat['automat_id'] not in old_ids]
            return comparison_list     
               
        except FileNotFoundError:
            return self.get_params_automat_ERROR
    
    @property
    def get_params(self) -> list:
        '''
        Метод выборочно отбирает параметры каждого автомата из списка,
        полученного от метода "comparison_error_ids" и присваивает им
        отдельный ключ. Возвращает список с выборочными параметрами по
        каждому автомату, выпавшему в ошибку.
        '''
        errors_automat_list = []
        for params in self.comparison_error_ids:
            automat_param = {
                # выборочные параметры каждого автомата
                'id': params['automat_id'],
                'model': params['model_name'],
                'adress': params['point_adress'],
                'point': params['point_comment'],
                'name': params['point_name']
            }
            errors_automat_list.append(automat_param)
        return errors_automat_list            

    @property
    def get_automat_errors(self) -> list:
        '''
        Метод реализует получение описания ошибки каждого автомата
        выпавшего в ошибку посредством использования метода 
        "request_params" из объекта "RequestsServer" с фильтрацией
        данных по параметру "automat_id"(FILTER["automat"]). Параметр
        идентификатора каждого автомата взят из списка метода "get_params".
        Возвращает список ошибок каждого автомата.
        '''
        error_descriptions = []
        for params in self.get_params:
            get_error = self.request_params(
                PATH['error'],
                ACTION['read'],
                FILTER['automat'],
                params['id']
            )
            for error in get_error['data']:
                error_descriptions.append({'error': error['description']})
        return error_descriptions

    
    @property
    def merge_params(self):
        '''
        Метод реализует слияние выборочных параметров каждого автомата выпавшего
        в ошибку и их описание ошибки.
        '''
        merge_list = []
        for params_dict, params_errors in zip(self.get_params, self.get_automat_errors):
            merge_list.append(params_dict | params_errors)
        return merge_list

    @property
    def filter_sales(self):
        '''
        Метод реализует игнорирование ошибки о состоянии автомата,
        которые долго не продавали в определённое время суток,
        а так же игнорирование ошибки, которая свидетельствует о том,
        что оплата по безналу не прошла.
        '''
        now_hour = datetime.datetime.now().hour
        weekends = [5, 6]
        now_day = datetime.datetime.today().weekday()
        new_filter_list = []
        for param in self.merge_params:
            if param['error'] in ERRORS and 9 <= now_hour <= 13 and now_day not in weekends:
                return None
            if param['error'] not in ERRORS and SPEC_ERROR not in param['error']:
                new_filter_list.append(param)
        return new_filter_list

    @property
    def send_errors(self) -> None:
        '''
        Метод формирует тесктовое сообщение для отправки через
        метод "send_message" в телеграм-канал и реализует вывод
        лога в терминал. Затем идентификаторы автоматов
        перезаписывает в новый файл "errors_ids.json"
        '''
        try:
            for error_automat in self.filter_sales:
                message = (
                    f'Автомат № {error_automat["id"]}\n'
                    f'{error_automat["adress"]}\n'
                    f'{error_automat["point"]} --> {error_automat["name"]}\n'
                    f'{error_automat["error"]}'
                    ),
                logging.warning(f'Автомат № {error_automat["id"]} выпал в ошибку {error_automat["error"]}')
                send_message(message)
        except TypeError:
            None
        ids_automat_ERROR =  [ids['automat_id'] for ids in self.get_params_automat_ERROR]
        with open(
            file = 'main/respond_ephor/ids_errors/errors_id.json',
            mode = 'w+'
        ) as file:
            json.dump(ids_automat_ERROR, file) 