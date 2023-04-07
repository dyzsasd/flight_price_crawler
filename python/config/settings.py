import os

# Web scraping settings
HEADERS = {
    "User-Agent": os.environ.get("HEADERS_USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"),
}
TIMEOUT = int(os.environ.get("TIMEOUT", "10"))
RETRY_ATTEMPTS = int(os.environ.get("RETRY_ATTEMPTS", "3"))
RETRY_DELAY = int(os.environ.get("RETRY_DELAY", "5"))

# Ryanair settings
RYANAIR_BASE_URL = os.environ.get("RYANAIR_BASE_URL", "https://www.ryanair.com")

# MongoDB settings
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://username:password@localhost:27017/")
MONGODB_DB_NAME = os.environ.get("MONGODB_DB_NAME", "flight_data")
MONGODB_COLLECTION_NAME = os.environ.get("MONGODB_COLLECTION_NAME", "flights")