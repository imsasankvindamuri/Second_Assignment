num=int(input("Enter Number of Elements: "))
list1 = []
for i in range(num):
    entry=int(input("Enter element: "))
    list1.append(entry)
print(f"Unorganized list: {list1}\n\n")
list2=[]
while len(list1)!=0:
    min=0
    for i in range(len(list1)):
        if list1[min]>list1[i]:
            min=i
    list2.append(list1[min])
    list1.pop(min)
print(list2)