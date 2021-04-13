def my_decorator(func):
    """
    Simple Decorator
    """

    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


say_whee()


def do_twice(func):
    """
    Decorator with arguments
    """

    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")


greet('hi')
