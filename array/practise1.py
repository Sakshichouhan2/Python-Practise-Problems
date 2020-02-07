# Python program to count positive and negative numbers in a List 
list = [12,34,-8,4,-56,47,-6,41,6,-6]

positive_count, negative_count = 0,0

for num in list:
	if num >=0:
		positive_count += 1
	else:	
		negative_count += 1

	print("Positive numbers in the list: ", positive_count) 
	print("Negative numbers in the list: ", negative_count) 