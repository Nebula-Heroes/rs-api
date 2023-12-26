from . import router, engine, users_interactions_table
from sqlalchemy import text, MetaData, Table, insert
import datetime
from unidecode import unidecode
import numpy as np
from fastapi import Query, HTTPException, status
from datetime import datetime
from . import popularity_worker, content_based_worker, hybrid_worker

event_type_strength = {
    'VIEW': 1.0,
    'LIKE': 2.0, 
    'BOOKMARK': 2.5, 
    'FOLLOW': 3.0,
    'COMMENT CREATED': 4.0,  
}


@router.get("/api/interaction")
def load_user_interaction(user_id: int = Query(0),
                           event_type: str = Query(None),
                           content_id: str = Query(0),
                           session_id: str = Query(0),
                           user_agent: str = Query(None),
                           user_region: str = Query(None),
                           user_country: str = Query(None)):

    try:
        int(content_id)
        int(session_id)
    except:
        return {"message": "Error: content_id and session_id must be integer"}
    
    VIEW_EVENTS = ['VIEW', 'LIKE', 'BOOKMARK', 'FOLLOW', 'COMMENT CREATED', 'FOLLOW']
    if event_type not in VIEW_EVENTS:
        return {"message": "Error: event_type must be in " + str(VIEW_EVENTS)}

    insert_query = insert(users_interactions_table).values(
        timestamp= int(datetime.now().timestamp()),
        eventtype = event_type,
        contentid = content_id,
        personid = user_id,
        sessionid = session_id,
        useragent = user_agent,
        userregion = user_region,
        usercountry = user_country
    )
    conn = engine.connect()
    try:
        conn.execute(insert_query)
        conn.commit()
        
        event_strength = event_type_strength[event_type]
        new_row = [99999,
                   int(datetime.now().timestamp()),
                   event_type,
                   int(content_id),
                   int(user_id),
                   int(session_id),
                   user_agent,
                   user_region,
                   user_country,
                   event_strength]
        
        content_based_worker.update_model(person_id = user_id, new_row = new_row)
        hybrid_worker.update_model(person_id = user_id, new_row = new_row)
        
        return {"message": "Data inserted successfully"} 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        conn.close()

