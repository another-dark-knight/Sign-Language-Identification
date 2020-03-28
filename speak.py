import os
def speak(x):
    os.system('espeak -a 150 -g 15 -s 150 "'+x+'"</dev/null &>/dev/null')
    print("Successfully spoken")
