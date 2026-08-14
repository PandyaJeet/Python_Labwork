dict1= {}
per=0
n = int(input("Enter Size of dict: "))
for i in range(n):
    key = input("Student ID  : ")
    lis=[]
    for j in range(5):
        k = int(input("Enter data : "))
        lis.append(k)
        per+=k
        print(lis)
    dict1[key] = per/5
print (dict1)