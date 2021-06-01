#!/usr/bin/python3
'''I/O Python'''


def read_file(filename=""):
    '''reads a text file (UTF8) and prints it to stdout'''
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end='')
