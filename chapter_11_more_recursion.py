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


def scotland_yard(str_x):
    ''''return the location/index of "x" in the string. This is just like Scotland Yard'''
    if str_x[0] != "x":
        return 1 + scotland_yard(str_x[1:])
    else:
        return 0

# print(scotland_yard("abcdefghijklmnopqrstuvwxyz"))

def unique_paths(row_count,col_count):
    '''Unique Path Problem - return all possible paths from the top left to the bottom right
    of a grid with row_count rows and col_count columns'''
    print("hi")
    # ngl this was a bit of a mind-bender, I was not expecting two recursions but that makes sense.
    if row_count == 1 or col_count == 1:
        return 1
    return unique_paths(row_count-1, col_count) + unique_paths(row_count, col_count-1)

print(unique_paths(3,7))




