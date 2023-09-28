import logging
import json


from main.core.config import STATE, PATH, ACTION
from main.request_ephor.request_to_server import RequestsServer
from main.respond_ephor.send_error import send_message


class RespondErrorSIGNAL(RequestsServer):

    def __init__(self):
        super().__init__()
        self.signal = self.request_state(
            path = PATH['state'],
            action = ACTION['read']
        )

    @property
    def get_automat_error_SIGNAL(self):
        automats_signal_error = [param for param in self.signal['data'] if param['automat_state'] == STATE['no connect']]
        return automats_signal_error
        
    @property
    def comparison_signal_error_ids(self):
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

    @property
    def get_params(self) -> list:
        signal_error_list = []
        for params in self.comparison_signal_error_ids:
            automat_param = {
                'id': params['automat_id'],
                'model': params['model_name'],
                'adress': params['point_adress'],
                'point': params['point_comment'],
                'name': params['point_name'],
                'error': 'Нет связи с автоматом!.'
            }
            signal_error_list.append(automat_param)
        return signal_error_list  

    @property
    def listen_signal_error(self):
        for error_automat in self.get_params:
            message = (
                f'Автомат № {error_automat["id"]}\n'
                f'{error_automat["adress"]}\n'
                f'{error_automat["point"]} --> {error_automat["name"]}\n'
                f'{error_automat["error"]}'
                ),
            logging.warning(f'Автомат № {error_automat["id"]}: {error_automat["error"]}')
            send_message(message)
            ids_automat_ERROR =  [ids['automat_id'] for ids in self.get_automat_error_SIGNAL]
            with open(
                file = 'main/respond_ephor/ids_errors/signal_error_ids.json',
                mode = 'w+'
            ) as file:
                json.dump(ids_automat_ERROR, file)