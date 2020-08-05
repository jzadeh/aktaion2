import pandas as pd
import re


class micro_behaviors:

    # Define an class method for matching base64 strings
    def is_base64(s):
        return re.match('^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$', s)

    def max_path_length(in_list):
        """return the max path length of all URIs"""
        # Declare local var that will store the max path length
        max_length = 0

        # Count the depth of the file structure for each uri in inList
        for uri in in_list:

            # Check the current uri path length against the running length
            if uri.count('/') > max_length:
                max_length = uri.count('/')

        return max_length
