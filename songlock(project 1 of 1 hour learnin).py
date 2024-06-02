import os
import base64
from requests import post, get
import json
from random import shuffle
# finables, (connect to spotify, end-trans, start-trans)
#ask if you want to run code 1 or code 2
done = 0

#find connect to spotify
def get_token():
   clientid = "e6a25b6d0d164a1dbd3095a6d6603c46"
   clientsecret = "7396ac72a5be4183a4bebb731094a923"
   
   auth_str = clientid + ":" + clientsecret
   auth_UTF = auth_str.encode("utf-8")
   auth_b64 = str(base64.b64encode(auth_UTF), "utf-8")

   url = "https://accounts.spotify.com/api/token"

   heder = {
      "Authorization": "Basic " + auth_b64,
      "Content-Type": "application/x-www-form-urlencoded"
   }

   data = {"grant_type": "client_credentials"}

   result = post(url, headers=heder, data=data)
   
   json_auth = json.loads(result.content)
   
   return json_auth["access_token"]

def auth_head(token):
   return {"Authorization": "Bearer " + token}

def search_song_items(tok, song):
   url = "https://api.spotify.com/v1/search"
   head = auth_head(tok)
   query = f"?q={song}&type=track&limit=5"
   queryurl = url + query
    
   search = get(queryurl, headers=head)

   
   json_result = json.loads(search.content)["tracks"]["items"]

   return  json_result
token = get_token()

def artist_list(song):
   artists= {}
   for x in range(0,5):
      artists[int(x) + 1] = str(search_song_items(token, song)[x]["artists"][0]["name"])
   
   return artists


q1 = "Hello I am the song encryptor \n I will encrypt your password based on your favorite song \n Encrypt or Decrypt password?"
print(q1)


while done == 0:
 choice = input()
 if choice.upper() == str("ENCRYPT"):
   #find start-trans
   print("what is your favorite song")
   favtemp = str(input())
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
   
   favsong = str(search_song_items(token, favtemp)[int(favartist)]["name"])
   favsongid = str(search_song_items(token,favtemp)[int(favartist)]["id"])
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
   enc_trans = tuple(enc_trans)

   print(enc_trans)
   #find end-trans

 elif choice.upper() == str("DECRYPT"):
    print("place the encrypted password: ")
    done = 1
 else:
     print('please type Encrypt or Decrypt ')
print("done :)")
    
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

