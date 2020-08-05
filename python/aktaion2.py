# author: mvaouli
# author: jzadeh/jzsplunk
# Version 2.0
# Prototype Microbehavior extraction logic and exploit/phishing detection
from colorama import Fore, Style
import subprocess as sp
import pandas as pd
import python.parsing_logic.generic_proxy_parser as gpp
from python.parsing_logic.bro_parser import bro_parse
import python.machine_learning.microbehavior_core as ex
from python.demo_tools.boot import boot
import time
import shutil


time.sleep(1.0)


# first ascii art splash message
boot()
sp.call('clear', shell=True)

# demo specific ascii art ( I guess we decided two ASCII art displays was better than one...)
print(Fore.GREEN + 81 * '-'+ Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +"              █████╗ ██╗  ██╗████████╗ █████╗ ██╗ ██████╗ ███╗   ██╗             "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +"             ██╔══██╗██║ ██╔╝╚══██╔══╝██╔══██╗██║██╔═══██╗████╗  ██║             "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +"             ███████║█████╔╝    ██║   ███████║██║██║   ██║██╔██╗ ██║             "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +"             ██╔══██║██╔═██╗    ██║   ██╔══██║██║██║   ██║██║╚██╗██║             "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +"             ██║  ██║██║  ██╗   ██║   ██║  ██║██║╚██████╔╝██║ ╚████║             "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +"             ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝             "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +" ██╗   ██╗███████╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗    ██████╗     ██████╗  "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +" ██║   ██║██╔════╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║    ╚════██╗   ██╔═████╗ "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +" ██║   ██║█████╗  ██████╔╝███████╗██║██║   ██║██╔██╗ ██║     █████╔╝   ██║██╔██║ "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +" ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║██║   ██║██║╚██╗██║    ██╔═══╝    ████╔╝██║ "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +"  ╚████╔╝ ███████╗██║  ██║███████║██║╚██████╔╝██║ ╚████║    ███████╗██╗╚██████╔╝ "+ Style.RESET_ALL);
print(Fore.LIGHTWHITE_EX + Style.BRIGHT +"   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝ ╚═════╝  "+ Style.RESET_ALL);
print(Fore.WHITE+"                               M A I N - M E N U                                 "+ Style.RESET_ALL)
print(Fore.GREEN + 81 * '-' + Style.RESET_ALL)
print(Fore.GREEN + '1:' + Fore.WHITE + ' Run Demo ' + Style.RESET_ALL),
print(Fore.GREEN + '2:' + Fore.WHITE + ' Analyze Bro HTTP Log File                                  ' + Style.RESET_ALL),
print(Fore.GREEN + 81 * '-'+ Style.RESET_ALL)

# Get input
choice = input(Fore.WHITE + 'Enter your choice' + Fore.GREEN + ' (1-2)'+ Fore.GREEN+':' + Style.RESET_ALL)
choice = int(choice)
sp.call('clear', shell=True)

# Take action as per selected menu-option
if choice == 1:
    columns = shutil.get_terminal_size().columns
    path = "data/logs_proxy_format/exploit/2014-01-02-neutrino-exploit-traffic.webgateway"
    print('The file we are analyzing is located here: '.center(columns), path.center(columns))
    print('\n' * 1)
    print('Begin Processing Single Input Proxy Log For Potential Exploit Behavior'.center(columns))
    time.sleep(2.0)
    #sp.call('clear', shell=True)
    from python.demo_tools.loading import load_analyzer

    load_analyzer()

    #sp.call('clear', shell=True)
    print("File for analysis : ", path)
    #sp.call('clear', shell=True)
    proxy_df = gpp.generic_proxy_parser(path)
    # print(proxy_df)

    # Test merge/normalization of bro and proxy logs
    fname = "data/logs_bro_format/exploit/http.log"
    bro_df = bro_parse.bro_http_to_df(fname)
    new_df = pd.concat([bro_df, proxy_df], axis=0)
    # reset index
    new_df = pd.DataFrame.reset_index(new_df)
    # blow out old index information
    del new_df['index']

    print(ex.HTTPMicroBehaviors.behaviorVector(new_df))
    time.sleep(2.0)
    # os.system('cls||clear')
    import python.demo_tools.ascii_splash_exploit as ex_ascii
    ex_ascii.exploit_chain_art()

if choice == 2:
    file_path = input(Fore.WHITE + 'Please enter file location as string of BRO http.log' + Fore.GREEN + ':' + Style.RESET_ALL)
    user_bro_df = bro_parse.bro_http_to_df(file_path)
    print(ex.HTTPMicroBehaviors.behaviorVector(user_bro_df))
# try:
#    in_file = broParse.bro_http_to_df(fileName)
#    print('File opened successfully!')
#    in_file.close()
# except IOError:
#    print(Fore.RED+"Cannot open file!"+ Style.RESET_ALL)

# else:
#     print(Fore.RED+"Invalid number. Try again..." + Style.RESET_ALL)

