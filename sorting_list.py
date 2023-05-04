n = int(input('size of list :'))
list = list()
for i in range(n):
    value = int(input())
    list.append(value)
print(list)

for j in range (len(list)):
    for k in range (len(list)-1):
        if list[k]>list[k+1]:
            print('before',list[k],list[k+1])
            list[k],list[k+1]= list[k+1],list[k]
            print('after',list[k],list[k+1])
print(list)
