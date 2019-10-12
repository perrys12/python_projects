#!/bin/python3
import random
chars = 'abcdefghijklmnopoqrstuvwxyz1234567890'

lenght = input('password lenght?')
length = int(lenght)


for p in range(3):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
