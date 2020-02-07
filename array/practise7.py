#Write a Python program to remove the first occurrence of a specified element from an array. 
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3, 56, 67,78,98])
print("Original array: "+str(array_num))
array_num.remove(5)
print("New array: "+str(array_num))