# from pprint import pprint
# from BroHttpPyParser import bro_http_parser
# import os
# import inspect
#
# # Run the bro reader on a given log file
# # logLine = ' "Nico Rosberg" 77.75.107.241 1500 200 TCP_HIT "GET http://www.divernet.com/ HTTP/1.1" "Internet Services" "low risk " "text/html; charset=utf-8" 470 396 "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)" "http://www.google.com/url?sa=t&rct=j&q=&esrc=s&frm=1&source=web&cd=1&sqi=2&ved=0CCoQFjAA&url=http%3A%2F%2Fwww.divernet.com%2F&ei=opvOUpyXFrSA2QXnv4DwDg&usg=AFQjCNHeSe4ebK0u69M-TBEGNkTZy-C-Nw&bvm=bv.59026428,d.b2I" "-" "0" "" "-" '
# #
# # generic_line_parser(logLine)
#
# directory = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
# fileName = os.path.join(directory, '../../data/broData/ExploitExample/http.log')
#
# pprint(bro_http_parser(fileName))

import subprocess

subprocess.call('sudo ./p0f -i en0', cwd="/Users/Gary/p0f-3.09b/", shell=True)
#Popen("sudo ./p0f -i en0 -p", cwd="/Users/Gary/p0f-3.09b/")