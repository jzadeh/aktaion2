from colorama import Fore, Style, Back
#author:mvaouli
# Version 2.0
## Show menu ##
import subprocess as sp

import python.parser_dev.generic_proxy_parser as gpp
# from python.parserDev.BroHttpPyParser import add_full_URL
import os
import inspect
from python.parserDev.broParse import broParse
import urllib
import pandas as pd
# from python.researchDev.randomForest.exploitUriBehaviors import microBehaviors as mb
import python.researchDev.randomForest.exploitUriBehaviors as ex


from python.demo_tools.boot import boot

boot()
sp.call('clear',shell=True)


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

## Get input ###
choice = input(Fore.WHITE + 'Enter your choice' + Fore.GREEN + ' (1-4)'+ Fore.GREEN+':')
### Convert string to int type ##
choice = int(choice)

### Take action as per selected menu-option ###
if choice == 1:
    print("")





elif choice == 2:
    print("")
elif choice == 3:
    print("")
else:  ## default ##
    print(Fore.RED+"Invalid number. Try again..."+ Style.RESET_ALL)