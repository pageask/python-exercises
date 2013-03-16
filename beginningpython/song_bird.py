from bird import Bird

class SongBird(Bird):

    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print self.sound


if __name__ == "__main__":
    song_bird = SongBird()
    song_bird.eat()
    song_bird.eat()
    song_bird.sing()
