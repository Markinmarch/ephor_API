import json
import logging
from typing import Coroutine


from core.config import DESCRIPTION
from .send_error import send_msg


class RespondDoorStatus():
    '''
    Объект осуществляет получение и обработку данных 
    после GET-запроса на сервер в понятный читабельный вид.
    На выходе имеем данные по общим ошибкам в системе Эфор.
    Наследуется объект RequestServer
    '''
    def __init__(
        self,
        request_events,
        states_request
    ):
        self.request_events: Coroutine = request_events
        self.states_request: Coroutine = states_request

    async def get_automat_id_by_door_status(self) -> list:
        '''
        Метод выбирает из полученных данных после GET-запроса без фильрации
        параметры, у которых на сервере параметр "description" равен параметру
        DESCRIPTION['open_door'], равный нулю (0). Таким образом мы получаем
        список идентификаторов автоматов, у которых открыта дверь.
        '''
        return [
            param['automat_id'] for param
            in self.request_events['data']
            if param['description'] == DESCRIPTION['open_door']
            and 8 > int(param['date'][11:13]) >= 21
        ]

    async def comparison_ids_door_status(self) -> list:
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
                file = 'main_api/respond_ephor/ids_errors/door_status_open.json',
                mode = 'r'
            ) as file:
                old_ids = json.load(file)
            comparison_list = [ids for ids in await self.get_automat_id_by_door_status() if ids not in old_ids]
            return comparison_list     
               
        except FileNotFoundError:
            return await self.get_automat_id_by_door_status()
    
    async def get_params(self) -> list:
        '''
        Метод выборочно отбирает параметры каждого автомата из списка,
        полученного от метода "comparison_error_ids" и присваивает им
        отдельный ключ. Возвращает список с выборочными параметрами по
        каждому автомату, выпавшему в ошибку.
        '''
        automat_params_list = []
        for automat_id in await self.comparison_ids_door_status():
            automat_params_by_door_status = [param for param in self.states_request['data'] if param['automat_id'] == automat_id]
            for params in automat_params_by_door_status:
                automat_params = {
                    # выборочные параметры каждого автомата
                    'id': automat_id,
                    'adress': params['point_adress'],
                    'point': params['point_comment'],
                    'name': params['point_name'],
                    'door_status': DESCRIPTION['open_door']
                }
                automat_params_list.append(automat_params)
        return automat_params_list

    async def send_door_status(self) -> None:
        '''
        Метод формирует тесктовое сообщение для отправки через
        метод "send_message" в телеграм-канал и реализует вывод
        лога в терминал. Затем идентификаторы автоматов
        перезаписывает в новый файл "errors_ids.json"
        '''
        try:
            for automat_params in await self.get_params():
                message = 'Автомат № {0}\n{1}\n{2} --> {3}\n{4}'.format(
                    automat_params['id'],
                    automat_params['adress'],
                    automat_params['point'],
                    automat_params['name'],
                    automat_params['door_status']
                )
                logging.warning(f'Автомат № {automat_params["id"]} --> {automat_params["door_status"]}')
                await send_msg(message)
        except TypeError:
            None
        ids_automat_door_status = [ids for ids in await self.get_automat_id_by_door_status()]
        with open(
            file = 'main_api/respond_ephor/ids_errors/door_status_open.json',
            mode = 'w+'
        ) as file:
            json.dump(ids_automat_door_status, file) 