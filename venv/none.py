shoppinglist=["pencil","pen","rubber"]
checkitem=None
itemtocheck="pen"
for i in shoppinglist:
    if itemtocheck in shoppinglist:
        checkitem=shoppinglist.index(itemtocheck)
if checkitem is not None:
    print("Item found at position{}".format(checkitem))
else:
    print("{} item not found".format(checkitem))

print(shoppinglist[0])

for i in range(len(shoppinglist)):
    if shoppinglist[i]==itemtocheck:
        continue
    #print(shoppinglist[i])
    else:
        #     break
        print(shoppinglist[i])

# for i in shoppinglist:
#     print(i)
