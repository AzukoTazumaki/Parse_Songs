from flask import Flask, render_template, request

project = Flask(__name__)


@project.route('/')
def index():
    return render_template('welcome.html')


if __name__ == '__main__':
    project.run(debug=True)