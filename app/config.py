import os
import sys

BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Project
# -------

TITLE = 'TOPIC SPACE'
ADMINS = []

# Server
# ------

HOST = '0.0.0.0'
PORT = 5000
DEBUG = False
DEMO = True

# Database
# --------

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'resources/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')

# Email
# -----

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEBUG = True
DEFAULT_MAIL_SENDER = MAIL_USERNAME

# Girder
# ------

GIRDER_STATIC_DIR = os.path.join(BASEDIR, 'static/girder')