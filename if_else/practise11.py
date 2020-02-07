''' Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and 
then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.'''

Age = int(input("Enter the age of employee: "))
Gender = input("Enter the gender of employee: ")
Marital_Status = input("Enter 'Y' or 'N': ")
# Y for Yes
# N for No

if Gender = "female"
	print("she will work only in urban areas.")
elif Gender = "male" and age>=20 and age<=40
	print("he will work in anywhere: ")
elif Gender ="male" and age>=40 and age<=60
	print("he will work in urban areas only.: ")
else:
	print("ERROR")


