import sys
import dns.resolver
from colorama import Fore, Style

print (Fore.RED + """                             

   _____ __  ______  ____  ____  __  ______    _____   __
  / ___// / / / __ )/ __ \/ __ \/  |/  /   |  /  _/ | / /
  \__ \/ / / / __  / / / / / / / /|_/ / /| |  / //  |/ / 
 ___/ / /_/ / /_/ / /_/ / /_/ / /  / / ___ |_/ // /|  /  
/____/\____/_____/_____/\____/_/__/_/_/  |_/___/_/ |_/   
                  / __ \/ | / / ___/                     
                 / / / /  |/ /\__ \                      
                / /_/ / /|  /___/ /                      
    ____  _____/_____/_/_|_//____/  ____________         
   / __ \/ ____/ ___// __ \/ /| |  / / ____/ __ \        
  / /_/ / __/  \__ \/ / / / / | | / / __/ / /_/ /        
 / _, _/ /___ ___/ / /_/ / /__| |/ / /___/ _, _/         
/_/ |_/_____//____/\____/_____/___/_____/_/ |_|          
                                                         

        """)
print(Style.RESET_ALL)



arguments = sys.argv

try:
    domain = arguments[1]
    wordlist = arguments[2]
except:
    print(Fore.RED + "Missing arguments!")
    sys.exit(1)


try:
    read_list = open(wordlist).read().splitlines()
except:
    print(Fore.RED + "Non existent or unvalid file!")
    sys.exit(1)


for line in read_list:
    subdomain = (line + "." + domain)
    try:
        responses = dns.resolver.resolve(subdomain, 'a')
        for result in responses:
            print(Fore.GREEN + subdomain, result)
    except:
        pass
