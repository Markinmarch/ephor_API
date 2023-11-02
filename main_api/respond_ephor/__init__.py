from . import respond_error
from . import respond_coins
from . import respond_no_signal
from . import signal_appeared

from main_api.request_ephor import basic_request
from main_api.respond_ephor.respond_error import RespondError
from main_api.respond_ephor.respond_coins import RespondCoinsCount
from main_api.respond_ephor.respond_no_signal import RespondErrorSignal
from main_api.respond_ephor.signal_appeared import StatusSignalOK
    

responder_error = RespondError(basic_request)
responder_coins = RespondCoinsCount(basic_request)
responder_error_signal = RespondErrorSignal(basic_request)
appeared_signal = StatusSignalOK()