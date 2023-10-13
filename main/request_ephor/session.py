import time
import requests


from main.core.config import URL, PATH, LOGIN, PASSWORD


class Session:
    '''
    Объект создаёт сессию для (зарегестрированного) пользователя
    '''
    def __init__(self):
        '''
        Устанавливает все необходимые атрибуты для объекта Session
            Параметры:
            *self
                user_login: str
                    индивидуальный логин пользователя при регистрации
                user_password: str
                    индивидуальный пароль пользователя при регистрации
                url: str
                    адрес сервера
                path: str
                    путь к обработчику данных
                    (url + path = путь запроса на сервер)
                time_zone: int
                    местный часовой пояс (по GSM)
                id_request: int
                    генерация числового значения по времени в секундах
                    (необходим при создании PHPSESSIONID)
                json: dict
                    скомпонованные JSON-параметры для осуществления запроса
                headers: dict
                    параметры REST-запроса
        '''

        self.user_login: str = LOGIN
        self.user_password: str = PASSWORD
        self.url: str = URL
        self.path: str = PATH['auth']
        self.time_zone: int = 3
        self.id_request: int = int(time.time())
        self.json: dict = {
                'login': self.user_login,
                'password': self.user_password,
                'time_zone': self.time_zone
            }
        self.headers: dict = {'Content-Type': 'application/json'}

    def login(self, action):
        '''
        Метод отправляет POST-запрос на сервер; в ответ
        получает параметр PHPSESSIONID для дальнейшей
        отправки GET-запросов. Выполяется вход пользователя 
        в систему. Возвращает параметр PHPSESSIONID
            Параметры:
                action: str
                    команда обработчика
        '''
        respond = requests.api.post(
            url = self.url + self.path,
            json = self.json,
            headers = self.headers,
            params = {
                'action': action,
                '_dc': self.id_request
            },
        )
        return respond.headers.get('Set-Cookie').split('; ')[0]
            
    def logout(self, action):
        '''
        Метод отправляет POST-запрос на сервер; 
        Выполняется закрытие сесси и выход пользователя
        их системы.
            Параметры: 
                action: str
                    команда обработчика
        '''
        respond = requests.api.post(
            url = self.url + self.path,
            json = self.json,
            headers = self.headers,
            params = {
                'action': action,
                '_dc': self.id_request
            }
        )
        return respond.status_code
