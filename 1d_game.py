import time
from time import sleep
import keyboard
import random
import os
import pandas as pd
import numpy as np
from sys import stdout

path_length = 100
sleep_time = 0.1
opening_sleep_time1 = 0.1
opening_sleep_time2 = 0.15
fast = 0
empty_path = '_'
string = empty_path*path_length
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
        #os.system('clear')
        #print(string)
        
        stdout.flush()
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

def print_leaderboard(name,score,emoticon):
    scores_pd = pd.read_csv('scores.csv')
    scores_pd = scores_pd.append(pd.DataFrame([[name[:-1], score]], columns=['player', 'score']), ignore_index = True)
    scores_pd.to_csv('scores.csv', index = False)
    lead = scores_pd.sort_values('score',ascending = False)
    board = '\n \n'
    for ind in range(len(lead)):
        board = board + lead.player.values[ind]+' : '+str(lead.score.values[ind])+'\n'
    if emoticon == 1:
        board = board + '\nPress \'Enter\' to play emoticon-mode! Sorry, it\'s still a bit buggy... :('
    else:
        board = board + '\nPress \'Esc\' to quit.'
        
    return board

intro = 'Please type in your name and press \'Enter\'.'
os.system('clear')
name = input(intro)
while (len(name) > path_length-1) or len(name)==0:
    print_sequencially('\n \nSorry, your name is too long or too short. It will break my game. Please type in another name and press enter.',show_all_strings)
    name = input()
#os.system('clear')
print_sequencially('\n \nYour name is '+name+'. Press \'Enter\' to continue.',show_all_strings)
_ = input()
name = name + ':'
score = len(name)

print_sequencially('\n \nThe rules of this game are simple: You sit on the left and there is a cannon shooting words at you from the right. \n \nThe only way to protect yourself is to type in the word that is being shot before it reaches you. \n \nTwo more things: \n \n1. \'Backspace\' is disabled. Don\'t make mistakes! \n \n2. If you are sure of yourself you can press \'Enter\' to speed up the incoming word and end the round faster. \n \nPress \'Enter\' to start.',show_all_strings)
_ = input()

#The path is not displayed for the first few times after the projectile leaves the canon. This almost solves the problem. I don't know why.
keyboard.start_recording()
events = keyboard.stop_recording()
    
