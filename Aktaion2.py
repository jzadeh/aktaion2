import argparse
from python.parserDev import broParse as bp
from pprint import pprint
import os.path

#TODO add option for pcap parsing using -p flag
parser = argparse.ArgumentParser(description="Parse a Bro log file or PCAP file (-p), return a dictionary with"
                                             " integer key values corresponding to log-row number.")
parser.add_argument('fileName', metavar='F', type=str, nargs='+',
                     help='bro-log / pcap fully qualified filename')
args = parser.parse_args()

#foo = "/Users/Gary/PycharmProjects/Aktaion2/data/broData/ExploitExample/http2.log"
if (os.path.isfile(args.fileName[0])):
    pprint(bp.bro_http_to_df(args.fileName[0]))
else:
    print("Not a valid file path")
