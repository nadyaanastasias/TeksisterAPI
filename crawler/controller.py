from bs4 import BeautifulSoup
import crawler.request as request
import json
  
def get_bicycles(page=1):
  '''
  Akses web bukalapak di url: https://www.bukalapak.com/c/sepeda/fullbike.
  '''
  endpoint = '/c/sepeda/fullbike'
  response = request.get(endpoint, page)

  '''
  Bad news for crawler is, it doesn't last long :)
  Karna Bukalapak bisa ganti page html-nya kapan aja :)
  Walaupun harusnya jarang.
  Lebih baik page html-nya kita save ke file supaya bisa
  kita cek kalau ada perubahan html.
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
  Akses atribut dari elemen html yang memuat datay ang dicari.

  nama sepeda di atribut 'data-name'
  harga sepeda di atribut 'data-value'
  tipe sepeda di atribut 'data-subcategory2'

  Nama atributnya juga dicari di source html-nya Bukalapak.
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
