"""
This is the startup file, it will create your admin account credentials.
Currently, only one admin is supported.
"""
import bcrypt, hmac, ast, os
from blogengine import pageLocation


if __name__ == '__main__':
    with open('config.txt', 'w') as f:
        out = {'adminHash':'', 'adminName':''}
        password = input("Password for admin: ")
        name = input("Username for admin: ")
        hashed = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
        out['adminHash'] = hashed
        out['adminName'] = name
        f.write(str(out))

def checkPassword(password):

    credentials = {}
    path = os.path.join(os.path.join(pageLocation, '..'), 'config.txt')
    with open(path, 'r') as f:
        credentials = ast.literal_eval(f.read())
    hashed = credentials['adminHash']
    convertedPass = bytes(password, 'utf-8')
    if hmac.compare_digest(bcrypt.hashpw(convertedPass, hashed), hashed):
        return True
    else:
        return False




#print(checkPassword(input('check: ')))