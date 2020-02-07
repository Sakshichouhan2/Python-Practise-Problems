'''A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.'''

classes_held = int(input("Enter the number of classes held: ")) 

classes_attended = int(input("Enter the number of classes attend: "))

Attended = (classes_attended/float(classes_held))*100
print("Attendence is",classes_attended)
if Attended >= 75:
 	print("You are allowed to sit in exam")
else:
	print("Sorry, you are not allowed. Attend the exam.")