import requests
import json
import asyncio
import time
import logging


from telegram_bot.settings.config import BOT_TOKEN, CHANNEL_ID
from main.core.config import STATUS
from main.request.request_to_server import Requests_automat
from main.request.test import lstlst


def search_errors() -> list:
    request_all = asyncio.run(Requests_automat().request_automat())
    errors_automat_ids = [
        automat_param['automat_id'] for automat_param in request_all['data'] if automat_param['automat_state'] == STATUS['error']
        ]
    errors_automat = [
        automat_param for automat_param in request_all['data'] if automat_param['automat_state'] == STATUS['error']
        ]
    with open(
        file = 'main/request/datas.json',
        mode = 'w+'
    ) as file:
        json.dump(errors_automat_ids, file)
    return errors_automat

def comparison():
    try:
        with open(
            file = 'main/request/datas.json',
            mode = 'r'
        ) as file:
            old_errors = json.load(file)
            comparison_list = [automat for automat in search_errors() if not automat['automat_id'] in old_errors]
            if comparison_list == []:
                return None
            else:
                return comparison_list
    except FileNotFoundError:
        return search_errors()

def check_automat_params() -> list:
    try:
        errors_automat_list = []
        for params in comparison():
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
        for params in search_errors():
            automat_param = {
                'id': params['automat_id'],
                'model': params['model_name'],
                'adress': params['point_adress'],
                'point': params['point_comment'],
                'name': params['point_name']
            }
            errors_automat_list.append(automat_param)
        return errors_automat_list


def check_automat_errors() -> list:
    for params in check_automat_params():
        get_error = asyncio.run(Requests_automat().check_error(params['id']))
        error_descriptions = []
        for error in get_error['data']:
            error_descriptions.append({'error': error['description']})
        return error_descriptions

def merge_params():
    check_list = []
    for params_dict, params_errors in zip(check_automat_params(), check_automat_errors()):
        check_list.append(params_dict | params_errors)
    return check_list

def send_message(token, chat_id, message, method):
    response = requests.post(
        url = 'https://api.telegram.org/bot{0}/{1}'.format(token, method),
        data = {
            'chat_id': chat_id,
            'text': message
        }
    )
    return response.json()

def listen_errors():
    while True:
        if comparison() != None:
            for error_automat in merge_params():
                send_message(
                    token = BOT_TOKEN,
                    chat_id = CHANNEL_ID,
                    message = (
                        f'Автомат № {error_automat["id"]}\n'
                        f'{error_automat["adress"]}\n'
                        f'{error_automat["point"]} --> {error_automat["name"]}\n'
                        f'{error_automat["error"]}'
                    ),
                    method = 'sendMessage'
                )
                logging.warning(
                    f'--- AUTOMAT ID: {error_automat["id"]} --- '
                    f'ADRESS: {error_automat["adress"]} --- '
                    f'ERROR: {error_automat["error"]} ---\n'
                    '----------------------------------------------'
                )
        time.sleep(60)
    
listen_errors()