from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    hasil_input = None
    if request.method == "POST":
        hasil_input = request.form.get("nama_input")
    return render_template("index.html", hasil=hasil_input)

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"

if __name__ == "__main__":
    app.run(debug=True)