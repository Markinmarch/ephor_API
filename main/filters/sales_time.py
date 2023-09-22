import datetime


from main.core.config import ERRORS


def cathc_sales_error(func):
    def wrapper(*args):
        now_hour = datetime.datetime.now().hour
        weekends = [5, 6]
        now_day = datetime.datetime.today().weekday()
        for item in func(*args):
            return_val = item['error']
            if return_val in ERRORS and 8 <= now_hour <= 11 and now_day not in weekends:
                return return_val
            elif return_val not in ERRORS:
                return return_val
    return wrapper

