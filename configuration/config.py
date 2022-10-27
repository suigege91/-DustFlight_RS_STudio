DB_SERVER_USER = "root"
DB_SERVER_PASS = "DustFlight_DB_Pass_01"
DB_SERVER_HOST = "127.0.0.1"
DB_SERVER_PORT = "3306"
DB_SERVER_NAME = "dustflight_rs_studio"
DB_SERVER_ENCODING = "utf8"
DB_SERVER_CONNECTION_URL = "mysql+pymysql://%s:%s@%s:%s/%s?charset=%s" % (
    DB_SERVER_USER, DB_SERVER_PASS, DB_SERVER_HOST, DB_SERVER_PORT, DB_SERVER_NAME, DB_SERVER_ENCODING)


class Configuration(object):
    pass


class Configuration_Development(Configuration):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_SERVER_CONNECTION_URL


class Configuration_Test(Configuration):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_SERVER_CONNECTION_URL


class Configuration_Product(Configuration):
    SQLALCHEMY_DATABASE_URI = DB_SERVER_CONNECTION_URL
    DEBUG = False
