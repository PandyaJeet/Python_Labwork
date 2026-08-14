n = int(input("Enter size: "))
data = []

for i in range(n):
    k = int(input("Enter data " + str(i) + ": "))

    if k in data:
        print("Duplicate Data detected!!!")
    else:
        data.append(k)

print("Data:", data)