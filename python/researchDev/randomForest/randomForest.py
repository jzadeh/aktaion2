# Load bro parser
from python.parserDev.broParse import broParse as br

# Load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier

# Load pandas
import pandas as pd

# Load numpy
import numpy as np

# Load os to parse directories
import os


# Define make_training_class to pick rows for training/test
def make_training_class(df):
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
    return(df)

# Specify training data directory
bro_exploit_dir = "/Users/Gary/PycharmProjects/Aktaion2/python/researchDev/randomForest/brologs/exploits"
bro_benign_dir = "/Users/Gary/PycharmProjects/Aktaion2/python/researchDev/randomForest/brologs/benign"

# Declare global exploit and benign dataFrame vars
df_ex = pd.DataFrame()
df_be = pd.DataFrame()

# Load exploit data into df_ex
for filename in os.listdir(bro_exploit_dir):
    bro_df = br.bro_http_to_df(bro_exploit_dir + "/" + filename)
    df_ex = df_ex.append(bro_df)

# Reset the df_ex rows index
df_ex = df_ex.reset_index()
# Add and populate threat_class column
df_ex['threat_class'] = 1


# Load benign data into df_be
df_be = pd.DataFrame()
for filename in os.listdir(bro_benign_dir):
    bro_df = br.bro_http_to_df(bro_benign_dir + "/" + filename)
    df_be = df_be.append(bro_df)

# Reset the df_be rows index
df_be = df_be.reset_index()
# Add and populate threat_class column
df_be['threat_class'] = 0

# Add is_train column
df_ex = make_training_class(df_ex)
df_be = make_training_class(df_be)

# Create two for each set new dataframes, one with the training rows, one with the test rows
train_ex, test_ex = df_ex[df_ex['is_train']==True], df_ex[df_ex['is_train']==False]
train_be, test_be = df_be[df_be['is_train']==True], df_be[df_be['is_train']==False]

# Concatenate the test and training data into two seperate dataframes
train = pd.concat([train_ex, train_be])
test = pd.concat([test_ex, test_be])

# Show the number of observations for the test and training dataframes
print('Number of observations in the training data:', len(train))
print('Number of observations in the test data:',len(test))

