import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []


def read_csv_products():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception:
        pass
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        data = read_json_products()
    else:
        data = read_csv_products()

    if product_id:
        try:
            p_id = int(product_id)
            data = [p for p in data if p['id'] == p_id]
            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
