f = open("Testing.txt", "r")
a = f.read()
d = ""
b = ""
str = a.split()

for y in str:
    if y[0]=='#' :
        #print(y)
        d += y
    elif r"\n" in y:
        if "#" in y:
            b = y.split(r"\n")
            for x in b:
                if "#" in x:
                    #print(x)
                    d += x

my_str = d.split("#")

final_str = list(set(my_str))
for z in final_str:
    print(z)

file1 = open("Testing2.txt", "w")
file1.writelines(final_str)
