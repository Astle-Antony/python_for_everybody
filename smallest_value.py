smallest = None
for i in [1,3,4,2,-3]:
    if smallest is None:
        smallest = i
    elif i<smallest:
        smallest = i
    print(i,smallest)
print("the smallest value is :",smallest)
