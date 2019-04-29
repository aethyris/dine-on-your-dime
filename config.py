import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://2lmZ1LfsCc:RUMm0cneDj@remotemysql.com/2lmZ1LfsCc"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very secret much wow'
