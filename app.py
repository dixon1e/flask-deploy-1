import os
import logging
import config
from api import api
from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from gevent import pywsgi

# Following import is where db = SQLAlchemy() happens
# N.B. it is initialized with app below
# TODO: Inits are messy and not good practice
from models import db

logging.basicConfig(level=logging.DEBUG,
                   format='[%asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object('config')
    api.init_app(app)
    # initialize SQLAlchemy
    db.init_app(app)
    # prepare for db migration
    migrate = Migrate(app, db)



    # define hello world page
    @app.route('/')
    def hello_world():
        return render_template('/index.html')

    @app.route('/aboutus')
    def about_us():
        return render_template('/aboutus.html')

    @app.route('/contactus')
    def contact_us():
        return render_template('/contactus.html')

    @app.route('/smartvenue')
    def smartventue():
        return render_template('/smartvenue.html')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=False)
