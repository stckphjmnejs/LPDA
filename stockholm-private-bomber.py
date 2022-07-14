
#   Version 12.1
import requests, random, datetime, sys, time, argparse, os , colorama ,pickle
from colorama import *
from Banners import *
from ServesSMS import *
from Message import *
from Function import *
init()

os.system("title stockholm-private-bomber")
version = 'Бета'

#Баннер cпамера
check_update()
time.sleep(1.8)
OSystem()
start()
