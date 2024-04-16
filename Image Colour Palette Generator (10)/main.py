from flask import Flask, render_template, request
from image_processing import get_top_colors

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file', 400

    top_colors = get_top_colors(file)
    return render_template('result.html', top_colors=top_colors)

if __name__ == '__main__':
    app.run(debug=True)
