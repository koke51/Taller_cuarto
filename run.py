from app import app
#Route = decorador
@app.route("/")
def hello_world():
    return "<p>Hola, Mundo</p>"

#si está aquí el programa principal, ejecutelo
if __name__ == "__master__":
    app.run(debug = True)

