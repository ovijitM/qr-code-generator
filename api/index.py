from flask import Flask, request, render_template, send_file, url_for, jsonify
import qrcode
import io
import os
import base64
from datetime import datetime

app = Flask(__name__, template_folder='../templates')

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
            
            # Save to BytesIO for serverless environment
            img_io = io.BytesIO()
            img.save(img_io, 'PNG')
            img_io.seek(0)
            
            # Convert to base64 for display
            img_base64 = base64.b64encode(img_io.getvalue()).decode()
            qr_data_url = f"data:image/png;base64,{img_base64}"
            
            return render_template('index.html', 
                                 qr_code=qr_data_url,
                                 url=url)
        except Exception as e:
            return render_template('index.html', error=f"Error generating QR code: {str(e)}")
    
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        url = request.form.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Basic URL validation
        if not (url.startswith('http://') or url.startswith('https://')):
            url = 'https://' + url
        
        img = qrcode.make(url)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        
        return send_file(buf, mimetype='image/png', as_attachment=True, 
                        download_name=f'qr_code_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

# For Vercel deployment
if __name__ == '__main__':
    app.run(debug=False)
