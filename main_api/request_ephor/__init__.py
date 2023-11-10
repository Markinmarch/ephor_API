import asyncio


from . import session
from . import request_to_server


from .session import Session
from .request_to_server import RequestsServer
from ...core.config import PATH, ACTION


connection = asyncio.run(Session().login())
disconnection = asyncio.run(Session().logout())

ephor_requset = RequestsServer(connection=connection, disconnection=disconnection)

states_request = asyncio.run(
    ephor_requset.basic_request(
        path = PATH['state'],
        action = ACTION['read']
    )
)

event_request = asyncio.run(
    ephor_requset.basic_request(
        path = PATH['event'],
        action = ACTION['read_all']
    )
)