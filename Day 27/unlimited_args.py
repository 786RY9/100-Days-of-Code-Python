
# positional args
def add(*args): # *args is a tuple of inputs
    sum = 0
    print(args[1])
    for n in args:
        sum+=n
    return sum

# print(add(1,2,3,4,5,5,64,3,9,8))


# named arguments: **kwargs
def calculate(n,**kwargs): # kwargs = key word arguments
    print(kwargs) # dictionary
    # for (key,value) in kwargs.items():
    #     print(key)
    #     print(value)
    n+=kwargs['add']
    n*=kwargs['multiply']
    print(n)

# calculate(2,add=3,multiply=5)


class Car:
    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')
        self.power = kw.get('power')

my_car = Car(make='Toyota',model='Revo',power='1000')

print(my_car.make)
print(my_car.model)
print(my_car.power)