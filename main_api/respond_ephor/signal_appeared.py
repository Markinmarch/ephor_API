import logging
import json
import datetime
from typing import Any


from main_api.respond_ephor.respond_no_signal import RespondErrorSignal
from main_api.respond_ephor.send_error import send_msg
from main_api.request_ephor import states_request


class StatusSignalOK(RespondErrorSignal):
    '''
    Объект осуществляет получение, обработку данных
    и преобразование в понятный читабельный вид после
    GET-запроса. На выходе имеем данные по автоматам,
    у которых появился сигнал связи.
    Наследуется объект RespondErrorSignal.
    '''
    def __init__(self) -> None:
        super().__init__(states_request)

    async def check_signal(self) -> (list[Any] | None):
        '''
        Сначала метод проверяет диапазон времени для отправки этой ошибки, затем
        метод считывает идентификаторы (id) автоматов из файла "signal_error_ids.json" 
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
            signal_error_ids = [ids['automat_id'] for ids in await self.get_automat_error_SIGNAL()]
            comparison_list = [ids for ids in old_ids if ids not in signal_error_ids]
            return comparison_list
        except FileNotFoundError:
            None
            
    async def get_appeared_signal_automat(self) -> (list[Any] | None):
        '''
        Из метода "check_signal" получает идентификаторы и по ним
        получает параметры автоматов, которые вышли на связь.
        '''
        try:
            return [param for param in self.request_signal_errors['data'] if param['automat_id'] in await self.check_signal()]
        except TypeError:
            None
        
    async def get_signal_appeared(self) -> list:
        '''
        Метод выборочно отбирает параметры каждого автомата из списка,
        полученного от метода "get_appeared_signal_automat" и присваивает им
        отдельный ключ. Возвращает список с выборочными параметрами по
        каждому автомату, который вышел на связь.
        '''
        signal_appeared_list = []
        for params in await self.get_appeared_signal_automat():
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

    async def send_signal_appeared(self) -> None:
        '''
        Метод формирует тесктовое сообщение для отправки через
        метод "send_message" в телеграм-канал и реализует вывод
        лога в терминал.
        '''
        now_hour = datetime.datetime.now().hour
        if 8 <= now_hour < 20:
            if await self.get_appeared_signal_automat() == None:
                None
            else:
                for param in await self.get_signal_appeared():
                    message = 'Автомат № {0}\n{1}\n{2} --> {3}\n{4}'.format(
                        param["id"],
                        param["adress"],
                        param["point"],
                        param["name"],
                        param["error"]
                    )
                    logging.info(f'Автомат № {param["id"]}: {param["info"]}')
                    send_msg(message)
        else:
            None
