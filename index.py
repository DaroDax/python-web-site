from flask import Flask, render_template

app = Flask(__name__) #Indica el archivo principal

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about') #Asi se crean las rutas
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) #En pruebas para que se reinicie cada vez que cambie