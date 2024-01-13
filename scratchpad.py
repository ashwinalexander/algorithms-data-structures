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

def get_intersection(arr_one, arr_two):
    arr_intersection = []
    counter = 0
    for i in range (len(arr_one)):
        counter += 1
        for j in range (len(arr_two)):
            counter += 1
            if arr_one[i] == arr_two[j]:
                arr_intersection.append(arr_one[i])
                break;
    print(counter)
    return arr_intersection

def twoSum(array):
    counter = 0
    for i in range(len(array)):
        counter += 1
        for j in range(len(array)):
            counter += 1
            if i != j and array[i] + array[j] == 10:
                print(counter)
                return True
    print(counter)
    return False
def containsX(str_input):
    for i in range(len(str_input)):
        if str_input[i] == 'X':
            return True

    return False

print(containsX("BLAHX"))

# arr_test = [1,2,3,2,4,6]
# print(twoSum(arr_test))

# array_first = [1,2,3,4,5]
# array_second = [5,6,13,4,10,12,13]
# print(get_intersection(array_first, array_second))
# example_array = [1,2,34,8,44,55,24,43]
# print(get_largest_val(example_array))
# # print(has_duplicate_values(example_array))
# print(has_duplicate_values_v2(example_array))

