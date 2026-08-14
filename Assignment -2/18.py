dict1= {}
n = int(input("Enter Size of dict: "))
for i in range(n):
    key = input("Fruit Name : ")
    value = int(input("Price : "))
    dict1[key] = value
i=0
print(" KEY ---------> VALUE ") 
for key,value in dict1.items():
    print(" " + key +" -----> " + str(value))

print (dict1)