from .popularity_model import PopularityRecommender, event_type_strength as popularity_event_type_strength
from .hybrid_model import HybridRecommender
from .content_based_model import ContentBasedRecommender, event_type_strength as content_based_event_type_strength

class PoppularityWorker:
    def __init__(self, interactions_df, articles_df):
        self.interactions_df = interactions_df
        self.articles_df = articles_df
        self.popularity_recommender_model = PopularityRecommender(self.interactions_df, self.articles_df, popularity_event_type_strength)
    
    def recommend(self, topn = 10):
        return self.popularity_recommender_model.recommend_items(topn = topn, verbose = True)
    
class ContentBasedWorker:
    def __init__(self, articles_df, interactions_df):
        self.articles_df = articles_df
        self.interactions_df = interactions_df
        self.content_based_recommender_model = ContentBasedRecommender(self.articles_df, self.interactions_df, content_based_event_type_strength)
    
    def update_model(self, person_id = -1479311724257856983, new_row = None):
        print(len(self.interactions_df))
        print(self.interactions_df.tail())
        self.interactions_df.loc[len(self.interactions_df)] = new_row
        self.content_based_recommender_model.update_interactions_df(self.interactions_df)
        self.content_based_recommender_model.update_user_profile(person_id = person_id)
        
    
    def get_similar(self, contentid, topn = 10):
        return self.content_based_recommender_model.get_similar_items_to_item_profile(item_id = contentid, topn = topn)

    def recommend(self, user_id, topn = 10):
        return self.content_based_recommender_model.recommend_items(user_id = user_id, user_profile = None,
                                                                    ignore_interacted = True, topn = topn, verbose = True)

class HybridWorker:
    def __init__(self, articles_df, interactions_df):
        self.articles_df = articles_df
        self.interactions_df = interactions_df
        self.hybrid_recommender_model = HybridRecommender(self.articles_df, self.interactions_df, cb_ensemble_weight=1.0,
                                                          cf_ensemble_weight=100, ap_ensemble_weight=1.0)
    
    def update_model(self, person_id = -1479311724257856983, new_row = None):
        # self.interactions_df.loc[len(self.interactions_df)] = new_row
        self.hybrid_recommender_model.update_user_profile(person_id = person_id, new_interactions_df = self.interactions_df)
        print(len(self.interactions_df))
        print(self.interactions_df.tail())
        pass
    def recommend(self, user_id, topn = 10):
        return self.hybrid_recommender_model.recommend_items(user_id, True, topn, True)
        