# 1d_game
As a fun exercise, I made a typing game with python based on the print() function. The game interface is a string that is changed at each time step and displayed in the console.

The rules of the game are simple: There is a canon on the right-hand side of the screen that shoots words at the player (situated on the left-hand side of the screen). The player moves on to the next round if they type in the word being shot at them. The game ends when a word is not typed correctly. Also: 'Backspace' is disabled and the player can temporarily speed up the projectils by pressing 'Enter'.

The score is the sum of the number of characters in the player's name and the number of characters that were caught. I keep track of all the scores in scores.csv. At the end of the game, all the scores are displayed. If you play the game, then send me your 'scores.csv' and I'll merge it with mine here.

There is a hard-mode and an emoticon-mode that are also accessible.

Still to do:
- Make the animation look good.
- By construction, the framerate is directly tied to the speed of the prjectile. With the current parameters, it's a bit hard to catch the projectile but not too much. It is howewver hard to read because the projectile does not move smoothly. I could try to increase the framerate (without speeding up the projectile) by having a two-step animation (described below). This should double the frame-rate for a given projectile speed. I would have to do something with the right-most '_' as well so that the cannon does not shake. I would have to experiment with the character to replace '_' to make it look good.
- - first change the left-most '_' for '.' (or ':'). This shortens the path a bit and moves the projectile to the left by less than an entire underscore.
- - restore the left-most '_' and move the projectile at the same time.
- Get bash to ignore the keyboard inputs while I play. Once the word gs came along and it immediately opened ghost view at the end of the game. Any help to fix this would be welcome.

Here are additional ideas:
- Include upper case characters in the projectile.
- There are 3 parameters controling the difficulty: the projectile speed, the length of the path, the length of the projectile. Offer the player to choose which parameter is increased at the end of each round.
- Show two lines of text with first the state of the game (current score, projectile speed, path length, projectile legth)
- Offer a 'shield' bonus. If the player type 'shield' they are protected. This only works once. Maybe the player can earn additional shields along the way. Then if they type (by accident) 'shields', then all the shields are used at once and waisted.
