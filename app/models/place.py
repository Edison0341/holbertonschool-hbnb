from BaseModel import BaseModel
from datetime import datetime
from typing import List

class Place(BaseModel):
    def __init__(self, id, title, description, price, latitude, longitude, owner, created_at, updated_at):
        super().__init__()
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.latitued = latitude
        self.longitude = longitude
        self.owner = owner
        self.created_at = created_at
        self.updated_at = updated_at
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)
    
    def add_amenities(self, amenity):
        self.amenities.append(amenity)
