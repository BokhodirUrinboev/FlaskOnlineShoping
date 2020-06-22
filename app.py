from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/product-single')
def product_single():
    return render_template('product-single.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog-single')
def blog_single():
    return render_template('blog-single.html')


if __name__ == '__main__':
    app.run()
