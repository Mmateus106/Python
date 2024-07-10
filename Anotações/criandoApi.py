from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}'

@app.route('/status/')
def get_status():
    return {"status" : "OK"}

@app.route('/status_/')
def get_status_():
    return jsonify({"status" : "OKOKOKOK"})

@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    return f'A soma de {n1} com {n2} é {n1+n2}'

                        #2.7
@app.route('/rev/<float:revNo>')
def revision(revNo):
    #return 'Revision No %f' %revNo
    return f'Revision No {revNo}'


#principal
if __name__ == "__main__":
    app.run()