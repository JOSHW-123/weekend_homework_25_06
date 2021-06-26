class Song:
    
    def __init__(self, name, playlist):
        # self.artist = artist
        self.name = name
        self.playlist = {}

# Need to use loop to check if song in playlist
    def find_song_by_name(self):
        for song in self.playlist:
            return song
        else:
            return "Song not found"
       