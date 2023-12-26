from sqlalchemy import MetaData, Table, Column, Integer, String, DECIMAL, text
import os
import sqlalchemy

POSTGRES_CONNECTION_STRING = os.getenv('POSTGRES_CONNECTION_STRING')
engine = sqlalchemy.create_engine(POSTGRES_CONNECTION_STRING)

metadata = MetaData()
users_interactions_table = Table(
    'users_interactions',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('timestamp', Integer),
    Column('eventtype', String),
    Column('contentid', String),
    Column('personid', String),
    Column('sessionid', String),
    Column('useragent', String),
    Column('userregion', String),
    Column('usercountry', String)
)

articles_table = Table(
    'articles',
    metadata,
    Column('timestamp', Integer),
    Column('eventtype', String),
    Column('contentid', String, primary_key=True),
    Column('authorpersonid', String),
    Column('authorsessionid', String),
    Column('authoruseragent', String),
    Column('authorregion', String),
    Column('authorcountry', String),
    Column('contenttype', String),
    Column('url', String),
    Column('title', String),
    Column('text', String),
    Column('lang', String(5))
)
metadata.create_all(engine)
