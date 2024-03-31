import datetime
import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Category_id(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'category_id'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    job_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    category_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
