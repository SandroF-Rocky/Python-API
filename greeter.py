#!C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe
import os
import urllib.parse

import sys


def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')


def greeter(name, surname):
    return ("Olá " + str(name.capitalize() + ' ' + str(surname)).capitalize() + ' Como vai?')


query_dict = urllib.parse.parse_qs(os.environ['QUERY_STRING'])


input_name = str(query_dict['name'])[2:-2]
input_surname = str(query_dict['surname'])[2:-2]

enc_print("Content-Type: text/html; charset=utf-8\n")
enc_print(greeter(input_name, input_surname)) 


























