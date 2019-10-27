'''
Kode pendukung untuk membaca dan menyimpan JSON dari file.
'''

import os
import json
import errno

def save(filepath, data):
  if not os.path.exists(os.path.dirname(filepath)):
    try:
      os.makedirs(os.path.dirname(filepath))
    except OSError as exc:
      if exc.errno != errno.EEXIST:
        raise

  with open(filepath, 'w+') as outfile:
    json.dump(data, outfile)

def read(filepath):
  file_exists = os.path.isfile(filepath)

  if not file_exists:
    return None

  with open(filepath, 'r') as sourcefile:
    return json.load(sourcefile)
