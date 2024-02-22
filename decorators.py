import time
def checktime(func):
    def wrapper():
        t1=time.time()
        func()
        t2=time.time()-t1
        print(f'{func.__name__} The time is {t2}')
    return wrapper

@checktime
def func1():
    print("Hello World")
    time.sleep(3)
@checktime
def func2():
    print("Chirag is great")
    time.sleep(3)
func1()
func2()