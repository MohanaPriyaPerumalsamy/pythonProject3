# num={2:"apple",1:"orange",3:"king"}
# for key in num:
#     print(num[key])
#
# for key in sorted(num):
#     print(num[key])

################################################################
# l=["a","b","c"]
# # for i in l:
# #     print(i)
# for i in range(len(l)):
#     print(l[i])
################################################################
# cities= {"chennai":"south side of India","Bangalore":"Karnataka Capital","Delhi":"India's Capital"}
# print(cities)
# print(cities["chennai"])
# cities["Kolkata"]="East side of India"
# print(cities)
# cities["Kolkata"]="city of sweets"
# print(cities)
# cities= {"chennai":"south side of India","Bangalore":"Karnataka Capital","Delhi":"India's Capital","Kolkata":"East side of India","Kolkata":"city of sweets"}
# print(cities)

###################################################################
# num={"a":"apple","b":"orange",3:9}
# print(num)
# path={"p1":"c://Desktop//home","dic":num}
# print(path)
# tup=("3","d","are")
# path={"p1":"c://Desktop//home","dic":num,"tup":tup}
# print(path)
# ######################################################################
# #deleting the key and value in Dictionary
# del path["tup"]
# print(path)
# # del(path)
# # print(path)
# #clearing the dictionary
# path.clear()
# print(path)
# #fetching the value
num={"a":"apple","b":"orange",3:9}
while True:
    inputkey=input("enter the key")
    print(num[inputkey])
