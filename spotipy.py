import json
import os
import base64
from requests import post, get
from dotenv import load_dotenv

load_dotenv("D:\solocoding\python studi\songlocked\.env")

clientid = os.environ.get("clientid")
clientsecret = os.environ.get("clientsecret")

def get_token():
   
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
token = get_token()

def auth_head():
   return {"Authorization": "Bearer " + token}

def search_song_items(song):
   url = "https://api.spotify.com/v1/search"
   head = auth_head()
   query = f"?q={song}&type=track&limit=5"
   queryurl = url + query
    
   search = get(queryurl, headers=head)

   
   json_result = json.loads(search.content)["tracks"]["items"]

   return  json_result

def artist_list(song):

   artists= {}
   for x in range(0,5):
      artists[int(x) + 1] = str(search_song_items(song)[x]["artists"][0]["name"])
   
   return artists
