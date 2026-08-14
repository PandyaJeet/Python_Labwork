dict ={
    "Banana" : 100,
    "Apple" : 200,
    "Mango" : 300,
}
dict1= {}
n = int(input("Enter Size of dict: "))
for i in range(n):
    key = input("Fruit Name : ")
    value = int(input("Price : "))
    dict1[key] = value 
print (dict1)