import pandas as pd
import re

class microBehaviors:

    # Define an class method for matching base64 strings
    def isBase64(s):
        return re.match('^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$', s)


    def max_path_length(inList):
        """return the max path length of all URIs"""
        # Declare local var that will store the max path length
        maxLength = 0

        # Count the depth of the file structure for each uri in inList
        for uri in inList:

            # Check the current uri path length against the running length
            if uri.count('/') > maxLength :
                maxLength = uri.count('/')

        return(maxLength)

