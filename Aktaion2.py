import argparse
from python.parserDev import broParse as bp
from pprint import pprint
import os
import sys

#TODO add option for pcap parsing using -p flag
parser = argparse.ArgumentParser(description="Parse a Bro log file or PCAP file (-p), return a dictionary with"
                                             " integer key values corresponding to log-row number.")
parser.add_argument('fileName', metavar='F', type=str, nargs='+',
                     help='bro-log / pcap fully qualified filename')
args, commands = parser.parse_known_args()

# Check for unknown args
if commands:
    print('Unrecognized args: %s' % commands)
    sys.exit(1)

# If no args just call help
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

if (os.path.isfile(args.fileName[0])):
    pprint(bp.broParse.bro_http_to_df(args.fileName[0]))
else:
    print("Not a valid file path")

