import logging
import json


from main.core.config import STATE, PATH, ACTION
from main.request_ephor.request_to_server import RequestsServer
from main.respond_ephor.send_error import send_message


class RespondCoinsCount(RequestsServer):

    def __init__(self):
        super().__init__()
        self.coins = self.request_state(
            path = PATH['state'],
            action = ACTION['read']
        )

    @property
    def get_automat_COINS(self):
        automats_COINS = [param for param in self.coins['data'] if param['model_name'] != 'Coffeemar G-23' and param['automat_state'] == STATE['ok']]
        get_few_coins_automat = [param for param in automats_COINS if param['now_tube_val'] <= 550]
        return get_few_coins_automat
        
    @property
    def comparison_coins_ids(self):
        try:
            with open(
                file = 'main/respond_ephor/coins_ids.json',
                mode = 'r'
            ) as file:
                old_ids = json.load(file)

            comparison_list = [automat for automat in self.get_automat_COINS if automat['automat_id'] not in old_ids]
            return comparison_list     
               
        except FileNotFoundError:
            return self.get_automat_COINS

    @property
    def get_params(self) -> list:
        few_coins_list = []
        for params in self.comparison_coins_ids:
            automat_param = {
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
    def listen_coins_count(self):
        for error_automat in self.get_params:
            message = (
                f'Автомат № {error_automat["id"]}\n'
                f'{error_automat["adress"]}\n'
                f'{error_automat["point"]} --> {error_automat["name"]}\n'
                f'{error_automat["error"]}'
                ),
            logging.warning(f'Автомат № {error_automat["id"]}: {error_automat["error"]}')
            send_message(message)
            ids_automat_ERROR =  [ids['automat_id'] for ids in self.get_automat_COINS]
            with open(
                file = 'main/respond_ephor/coins_ids.json',
                mode = 'w+'
            ) as file:
                json.dump(ids_automat_ERROR, file)