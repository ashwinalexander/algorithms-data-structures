
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

# print(mark_inventory(["Shirt", "Hat",'Hatas']))

