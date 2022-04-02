from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models.medicalRecords import UserRecords

class User(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    username =  db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    record=db.relationship('UserRecords', backref='User', useList=False)

    def __init__(self,id,username,email,password):
        self.id=id
        self.username=username
        self.email=email
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'password': self.password
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

