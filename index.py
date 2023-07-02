from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
config = dotenv_values(".env")

print(config['host'])
db=SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=f"postgresql://{config['user']}:{config['pswd']}@{config['host']}:5432/verceldb?connect_timeout=15"
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self) -> str:
        return f"User({self.username}, {self.email})"

@app.route("/")
def appstart():
    db.create_all()
    u1=User(username='corey',email='abc@gmail.com')
    db.session.add(u1)
    db.session.commit()
    return "db synced"

@app.route("/find")
def hello_world():
    print(User.query.first())
    return "<h1>Hello, World!</h1>"