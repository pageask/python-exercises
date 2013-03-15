class Color:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def brightness_index(self):
        return (299 * self.red + 587 * self.green + 144 * self.blue) / 1000

    def brightness_difference(self, another_color):
        return abs(
            self.brightness_index() - another_color.brightness_index())

    def hue_difference(self, another_color):
        return (abs(self.red - another_color.red) +
                abs(self.green - another_color.green) +
                abs(self.blue - another_color.blue))

    def enough_contrast(self, another_color):
        return (self.brightness_difference(another_color) > 125 and
                self.hue_difference(another_color) > 500)
