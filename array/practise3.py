#Write a Python program to reverse the order of the items in the array
from array import*
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
array_num.reverse()
print(array_num)