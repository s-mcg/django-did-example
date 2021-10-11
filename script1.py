from cryptography.hazmat.primitives import serialization
import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

#generate private key, create public key from it, get bytes from keys
private_key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
    key_size=2048)
public_key = private_key.public_key()

private_bytes = private_key.private_bytes(
  encoding=serialization.Encoding.PEM, \
  format=serialization.PrivateFormat.PKCS8, \
  encryption_algorithm=serialization.NoEncryption() \
)
public_bytes = public_key.public_bytes(
  encoding=serialization.Encoding.PEM, \
  format=serialization.PublicFormat.PKCS1 \
)

# decode to printable strings
private_key_str = private_bytes.decode('utf-8')
public_key_str = public_bytes.decode('utf-8')

with open('public-key.key', 'wb') as file_out:
  file_out.write(public_bytes)
  print('public key written to public-key.key')
  file_out.close()

with open('private-key.key', 'wb') as file_out:
  file_out.write(private_bytes)
  print('private key written to private-key.key')
  file_out.close()

#add public key to json template
did_json = {
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "did:example:123456789abcdefghi",
  "authentication": [{
    "id": "did:example:123456789abcdefghi#keys-1",
    "type": "RsaSignatureAuthentication2018",
    "controller": "did:example:123456789abcdefghi",
    "publicKeyMultibase": "changeme"
  }]
}
did_json["authentication"][0]["publicKeyMultibase"] = public_key_str
with open('public-did.json', 'w') as file_out:
  json.dump(did_json, file_out)
  file_out.close()
print('wrote DID document to file public-did.json')
