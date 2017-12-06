"""broParse: this class defines broParse, which contains methods for converting the
            individual rows of Bro Logs into dataframes using Brothon's built-in method

        Args:
            inFile (str): The full path to the file.
            delimiter (str): The delimiter in the Bro log file (default='\t')
"""
import sys
import pandas as pd
from brothon import bro_log_reader

class broParse:

    def bro_http_to_df(inFile):
        """Parses a Bro http.log file, returns a pandas data frame"""
        if not inFile.endswith('log'):
            print('This method only works with Bro http.log files, the file ' + inFile + ' is not valid.' )
            sys.exit(1)

        reader = bro_log_reader.BroLogReader(inFile)
        bro_df = pd.DataFrame(reader.readrows())
        bro_df = broParse.add_full_URL(bro_df)
        bro_df = broParse.normalize_bro(bro_df)

        return(bro_df)

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
        return (inFrame)

    def normalize_bro(df):
        """takes a bro-log data frame and returns a dataframe with the column names updated
            to match the proxy-log column names"""
        df.rename(columns={'ts': 'epochTime', 'id.resp_h': 'respHost',
                           'method': 'httpMethod', 'orig_mime_types': 'mimeType',
                           'id.orig_h': 'origHost', 'status_code': 'statusCode',
                           'user_agent': 'userAgent', 'username': 'userName'}, inplace=True)
        return(df)