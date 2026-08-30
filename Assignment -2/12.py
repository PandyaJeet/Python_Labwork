l=[]
e=[]
o=[]
for i in range(5):
    n=int(input("Enter Data : "))
    l.append(n)
    if(n%2 == 0):
        e.append(n)
    else:
        o.append(n)
print("Even : "+str(e))
print("Odd : "+str(o))