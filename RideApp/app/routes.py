from flask import render_template, request
from app import app
from app.utils import calculate_distance, get_directions, calculate_price

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        source = request.form["source"]
        destination = request.form["destination"]
        mode = request.form["mode"]
        
        distance = calculate_distance(source, destination)
        price = calculate_price(distance, mode)
        directions = get_directions(source, destination, mode)
        
        return render_template("index.html", distance=distance, price=price, directions=directions, source=source, destination=destination, mode=mode)
    
    return render_template("index.html")
