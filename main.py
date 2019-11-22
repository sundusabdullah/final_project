import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL


Images = os.path.join('static', 'image')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = Images
app.config['MYSQL_DATABASE_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_DATABASE_USER'] = '********'
app.config['MYSQL_DATABASE_PASSWORD'] = '********'
app.config['MYSQL_DATABASE_DB'] = 'sql12312952'
mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def home():
  icon = os.path.join(app.config['UPLOAD_FOLDER'], 'icon.png')
  return render_template("home.html", icon_=icon)

@app.route("/about")
def about():
  icon = os.path.join(app.config['UPLOAD_FOLDER'], 'icon.png')
  return render_template("about.html", icon_=icon,)

@app.route("/products")
def products():
  icon = os.path.join(app.config['UPLOAD_FOLDER'], 'icon.png')
  return render_template("products.html", icon_=icon)

@app.route("/contact")
def contact():
  icon = os.path.join(app.config['UPLOAD_FOLDER'], 'icon.png')
  return render_template("contact.html", icon_=icon)


@app.route("/order", methods=['GET', 'POST'])

def order():
  cursor = mysql.get_db().cursor()

  #Condition to select only type
  if request.method == 'POST':

    prod_type = request.form['prod_type']

  else:
    prod_type = ""

  cursor.execute('select * from products where prod_type="'+str(prod_type)+'"')
  result = cursor.fetchall()

  if request.method == 'POST' and "prod_name" in request.form:

    prod_name = request.form['prod_name']
    Quantity = request.form['number']

    # Insert Data into database
    cursor.execute('select price from products where prod_name= "'+str(prod_name)+'"')
    result_price = cursor.fetchall()
    cursor.execute("INSERT INTO orders(prod_name, Quantity, price) VALUES (%s, %s, %s)",
                     (prod_name, Quantity, result_price))
    mysql.get_db().commit()
    #End of insert

  #Show orders
  cursor.execute('''select * from orders''')
  order_result = cursor.fetchall()

  #Calculate Total
  cursor.execute("select sum(Quantity*price) from orders")
  total = cursor.fetchall()
  for i in total:
    total = float(i[0])

  #Calculate Total with tax
  cursor.execute("select sum((Quantity*price)*.05) from orders")
  tax = cursor.fetchall()
  for i in tax:
    tax = float(i[0])
  Total_tax = total+tax
  cursor.close()



  icon = os.path.join(app.config['UPLOAD_FOLDER'], 'icon.png')
  return render_template("order.html", title="order", icon_=icon, result=result,
                         order=order_result, total=total,
                         Total_tax=Total_tax)


if __name__ == "__main__":
  app.run(debug=True)