import asyncio


from . import session
from . import request_to_server


from main.core.config import ACTION

async def huef():
    _get_request = request_to_server.RequestsServer(
        await asyncio.run(session.Session().login(action = ACTION['login'])),
        await asyncio.run(session.Session().logout(action = ACTION['logout']))
    )