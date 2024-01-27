import os
import random
# Using recursion to calculate factorials
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# Using recursion to generate a countdown timer
def countdown(number):
    print(number)
    if number == 0:
        return 0
    else:
        return countdown(number -1)

# test exercise
def print_every_other(low, high):
    if low > high:
        return

    print(low)
    print_every_other(low + 2, high)

# print_every_other(2,10)

def factorial(n):
    print(n)
    if n == 1:
        return n
    else:
        return n * factorial(n -2)

def sum (low, high):
    if high == low:
        return low
    else:
        print(f"/{high}/{low}/")
        return high + sum(low, high -1)

# print(sum(3,10))


test_array = [1,2,3,[4,5,6],7,[8,[9,10,11,[12,13,14]]],[15,16,17,18,19,[20,21,22,[23,24,25,[26,27,29]],30,31],32],33]

def print_nums(arr_test):
    for num in arr_test:
        if type(num) is int:
            print(f"{num} is a number")
            print(num)
        elif type(num) is list:
            print(f"{num} is a list")
            print(num)
            print_nums(num)

print_nums(test_array)



#
# # Just creating a set of folders and files to recursively traverse through
# def create_test_folder_structure():
#     parent_dir = "D:/python-learning/recursion-test"
#     dir_names = ["first","second", "third", "alice","bob", "fish", "porsche", "ferrari"]
#
#     for name in dir_names:
#         path = os.path.join(parent_dir,name)
#         os.mkdir(path)
#
#
# create_test_folder_structure()



