import arcade
import os
import random


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Define constants
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
BACKGROUND_COLOR = arcade.color.AERO_BLUE
GAME_TITLE = "Froggy Road"
GAME_SPEED = 1 / 60

#constants for drawing the "grid" of columns and rows to draw lillies, boats, frog, etc.
ROWS = 6
COLUMNS_1 = 3
COLUMNS_23 = 5
LEVEL1_WIDTH = WINDOW_WIDTH / COLUMNS_1
LEVEL23_WIDTH = WINDOW_WIDTH / COLUMNS_23
OFFSET1 = LEVEL1_WIDTH / 2
OFFSET23 = LEVEL23_WIDTH / 2
LEVEL_HEIGHT = WINDOW_HEIGHT / 6
Y_OFFSET = LEVEL_HEIGHT / 2