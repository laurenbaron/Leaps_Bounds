from Constants import *


class LilySprite(arcade.Sprite):
    """ Lily Sprite the frog jumps on. drawn by putting in a sprite list w a while loop """

    def __init__(self):
        """Initialize variables"""
        super().__init__()
        self.texture = arcade.load_texture("images/lily.png", scale=.25)

    def update(self):
        """Called whenever sprite updates"""
        super().update()


class LogSprite(arcade.Sprite):
    """ Log Sprite the frog cannot jump on. drawn by putting in a sprite list w a while loop """

    def __init__(self):
        """Initialize variables"""
        super().__init__()
        self.texture = arcade.load_texture("images/log.PNG", scale=.1)

    def update(self):
        """Called whenever sprite updates"""
        super().update()


class BoatSprite(arcade.Sprite):
    """ Boat Sprite the frog cannot hit. drawn by putting in a sprite list w a while loop """
    new_boat: int
    speed: int
    already_added: bool #make sure don't keep adding a new boat once it passes the generated point (only add once)

    def __init__(self, width: int, offset: int, column: int):
        """
        Initialize variables. parameters in constructor because we get what level they are on from the GameView,
        which determines how many columns there are and how big those columns are, which determines where to
        draw the boat
        :param width: the width of the columns to base where to draw boat
        :param offset: ensure drawing boat in center of the column. based off the width, which is based on the level
        :param column: for the harder levels, need to know if drawing boat in the 1st boat column (2)
        or the 2nd boat column (4)
        """
        super().__init__()
        self.speed = 5  # default speed
        self.center_y = 0
        self.center_x = (width * 2) - offset
        if column == 4:
            self.center_x = (width * 4) - offset
        self.angle = -90  # make boat face up
        self.texture = arcade.load_texture("images/boat.PNG", scale=.1)
        '''
        the random location to start drawing the next boat once this boat reaches it.
        used that range to allow enough room for frog to move in between boats 
        '''
        self.new_boat = random.randrange(WINDOW_HEIGHT / 2, WINDOW_HEIGHT)
        self.already_added=False

    def update(self):
        """Called whenever sprite updates"""
        super().update()


class FrogSprite(arcade.Sprite):
    """ Frog Sprite the user controls and is trying to get to cross the pond without touching boats/logs """

    def __init__(self, width: int, offset: int):
        """
        Initialize variables. parameters in constructor because we get what level they are on from the GameView,
        which determines how many columns there are and how big those columns are, which determines where to
        draw the frog (make sure its directly on the lilies)
        :param width: the width of the columns to base where to draw frog
        :param offset: ensure drawing frog in center of the column. based off the width, which is based on the level
        so that the frog and lilies align
        """
        super().__init__()
        self.texture = arcade.load_texture("images/frog.PNG", scale=.05)
        # default location
        self.center_x = width - offset
        self.center_y = LEVEL_HEIGHT * 3 - Y_OFFSET  # 3 is from starting on the 3rd lilypad

    def update(self):
        """Called whenever sprite updates"""
        super().update()
