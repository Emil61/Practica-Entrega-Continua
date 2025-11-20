from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo desde CI/CD"

if __name__ == "__main__":
    # host='0.0.0.0' para que Docker pueda exponerlo
    app.run(host="0.0.0.0", port=5000)
