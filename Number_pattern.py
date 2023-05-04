rows = int(input("enter the number of rows:"))
for i in range(rows+1):
    for j in range(i):
        print(i,end='') # To print in same line
    print('')
