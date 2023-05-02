#теорія декоратори

def myWrapper(func):#3
    def myInnerFunc(): #4
        print("Inside wrapper")
        func()#5
    return myInnerFunc

@myWrapper #2
def myFunc(): #6 це і є func()
    print('Hello world!')
myFunc() #1