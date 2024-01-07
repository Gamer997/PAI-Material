from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def show_all_data():
    conn = sqlite3.connect('cricket.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cricket_data')
    data = cursor.fetchall()
    conn.close()
    return render_template('test_file.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
