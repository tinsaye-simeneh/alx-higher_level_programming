#!/usr/bin/python3
'''script that fetches https://intranet.hbtn.io/status '''
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        r = response.read()
        print('Body response:')
        print('\t- type:', type(r))
        print('\t- content:', r)
        print('\t- utf8 content:', r.decode('utf-8'))
