# PROBLEM DESCRIPTION:
# Due to a bug in a trading problem, the digits of the decimal systems got shuffled. For instance, 
# each 0 changed to 2, each 1 changed to 3, and each 2 got changed to 0. If the correct number is 
# "021", the system shows "203".
# 
# Given the numbers that the program needs to sort and the mapping, i.e., the shuffled version of 
# the decimal digits, return a list of the jumbled numbers sorted by their correct decimal values,
# ascending. If multiple mapped values are equal, the values returned should be in the original 
# order they were presented.
# 
# For example, mapping=[3,5,4,6,2,8,9,0,1] of fixed length of m=10 and the another array of number 
# strings, nums=['990','332','32'] of length n=3
# 
# Mapping of '990' is '668'
# Mapping of '332' is '004'
# Mapping of '32' is '04'
# 
# Ordering by integer values yields [4,4,668], and retaining order for '332' and '32' results in a
# return array of associated original values: ['332', '32', '990']

def strange_sort(mapping, nums):
    pos_dict = {num:index for index, num in enumerate(mapping)}

    nums_list = list()
    for num in nums:
        num_str = ""
        for digit in num:
            num_str += str(pos_dict[int(digit)])
        
        nums_list.append([int(num), int(num_str)])

    nums_list.sort(key = lambda x: x[1])

    return [num[0] for num in nums_list]

print(strange_sort([3,5,4,6,2,8,9,0,1], ['990','332','32']))
print(strange_sort([3,5,4,6,2,8,9,0,1], ['990','333332','32','332','32']))