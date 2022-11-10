from led_demo import led_set, led_set_all
from flask import Flask, request
from serial import Serial

ser = Serial('COM6')
app = Flask(__name__)


def parse_data(data):
    if 'red' in data and (data['red'] > 255 or data['red'] < 0):
        return (data, "Red out of bounds")
    elif 'red' not in data:
        data['red'] = 0

    if 'green' in data and (data['green'] > 255 or data['green'] < 0):
        return (data, "Green out of bounds")
    elif 'green' not in data:
        data['green'] = 0

    if 'blue' in data and (data['blue'] > 255 or data['blue'] < 0):
        return (data, "Blue out of bounds")
    elif 'blue' not in data:
        data['blue'] = 0

    if 'white' in data and (data['white'] > 255 or data['white'] < 0):
        return (data, "White out of bounds")
    elif 'white' not in data:
        data['white'] = 0

    return (data, None)


@app.route('/')
def root():
    return 'Welcome to the world of LED'


@app.route('/led')
def led():
    data = request.get_json()

    if 'led_id' not in data:
        return '400 Bad Request: Missing led_id', 400

    data, error = parse_data(data)

    if error is not None:
        return f'400 Bad Request: {error}', 400

    led_set(ser, int(data['led_id']),
            int(data['red']), int(data['green']), int(data['blue']), int(data['white']))

    return 'OK'


@app.route('/strip')
def strip():
    data = request.get_json(silent=True)

    if data is None:
        data = dict()

    data, error = parse_data(data)

    if error is not None:
        return f'400 Bad Request: {error}', 400

    led_set_all(ser, 30, int(data['red']),
                int(data['green']), int(data['blue']), int(data['white']))

    return 'OK'
