import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Define constants
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
BACKGROUND_COLOR = arcade.color.WHITE
GAME_TITLE = "Froggy Road"
GAME_SPEED = 1 / 60

#variables the sprites and views need about the window to draw things
level1_width = WINDOW_WIDTH / 3
# level23_width = WINDOW_WIDTH / 7
offset1 = level1_width / 2
# offset23 = level23_width / 2
level_height = WINDOW_HEIGHT / 6
y_offset = level_height / 2
LILLIES = 6
ROWS = 3