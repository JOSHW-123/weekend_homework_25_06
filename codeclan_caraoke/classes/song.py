class Song:
    
    def __init__(self, name, artist, library):
        # self.artist = artist
        self.name = name
        self.artist = artist
        self.library = []
        

    def song_count(self):
        return len(self.library)

# # Need to use loop to check if song in playlist
#     def find_song_by_name(self, name, library):
#         if name in self.library:
#             return name
#         else:
#             return "Song not found"

  
    def add_song(self, name, artist):
        self.library.append(name, artist)  