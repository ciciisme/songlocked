from dotenv import load_dotenv
import json
from base import questions

with open("D:\solocoding\python studi\songlocked\cipher.json") as file:
   cipher_list = json.load(file)["list"]

load_dotenv("D:\solocoding\python studi\songlocked\.env")

question = questions("DECRYPT")

favsong = question[0]
favsongid = question[1]
password = input("Place the password you want to decrypt: ")
password = list(str(password))


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
      print(fun)
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

unciphered_password = str(password)
unciphered_password = unciphered_password.replace("'", "").replace(",", "").replace(" ", "").replace("]", "").replace("[", "")

print(unciphered_password)
