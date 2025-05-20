# 5-11 Ordinal numbers 
# Ordinal numbers indicate their position in a list
# such as 1st or 2nd.

# Store th number 1-9 in a list
num_list = [i for i in range (1, 10)]
#loop through the list
# use if-elif-else chain inside the loop to print
# the proper ordinal number. Numbers 1 2 and 3
# end in 'st', 'nd', or 'rd' respectively
for num in num_list:
    if num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num ==3:
        print(str(num) + 'rd')
    else:
        print(str(num) + 'th')