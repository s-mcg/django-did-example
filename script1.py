from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

print('begin!')

#generate private key, sign it, create public key from it
auth_message_bytes = bytes("this is my authenticated message to verify the keys are a pair", "utf-8")
private_key = Ed25519PrivateKey.generate()
signature = private_key.sign(auth_message_bytes)
public_key = private_key.public_key()

#get private bytes and public bytes
#check later: encryption?
private_bytes = private_key.private_bytes(
  encoding=serialization.Encoding.PEM, \
  format=serialization.PrivateFormat.PKCS8, \
  encryption_algorithm=serialization.NoEncryption() \
)
public_bytes = public_key.public_bytes(
  encoding=serialization.Encoding.OpenSSH, \
  format=serialization.PublicFormat.OpenSSH \
)

# decode to printable strings
private_key_str = private_bytes.decode('utf-8')
public_key_str = public_bytes.decode('utf-8')

print('Private key = ')
print(private_key_str)
print('Public key = ')
print(public_key_str)

# Raises InvalidSignature if verification fails
public_key.verify(signature, auth_message_bytes)

with open('public-key.key', 'wb') as file_out:
  file_out.write(public_bytes)
  file_out.close()

with open('private-key.key', 'wb') as file_out:
  file_out.write(private_bytes)
  file_out.close()

print('end!')
