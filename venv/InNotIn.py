phrase="chennai is a good city"
check=input("enter a word")

if check in phrase:
    print("\"{}\" in \"{}\"".format(check,phrase))
else:
    print("\'{}\' is not in \'{}\'".format(check, phrase))
