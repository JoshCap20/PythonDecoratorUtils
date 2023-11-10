# PythonDecoratorUtils

A collection of Python decorators designed for enhancing functions with concurrency, error handling, and performance measurement capabilities.

## Concurrency Decorators (`concurrency.py`)

This module provides decorators for running functions concurrently, utilizing threads and processes.

- `@threaded`: Runs a function in a separate thread, suitable for I/O-bound tasks to avoid blocking the main thread.
- `@process`: Runs a function in a separate process, ideal for CPU-bound tasks to bypass the Global Interpreter Lock (GIL).

## Error Handling Decorators (`errors.py`)

This module contains decorators to elegantly handle exceptions and perform retries.

- `@suppress_errors`: Suppresses specified exceptions and optionally returns a predefined default value.
- `@retry`: Retries a function call with a specified delay between attempts if exceptions occur.

## Performance Measurement Decorators (`performance.py`)

Includes decorators for detailed monitoring of function execution, resource consumption, and call frequency.

- `@timeit`: Times the function execution and prints the duration in seconds.
- `@timeit_detailed`: Provides a detailed timing of function execution in milliseconds using `time.perf_counter`.
- `@resource_usage`: Monitors and reports the memory usage of the decorated function.
- `@cpu_timeit`: Measures the CPU time taken by the function, excluding any sleep time.
- `@cpu_timeit_detailed`: Similar to `@cpu_timeit` but provides time in detailed milliseconds.
- `@count_calls`: Counts and prints the number of times a function is called.

## Installation

To use these decorators, clone the repository and import the desired decorators into your Python project.

```sh
git clone https://github.com/JoshCap20/PythonDecoratorUtils.git
```

## Contributing
Contributions to enhance the utility and efficiency of these decorators are welcome. Please feel free to submit pull requests or raise issues to improve the functionality of PythonDecoratorUtils.

## License
This project is open-sourced and available under the MIT License.