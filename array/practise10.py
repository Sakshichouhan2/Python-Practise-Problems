#Write a Python script to merge two Python dictionaries
dic1 = {'reshu':100, 'reshu1':200}
dic2 = {'neha':300, 'neha1':400}
dic = dic1.copy()
dic.update(dic2)
print(dic)