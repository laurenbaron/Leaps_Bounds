from Sprites import *


# to do list: background of start, logs, fix boats, reflect frog, documentation

class GameView(arcade.View):
    speed: int
    frog: arcade.Sprite
    lily_list: arcade.SpriteList[LilySprite]
    # need 2 lists for 2nd screen because want the 2 boat columns in level 2 to be differently spaced
    boat_list_2: arcade.SpriteList[BoatSprite]
    boat_list_4: arcade.SpriteList[BoatSprite]
    logs: int
    logs_location: int
    log_list: arcade.SpriteList[LogSprite]
    level: int
    columns: int
    column_width: int
    offset: int

    def __init__(self, level_speed, my_level):
        super().__init__()
        self.speed = level_speed
        self.level = my_level
        self.frog = None
        self.lily_list = None
        self.boat_list_2 = None
        self.boat_list_4 = None
        self.logs = 0
        self.log_location = 0
        self.log_list = None
        self.columns = 0
        self.column_width = 0
        self.offset = 0

    def on_show(self):
        """ Setup the game (or reset the game) """
        self.set_columns()

        arcade.set_background_color(BACKGROUND_COLOR)
        self.background = arcade.load_texture("images/pond2.jpg")
        self.frog = FrogSprite(self.column_width, self.offset)
        self.lily_list = arcade.SpriteList()
        self.boat_list_2 = arcade.SpriteList()
        self.boat_list_4 = arcade.SpriteList()
        self.log_list = arcade.SpriteList()

        # how many logs. possible numbers 1-4 because want to have at least 2 lily pads
        self.logs = random.randrange(1, 5)

        # make lily pad/log/boat grid
        column = 1
        while column <= self.columns:
            if column % 2 == 0:  # only draw boat on even columns
                boat = BoatSprite(self.column_width, self.offset, column)
                self.boat_list_2.append(boat)
                self.boat_list_4.append(boat)
            else:
                row = 1
                current_log = 1
                while row <= ROWS:
                    all_rows = [1, 2, 3, 4, 5, 6]  # need a new set of columns for each row
                    while current_log <= self.logs:
                        self.log_location = random.choice(all_rows)  # randomly place it in one of the 6 rows
                        all_rows.remove(self.log_location)
                        log = LogSprite()
                        log.center_y = (LEVEL_HEIGHT * self.log_location) - Y_OFFSET  # put it at the chosen row
                        log.center_x = (self.column_width * column) - self.offset
                        self.log_list.append(log)
                        current_log += 1
                    for empty in all_rows:  # if no log has taken the row, put a lily in it
                        lily = LilySprite()
                        lily.center_y = (LEVEL_HEIGHT * empty) - Y_OFFSET
                        lily.center_x = (self.column_width * column) - self.offset
                        self.lily_list.append(lily)
                    row += 1
            column += 1

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)

        self.lily_list.draw()
        self.boat_list_2.draw()
        self.log_list.draw()
        if self.level != 1:
            self.boat_list_4.draw()  # only draw the 2nd boat row if on the advanced levels

        for boat in self.boat_list_2:
            '''
            random time to send the next boat based on other boat's location
            why in range: hanging y by speed so counts by speed. can miss the new_boat since new_boat doesnt 
            count by 2s,5s,10s
            '''
            if boat.center_y in range(boat.new_boat, boat.new_boat + self.speed):
                self.boat_list_2.append(BoatSprite(self.column_width, self.offset, 2))
        for boat in self.boat_list_4:
            if boat.center_y in range(boat.new_boat, boat.new_boat + self.speed):
                self.boat_list_4.append(BoatSprite(self.column_width, self.offset, 4))
        self.frog.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        for boat in self.boat_list_2:
            boat.change_y = self.speed
            self.boat_list_2.update()
            boat.change_y = 0  # reset speed of boat for the next one
        for boat in self.boat_list_4:
            boat.change_y = self.speed
            self.boat_list_4.update()
            boat.change_y = 0
        self.frog.update()

        if self.frog.collides_with_list(self.boat_list_2) or self.frog.collides_with_list(self.boat_list_4):
            lose = LoseView()
            self.window.show_view(lose)

        if self.frog.collides_with_point([WINDOW_WIDTH + self.offset, self.frog.center_y]):
            if self.level == 1:  # don't go to win screen yet go to next level
                self.level += 1
                next_level = GameView(self.speed, self.level)
                self.window.show_view(next_level)
            else:
                win = WinView()
                self.window.show_view(win)

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            self.frog.angle = 0
            if (self.frog.center_x - self.column_width) < 0:  # make sure frog isn't moving off the screen or on a log
                pass
            else:
                self.frog.center_x = self.frog.center_x - self.column_width
        elif symbol == arcade.key.RIGHT:
            # how to reflect an image!!!!
            self.frog.center_x = self.frog.center_x + self.column_width
        elif symbol == arcade.key.UP:
            self.frog.angle = -90
            if (self.frog.center_y + LEVEL_HEIGHT) > WINDOW_HEIGHT:
                pass
            else:
                self.frog.center_y = self.frog.center_y + LEVEL_HEIGHT
        elif symbol == arcade.key.DOWN:
            self.frog.angle = 90
            if (self.frog.center_y - LEVEL_HEIGHT) < 0:
                pass
            else:
                self.frog.center_y = self.frog.center_y - LEVEL_HEIGHT

    def set_columns(self):
        if self.level == 1:
            self.columns = COLUMNS_1
            self.column_width = LEVEL1_WIDTH
            self.offset = OFFSET1
        else:
            self.columns = COLUMNS_23
            self.column_width = LEVEL23_WIDTH
            self.offset = OFFSET23


