import random
import string
import hashlib

def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(8))

def pw_salt(name, pw):
	salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h, salt)

print pw_salt('frank', 'password1')
