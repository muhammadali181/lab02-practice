def remove_negatives(numbers):
    result = []
    for num in numbers:
        if num >= 0:
            result.append(num)
    return result
print(remove_negatives([1, -2, -3, 4, -5]))