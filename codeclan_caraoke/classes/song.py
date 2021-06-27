class Song:
    
    def __init__(self, name, artist):
        # self.artist = artist
        self.name = name
        self.artist = artist
       
        

    def song_count(self):
        return len(self.song.library)

# # Need to use loop to check if song in playlist
    def check_if_song_in_library(self, song):
        if song in self.room.playlist == True :
            return "We have this song"
        else:
            return "Song not found"

  
    def add_song(self, name, artist):
        self.library.append(name, artist)  