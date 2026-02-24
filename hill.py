import random

def f(x):
    return -x*x+4*x


def hill_climb():
    x=random.uniform(-10,10)
    step=0.1

    while True:
        if f(x + step) > f(x):
            x = x + step
        elif f(x - step) >f(x):
            x = x - step
        else:
            break

    return x,f(x)

x,val = hill_climb()
print("Best solution",x)
print("Maximum value",val)