n = int(input("Enter a number: "))
tup=[]
for i in range(n):
    k= int(input("Enter data " + str(i)+ " : "))
    tup.append(k)
tup=tuple(tup)
greatest = 0
great = 0
for i in tup:
    for j in tup:
        if i==j:
            continue
        elif i>j and i>greatest:
            greatest = i
        if greatest>i and  great<i:
            great = i
print(f"{greatest} + {great}")    