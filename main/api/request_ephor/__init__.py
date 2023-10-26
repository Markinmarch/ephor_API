import asyncio


from . import session
from . import request_to_server
from . session import Session
from . request_to_server import RequestsServer
from main.core.config import PATH, ACTION, FILTER


connection = asyncio.run(Session().login())
disconnection = asyncio.run(Session().logout())

ephor_requset = RequestsServer(connection=connection, disconnection=disconnection)

basic_request = asyncio.run(
    RequestsServer(
        connection=connection,
        disconnection=disconnection
        ).basic_request(
            path = PATH['state'], action = ACTION['read'])
            )

requset_params = asyncio.run(
    RequestsServer(

    )
)
