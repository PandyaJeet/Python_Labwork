class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        print("Area:", 3.14 * self.r * self.r)

def main():
    c1 = Circle(10)
    c1.area()

main()
