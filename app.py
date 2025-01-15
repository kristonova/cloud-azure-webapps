from flask import Flask
import integral

app = Flask(__name__)


@app.route('/integralapp/<lower>/<upper>')
def show_user_profile(lower, upper):
    result = integral.looper(float(lower), float(upper))
    return f'User {result}'
