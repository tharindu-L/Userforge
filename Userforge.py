import argparse
from itertools import product
from colorama import Fore, Style, init

def banner():
    print(Fore.CYAN + Style.BRIGHT +r"""
          
██╗   ██╗███████╗███████╗██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██║   ██║███████╗█████╗  ██████╔╝█████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
╚██████╔╝███████║███████╗██║  ██║██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
"""+Fore.YELLOW +Style.BRIGHT+"""
            UserForge | Ethical Hacking Tool
""")

def parse_args():
    parser = argparse.ArgumentParser(description="UserForge - Ethical Hacking Tool")
    parser.add_argument("-n", "--name", help="Base name for username generation", required=True)
    parser.add_argument("-r", "--role", help="Role to append to the username", required=True)
    parser.add_argument("-s", "--separator", help="Separator between name and role", default=",_")
    return parser.parse_args()


def varients(word):
    return[word,word.capitalize(),word.upper()]

def main():
    banner()
    args=parse_args()
    names=args.name.split(",")
    roles=args.role.split(",")
    separators=args.separator.split(",")

    with open("usernames.txt","w") as f:
        for names,roles,separators in product(names,roles,separators):
            for namev,rolev in product(varients(names),varients(roles)):
                f.write(f"{namev}{separators}{rolev}\n")

if __name__ == "__main__":
    main()