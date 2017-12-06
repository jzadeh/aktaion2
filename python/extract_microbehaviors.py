# Load bro parser
from python.parser_dev.bro_parser import broParse as br

# Load proxy parser
import python.parser_dev.generic_proxy_parser as gpp

import python.research_dev.random_forest.microbehavior_core_logic as ex

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

# Declare global exploit and benign dataFrame vars for keeping the raw log data
df_ex = pd.DataFrame()
df_be = pd.DataFrame()

# keep the extracted micro behaviors here
df_mb_ex = pd.DataFrame()
df_mb_be = pd.DataFrame()

#specify the length of window used in generating microbehavior statistics
window_len = 5

#configuration for output
bro_benign = True
bro_exploit = False
proxy_benign = False
proxy_exploit = False

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

def create_df_of_sliding_windows(df_raw_log, df_microbeahaviors):

    # use for determining upper bound in number of sliding windows we create
    df_len = len(df_raw_log)

    if df_len > window_len:
        for i in range(0, df_len - window_len):
            # create sliding window which outputs another dataframe
            df_raw_log_window = df_raw_log[i:i + window_len]

            # use the micro behavior api to extract the stats as a dict
            dict_mb = ex.TimeBehaviors.behavior_vector(df_raw_log_window)

            # convert each dict (window) to a dataframe and add to our global variable
            df_from_dict = pd.DataFrame([dict_mb], columns=dict_mb.keys())
            print(df_from_dict)
            print(len(df_microbeahaviors))
            df_microbeahaviors = df_microbeahaviors.append(df_from_dict, ignore_index=True)

    return df_microbeahaviors

# Step 1: Build Stats For Benign Bro Files
if bro_benign == True:
    for filename in os.listdir(bro_benign_dir):

        #convert raw log to dataframe
        try:
            df_bro_raw_log_benign = br.bro_http_to_df(bro_benign_dir + "/" + filename).head(100)
        except: print("Parsing Error")

        df_mb_be = create_df_of_sliding_windows(df_bro_raw_log_benign, df_mb_be)
        # #use for determining upper bound in number of sliding windows we create
        # df_len = len(df_bro_raw_log_benign)
        #
        # if df_len > window_len:
        #     for i in range(0,df_len -window_len):
        #       print(i)
        #
        #       #create sliding window which outputs another dataframe
        #       df_raw_log_window = df_bro_raw_log_benign[i:i+window_len]
        #
        #       # use the micro behavior api to extract the stats as a dict
        #       dict_mb = ex.TimeBehaviors.behavior_vector(df_raw_log_window)
        #
        #       # convert each dict (window) to a dataframe and add to our global variable
        #       df_from_dict = pd.DataFrame([dict_mb], columns=dict_mb.keys())
        #       df_mb_be = df_mb_be.append(df_from_dict, ignore_index=True)

    output_path = 'data/benign_bro_microbehaviors.csv'
    print("Writing Benign BRO Benign Microbehavior Statistics to CSV file: " + output_path)
    df_mb_be.to_csv(output_path)
    print("Done Writing BRO Benign Microbehavior Data")

# Step 2: Build Stats For Malicious Bro Files
if bro_exploit == True:
    for filename in os.listdir(bro_exploit_dir):

        try:
            df_bro_raw_log_exploit = br.bro_http_to_df(bro_exploit_dir + "/" + filename)
        except:
            print("Parsing Error")

        # use for determining upper bound in number of sliding windows we create
        df_len = len(df_bro_raw_log_exploit)

        if df_len > window_len:
            for i in range(0, df_len - window_len):
                print(i)

                # create sliding window which outputs another dataframe
                df_raw_log_window = df_bro_raw_log_exploit[i:i + window_len]

                # use the micro behavior api to extract the stats as a dict
                dict_mb = ex.TimeBehaviors.behavior_vector(df_raw_log_window)

                # convert each dict (window) to a dataframe and add to our global variable
                df_from_dict = pd.DataFrame([dict_mb], columns=dict_mb.keys())
                df_mb_be = df_mb_be.append(df_from_dict, ignore_index=True)

    output_path = 'data/benign_bro_microbehaviors.csv'
    print("Writing Benign BRO Benign Microbehavior Statistics to CSV file: " + output_path)
    df_mb_be.to_csv(output_path)
    print("Done Writing BRO Benign Microbehavior Data")

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