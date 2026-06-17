def highest_even(lst):
    '''Returns the highest even number in the list. If there are no even numbers, returns None.'''
    highest = None
    for num in lst:
        if num % 2 == 0:
            if highest is None or num > highest:
                highest = num
    return highest

print(highest_even([1, 2, 3, 4, 5, 6,8,10])) # should return 6
print(highest_even([1, 3, 5, 7])) # should return None
print(highest_even([2, 4, 6, 8])) # should return 8
print(highest_even([-2, -4, -6, -8])) # should return -2
