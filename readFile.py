f = open("Testing.txt", "r")
a = f.read()
d = ""

str = a.split()

for y in str:
    if y[0]=='#':
        print(y)
        d += y

#print(d)
file1 = open("Testing2.txt", "w")
file1.writelines(d)
