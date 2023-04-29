a=input()      #removing duplicates by using membership operator
b=[]
for i in a:
    if i not in b:
        b.append(i)
    c="".join(b)
print(c)
count=len(c)
print(count)
        