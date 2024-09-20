from flask import Flask

app = Flask(__name__)
@app.route('/')
def saludo():
    return '''<h1>Hola desde Flask</h1>
            <h2>Hola desde Flask</h2>  
            <h3>Hola desde Flask</h3>'''

if __name__ == '__main__':
    app.run(debug=True)