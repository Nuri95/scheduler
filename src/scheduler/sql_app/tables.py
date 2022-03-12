import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.Text)
    email = sqlalchemy.Column(sqlalchemy.Text, unique=True)
    password_hash = sqlalchemy.Column(sqlalchemy.Text)

    tasks = relationship('Task')


class Task(Base):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    header = sqlalchemy.Column(sqlalchemy.Text)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

