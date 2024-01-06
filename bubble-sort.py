def bubble_sort(array_to_sort):
    ''' Testing out an algorithm in Jay Wengrow's book It is known to be inefficient O(n^2) but
         let's try it out anyway
         As the array size increases, more comparisons and swaps have to be completed'''
    sort_until_index = len(array_to_sort) - 1

    while sort_until_index > 0:
        for i in range(sort_until_index):
            print("entering")
            if array_to_sort[i] > array_to_sort[i+1]:
                array_to_sort[i], array_to_sort[i+1] = array_to_sort[i+1], array_to_sort[i]
        sort_until_index -= 1
    return array_to_sort

unsorted_array = [1, 20, 3, 44, 76, 2, 69,424,22]
print(bubble_sort(unsorted_array))