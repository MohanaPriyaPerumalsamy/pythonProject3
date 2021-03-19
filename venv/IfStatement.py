# age=input("Enter ur age\n")
# if int(age)>18:
#     print("Allow for voting")
# elif int(age)<18 and int(age)>0:
#     print("come after 18 years")
# else:
#     print("Enter valid age")

 ############################################################################
age=input("Enter ur age\n")

if age.isnumeric():
    if int(age)>=18:
        print("Allow")
    elif int(age)==0:
        print("Enter age greater than 0")
    else:
       print("Not Allowed")
else:
    print("Enter valid age")