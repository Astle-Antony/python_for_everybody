def array():
 list1 = []
 n = int(input("enter the range of the list1:"))
 for i  in range (0,n):
    val = int(input())
    list1.append(val)
 print(sorted(list1))
 list2 =[]
 m = int(input("enter the range of the list2:"))
 for j in range(m):
    val1 = int(input())
    list2.append(val1)
 print(sorted(list2))
 if len(list1) == len(list2):
    print("the size of the lists are same")
    for i in list1:
        if i not in list2:
            print("they are not same")
            break
        else:
            return("they are same")

print(array())