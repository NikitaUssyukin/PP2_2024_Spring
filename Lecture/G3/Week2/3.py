x = "great"

def func1():
    print("KBTU is", x)

def func2():
    global x
    x = "awesome"
    print("KBTU is", x)

func1()
func2()
func1()
