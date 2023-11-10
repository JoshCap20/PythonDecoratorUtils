from functools import wraps
import time


def suppress_errors(default_value=None, exceptions=(Exception,)):
    """
    Decorator that suppresses specified exceptions and optionally returns a default value.

    Args
        default_value: Optional default value to return when an exception is suppressed.
        exceptions: Tuple of exceptions to suppress. Defaults to catching all exceptions.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                print(f"Exception suppressed: {e}")
                return default_value

        return wrapper

    return decorator


def retry(attempts: int = 3, delay: int = 1):
    """
    Decorator to retry a function call with a specified delay between attempts.

    Args:
        attempts (int): The number of times to retry the function call.
        delay (int): The delay in seconds between each retry attempt.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal attempts
            while attempts > 1:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying {func.__name__}, attempts remaining: {attempts-1}")
                    time.sleep(delay)
                    attempts -= 1
            return func(*args, **kwargs)

        return wrapper

    return decorator
