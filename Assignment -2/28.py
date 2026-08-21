def si(p,r=7.5,t=1):
    return (p*r*t/100)
def main():
    n=int(input("Enter Principal Amount : "))
    print(str(si(n)))
    r=int(input("Enter Rate of interest : "))
    t=int(input("Enter time : "))
    print(str(si(n,r,t)))