from flask import Flask,render_template,Request, request
from db import db
from flask_migrate import Migrate
from model import User


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///Database.db"
db.init_app(app)
Migrate(app,db)

#defintion des route
@app.route("/",methods=["GET","POST"]) #Lie une fonction a une URL
def rout():
    if request.method =="GET":
        return render_template("form.html")
    if request.method == "POST":
        return "Success"
@app.route("/Chococam")
def index():
    """
    permet de rebondir sur les templates
    Template: pages HTML
    """
    return render_template ("index.html")

@app.route('/Traitement', methods=["GET","POST"])
def traitement():
    if request.method =="GET":
        return render_template("form.html")
    if request.method == "POST":

        nom = request.form.get("Nom")
        age = request.form.get("Age")
        U1 = User(nom,age)
        db.session.add(U1)
        db.session.commit()
        return 'Success'

    
