#Take values of length and breadth of a rectangle from user and check if it is square or not. 

lenght = int(input("Enter the lenght of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))

if lenght == breadth:
	print("yes it is an square")
else:
	print("No its an rectangle")