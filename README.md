# 1d_game
As a fun exercise, I made a typing game with python based on the print() function. The game interface is a string that is changed at each time step and displayed in the console. To run the game, open a terminal in the same folder as everything else and enter sudo ./1d_game.sh. The sudo is necessary to use the keyboard module, sorry.

The rules of the game are simple: There is a canon on the right-hand side of the screen that shoots words at the player (situated on the left-hand side of the screen). The player moves on to the next round if they type in the word being shot at them. The game ends when a word is not typed correctly. Also: 'Backspace' is disabled and the player can temporarily speed up the projectils by pressing 'Enter'.

The score is the sum of the number of characters in the player's name and the number of characters that were caught. I keep track of all the scores in scores.csv. At the end of the game, all the scores are displayed. If you play the game, then send me your 'scores.csv' and I'll merge it with mine here.

There is a hard-mode and an emoticon-mode that are also accessible.

Still to do:
- Get bash to ignore the keyboard inputs while I play. Once the word 'gs' came along and it immediately opened ghost view at the end of the game. Any help to fix this would be welcome.
- To make it look better, I use stty -echo and stty echo in the .sh file. This has the side effect that the input of the player is not displayed when the input() function is called. This is a problem at the beginning of the game where the player is asked to type their name but is not given feedback. One fix could be to re-invent the input() function using the keyboard module. Another smarter solution would be to better learn how to use stty -echo to solve this problem and the one above.
- Test (and fix) the emoticon mode

Here are additional ideas:
- Include upper case characters in the projectile.
- There are 3 parameters controling the difficulty: the projectile speed, the length of the path, the length of the projectile. Offer the player to choose which parameter is increased at the end of each round.
- Show two lines of text with first the state of the game (current score, projectile speed, path length, projectile legth)
- Offer a 'shield' bonus. If the player type 'shield' they are protected. This only works once. Maybe the player can earn additional shields along the way. Then if they type (by accident) 'shields', then all the shields are used at once and waisted.
