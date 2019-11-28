from bs4 import BeautifulSoup
import crawler.request as request
import json
  
def get_tas(page=1):
  '''
  Akses web bukalapak di url: https://www.bukalapak.com/c/fashion-wanita.
  '''
  endpoint = '/c/fashion-wanita/tas-wanita'
  response = request.get(endpoint, page)

  '''
  Dikarenakan website BukaLapak suka berganti strukturnya maka pagen htmlnya
  akan disave terlebih dahulu menjadi file supaya bisa dicek kalau ada
  perubahan pada struktur htmlnya
  '''
  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')

  '''
  Hasil request-nya di-parse pake BeautifulSoup supaya bisa akses elemen-elemen
  html-nya.
  '''
  html = BeautifulSoup(response.content, "html.parser")

  '''
  Ambil elemen html yang relevan buat ambil data yang diinginkan.
  Cara nemu elemen html-nya itu liat langsung ke source html-nya Bukalapak,
  dan dicari elemen yang memuat data yang mau diambil.
  Source html bukalapak ada di folder html.
  '''
  products = list(html.select('div[class="product-detail-track"]'))

  '''
  Akses atribut dari elemen html yang memuat data yang dicari.
  nama sepeda di atribut  data-product['name']
  harga sepeda di atribut data_product['price']
  tipe sepeda di atribut  category['structure'][2]
  '''
  
  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][2]
    })
  
  return result

def get_sandal(page=1):

  endpoint = '/c/fashion-wanita/sandal'
  response = request.get(endpoint, page)
  
  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')
    
  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))
  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][2]
    })
  
  return result

def get_kaos(page=1):

  endpoint = '/c/fashion-wanita/kaos'
  response = request.get(endpoint, page)

  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')

  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))

  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][1]
    })
  
  return result

def get_jumpsuit(page=1):
 
  endpoint = '/c/fashion-wanita/celana'
  response = request.get(endpoint, page)

  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')


  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))

  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][1]
    })
  return result

def get_poloshirt(page=1):

  endpoint = '/c/fashion-wanita/polo-shirt-1099'
  response = request.get(endpoint, page)
  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')
    
  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))

  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][1]
    })
  
  return result

'''
penambahan endpoint untuk dapat disesuaikan dengan API Lidya Jessica
'''

def get_keretabayi(page=1):

  endpoint = '/c/perlengkapan-bayi/stroller-walker'
  response = request.get(endpoint, page)
  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')
    
  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))

  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][1]
    })
  
  return result

def get_kursimobil(page=1):
  endpoint = '/c/perlengkapan-bayi/baby-carrier'
  response = request.get(endpoint, page)
  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')
    
  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))

  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][1]
    })
  
  return result

def get_mainan(page=1):
  endpoint = '/c/hobi-koleksi/mainan/mainan-lainnya'
  response = request.get(endpoint, page)
  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')
    
  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))

  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][1]
    })
  
  return result

def get_handuk(page=1):
  endpoint = '/c/rumah-tangga/kamar-mandi?from=omnisearch&from_keyword_history=false&search%5Bkeywords%5D=handuk&search_source=omnisearch_category&source=navbar'
  response = request.get(endpoint, page)
  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')
    
  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))

  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][1]
    })
  
  return result

def get_perlengkapanmandi(page=1):
  endpoint = '/c/perlengkapan-bayi/perlengkapan-mandi'
  response = request.get(endpoint, page)
  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')
    
  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))

  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][1]
    })
  
  return result

def get_makananbayi(page=1):
  endpoint = '/c/perlengkapan-bayi/makanan-711'
  response = request.get(endpoint, page)
  try:
    f = open("html/bukalapak.html","w")
    f.write(response.text)
  except:
    print('failed to save html/bukalapak.html')
    
  html = BeautifulSoup(response.content, "html.parser")

  products = list(html.select('div[class="product-detail-track"]'))

  result = []
  for product in products:
    data_product = json.loads(product['data-product'])
    category = data_product['category']

    result.append({
      'nama': data_product['name'],
      'harga': data_product['price'],
      'tipe': category['structure'][1]
    })
  
  return result