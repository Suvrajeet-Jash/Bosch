def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

x= int(input("Enter the Number: "))

print(f" The factorial of {x} is {factorial(x)}")
