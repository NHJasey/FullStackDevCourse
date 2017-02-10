import random
import string
import hashlib

def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(8))

def pw_salt(name, pw, salt = None):
	if not salt:
		salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
	salt = h.split(',')[1]
	return h == pw_salt(name, pw, salt)

h = pw_salt('frank', 'password1')
print valid_pw('frank', 'password1', h)

