print("largest_number")
large = None
# none flag value
for i in [45,67,78,799,86,78,100] :
    if large is None:
        large = i
    elif i>large :
        large = i
    print("large:",large ,":",i)
print("the largest number is:",large)
