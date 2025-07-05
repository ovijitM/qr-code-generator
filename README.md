# QR Code Generator Web Application

A modern, responsive web application that allows users to generate QR codes from URLs. Built with Flask and qrcode library, featuring a beautiful UI and mobile-first design.

![QR Code Generator](https://img.shields.io/badge/QR-Code%20Generator-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

- 🎯 Generate QR codes from any URL
- 📱 Fully responsive design (mobile-first)
- 💾 Download QR codes as PNG images
- 🎨 Modern and clean user interface
- ⚡ Fast and efficient QR code generation
- 🔒 No data storage - privacy focused
- 🌐 Works on all modern browsers
- 📦 Easy to deploy and maintain

## 🚀 Live Demo

Visit the live demo: [QR Code Generator](https://your-demo-url.com)

## 🛠️ Technology Stack

- **Backend:**
  - Python 3.8+
  - Flask 2.3.3
  - qrcode 7.4.2
  - Pillow 9.5.0

- **Frontend:**
  - HTML5
  - Tailwind CSS
  - Responsive Design
  - Mobile-first approach

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

2. Create and activate a virtual environment:
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter a URL in the input field and click "Generate QR Code"

4. Download the generated QR code by clicking the "Download QR Code" button

## 📱 Mobile Support

The application is fully responsive and optimized for mobile devices:
- Touch-friendly interface
- Mobile-optimized input fields
- Responsive QR code display
- Easy-to-tap buttons
- Proper viewport scaling
- iOS and Android compatible

## 🔧 Configuration

The application can be configured by modifying the following parameters in `app.py`:

- QR Code version
- Error correction level
- Box size
- Border size
- Colors

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [qrcode](https://github.com/lincolnloop/python-qrcode)
- [Tailwind CSS](https://tailwindcss.com/)
- [Pillow](https://python-pillow.org/)

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/qr-code-generator](https://github.com/yourusername/qr-code-generator) 