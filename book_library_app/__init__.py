from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from book_library_app import authors
from book_library_app import models
