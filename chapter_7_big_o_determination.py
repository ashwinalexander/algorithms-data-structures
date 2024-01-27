
# Average of Even Numbers
# Efficiency = O(N)
def average_of_even_numbers(array):
    sum = 0
    count_even_numbers = 0

    for number in array:
        if number % 2 == 0:
            sum += number
            count_even_numbers += 1
    return sum/count_even_numbers
#
# sample_array = [24,48,72,96, 120]
# print(average_of_even_numbers(sample_array))

# Word Builder
# Efficiency = O(N^2)
def word_builder(array):
    collection = []
    for element in array:
        for other_element in array:
            if element != other_element:
                collection.append(element + other_element)
    return collection

# print(word_builder(["a","b","c","d"]))


# Array Sample
# Efficiency = O(1)
def array_sample(arr_test):
    first = arr_test[0]
    middle = arr_test[int(len(arr_test)/2)]
    last = arr_test[-1]

    return [first,middle,last]

# print(array_sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))



# Average Celsius Reading
# Efficiency: 0(N)
def average_celsius(fahrenheit_readings):
    celsius_numbers = []

    for f_reading in fahrenheit_readings:
        cel_conversion = (f_reading - 32)/1.8
        celsius_numbers.append(cel_conversion)

    sum = 0

    for c_reading in celsius_numbers:
        sum += c_reading

    return sum/len(celsius_numbers)

# print(average_celsius([-40,-40,-40,-40,-40]))

# Clothing Labels
# Efficiency: 0(N)
def mark_inventory(clothing_items):
    clothing_options = []

    for item in clothing_items:
        for size in range(1,6):
            clothing_options.append(item + " size:" + str(size))

    return clothing_options

# print(mark_inventory(["Shirt", "Hat",'Pants']))

# Count the Ones
# Efficiency: O(N)
# This was a tricky one to comprehend. I, initially jumped to the conclusion that this was O(N^2) seeing a nested loop
def count_ones(outer_array):
    count = 0
    for inner_array in outer_array:
        for number in inner_array:
            if number == 1:
                count += 1
    return count


# print(count_ones([[0,1,1,1,0],[0,1,1,1,0,1,1,1],[1,1,1,1,0,0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0]]))

# Palindrome Checker
# Efficiency: O(N)
def pal_checker(string):
    leftIndex = 0
    rightIndex = len(string) - 1

    while leftIndex < len(string)/2:
        if string[leftIndex] != string[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -=1

    return True
# print(pal_checker("kayak"))


# Get All Products
# Efficiency: O(N^2)
def get_all_products(array):
    arr_product = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            arr_product.append(array[i]*array[j])
    return arr_product
# print(get_all_products([1,2,3,4,5]))

# Get All Products
# Efficiency: O(N^2)
def get_two_products(arr_one, arr_two):
    arr_product = []
    for i in range(len(arr_one)):
        for j in range(len(arr_two)):
            arr_product.append(arr_one[i]*arr_two[j])
    return arr_product
# print(get_two_products([1,2,3],[10,100,1000]))








