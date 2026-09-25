class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        print("Area:", self.width * self.height)
    def perimeter(self):
        print("Perimeter:", 2 * (self.width + self.height))
def main():
    r1 = Rectangle(10,20)
    r1.area()
    r1.perimeter()
main()    