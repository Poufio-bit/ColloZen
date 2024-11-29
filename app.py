from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bienvenue sur le site ColloZen</h1>"

@app.route("/ask", methods=["GET", "POST"])
def ask():
    if request.method == "POST":
        question = request.form.get("question")
        # Remplace temporairement la réponse avec un texte fixe pour vérifier Flask
        return jsonify({"question": question, "response": "Ceci est une réponse de test."})
    return render_template("ask.html")

if __name__ == "__main__":
    app.run(debug=True)
