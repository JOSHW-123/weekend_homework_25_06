class Song:
    
    def __init__(self, song, playlist):
        # self.artist = artist
        self.song = song
        self.playlist = []
        

    def song_count(self):
        return len(self.playlist)

# Need to use loop to check if song in playlist
    def find_song_by_name(self, song):
        if song in self.playlist:
            return song
        else:
            return "Song not found"

    def add_song(self, song):
        self.playlist.append(song)
       