from math_tools import add, multiply, is_even, subtract, max_of_three, is_palindrome, find_min

def test_add():
    assert add (2,3) == 5
    assert add (-1,1) == 0
    assert add (0,0) == 0
    print("test_add : ALL PASSED")

def test_multiply():
    assert multiply (3,4) == 12
    assert multiply (-2,5) == -10
    assert multiply (0,100) == 0
    print("test_multiply : ALL PASSED")
    
def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even : ALL PASSED")

def test_subtract():
    assert subtract(4,0) == 4
    assert subtract(8,9) == -1
    assert subtract(0,0) == 0
    print("test_subtract : ALL PASSED")

def test_max_of_three():
    assert max_of_three(0,1,2) == 2
    assert max_of_three(5,6,8) == 8
    assert max_of_three(3,3,3) == "All these numbers are equal"
    assert max_of_three(2,2,5) == 5
    assert max_of_three(4,1,9) == 9
    print("test_max_of_three : ALL PASSED")

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("car") == False
    assert is_palindrome("i") == True
    assert is_palindrome("") == True
    print("test_is_palindrome : ALL PASSED")
def test_find_min():
    assert find_min([1,2,3,4]) == 1
    assert find_min([2,5,6,8]) == 2
    assert find_min([9,8,7,6]) == 6
    print("test_find_min : ALL PASSED")

test_add()
test_multiply()
test_is_even()
test_subtract()
test_max_of_three()
test_is_palindrome()
test_find_min()

print("--- All tests passed ---")
