from crudflask import db



#########################   DB model
class User(db.Model): # that sould manage our loggin sessions  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20) )
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.phone}')"

