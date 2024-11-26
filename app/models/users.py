from BaseModel import BaseModel

class User(BaseModel):
    def __init__(self, id, first_name, last_name, email, is_admin, created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email
        self.is_admin
        self.created_at
        self.updated_at

def hash_password(self, password):
    """Hashes the password before storing it."""
    self.password = bcrypt.generate_password_hash(password).decode('utf-8')

def verify_password(self, password):
    """Verifies if the provided password matches the hashed password."""
    return bcrypt.check_password_hash(self.password, password)
