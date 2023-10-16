import logging
import json
from typing import Any


from main.respond_ephor.respond_no_signal import RespondErrorSignal
from main.respond_ephor.send_error import send_message


class StatusSignalOK(RespondErrorSignal):
    '''
    Объект осуществляет получение, обработку данных
    и преобразование в понятный читабельный вид после
    GET-запроса. На выходе имеем данные по автоматам,
    у которых появился сигнал связи.
    Наследуется объект RespondErrorSignal.
    '''
    def __init__(self) -> None:
        super().__init__()

    @property
    def check_signal(self) -> (list[Any] | None):
        '''
        Метод считывает идентификаторы (id) автоматов из файла "signal_error_ids.json" 
        и сравнивает их с идетификаторами, которые берёт из нового списка
        обработанных данных метода "get_automat_error_SIGNAL". Если файла
        "signal_error_ids.json" нет, то он возвращает "None". Если файл имеется,
        тогда при отсутствии идентификаторов из старого списка в запрошенном - возвращает
        идентификаторы, которые отсутствуют в новом списке идентификаторов.
        '''
        try:
            with open(
                file = 'main/respond_ephor/ids_errors/signal_error_ids.json',
                mode = 'r'
            ) as file:
                old_ids = json.load(file)
            signal_error_ids = [ids['automat_id'] for ids in self.get_automat_error_SIGNAL]
            comparison_list = [ids for ids in old_ids if ids not in signal_error_ids]
            return comparison_list
        except FileNotFoundError:
            return None
    
    @property
    def get_appeared_signal_automat(self) -> (list[Any] | None):
        '''
        Из метода "check_signal" получает идентификаторы и по ним
        получает параметры автоматов, которые вышли на связь.
        '''
        try:
            return [param for param in self.signal['data'] if param['automat_id'] in self.check_signal]
        except TypeError:
            return None
        
    @property
    def get_signal_appeared(self) -> list:
        '''
        Метод выборочно отбирает параметры каждого автомата из списка,
        полученного от метода "get_appeared_signal_automat" и присваивает им
        отдельный ключ. Возвращает список с выборочными параметрами по
        каждому автомату, который вышел на связь.
        '''
        signal_appeared_list = []
        for params in self.get_appeared_signal_automat:
            automat_param = {
                'id': params['automat_id'],
                'model': params['model_name'],
                'adress': params['point_adress'],
                'point': params['point_comment'],
                'name': params['point_name'],
                'info': 'Автомат вышел на связь!'
            }
            signal_appeared_list.append(automat_param)
        return signal_appeared_list  

    @property
    def send_signal_appeared(self) -> None:
        '''
        Метод формирует тесктовое сообщение для отправки через
        метод "send_message" в телеграм-канал и реализует вывод
        лога в терминал.
        '''
        if self.get_appeared_signal_automat == None:
            return None
        else:
            for param in self.get_signal_appeared:
                message = (
                    f'Автомат № {param["id"]}\n'
                    f'{param["adress"]}\n'
                    f'{param["point"]} --> {param["name"]}\n'
                    f'{param["info"]}'
                    ),
                logging.info(f'Автомат № {param["id"]}: {param["info"]}')
                send_message(message)
