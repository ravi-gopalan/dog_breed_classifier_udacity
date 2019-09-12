# import Flask class from the flask module
from flask import Flask

import numpy as np
import pickle

# Create Flask object to run
app = Flask(__name__)

@app.route('/')
def home():
    return "Hi, Welcome to Flask!!"

  if __name__ == "__main__":
	print("**Starting Server...")
	
	# Run Server
	app.run()
