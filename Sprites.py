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
    speed:int

    def __init__(self, level): #need to know what level to know where to draw boat bc columns diff
        super().__init__()
        self.speed=5 #default speed
        self.center_y=0
        if level == 1:
            self.center_x = (LEVEL1_WIDTH * 2) - OFFSET1
        else:
            self.center_x = (LEVEL23_WIDTH * 2) - OFFSET23
        self.angle = -90
        self.texture = arcade.load_texture("images/boat.PNG", scale=.1)
        #the random location to start drawing the next boat once this boat reaches it.
        self.new_boat = random.randrange(int(self.height)*2.5, WINDOW_HEIGHT + 1) #start when boat is completely through window. (avoids overlapping boats)

    def update(self):
        super().update()


class FrogSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/frog.PNG", scale=.05)
        # default location
        self.center_x = LEVEL1_WIDTH - OFFSET1
        self.center_y = LEVEL1_WIDTH * 3 - Y_OFFSET

    def update(self):
        super().update()
