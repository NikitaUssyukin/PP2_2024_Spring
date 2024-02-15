x = 200

def myfunc():
    y = 300
    def innerfunc():
        print(y)
    innerfunc()

print(x)
# print(y)
# innerfunc()
myfunc()