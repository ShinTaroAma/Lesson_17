import time
from datetime import datetime


def time_decorator(function):
    now = datetime.now()

    def wrap(*args):
        function(*args)
        after = datetime.now()
        print(after - now)

    return wrap


@time_decorator
def say_hi(a, b):
    return a * b


say_hi(2, 4)


def counter(function):
    counter.count = 0

    def wrap(*args):
        counter.count += 1
        print(f"Number of times {function.__name__} has been called so far {counter.count}")

    return wrap


@counter
def multi(a, b):
    return a * b


multi(2, 2)
multi(2, 3)
multi(2, 4)


def logo(function):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    slash = " "

    def wrap(*args):
        function(*args)
        with open("file.text", "a") as my_file:
            my_file.write(current_time)
            my_file.write(slash)

    return wrap


@logo
def multi2(a, b):
    return a * b


multi2(4, 6)
multi2(5, 6)
multi2(6, 6)
multi2(4, 2)


def parm(function):
    a = 3
    b = 4

    def wrap(*args):
        function(a, b)
        print(function(a, b))

    return wrap


@parm
def multi3(a, b):
    return a * b


multi3(4, 5)
