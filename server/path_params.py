'''
Kode pendukung untuk mengambil variabel dari endpoint, atau disebut "Path Parameters".
Misalnya endpoint /account/:id mengandung variabel "id"
'''

'''
Memeriksa apakah suatu subpath merupakan variabel (param).
'''
def is_param(subpath):
  return len(subpath) > 0 and subpath[0] == ':'

'''
Mengumpulkan dan mengembalikan path parameters dari suatu path.
'''
def collect_from(path):
  params = []
  subpaths = path.split('/')[1:]

  for i in range(len(subpaths)):
    subpath = subpaths[i]

    if is_param(subpath):
      param = {
        'index': i,
        'name': subpath[1:]
      }
      params.append(param)   

  return params 

'''
Menghilangkan subpath yang merupakan path parameter dan mengembalikan hasilnya.
Misalnya, /account/:id diubah menjadi /account/.*
Tujuannya untuk membantu server dalam "path matching" saat melayani request.
'''
def clean(path):
  subpaths = path.split('/')[1:]
  cleaned_path = ''

  for subpath in subpaths:
    cleaned_path += '/'
    if is_param(subpath):
      cleaned_path += '.*'   
    else:
      cleaned_path += subpath
  
  return cleaned_path
