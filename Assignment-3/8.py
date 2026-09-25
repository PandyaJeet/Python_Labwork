class MovieTicket:
    def __init__(self, movie_name, seat_no, price):
        self.movie_name = movie_name
        self.seat_no = seat_no
        self.price = price

    def display_ticket(self):
        print("Movie Name:", self.movie_name)
        print("Seat No:", self.seat_no)
        print("Price:", self.price)

    def is_affordable(self, budget):
        if self.price <= budget:
            print("Affordable")
        else:
            print("Not Affordable")


def main():
    ticket = MovieTicket("Inception", "A12", 300)
    ticket.display_ticket()
    ticket.is_affordable(350)


main()
