from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def load_json_products():
    if not os.path.exists("products.json"):
        return []
    with open("products.json") as f:
        return json.load(f)

def load_csv_products():
    if not os.path.exists("products.csv"):
        return []
    with open("products.csv", newline='') as f:
        reader = csv.DictReader(f)
        return [ 
            {
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            } for row in reader
        ]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products = load_json_products()
    elif source == 'csv':
        products = load_csv_products()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Si hay ID, filtrar
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID format"
            products = []
    
    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
