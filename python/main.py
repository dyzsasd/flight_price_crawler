from crawlers.ryanair import RyanairCrawler
from db import save_flight

def main():
    origin = "BCN"  # Barcelona
    destination = "AMS"  # Amsterdam
    departure_date = "2023-05-01"
    return_date = "2023-05-10"

    ryanair_crawler = RyanairCrawler()

    crawlers = [
        ryanair_crawler,
    ]

    flights = []

    for crawler in crawlers:
        try:
            flights += crawler.get_flights(origin, destination, departure_date, return_date)
        except Exception as e:
            print(f"Error fetching flights from {crawler.__class__.__name__}: {e}")

    print(f"Found {len(flights)} flights:")
    for flight in flights:
        print(flight)
        flight_id = save_flight(flight)
        print(f"Saved flight with ID: {flight_id}")

if __name__ == "__main__":
    main()
