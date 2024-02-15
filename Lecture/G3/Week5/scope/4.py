x = 300

def myfunc():
    x = 200
    def innerfunc():
        print(x)
    innerfunc()

myfunc()
print(x)