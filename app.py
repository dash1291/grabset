import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from flask import Flask
from jinja2 import Template, Environment, FileSystemLoader
import flickr

app = Flask(__name__)

templates_path = os.path.join(os.path.dirname(__file__), 'templates')
STATIC = '/static/'
env = Environment(loader=FileSystemLoader(templates_path))

@app.route('/')
def index():
    template = env.get_template('index.html')
    ctx = {'STATIC': STATIC}
    rendered = template.render(ctx)
    return rendered

@app.route('/download')
def download_set():
    return 'here is your download link'

app.run(port=8000)
