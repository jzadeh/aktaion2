import itertools
import threading
import time
import sys
from colorama import Fore, Style
import shutil

done = False
#loading animation
def load_analyzer():
    print('\n' * 25)
    columns = shutil.get_terminal_size().columns
    for f in itertools.cycle([ Fore.LIGHTWHITE_EX + Style.BRIGHT + '*' + Fore.YELLOW + 'ᗧ' + Fore.LIGHTWHITE_EX +
                               Style.BRIGHT + 'Analyzing*File*','*A' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'nalyzing*File*' , '*An' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'alyzing*File*' , '*Ana' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'lyzing*File*' , '*Anal' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'yzing*File*' , '*Analy' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'zing*File*' , '*Analyz' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'ing*File*' , '*Analyzi' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'ng*File*' , '*Analyzin' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'g*File*' , '*Analyzing' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + '*File*' , '*Analyzing*' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'File*' , '*Analyzing*F' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'ile*' , '*Analyzing*Fi' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'le*' , '*Analyzing*Fil' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + 'e*' , '*Analyzing*File' + Fore.YELLOW + 'ᗧ' +
                               Fore.LIGHTWHITE_EX + Style.BRIGHT + '*' + Style.RESET_ALL ]):
    #for f in itertools.cycle(['ᗧ','ᗧ*','*ᗧ*','**ᗧ*','.center(columns)***ᗧ*','****ᗧ*','*****ᗧ*','****ᗧ']):

        if done:
            break
        sys.stdout.write('\r'+ f.center(columns))
        #sys.stdout.write('\rAnalyzing File ' + f)
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write('\rCompleted!' + '\n')
    time.sleep(0.2)

t = threading.Thread(target=load_analyzer)
t.start()

#process timer
time.sleep(10)
done = True