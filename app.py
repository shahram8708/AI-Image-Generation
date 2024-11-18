from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'API_Key'
CX = 'CX'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    term = request.args.get('term')
    if not term:
        return jsonify([])
    else:
        google_api_url = f"https://www.googleapis.com/customsearch/v1?q={term}&cx={CX}&key={API_KEY}&searchType=image&safe=active"
        response = requests.get(google_api_url)
        if response.status_code == 200:
            data = response.json()
            images = [item['link'] for item in data.get('items', [])]
            return jsonify(images)
        else:
            return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
