from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'
@app.route('/about/<username>')
def about_page(username):

    return f'<p>This is about page of {username}</p>'
if __name__ == '__main__':
    app.run(debug=True)
