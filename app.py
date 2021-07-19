#cursor.execute('''CREATE TABLE IF NOT EXISTS posts (id integer primary key AUTOINCREMENT, title text, description text, date text)''')

import sqlite3

from flask import Flask, request, render_template, redirect

from datetime import date




app = Flask(__name__)







# main page which shows all posts,

# and redirects to the main page

@app.route('/main')

def main():

    connection = sqlite3.connect('blog.sqlite3')

    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM posts''')

    posts = cursor.fetchall()

    return render_template('index.html', posts=posts)







# page which writes title and description of posts,

# and redirects to the main page

@app.route('/title/description')

def title_description():

    post_date = date.today()

    connection = sqlite3.connect('blog.sqlite3')

    cursor = connection.cursor()

    title = request.args.get('title')

    description = request.args.get('description')

    cursor.execute('''INSERT INTO posts (title, description, date) VALUES (?, ?, ?)''', (title, description, post_date))

    connection.commit()

    connection.close()

    return redirect('/main')







# page which updates title&description of the posts,

# and redirects to the main page

@app.route('/update')

def update():

    connection = sqlite3.connect('blog.sqlite3')

    cursor = connection.cursor()

    title_to_change = request.args.get('title')

    descr_to_change = request.args.get('description')

    post_id = request.args.get('id')

    cursor.execute('''UPDATE posts SET (title, description) = (?, ?) WHERE id = ? ''', (title_to_change, descr_to_change, post_id))

    connection.commit()

    connection.close()

    return redirect('/main')







# page which deletes posts by id,

# and redirects to the main page

@app.route('/delete')

def delete():

    connection = sqlite3.connect('blog.sqlite3')

    cursor = connection.cursor()

    id_to_delete = request.args.get('id')

    cursor.execute('''DELETE FROM posts WHERE id = ? ''', id_to_delete)

    connection.commit()

    connection.close()

    return redirect('/main')







if __name__ == '__main__':

    app.run(debug=True)
