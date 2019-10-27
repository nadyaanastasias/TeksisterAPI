'''
Kode pendukung untuk request halaman web.
'''

import requests

BASE_URL = 'https://www.bukalapak.com'

def get(endpoint, page=1):
  if page > 1:
    endpoint += '?page=' + str(page)

  return requests.get(BASE_URL + endpoint)
