import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "ariel_secret"

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'uts_flask')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 3306))

mysql = MySQL(app)

@app.route('/')    
def home():
    return render_template('dashboard.html') 

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('users.html', users=data)

@app.route('/users/add', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        flash('User berhasil ditambahkan!')
        return redirect(url_for('users'))
    return render_template('user_form.html', action='Tambah', user=None)

@app.route('/users/edit/<int:id>', methods=['GET','POST'])
def edit_user(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cur.fetchone()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, id))
        mysql.connection.commit()
        flash('User berhasil diubah!')
        return redirect(url_for('users'))
    return render_template('user_form.html', action='Edit', user=user)

@app.route('/users/delete/<int:id>')
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    flash('User dihapus!')
    return redirect(url_for('users'))

@app.route('/products')
def products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    cur.close()
    return render_template('products.html', products=data)

@app.route('/products/add', methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
        mysql.connection.commit()
        flash('Produk berhasil ditambahkan!')
        return redirect(url_for('products'))
    return render_template('product_form.html', action='Tambah', product=None)

@app.route('/products/edit/<int:id>', methods=['GET','POST'])
def edit_product(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cur.fetchone()
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']
        cur.execute("UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s", (name, price, stock, id))
        mysql.connection.commit()
        flash('Produk berhasil diubah!')
        return redirect(url_for('products'))
    return render_template('product_form.html', action='Edit', product=product)

@app.route('/products/delete/<int:id>')
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM products WHERE id=%s", (id,))
    mysql.connection.commit()
    flash('Produk dihapus!')
    return redirect(url_for('products'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
