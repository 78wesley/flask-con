from dotenv import load_dotenv
from flask import Flask
from flask_crontab import Crontab
import datetime
import os
from logging.config import dictConfig

app = Flask(__name__)
crontab = Crontab(app)

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {"wsgi": {"class": "logging.StreamHandler", "stream": "ext://flask.logging.wsgi_errors_stream", "formatter": "default"}},
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)


def ensure_crontabs():
    # Ensure the crontabs are added; avoid duplicates by clearing and re-adding.
    os.system(".venv/bin/flask crontab remove")
    os.system(".venv/bin/flask crontab add")


def create_app():
    load_dotenv()
    ensure_crontabs()
    crontab.init_app(app)
    return app


@app.route("/")
def home():
    return "Welcome to the Flask Cron Job Example!"


@crontab.job(minute="*")
def scheduled_task():
    with app.app_context():
        app.logger.info("Task running at {0}".format(datetime.datetime.now()))
