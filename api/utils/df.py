import pandas as pd
def change_type_articles(df):
    articles_data_types = {
        'contentId': int,
        'authorPersonId': int,
        'authorSessionId': int,
    }
    
    df = df.astype(articles_data_types)
    return df

def change_type_interactions(df):
    interactions_data_types = {
        'contentId': int,
        'personId': int,
        'sessionId': int,
    }
    
    df = df.astype(interactions_data_types)
    return df