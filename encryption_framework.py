import os
from dotenv import load_dotenv
import base64
from requests import post, get
import json
from random import shuffle
from spotipy import get_token, auth_head, search_song_items, artist_list
# finables, ( end-trans, start-trans)
#ask if you want to run code 1 or code 2
done = 0

with open("D:\solocoding\python studi\songlocked\cipher.json") as file:
   cipher_list = json.load(file)["list"]

load_dotenv("D:\solocoding\python studi\songlocked\.env")

token = get_token()

q1 = "Hello I am the song encryptor \n I will encrypt your password based on your favorite song \n Encrypt or Decrypt password?"
print(q1)


while True:
 choice = input()
 if choice.upper() == str("ENCRYPT"):
   #find start-trans
   print("what is your favorite song")
   favtemp = str(input())
   favitems = str(search_song_items(favtemp))
   break


while len(favitems) == 0:
   print("The system cannot find your song")
   favtemp = input("Please try again: ")
   favitems = str(search_song_items(favtemp))
   

print(f"which of these artists made your favorite song \n {artist_list(favtemp)} \n (if there is a duplicate, choose the lowest number)")
favartist = input("Place artist number: ")
print("If there was a typo in the title of the song, the encryption will be wrong \
      \n ---------------------------------------------------------------------------")
while True:
   try:
     favartist = int(favartist)
     if favartist < 6 and favartist > 0:
      break
     else:
      continue
   except:
      input("Place artist number under 5: ")

favsong = str(search_song_items(favtemp)[int(favartist)]["name"])
favsongid = str(search_song_items(favtemp)[int(favartist)]["id"])
password = input("Place the password you want to encrypt: ")
password = str(password)


favcipher = [*(str(favsongid[0:6]))]
shuffle(favcipher)  

trans:dict = {}

valo:int = 6
while int(len(password)) < valo:
   valo = valo + 6

valo = int(valo) / 6
valo = int(valo) + 1
valo = int(valo)
tru_valo = (valo * 6)
#note valo is the ammount of rows you need
   
for y in range(0, valo):
   for x in range(1,7):
      try:
        trans.update({(favsongid[x - 1],y + 1): password[(y*6)+ x - 1]})

      except:
         nxt_key = int((6 - (tru_valo  - int(len(trans)))) + 1)
         trans.update({(favsongid[x-1], y+1): " "})

enc_trans = []

for i in range(0,6):
   for l in range(0,2):
      enc_trans += trans[(str(favcipher[i]), l + 1)]
enc_trans = list(enc_trans)

print(enc_trans)
#find end-trans

num:int = len(favsong)

if (num % 2) == 0:
   odd:bool = True
else:
   odd:bool = False

if odd == True:
   for eminem in range(0, int(len(enc_trans))):
      fun = enc_trans[eminem]
      fun = cipher_list.index(fun)
      fun = fun + num
      if fun > 93:
         fun = fun - 94
      fun = cipher_list[fun]
      enc_trans[eminem] = str(fun)
else:
   for eminem in range(0, int(len(enc_trans))):
      fun = enc_trans[eminem]
      fun = cipher_list.index(fun)
      fun = fun - num
      if fun < 0:
         fun = fun +94
      fun = cipher_list[fun]
      enc_trans[eminem] = str(fun)

print(f"encrypted cipher {enc_trans}")
final:tuple = ""
for chr in range(len(enc_trans)):
   final = final + str(enc_trans[chr])
print(f"Your encrypted password is:  {final}\
      \n ------------------------------------- \
      \n Remember to save it somewhere to keep it safe")
done = 1
 
   #step 1 of c1: we need to encrypt the password based on the favorite song of the user
       
        #step 2 of c1: The cipher should come from the song, lets use the spotify api to get the song info
        #for now lets make the cipher a the spotify song ID (findable in the URL of a song)
        #we may change it to meta data in the future



  #step 3: trans cipher
  #all characters of the password should change based on the transcription cipher on the spotify id
       # https://docs.google.com/document/d/1o8BB3RoNAYYu9Ys0Kiz2zlCb4dEZtZbFIBIOuB2WG_I/edit
  #this only scrambles it, now we ceaser cipher it

 

 # step 4: ceaser cipher :)
    # so we will make the first letter of the song title and shift the cipher that many spaces
    # if the title is an odd number of characters, it moves left
    # if even, right

 #step 5: that should give us the encrypted passcode and should finish up the first step of the cod

