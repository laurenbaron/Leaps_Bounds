from Sprites import *

#my to do list: add boats randomly spaced, multiple screens, make pictures pretty, win/lose, logs, frog off screen, rearrange scope of variables bc keep importing game

class GameView(arcade.View):
    speed: int
    frog: arcade.Sprite
    lily_list: arcade.SpriteList[LilySprite]
    boat_list: arcade.SpriteList[BoatSprite]

    #on website link sent in slack, they didn't use inits with views. do we still need them?
    def on_show(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.background = arcade.load_texture("images/water.jpg")
        self.frog = FrogSprite()
        self.lily_list = arcade.SpriteList()
        self.boat_list = arcade.SpriteList()

        # make lily pad/boat grid
        row = 1
        while row <= ROWS:
            # boat in the middle
            if row == 2:
                boat = BoatSprite()
                self.boat_list.append(boat)
            else:
                index = 1
                while index <= LILLIES:
                    lily = LilySprite()
                    lily.center_y = (level_height * index) - y_offset
                    lily.center_x = (level1_width * row) - offset1
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
            if boat.center_y == WINDOW_HEIGHT/2:
                self.boat_list.append(BoatSprite())
        self.frog.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        for boat in self.boat_list:
            boat.change_y=5
            self.boat_list.update()
            boat.change_y=0 #reset speed of boat for the next one
        self.frog.update()

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            self.frog.center_x = self.frog.center_x - level1_width
        elif symbol == arcade.key.RIGHT:
            self.frog.center_x = self.frog.center_x + level1_width
        elif symbol == arcade.key.UP:
            self.frog.center_y = self.frog.center_y + level_height
        elif symbol == arcade.key.DOWN:
            self.frog.center_y = self.frog.center_y - level_height

        if self.frog.collides_with_list(self.boat_list):
            lose=LoseView()
            self.window.show_view(lose)


class IntroView(arcade.View):
    title: arcade.Sprite
    frog: arcade.Sprite
    beginner: arcade.Sprite
    intermediate: arcade.Sprite
    difficult: arcade.Sprite

    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.title = arcade.Sprite("images/froggy.png", 1.5)
        self.frog = arcade.Sprite("images/frog.jpg", .25)
        self.beginner = arcade.Sprite("images/beginner.png", .5)
        self.intermediate = arcade.Sprite("images/intermediate.png", .5)
        self.difficult = arcade.Sprite("images/difficult.png", .5)

    def on_draw(self):
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

    def on_mouse_press(self, x, y, button, modifiers):
        if self.difficult.collides_with_point([x, y]):
            speed = 10
        elif self.intermediate.collides_with_point([x, y]):
            speed = 5
        else:
            speed = 1 #default if don't press in buttons. need to do speed stuff later
        start_game=GameView()
        self.window.show_view(start_game)


class LoseView(arcade.View):
    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("YOU LOSE", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")


class WinView(arcade.View):
    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("YOU WIN", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    intro = IntroView()
    window.show_view(intro)
    arcade.run()


if __name__ == "__main__":
    main()
