# Fibonacci sequence with dynamic programming -
# Dynamic programming is when we optimize recursive algorithms that have overlapping subproblems

def fib(n,memo):
    if n == 1 or n == 0:
        return 1
    if n not in memo:
        print(f"calculating for {n}")
        memo[n] = fib(n-1, memo) + fib(n-2,memo)
    return memo[n]

# Chapter 12 exercises
def add_until_100(array):
    if len(array) == 0:
        return 0
    blah = add_until_100(array[1:len(array)-1])
    if array[0] + blah > 100:
         return blah
    else:
        return array[0] + blah

# print(add_until_100([1,2,3,4,5,6,100,400]))

# Golomb Sequence - with memoization
def golomb(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    memo[n] = 1 + golomb(n - golomb(golomb(n-1, memo), memo), memo)
    return memo[n]

# Unique Paths - improve efficiency
# Worked out that tuples can be keys in dictionaries - how cool !
def unique_paths(rows, columns, memo):
    if rows == 1 or columns == 1:
        return 1
    if (rows,columns) not in memo:
        memo[(rows, columns)] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
    return memo[(rows, columns)]

print(unique_paths(3,7,{}))

# Testing out tuples in dictionaries
# def test(m,n):
#     dict_blah = {
#         (1,2): 100,
#         (2,3): 200,
#         (3,4): 300}
#
#     if (m,n) in dict_blah:
#         print(dict_blah[(m,n)])
#         return "it's there"
#     else:
#         dict_blah[(m,n)] = n * 100
#         print(dict_blah)
#         return "npe"
#
#
# print(test(2,3))