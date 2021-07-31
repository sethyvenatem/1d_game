import time
from sys import stdout
from time import sleep
import keyboard

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

sleep_time = 0.1
string = '_'*100
s = list(string)
s.append('>o')
string = "".join(s)
l = len(string)
proj = 'x'
all = 1

print_sequencially(string,all)
time.sleep(sleep_time)

s = list(string)
s[-1] = 'O'
s[-2] = '>'
string = "".join(s)
print_sequencially(string,all)
time.sleep(sleep_time)

s = list(string)
s[-1] = '0'
s[-2] = '>'
string = "".join(s)
print_sequencially(string,all)
time.sleep(sleep_time)

string = make_bold(string,l-1)
print_sequencially(string,all)
time.sleep(sleep_time)

string = remove_all_bold(string)
string = make_bold(string,l-2)
print_sequencially(string,all)
time.sleep(sleep_time)

s = list(string)
s[l-3] = proj
s[-1] = 'O'
string = ''.join(s)
print_sequencially(string,all)

keyboard.start_recording()
time.sleep(sleep_time)
events = keyboard.stop_recording()

s = list(string)
s[-1] = 'o'
s[l-3] = '_'
s[l-4] = proj

k = 0
for ev in events:
    if ev.event_type == 'down':
        s[k] = ev.name
        k = k+1

string = "".join(s)
print_sequencially(string,all)

keyboard.start_recording()
time.sleep(sleep_time)
events = keyboard.stop_recording()


sleep_time = 0.05
for pos in range(5,l+1,1):

    s = list(string)
    s[l-pos] = 'x'
    s[l-pos+1] = '_'
    
    for ev in events:
        if ev.event_type == 'down':
            s[k] = ev.name
            k = k+1


    string = "".join(s)

    print_sequencially(string,all)
    
    keyboard.start_recording()
    time.sleep(sleep_time)
    events = keyboard.stop_recording()

