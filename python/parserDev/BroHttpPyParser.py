#TODO add docstring info
from brothon import bro_log_reader
import pandas as pd


#take a Bro log file
#return a dictionary with all log info, including legacy variable names from the scala version.

##Brothon Behaviors
    ##Given an inivalid file path broLogReader throws no errors
    ##Given an empty file, BroHttpPyParser hangs
    ##

def add_full_URL(inFrame):
    """Given a bro http.log dataframe, returns the frame with a 'fullUrl' colum appended"""
    masterDictionary = []
    for index, row in inFrame.iterrows():
        if row['id.resp_h'] == 443:
            fUrl = "https://" + row['host'] + row['uri']
        else:
            fUrl = "http://" + row['host'] + row['uri']

        masterDictionary.append(fUrl)

    inFrame['fullUrl'] = pd.Series(masterDictionary).values
    return(inFrame)

