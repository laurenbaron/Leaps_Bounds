from Constants import *


class LilySprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/lily.png", scale=.25)

    def update(self):
        super().update()


class LogSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/log.jpg", scale=.25)

    def update(self):
        super().update()


class BoatSprite(arcade.Sprite):
    new_boat:int

    def __init__(self):
        super().__init__()
        self.center_x=(level1_width * 2) - offset1 #the 2 is hardcoded. need to make it alter bc of the change in rows
        self.center_y=0
        self.angle = -90
        self.texture = arcade.load_texture("images/boat.PNG", scale=.1)
        #the random location to start drawing the next boat once this boat reaches it.
        self.new_boat = random.randrange(int(self.height)*2.5, WINDOW_HEIGHT + 1) #start when boat is completely through window. (avoids overlapping boats)
        print(self.new_boat)

    def update(self):
        super().update()


class FrogSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/frog.PNG", scale=.05)
        # default location
        self.center_x = level1_width - offset1
        self.center_y = level_height * 3 - y_offset

    def update(self):
        super().update()
