import logging
import json
import datetime


from main.core.config import STATE, PATH, ACTION, ERRORS, SIGNAL_ERROR
from main.request_ephor.request_to_server import RequestsServer
from main.respond_ephor.send_error import send_message


class RespondErrorSignal(RequestsServer):
    '''
    Объект осуществляет получение, обработку данных
    и преобразование в понятный читабельный вид после
    GET-запроса. На выходе имеем данные по автоматам,
    у которых пропал сигнал.
    Наследуется объект RequestServer.
    '''
    def __init__(self) -> None:
        super().__init__()
        self.signal = self.basic_request(
            path = PATH['state'],
            action = ACTION['read']
        )

    @property
    def get_automat_error_SIGNAL(self) -> list:
        '''
        Метод получает параметры автоматов после GET-запроса
        у которых на сервере параметр "automat_state" равен параметру
        STATE["no connect"] равный двум (2). Таким образом мы получаем список данных
        с автоматами, у которых пропал сигнал.
        '''
        automats_signal_error = [param for param in self.signal['data'] if param['automat_state'] == STATE['no connect']]
        return automats_signal_error
        
    @property
    def comparison_signal_error_ids(self) -> list:
        '''
        Сначала метод проверяет диапазон времени для отправки этой ошибки, затем
        метод считывает идентификаторы (id) автоматов из файла "signal_error_ids.json" 
        и сравнивает их с идетификаторами, которые берёт из нового списка
        обработанных данных метода "get_automat_error_SIGNAL". Если файла
        "signal_error_ids.json" нет, то он просто возвращает список метода
        "get_automat_error_SIGNAL". Если файл имеется, тогда при наличии
        новых идентификаторов из нового списка - возвращается список с данными,
        имеющие новые идетификаторы.
        '''
        now_hour = datetime.datetime.now().hour
        if 10 <= now_hour < 20:
            try:
                with open(
                    file = 'main/respond_ephor/ids_errors/signal_error_ids.json',
                    mode = 'r'
                ) as file:
                    old_ids = json.load(file)
                comparison_list = [automat for automat in self.get_automat_error_SIGNAL if automat['automat_id'] not in old_ids]
                return comparison_list     
                
            except FileNotFoundError:
                return self.get_automat_error_SIGNAL
        else:
            None

    @property
    def get_params(self) -> list:
        '''
        Метод выборочно отбирает параметры каждого автомата из списка,
        полученного от метода "comparison_signal_error_ids" и присваивает им
        отдельный ключ. Возвращает список с выборочными параметрами по
        каждому автомату, у которого пропала связь.
        '''
        signal_error_list = []
        for params in self.comparison_signal_error_ids:
            automat_param = {
                'id': params['automat_id'],
                'model': params['model_name'],
                'adress': params['point_adress'],
                'point': params['point_comment'],
                'name': params['point_name'],
                'error': SIGNAL_ERROR
            }
            signal_error_list.append(automat_param)
        return signal_error_list  
    
    @property
    def send_signal_error(self) -> None:
        '''
        Метод формирует тесктовое сообщение для отправки через
        метод "send_message" в телеграм-канал и реализует вывод
        лога в терминал. Затем идентификаторы автоматов
        перезаписывает в новый файл "signal_error_ids.json"
        '''
        for error_automat in self.get_params:
            message = (
                f'Автомат № {error_automat["id"]}\n'
                f'{error_automat["adress"]}\n'
                f'{error_automat["point"]} --> {error_automat["name"]}\n'
                f'{error_automat["error"]}'
                ),
            logging.warning(f'Автомат № {error_automat["id"]}: {error_automat["error"]}')
            send_message(message)
        ids_automat_NO_SIGNAL =  [ids['automat_id'] for ids in self.get_automat_error_SIGNAL]
        with open(
            file = 'main/respond_ephor/ids_errors/signal_error_ids.json',
            mode = 'w+'
        ) as file:
            json.dump(ids_automat_NO_SIGNAL, file)

