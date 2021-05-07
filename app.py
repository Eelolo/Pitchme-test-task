from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'

@app.route('/')
def index():
    return 'test'

if __name__ == '__main__':
    app.run(debug=True)
