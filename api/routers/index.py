from . import router, engine, users_interactions_table, articles_table
from . import popularity_worker, content_based_worker, hybrid_worker

from sqlalchemy import text
import datetime
from unidecode import unidecode
import numpy as np
import json 
from fastapi import Query

@router.get("/api/is_old_user")
def is_user_in_db(user_id):
    is_user_in_db = users_interactions_table.select().where(users_interactions_table.c.personid == str(user_id))
    conn = engine.connect()
    is_user_in_db = conn.execute(is_user_in_db)
    is_user_in_db = [row for row in is_user_in_db]
    conn.close()
    return len(is_user_in_db) > 0

@router.get("/api/recommend_popularity_model")
def recommend_popularity_model():
    result = popularity_worker.recommend()
    result = json.loads(result.to_json(orient = 'records'))
    return result

@router.get("/api/recommend_content_based_model")
def recommend_content_based_model(user_id: int = Query(0)):
    result = content_based_worker.recommend(user_id = user_id)
    result = json.loads(result.to_json(orient = 'records'))
    return result


@router.get("/api/recommend_homepage_articles")
def get_homepage_articles(user_id: int = Query(0)):

    if not is_user_in_db(user_id):
        return recommend_popularity_model()
    
    result = hybrid_worker.recommend(user_id = user_id)
    result = json.loads(result.to_json(orient = 'records'))

    return result

@router.get("/api/recommend_followed_articles")
def get_followed_articles(author_person_id: int = Query(0),
                          limit: int = Query(5)):
    
    articles = articles_table.select().where(articles_table.c.authorpersonid == str(author_person_id)).limit(limit)
    conn = engine.connect()
    articles = conn.execute(articles)
    articles = [row for row in articles]
    conn.close()
    if len(articles) == 0:
        return None
    for i in range(len(articles)):
        articles[i] = {
            'contentId': articles[i][2],
            'authorPersonId': articles[i][3],
            'url': articles[i][9],
            'title': articles[i][10],
            # 'text': articles[i][11],
            'lang': articles[i][12]
        }
    return articles

@router.get("/api/recommend_liked_articles")
def get_liked_articles(content_id: int = Query(0)):
    
    result = content_based_worker.get_similar(contentid = content_id)
    print(result)
    result = json.loads(result.to_json(orient = 'records'))
    return result

@router.get("/api/recommend_related_articles")
def get_related_articles(user_id: int = Query(0)):
        
    if not is_user_in_db(user_id):
        return recommend_popularity_model()
    
    result = content_based_worker.recommend(user_id = user_id)
    result = json.loads(result.to_json(orient = 'records'))
    return result

@router.get("/api/get_article")
def get_article(content_id: int = Query(0)):
    article = articles_table.select().where(articles_table.c.contentid == str(content_id))
    conn = engine.connect()
    article = conn.execute(article)
    article = [row for row in article]
    conn.close()
    if len(article) == 0:
        return None
    article = article[0]
    data = {
        'timestamp': article[0],
        'eventType': article[1],
        'contentId': article[2],
        'authorPersonId': article[3],
        'authorSessionId': article[4],
        'authorUserAgent': article[5],
        'authorRegion': article[6],
        'authorCountry': article[7],
        'contentType': article[8],
        'url': article[9],
        'title': article[10],
        'text': article[11],
        'lang': article[12]
    }
    return data

