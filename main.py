from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/main', methods=['GET'])
def modify_url():
    url = request.args.get('url')
    if url:
        modified_url = "loadstring(game:HttpGet(\"{}\"))()".format(url)
        return modified_url
    else:
        return "Please provide a url! 😠"

if __name__ == '__main__':
    app.run()
