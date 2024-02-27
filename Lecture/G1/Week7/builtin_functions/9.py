# Built-in functions

# all()
# any()

list1 = [True, True, True] 
list2 = [True, False, True] 

print("all:", all(list1), all(list2))
print("any:", any(list1), any(list2))

nums = [2, 4, 6, 8, 9]

is_even = lambda x : x % 2 == 0

print("All elements are even:", all(map(is_even, nums)))
print("At least one element is even:", any(map(is_even, nums)))

   