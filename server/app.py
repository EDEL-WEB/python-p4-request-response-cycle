#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    # Your virtual environment is activated and using the correct Python interpreter.
    # You do not need to add any code here for virtual environment management.
    # To run your Flask app, use:
    #   flask run
    # or
    #   python app.py
    # Ensure Flask is installed in your virtual environment.
