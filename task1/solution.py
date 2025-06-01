import functools
import inspect


def strict(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        for new_arg, protofunc_arg in zip(args, sig.parameters.values()):
            if isinstance(new_arg, protofunc_arg.annotation):
                result = func(*args, **kwargs)
            else:
                raise TypeError
        return result
    return wrapper
