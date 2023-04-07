import time
from functools import wraps


def retry_on_exception(retries=3, delay=5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < retries:
                        time.sleep(delay)
                    else:
                        raise e
        return wrapper
    return decorator
