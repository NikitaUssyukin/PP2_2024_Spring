def my_map(myfunc, mylist):
    result = []
    for element in mylist:
        result.append(myfunc(element))
    
    return result

nums = [1, 2, 3, 4, 5]

squared_nums = my_map(lambda a : a ** 2, nums)

print(squared_nums)