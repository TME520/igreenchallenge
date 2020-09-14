from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def server_running():
    return "Server is running."

@app.route('/version', methods=['GET'])
def version():
    version_data = {
        'myapplication':
            {'version': '1.0',
            'lastcommitsha': 'unknown',
            'description': 'Test app for iGreen tech challenge.'}
        }
    return jsonify(version_data)

if __name__ == '__main__':
    app.run()
