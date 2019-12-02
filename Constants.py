import arcade
import os
import random

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Define constants
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
BACKGROUND_COLOR = arcade.color.WHITE
GAME_TITLE = "Froggy Road"
GAME_SPEED = 1 / 60

level1_width = WINDOW_WIDTH / 3
# level23_width = WINDOW_WIDTH / 7
offset1 = level1_width / 2
# offset23 = level23_width / 2
level_height = WINDOW_HEIGHT / 6
y_offset = level_height / 2
ROWS = 6
COLUMNS = 3

#intro_image=arcade.load_texture("images/frog.PNG",8)