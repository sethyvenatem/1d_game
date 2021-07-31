import time
from sys import stdout
from time import sleep
import keyboard
#import string
import random

path_length = 100
sleep_time = 0.15
opening_sleep_time = 0.5
string = '_'*path_length

#prepare the projectile
projectile_length = 7
letters = 'abcdefghijklmnopqrstuvwxyz'
proj = ''.join(random.choice(letters) for i in range(projectile_length))
proj_length = len(proj)
p = list(proj)

# all can be set to zero for debugging.
all = 1

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
    
    if all == 0:
        print(string)
    elif all == 1:
        stdout.write("\r")
        stdout.write(string)
        stdout.write("\r")
        stdout.flush()
    else:
        print('What do you want to print')

keyboard.start_recording()
events = keyboard.stop_recording()

#initialise string
s = list(string)
s.append('=o')
l = len(string)
string = "".join(s)

print_sequencially(string,all)
time.sleep(opening_sleep_time)

#Animate canon
s = list(string)
s[-1] = 'O'
string = "".join(s)
print_sequencially(string,all)
time.sleep(opening_sleep_time)

s = list(string)
s[-1] = '0'
string = "".join(s)
print_sequencially(string,all)
time.sleep(opening_sleep_time)

string = make_bold(string,path_length+1)
print_sequencially(string,all)
time.sleep(opening_sleep_time)

string = make_bold(string,path_length)
print_sequencially(string,all)
time.sleep(opening_sleep_time)

string = remove_all_bold(string)
s = list(string)
s[-2] = '>'
string = ''.join(s)
string = make_bold(string,path_length)
string = make_bold(string,path_length+1)
print_sequencially(string,all)
time.sleep(opening_sleep_time)

#The projectile enters here
s = list(string)
s[path_length-1] = p[0]
string = ''.join(s)
print_sequencially(string,all)
    
keyboard.start_recording()
time.sleep(opening_sleep_time)
events = keyboard.stop_recording()
    
for pos in range(path_length-2,path_length-proj_length-1,-1):
    s = list(string)
    s[pos:path_length] = p[0:path_length-pos]

    
    for ev in events:
        if ev.event_type == 'down':
            s[k] = ev.name
            ans = ans + ev.name
            k = k+1
    
    string = ''.join(s)
    print_sequencially(string,all)
    
    keyboard.start_recording()
    time.sleep(sleep_time)
    events = keyboard.stop_recording()


#The for loop starts when the projectile has entirely entered the path.
#pos denotes the left-most letter of the projectile. It runs to zero.

string = remove_all_bold(string)
s = list(string)
s[-1] = 'o'
s[-2] = '='
s[path_length-proj_length-1:path_length-1] = proj
s[path_length-1] = '_'
    
for ev in events:
    if ev.event_type == 'down':
        s[k] = ev.name
        ans = ans + ev.name
        k = k+1

        
string = "".join(s)
print_sequencially(string,all)

keyboard.start_recording()
time.sleep(sleep_time)
events = keyboard.stop_recording()

    
for pos in range(path_length-proj_length-2,-1,-1):

    s = list(string)
    s[pos:pos+proj_length] = proj
    s[pos+proj_length] = '_'
    
    for ev in events:
        if ev.event_type == 'down':
            s[k] = ev.name
            ans = ans + ev.name
            k = k+1

    
    string = "".join(s)

    print_sequencially(string,all)
    
    if pos+1 == len(ans):
        if ans == proj:
            print_sequencially('Horray, you win!  Press Esc to quit.',all)
            keyboard.wait('esc')
            quit()
        else:
            print_sequencially('Aw, you loose...  Press Esc to quit.',all)
            keyboard.wait('esc')
            quit()
    else:
        keyboard.start_recording()
        time.sleep(sleep_time)
        events = keyboard.stop_recording()
        
print_sequencially('You didn\'t enter anything... Don\'t you like my game?  Press Esc to quit.',all)
keyboard.wait('esc')
quit()
