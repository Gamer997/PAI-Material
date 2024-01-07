@app.route('/sorted_data')
def show_sorted_data():
    conn = sqlite3.connect('cricket.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cricket_data ORDER BY Bowler_Id')
    sorted_data = cursor.fetchall()
    conn.close()
    return render_template('test_file.html', data=sorted_data)
