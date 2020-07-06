import numpy as np
import pandas as pd
import os

housing1=pd.read_csv('housing.csv')
# print(housing.head())
HOUSING_PATH=""
def load_housing_data(housing_path=HOUSING_PATH):
    csv_path=os.path.join(housing_path,'housing.csv')
    return pd.read_csv(csv_path)

housing=load_housing_data()
# print(housing.head())

# can getthe info of the dataframe from '.info'
# print(housing.info())

# Can read a particular data detail with its label and function added to it.
print(housing['ocean_proximity'].value_counts())

# Also the descriptive detail for the entire sheet could be reviewed by the '.describe' function
print(housing.describe())


import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
plt.show()