from app import app
from db import db

db.init_app(app)


# we create the db and tables inside here before any requests will be made
@app.before_first_request
def create_tables():
    db.create_all()
