# database.py
# ------------------------
# Simulated (temporary) database for Bloomify 🌸

# Stores registered users
users = {}

# Available flowers in the shop
flowers = [
    {"id": 1, "name": "Red Rose", "price": 15, "image": "images/rosesk.jpg"},
    {"id": 2, "name": "Tulip", "price": 12, "image": "images/tulipsk.jpg"},
    {"id": 3, "name": "Sunflower", "price": 10, "image": "images/sunflowersk.jpg"}
]

# Stores customer orders
orders = []

# Admin login info
admin_user = {"username": "admin", "password": "1234"}


