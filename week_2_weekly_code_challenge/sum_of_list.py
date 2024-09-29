from functools import reduce

nums = input('Enter numbers ')
nums_list = []
for num in nums:
    nums_list.append(int(num))

nums_sum = reduce(lambda a, b: a + b, nums_list)
print("The sum of the numbers in the list is", nums_sum)