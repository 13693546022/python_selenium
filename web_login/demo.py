def decorator_a(func):
    print ('Get in decorator_a')
    def inner_a(*args,**kwargs):
        print ('Get in inner_a')
        return func(*args,**kwargs)
    return inner_a

def decorator_b(func):
    print ('Get in decorator_b')
    def inner_b(*args,**kwargs):
        print ('Get in inner_b')
        return func(*args,**kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print ('Get in f')
    return x*2
f(1)

mydict={'a':1,'b':2}
def func(d):
    d['a']=0
    return d

func(mydict)
mydict['c']=2
print(mydict)