age = input("please input your age: ")
print('your age is: ', age)
if (int(age) >= 18):
    print ('adults')
elif (int(age) >= 6):
    print ('adults')
else:
    print('kids')



birth = input('year of birth: ')
if int(birth) < 1980:
    print("before 80")
elif int(birth) < 1990:
    print("after 80")
else:
    print("So yong!")



salaryStr = input("your salary: ")
salary = int(salaryStr)
if salary <= 5000:
    print("crying...")
elif salary <= 10000:
    print("just so so...")
elif salary <= 20000:
    print("not bad...")
elif salary <= 30000:
    print("happy...")
else:
    print("Wow....")
