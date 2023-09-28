import logging
import json


from main.respond_ephor.respond_no_signal import RespondErrorSIGNAL
from main.respond_ephor.send_error import send_message


class StatusSignalOK(RespondErrorSIGNAL):

    def __init__(self):
        super().__init__()

    @property
    def check_signal(self):
        try:
            with open(
                file = 'main/respond_ephor/ids_errors/signal_error_ids.json',
                mode = 'r'
            ) as file:
                old_ids = json.load(file)
            signal_error_ids = [ids['automat_id'] for ids in self.get_automat_error_SIGNAL]
            comparison_list = [ids for ids in old_ids if ids not in signal_error_ids]
            if comparison_list == []:
                pass
            else:
                return comparison_list
        except FileNotFoundError:
            return None

    @property
    def get_params(self) -> list:
        signal_appeared_list = []
        for params in self.check_signal:
            automat_param = {
                'id': params['automat_id'],
                'model': params['model_name'],
                'adress': params['point_adress'],
                'point': params['point_comment'],
                'name': params['point_name'],
                'error': 'Автомат вышел на сявзь!'
            }
            signal_appeared_list.append(automat_param)
        return signal_appeared_list  

    @property
    def listen_signal_appeared(self):
        for param in self.get_params:
            message = (
                f'Автомат № {param["id"]}\n'
                f'{param["adress"]}\n'
                f'{param["point"]} --> {param["name"]}\n'
                f'{param["error"]}'
                ),
            logging.info(f'Автомат № {param["id"]}: {param["error"]}')
            send_message(message)
