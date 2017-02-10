import random
import string

def make_salt():
	return "".join(random.choice(string.letters) for x in xrange(8))

print make_salt()
