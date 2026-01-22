# create two list and compare those list with is and ==

first_list = [1, 2, 5, 6, 7, 8]
second_list = [1, 2, 5, 6, 7, 8]
third_list = first_list

# here we are checking memory location  of lists
print(first_list is second_list)
# here we are compare values of two list of lists
print(first_list == second_list)

# here we are checking memory lcation of lists
print(third_list is first_list)
# here we are compare values of two list of lists
print(third_list == second_list)
