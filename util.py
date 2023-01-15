import hashlib
import re

class validator:
    def email_format(email_text):
        return bool(re.match(r'^(\w{3,})+(\.\w+)*@(\w+\.)+(com|net|org|edu|gov)(\.\w{2})*$', email_text))

    def name_format(name):
        return bool(re.match(r'[a-zA-Z -]{3,}', name))

class crytography:
    def hash_salt(raw_pass, salt, looping_len):
        encryptor = hashlib.sha256()
        encryptor.update(str(raw_pass).encode('utf-8') + str(salt).encode('utf-8'))
        encrypted_pass = encryptor.hexdigest()
        for _ in range(looping_len + int(re.findall('\d{2}', encrypted_pass)[0])):
            encryptor.update(str(raw_pass).encode('utf-8') + str(salt).encode('utf-8'))
            encrypted_pass = encryptor.hexdigest()

        return encrypted_pass