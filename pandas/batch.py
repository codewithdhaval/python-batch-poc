import pandas as pd
import numpy as np
from multiprocessing import Pool

num_partitions = 10 #number of partitions to split dataframe
num_cores = 4 #number of cores on your machine


def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df


def multiply_columns(data):
    data['length_of_word'] = data['species'].apply(lambda x: len(x))
    return data

iris = pd.DataFrame()
iris = parallelize_dataframe(iris, multiply_columns)
