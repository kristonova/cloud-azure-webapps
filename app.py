from flask import Flask
import math

app = Flask(__name__)

def numerical_integration(lower, upper, N):
    width = (upper - lower) / N
    total_area = 0.0
    for i in range(N):
        x = lower + i * width
        height = abs(math.sin(x))
        total_area += height * width
    return total_area

def looper(lower: float, upper: float) -> list:
    results = []
    for N in [1, 10, 100, 100, 1000, 10000, 100000, 1000000]:
        results.append(numerical_integration(lower, upper, N))
    return results

@app.route('/integralapp/<lower>/<upper>')
def show_user_profile(lower, upper):
    result = looper(float(lower), float(upper))
    return f'User {result}'
