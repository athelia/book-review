from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

import os
import requests

from model import connect_to_db, db, User, Review, Book

app = Flask(__name__)
app.config.from_pyfile('flaskconfig.cfg')

app.jinja_env.undefined = StrictUndefined



if __name__ == '__main__':

    app.debug = True
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)

    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0')