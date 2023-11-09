# from . import respond_error
# from . import respond_coins
# from . import respond_no_signal
# from . import signal_appeared
from . import door_status

from main_api.request_ephor import states_request, event_request
from main_api.respond_ephor.respond_error import RespondError
from main_api.respond_ephor.respond_coins import RespondCoinsCount
from main_api.respond_ephor.respond_no_signal import RespondErrorSignal
from main_api.respond_ephor.signal_appeared import StatusSignalOK
from main_api.respond_ephor.door_status import RespondDoorStatus
    

responder_error = RespondError(states_request)
responder_coins = RespondCoinsCount(states_request)
responder_error_signal = RespondErrorSignal(states_request)
appeared_signal = StatusSignalOK()
responder_door_status = RespondDoorStatus(event_request, states_request)