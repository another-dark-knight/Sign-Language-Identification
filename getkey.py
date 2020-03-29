import cv2,os
import matplotlib.pyplot as plt


gesturespath = os.path.join('data','gestures')


gestures = os.listdir(gesturespath)
gestures.sort()
samples =[]

for gesture in gestures:
    g = os.path.join(gesturespath,gesture,'0.png')
    print(g)
    img = cv2.cvtColor(cv2.imread(g), cv2.COLOR_BGR2RGB) 
    samples.append(img)

size = int(len(gesture)**0.5)
if size == len(gesture):
    sizex, sizey = size,size
else:
    sizex, sizey = size, size+1

plt.figure(1)

for i in range(1,len(gestures)):
    plt.subplot(sizex,sizey, i)
    plt.imshow(samples[i-1])
    plt.title(gestures[i-1])

plt.show()
