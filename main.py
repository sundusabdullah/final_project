import os
from flask import Flask, render_template


Images = os.path.join('static', 'image')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = Images


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

@app.route("/order")
def order():
  icon = os.path.join(app.config['UPLOAD_FOLDER'], 'icon.png')
  return render_template("order.html", title="order", icon_=icon)


if __name__ == "__main__":
  app.run(debug=True)

