class Vehicle:
    engine=""
    def __init__(self, engine):
        self.engine=engine
class Car(Vehicle):
    door=""
    def __init__(self, engine, door):
        super().__init__(engine)
        self.door=door
class SportsCar(Car):
    turbo=""
    def __init__(self, engine, door, turbo):
        super().__init__(engine, door)
        self.turbo=turbo
def main():
    s1 = SportsCar("V8", 4, "Turbo")
    print("Engine:", s1.engine)
    print("Door:", s1.door)
    print("Turbo:", s1.turbo)
main()