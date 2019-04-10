from flask import Flask

app = Flask(__name__)

@app.route("/bit", methods=["GET"])
def index():
    return "4 BIT ADDITION"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)
