# PROBLEM DESCRIPTION:
# Given an array arr[] of integers, find out the maximum difference between any two elements such 
# that larger element appears after the smaller number.
# GeeksForGeeks link: https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

def max_difference(arr):
    min_arr = arr.copy()
    for i in range(1, len(arr)):
        min_arr[i] = min(arr[i], arr[i-1])

    max_arr = arr.copy()
    for i in range(len(arr)-2, -1, -1):
        max_arr[i] = max(max_arr[i], max_arr[i+1])

    diff_arr = [max_arr[i]-min_arr[i] for i in range(len(arr))]

    return max(diff_arr)

print(max_difference([1,2,3,4,5]))
print(max_difference([7,9,5,6,3,2]))
print(max_difference([2,3,10,6,4,8,1]))
print(max_difference([5,4,3,2,1]))