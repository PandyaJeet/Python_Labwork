n = int(input("Enter a number: "))
tup=[]
sum=0
for i in range(n):
    k= int(input("Enter data " + str(i)+ " : "))
    tup.append(k)
tup=tuple(tup)
for j in tup:
    sum+=j    
print(sum)