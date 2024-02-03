# double every element of an array
def double_array_loop(array):
    new_array = []
    for num in array:
        new_array.append(num*2)
    return new_array

# double every element of an array in-place using re-cursion
def double_array(array_blah, idx=0):
    if idx < len(array_blah):
        array_blah[idx] *= 2
        return double_array(array_blah, idx + 1)
    else:
        return array_blah

# print(double_array([1,2,3,4,5]))

def factorial_loop(n):
    product = 1
    for num in range(1,n):
        product *= num
    return product

# Calculate the factorial recursively
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

# print(factorial(10))

def sum_nums_in_array_loop(array):
    sum =0
    for num in array:
        sum += num
    return sum

# Calculate the sum of an array recursively
def sum_array(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:len(array)])

# print(sum_array([1,2,3,4,5]))

#
# def test(array):
#     print(array[0: len(array) -1])


def string_reversal_loop(test_string):
    for num in range(len(test_string)-1,-1,-1):
        print(test_string[num])

# string_reversal_loop("blah")

# Use recursion to reverse a string
def string_reversal(test_string):
    if len(test_string) ==1:
        return test_string[0]
    return test_string[len(test_string)-1] + string_reversal(test_string[0:len(test_string)-1])

# print(string_reversal("abcd"))

# count x's in a string using recursion
def count_x_loop(test_string):
    count = 0
    for let in test_string:
        if let == "x":
            count +=1
    return count

def count_x(test_string):
 if len(test_string) == 0:
     return 0

 if test_string[0] == "x":
     return 1 + count_x(test_string[1: len(test_string)])
 else:
     return 0 + count_x(test_string[1: len(test_string)])

# print(count_x("xasdhbhbhxbx"))


# Solving the staircase problem using recursion
# For n steps, how many pathways exist if someone can take 1, 2 or 3 steps at a time
# I don't claim to understand fully how this works, it hurts my brain
def staircase_problem(n):
    print(n)
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1

    return staircase_problem(n-1) + staircase_problem(n-2) + staircase_problem(n-3)


# print(staircase_problem(19))
#
# # Create all possible anagrams using the characters in the input string
# def generate_anagram(anagram_fodder):
#     return



# Exercise 1:
def total_chars(arr_words):
    if len(arr_words) == 0:
        return 0
    return len(arr_words[0]) + total_chars(arr_words[1:len(arr_words)])


# print(total_chars(["av","c","d","dejee"]))

# Exercise 2:
def only_even_nums(arr_odd_even):
   if len(arr_odd_even) == 0:
       return []
   if arr_odd_even[0] % 2 == 0:
       return [arr_odd_even[0]] + only_even_nums(arr_odd_even[1:len(arr_odd_even)])
   else:
       return only_even_nums(arr_odd_even[1:len(arr_odd_even)])


def triangular_nums(num_tri):
    '''Generate the triangular number'''
    '''Wow, this was easy'''
    if num_tri == 0:
        return 0
    return num_tri + triangular_nums(num_tri-1)


