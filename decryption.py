from dotenv import load_dotenv
import json
from base import questions

with open("D:\solocoding\python studi\songlocked\cipher.json") as file:
   cipher_list = json.load(file)["list"]

load_dotenv("D:\solocoding\python studi\songlocked\.env")

question = questions("DECRYPT")

favsong = question[0]
favsongid = question[1]
encrypted_password = input("Place the password you want to decrypt: ")
splitter = len(encrypted_password) - 7

password_list = encrypted_password.split(encrypted_password[splitter])
password = password_list[0]
password = list(str(password))
key = password_list[1]
key_correct = list(favsongid[0:6])
print(key_correct)


num:int = len(favsong)

if (num % 2) == 0:
   odd:bool = True
else:
   odd:bool = False

if odd == False:
   for eminem in range(0, int(len(password))):
      fun = password[eminem]
      fun = cipher_list.index(fun)
      fun = fun + num
      if fun > 93:
         fun = fun - 94
      fun = cipher_list[fun]
      password[eminem] = str(fun)
else:
   for eminem in range(0, int(len(password))):
      fun = password[eminem]
      fun = cipher_list.index(fun)
      fun = fun - num
      if fun < 0:
         fun = fun +94
      fun = cipher_list[fun]
      password[eminem] = str(fun)

unciphered_password = password
print(unciphered_password)

rows = len(password) / 6

trans_cipher_chart:dict = {}
rows = int(rows)

for x in range(0,6):
    for y in range(0, rows):
       trans_cipher_chart.update({(key[x], y + 1): str(unciphered_password[(x*2) +y])}) 

print(trans_cipher_chart)

trans_cipher = []
for row in range(rows):
   for items in range(6):
           trans_cipher += str(trans_cipher_chart[(key_correct[items], row + 1)])
      
final = ("")
for character in range(len(trans_cipher)):
     final += str(trans_cipher[character])

print(final)