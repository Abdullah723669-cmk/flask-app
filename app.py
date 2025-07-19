from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
     return """
    <html>
        <head><title>My App</title></head>
        <body>
            <h1 style="color:red; background-color:green; text-align:center">Hello, Abdullah!</h1>
            <p>This HTML is written directly in Python!</p>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

