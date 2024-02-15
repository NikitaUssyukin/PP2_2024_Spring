def ispalindrome(num):
    if num // 10 == 0:
        return True
    temp = num
    r_num = 0
    while temp != 0:
        r_num = r_num * 10 + temp % 10
        temp = temp // 10
    if r_num == num:
        return True
    return False

def palindrome_gen(start, stop):
    while start < stop:
        if ispalindrome(start):
            yield start
        start += 1

square_nums = list(palindrome_gen(1, 1000))

print(square_nums)