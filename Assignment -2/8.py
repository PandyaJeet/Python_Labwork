l=[]
for i in range(5):
    n=int(input("Enter Data : "))
    l.append(n)
print("Ascending : "+str(sorted(l)))
print("Descending : "+str(sorted(l, reverse=True)))