x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

print("Before Swapping")
print("First Number: ", x , "....." , "Second Number: " , y)

x=x+y
y=x-y
x=x-y

print("After Swapping")
print("First Number: ", x , "....." , "Second Number: " , y)

