# currency.py file

from flask import Flask

app = Flask(__name__)


def is_value_in_array(arr, value):
    return value in arr

