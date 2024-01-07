from flask import Flask , render_template
app = Flask(__name__)
posts = [

    {'author': 'Ali Khan',
    'title': 'Post Lumber 1',
    'content': 'This is first post',
    'date': 'May 20, 2019'},
    {'author': 'Kamaludin Shah',
    'title': 'I am under the water',
    'content': 'I love to suffer',
    'date': 'June 12, 2021'

    }
]
@app.route("/")
@app.route("/index")
def test():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html', posts = posts)

if __name__ == '__main__':
    app.run(debug=True)
