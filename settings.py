class Config:
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:C1z9w9906250618@127.0.0.1:3306/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    ENV = "development"


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
