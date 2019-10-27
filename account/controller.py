import os.path
import json
import time
import account.file_handler as file_handler

'''
Mengambil dan mengembalikan data account dari file.
Mengembalikan object kosong {} kalau file tidak ditemukan.
'''
def get_accounts():
  data = file_handler.read('data/account.json')

  if data == None:
    return {}

  return data

'''
Mengambil data account dari file dan menambahkan account baru.
id dari account otomatis di-generate dari waktu saat ini.
Menyimpan kembali data yang sudah ditambah ke file.
'''
def new(account):
  data = get_accounts()

  account_id = int(time.time())
  data[str(account_id)] = account

  file_handler.save('data/account.json', data)

'''
Mengambil data account dari file dan 
mengubah data account berdasarkan id yang diberikan.
Menyimpan kembali data yang sudah dimodifikasi ke file.

Mengembalikan 1 kalau ada data account yang dimodifikasi, 
mengembaikan 0 kalau data account dengan id yang diberikan tidak ditemukan.
'''
def update(id, account):
  data = get_accounts()

  if id in data:
    data[id] = account
    file_handler.save('data/account.json', data)

    return 1

  return 0

'''
Mengambil data account dari file dan 
menghapus data account berdasarkan id yang diberikan.
Menyimpan kembali data yang sudah dikurangi ke file.

Mengembalikan 1 kalau ada data account yang duhapus, 
mengembaikan 0 kalau data account dengan id yang diberikan tidak ditemukan.
'''
def delete(id):
  data = get_accounts()

  if id in data:
    del data[id]
    file_handler.save('data/account.json', data)

    return 1

  return 0
