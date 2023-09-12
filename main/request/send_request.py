from aiohttp import ClientSession
import asyncio
import time
import logging
import json


from main.core.config import URL, PATH, STATUS
from main.request.session import connect, disconnect


class Requests_automat:

    def __init__(self):  
        self.url = URL
        self.time_zone = 3
        self.id_request = int(time.time())
        
    async def request_automat(self):
        async with ClientSession(base_url = self.url) as session:
            async with session.get(
                url = PATH['state'],
                headers = {
                    'Content-Type': 'application/json',
                    'Host': 'erp.ephor.online',
                    'Connection': 'keep-alive',
                    'Cookie': connect,
                },
                params = {
                    'action': 'Read',
                    '_dc': self.id_request
                }
            ) as respond:
                disconnect
                return await respond.json(content_type = 'text/html')
        
    async def check_error(self, id):
        async with ClientSession(base_url = self.url) as session:
            async with session.get(
                url =  PATH['error'],
                headers = {
                    'Content-Type': 'application/json',
                    'Host': 'erp.ephor.online',
                    'Connection': 'keep-alive',
                    'Cookie': connect,
                },
                params = {
                    'action': 'Read',
                    '_dc': self.id_request,
                    'filter': ('[{"property": "automat_id", "value": %s}]' % id)
                }
            ) as respond:
                disconnect
                return await respond.json(content_type = 'text/html')

request_all = asyncio.run(Requests_automat().request_automat())

def search_errors() -> list:
    errors_automat_ids = [
        automat_param['automat_id'] for automat_param in request_all['data'] if automat_param['automat_state'] == STATUS['error']
        ]
    errors_automat = [
        automat_param for automat_param in request_all['data'] if automat_param['automat_state'] == STATUS['error']
        ]
    with open(
        file = 'main/request/datas.json',
        mode = 'w'
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


def check_errors():
    errors_automat_list = []
    try:
        for param in comparison():
            get_error = asyncio.run(Requests_automat().check_error(param['automat_id']))
            for error in get_error['data']:
                error_automat = {
                    'id': param['automat_id'],
                    'model': param['model_name'],
                    'adress': param['point_adress'],
                    'point': param['point_comment'],
                    'name': param['point_name'],
                    'error': error['description']
                }
                errors_automat_list.append(error_automat)           
            return errors_automat_list
        
    except (FileNotFoundError, TypeError):
        for param in search_errors():
            get_error = asyncio.run(Requests_automat().check_error(param['automat_id']))
            for error in get_error['data']:
                error_automat = {
                    'id': param['automat_id'],
                    'model': param['model_name'],
                    'adress': param['point_adress'],
                    'point': param['point_comment'],
                    'name': param['point_name'],
                    'error': error['description']
                }
                errors_automat_list.append(error_automat)           
            return errors_automat_list
    
    # except TypeError:
    #     return None
    
# print(check_errors())

        #     get_error = asyncio.run(Requests_automat().check_error(param['automat_id']))
        #     for error in get_error['data']:
        #         error_automat = {
        #             'id': param['automat_id'],
        #             'model': param['model_name'],
        #             'adress': param['point_adress'],
        #             'point': param['point_comment'],
        #             'name': param['point_name'],
        #             'error': error['description']
        #         }
        #         errors_automat_list.append(error_automat)           
        # return errors_automat_list 

# print(check_errors())

def listen_errors():
    while True:
        # print(check_errors())
        # print('-----------------------------------------')
        # print(comparison())
        # print('-----------------------------------------')

        if comparison() != None:
            for error_automat in check_errors():
                logging.warning(
                    f'--- AUTOMAT ID: {error_automat["id"]} --- '
                    f'ADRESS: {error_automat["adress"]} --- '
                    f'ERROR: {error_automat["error"]} ---\n'
                    '----------------------------------------------'
                )
        elif comparison() == None:
            logging.info('--- All machines in the OK state ---')
        time.sleep(10)
    
listen_errors()
