"""
Provides decorators for running functions concurrently.

Note that the usage of processes and threads should be chosen based on the task at hand. 
Processes are better for CPU-bound tasks, while threads are better for I/O-bound tasks due to the Global Interpreter Lock (GIL) in CPython.
"""

from threading import Thread
from multiprocessing import Process



def threaded(func):
    """Runs a function in a separate thread.

    Args:
        func: The function to run in a separate thread.

    Returns:
        A Thread object representing the new thread.
    """

    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


def process(func):
    """
    Runs a function in a separate process.

    Args:
        func: The function to be run in a separate process.

    Returns:
        A process object representing the running process.
    """

    def wrapper(*args, **kwargs):
        process = Process(target=func, args=args, kwargs=kwargs)
        process.start()
        return process

    return wrapper
