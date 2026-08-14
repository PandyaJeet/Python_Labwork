dict ={
    "January": "",
    "February": "",
    "March" : "",
    "April" : "",
    "May": "",
    "June": "",
    "July" : "",
    "August" : "",
    "September": "",
    "October": "",
    "November" : "",
    "December" : "",
}
greater=0
k=0
for i in dict.keys():
    value = int(input("Enter bill for " + i +" : "))
    dict[i] = value
    if (value>greater):
        greater=value
        k = i

print(k + " : "+ str(greater))