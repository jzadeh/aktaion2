from pprint import pprint
from python.parserDev.BroHttpPyParser import add_full_URL
import os
import inspect
from python.parserDev.broParse import broParse

# generic_line_parser(logLine)

#directory = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
#fileName = os.path.join(directory, '../../data/broData/ExploitExample/http.log')
#fileName = os.path.join(directory, '../../data/testData/badBroLog.log')

#http.log
fileName = "/Users/Gary/PycharmProjects/Aktaion2/data/broData/ExploitExample/http.log"

#bro.csv
#fileName = "/Users/Gary/PycharmProjects/Aktaion2/data/testData/bro.csv"

#brothon built-in
#pprint(broParse.bro_http_to_df(fileName))
df = broParse.bro_http_to_df(fileName)
#custom parser
pprint(add_full_URL(df))

#p0f testing
# import subprocess
#
# subprocess.call('sudo ./p0f -i en0', cwd="/Users/Gary/p0f-3.09b/", shell=True)
# #Popen("sudo ./p0f -i en0 -p", cwd="/Users/Gary/p0f-3.09b/")