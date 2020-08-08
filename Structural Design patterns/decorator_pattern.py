# Add the functionality directly to the class the object belongs to, if it makes sense
# Use composition
# Use inheritance - Composition should generally be preferred over inheritance, because inheritance
# makes code reuse harder, it's static, and applies to an entire class and all instances
# of it

# A Decorator pattern can add
# responsibilities to an object dynamically, and in a transparent manner (without
# affecting other objects)


# A Python decorator is a specific change to the syntax
# of Python that is used for extending the behavior of a class, method, or function
# without using inheritance. In terms of implementation, a Python decorator is a
# callable (function, method, class) that accepts a function object fin as input, and
# returns another function object fou

# Python decorators can actually do much more than the Decorator
# pattern. One of the things they can be used for, is to implement the Decorator pattern

# Another popular example of using the Decorator pattern is Graphical User
# Interface (GUI) toolkits. In a GUI toolkit, we want to be able to add features
# such as borders, shadows, colors, and scrolling to individual components/widgets

# Data validation
# Transaction processing
# Caching
# Logging
# Monitoring
# Debugging
# Business rules
# Compression
# Encryption

import functools


# Using Decorators:
def memoize(fn):
    known = dict()

    # Preserves Func. documentatation
    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer


# Normal Fibonacchi
def fibonacci(n):
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


# With memorization

known = {0: 0, 1: 1}


def fibonacci_memo(n):
    assert (n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


# With decorator
@memoize
def fibonacci_deco(n):
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    from timeit import Timer

    # t = Timer('fibonacci(8)', 'from __main__ import fibonacci')
    # print(t.timeit())
    t = Timer('fibonacci_memo(8)', 'from __main__ import fibonacci_memo')
    print(t.timeit())
    t = Timer('fibonacci_deco(8)', 'from __main__ import fibonacci_deco')
    print(t.timeit())
    t = Timer('memoize(fibonacci)(fibonacci(8))', 'from __main__ import fibonacci, memoize')
    print(t.timeit())
