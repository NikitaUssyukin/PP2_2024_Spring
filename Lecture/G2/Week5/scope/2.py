x = 200

def myfunc():
    x = 300
    def innerfunc():
        print(x)
    innerfunc()

print(x)
myfunc()