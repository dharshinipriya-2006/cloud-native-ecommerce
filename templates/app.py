
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {
        "id": 1,
        "name": "Headphones",
        "price": 999,
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "price": 1499,
        "category": "Electronics"
    },
    {
        "id": 3,
        "name": "Laptop Bag",
        "price": 799,
        "category": "Accessories"
    },
    {
        "id": 4,
        "name": "Keyboard",
        "price": 1199,
        "category": "Electronics"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/products")
def get_products():
    return jsonify(products)


@app.route("/api/products/<int:product_id>")
def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


@app.route("/health")
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "CloudCart API"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
