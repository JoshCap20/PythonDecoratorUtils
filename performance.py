"""Provides decorators for measuring performance."""

import time
import resource
from functools import wraps

def timeit(func):
    """
    Decorator to measure the execution time of a function.

    Args:
        func: The function to be timed.

    Returns:
        The result of the function call.

    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds to run.")
        return result
    return wrapper


def timeit_detailed(func):
    """Decorator to measure detailed execution time of a function (in milliseconds).
    
    Args:
        func: The function to be timed.
        
    Returns:
        The result of the function call.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {(end - start) * 1000:.3f} milliseconds to run.")
        return result
    return wrapper

def resource_usage(func):
    """
    Decorator to measure OS resources used by the function.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        usage_start = resource.getrusage(resource.RUSAGE_SELF)
        result = func(*args, **kwargs)
        usage_end = resource.getrusage(resource.RUSAGE_SELF)
        print(f"{func.__name__} used {usage_end.ru_maxrss - usage_start.ru_maxrss} kilobytes of memory")
        return result
    return wrapper

def cpu_timeit(func):
    """
    Decorator to measure the CPU execution time of a function (excluding sleep time).
    
    Parameters:
    func (function): The function to be timed.
    
    Returns:
    function: The wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        result = func(*args, **kwargs)
        end = time.process_time()
        print(f"{func.__name__} took {end - start} CPU seconds to run.")
        return result
    return wrapper

def cpu_timeit_detailed(func):
    """
    Decorator to measure the CPU execution time of a function (excluding sleep time).

    Args:
        func: The function to be timed.

    Returns:
        The result of the function call.

    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {(end - start) * 1000:.3f} milliseconds CPU seconds to run.")
        return result
    return wrapper

def count_calls(func):
    """
    Decorator to count the number of calls made to the function.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    function: The decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} of {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper