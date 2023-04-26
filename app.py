from flask import Flask, request, render_template

app = Flask(__name__, static_folder="./static", template_folder="./template")

@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        a = float(request.form["n1"])
        b = float(request.form["n2"])
        c = float(request.form["n3"])
        return str((a*2)+(b*2)+(c*2))
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
