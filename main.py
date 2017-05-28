"""Main module.

This module is the main module of this project.
"""


import data
import recommender


def read_data():
    """Read the train and test data
    
    :return: train and test data frames
    """
    rating_cols = ['user_id', 'item_id', 'play_count']

    train_rating_files = ['../src/data_sets/valid_triplets_visible.txt', '../src/data_sets/test_triplets_visible.txt']
    train = data.Data(rating_files=train_rating_files, rating_cols=rating_cols)

    test_rating_files = ['../src/data_sets/valid_triplets_hidden.txt', '../src/data_sets/test_triplets_hidden.txt']
    test = data.Data(rating_files=test_rating_files, rating_cols=rating_cols)

    return train, test


def recommend(train, test):
    """Make and evaluate recommendations
    
    :param train: Data object of train set
    :param test: Data object of test set
    :return: recommendations and evaluate
    """
    rec = recommender.RecommenderBaseline()
    recommendations = rec.recommend(train, 500)
    evaluation = rec.evaluate(test)
    return recommendations, evaluation


def main():
    train, test = read_data()
    recommendations, evaluation = recommend(train, test)
    print('The mean average precision is {}.'.format(evaluation))


if __name__ == '__main__':
    main()
