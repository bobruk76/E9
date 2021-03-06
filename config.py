import os


class Config:
    SECRET_KEY = str(os.environ.get("SECRET_KEY",os.urandom(32)))
    PORT = os.getenv('PORT', 5000)
    SQLALCHEMY_DATABASE_URI = str(os.environ.get("DATABASE_URL",
                                                 "postgresql://e9user:e9user@localhost:5432/e9"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

