class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


ride_twentyonepilot = Song(["I just wanna stay in the sun where I find",
                   "I know it\'s hard sometimes",
                   "Pieces of peace in the sun\'s peace of mind",
                   "I know it\'s hard sometimes"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

ride_twentyonepilot.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
