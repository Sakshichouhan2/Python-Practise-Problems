#Write a Python program to get the number of occurrences of a specified element in an array.
from array import*
array_num = array('d', [1.9, 3, 5.8, 7.3, 7.1, 9.9, 3, 3, 1.9, 1.9])
print("Original array: "+str(array_num))
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))