from math import ceil
from time import sleep

import requests


# @Decorator function used to rate-limit API calls
def rate_limiter(max_calls_per_second):
    """
    Used with decorators to limit the number of calls to the Workable api
    """

    interval = ceil(1.0 / max_calls_per_second)

    def decorate(func):
        def rate_limited_function(*args, **kargs):
            sleep(interval)
            ret = func(*args, **kargs)

            return ret

        return rate_limited_function

    return decorate


@rate_limiter(max_calls_per_second=0.9)
def get_rate_limited_request(url, headers):
    result = requests.get(url, headers=headers)
    return result
