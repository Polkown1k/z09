from datetime import datetime

def timer(func):
    def decor():
        before = datetime.now()
        func()
        after = datetime.now()
        print(after-before)
    return decor

@timer
def some_function():
    for i in range(100):
        print(i)

some_function()


    