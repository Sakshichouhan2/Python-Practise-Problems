#Take two int values from user and print greatest among them.

'''Number1 = int(input("Enter first Number")) 
Number2 = int(input("Enter second Number"))


if Number1 > Number2 > Number3:
	print("Number {} is greatest".format(Number1))
else:
	print("Number {} is greatest".format(Number2))'''


#Greatest of three number 
Number1 = int(input("Enter first Number ")) 
Number2 = int(input("Enter second Number "))
Number3 = int(input("Enter three Number "))

if (Number1 >= Number2) and (Number1 >= Number3):
      largest = Number1
elif (Number2 >= Number1) and (Number2 >= Number3):
    largest = Number2
else:
    largest = Number3
print("The largest number is", largest)



