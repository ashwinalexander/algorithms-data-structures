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
# Efficiency: O(N)
def get_intersection(arr_one, arr_two):
    larger_array = []
    smaller_array = []
    # dictionary to contain the larger array values and True for the value
    dicty = {}
    arr_intersection = []

    # now add all the values in the larger array
    for num in arr_one:
        dicty.update({num: True})

    for other_num in arr_two:
        if dicty.get(other_num):
            arr_intersection.append(other_num)

    return arr_intersection


# print(get_intersection([1,2,3,4,10,11,12,14],[1,2,3,4,5,6,7,8,9,10,11,12,14]))
# Efficiency: O(N) using a hashtable
def find_first_duplicate(arr_test):
    # This is the hashtable
    dict = {}
    for element in arr_test:
        # before adding to the hashtable check if it already exists
        if dict.get(element):
            return element
        dict.update({element: True})

# print(find_first_duplicate(["a","b","c","b","e","c","f"]))

def find_missing_alphabet(arr_test):
    # alphabet = {"a": True, "b": True, "c": True, "d": True, "e": True, "f": True, "g": True, "h": True, "i": True, "j": True, "k": True, "l": True, "m": True, "n": True, "o": True, "p": True,"q": True, "r": True, "s": True, "t": True, "u": True, "v": True, "w": True, "x": True, "y": True, "z": True}
    arr_test = arr_test.replace(" ","")
    alphabet_hashtable = {}
    for letter in arr_test:
        alphabet_hashtable.update({letter: True})

    alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for alphabet in alphabet_list:
        if not alphabet_hashtable.get(alphabet):
            return alphabet

# print(find_missing_alphabet("the quick brown fof jumps over a lazy dog"))

# This was a little mind-bending but I finally figured out an O(N) solution for it  woot!
def first_non_duplicate(arr_test):
    letter_count_hashtable = {}
    arr_test_backup = arr_test
    for letter in arr_test:
        if letter_count_hashtable.get(letter):
            arr_test_backup = arr_test_backup.replace(letter,"")
        else:
            letter_count_hashtable.update({letter:True})
    print(arr_test_backup)
    return arr_test_backup[0]



print(first_non_duplicate("aabbcddeefc"))