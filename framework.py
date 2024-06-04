from spotipy import search_song_items, artist_list



def questions(mode):

    q1 = "Hello I am the song encryptor \n I will encrypt your password based on your favorite song \n Encrypt or Decrypt password?"
    print(q1)
   
    while True:
        choice = input()
        if choice.upper() == str(mode):
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
    
    return favsong, favsongid

