from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# 🌸 Flower data
flowers = [
    {"id": 1, "name": "Rose", "price": 10, "image": "images/rosesk.jpg", "likes": 0, "saved": False},
    {"id": 2, "name": "Tulip", "price": 12, "image": "images/tupipsk.jpg", "likes": 0, "saved": False},
    {"id": 3, "name": "Sunflower", "price": 8, "image": "images/sunflowersk.jpg", "likes": 0, "saved": False},
]



cart = []


# 🏠 Home page
@app.route('/')
def index():
    return render_template('index.html')


# 🌼 Flowers page
@app.route('/flowers')
def show_flowers():
    return render_template('flowers.html', flowers=flowers)


# ❤️ Like flower
@app.route('/like/<int:flower_id>')
def like_flower(flower_id):
    for flower in flowers:
        if flower["id"] == flower_id:
            flower["likes"] += 1
            break
    return redirect(url_for('show_flowers'))


# 💾 Save/Unsave flower
@app.route('/save/<int:flower_id>')
def save_flower(flower_id):
    for flower in flowers:
        if flower["id"] == flower_id:
            flower["saved"] = not flower["saved"]
            break
    return redirect(url_for('show_flowers'))


# 🛒 Add flower to cart
@app.route('/add_to_cart/<int:flower_id>')
def add_to_cart(flower_id):
    for flower in flowers:
        if flower["id"] == flower_id:
            cart.append(flower)
            break
    return redirect(url_for('order'))


# 🧺 Cart page
@app.route('/order')
def order():
    total = sum(f["price"] for f in cart)
    return render_template('order.html', cart=cart, total=total)


# 💳 Payment page
@app.route('/payment', methods=["GET", "POST"])
def payment():
    total = sum(f["price"] for f in cart)

    # If user submits the form
    if request.method == "POST":
        name = request.form["name"]
        card = request.form["card"]
        address = request.form["address"]

        cart.clear()

        return render_template("thank_you.html", name=name, total=total)

    # If user opens payment page normally (GET)
    return render_template('payment.html', cart=cart, total=total)




# 🔐 Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('show_flowers'))
    return render_template('login.html')


# 🧾 Register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('login'))
    return render_template('register.html')


# 🛍 Shop page (MOVED UP HERE!)
@app.route('/shop')
def shop():
    return render_template("shop.html")


# 🚀 Run Flask
if __name__ == "__main__":
    app.run(debug=True)
