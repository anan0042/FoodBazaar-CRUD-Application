"""
This script runs the Assignment4 application using a development server.
Name:Rohan Aanand
Date:2018-11-10
"""

from os import environ
from FinalProject import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
