import pandas as pd


def get_similarity(df1, df2=None):
    """
    The similarity measure - simple matrix product
    between compared dataframes of same dimensions_.
    If only one dataframes is passed - it will be compared with itself_.
    
    :param df1: first compared dataframe
    :type df1: pandas.DataFrame
    :param df2: second compared dataframe
    :type df2: pandas.DataFrame
    :return: the resulting similarity
    :rtype: pandas.DataFrame
    """
    try:
        return df1 @ df2.T if df2 is not None else df1 @ df1.T
    except TypeError:
        print("There were some non-numeric values encountered in (one of) the dataframes")
        return None
    except ValueError:
        print("The dataframes have different dimensions:\n"
              f"{df1.shape} and {df2.shape} respectively")
        return None
    

def similarities_to_ratings(sims, r_min, r_max):
    """
    Rescale similarities to ratings_.
    
    :param sims: given similarities
    :type sims: pandas.Series
    :param r_min: the lowest rating
    :type r_min: float
    :param r_max: the highest rating
    :type r_max: float
    :return: ratings
    :rtype: pandas.Series
    """
    sim_min = sims.min()
    sim_max = sims.max()
    
    return (r_max - r_min) * (sims - sim_max) / (sim_max - sim_min) + r_max \
                if sim_min < sim_max \
                else (r_max - r_min) * (sims - sim_max) + r_max


def evaluate(ratings, ratings_pred):
    """
    Calculate RMSE for predicted and real ratings_.
    
    :param ratings: given ratings
    :type ratings: pandas.DataFrame
    :param ratings_pred: predicted ratings
    :type ratings_pred: pandas.DataFrame
    :return: RMSE
    :rtype: float
    """
    diff = (ratings - ratings_pred)['rating'].dropna()
    print(f"Number of compared ratings: {diff.shape[0]}")
    return (diff ** 2).mean() ** (.5)
