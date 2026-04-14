from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>🐳 Hello from Docker!</h1>
            <p>This app is built and published by <strong>ameso</strong></p>
            <p>Running on Flask inside a Docker container</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)