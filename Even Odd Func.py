def even(x):
    if x%2 == 0:
        return 1
    else:
        return 0

a = int(input("Enter the Number: "))
res = even(a)

if res == 1:
    print (f"{a} is Even")
else:
    print (f"{a} is Odd")
