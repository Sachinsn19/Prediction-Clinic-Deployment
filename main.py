from flask import Flask, render_template,url_for
from diabetes.diabetic import diabetic
from cancer.cancer import cancer
from insurance.insurance import insurance
from heart.heart import heart


app = Flask(__name__)

app.register_blueprint(diabetic,url_prefix="/diabetes")
app.register_blueprint(cancer,url_prefix= "/cancer")
app.register_blueprint(insurance, url_prefix="/insurance")
app.register_blueprint(heart, url_prefix = "/heart" )

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)