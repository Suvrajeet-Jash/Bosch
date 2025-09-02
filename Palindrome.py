str = str(input("Enter a Word: ")).upper() #Entering a Word and Converting to Palindrome

if str == str[::-1]:
    print(f"{str} is Palindrome")
else:
    print(f"{str} is Not Palindrome")

