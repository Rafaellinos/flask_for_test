"""
ACR122u-A9
Mifare Classic 1K
pyscard (1.9.9)

"""
import time
import smartcard
from smartcard.util import toHexString

BLOCK_NUMBER = 0x00 #default
KEY_A = [0xFF, 0x82, 0x00, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
AUTH_BLOCK = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, BLOCK_NUMBER, 0x60, 0x00]
READ_16_BYTES = [0xFF, 0xB0, 0x00, BLOCK_NUMBER, 0x10]

class reader():

    def make_conn(self):
        reader = smartcard.System.readers()
        if not reader:
            print("Please, connect a reader")
            return
        conn = reader[0].createConnection()
        conn.connect()
        print("Successful connection with "+str(reader[0]))
        return conn

    def execute_command(self, conn, command):
        response = conn.transmit(command)
        return response

    def check_action(self, response):
        if response[1] == 144:
            return True
        return False

    def load_key_a(self, conn):
        #conn = self.make_con()
        response = self.execute_command(conn, KEY_A)
        if self.check_action(response):
            print("Key loaded successfully")
        else:
            print("Something wrong when loading the key A")
        
    def read(self):
        try:
            conn = self.make_conn()
            self.load_key_a(conn)
            AUTH_BLOCK[7] = 0x08
            READ_16_BYTES[3] = 0x08
            response = self.execute_command(conn, AUTH_BLOCK)
            response = self.execute_command(conn, READ_16_BYTES)
            print("Tag 8: "+toHexString(response[0]))
            return toHexString(response[0])
        except:
            return False

#res = reader()
#response = res.read()
