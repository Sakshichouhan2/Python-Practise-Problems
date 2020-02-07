#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount

salary = int(input("Enter your salary: "))
year = int(input("Enter your year of services: "))

if year > 5:
	print("Bonus is",.05 * salary)
else:
	print("No Bonus ")
