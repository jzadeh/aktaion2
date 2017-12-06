# Load bro parser
from python.parser_dev.bro_parser import broParse as br

# Load proxy parser
import python.parser_dev.generic_proxy_parser as gpp

import python.research_dev.random_forest.exploit_uri_behaviors as ex

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

# Specify bro data directories
bro_exploit_dir = "data/logs_bro_format/exploit"
bro_benign_dir = "data/logs_bro_format/benign"

# Declare global exploit and benign dataFrame vars
df_ex = pd.DataFrame()
df_be = pd.DataFrame()

df_mb_ex = pd.DataFrame()
df_mb_be = pd.DataFrame()


# Load exploit Bro data into df_ex
# for filename in os.listdir(bro_exploit_dir):
#  #   try:
#     bro_df = br.bro_http_to_df(bro_exploit_dir + "/" + filename)
#     df_ex = df_ex.append(bro_df)
# #    except:

#print(df_ex)

# # Reset the df_ex rows index
# df_ex = df_ex.reset_index()
# # Add and populate threat_class column
# df_ex['threat_class'] = 1
#
# # Load benign Bro data into df_be
df_be = pd.DataFrame()


window_len = 5

for filename in os.listdir(bro_benign_dir):
    print(filename)
    try:
        bro_df = br.bro_http_to_df(bro_benign_dir + "/" + filename)
        # df_be = df_be.append(bro_df)
        mb_df = ex.exploitationTimeBehaviors.behavior_vector(bro_df)


        print(mb_df)
        df_mb_be.append(mb_df)
    except: print ("bro parsing error")

   # mb_df = ex.microBehaviors.behaviorVector(df_be)
   # df_mb_be = df_mb_be.append(mb_df)


# #df_be.to_csv('data/benign_proxy_logs.csv')
#
# mb_df = ex.microBehaviors.behaviorVector(df_be)
#
# print(mb_df)
#
df_mb_be.to_csv('data/benign_proxy_microbehaviors.csv')

#
# # Reset the df_be rows index
# df_be = df_be.reset_index()
# # Add and populate threat_class column
# df_be['threat_class'] = 0
#
# # Add is_train column
# df_ex = make_training_class(df_ex)
# df_be = make_training_class(df_be)
#
# # Create two for each set new dataframes, one with the training rows, one with the test rows
# train_ex, test_ex = df_ex[df_ex['is_train']==True], df_ex[df_ex['is_train']==False]
# train_be, test_be = df_be[df_be['is_train']==True], df_be[df_be['is_train']==False]
#
# # Concatenate the test and training data into two seperate dataframes
# train = pd.concat([train_ex, train_be])
# test = pd.concat([test_ex, test_be])



# Show the number of observations for the test and training dataframes
# print('Number of observations in the training data:', len(train))
# print('Number of observations in the test data:',len(test))

# Initialize proxy data directories
proxy_exploit_dir = "data/logs_proxy_format/exploit"
# proxy_benign_dir  = "data/logs_proxy_format/benign"
#
# # Initialize proxy data frames
# df_p_ex = pd.DataFrame()
# df_p_be = pd.DataFrame()
#
# # Initialized proxy holding frames
# proxy_df = pd.DataFrame()

#Load exploit proxy data into df_p_ex
# for filename in os.listdir(proxy_exploit_dir):
#
#     try:
#         proxy_df = gpp.generic_proxy_parser(proxy_exploit_dir + "/" + filename)
#         print(proxy_df)
#         print(filename)
#         df_p_ex = pd.concat([proxy_df, df_p_ex])
#
#    # df_p_ex.append(p_ex)
#
#     except NameError:
#         print("problem with parsing file name: " + filename)
#
#
# print("the number of observations in the generic proxy parser exploit frame is ", len(df_p_ex))
#df_p_ex.to_csv('data/exploit_proxy_logs.csv')

# for filename in os.listdir(proxy_benign_dir):
#
#     try:
#         proxy_df_benign = gpp.generic_proxy_parser(proxy_benign_dir + "/" + filename)
#         print(proxy_df_benign)
#         print(filename)
#         df_p_benign = pd.concat([proxy_df_benign, df_p_benign])
#
#     except NameError:
#         print("problem with parsing file name: " + filename)
#
# print("the number of observations in the generic proxy parser benign frame is ", len(df_p_benign))
# df_p_benign.to_csv('data/benign_proxy_logs.csv')