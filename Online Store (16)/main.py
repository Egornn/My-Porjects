from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    product = {
        'id': product_id,
        'name': 'Product Name',
        'description': 'Product Description',
        'price': 19.99
    }
    return render_template('product.html', product=product)

@app.route('/cart')
def cart():
    cart_items = []
    return render_template('cart.html', cart_items=cart_items)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
