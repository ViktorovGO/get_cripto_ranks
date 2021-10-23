import requests
import pandas as pd
from requests import Session
import secrets
from pprint import pprint as pp
import openpyxl
import bitok as bit
cmc = bit.CMC(bit.token)
info=cmc.getAllCoins()
bit.d_f_all(info)
k = input("press close to exit")