from logging import exception
a=int(input("Enter a value"))
try:
    print(a/0)
except Exception as e:
    print(e)
    print("error in user input")
print("end of execution")