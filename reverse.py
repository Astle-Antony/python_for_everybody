numbers = int(input("enter the value"))
reverse = 0 # it just keeps on updating
while numbers != 0:
    digits = numbers % 10  # to separate the last digit
    reverse = reverse*10 + digits # to store the values in reverse order
    numbers//= 10 # this checks the while condition

print("the reversed number value is ", reverse) # it prints the statement

stuff = dict()
stuff['hello']=1
print(stuff.items())