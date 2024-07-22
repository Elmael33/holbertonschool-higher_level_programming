from flask import Flask, request, render_template
import csv
import json
import sqlite3

app = Flask(__name__)

def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def load_csv_data(filepath):
    records = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            records.append(row)
    return records

def fetch_sqlite_data():
    connection = sqlite3.connect('products.db')
    cur = connection.cursor()
    cur.execute('SELECT * FROM Products')
    rows = cur.fetchall()
    connection.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]

@app.route('/products')
def show_products():
    source_type = request.args.get('source')
    prod_id = request.args.get('id', type=int)
    data = []

    try:
        if source_type == 'json':
            data = load_json_data('products.json')
        elif source_type == 'csv':
            data = load_csv_data('products.csv')
        elif source_type == 'sql':
            data = fetch_sqlite_data()
        else:
            return render_template('product_display.html', error="Invalid source provided")
        
        if prod_id is not None:
            data = [item for item in data if item['id'] == prod_id]
            if not data:
                return render_template('product_display.html', error="Product not found")

        return render_template('product_display.html', products=data)
    
    except (FileNotFoundError, sqlite3.Error) as e:
        return render_template('product_display.html', error=f"Error fetching data: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
