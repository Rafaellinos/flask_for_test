from flask import Flask
from flask import jsonify
from flask import request

from RFID_READER import reader

app = Flask(__name__)

@app.route('/')
def index():
    return "Server running..."

@app.route('/get_class', methods=['GET'])
def login(**kw):
    #http://127.0.0.1:5000/get_class   /login/userid=2
    #user_id = request.args.get('id',False)
    print(request.data) # get data from payload
    subject = request.form.get('ha') # from posted data
    print(subject)
    # subject = request.args.get('ha') # from query params (on headers)
    """
        receive: subject, body
        return : classificação
    """

    return jsonify({'class': 'infra'})

if __name__ == '__main__':
    app.run(debug=True)