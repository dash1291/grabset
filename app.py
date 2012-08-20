import os.path
import shutil
import sys

# Configs #
APP_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(APP_DIR, 'lib'))
TEMPLATES_PATH = os.path.join(APP_DIR, 'templates')
SITE_PREFIX = 'http://localhost:8000'
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(APP_DIR, 'static')

from flask import Flask, request, redirect
from jinja2 import Template, Environment, FileSystemLoader
from flickr import Grabber

app = Flask(__name__)
env = Environment(loader=FileSystemLoader(TEMPLATES_PATH))

@app.route('/')
def index():
    template = env.get_template('index.html')
    ctx = {'STATIC': STATIC_URL}
    rendered = template.render(ctx)
    return rendered

@app.route('/download/<path:seturl>')
def download_set(seturl):
    g = Grabber(seturl)
    setid = g.grabSet('tmp/')
    shutil.make_archive(STATIC_PATH + '/archives/' + setid, 'zip',
            'tmp/' + setid + '/')
    return SITE_PREFIX + STATIC_URL + 'archives/' + setid + '.zip'

app.run(port=8000, debug=True)
