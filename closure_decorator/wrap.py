from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print 'Called example function'

wrap = my_decroator(example)
wrap()
print wrap.__name__

#example = my_decorator(example)
#example()

example()

print example.__name__
