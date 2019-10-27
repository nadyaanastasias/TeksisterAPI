'''
Kode pendukung untuk menangani response dari server ke client.
'''
import json as JSON

def json(data):
  status_code = 200
  headers = { 'Content-Type': 'application/json'}
  
  return {
    'status_code': status_code,
    'headers': headers,
    'data': JSON.dumps(data)
  }

def not_found_response():
  status_code = 404
  headers = { 'Content-Type': 'application/json'}
  data = { 'message': 'page not found' }

  return {
    'status_code': status_code,
    'headers': headers,
    'data': JSON.dumps(data)
  }
