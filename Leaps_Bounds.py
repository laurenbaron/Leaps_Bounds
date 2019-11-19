import arcade
import os

# Define constants
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
BACKGROUND_COLOR = arcade.color.AQUA
GAME_TITLE = "Froggy Road"
GAME_SPEED = 1 / 60


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
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/boat.jpg", scale=.25)

    def update(self):
        super().update()


class FrogSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/frog.jpg", scale=.25)

    def update(self):
        super().update()


class Intro(arcade.Window):
    title: arcade.Sprite
    frog: arcade.Sprite
    beginner: arcade.Sprite
    intermediate: arcade.Sprite
    difficult: arcade.Sprite

    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.title = arcade.Sprite("images/froggy.png", 1.5)
        self.frog = arcade.Sprite("images/frog.jpg", .25)
        self.beginner = arcade.Sprite("images/beginner.png", .5)
        self.intermediate = arcade.Sprite("images/intermediate.png", .5)
        self.difficult = arcade.Sprite("images/difficult.png", .5)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.title.center_x = WINDOW_WIDTH / 2
        self.title.center_y = 3 * WINDOW_HEIGHT / 4
        self.title.draw()

        self.frog.center_x = WINDOW_WIDTH / 2
        self.frog.center_y = WINDOW_HEIGHT / 2
        self.frog.draw()

        self.beginner.center_x = WINDOW_WIDTH / 5
        self.beginner.center_y = WINDOW_HEIGHT / 4
        self.beginner.draw()

        self.intermediate.center_x = 2.5 * WINDOW_WIDTH / 5
        self.intermediate.center_y = WINDOW_HEIGHT / 4
        self.intermediate.draw()

        self.difficult.center_x = 4 * WINDOW_WIDTH / 5
        self.difficult.center_y = WINDOW_HEIGHT / 4
        self.difficult.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self.difficult.collides_with_point([x, y]):
            speed = 10
        elif self.intermediate.collides_with_point([x, y]):
            speed = 5
        else:
            speed = 1
        MyGame().setup(speed)


class MyGame(arcade.Window):
    speed: int
    frog: FrogSprite
    lily_list: arcade.SpriteList[LilySprite]
    boat_list: arcade.SpriteList[BoatSprite]
    level1_width = WINDOW_WIDTH / 3
    level23_width = WINDOW_WIDTH / 7
    offset1 = level1_width / 2
    offset23 = level23_width / 2
    level_height = WINDOW_HEIGHT / 6
    y_offset = level_height / 2
    LILLIES = 6
    ROWS = 3

    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.background = None
        self.lily_list = []
        self.boat_list = []

    def setup(self, user_speed):
        """ Setup the game (or reset the game) """
        self.speed = user_speed
        arcade.set_background_color(BACKGROUND_COLOR)
        self.background = arcade.load_texture("images/water.jpg")
        self.frog = FrogSprite()
        self.lily_list = arcade.SpriteList()
        self.boat_list = arcade.SpriteList()

        # make lily pad/boat grid
        row = 1
        while row <= self.ROWS:
            # boat in the middle
            if row == 2:
                boat = BoatSprite()
                boat.center_y = 0
                boat.center_x = (self.level1_width * row) - self.offset1
                boat.angle=90
                self.boat_list.append(boat)
            else:
                index = 1
                while index <= self.LILLIES:
                    lily = LilySprite()
                    lily.center_y = (self.level_height * index) - self.y_offset
                    lily.center_x = (self.level1_width * row) - self.offset1
                    self.lily_list.append(lily)
                    index += 1
            row += 1

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.lily_list.draw()
        self.boat_list.draw()
        for boat in self.boat_list:
            boat.forward(1.0)
        self.frog.center_x = self.level1_width - self.offset1
        self.frog.center_y = self.level_height * 3 - self.y_offset
        self.frog.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        for boat in self.boat_list:
            boat.change_y=5
            self.boat_list.update()

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            self.frog.thrust = 0
        elif symbol == arcade.key.RIGHT:
            self.frog.thrust = 0
        elif symbol == arcade.key.UP:
            self.frog.thrust = 0
        elif symbol == arcade.key.DOWN:
            self.frog.thrust = 0


def main():
    window = Intro()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
