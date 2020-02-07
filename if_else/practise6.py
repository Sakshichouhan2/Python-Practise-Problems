#Take input of age of 3 people by user and determine oldest and youngest among them. 
Age1 = int(input("Enter First User Age: "))
Age2 = int(input("Enter Second User Age: "))
Age3 = int(input("Enter Three User Age: "))
if Age1>=Age2:
	print("Age1 is youngest" )
elif Age1>=Age3:
	print("Age1 is youngest" )
elif Age2>=Age1:
	print("Age2 is youngest" )
elif Age2>=Age3:
	print("Age2 is youngest" )
elif Age3>=Age1:
	print("Age3 is youngest" )
elif Age3>=Age2:
	print("Age3 is youngest" )
else:
	print("Invalid Entry: ")