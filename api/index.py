from flask import Flask, request, render_template, send_file
import qrcode
import io

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']
    img = qrcode.make(url)

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

# Vercel will look for "app" variable
