import requests
import json
import time
import logging


from telegram_bot.settings.config import BOT_TOKEN, CHANNEL_ID
from main.core.config import STATUS
from main.request.request_to_server import RequestsServer


class Responders:

    def __init__(self):
        self.R_server = RequestsServer().request_server
        self.token = BOT_TOKEN
        self.chat_id = CHANNEL_ID
        self.post_method = 'sendMessage'

    @property
    def get_params_automat_ERROR(self):
        automats_ERROR = [param for param in self.R_server['data'] if param['automat_state'] == STATUS['error']]
        ids_automat_ERROR =  [ids['automat_id'] for ids in automats_ERROR]
        with open(
            file = 'main/request/datas.json',
            mode = 'w+'
        ) as file:
            json.dump(ids_automat_ERROR, file)
        return automats_ERROR

    @property
    def comparison(self):
        try:
            with open(
                file = 'main/request/datas.json',
                mode = 'r'
            ) as file:
                old_ids = json.load(file)
            comparison_list = [automat for automat in self.get_params_automat_ERROR if automat['automat_id'] not in old_ids]
            if comparison_list == []:
                return None
            else:
                return comparison_list
        except FileNotFoundError:
            return self.get_params_automat_ERROR
    
    @property
    def get_params(self):
        try:
            errors_automat_list = []
            for params in self.comparison:
                automat_param = {
                    'id': params['automat_id'],
                    'model': params['model_name'],
                    'adress': params['point_adress'],
                    'point': params['point_comment'],
                    'name': params['point_name']
                }
                errors_automat_list.append(automat_param)
            return errors_automat_list      

        except TypeError:
            errors_automat_list = []
            for params in self.get_params_automat_ERROR:
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
            get_error = RequestsServer().check_error(params['id'])
        for error in get_error['data']:
            error_descriptions.append({'error': error['description']})
        return error_descriptions

    @property
    def merge_params(self):
        check_list = []
        for params_dict, params_errors in zip(self.get_params, self.check_automat_errors):
            check_list.append(params_dict | params_errors)
        return check_list

    def send_message(
        self,
        message
    ):
        response = requests.post(
            url = 'https://api.telegram.org/bot{0}/{1}'.format(self.token, self.post_method),
            data = {
                'chat_id': self.chat_id,
                'text': message
            }
        )
        return response.json()

    @property
    def listen_errors(self):
        while True:
            if self.comparison != None:
                for error_automat in self.merge_params:
                    message = (
                        f'Автомат № {error_automat["id"]}\n'
                        f'{error_automat["adress"]}\n'
                        f'{error_automat["point"]} --> {error_automat["name"]}\n'
                        f'{error_automat["error"]}'
                        ),
                    logging.warning(f'Автомат № {error_automat["id"]} выпал в ошибку {error_automat["error"]}')
                    self.send_message(message = message)
            time.sleep(60)
    
Responders().listen_errors