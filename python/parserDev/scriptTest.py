from pprint import pprint
import python.parserDev.GenericProxyParser as gpp
#from python.parserDev.BroHttpPyParser import add_full_URL
import os
import inspect
from python.parserDev.broParse import broParse
import urllib
import pandas as pd
from python.researchDev.randomForest.exploitUriBehaviors import microBehaviors as mb

# #directory = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
# #fileName = os.path.join(directory, '../../data/broData/ExploitExample/http.log')
# #fileName = os.path.join(directory, '../../data/testData/badBroLog.log')
#
# #http.log
# fileName = "/Users/Gary/PycharmProjects/Aktaion2/data/broData/ExploitExample/http.log"
#
# #bro.csv
# #fileName = "/Users/Gary/PycharmProjects/Aktaion2/data/testData/bro.csv"
#
# #brothon built-in
# df = broParse.bro_http_to_df(fileName)
# pprint(df['uri'])
# pprint(df['fullUrl'])

# urlparse testing
# fullUrl =  'http://kanon-finale.com/public/js/3rd_party/calendar_date_select/locale/0277201945/?f=s&k=4888675651029212'
# pprint(urllib.parse.urlparse(fullUrl).path)


# df = broParse.bro_http_to_df(fileName)
# pprint(df)
# #custom
# #pprint(broParse.add_full_URL(df))
#
# #p0f testing
# # import subprocess
# #
# # subprocess.call('sudo ./p0f -i en0', cwd="/Users/Gary/p0f-3.09b/", shell=True)
# # #Popen("sudo ./p0f -i en0 -p", cwd="/Users/Gary/p0f-3.09b/")

# #test GenericProxyParser.generic_proxy_parser
proxy_df = gpp.generic_proxy_parser("/Users/Gary/PycharmProjects/Aktaion2/data/proxyData/exploitData/2014-01-02-neutrino-exploit-traffic.webgateway")
#pprint(proxy_df)

# #Test merge/normalization of bro and proxy logs
fileName = "/Users/Gary/PycharmProjects/Aktaion2/data/broData/ExploitExample/http.log"
bro_df = broParse.bro_http_to_df(fileName)
#pprint(type(bro_df['epochTime'][0]))

new_df = pd.concat([bro_df, proxy_df], axis=0)
new_df = pd.DataFrame.reset_index(new_df)
#pprint(new_df)

# create a list of the uri in the head
uriList = new_df.head()['uri'].tolist()
print(uriList)

# # test the exploitationUriBehaviors.max_path_length, 4
# print("max uri path length is ", mb.max_path_length(uriList))
#
# # test the exploitationUriBehaviors.max_path_length, 1
# print("min uri path length is ", mb.min_path_length(uriList))
#
# # test exploitationUriBehaviors.max_length, 777
# print("max path length is ", mb.max_length(uriList))
#
# # test exploitationUriBehaviors.max_length, 4
# print("min path length is ", mb.min_length(uriList))
#
# # test exploitationUriBehaviors.max_entropy, 0.536905227321473
# print("the max entropy is ", mb.max_entropy(uriList))
#
# # test exploitationUriBehaviors.min_entropy, 0.25
# print("the min entropy is ", mb.min_entropy(uriList))
#
# # test exploitationUriBehaviors.base_64_match, 1
# print("the number of base64 encoded uri is ", mb.base_64_match(uriList))
#
# # check that mb.base_64_match works, 4
# print("the number of base64 encoded strings in [dGVzdA0K, dGVzdDE=, dGVzdDI=, dGVzdDM=, #&sj.s3] is ",
#       mb.base_64_match(['dGVzdA0K', 'dGVzdDE=', 'dGVzdDI=', 'dGVzdDM=','#&sj.s3']))
#
# #test exploitationUriBehaviors.isUrlencoded empty string catch, False
# print("the empty string is  url encoded ", mb.isUrlEncoded(""))
#
# #test exploitationUriBehaviors.url_encoded_match, 0
# print("The number of url encoded strings is ", mb.percent_encoding_match(uriList))
#
# #test exploitationUriBehaviors.url_encoded_match, should return 1
# print("The number of url encoded strings is ", mb.percent_encoding_match(['%34%jd%kl%',
#                                                                           '12345',
#                                                                           '%ji.,%,./n3']))
#
# #test exploitationUriBehaviors.uri_distrint, expected return 2
# print("The number of distinct uri strings is ", mb.uri_distinct(['a','b','a','b']))
#
# #test exploitationUriBehaviors.uri_distrint, expected return 5
# print("The number of distinct uri strings is ", mb.uri_distinct(uriList))

pprint(mb.behaviorVector(uriList))
#pprint(type(new_df['epochTime'][4]))
#pprint(new_df['fullUrl'])
# #test GenericProxyParser.generic_line_parser
# logLine = '[09/Jan/2014:04:53:28 -0800] "Nico Rosberg" 172.16.2.101 85.93.134.203 1500 204 TCP_HIT "GET http://www.grad.ru/forum/public/js/3rd_party/colorpicker/0490c7979e/?f=s&k=5797540687062411 HTTP/1.1" "Internet Services" "low risk " "text/html" 329 203 "Mozilla/4.0 (Windows 7 6.1) Java/1.7.0_13" "" "-" "0" "" "-"'
#
# pprint (gpp.generic_line_parser(logLine))
