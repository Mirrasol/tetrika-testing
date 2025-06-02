import functools
import inspect


def strict(func):
    """A decorator to check if function's arguments are
    in accordance with their annotations.
    """
    @functools.wraps(func)
    def wrapper(*args):
        sig = inspect.signature(func)
        for new_arg, protofunc_arg in zip(args, sig.parameters.values()):
            if isinstance(new_arg, protofunc_arg.annotation):
                continue
            else:
                if protofunc_arg.annotation == 'inspect._empty':
                    raise TypeError(f'No annotation provided for argument {new_arg}')
                raise TypeError(f'Argument {new_arg}: wrong type, expected type {protofunc_arg.annotation}')
        result = func(*args)
        return result
    return wrapper
