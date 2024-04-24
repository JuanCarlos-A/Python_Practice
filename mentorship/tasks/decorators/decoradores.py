import time
import functools

def decorator_func(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        tiempo_inicio = time.perf_counter()
        value = func(*args, **kwargs)
        tiempo_fin = time.perf_counter()
        tiempo_ejec = tiempo_inicio - tiempo_fin
        print(f'Finished {func.__name__}() in {tiempo_ejec:.4f} secs')

        return value
    return inner_func