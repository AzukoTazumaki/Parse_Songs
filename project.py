from flask import Flask, render_template, request
from parse import Songs

project = Flask(__name__)


@project.route('/')
def index():
    popular_songs = Songs('').popular_songs()[0]
    new_songs = Songs('').popular_songs()[1]
    top_songs = Songs('').popular_songs()[2]
    return render_template('content.html', popular_songs=popular_songs, new_songs=new_songs, top_songs=top_songs)


@project.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'GET':
        form_data = request.args.getlist('search')[0]
        dict_data = Songs(form_data).search_artists()
        return render_template('search_artists.html', data=dict_data, request_search=form_data)
    return index()


if __name__ == '__main__':
    project.run(debug=True)
