students=["priya","mohana","roshini","hari","srini"]
# for items in students:
#     print(items)

# Iterating the string
# for i in students:
#     for j in i:
#         print("{}".format(j))
#
#Using continue Statement
# for name in students:
#      if name=="mohana":
#         continue
#      print(name)
#
# #Using Break Statement
# for name in students:
#     if name=="hari":
#         break
#     print(name)
############################################################
#Using Interger
string_num="45,58,65,7"
for i in string_num:
    if not i.isnumeric():
        continue
    print(i)

