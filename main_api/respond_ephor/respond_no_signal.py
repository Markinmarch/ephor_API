import logging
import json
import datetime
from typing import Coroutine


from core.config import STATE, PATH, ACTION, ERRORS, SIGNAL_ERROR
from main_api.respond_ephor.send_error import send_msg
from main_api.request_ephor import ephor_requset


class RespondErrorSignal():
    '''
    Объект осуществляет получение, обработку данных
    и преобразование в понятный читабельный вид после
    GET-запроса. На выходе имеем данные по автоматам,
    у которых пропал сигнал.
    Наследуется объект RequestServer.
    '''
    def __init__(
        self,
        request
    ):
        super().__init__()
        self.request_signal_errors: Coroutine = request

    async def get_automat_error_SIGNAL(self) -> list:
        '''
        Метод получает параметры автоматов после GET-запроса
        у которых на сервере параметр "automat_state" равен параметру
        STATE["no connect"] равный двум (2). Таким образом мы получаем список данных
        с автоматами, у которых пропал сигнал.
        '''
        return [param for param in self.request_signal_errors['data'] if param['automat_state'] == STATE['no connect']]
        
    async def comparison_signal_error_ids(self) -> list:
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
        try:
            with open(
                file = 'main_api/respond_ephor/ids_errors/signal_error_ids.json',
                mode = 'r'
            ) as file:
                old_ids = json.load(file)
            comparison_list = [automat for automat in await self.get_automat_error_SIGNAL() if automat['automat_id'] not in old_ids]
            return comparison_list     
                
        except FileNotFoundError:
            return await self.get_automat_error_SIGNAL()

    async def get_params(self) -> list:
        '''
        Метод выборочно отбирает параметры каждого автомата из списка,
        полученного от метода "comparison_signal_error_ids" и присваивает им
        отдельный ключ. Возвращает список с выборочными параметрами по
        каждому автомату, у которого пропала связь.
        '''
        signal_error_list = []
        for params in await self.comparison_signal_error_ids():
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

    async def send_signal_error(self) -> None:
        '''
        Метод формирует тесктовое сообщение для отправки через
        метод "send_message" в телеграм-канал и реализует вывод
        лога в терминал. Затем идентификаторы автоматов
        перезаписывает в новый файл "signal_error_ids.json"
        '''
        now_hour = datetime.datetime.now().hour
        if 8 <= now_hour < 20:
            for signal_error in await self.get_params():
                message = 'Автомат № {0}\n{1}\n{2} --> {3}\n{4}'.format(
                    signal_error["id"],
                    signal_error["adress"],
                    signal_error["point"],
                    signal_error["name"],
                    signal_error["error"]
                )
                logging.warning(f'Автомат № {signal_error["id"]}: {signal_error["error"]}')
                await send_msg(message)
            ids_automat_NO_SIGNAL =  [ids['automat_id'] for ids in await self.get_automat_error_SIGNAL()]
            with open(
                file = 'main_api/respond_ephor/ids_errors/signal_error_ids.json',
                mode = 'w+'
            ) as file:
                json.dump(ids_automat_NO_SIGNAL, file)
        else:
            None
