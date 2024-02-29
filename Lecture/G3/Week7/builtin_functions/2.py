# built-in functions

# map()

nums = [1, 2, 3, 4, 5]

map_obj = map(str, nums)

print(next(map_obj))

print(', '.join(map(str, nums))) # join() expects elements of the list to be str, not int