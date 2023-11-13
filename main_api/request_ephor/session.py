import time
import aiohttp


from core.config import URL, PATH, LOGIN, PASSWORD, ACTION


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

    async def login(self) -> str:
        '''
        Метод отправляет POST-запрос на сервер; в ответ
        получает параметр PHPSESSIONID для дальнейшей
        отправки GET-запросов. Выполяется вход пользователя 
        в систему. Возвращает параметр PHPSESSIONID
            Параметры:
                action: str
                    команда обработчика
        '''
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url = self.url + self.path,
                json = self.json,
                headers = self.headers,
                params = {
                    'action': ACTION['login'],
                    '_dc': self.id_request
                }
            ) as respond:
                return respond.headers.get('Set-Cookie').split('; ')[0]

    async def logout(self) -> int:
        '''
        Метод отправляет POST-запрос на сервер; 
        Выполняется закрытие сесси и выход пользователя
        их системы.
            Параметры: 
                action: str
                    команда обработчика
        '''
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url = self.url + self.path,
                json = self.json,
                headers = self.headers,
                params = {
                    'action': ACTION['logout'],
                    '_dc': self.id_request
                }
            ) as respond:
                return respond.status     