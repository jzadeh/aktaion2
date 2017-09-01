"""broParse: this class reads in Bro logs, converting the individual rows
             into dataframes using Brothon's built-in method

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
        if not inFile.endswith('http.log'):
            print('This method only works with Bro http.log files..')
            sys.exit(1)

        reader = bro_log_reader.BroLogReader(inFile)
        bro_df = pd.DataFrame(reader.readrows())

        return(bro_df)



    # #parse the rows
    # df = pd.read_csv('cryptoWallBroHttp.log', sep='\t', header=6, skiprows=[7], index_col=False, skipfooter=1, engine='python')
    # df_modified = df[df.columns[:-1]]
    # df_modified.columns = df.columns[1:]
    # #print(df_modified)
    #
    # print(df_modified.groupby(by='id.orig_p').head(2).reset_index(drop=True))