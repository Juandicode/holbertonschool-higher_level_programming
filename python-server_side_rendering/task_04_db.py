from flask import Flask, render_template, request
import json
import csv
import sqlite3
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

def load_sql_products():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

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
    elif source == 'sql':
        products = load_sql_products()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

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
