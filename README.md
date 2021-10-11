# django-did-example
This project is a simple DID document web host with Django.

# installation-instructions
Note: these scripts should be run with python3. If your system has `python` mapped to `python27` and `python3` to python 3, then replace the `python` commands with `python3`. you may want to do this in pipenv to avoid global installs.

Step 0. clone repository and install dependencies

```pip install cryptography
pip install python-jose[cryptography]
pip install django
pip install requests```


Step 1. run the first script. it should create 3 files.

```python script1```

Step 2. in a separate terminal, run the django server.

```cd webserver;python manage.py runserver```

You may want to verify the server is running with a command, or paste the url in your web browser.

```curl http://127.0.0.1:8000/didservice/.well-known/did.json```

Step 3. back in the original terminal and directory, run script2 to create a signed JWT token.

```python script2```

Step 4. use the token from step 3/script2 to view the payload from step 2. The script will retrieve the public key from the webserver, so the server must be running.

```python script3 <token>```