from flask import Flask, request, render_template, send_file, url_for
import qrcode
import io
import os
from datetime import datetime

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            
            # Create an image from the QR Code
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save to BytesIO for Vercel (serverless environment)
            img_io = io.BytesIO()
            img.save(img_io, 'PNG')
            img_io.seek(0)
            
            # For Vercel, we'll return the image directly or render with base64
            import base64
            img_base64 = base64.b64encode(img_io.getvalue()).decode()
            qr_data_url = f"data:image/png;base64,{img_base64}"
            
            return render_template('index.html', 
                                 qr_code=qr_data_url,
                                 url=url)
    
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
