# testing out the binary search algorithm
def binary_search(ordered_array, val):
    '''Establish lower and upper bounds
    Loop through as long as the lower bounds are lower than the upper bound
    Find the midpoint and see if the search value is at it, lower than it, or higher
    If at it, return the midpoint index,
    If lower, set the upperbound to the current midpoint index
    If higher, set the lowerbound to the current midpoint index'''
    lower_bound = 0
    upper_bound = len(ordered_array) - 1

    while lower_bound < upper_bound:
        print("looping again")
        print("current lower bound",lower_bound)
        print("current upper bound", upper_bound)
        mid_bound = round((lower_bound + upper_bound) / 2)
        print("mid bound",mid_bound)

        if val == ordered_array[mid_bound]:
            print("search val is at mid point. jackpot!")
            return mid_bound
        elif val <= ordered_array[mid_bound]:
            print("search val is less than the midpoint in the array")
            print("changing upper bound to midpoint")
            upper_bound = mid_bound
        elif val > ordered_array[mid_bound]:
            print("search val is higher than the midpoint in the array")
            print("changing lower bound to midpoint")
            lower_bound = mid_bound
    return null

array_to_search = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
search_val = 19
idx = binary_search(array_to_search,search_val)
print("this is the final result")
print(idx)



