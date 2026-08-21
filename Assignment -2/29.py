def bmi(h:float,w:float):
    return (w/(h*h))*1000
def main():
    w=float(input("Enter weight (in kg) : "))
    h=float(input("Enter height (in meters) : "))
    print("Body Mass Index : " + str(bmi(w,h)))
main()