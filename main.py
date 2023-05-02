#теорія декоратори
#приклад порівняння та синтаксису
def my_decorator(func):
    def wrapper():
        print("та щось")
        func()
        print("та це тоже")
    return  wrapper
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
