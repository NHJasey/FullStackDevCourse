import hashlib

def hash_str(s):
	return hashlib.md5(s).hexdigest()

def make_secure_val(s):
	return "%s,%s" % (s, hash_str(s))

def check_secure_val(h):
	val = h.split(',')[0]
	if h == make_secure_val(val):
		return val

# first run this with the string you would like and run
print make_secure_val("Hello World!")


#then uncomment this/comment line 15 and pass the value you got below to test
#print check_secure_val("Hello World!,ed076287532e86365e841e92bfc50d8c")
