from flask import Flask, render_template, request, redirect, url_for
import os
from plag import jplag_light

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/organizer')
def organizer():
    return render_template('organizer.html')

@app.route('/participant')
def participant():
    return render_template('participant.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('upload_success'))
    return render_template('upload.html')

@app.route('/upload_success')
def upload_success():
    return "File uploaded successfully!"

@app.route('/results')
def results():
    # run plagiarism check
    jplag_light(app.config['UPLOAD_FOLDER'])
    return "Plagiarism check complete! Check terminal for results."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
