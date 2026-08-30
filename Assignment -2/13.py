l=[]
for i in range(5):
    n=input("Enter Data : ")
    l.append(n)
nl=list(set(l))
print("Unique List : "+str(nl))