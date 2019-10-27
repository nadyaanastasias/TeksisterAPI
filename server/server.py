'''
Kode pendukung untuk mendefinisikan routing (endpoint dan http method) dan menyalakan server.
'''

from http.server import HTTPServer
import server.http_handler as http_handler

def POST(path):
  def route(handler): 
    http_handler.route('POST', path, handler)
  return route

def GET(path):
  def route(handler):
    http_handler.route('GET', path, handler)
  return route

def PUT(path):
  def route(handler):
    http_handler.route('PUT', path, handler)
  return route

def DELETE(path):
  def route(handler):
    http_handler.route('DELETE', path, handler)
  return route

def start(port):
  server = HTTPServer(('', port), http_handler.Handler)
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    pass
  server.server_close()
