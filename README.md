# Froggy Road
A game using Arcade that plays on "Crossy Road" where a frog needs to leap on 
the lily pads to cross the pond without colliding with a moving boat. 
# About
This game involves a frog sprite the user controls. The frog can only move on the lily sprites (contained in a sprite
 list). The log sprites that the frog cannot move on are also contained in a sprite list and are randomly placed at a 
 random amount. If there is a collision between the frog and the list of boat sprites, then the user loses. The boats
  are randomly spaced out and moving in accordance to a speed that determines the dificulty of the game (user picks 
  between beginner, intermediate, and difficult). When the user makes it to the other side of the pond, there is another
  level they are taken to where they must cross two columns of boats. If the frog survives that, then the user wins. 
  Whether the user wins or loses, they are taken to a screen where they can reset the game. 
# Preview
...
# Installation
python Leaps_Bounds.py
# Instructions
Up, Down, Right, Left Arrow keys move the frog respectfully. The object of the game is for the frog cross the pond (to 
the right) without getting hit by a moving boat. The frog can only "leap" on the lilypads; the logs are obstacles! The 
user can choose different levels which control the speed of the boats, as it is easier to cross the pond if the boats 
are going slow and vice versa. If the game is over, the user can reset the game, which takes them back to the home 
screen where they can choose a new level.  
# Authors
Lauren Baron; lbaron@udel.edu
# Acknowledgements 
* graphics are not my own
    * http://arcade.photonstorm.com/
    * https://www.google.com/imghp
* used Views for multiple screens, looked at full examples
    * http://arcade.academy/examples/view_instructions_and_game_over.html#view-instructions-and-game-over
    * http://arcade.academy/examples/sprite_collect_coins_with_stats.html#sprite-collect-coins-with-stats
    * http://arcade.academy/examples/asteroid_smasher.html#asteroid-smasher
* introduction to how to use the Arcade library- Professor Bart's ArcadeActivities 
* inspiration for Froggy Road
    * https://poki.com/en/g/crossy-road