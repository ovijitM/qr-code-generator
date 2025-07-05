import os
import qrcode
from io import BytesIO
from flask import Flask, render_template, request, send_file, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            url = request.form.get('url')
            if not url:
                return render_template('index.html', error="Please enter a valid URL")
            
            # Basic URL validation
            if not (url.startswith('http://') or url.startswith('https://')):
                url = 'https://' + url
            
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
                                 url=url,
                                 filename=filename)
        except Exception as e:
            return render_template('index.html', error=f"Error generating QR code: {str(e)}")
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    try:
        file_path = os.path.join('static', 'temp', filename)
        if os.path.exists(file_path):
            return send_file(file_path,
                            as_attachment=True,
                            download_name=filename)
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True) 