num=int(input("Enter Number of Elements: "))
list1 = []
for i in range(num):
    entry=int(input("Enter element: "))
    list1.append(entry)
print(f"Unorganized list: {list1}\n\n")
for i in range(num):
    for j in range(i):
        if j!=i and list1[j]>list1[i]:
            list1[i]=list1[i]+list1[j]
            list1[j]=list1[i]-list1[j]
            list1[i]=list1[i]-list1[j]
print(list1)