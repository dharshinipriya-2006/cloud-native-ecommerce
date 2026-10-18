
from flask import Flask, render_template, jsonify

app = Flask(__name__)
   
products = [
    {
        "id": 1,
        "name": "Headphones",
        "price": 999,
        "category": "Electronics",
        "emoji": "🎧"
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "price": 1499,
        "category": "Electronics",
        "emoji": "⌚"
    },
    {
        "id": 3,
        "name": "Laptop Bag",
        "price": 799,
        "category": "Accessories",
        "emoji": "🎒"
    },
    {
        "id": 4,
        "name": "Keyboard",
        "price": 1199,
        "category": "Electronics",
        "emoji": "⌨️"
    },
    {
        "id": 5,
        "name": "Wireless Mouse",
        "price": 599,
        "category": "Electronics",
        "emoji": "🖱️"
    },
    {
        "id": 6,
        "name": "Bluetooth Speaker",
        "price": 1299,
        "category": "Electronics",
        "emoji": "🔊"
    },
    {
        "id": 7,
        "name": "Men's T-Shirt",
        "price": 499,
        "category": "Fashion",
        "emoji": "👕"
    },
    {
        "id": 8,
        "name": "Women's Handbag",
        "price": 999,
        "category": "Fashion",
        "emoji": "👜"
    },
    {
        "id": 9,
        "name": "Running Shoes",
        "price": 1499,
        "category": "Fashion",
        "emoji": "👟"
    },
    {
        "id": 10,
        "name": "Water Bottle",
        "price": 299,
        "category": "Home & Kitchen",
        "emoji": "🧴"
    },
    {
        "id": 11,
        "name": "Coffee Mug",
        "price": 199,
        "category": "Home & Kitchen",
        "emoji": "☕"
    },
    {
        "id": 12,
        "name": "Desk Lamp",
        "price": 699,
        "category": "Home & Kitchen",
        "emoji": "💡"
    },
    {
        "id": 13,
        "name": "Sunglasses",
        "price": 399,
        "category": "Accessories",
        "emoji": "🕶️"
    },
    {
        "id": 14,
        "name": "Backpack",
        "price": 899,
        "category": "Accessories",
        "emoji": "🎒"
    },
    {
        "id": 15,
        "name": "Power Bank",
        "price": 1099,
        "category": "Electronics",
        "emoji": "🔋"
    },
    {
        "id": 16,
        "name": "Cushion Set",
        "price": 549,
        "category": "Home & Kitchen",
        "emoji": "🛋️"
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
