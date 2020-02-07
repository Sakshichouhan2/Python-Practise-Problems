#A 4 digit number is entered through keyboard. Write a program to print a new number with 
#digits reversed as of orignal one. E.g.-
#INPUT : 1234        OUTPUT : 4321
#INPUT : 5982        OUTPUT : 2895 

Number = int(input(" 1234,5982"))
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10

print("\n Reverse of entered number is = %d" %Reverse)