while True:
    k = len(name)
    ans = ''
    #initialise string
    string = empty_path*path_length
    s = list(string)
    s.append(empty_path+empty_path+'=O')
    s[0:len(name)] = list(name)
    string = "".join(s)

    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time1)

    s = list(string)
    s[-1] = '0'
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time1)
    
    string = make_bold(string,-1)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time1)
    
    string = remove_all_bold(string)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time1)
    
    s = list(string)
    s[-1] = '0'
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time1)
    
    s = list(string)
    s[-1] = 'O'
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time1)
    
    s = list(string)
    s[-1] = '0'
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time1)
    
    string = make_bold(string,-1)
    print_sequencially(string,show_all_strings)
    sleep_time_anim = 0.3
    time.sleep(opening_sleep_time2)

    string = remove_all_bold(string)
    s = list(string)
    s[-1] = 'o'
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time2)
    
    string = remove_all_bold(string)
    s = list(string)
    s[-3] = '='
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time2)
    
    string = remove_all_bold(string)
    s = list(string)
    s[-4] = '='
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time2)
    
    string = remove_all_bold(string)
    string = make_bold(string,-2)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time2)

    string = remove_all_bold(string)
    string = make_bold(string,-3)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time2)
    
    string = remove_all_bold(string)
    string = make_bold(string,-4)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time2)
    
    string = remove_all_bold(string)
    s = list(string)
    s[-4] = '>'
    string = ''.join(s)
    string = make_bold(string,-4)
    print_sequencially(string,show_all_strings)
    time.sleep(opening_sleep_time1)

    keyboard.start_recording()
    
    #The projectile enters here
    s = list(string)
    s[path_length-1] = p[0]
    string = ''.join(s)
    print_sequencially(string,show_all_strings)
    time.sleep(sleep_time)

    events = keyboard.stop_recording()

    for pos in range(path_length-2,path_length-projectile_length-1,-1):
        
        keyboard.start_recording()
        
        s = list(string)
        s[pos:path_length] = p[0:path_length-pos]
        s, k, ans, sleep_time, fast = take_inputs(events, s, ans, k, sleep_time, fast)
        string = ''.join(s)
        print_sequencially(string,show_all_strings)
        
        time.sleep(sleep_time)
        events = keyboard.stop_recording()

    keyboard.start_recording()
    
    string = remove_all_bold(string)
    s = list(string)
    s[-1] = 'o'
    s[-2] = '='
    s[-3] = empty_path
    s[-4] = empty_path
    s[path_length-projectile_length-1:path_length-1] = p
    s[path_length-1] = empty_path
    s, k, ans, sleep_time, fast = take_inputs(events, s, ans, k, sleep_time, fast)
    string = "".join(s)
    print_sequencially(string,show_all_strings)
    
    time.sleep(sleep_time)
    events = keyboard.stop_recording()

    #The for loop starts when the projectile has entirely entered the path.
    #pos denotes the left-most letter of the projectile. It runs to zero.
    for pos in range(path_length-projectile_length-2,-1,-1):

        keyboard.start_recording()
        
        s = list(string)
        s[pos:pos+projectile_length] = p
        s[pos+projectile_length] = empty_path
        s, k, ans, sleep_time, fast = take_inputs(events, s, ans, k, sleep_time, fast)
        string = "".join(s)
        print_sequencially(string,show_all_strings)
            
            
        if pos+1 == len(ans)+len(name)+1:
            if ans == proj:
                
                time.sleep(sleep_time)
                events = keyboard.stop_recording()
            
                print_sequencially('\n \nHorray, you win this round!  Press \'Enter\' to continue.',show_all_strings)
                keyboard.wait('enter')
                
                score = score + len(proj)
                
                #prepare a new projectile
                projectile_length = projectile_length + 1
                if (projectile_length > 14) and (hard == 0) and (emoticon == 0):
                    
                    print_sequencially('\n \nCongratulations you have reached the longest words in my dictionnary! Would you rather: \n1. Play in hard mode? Press \'h\'. \n2. Stop here? Press \'s\'. \n3. Play emoticon mode (your score will stop growing)? Press \'e\' \nThen press \'Enter\'.\n \n',show_all_strings)
                    events = keyboard.record('enter')
                    choice = events[1].name                    
                    
                    if choice == 'h':
                        hard = 1
                        projectile_length = 1
                    elif choice == 's':
                        print_sequencially('\n \nYour score is '+str(score)+'! Press \'Enter\' to see the leaderboard.',show_all_strings)
                        keyboard.wait('enter')
                        board = print_leaderboard(name,score,emoticon)
                        print_sequencially(board,show_all_strings)
                        keyboard.wait('esc')
                        quit()
                    elif choice == 'e':
                        emoticon = 1
                        print_sequencially('\n \nYour score is '+str(score)+'! Press \'Enter\' to see the leaderboard.',show_all_strings)
                        keyboard.wait('enter')
                        board = print_leaderboard(name,score,emoticon)
                        print_sequencially(board,show_all_strings)
                        keyboard.wait('enter')
                    else:
                        print_sequencially('\n \nSomething went wrong with your input. I\'ll set you to play on hard mode. Press \'Enter\' to continue.',show_all_strings)
                        keyboard.wait('enter')
                        hard = 1
                        projectile_length = 1
                        
                if hard == 1:
                    proj = ''.join(random.choice(letters) for i in range(projectile_length))
                    p = list(proj)
                elif emoticon == 1:
                    words_raw = pd.read_csv('emoticons.csv',names = ['words'])
                    words_raw = words_raw.apply(lambda x: x[0],axis = 1)
                    proj = np.random.choice(words_raw.values, size = 1)[0]
                    p = list(proj)
                    projectile_length = len(proj)
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
                time.sleep(sleep_time)
                events = keyboard.stop_recording()
                
                if emoticon == 1:
                    print_sequencially('\n \nAw, you loose... Thanks for playing for so long! Press \'Esc\' to quit.',show_all_strings)
                    keyboard.wait('esc')
                    quit()
                if hard == 1:
                    print_sequencially('\n \nAw, you loose... Thanks for playing for so long! Your score is '+str(score)+'! Press \'Enter\' to see the leaderboard.',show_all_strings)
                    keyboard.wait('enter')
                    board = print_leaderboard(name,score,emoticon)
                    print_sequencially(board,show_all_strings)
                    keyboard.wait('esc')
                    quit()
                else:
                    print_sequencially('\n \nAw, you loose...  Your score is '+str(score)+'! Press \'Enter\' to see the leaderboard.',show_all_strings)
                    keyboard.wait('enter')
                    board = print_leaderboard(name,score,emoticon)
                    print_sequencially(board,show_all_strings)
                    keyboard.wait('esc')
                    quit()
        else:
            time.sleep(sleep_time)
            events = keyboard.stop_recording()
