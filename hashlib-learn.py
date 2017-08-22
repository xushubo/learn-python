import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md4 = hashlib.md5()
md4.update('how to use md5 in '.encode('utf-8'))
md4.update('python hashlib?'.encode('utf-8'))
print(md4.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

sha2 = hashlib.sha1()
sha2.update('how to use sha1 in '.encode('utf-8'))
sha2.update('python hashlib?'.encode('utf-8'))
print(sha2.hexdigest())

sha3 = hashlib.sha256()
sha3.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha3.hexdigest())

def calc_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

print(calc_md5('how to use md5 in python hashlib?'))


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(username, password):
	md5_date = db[username]
	temp_md5 = hashlib.md5()
	temp_md5.update(password.encode('utf-8'))
	temp_md5_data = temp_md5.hexdigest()
	if md5_date == temp_md5_data:
		print('password true')
		return True
	else:
		print('password false')
		return False

login('michael', '123456')

account_db = {}

def register(username, password):
	account_db[username] = calc_md5(password + username + 'the-Salt')

def login_for_Salt(username, password):
	md5_salt_date = account_db[username]
	temp_md5_salt_date = calc_md5(password + username + 'the-Salt')
	if md5_salt_date == temp_md5_salt_date:
		print('login sucess')
		return True
	else:
		print('password error')
		return False

register('lucky', '123456')
login_for_Salt('lucky', '123456')