from flask import Flask
from flask_cors import CORS
from decimal import Decimal, getcontext

app = Flask(__name__)
CORS(app)


def calc_pi():
    return sum(1 / Decimal(16) ** k *
        (Decimal(4) / (8 * k + 1) -
         Decimal(2) / (8 * k + 4) -
         Decimal(1) / (8 * k + 5) -
         Decimal(1) / (8 * k + 6)) for k in range(100))


@app.route('/')
def dashboard():
    getcontext().prec = 10000000
    return str(calc_pi())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
