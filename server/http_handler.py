'''
Kode yang berperan dalam pendefinisian pasangan endpoint dengan handler-nya.

Setiap endpoint memiliki handler.
Handler dieksekusi ketika ada request ke endpoint tertentu.
Kode di file ini yang mengatur eksekusi handler dari endpoint yang berkaitan.
'''

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import server.response as Response
import server.path_params as path_params
import json
import re

ROUTES = {
  'GET': {},
  'POST': {},
  'PUT': {},
  'DELETE': {}
}

'''
Mendefinisikan endpoint dan handler yang terkait.
'''
def route(method, path, handler):
  if method not in ROUTES:
    raise Exception('invalid http method definition')

  cleaned_path = path_params.clean(path)

  ROUTES[method][cleaned_path] = {
    'handler': handler,
    'params': path_params.collect_from(path)
  }

'''
Kelas yang bertanggung jawab untuk melayani http request dengan method GET, POST, PUT, DELETE.
'''
class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.handle_request('GET')

  def do_POST(self):
    self.handle_request('POST')

  def do_PUT(self):
    self.handle_request('PUT')

  def do_DELETE(self):
    self.handle_request('DELETE')

  '''
  Eksekutor dari setiap http method.
  1. Menyiapkan request arguments,
  2. Eksekusi handler.
  3. Pengembalian respon ke client.
  '''
  def handle_request(self, http_method):
    request_args = self.get_request_args(http_method)

    if request_args == None:
      return self.respond(Response.not_found_response())

    handler = request_args['handler']
    response = handler(request_args)
    
    self.respond(response)

  '''
  Mengatur lebih detil tentang pengembalian respon ke client.
  '''
  def respond(self, response):
    self.send_response(response['status_code'])
    self.send_header("Access-Control-Allow-Origin","*")
    headers = response['headers']
    for key in headers:
      self.send_header(key, headers[key])
    self.end_headers()
    self.wfile.write(bytes(response['data'], 'UTF-8'))

  '''
  Mengambil query string dari suatu url yang sudah di-parse dengan urllib.
  '''
  def get_query_string(self, parsed_url):
    raw_qs = parse_qs(parsed_url)
    clean_qs = {}

    for key in raw_qs:
      clean_qs[key] = raw_qs[key][0]

    return clean_qs 

  '''
  Mengambil request body yang berformat JSON.
  '''
  def get_json_body(self):
    if self.headers['Content-Length'] == None:
      return None

    content_length = int(self.headers['Content-Length'])
    raw_body = self.rfile.read(content_length)
    str_body = raw_body.decode('utf-8')
    
    return json.loads(str_body)

  '''
  Mengambil value dari path parameters.
  '''
  def get_params(self, original_path, param_keys):
    params = {}
    subpaths = original_path.split('/')[1:]

    for key in param_keys:
      params[key['name']] = subpaths[key['index']]
    
    return params

  '''
  Mengatur lebih detil pengumpulan request arguments:
  original path, known path (routing path), params, query string, request body, handler, dan http method.
  '''
  def get_request_args(self, http_method):
    request_args = {}

    url = urlparse(self.path)

    for defined_path in ROUTES[http_method]:
      if re.search(defined_path, url.path):
        param_keys = ROUTES[http_method][defined_path]['params']

        request_args['original_path'] = url.path
        request_args['known_path'] = defined_path
        request_args['params'] = self.get_params(url.path, param_keys)
        request_args['query'] = self.get_query_string(url.query)
        request_args['body'] = self.get_json_body()
        request_args['handler'] = ROUTES[http_method][defined_path]['handler']
        request_args['method'] = http_method
        
        return request_args
    
    return None
