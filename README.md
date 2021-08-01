# 1d_game
As a fun exercise, I made a typing game with python based on the print() function. The game interface is a string that is changed at each time step and displayed in the console.

The rules of the game are simple: There is a canon on the right-hand side of the screen that shoots words at the player (situated on the left-hand side of the screen). The player wins if they match the word being shot at them.

Here are ideas for improvement:
- Enable the player to press enter when they are satisfied to speed up the projectile.
- Include upper case characters in the projectile.
- Make the animation look good.
- Make the game start over with an increased difficulty if the player wins. There are 3 parameters controling the difficulty: the projectile speed, the length of the path, the length of the projectile. Offer the player to choose which parameter is increased.
- Now, the game is quite hard: The words are strings of random characters. Make it easier by picking actual words from a list.
- Include a 'menu'
- - Ask the player's name and type it on the left side of the screen. This shortens the path of the projectile and makes the game harder for player with longer names.
- - Ask the player to choose between easy mode (words from a list) and expert mode (random words). Maybe I can hide an 'emoji mode' in the game.
- Set up a system to keep track of the score.
- - The score could be the number of words that were caught or the number of characters caught (longer words give more points).
- - The initial score is the number of characters in the player's name. This offsets (a bit) the disadvantage of long names.
- - Export the score to a text file which is used to keep track of all the scores obtained. Then show a leaderboard at the end of the game.
- Show two lines of text with first the state of the game (current score, projectile speed, path length, projectile legth)
- Offer a 'shield' bonus. If the player type 'shield' they are protected. This only works once. Maybe the player can earn additional shields along the way. Then if they type (by accident) 'shields', then all the shields are used at once and waisted.
- By construction, the framerate is directly tied to the speed of the prjectile. With the current parameters, it's a bit hard to catch the projectile but not too much. It is howewver hard to read because the projectile does not move smoothly. I could try to increase the framerate (without speeding up the projectile) by having a two-step animation (described below). This should double the frame-rate for a given projectile speed. I would have to do something with the right-most '_' as well so that the cannon does not shake. I would have to experiment with the character to replace '_' to make it look good.
- - first change the left-most '_' for '.' (or ':'). This shortens the path a bit and moves the projectile to the left by less than an entire underscore.
- - restore the left-most '_' and move the projectile at the same time.
