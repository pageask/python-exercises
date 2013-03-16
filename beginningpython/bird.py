class Bird(object):

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry = False
        else:
            print 'No, thanks!'


if __name__ == "__main__":
    bird = Bird()
    bird.eat()
    bird.eat()
