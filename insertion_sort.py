def insertion_sort(arr_to_sort):
    '''Testing out the insertion sort algorithm
    1. '''
    for i in range(1,len(arr_to_sort)):
        temp_val = arr_to_sort[i]
        position = i - 1

        while position >= 0:
           if arr_to_sort[position] > temp_val:
               arr_to_sort[position+1] = arr_to_sort[position]
               position = position - 1
           else:
               break
           arr_to_sort[position + 1] = temp_val
    return arr_to_sort

arr_example = [5,4,2,3]
print(insertion_sort(arr_example))


