pas = input("Enter password : ")
if(len(pas) < 8):
    print("Password must be at least 8 characters long.")
flag1 = False
flag2 = False
for c in pas:
    if c.isdigit():
        flag1 = True
    if c.isupper():
        flag2 = True

if flag1 != True:
    print("Password must contain at least one digit.")
if flag2 != True:
    print("Password must contain at least one uppercase letter.")