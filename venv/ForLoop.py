# name="Canada is near to America"
# for i in name:
#     print(i)
##################################################################################
# num_str="10,96:56;89_63"
# delimiters=""
# number=""
# for i in num_str:
#     if not i.isnumeric():
#         delimiters=delimiters+i
#         print(delimiters)
#     else:
#         number=number+""+i
#         print(number)
####################################################################################
# num_str="10,96:56;89_63"
# delimiters=""
# number=0
# j = 0
# for i in num_str:
#     if i.isnumeric():
#         if j!=1:
#             number=number+1
#         elif j==1:
#             number=number+""+i
#
#         elif not i.isnumeric():
#             delimiters=delimiters+i
#             j=1
#         print(delimiters)
#         print(number)

#############################################################################
#For Loop using Range

# for i in range(2,100):
#     print(i)

# for i in range(100,2):
#     print(i)

# for i in range(100,2,-1):
#     print(i)

# for i in range(100,2,1):
#     print(i)

# # Print Tables
# for i in range(1,6):
#     for j in range(1,11):
#         print("{0} time {1} is equal to {2}".format(i,j,i*j))
#
count=0
for i in range(1,1001):
    if i%9==0:
        count=count+1
        print(i)
        print("cnt"+str(count))

