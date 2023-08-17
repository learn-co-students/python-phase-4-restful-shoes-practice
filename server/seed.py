from app import app
from models import Shoe, db

with app.app_context():
    print("Clearing old shoes...")

    Shoe.query.delete()

    print("Adding some shoes...")

    shoes = []

    for _ in range(10):
        pass
