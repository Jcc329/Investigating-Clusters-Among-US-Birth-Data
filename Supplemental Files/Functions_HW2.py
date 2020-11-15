from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
#https://www.geeksforgeeks.org/ml-one-hot-encoding-of-datasets-in-python/
def onehotencoder(df, List_of_Variables):
    '''
    Takes list of variables that need to be encoded,
    returns a dataframe of the encoded variables
    '''
    enc = OneHotEncoder(handle_unknown='ignore',sparse=False)

    enc.fit(df[List_of_Variables])
    x = enc.transform(df[List_of_Variables])
    return pd.DataFrame(x, columns=enc.get_feature_names(list(List_of_Variables)))