import json
from flask import Flask, render_template

from config import load_secret_key
from forms import WayForm
from rooms import Room


app = Flask(__name__)
app.config.from_mapping({'SECRET_KEY': load_secret_key()})

rooms = Room()
rooms.set_location()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/adventure/', methods=['get', 'post'])
def adventure():
    form_way = WayForm()
    return render_template('adventure.html', form_way=form_way, location=rooms.location)


@app.route('/forma', methods=['get', 'post'])
def forma():

    form_way = WayForm()
    way = form_way.way.data
    num = form_way.number_steps.data
    rooms.movement(way, num)
    return json.dumps({'location': rooms.location, 'wall': rooms.wall})


if __name__ == '__main__':
    """Чтобы активировать режим отладки 
    set FLASK_DEBUG=1 в командной строке ИЛИ export FLASK_DEBUG=1 в терминале"""
    app.run(host='127.0.0.1', port=5000, debug=True)  # debug=True)

