import sqlalchemy
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Category(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'category'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    category = sqlalchemy.Column(sqlalchemy.String, nullable=True)
