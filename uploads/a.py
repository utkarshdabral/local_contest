def sum_of_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

nums = [1, 2, 3, 4, 5]
print("Sum:", sum_of_list(nums))
