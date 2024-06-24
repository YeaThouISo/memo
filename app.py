from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection, init_db

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    memos = conn.execute('SELECT * FROM memos').fetchall()
    conn.close()
    return render_template('index.html', memos=memos)

@app.route('/add', methods=('GET', 'POST'))
def add_memo():
    if request.method == 'POST':
        content = request.form['content']
        tags = request.form['tags']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO memos (content, tags) VALUES (?, ?)', (content, tags))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('add_memo.html')

@app.route('/search', methods=('GET', 'POST'))
def search_memo():
    if request.method == 'POST':
        tag = request.form['tag']
        conn = get_db_connection()
        memos = conn.execute('SELECT * FROM memos WHERE tags LIKE ?', ('%' + tag + '%',)).fetchall()
        conn.close()
        return render_template('index.html', memos=memos)
    
    return render_template('search_memo.html')

if __name__ == '__main__':
    init_db()  # 初回実行時にデータベースを初期化
    app.run(debug=True)
