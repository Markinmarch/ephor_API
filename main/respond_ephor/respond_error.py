import requests
import json
import logging


from main.core.config import STATE, PATH, ACTION, FILTER
from main.request_ephor.request_to_server import RequestsServer
from main.respond_ephor.send_error import send_message


class RespondError(RequestsServer):

    def __init__(self):
        super().__init__()
        self.state = self.request_state(PATH['state'], ACTION['read'])

    @property
    def get_params_automat_ERROR(self):
        automats_ERROR = [param for param in self.state['data'] if param['automat_state'] == STATE['error']]
        return automats_ERROR

    @property
    def comparison_error_ids(self):
        try:
            with open(
                file = 'main/respond_ephor/errors_id.json',
                mode = 'r'
            ) as file:
                old_ids = json.load(file)
            comparison_list = [automat for automat in self.get_params_automat_ERROR if automat['automat_id'] not in old_ids]
            return comparison_list     
               
        except FileNotFoundError:
            return self.get_params_automat_ERROR
    
    @property
    def get_params(self):
        errors_automat_list = []
        for params in self.comparison_error_ids:
            automat_param = {
                'id': params['automat_id'],
                'model': params['model_name'],
                'adress': params['point_adress'],
                'point': params['point_comment'],
                'name': params['point_name']
            }
            errors_automat_list.append(automat_param)
        return errors_automat_list            

    @property
    def check_automat_errors(self) -> list:
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
        check_list = []
        for params_dict, params_errors in zip(self.get_params, self.check_automat_errors):
            check_list.append(params_dict | params_errors)
        return check_list

    @property
    def listen_errors(self):
        for error_automat in self.merge_params:
            message = (
                f'Автомат № {error_automat["id"]}\n'
                f'{error_automat["adress"]}\n'
                f'{error_automat["point"]} --> {error_automat["name"]}\n'
                f'{error_automat["error"]}'
                ),
            logging.warning(f'Автомат № {error_automat["id"]} выпал в ошибку {error_automat["error"]}')
            send_message(message = message)
            ids_automat_ERROR =  [ids['automat_id'] for ids in self.get_params_automat_ERROR]
            with open(
                file = 'main/respond_ephor/errors_id.json',
                mode = 'w+'
            ) as file:
                json.dump(ids_automat_ERROR, file)
