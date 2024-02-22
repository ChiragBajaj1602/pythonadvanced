import random
def func():
    for i in range(6):
        yield random.randint(1,40)

    yield random.randint(1,15)

for random_number in func():
    print("And the next number is ... %d"%random_number)
a = 1
b = 2
a, b = b, a
print(a, b)
# excercise
def fib():
    a=0
    b=1
    for i in range(10):
        a,b=b,a+b
        yield a

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
