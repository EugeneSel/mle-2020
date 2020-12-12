def select_features(df, features):
    """
    Select features from the dataframe_.
    
    :param df: target dataframe
    :type df: pandas.DataFrame
    :param features: list of features to choose
    :type features: list
    :return: dataframe with desired features (columns)
    :rtype: pandas.DataFrame
    """
    try:
        return df[features]
    except KeyError:
        print(f"The given list of features: {features} is not valid for a given dataframe")
        return None


def choose_row_cols(df, row_condition, features=None):
    """
    Select a row via condition/index from dataframe_.
    In case of multiple condition match - only the first row is returned_.
    Some particular row features (columns) can be optionally chosen_.
    
    :param df: target dataframe
    :type df: pandas.DataFrame
    :param row_condition: row condition/index
    :type row_condition: pandas.Series/int
    :param features: list of features to choose
    :type features: list
    :return: desired row if found
    :rtype: pandas.Series
    """
    if isinstance(row_condition, int):
        try:
            return df.iloc[row_condition][features] if features else df.iloc[row_condition]
        except IndexError:
            print(f"Row with the index {row_condition} was not found")
            return None
        except KeyError:
            print(f"The given list of features: {features}, is not valid for a given dataframe")
            return None
    else:
        try:
            return df.loc[row_condition][features].iloc[0] if features else df.loc[row_condition].iloc[0]
        except IndexError:
            print(f"There are no rows satisfying the given condition")
            return None
        except KeyError:
            print(f"The given list of features: {features} is not valid for a given dataframe")
            return None
