a = "nice"

def myfunc():
    print("KBTU is", a)

def myfunc2(b):
    print(b, "is", a)

def myfunc3(b) -> str:
    return(b + " is " + a)

myfunc()
myfunc2("Almaty")
print(myfunc3("Earth"))

