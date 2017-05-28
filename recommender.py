"""Definition of the Recommender class and its subclasses.

This module contains the definition of the Recommender class and its subclasses RecommenderBaseline.
"""


import metric


class Recommender:
    """Recommender class with `train` set, `test` set, `user_id`, `item_id` and `recommended_items`.
    
    Attributes:
        train: train set
        test: test set
        user_id: name of the user ID
        item_id: name of the item ID
        recommended_items: recommendations
    
    Methods:
        recommend(): make recommendations
        evaluate(): evaluate recommendations
    
    """
    def __init__(self, user_id='user_id', item_id='item_id'):
        """Initialize Recommender with `user_id` and `item_id`.
        
        :param user_id: name of the user ID
        :param item_id: name of the item ID
        """
        self.train = None
        self.test = None
        self.user_id = user_id
        self.item_id = item_id
        self.recommended_items = None

    def recommend(self, train):
        """Make recommendations.
        
        :param train: Data object of the train set
        :return: recommendations
        """
        self.train = train

    def evaluate(self, test):
        """Evaluate recommendations.
        
        :param test: Data object of the test set
        :return: evaluation
        """
        self.test = test


class RecommenderBaseline(Recommender):
    """RecommenderBaseline class.
    
    """
    def recommend(self, train, num=10):
        """Make recommendations.
        
        :param train: Data object of the train set
        :param num: number of recommendations
        :return: recommendations
        """
        super().recommend(train)
        grouped_items = self.train.ratings.groupby(self.item_id)[self.user_id]
        popular_items = grouped_items.count().sort_values(ascending=False).index.to_series().reset_index(drop=True)

        grouped_users = self.train.ratings.groupby(self.user_id)[self.item_id]
        rated_items = {user: items.tolist() for user, items in grouped_users}

        recommended_items = dict()
        for user, items in rated_items.items():
            recommended_items[user] = list()
            for item in popular_items:
                if item not in items:
                    recommended_items[user].append(item)
                if len(recommended_items[user]) >= num:
                    break

        self.recommended_items = recommended_items
        return self.recommended_items

    def evaluate(self, test):
        """Evaluate recommendations
        
        :param test: Data object of the test set
        :return: evaluation
        """
        super().evaluate(test)
        grouped_users = self.test.ratings.groupby(self.user_id)[self.item_id]
        rated_items = {user: items.tolist() for user, items in grouped_users}

        evaluation = metric.mean_ap(self.recommended_items, rated_items)
        return evaluation
