'''
@author:Maifeng
@file:wy_api.py
@time:2018/6/1719:15

'''
# -*- coding: utf-8 -*-
import requests, base64, os, json
from wy_api.wy_config import WY_DOWNLOAD_URL, WY_SEARCH_URL ,HEADERS
from  binascii import hexlify
from Crypto.Cipher import AES
class Encrypyed():
    '''传入歌曲的ID，加密生成'params'、'encSecKey 返回'''
    def __init__(self):
        self.pub_key = '010001'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'

    def create_secret_key(self, size):
        return hexlify(os.urandom(size))[:16].decode('utf-8')

    def aes_encrypt(self, text, key):

        pad = 16 - len(text) % 16
        text = text + chr(pad) * pad
        encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, b'0102030405060708')
        ciphertext = encryptor.encrypt(text.encode('utf-8'))
        ciphertext = base64.b64encode(ciphertext).decode('utf-8')
        return ciphertext


    def rsa_encrpt(self, text, pubKey, modulus):
        text = text[::-1]
        rs = pow(int(hexlify(text.encode('utf-8')), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)

    def work(self, ids, br=128000):
        text = {'ids': [ids], 'br': br, 'csrf_token': ''}
        text = json.dumps(text)
        i = self.create_secret_key(16)
        encText = self.aes_encrypt(text, self.nonce)
        encText = self.aes_encrypt(encText, i)
        encSecKey = self.rsa_encrpt(i, self.pub_key, self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data

    def search(self, text):
        text = json.dumps(text)
        i = self.create_secret_key(16)
        encText = self.aes_encrypt(text, self.nonce)
        encText = self.aes_encrypt(encText, i)
        encSecKey = self.rsa_encrpt(i, self.pub_key, self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data

class wy_api(object):
    def __init__(self):
        super(wy_api, self).__init__()

        self.download = WY_DOWNLOAD_URL

        self.search_url = WY_SEARCH_URL

        self.headers = HEADERS

        self.s = requests.session()

        self.ep = Encrypyed()

    def get_user_search(self, user_key):
        if user_key:
            text = {'s': user_key, 'type': 1, 'offset': 0, 'sub': 'false', 'limit': 9}
            data = self.ep.search(text)
            user_songs = []
            try:
                response_search = self.s.post(self.search_url, data=data, headers=self.headers)
                if response_search.status_code == 200:
                    results = response_search.json()
                    if 'result' in results:
                        results = results['result']
                        if 'songs' in results:
                            songs = results['songs']
                            for i, song in enumerate(songs):
                                name = song['name']
                                ID  = song['id']
                                if type(song['ar']) == dict:
                                    author = song['ar']['name']
                                else:
                                    author = song['ar'][0]['name']

                                info = {
                                    'num':i,
                                    'name':name,
                                    'ID':ID,
                                    'author':author,
                                }
                                user_songs.append(info)
                            return user_songs
                        else:
                            return None
                    else:
                        return None
                else:
                    return None

            except Exception as e:
                print('get_user_search:',e)
        else:
            return None

    def get_user_song(self, user_song):
        if user_song:
            ID = user_song['ID']
            name = user_song['name']
            url = self.download + str(ID) + '.mp3'
            try:
                resp_song = self.s.get(url)
                if resp_song.status_code == 200:
                    self.save(name, resp_song.content)
                else:
                    return None
            except Exception as e:
                print('download fail:',e)

    def save(self, file_name, content):
        with open(file_name + '.mp3', 'wb') as f:
            f.write(content)
            print('下载成功:',file_name)


