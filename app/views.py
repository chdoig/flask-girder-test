"""Main views for memex-explorer application"""
from __future__ import absolute_import, division, print_function

#  IMPORTS
# =========

# Standard Library
# ----------------

import os
import re
import logging
import json
import datetime as dt
import subprocess
import traceback
import shutil

# Third-party Libraries
# ---------------------

from flask import (redirect, flash, render_template, request, url_for,
                   send_from_directory, jsonify, session, abort)

# Local Imports
# -------------

from . import app

from .config import ADMINS, DEFAULT_MAIL_SENDER, BASEDIR, GIRDER_STATIC_DIR

from .forms import ContactForm
from .mail import send_email

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def application_error(e):
    # TODO
    # http://flask.pocoo.org/docs/0.10/errorhandling/#application-errors

    # sender = DEFAULT_MAIL_SENDER
    # send_email(subject=subject, sender=sender, recipients=ADMINS, text_body=text_body, html_body=text_body)
    return render_template('500.html'), 500


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(BASEDIR, 'static'),
                               'favicon.ico', mimetype='image/x-icon')


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/about/')
def about_page():
    return render_template('about.html')

