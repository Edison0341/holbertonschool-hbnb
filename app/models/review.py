from BaseModel import BaseModel

class Reviews(BaseModel):
    def __init__(self, id, text, rating, place, user, created_at, updated_at):
        self.id = id
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at
        
    def add_review(self, review):
        self.reviews.append(review)
