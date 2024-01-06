def has_duplicate_values(array_to_check):
    '''Efficiency = o(n^2)'''
    count = 0
    for i in range(len(array_to_check)):
        for j in range(len(array_to_check)):
            count += 1
            print(count)
            if array_to_check[i] == array_to_check[j] and i != j:
                return True
    return False

def has_duplicate_values_v2(array_to_check):
    ''' Pretty clever way to check for duplicates without a nested for loop. This will only work for numbers. Efficiency = o(n)'''
    tracker_array = []
    for i in range(len(array_to_check)):
        print(i)
        if tracker_array[array_to_check[i]] == 9:
            return True
        else:
            tracker_array[array_to_check[i]] = 9
    return False


def get_largest_val(array):
    highest_val = 0
    for i in range(len(array)):
        if array[i] > highest_val:
            highest_val = array[i]
    return highest_val





example_array = [1,2,34,8,44,55,24,43]
print(get_largest_val(example_array))
# # print(has_duplicate_values(example_array))
# print(has_duplicate_values_v2(example_array))

