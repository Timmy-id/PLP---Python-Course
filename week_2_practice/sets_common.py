set_A = set([int(num) for num in input('Enter numbers separated by a space for set A ').split()])
set_B = set([int(num) for num in input('Enter numbers separated by a space for set B ').split()])

set_intersection = set_A & set_B

print(set_intersection)