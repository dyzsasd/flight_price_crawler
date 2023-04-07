class Flight:
    def __init__(
        self,
        airline,
        origin,
        destination,
        departure_time,
        arrival_time,
        price,
    ):
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price

    def __str__(self):
        return (
            f"{self.airline}: {self.origin} -> {self.destination}, "
            f"Departure: {self.departure_time}, Arrival: {self.arrival_time}, Price: €{self.price}"
        )

    def __repr__(self):
        return self.__str__()
