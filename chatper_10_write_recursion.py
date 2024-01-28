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

def string_reversal(test_string):
    if len(test_string) ==1:
        return test_string[0]
    return test_string[len(test_string)-1] + string_reversal(test_string[0:len(test_string)-1])

print(string_reversal("abcd"))
