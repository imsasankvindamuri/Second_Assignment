num=int(input("Enter Number of Elements: "))
list1 = []
for i in range(num):
    entry=int(input("Enter element: "))
    list1.append(entry)
print(f"Unorganized list: {list1}\n\n")
for vals in range(len(list1) - 1):
    for i in range(len(list1) - 1):
        if list1[i] > list1[i + 1]:
            temp = list1[i + 1]
            list1[i + 1] = list1[i]
            list1[i] = temp
print(f"Organized List: {list1}\n\n")
