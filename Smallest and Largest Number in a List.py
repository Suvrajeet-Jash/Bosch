list1 = input("Enter elements separated by space: ").split()

list2 = []

for i in list1:
    list2.append(int(i)) #Converting str to int and storing it in list2

sorted_list = sorted(list2)

print(list1)
print(sorted_list)
print("Smallest Element: ", list2[0])
print("Biggest Element: ", list2[-1])
