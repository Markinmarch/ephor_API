import asyncio


from . import respond_error
# from . import respond_coins
# from . import send_error
# from . import respond_no_signal
# from . import signal_appeared

from main.core.config import PATH, ACTION, FILTER


from main.api.request_ephor import _get_request

_get_respond_error = respond_error.RespondError(
    state = asyncio.run(
        _get_request.basic_request(
            path = PATH['state'],
            action = ACTION['read']
        )
    )
)