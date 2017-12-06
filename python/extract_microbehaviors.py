# Load bro parser
from python.parser_dev.bro_parser import broParse as br

# Load proxy parser
import python.parser_dev.generic_proxy_parser as gpp

import python.research_dev.random_forest.microbehavior_core_logic as ex

# Load pandas
import pandas as pd

# Load os to parse directories
import os

# Specify  data directories
bro_exploit_dir = "data/logs_bro_format/exploit"
bro_benign_dir = "data/logs_bro_format/benign"

proxy_exploit_dir = "data/logs_proxy_format/exploit"
proxy_benign_dir  = "data/logs_proxy_format/benign"

# Declare global exploit and benign dataFrame vars for keeping the raw log data
df_ex = pd.DataFrame()
df_be = pd.DataFrame()

# keep the extracted micro behaviors here
df_mb_ex = pd.DataFrame()
df_mb_be = pd.DataFrame()

#specify the length of window used in generating microbehavior statistics
window_len = 5

#configuration for output
bro_benign = False
bro_exploit = False
proxy_benign = False
proxy_exploit = True

#helper method for building a dataframe of sliding windows
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
if bro_benign:
    for filename in os.listdir(bro_benign_dir):
        #convert raw log to dataframe
        try:
            df_bro_raw_log_benign = br.bro_http_to_df(bro_benign_dir + "/" + filename).head(100)
        except: print("Parsing Error")

        df_mb_be = create_df_of_sliding_windows(df_bro_raw_log_benign, df_mb_be)

    output_path = 'data/benign_bro_microbehaviors.csv'
    print("Writing Benign BRO Microbehavior Statistics to CSV file: " + output_path)
    df_mb_be.to_csv(output_path)
    print("Done Writing Benign BRO Microbehavior Data")

# Step 2: Build Stats For Malicious Bro Files
if bro_exploit:
    for filename in os.listdir(bro_exploit_dir):
        try:
            df_bro_raw_log_exploit = br.bro_http_to_df(bro_exploit_dir + "/" + filename)
        except:
            print("Parsing Error")

            df_mb_ex = create_df_of_sliding_windows(df_bro_raw_log_exploit, df_mb_ex)

    output_path = 'data/exploit_bro_microbehaviors.csv'
    print("Writing Exploit BRO Microbehavior Statistics to CSV file: " + output_path)
    df_mb_ex.to_csv(output_path)
    print("Done Writing Exploit BRO Microbehavior Data")

# Step 3: Build Stats For Benign Proxy Files
if proxy_benign:
    for filename in os.listdir(proxy_benign_dir):
        try:
            df_proxy_raw_log_benign = gpp.generic_proxy_parser(proxy_benign_dir + "/" + filename)
            df_mb_be = create_df_of_sliding_windows(df_proxy_raw_log_benign, df_mb_be)
        except UnicodeDecodeError:
            print("Unicode Parsing Error")

    output_path = 'data/benign_proxy_microbehaviors.csv'
    print("Writing Benign Proxy Microbehavior Statistics to CSV file: " + output_path)
    df_mb_be.to_csv(output_path)
    print("Done Writing Benign Proxy Microbehavior Data")

if proxy_exploit:
    for filename in os.listdir(proxy_exploit_dir):
        try:
            df_proxy_raw_log_exploit = gpp.generic_proxy_parser(proxy_exploit_dir + "/" + filename)
            df_mb_ex = create_df_of_sliding_windows(df_proxy_raw_log_exploit, df_mb_ex)
        except UnicodeDecodeError:
            print("Unicode Parsing Error")

    output_path = 'data/exploit_proxy_microbehaviors.csv'
    print("Writing Exploit Proxy Microbehavior Statistics to CSV file: " + output_path)
    df_mb_ex.to_csv(output_path)
    print("Done Writing Exploit Proxy Microbehavior Data")




# Show the number of observations for the test and training dataframes
# print('Number of observations in the training data:', len(train))
# print('Number of observations in the test data:',len(test))

# Initialize proxy data directories

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