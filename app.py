from flask import Flask, request, redirect, url_for, render_template
import QR_code_generator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('qr-code.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        url = request.form['url']
        QR_code_generator.generateQRCode(url)
        return redirect(url_for('success'))
    except KeyError:
        return "Error: 'url' field is missing in the form data", 400


if __name__ == '__main__':
    app.run(port=8000, debug=True)
