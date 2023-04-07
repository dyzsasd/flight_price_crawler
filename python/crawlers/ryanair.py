import requests
from bs4 import BeautifulSoup
from config.settings import RYANAIR_BASE_URL, HEADERS, TIMEOUT, RETRY_ATTEMPTS, RETRY_DELAY
from models.flight import Flight
from utils.helpers import retry_on_exception


class RyanairCrawler:
    def __init__(self):
        self.base_url = RYANAIR_BASE_URL
        self.headers = HEADERS
        self.timeout = TIMEOUT

    @retry_on_exception(retries=RETRY_ATTEMPTS, delay=RETRY_DELAY)
    def fetch_flight_data(self, origin, destination, departure_date, return_date=None):
        url = f"{self.base_url}/search?origin={origin}&destination={destination}&departure_date={departure_date}"

        if return_date:
            url += f"&return_date={return_date}"

        response = requests.get(url, headers=self.headers, timeout=self.timeout)
        response.raise_for_status()

        return response.content

    def parse_flight_data(self, html_content):
        flights = []
        soup = BeautifulSoup(html_content, "html.parser")

        # Locate the flight information container in the HTML
        flight_containers = soup.find_all("div", class_="flight-container")

        for container in flight_containers:
            origin = container.find("div", class_="origin").text.strip()
            destination = container.find("div", class_="destination").text.strip()
            departure_time = container.find("div", class_="departure-time").text.strip()
            arrival_time = container.find("div", class_="arrival-time").text.strip()
            price = float(container.find("div", class_="price").text.strip().replace("€", ""))

            flight = Flight(
                airline="Ryanair",
                origin=origin,
                destination=destination,
                departure_time=departure_time,
                arrival_time=arrival_time,
                price=price
            )
            flights.append(flight)

        return flights

    def get_flights(self, origin, destination, departure_date, return_date=None):
        html_content = self.fetch_flight_data(origin, destination, departure_date, return_date)
        flights = self.parse_flight_data(html_content)
        return flights
    
    def to_dict(self):
        return {
            "airline": self.airline,
            "origin": self.origin,
            "destination": self.destination,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "price": self.price,
        }
