username = "chaiorcode"

def test():
    pass

if True:
    pass

def func():
    #username = "chai"
    print(username)
    
print(username)
func()

x = 99

# def func2(y):
#     z = x+y
#     return z

# result = func2(1)

# print(result)


# def func3():
#     global x
#     x = 12
#* avoid this
# func3()
# print(x)



def f1():
    x = 88
    def f2():
        print(x)
    return f2

myResult = f1()
myResult()

#*back pack dafination tar related sob data nia jay tar sata dia store hoy this is closer

def chaicode(num):
    def actual(x):
        return x ** num
    return actual

f = chaicode(2)
g = chaicode(3)

print(f(3))
print(g(3))