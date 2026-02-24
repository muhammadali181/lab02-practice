def add(a,b):
    return a + b
def multiply(a,b):
    return a*b
def is_even(n):
    return n%2 == 0
def subtract(a,b):
    return a - b
def max_of_three(a,b,c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    elif a==b==c:
        return "All these numbers are equal"
    else:
        return c
def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s == s[::-1]:
        return True
    return False
def find_min(numbers):
    min_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]
    return min_val
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result