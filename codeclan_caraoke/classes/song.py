class Song:
    
    def __init__(self, title, artist):
       self.title = title
       self.artist = artist
       
    def equals(self, song):
            return song.title == self.title and song.artist == self.artist 
    # def song_count(self):
    #     return len(self.fav_song_list)

# # Need to use loop to check if song in playlist
#     def check_if_song_in_library(self, song):
#         if song in self.fav_song_list == True :
#             return "We have this song"
        # else:
        #     return "Song not found"

  
    # def add_song(self, name, artist):
    #     self..append(name, artist)  