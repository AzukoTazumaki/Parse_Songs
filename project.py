from flask import Flask, render_template, request
from parse import Songs

project = Flask(__name__)


@project.route('/')
def index():
    popular_songs = Songs('').popular_songs()[0]
    new_songs = Songs('').popular_songs()[1]
    top_songs = Songs('').popular_songs()[2]
    return render_template('index.html',
                           popular_songs=popular_songs,
                           new_songs=new_songs,
                           top_songs=top_songs)


if __name__ == '__main__':
    project.run(debug=True)