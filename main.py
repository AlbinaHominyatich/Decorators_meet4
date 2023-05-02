#теорія декоратори
#приклад порівняння та синтаксису
def my_decorator(func):
    def wrapper():
        print("та щось")
        func()
        print("та це тоже")
    return  wrapper
def say_hello():
    print("Hello!")
#туточки огортаємося
say_hello = my_decorator(say_hello)
say_hello()
