def my_map(myfunc, mylist):
    for element in mylist:
        print(myfunc(element))

square = lambda a : a ** 2

nums = [1, 2, 3, 4, 5]

my_map(square, nums)