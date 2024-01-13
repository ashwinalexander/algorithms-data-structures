def selection_sort(unsorted_array):
    ''' This will be more efficient than the Bubble Sort.
    And yet, it will have the same efficiency of O(n^2)
    demonstrating that Big O notation is best used when comparing algorithms orders of efficiency
    / skyscraper vs single-family home analogy '''
    # pseudo-code:
    # Make multiple passes, so this means a for loop for the length of the array
    # On each pass, track the index of the lowest value
    # By the end of the pass, swap the value at the index of the lowest value with the index that has not yet been swapped
    # Repeat until the end of the array

    for i in range(len(unsorted_array)):
        index_of_lowest_value = i
        for j in range(len(unsorted_array)):
            if unsorted_array[index_of_lowest_value] < unsorted_array[j]:
                index_of_lowest_value = j
            unsorted_array[i], unsorted_array[index_of_lowest_value] = unsorted_array[index_of_lowest_value], unsorted_array[i]
    return unsorted_array

array_to_sort = [23 ,6 ,8, 4,8,4,6,1,46,23]
print(selection_sort(array_to_sort))