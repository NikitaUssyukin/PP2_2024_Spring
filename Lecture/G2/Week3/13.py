# Lambda functions
def ourmap(func, arr):
    result = []

    for element in arr:
        result.append(func(element))

    return result

nums = [1, 2, 3, 4, 5]

print(ourmap(lambda a : a ** 2, nums))