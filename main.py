fname = input("Enter file name: ")
fh = open(fname)
words = list()
for line in fh:
    line = line.split()
    line = line.rstrip()

    if line not in words:
        words.append(line)
    else:
        continue
words.sort()
print(words)


