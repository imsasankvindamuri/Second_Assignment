num=int(input("Enter Number of Elements: "))
list = []
for i in range(num):
    entry=int(input("Enter element: "))
    list.append(entry)
print(f"Unorganized list: {list}\n\n")
for vals in range(len(list) - 1):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            temp = list[i + 1]
            list[i + 1] = list[i]
            list[i] = temp
print(f"Organized List: {list}\n\n")


# Notes
"""
For 15 Elements it is near instantaneous

"""
