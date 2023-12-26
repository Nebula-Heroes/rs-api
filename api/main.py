
import os
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy import MetaData, Table, Column, Integer, String, DECIMAL, text
import pandas as pd

from .utils.df import *
from .orm.table import *
from .models.build import *

QUERY_LIMIT = 100000
conn = engine.connect()
articles_query = conn.execute(articles_table.select().limit(100000))
articles_data = [row for row in articles_query]
interactions_query = conn.execute(users_interactions_table.select().limit(QUERY_LIMIT))
interactions_data = [row for row in interactions_query]
conn.close()


articles_df = pd.DataFrame(articles_data, columns=['timestamp', 'eventType', 'contentId', 'authorPersonId', 
                                                   'authorSessionId', 'authorUserAgent', 'authorRegion', 
                                                   'authorCountry', 'contentType', 'url', 'title', 'text', 'lang'],)
articles_df = change_type_articles(articles_df)

interactions_df = pd.DataFrame(interactions_data, columns=['id', 'timestamp', 'eventType', 'contentId', 'personId', 'sessionId', 'userAgent', 'userRegion', 'userCountry'])
interactions_df = change_type_interactions(interactions_df)
hybrid_worker = HybridWorker(articles_df, interactions_df)
popularity_worker = PoppularityWorker(interactions_df, articles_df)
content_based_worker = ContentBasedWorker(articles_df, interactions_df)

from .routers import router as machine_router

app = FastAPI()
app.include_router(machine_router)

@app.get("/")
def root():
    """
    Returns a greeting message indicating that the RS API is up and running.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {
        "message": "Welcome to the RS API. It is currently running and ready to serve requests.",
        "version": "1.0.0"  
    }