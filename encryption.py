from dotenv import load_dotenv
import json
from random import shuffle
import framework
# finables, ( end-trans, start-trans)
#ask if you want to run code 1 or code 2
done = 0

with open("D:\solocoding\python studi\songlocked\cipher.json") as file:
   cipher_list = json.load(file)["list"]

load_dotenv("D:\solocoding\python studi\songlocked\.env")


questions = framework.questions("ENCRYPT")

framework.questions("ENCRYPT")

favsong = questions[0]
favsongid = questions[1]
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

