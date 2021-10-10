from jose import jwt

print('script 2 payload')
payload = {
"text": "It was the open sea, whose waves were still dashing with tremendous violence! It was the ocean, without any visible limits, even for those whose gaze, from their commanding position, extended over a radius of forty miles. The vast liquid plain, lashed without mercy by the storm, appeared as if covered with herds of furious chargers, whose white and disheveled crests were streaming in the wind. No land was in sight, not a solitary ship could be seen."
}

print(payload)

secret = 'changeme'
with open("./private-key.key", 'r', encoding = 'utf-8') as f:
    secret = f.read()
    f.close()
print('secret:')
print(secret)

token = jwt.encode(payload, secret, algorithm='HS256')
print('token:')
print(token)
