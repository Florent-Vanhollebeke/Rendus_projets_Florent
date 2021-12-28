from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("home.html", message='Hello World!')

@app.route('/page2')
def suite():
    return render_template("page2.html")

@app.route('/test-formulaire')
def enregistrement():
    return render_template("formulaire.html")

@app.route('/retour-formulaire', methods=['POST'])
def text_box():
    text_first_name = request.form['first_name']
    text_last_name = request.form['last_name']
    text_sex = request.form['sex']
    text_pseudo = request.form['pseudo']
    return render_template("bienvenue.html",text_first_name,text_last_name, text_sex, text_pseudo)

if __name__ == "__main__":
    app.run()
    
    