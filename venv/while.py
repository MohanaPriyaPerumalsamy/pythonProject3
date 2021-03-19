i=0
while i<3:
    print(i)
    i+=1

win_number=100
answer=0
while answer!=win_number:
    answer=int(input("enter a new guess"))
    if answer==win_number:
        print("you won")
        break