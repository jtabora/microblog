from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'JTAb'}
    posts = [
        {'author': {'username':'John'}
        , 'body': 'Bea day in Seattle'
        }
        , {
        'author': {'username': 'Susan'}
        , 'body': 'Go to the movies'
        }
        , {
        'author': {'username': 'Karen'}
        , 'body': 'Such a Karen'
        }
        , {
        'author': {'username': 'Mia'}
        , 'body': 'Thanksgiving ham'
        }
    ]
    return render_template('index.html', user=user, title='My first microblog', posts=posts)
