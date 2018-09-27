from Crypto.Cipher import AES
from base64 import b64decode

if __name__ == '__main__':
	content = b64decode(open('7.txt').read())
	key = "YELLOW SUBMARINE"
	cipher = AES.new(key, AES.MODE_ECB)
	print cipher.decrypt(content)