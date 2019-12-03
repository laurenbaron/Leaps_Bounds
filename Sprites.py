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
        self.texture = arcade.load_texture("images/log.PNG", scale=.1)

    def update(self):
        super().update()


class BoatSprite(arcade.Sprite):
    new_boat:int
    speed:int

    def __init__(self, width, offset, column):
        super().__init__()
        self.speed=5 #default speed
        self.center_y=0
        self.center_x = (width * 2) - offset
        if column==4:
            self.center_x = (width * 4) - offset
        self.angle = -90 #make boat face up
        self.texture = arcade.load_texture("images/boat.PNG", scale=.1)
        #the random location to start drawing the next boat once this boat reaches it.
        self.new_boat = random.randrange(WINDOW_HEIGHT/2, WINDOW_HEIGHT)

    def update(self):
        super().update()


class FrogSprite(arcade.Sprite):
    def __init__(self, width, offset):
        super().__init__()
        self.texture = arcade.load_texture("images/frog.PNG", scale=.05)
        # default location
        self.center_x = width-offset
        self.center_y = LEVEL_HEIGHT * 3 - Y_OFFSET #3 is from starting on the 3rd lilypad

    def update(self):
        super().update()
