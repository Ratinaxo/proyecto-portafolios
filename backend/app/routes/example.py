# app/routes/example.py
from flask import Blueprint

example_bp = Blueprint('example', __name__)

@example_bp.route("/api/hello")
def hello():
    return {"message": "Hello from Flask!"}
