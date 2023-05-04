# looping through strings using for loop

fruits = 'bananana'
for i in fruits:
    print(i)


# looping through strings using while loop

fruits = "banana"
count = 0
while count<len(fruits):
    print(fruits[count])
    count = count+1

# counting letters in string

count = 0
for i in fruits:
    if i == "a":
        count= count+1
print("the total occurence of 'a' is:",count)