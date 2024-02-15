def ispalindrome(num):
    temp = str(num)
    return temp == temp[::-1]

def palindrome_gen(start, stop):
    while start < stop:
        if ispalindrome(start):
            yield start
        start += 1

square_nums = list(palindrome_gen(1, 1000))

print(square_nums)