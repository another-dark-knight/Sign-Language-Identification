import cv2
import time
import numpy as np
import os

cap = cv2.VideoCapture(0)
startx, starty = start =(45,80)
endx, endy = end = (290,380)
datapath='data'
gesturepath = os.path.join(datapath,'gestures')
def makedir(x):
    try:
        os.mkdir(x)
    except:
        print(x + " Exists")

words = np.genfromtxt(os.path.join(datapath,'vocab.csv'),dtype=str, delimiter='\n')
print(words)

if not os.path.exists(gesturepath):
    makedir(gesturepath)

i=0
k=0
wordpath=None
a = len(words)
while True and i<a:
    if i==0:
        wordpath = os.path.join(gesturepath,words[i])
        makedir(wordpath)
        k = len(os.listdir(wordpath))     
    ret, frame = cap.read()
    frame = cv2.resize(frame,(600,600))
    cv2.rectangle(frame,start,end,(0,0,255),2)
    hand = cv2.resize(frame[starty:endy, startx:endx], (300,300))
    hand2 = cv2.flip(hand,1)
    frame = cv2.flip(frame,1)
    cv2.putText(frame,"Record " + words[i],10,500, cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0))
    cv2.imshow("stream", frame)
    cv2.imshow("hand",hand2)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        cv2.imwrite(os.path.join(wordpath,str(k)+".png"), hand)
        k = k + 1
        cv2.imwrite(os.path.join(wordpath,str(k)+".png"), hand2)
        k = k + 1

    if key==ord("n"):
        i = i+1
        try:
            wordpath = os.path.join(gesturepath,words[i])
            makedir(wordpath)
            k=len(os.listdir(wordpath))
        except:
            print("Words over!")
            break

    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
