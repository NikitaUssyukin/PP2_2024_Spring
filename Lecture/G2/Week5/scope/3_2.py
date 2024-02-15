def myfunc():
    global x
    x = 300
    def innerfunc():
        print(x)
    innerfunc()

print(x)
myfunc()


