#Write a Python program to append, remove a new item to the end of the array.
from array import *
array_num = array('I', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
array_num.append(11)
array_num.remove(1)
print("New array: "+str(array_num))



