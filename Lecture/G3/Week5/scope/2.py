x = 200

def myfunc():
    global x
    x = 300
    print(x)

myfunc()
print(x)