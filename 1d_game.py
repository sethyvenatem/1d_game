import time
from sys import stdout
from time import sleep
import keyboard
#import string
import random
import os
import pandas as pd
import numpy as np

path_length = 100
sleep_time = 0.15
opening_sleep_time = 0.5
fast = 0
string = '_'*path_length
hard = 0
emoticon = 0

#prepare the projectile
projectile_length = 1
letters = 'abcdefghijklmnopqrstuvwxyz'
proj = ''.join(random.choice(letters) for i in range(projectile_length))
p = list(proj)

# show_all_strings can be set to zero for debugging.
show_all_strings = 0

#These are the variables for the player answer. k is the answer length and ans is the anser
ans = ''
k = len(ans)


def remove_all_bold(string):
    string = string.replace('\x1b[1m','')
    string = string.replace('\x1b[0m','')
    return string
    
def cout_all_bold(string):    
    n = 0
    ind = string.find('\x1b[1m')
    while ind != -1:
        s = list(string)
        s[ind] = ''
        string = "".join(s)
        ind = string.find('\x1b[1m')
        n = n+1
    return n

def find_all_bold(string):
    ind = string.find('\x1b[1m')
    
    if ind == -1:
        n = []
    else:
        n = [ind]
        
    while ind != -1:
        s = list(string)
        s[ind] = ''
        s[ind+1] = ''
        s[ind+2] = ''
        s[ind+3] = ''
        s[ind+5] = ''
        s[ind+6] = ''
        s[ind+7] = ''
        s[ind+8] = ''
        string = "".join(s)
        ind = string.find('\x1b[1m')
        if ind != -1:
            n.append(ind)
    return n
    
def make_bold(string,n):
    #make the nth letter in the string bold
    
    bolds = find_all_bold(string)
    string = remove_all_bold(string)
    s = list(string)
    s[n] = '\x1b[1m'+s[n]+'\x1b[0m'
    
    for ind in bolds:
        if ind != n:
            s[ind] = '\x1b[1m'+s[ind]+'\x1b[0m'
            
    return "".join(s)

def print_sequencially(string,all):
    
    
    if all == 1:
        print(string)
    elif all == 0:
        os.system('clear')
        stdout.write("\r")
        stdout.write(string)
        stdout.write("\r")
        stdout.flush()
    else:
        print('What do you want to print')
        
def take_inputs(events, s, ans, k, sleep_time, fast):
    for ev in events:
        if (ev.event_type == 'down') and not(ev.name in keyboard.all_modifiers or ev.name == 'backspace'):
            if ev.name == 'space':
                s[k] = ' '
                ans = ans + ' '
                k = k+1
            elif ev.name == 'enter':
                if fast == 0:
                    sleep_time = sleep_time/10
                    fast = 1
            else:
                s[k] = ev.name
                ans = ans + ev.name
                k = k+1
    return s, k, ans, sleep_time, fast

intro = 'Please type in your name and press \'Enter\'.'
name = input(intro)
while (len(name) > path_length-1) or len(name)==0:
    print_sequencially('Sorry, your name is too long or too short. It will break my game. Please type in another name and press enter.',show_all_strings)
    name = input()
print_sequencially('Your name is '+name+'. Press \'Enter\' to continue.',show_all_strings)
_ = input()
name = name + ':'
score = len(name)

print_sequencially('The rules of this game are simple: You sit on the left and there is a cannon shooting words at you from the right. \n \nThe only way to protect yourself is to type in the word that is being shot before it reaches you. \n \nTwo more things: \n \n1. \'Backspace\' is disabled. Don\'t make mistakes! \n \n2. If you are sure of yourself you can press \'Enter\' to speed up the incoming word and end the round faster. \n \nPress \'Enter\' to start.',show_all_strings)
_ = input()

#The path is not displayed for the first few times after the projectile leaves the canon. This almost solves the problem. I don't know why.
keyboard.start_recording()
events = keyboard.stop_recording()
    
