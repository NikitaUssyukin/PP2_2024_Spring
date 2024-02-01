# Lambda functions
def ourmap(func, arr):
    for element in arr:
        print(func(element))

nums = [1, 2, 3, 4, 5]

ourmap(lambda a : a ** 2, nums)