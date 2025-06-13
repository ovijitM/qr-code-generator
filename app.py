import os
import qrcode
from io import BytesIO
from flask import Flask, render_template, request, send_file, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code = None
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
            
            # Save the image to a BytesIO object
            img_io = BytesIO()
            img.save(img_io, 'PNG')
            img_io.seek(0)
            
            # Generate a unique filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'qr_code_{timestamp}.png'
            
            # Save the QR code temporarily
            temp_path = os.path.join('static', 'temp', filename)
            os.makedirs(os.path.dirname(temp_path), exist_ok=True)
            img.save(temp_path)
            
            return render_template('index.html', 
                                 qr_code=url_for('static', 
                                               filename=f'temp/{filename}'),
                                 url=url)
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join('static', 'temp', filename),
                    as_attachment=True,
                    download_name=filename)

if __name__ == '__main__':
    app.run(debug=True) 