from Sprites import *

#to do list: background of start, multiple screens, make pictures pretty, win/lose, logs, frog off screen, rearrange scope of variables bc keep importing game

class GameView(arcade.View):
    speed: int
    frog: arcade.Sprite
    lily_list: arcade.SpriteList[LilySprite]
    boat_list: arcade.SpriteList[BoatSprite]
    logs: int
    logs_location: int
    log_list: arcade.SpriteList[LogSprite]

    def __init__(self):
        super().__init__()
        self.speed=0
        self.frog=None
        self.lily_list=None
        self.boat_list=None
        self.logs=0
        self.log_location=0
        self.log_list=None

    def on_show(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.background = arcade.load_texture("images/pond2.jpg")
        self.frog = FrogSprite()
        self.lily_list = arcade.SpriteList()
        self.boat_list = arcade.SpriteList()

        #how many logs. 1-5 because need to have at least one lilypad
        self.logs=random.randrange(1,6)

        # make lily pad/log/boat grid
        column = 1
        while column <= COLUMNS:
            # boat in the middle
            if column == 2:
                boat = BoatSprite()
                self.boat_list.append(boat)
            else:
                index = 1
                while index <= ROWS:
                    '''
                    print(self.logs)
                    current_log=1
                    while current_log<=self.logs:
                        self.log_location = random.randrange(1, 7) #randomly place it in one of the 6 rows
                        log = LogSprite()
                        log.center_y = (level_height * index) - y_offset
                        log.center_x = (level1_width * self.log_location) - offset1
                        print(log)
                        print(self.log_list)
                        self.log_list.append(log)
                        print(len(self.log_list))
                        current_log+=1
                
                    if not index.collides_with_list(self.frog_list):
                    '''
                    lily = LilySprite()
                    lily.center_y = (level_height * index) - y_offset
                    lily.center_x = (level1_width * column) - offset1
                    self.lily_list.append(lily)
                    index += 1
            column += 1


    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.lily_list.draw()
        self.boat_list.draw()
        #self.log_list.draw()
        for boat in self.boat_list:
            #random time to send the next boat based on other boat's location
            if boat.center_y in range(boat.new_boat,boat.new_boat+5): #changing y by 5 so counts by 5s. can miss the new_boat since new_boat doesnt count by 5s
                self.boat_list.append(BoatSprite())
        self.frog.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        for boat in self.boat_list:
            boat.change_y=5
            self.boat_list.update()
            boat.change_y=0 #reset speed of boat for the next one
        self.frog.update()

        if self.frog.collides_with_list(self.boat_list):
            lose=LoseView()
            self.window.show_view(lose)

        if self.frog.collides_with_point([WINDOW_WIDTH+offset1,self.frog.center_y]):
            win=WinView()
            self.window.show_view(win)

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            self.frog.center_x = self.frog.center_x - level1_width
            self.frog.angle= 0
        elif symbol == arcade.key.RIGHT:
            self.frog.center_x = self.frog.center_x + level1_width
            #how to reflect an image!!!!
        elif symbol == arcade.key.UP:
            self.frog.center_y = self.frog.center_y + level_height
            self.frog.angle = -90
        elif symbol == arcade.key.DOWN:
            self.frog.center_y = self.frog.center_y - level_height
            self.frog.angle = 90


class IntroView(arcade.View):
    title: arcade.Sprite
    frog: arcade.Sprite
    beginner: arcade.Sprite
    intermediate: arcade.Sprite
    difficult: arcade.Sprite

    def __init__(self):
        super().__init__()
        self.title=None
        self.frog=None
        self.beginner=None
        self.intermediate=None
        self.difficult=None

    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        #self.background = intro_image
        self.title = arcade.Sprite("images/froggyroad.PNG", .5)
        self.frog = arcade.Sprite("images/frog.PNG", .1)
        self.beginner = arcade.Sprite("images/beginner.png", .5)
        self.intermediate = arcade.Sprite("images/intermediate.png", .5)
        self.difficult = arcade.Sprite("images/difficult.png", .5)

    def on_draw(self):
        arcade.start_render()
        #print(self.background.width)
        #arcade.draw_texture_rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
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
            start_game = GameView()
            self.window.show_view(start_game)
        elif self.intermediate.collides_with_point([x, y]):
            speed = 5
            start_game = GameView()
            self.window.show_view(start_game)
        else:
            speed = 1 #default if don't press in buttons. need to do speed stuff later
            start_game = GameView()
            self.window.show_view(start_game)


class LoseView(arcade.View):
    restart: arcade.Sprite

    def __init__(self):
        super().__init__()
        self.restart=None

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
            restart_game=IntroView()
            self.window.show_view(restart_game)


class WinView(arcade.View):
    restart: arcade.Sprite

    def __init__(self):
        super().__init__()
        self.restart=None

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
            restart_game=IntroView()
            self.window.show_view(restart_game)


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    intro = IntroView()
    window.show_view(intro)
    arcade.run()


if __name__ == "__main__":
    main()
