import hashlib
m = hashlib.base64()
m.update(b'Pedro eres muy fuerte')
print(m.digest())

