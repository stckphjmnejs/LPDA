
import time , sys , os , pickle , colorama , random
from colorama import Fore, Back, Style
from colorama import init
init()


kol2 = 5
version = 'Бета'
servies_k = '30'


def banner3():
  print(Fore.YELLOW)
  banner2 = f"""


           ░██████╗████████╗░█████╗░░█████╗░██╗░░██╗██╗░░██╗░█████╗░██╗░░░░░███╗░░░███╗  
           ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝██║░░██║██╔══██╗██║░░░░░████╗░████║  
           ╚█████╗░░░░██║░░░██║░░██║██║░░╚═╝█████═╝░███████║██║░░██║██║░░░░░██╔████╔██║  
           ░╚═══██╗░░░██║░░░██║░░██║██║░░██╗██╔═██╗░██╔══██║██║░░██║██║░░░░░██║╚██╔╝██║  
           ██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝██║░╚██╗██║░░██║╚█████╔╝███████╗██║░╚═╝░██║  
           ╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░░░░╚═╝  

           ░█████╗░░█████╗░██████╗░██████╗░░█████╗░██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
           ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
           ██║░░╚═╝██║░░██║██████╔╝██████╔╝██║░░██║██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
           ██║░░██╗██║░░██║██╔══██╗██╔═══╝░██║░░██║██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
           ╚█████╔╝╚█████╔╝██║░░██║██║░░░░░╚█████╔╝██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
           ░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
                        \033[32mv.{version}\033[33m [Creator: \033[32mStockholm\033[33m]
                            You'r system - [\033[32mLinux\033[33m/\033[32mAndroid\033[33m]
                                    services - [\033[32m{servies_k}\033[33m]
                                                        """
  for char in banner2:
    sys.stdout.write(char)
    sys.stdout.flush()




def banner4():
  print(Fore.YELLOW)
  banner = f"""

           ░██████╗████████╗░█████╗░░█████╗░██╗░░██╗██╗░░██╗░█████╗░██╗░░░░░███╗░░░███╗  
           ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝██║░░██║██╔══██╗██║░░░░░████╗░████║  
           ╚█████╗░░░░██║░░░██║░░██║██║░░╚═╝█████═╝░███████║██║░░██║██║░░░░░██╔████╔██║  
           ░╚═══██╗░░░██║░░░██║░░██║██║░░██╗██╔═██╗░██╔══██║██║░░██║██║░░░░░██║╚██╔╝██║  
           ██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝██║░╚██╗██║░░██║╚█████╔╝███████╗██║░╚═╝░██║  
           ╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░░░░╚═╝  

           ░█████╗░░█████╗░██████╗░██████╗░░█████╗░██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
           ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
           ██║░░╚═╝██║░░██║██████╔╝██████╔╝██║░░██║██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
           ██║░░██╗██║░░██║██╔══██╗██╔═══╝░██║░░██║██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
           ╚█████╔╝╚█████╔╝██║░░██║██║░░░░░╚█████╔╝██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
           ░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
                                                                          \033[32mv.{version}\033[33m [Creator: \033[32mStockholm\033[33m]
                                                                             You'r system - [\033[32mLinux\033[33m/\033[32mAndroid\033[33m]
                                                                                     services - [\033[32m{servies_k}\033[33m]
      __________________________________________________________________________________________
      |                                                                                        |
      | [\033[32mCORPORATION\033[33m] - stockholmUE(с)                                                          |
      |                                                                                        |
      | [\033[32mContact\033[33m] - https://telegram.com/user/stockholmUE | https://github.com/id/stpckjlmne=id]|
      |________________________________________________________________________________________|

    """
  for char in banner:
    sys.stdout.write(char)
    sys.stdout.flush()





def banner1an():
    start_time = time.time()
    CLOSE_AFTER = kol2
    banner1 = f"""\033[31m
                             (                    (

██████╗░██████╗░██╗██╗░░░██╗░█████╗░████████╗███████╗  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██║██║░░░██║██╔══██╗╚══██╔══╝██╔════╝  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██████╔╝██║╚██╗░██╔╝███████║░░░██║░░░█████╗░░  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔═══╝░██╔══██╗██║░╚████╔╝░██╔══██║░░░██║░░░██╔══╝░░  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██║░░╚██╔╝░░██║░░██║░░░██║░░░███████╗  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
                        \033[32mv.{version}\033[33m [Creator: \033[32mStockholm\033[33m]
                            You'r system - [\033[32mLinux\033[33m/\033[32mAndroid\033[33m]
                                    services - [\033[32m{servies_k}\033[33m]
                                                        """
    r=0
    while True:
        if time.time() > start_time + float(CLOSE_AFTER):
            break

        if r == 0:
            print(banner1.replace(")", "(").replace("/", "╲"))
            time.sleep(0.1)
            os.system("clear")
            r+=1
        elif r == 1:
            print(banner1.replace("(", ")").replace("╲", "/"))
            time.sleep(0.1)
            os.system("clear")
            r-=1





