# 1d_game
As a fun exercise, I made a typing game with python based on the print() function. The game interface is a string that is changed at each time step and displayed in the console.

The rules of the game are simple: There is a canon on the right-hand side of the screen that shoots words at the player (situated on the left-hand side of the screen). The player wins if they match the word being shot at them.

Here are ideas for improvement:
- The game breaks down if the player uses keyboard modifiers (upper case).
- - Fix this (make the game not break down).
- - Include upper case characters in the projectile.
- Make the animation look good.
- Make the game start over with an increased difficulty if the player wins. There are 3 parameters controling the difficulty: the projectile speed, the length of the path, the length of the projectile. Offer the player to choose which parameter is increased.
- Now, the game is quite hard: The words are strings of random characters. Make it easier by picking actual words from a list.
- Include a 'menu'
- - Ask the player's name and type it on the left side of the screen. This shortens the path of the projectile and makes the game harder for player with longer names.
- - Ask the player to choose between easy mode (words from a list) and expert mode (random words).
- Set up a system to keep track of the score. The score could be the number of words that were caught or the number of characters caught (longer words give more points).
- Export the score to a text file which is used to keep track of all the scores obtained. Then show a leaderboard at the end of the game.
