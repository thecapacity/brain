from flask import Flask

def init_db():
    return

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()

