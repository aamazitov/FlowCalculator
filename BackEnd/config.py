import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "very-very-very-secret"
    DB_USERNAME = os.environ.get("DB_USERNAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@localhost/flowcalcdb".format(
        username=DB_USERNAME,
        password=DB_PASSWORD
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
