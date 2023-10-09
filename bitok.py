import requests
import pandas as pd
from requests import Session
import secrets
from pprint import pprint as pp
import openpyxl
from datetime import datetime
from decouple import config
current_datetime = datetime.now()
token=config('token')
y=(str(current_datetime.day),str(current_datetime.month),str(current_datetime.year))
y=str(".".join(y))
#/v1/cryptocurrency/map
class CMC:
  # https://coinmarketcap.com/api/documentation/v1/
  def __init__(self, token):
    self.apiurl = 'https://pro-api.coinmarketcap.com'
    self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
    self.session = Session()
    self.session.headers.update(self.headers)

  def getAllCoins(self):
    url = self.apiurl + '/v1/cryptocurrency/map'
    r = self.session.get(url)
    data = r.json()['data']
    return data

  def getTicker(self, symbol):
    url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol}
    r = self.session.get(url, params=parameters)
    data = r.json()['data']
    return data
  def getRank(self, symbol):
    symbol=str(symbol)
    url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol}
    r = self.session.get(url, params=parameters)
    data = r.json()['data'][symbol]['cmc_rank']
    return data

  def getPrice(self, symbol):
    url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol}
    r = self.session.get(url, params=parameters)
    data = r.json()['data'][symbol]['quote']['USD']['price']
    return data

def inp():
  global what
  what = str(input("all//all_e//ticker//rank//price//ticker_e?"))
  global ticker
  global n
  if (what == 'all'):  # Вывод всех монет
    pp(cmc.getAllCoins())

  if (what == 'all_e'):  # Вывод рангов всех монет в эксель
    return(cmc.getAllCoins())
  if (what == 'ticker'):  # Вывод определенной монеты
    n=int(input('Кол-во тикеров'))
    ticker = [] * n
    a = input('Введите тикер=')
    for i in range(n):
      ticker.append(a)
      if(i==(n-1)):break
      a = input('Введите тикер=')

    pp(cmc.getTicker(",".join(ticker)))
    return cmc.getTicker(",".join(ticker))

  if (what == 'ticker_e'):  # Вывод рангов в эксель
    n=int(input('Кол-во тикеров'))
    ticker = [] * n
    a = input('Введите тикер=')
    for i in range(n):
      ticker.append(a)
      if (i == (n - 1)): break
      a = input('Введите тикер=')


    return cmc.getTicker(",".join(ticker))

  if (what == 'rank'):    #вывод ранга
    ticker = str(input('Введите тикер='))
    rank = cmc.getRank(ticker)
    print('Rank is -', rank)
    return rank
  if (what == 'price'): #вывод цены
    ticker = str(input('Введите тикер='))
    price = cmc.getPrice(ticker)
    print('Price is -', price)
    return price

def d_f(info):  #Вывод рангов заданных монет
  global x
  x = {str(ticker[0]): str(info[str(ticker[0])]['cmc_rank'])}
  for i in range(1,n):
    x[str(ticker[i])]=str(info[str(ticker[i])]['cmc_rank'])
  df=pd.DataFrame([x])
  df.to_excel('./Ranks.xlsx')

def d_f_all(info):   #Вывод рангов 5000 монет
  global x
  x = {'Date': y}
  x[str(info[1]['name'])]=str(info[1]['rank'])
  for i in range(1,5000):
    x[str(info[i]['name'])]=str(info[i]['rank'])
  df=pd.DataFrame([x])
  new_df=df
  old_df = pd.read_excel('D:\pyprojects\Bitok\Ranks_all.xlsx', sheet_name="sheet_1")
  frames = [old_df, new_df]
  result = pd.concat(frames)
  result.to_excel("D:\pyprojects\Bitok\Ranks_all.xlsx", sheet_name="sheet_1", index=False)

def main():
  global cmc,info
  cmc = CMC(token)
  info = inp()
  print(info[1])
  if (what == 'ticker_e'):
    d_f(info)
  if (what == 'all_e'):
    d_f_all(info)

  k = input("press close to exit")


if __name__ == "__main__":
   main()
