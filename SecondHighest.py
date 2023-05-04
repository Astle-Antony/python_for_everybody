no = int(input("size of the list:"))
list = list()
for i in range(no):
    val= int(input())
    list.append(val)
print(list)

highest = 0
secondhighest = 0
for i in list:
    if i > highest:
        secondhighest = highest
        highest = i
    elif(i > secondhighest):
        secondhighest = i
print(highest)
print(secondhighest)
