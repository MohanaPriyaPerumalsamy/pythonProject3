# winingnumber=200
# print("Guess the number 1 to 1000")
# guessnum=int(input("Enter the number"))
# if guessnum<winingnumber:
#     print("Guess Higher")
# elif guessnum>winingnumber:
#     print("Guess Lower")
# else:
#     print("You won the game")

##########################################################

winingnumber=200
print("Guess the number 1 to 1000")
guessnum=int(input("Enter the number"))
if guessnum!=winingnumber:
    if guessnum<winingnumber:
        print("Guess Higher")
    else:# guessnum>winingnumber:
        print("Guess Lower")
        guessnum=int(input("Enter number"))
    if guessnum==winingnumber:
        print("You won the game")
    else:
        print("better luck next time")
else:
    print("You won the game at first attempt")