class IntroView(arcade.View):
    title: arcade.Sprite
    frog: arcade.Sprite
    beginner: arcade.Sprite
    intermediate: arcade.Sprite
    difficult: arcade.Sprite

    def __init__(self):
        super().__init__()
        self.title = None
        self.frog = None
        self.beginner = None
        self.intermediate = None
        self.difficult = None

    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        # self.background = intro_image
        self.title = arcade.Sprite("images/froggyroad.PNG", .5)
        self.frog = arcade.Sprite("images/frog.PNG", .1)
        self.beginner = arcade.Sprite("images/beginner.png", .5)
        self.intermediate = arcade.Sprite("images/intermediate.png", .5)
        self.difficult = arcade.Sprite("images/difficult.png", .5)

    def on_draw(self):
        arcade.start_render()
        # print(self.background.width)
        # arcade.draw_texture_rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
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
            start_game = GameView(6, 1)  # pass in the speed for the level and what level (if press intro buttons go to first level)
            self.window.show_view(start_game)
        elif self.intermediate.collides_with_point([x, y]):
            start_game = GameView(4, 1)
            self.window.show_view(start_game)
        elif self.beginner.collides_with_point([x, y]):
            start_game = GameView(2, 1)
            self.window.show_view(start_game)


class LoseView(arcade.View):
    restart: arcade.Sprite

    def __init__(self):
        super().__init__()
        self.restart = None

    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.background = arcade.load_texture("images/You_lose.png")
        self.restart = arcade.Sprite("images/restart.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.restart.center_x = WINDOW_WIDTH / 2
        self.restart.center_y = WINDOW_HEIGHT / 4
        self.restart.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.restart.collides_with_point([x, y]):
            restart_game = IntroView()
            self.window.show_view(restart_game)


class WinView(arcade.View):
    restart: arcade.Sprite

    def __init__(self):
        super().__init__()
        self.restart = None

    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.background = arcade.load_texture("images/You_win.png")
        self.restart = arcade.Sprite("images/restart.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.restart.center_x = WINDOW_WIDTH / 2
        self.restart.center_y = WINDOW_HEIGHT / 4
        self.restart.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.restart.collides_with_point([x, y]):
            restart_game = IntroView()
            self.window.show_view(restart_game)


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    intro = IntroView()
    window.show_view(intro)
    arcade.run()


if __name__ == "__main__":
    main()
