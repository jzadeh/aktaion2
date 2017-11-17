#author:mvaouli
# Version 2.0
## Show menu ##
print(80 * '-')
print("              █████╗ ██╗  ██╗████████╗ █████╗ ██╗ ██████╗ ███╗   ██╗ ");
print("             ██╔══██╗██║ ██╔╝╚══██╔══╝██╔══██╗██║██╔═══██╗████╗  ██║ ");
print("             ███████║█████╔╝    ██║   ███████║██║██║   ██║██╔██╗ ██║ ");
print("             ██╔══██║██╔═██╗    ██║   ██╔══██║██║██║   ██║██║╚██╗██║ ");
print("             ██║  ██║██║  ██╗   ██║   ██║  ██║██║╚██████╔╝██║ ╚████║ ");
print("             ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ");
print(" ██╗   ██╗███████╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗    ██████╗     ██████╗ ");
print(" ██║   ██║██╔════╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║    ╚════██╗   ██╔═████╗ ");
print(" ██║   ██║█████╗  ██████╔╝███████╗██║██║   ██║██╔██╗ ██║     █████╔╝   ██║██╔██║ ");
print(" ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║██║   ██║██║╚██╗██║    ██╔═══╝    ████╔╝██║ ");
print("  ╚████╔╝ ███████╗██║  ██║███████║██║╚██████╔╝██║ ╚████║    ███████╗██╗╚██████╔╝ ");
print("   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝ ╚═════╝ ");
print("                               M A I N - M E N U")
print(80 * '-')
print("1: Analyze Bro HTTP Sample Using Default Model")
print("2: Analyze PCAP Sample (Bro must be installed) Using Default Model")
print("3: Analyze Bro HTTP Sample Using Phishing Model")
print("4: Demo")
print(80 * '-')

## Get input ###
choice = input('Enter your choice [1-4] : ')

### Convert string to int type ##
choice = int(choice)

### Take action as per selected menu-option ###
if choice == 1:
    print("")
elif choice == 2:
    print("")
elif choice == 3:
    print("")
elif choice == 4:
    print("")
else:  ## default ##
    print("Invalid number. Try again...")