def banner2an():
    start_time = time.time()
    CLOSE_AFTER = kol2
    print(Fore.YELLOW)
    banner2 = f"""

           ░██████╗████████╗░█████╗░░█████╗░██╗░░██╗██╗░░██╗░█████╗░██╗░░░░░███╗░░░███╗  
           ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝██║░░██║██╔══██╗██║░░░░░████╗░████║  
           ╚█████╗░░░░██║░░░██║░░██║██║░░╚═╝█████═╝░███████║██║░░██║██║░░░░░██╔████╔██║  
           ░╚═══██╗░░░██║░░░██║░░██║██║░░██╗██╔═██╗░██╔══██║██║░░██║██║░░░░░██║╚██╔╝██║  
           ██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝██║░╚██╗██║░░██║╚█████╔╝███████╗██║░╚═╝░██║  
           ╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░░░░╚═╝  

           ░█████╗░░█████╗░██████╗░██████╗░░█████╗░██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
           ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
           ██║░░╚═╝██║░░██║██████╔╝██████╔╝██║░░██║██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
           ██║░░██╗██║░░██║██╔══██╗██╔═══╝░██║░░██║██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
           ╚█████╔╝╚█████╔╝██║░░██║██║░░░░░╚█████╔╝██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
           ░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
                                                                          \033[32mv.{version}\033[33m [Creator: \033[32mStockholm\033[33m]
                                                                             You'r system - [\033[32mLinux\033[33m/\033[32mAndroid\033[33m]
                                                                                     services - [\033[32m{servies_k}\033[33m]
      __________________________________________________________________________________________
      |                                                                                        |
      | [\033[32mCORPORATION\033[33m] - stockholmUE(с)                                                          |
      |                                                                                        |
      | [\033[32mContact\033[33m] - https://telegram.com/user/stockholmUE | https://github.com/id/stpckjlmne=id]|
      |________________________________________________________________________________________|

    """
    i=0
    while True:
       if time.time() > start_time + float(CLOSE_AFTER):
           break
       if i == 0:
            print(banner2.replace(")", "(").replace("/", "╲"))
            time.sleep(0.1)
            os.system("cls")


            i+=1
       elif i == 1:
            print(banner2.replace("(", ")").replace("╲", "/"))
            time.sleep(0.1)
            os.system("cls")
            i-=1





def banner_atack():
  print(Fore.YELLOW)
  print("""        _       _             _      ____  _             _   _
       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _
      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                                     |___/ ......""")
  print ("[                    ] \033[94m5%\033[0m")
  time.sleep(0.1)
  print ("[=====               ] \033[94m35%\033[0m")
  time.sleep(1)
  print ("[==========          ] \033[94m52%\033[0m")
  time.sleep(1)
  print ("[====================] \033[94m100%\033[0m")
  time.sleep(2)
  print(Fore.RED)
  print("stock corp start attack ||" + str(_phone)+ "||\033[94mDDSMS-Attack-S{C}\033[0m")

message = "\033[94m \n -|| start w8 pls ||- \033[0m"
message2 = " please use ENTER  for continuation ..."








def banner_atack2():
  print(Fore.GREEN)
  baner = """
			┏━━━┓┏┓     ┏┓
			┃┏━┓┣┛┗┓   ┏┛┗┓
			┃┗━━╋┓┏╋━━┳┻┓┏┛
			┗━━┓┃┃┃┃┏┓┃┏┫┃
			┃┗━┛┃┃┗┫┏┓┃┃┃┗┓
			┗━━━┛┗━┻┛┗┻┛┗━┛....."""
  print(baner)
  print ("[                    ] \033[94m5%\033[0m")
  time.sleep(0.1)
  print ("[=====               ] \033[94m35%\033[0m")
  time.sleep(1)
  print ("[==========          ] \033[94m52%\033[0m")
  time.sleep(1)
  print ("[====================] \033[94m100%\033[0m")
  time.sleep(2)
  print(Fore.RED)
  print("stock corp start attack ||" + str(_phone)+ "||\033[94mDDSMS-Attack-S{C}\033[0m")
