dict1= {}
n = int(input("Enter Size of dict: "))
for i in range(n):
    key = input("Student ID  : ")
    lis=[]
    for j in range(5):
        k = int(input("Enter data : "))
        lis.append(k)
    dict1[key] = lis 
print (dict1)