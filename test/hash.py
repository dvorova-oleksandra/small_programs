import hashlib

s = "Python Bootcamp"
#хешування методом MD5
hash_object = hashlib.md5(s.encode())
print(hash_object.hexdigest())

#хешування методом SHA1
hash_object2 = hashlib.sha1(s.encode())
hex_dig = hash_object2.hexdigest()
print(hex_dig)