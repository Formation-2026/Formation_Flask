from db import db 

class User(db.Model):
    __tablename__="utilisateurs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)


    def __init__(self,name,age):
        self.name = name
        self.age = age

        def Afficher(self):
            return f'nom : {self.nom}, age: {self.age}'
