class Ride:
    def __init__(self, ride_id, passenger_name, distance_km):
        self.ride_id = ride_id
        self.passenger_name = passenger_name
        self.distance_km = distance_km

    def calculate_fare(self):
        return 0


class EconomyRide(Ride):
    def calculate_fare(self):
        return 10 * self.distance_km


class PremiumRide(Ride):
    def calculate_fare(self):
        return 18 * self.distance_km + 50


class OutstationRide(Ride):
    def calculate_fare(self):
        return 15 * self.distance_km + 300


def main():
    economy = EconomyRide("R101", "Karan", 15)
    premium = PremiumRide("R102", "Rohan", 15)
    print(f"Booking Economy for {economy.passenger_name} ({economy.distance_km} km) -> Fare: ₹{economy.calculate_fare()}")
    print(f"Booking Premium for {premium.passenger_name} ({premium.distance_km} km) -> Fare: ₹{premium.calculate_fare()}")


main()
