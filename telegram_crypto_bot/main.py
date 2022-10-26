import requests, json

from requests import Session
import secrets


TOKENS_NAMES = []
TOP_TOKENS = []


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.API_KEY,
}

r = requests.get(url, headers=headers)


class Coinmarketcap:
  def __init__(self, token):
      self.apiurl = 'https://pro-api.coinmarketcap.com'
      self.headers = headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': secrets.API_KEY,}
      self.session = Session()
      self.session.headers.update(self.headers) 
  
  def getAllToken(self):
      url = self.apiurl + '/v1/cryptocurrency/map'
      r = self.session.get(url)
      data = r.json()['data']
 
      with open('./mapcoinmarketcap.json','w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
      for tokens in data:
        id = tokens['id']
        name = tokens['name']
        rank = tokens['rank']       
        symbol = tokens['symbol']
        is_active = tokens['is_active']
        
        '''Search all active tokens'''
        if is_active == 1:
           TOKENS_NAMES.append(name)
        if rank <= 100:
            TOP_TOKENS.append(str(name) + ' - ' + str(rank))
               
          
  def priceAllToken(self):
        pass
  def xmli_info(self):
        
        pass
c = Coinmarketcap(secrets.API_KEY)

print(c.getAllToken())
print(TOP_TOKENS)
print(len(TOP_TOKENS))