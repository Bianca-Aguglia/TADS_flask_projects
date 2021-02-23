import sqlite3

with sqlite3.connect('blog.db') as connection:
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                        (id INTEGER PRIMARY KEY,
                         title TEXT NOT NULL,
                         body TEXT NOT NULL)''')
    
    posts = [('First post', 'I\'m trying out this new blog.'),
             ('Python', 'Python is fun.')]
    
    cursor.executemany('INSERT INTO posts VALUES (null,?,?)', posts)