def myfunc(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} -> {value}")
    


myfunc(fname = "Linus", lname = "Torvalds")