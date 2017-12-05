# author:mvaouli
# Version 2.0
#Entry point for Blackhat 2017 EU Demo
#Protoype microbehavior extractio logic and exploit/phishing detection


from colorama import Fore, Style, Back
import subprocess as sp
import pandas as pd

import python.parser_dev.generic_proxy_parser as gpp
from python.parser_dev.bro_parser import broParse
import python.research_dev.random_forest.exploit_uri_behaviors as ex
from python.demo_tools.boot import boot


##inital spalsh message for aktaion
boot()
sp.call('clear',shell=True)

#demo speficic ascii art
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
print(Fore.GREEN + 81 * '-'+ Style.RESET_ALL)
print(Fore.GREEN +'1:' + Fore.WHITE + ' Run Demo ' + Style.RESET_ALL),
print(Fore.GREEN +'2:' + Fore.WHITE + ' Analyze Bro HTTP Sample Using Phishing Model                                  ' + Style.RESET_ALL),
print(Fore.GREEN +'3:' + Fore.WHITE + ' Demo                                                                          '+ Style.RESET_ALL),
print(Fore.GREEN + 81 * '-'+ Style.RESET_ALL)

# Get input
choice = input(Fore.WHITE + 'Enter your choice' + Fore.GREEN + ' (1-4)'+ Fore.GREEN+':')
### Convert string to int type ##
choice = int(choice)

# Take action as per selected menu-option
if choice == 1:
    print("Analyze Proxy Log For Potential Exploit Behavior")

    from python.demo_tools.loading import load_analyzer
    load_analyzer()


    path = "data/logs_proxy_format/exploit/2014-01-02-neutrino-exploit-traffic.webgateway"
    print("File for analysis : ", path)

    proxy_df = gpp.generic_proxy_parser(path)
    # print(proxy_df)

    # Test merge/normalization of bro and proxy logs
    fileName = "data/logs_bro_format/exploit/http.log"
    bro_df = broParse.bro_http_to_df(fileName)
    new_df = pd.concat([bro_df, proxy_df], axis=0)
    # reset index
    new_df = pd.DataFrame.reset_index(new_df)
    # blow out old index information
    del new_df['index']

    print(ex.microBehaviors.behaviorVector(new_df))
    import python.demo_tools.exploitascii
    import python.demo_tools.phishingascii
       # exploit_chain_art()

elif choice == 2:
    print("")
elif choice == 3:
    print("")
else:  ## default ##
    print(Fore.RED+"Invalid number. Try again..."+ Style.RESET_ALL)