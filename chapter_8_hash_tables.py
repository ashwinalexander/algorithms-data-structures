# Find if an array is a subset of another array
def is_array_subset(arr_one, arr_two):
    larger_array = []
    smaller_array = []
    # dictionary to contain the larger array values and True for the value
    dicty = {}

    # Determine which is the larger array - we will add this to the dictionary
    if len(arr_one) > len(arr_two):
        larger_array = arr_one
        smaller_array = arr_two
    else:
        larger_array = arr_two
        smaller_array = arr_one

    # now add all the values in the larger array
    for num in larger_array:
        dicty.update({num: True})

    for other_num in smaller_array:
        if not dicty.get(other_num):
            return False
    return True

# print(is_array_subset([1,2,3,4,10,11],[1,2,3,4,5,6,7,8,9,10,11]))

# function to return the intersection of two arrays
def get_intersection(arr_one, arr_two):
    larger_array = []
    smaller_array = []
    # dictionary to contain the larger array values and True for the value
    dicty = {}
    arr_intersection = []

    # Determine which is the larger array - we will add this to the dictionary
    if len(arr_one) > len(arr_two):
        larger_array = arr_one
        smaller_array = arr_two
    else:
        larger_array = arr_two
        smaller_array = arr_one

    # now add all the values in the larger array
    for num in larger_array:
        dicty.update({num: True})

    for other_num in smaller_array:
        if dicty.get(other_num):
            arr_intersection.append(other_num)

    return arr_intersection


print(get_intersection([1,2,3,4,10,11,12,14],[1,2,3,4,5,6,7,8,9,10,11,12,14]))
