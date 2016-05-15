from sqlalchemy_wrapper import SQLAlchemy

from app.config.base import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(SQLALCHEMY_DATABASE_URI, echo=True, record_queries=True)