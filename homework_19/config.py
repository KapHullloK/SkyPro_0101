class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    PWD_HASH_SALT = b'hgjd35jwdd23b'
    PWD_HASH_ITERATIONS = 100_000
    ALGO = 'HS256'
