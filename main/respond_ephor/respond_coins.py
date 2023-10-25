import logging
import json


from main.core.config import STATE, PATH, ACTION
from main.request_ephor.request_to_server import RequestsServer
from main.respond_ephor.send_error import send_message


class RespondCoinsCount(RequestsServer):
    '''
    Объект осуществляет получение, обработку данных
    и преобразование в понятный читабельный вид после
    GET-запроса. На выходе имеем данные по автоматам,
    у которых в аппарате для размена в тубах осталось
    меньше 550 рублей. Наследуется объект RequestServer.
    '''
    def __init__(self):
        super().__init__()
        self.coins = self.basic_request(
            path = PATH['state'],
            action = ACTION['read']
        )

    @property
    def get_automat_COINS(self) -> list:
        '''
        Метод на входе осуществляет GET-запрос с сервера
        и на выходе получаем данные автоматов у которых
        на размен осталось меньше 550 рублей
        '''
        automats_COINS = [param for param in self.coins['data'] if param['model_name'] != 'Coffeemar G-23' and param['automat_state'] == STATE['ok']]
        get_few_coins_automat = [param for param in automats_COINS if param['now_tube_val'] <= 550]
        return get_few_coins_automat
        
    @property
    def comparison_coins_ids(self) -> list:
        '''
        Метод считывает идентификаторы (id) автоматов из файла "coins_id.json" 
        и сравнивает их с идетификаторами, которые берёт из нового списка
        обработанных данных метода "get_automat_COINS". Если файла
        "coins_id.json" нет, то он просто возвращает список метода
        "get_automat_COINS". Если файл имеется, тогда при наличии
        новых идентификаторов из нового списка - возвращается список с данными,
        имеющие новые идетификаторы.
        '''
        try:
            with open(
                file = 'main/respond_ephor/ids_errors/coins_ids.json',
                mode = 'r'
            ) as file:
                old_ids = json.load(file)

            comparison_list = [automat for automat in self.get_automat_COINS if automat['automat_id'] not in old_ids]
            return comparison_list     
               
        except FileNotFoundError:
            return self.get_automat_COINS

    @property
    def get_params(self) -> list:
        '''
        Метод выборочно отбирает параметры каждого автомата из списка,
        полученного от метода "comparison_coins_ids" и присваивает им
        отдельный ключ. Возвращает список с выборочными параметрами по
        каждому автомату, у которого на размен осталось меньше 550 руб.
        '''
        few_coins_list = []
        for params in self.comparison_coins_ids:
            automat_param = {
                # выборочные параметры каждого автомата
                'id': params['automat_id'],
                'model': params['model_name'],
                'adress': params['point_adress'],
                'point': params['point_comment'],
                'name': params['point_name'],
                'error': 'В монетоприёмнике мало размена.'
            }
            few_coins_list.append(automat_param)
        return few_coins_list  

    @property
    def send_coins_count(self) -> None:
        '''
        Метод формирует тесктовое сообщение для отправки через
        метод "send_message" в телеграм-канал и реализует вывод
        лога в терминал. Затем идентификаторы автоматов
        перезаписывает в новый файл "coins_ids.json"
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
        ids_automat_COINS =  [ids['automat_id'] for ids in self.get_automat_COINS]
        with open(
            file = 'main/respond_ephor/ids_errors/coins_ids.json',
            mode = 'w+'
        ) as file:
            json.dump(ids_automat_COINS, file)