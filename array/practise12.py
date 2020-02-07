#Write a Python program to remove a key from a dictionary
myDict = {'a':9,'b':7.9,'c':7,'d':234}
print(myDict)
if 'i' in myDict: 
    del myDict['i']
print(myDict)
print(type(myDict))