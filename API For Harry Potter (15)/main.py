from flask import Flask, render_template
import requests

app = Flask(__name__)

API_BASE_URL = 'https://www.potterapi.com/v1/'
API_KEY = 'df8234c0e5726f1b9a9b17f14d8a48a2'

@app.route('/')
def index():
    endpoint = f'{API_BASE_URL}characters'
    params = {'key': API_KEY}
    
    response = requests.get(endpoint, params=params)
    
    if response.status_code == 200:
        characters = response.json()
        return render_template('index.html', characters=characters)
    else:
        return "Error fetching data from API"

if __name__ == '__main__':
    app.run(debug=True)
