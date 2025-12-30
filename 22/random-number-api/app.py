from flask import Flask, jsonify
import random
import logging 

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", handlers=[
    logging.FileHandler("/logs/apps.log"),
    logging.StreamHandler()
])

@app.route("/generate", methods=["GET"])
def generate():
    app.logger.info("Random number is generated")
    number = random.randint(0, 100)
    return jsonify(message=f"Random number: {number}")