while True:
    k = len(name)
    ans = ''
    #initialise string
    string = '_'*path_length
    s = list(string)
    s.append('=o')
    s[0:len(name)] = list(name)
    string = "".join(s)

    print_sequencially(string,show_all_strings)
    time.sleep(sleep_time)

    #Animate canon
    s = list(string)
    s[-1] = 'O'
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(sleep_time)

    s = list(string)
    s[-1] = '0'
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(sleep_time)

    string = make_bold(string,path_length+1)
    print_sequencially(string,show_all_strings)
    time.sleep(sleep_time)

    string = make_bold(string,path_length)
    print_sequencially(string,show_all_strings)
    time.sleep(sleep_time)

    string = remove_all_bold(string)
    s = list(string)
    s[-2] = '>'
    string = ''.join(s)
    string = make_bold(string,path_length)
    string = make_bold(string,path_length+1)
    print_sequencially(string,show_all_strings)
    time.sleep(sleep_time)

    #The projectile enters here
    s = list(string)
    s[path_length-1] = p[0]
    string = ''.join(s)
    print_sequencially(string,show_all_strings)

    keyboard.start_recording()
    time.sleep(sleep_time)
    events = keyboard.stop_recording()

    for pos in range(path_length-2,path_length-projectile_length-1,-1):
        s = list(string)
        s[pos:path_length] = p[0:path_length-pos]


        s, k, ans, sleep_time, fast = take_inputs(events, s, ans, k, sleep_time, fast)

        string = ''.join(s)
        print_sequencially(string,show_all_strings)

        keyboard.start_recording()
        time.sleep(sleep_time)
        events = keyboard.stop_recording()


    #The for loop starts when the projectile has entirely entered the path.
    #pos denotes the left-most letter of the projectile. It runs to zero.

    string = remove_all_bold(string)
    s = list(string)
    s[-1] = 'o'
    s[-2] = '='
    s[path_length-projectile_length-1:path_length-1] = p
    s[path_length-1] = '_'

    s, k, ans, sleep_time, fast = take_inputs(events, s, ans, k, sleep_time, fast)

    string = "".join(s)
    print_sequencially(string,show_all_strings)

    keyboard.start_recording()
    time.sleep(sleep_time)
    events = keyboard.stop_recording()


    for pos in range(path_length-projectile_length-2,-1,-1):

        s = list(string)
        s[pos:pos+projectile_length] = p
        s[pos+projectile_length] = '_'

        s, k, ans, sleep_time, fast = take_inputs(events, s, ans, k, sleep_time, fast)


        string = "".join(s)

        print_sequencially(string,show_all_strings)

        if pos+1 == len(ans)+len(name):
            if ans == proj:
                print_sequencially('Horray, you win this round!  Press \'Enter\' to continue.',show_all_strings)
                keyboard.wait('enter')
                
                score = score + len(proj)
                
                #prepare a new projectile
                projectile_length = projectile_length + 1
                if (projectile_length > 14) and (hard == 0) and (emoticon == 0):
                    
                    print_sequencially('Congratulations you have reached the longest words in my dictionnary! Would you rather: \n1. Play in hard mode? Press \'h\'. \n2. Stop here? Press \'s\'. \n3. Play emoticon mode (your score will stop growing)? Press \'e\' \nThen press \'Enter\'.',show_all_strings)
                    events = keyboard.record('enter')
                    choice = events[1].name
                    
                    
                    if choice == 'h':
                        hard = 1
                        projectile_length = 1
                    elif choice == 's':
                        print_sequencially('Your score is '+str(score)+'! Press \'Enter\' to see the leaderboard.',show_all_strings)
                        keyboard.wait('enter')
                        scores_pd = pd.read_csv('scores.csv')
                        scores_pd = scores_pd.append(pd.DataFrame([[name[:-1], score]], columns=['player', 'score']), ignore_index = True)
                        scores_pd.to_csv('scores.csv', index = False)
                        lead = scores_pd.sort_values('score',ascending = False)
                        board = ''
                        for ind in range(len(lead)):
                            board = board + lead.player.values[ind]+' : '+str(lead.score.values[ind])+'\n'
                        board = board + '\nPress \'Esc\' to quit.'
                        print_sequencially(board,show_all_strings)
                        keyboard.wait('esc')
                        quit()
                    elif choice == 'e':
                        emoticon = 1
                        print_sequencially('Your score is '+str(score)+'! Press \'Enter\' to see the leaderboard.',show_all_strings)
                        keyboard.wait('enter')
                        scores_pd = pd.read_csv('scores.csv')
                        scores_pd = scores_pd.append(pd.DataFrame([[name[:-1], score]], columns=['player', 'score']), ignore_index = True)
                        scores_pd.to_csv('scores.csv', index = False)
                        lead = scores_pd.sort_values('score',ascending = False)
                        board = ''
                        for ind in range(len(lead)):
                            board = board + lead.player.values[ind]+' : '+str(lead.score.values[ind])+'\n'
                        board = board + '\nPress \'Enter\' to play emoticon-mode!'
                        print_sequencially(board,show_all_strings)
                        keyboard.wait('enter')
                    else:
                        print_sequencially('Something went wrong with your input. I\'ll set you to play on hard mode. Press \'Enter\' to continue.',show_all_strings)
                        keyboard.wait('enter')
                        hard = 1
                        projectile_length = 1
                        
                if hard == 1:
                    proj = ''.join(random.choice(letters) for i in range(projectile_length))
                    p = list(proj)
                if emoticon == 1:
                    words_raw = pd.read_csv('emoticons.csv',names = ['words'])
                    words_raw = words_raw.apply(lambda x: x[0],axis = 1)
                    proj = np.random.choice(words_raw.values, size = 1)[0]
                    p = list(proj)
                else:
                    words_raw = pd.read_csv('words_raw.csv',names = ['words'])
                    words_raw = words_raw.apply(lambda x: x[0],axis = 1).str.lower()
                    proj = np.random.choice(words_raw[words_raw.str.len() == projectile_length].values, size = 1)[0]
                    p = list(proj)
                
                if fast == 1:
                    fast = 0
                    sleep_time = 10*sleep_time
                    
                break

            else:
                if emoticon == 1:
                    print_sequencially('Aw, you loose... Thanks for playing for so long! Press \'Esc\' to quit.',show_all_strings)
                    keyboard.wait('esc')
                    quit()
                if hard == 1:
                    print_sequencially('Aw, you loose... Thanks for playing for so long! Press \'Esc\' to quit.',show_all_strings)
                    keyboard.wait('esc')
                    quit()
                else:
                    print_sequencially('Aw, you loose...  Your score is '+str(score)+'! Press \'Enter\' to see the leaderboard.',show_all_strings)
                    keyboard.wait('enter')
                    scores_pd = pd.read_csv('scores.csv')
                    scores_pd = scores_pd.append(pd.DataFrame([[name[:-1], score]], columns=['player', 'score']), ignore_index = True)
                    scores_pd.to_csv('scores.csv', index = False)
                    lead = scores_pd.sort_values('score',ascending = False)
                    board = ''
                    for ind in range(len(lead)):
                        board = board + str(lead.player.values[ind])+' : '+str(lead.score.values[ind])+'\n'
                    board = board + '\nPress \'Esc\' to quit'
                    print_sequencially(board,show_all_strings)
                    keyboard.wait('esc')
                    quit()
        else:
            keyboard.start_recording()
            time.sleep(sleep_time)
            events = keyboard.stop_recording()
