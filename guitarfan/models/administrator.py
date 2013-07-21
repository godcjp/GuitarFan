from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class AdminUser(db.Model):
    __tablename__ = 'adminuser'

    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String)
    status = db.Column(db.Integer)

    def __init__(self, id, name, email, status):
        self.id = id
        self.name = name
        self.email = email
        self.status = status

    def __repr__(self):
        return '<AdminUser %r>' % self.name

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_password(self, new_password):
        self.password = generate_password_hash(new_password, salt_length=8)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.status

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)