dict1= {}
n = int(input("Enter Size of dict: "))
for i in range(n):
    key = input("Student ID  : ")
    value = input("Name : ")
    dict1[key] = value 
keyToSearch = input("Input ID to Search : ")
for j in dict1.keys():
    if(keyToSearch == j):
        print("ID FOUND !!!\n"+dict1[j])
        print()
print (dict1)