from jose import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key

payload = {
"sub": "1234560123",
"name": "Axl Rose",
"iat": "1387654321"
}

secret = None
with open("./private-key.key", 'rb') as f:
    secret = f.read()
    f.close()

priv_key = load_pem_private_key(secret, password=None, backend=default_backend())
token = jwt.encode(payload, secret, algorithm='RS256')

print(token)