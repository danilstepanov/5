__author__ = 'nurgaliev'
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5, AES, DES3
from Crypto.Hash import SHA, SHA256, HMAC
from Crypto.Util import Counter
from ssrv_orm import *
import Database as DB
import system_command
import struct, sqlalchemy
import Padding

class KeyLadder(object):

    def __init__(self):
        self.db = DB.Database()
        path_to_bbmk = '%s%s' % (system_command.get_homedir_in(), '/bbmk_clean.dat')
        self.priv_dbmk = RSA.importKey(open(path_to_bbmk).read())
        self.clear_kmbk = self.get_plain_kmbk_from_db()
        self.version = 0
        self.plain_le_set = ''

    def get_plain_kmbk_from_db(self):
        query = "select kmbk_value from fwkeys.ssrv_ladder_keys"
        kmbk_enc = self.db.conn.execute(query).fetchone()[0]
        dsize = SHA.digest_size
        sentinel = Random.new().read(15 + dsize)
        cipher = PKCS1_v1_5.new(self.priv_dbmk)
        clear_kmbk = cipher.decrypt(str(kmbk_enc),sentinel)
        return clear_kmbk

    def get_kmbe_key(self, index):
        IV = '00000000000000000000000000000000'.decode('hex')
        query = "select kmbe_value from fwkeys.ssrv_kmb_ekeys where kmbe_id = %s" % index
        kmbe_enc = self.db.conn.execute(query).fetchone()[0]
        aes_obj = AES.new(self.clear_kmbk, AES.MODE_CFB, (IV))
        clear_kmbe = aes_obj.decrypt(str(kmbe_enc))
        return clear_kmbe

    def get_kmbh_key(self, index):
        IV = '00000000000000000000000000000000'.decode('hex')
        query = "select kmbh_value from fwkeys.ssrv_kmb_hkeys where kmbh_id = %s" % index
        kmbh_enc = self.db.conn.execute(query).fetchone()[0]
        aes_obj = AES.new(self.clear_kmbk, AES.MODE_CFB, IV)
        clear_kmbh = aes_obj.decrypt(kmbh_enc)
        return clear_kmbh

    def decrypt_buf(self, key, buf, iv='', aes_mode='ECB'):
        if aes_mode == 'CBC':
            decr_buf = AES.new(key, AES.MODE_CBC, iv).decrypt(buf)
            #print decr_buf.encode('hex')
            decr_buf = Padding.removePadding(decr_buf)
        if aes_mode == 'ECB':
            decr_buf = AES.new(key, AES.MODE_ECB).decrypt(buf)
        return decr_buf

    def decrypt_buf_by_kmi_ladder(self, buf, param_for_iv):
        kmbe_ind = struct.unpack('<H', buf[2:4])[0]
        kmbe_key = self.get_kmbe_key(kmbe_ind)
        combination_for_iv = '%s%s%s' % (struct.pack('<L', param_for_iv), buf[2:4], buf[:2])
        iv = SHA256.new(combination_for_iv).digest()[:16]
        decr_buf = self.decrypt_buf(kmbe_key, buf[4:-32], iv, 'CBC')
        return decr_buf