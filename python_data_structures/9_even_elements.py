#!C:\Users\korch\AppData\Local\Programs\Python\Python312
my_list = [5, 4, 3, 2, 1]
new_list = []
for element in my_list:
    if element % 2 == 0:
        new_list.append(True)
    else:
        new_list.append(False)
my_tuple = tuple(new_list)
print(my_list)
print(my_tuple)
