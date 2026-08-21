rollnumbers = {101,102,103,104,105,106}
present=set()
print("Enter present numbers\n")
for i in range(6):
    roll= int(input())
    present.add(roll)
print("Present number : "+str(rollnumbers.intersection(present)))
print("Absent Numbers : " + str(rollnumbers.difference(present)))