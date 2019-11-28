'''

Made with Python v3.x.x.

Command to install libraries:
  - pip install --user requests
  - pip install --user beautifulsoup4

Command to run program:
  - python main.py

'''

import server.server as server
import server.response as response
import crawler.controller as crawler
import account.controller as account

'''
Endpoint untuk akses data. Bisa diakses di http://localhost:3000/tas.

Di web Bukalapak banyak page-nya. Bisa ganti page pake query string,
misal http://localhost:3000/tas?page=10.
'''
@server.GET('/tas')
def search_tas(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_tas(int(page))

  return response.json(data)

@server.GET('/sandal')
def search_sandal(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_sandal(int(page))

  return response.json(data)

@server.GET('/kaos')
def search_kaos(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_kaos(int(page))

  return response.json(data)

@server.GET('/jumpsuit')
def search_sandal(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_jumpsuit(int(page))

  return response.json(data)

@server.GET('/poloshirt')
def search_poloshirt(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_poloshirt(int(page))

  return response.json(data)

@server.GET('/keretabayi')
def search_keretabayi(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_keretabayi(int(page))

  return response.json(data)

@server.GET('/kursimobil')
def search_kursimobil(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_kursimobil(int(page))

  return response.json(data)

@server.GET('/makananbayi')
def search_makananbayi(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_makananbayi(int(page))

  return response.json(data)

@server.GET('/perlengkapanmandi')
def search_perlengkapanmandi(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_perlengkapanmandi(int(page))

  return response.json(data)

@server.GET('/handuk')
def search_handuk(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_handuk(int(page))

  return response.json(data)

@server.GET('/mainan')
def search_mainan(args):
  page = 1

  if 'page' in args['query']:
    page = args['query']['page']

  data = crawler.get_mainan(int(page))

  return response.json(data)

'''
Endpoint untuk liat account-account yang tersimpan.
'''

@server.GET('/account')
def get_accounts(args):
  data = account.get_accounts()

  return response.json({'data': data})

'''
Endpoint untuk menyimpan account baru dengan POST method.
'''
@server.POST('/account')
def insert_account(args):
  account.new(args['body'])
  message = {'message': 'successfully save new account'}

  return response.json(message)

'''
Endpoint untuk memodifikasi data account berdasarkan id-nya dengan PUT method.

Data yang mau diubah dicari dulu id-nya, dengan GET /account.
id dari account dimasukan ke request path, misalnya PUT /account/1571553842.
'''
@server.PUT('/account/:id')
def update_account(args):
  data = args['body']

  updated_count = account.update(args['params']['id'], data)

  if updated_count == 0:
    return response.json({'message': 'nothing is updated'})
  else:
    return response.json({'message': 'successfully update account'})

'''
Endpoint untuk menghapus data account berdasarkan id-nya dengan DELETE method.

Data yang mau dihapus dicari dulu id-nya, dengan GET /account.
id dari account dimasukan ke request path, misalnya DELETE /account/1571553842.
'''
@server.DELETE('/account/:id')
def delete_account(args):
  deleted_count = account.delete(args['params']['id'])

  if deleted_count == 0:
    return response.json({'message': 'nothing is deleted'})
  else:
    return response.json({'message': 'successfully delete account'})

'''
Nothing. Just. Hello :)
'''
@server.GET('/')
def hello(args):
  print(args)

  data = {'message': 'Hello!'}

  return response.json(data)

'''
Start server di port 3000.
'''
if __name__ == "__main__":
  print('Server listening on port 3500.')
  server.start(3500)
