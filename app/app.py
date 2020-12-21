from flask import Flask, request, Response
import logging
import pyfiglet
import requests
import os

try:
    app = Flask(__name__)

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
except Exception as e:
    logging.exception("Error at startup")


@app.route('/ping')
def ping():
    """
    Ping the endpoint
    :return:
    """
    logging.info('/ping')
    return "ping Ok"


def get_port():
    """
    Retrieves port
    :return:
    """
    return int(os.environ.get("PORT", 5000))


if __name__ == '__main__':
    ascii_banner = pyfiglet.figlet_format("1, 2, 3 Tutorial")
    print(ascii_banner)

    logging.info('Starting up')

    app.run(debug=True, port=get_port(), host='0.0.0.0')