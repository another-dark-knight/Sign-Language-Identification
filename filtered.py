import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    frame = cv2.resize(frame,(600,600))
    im_ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    skin_ycrcb_mint = np.array((0, 133, 77))
    skin_ycrcb_maxt = np.array((255, 173, 127))
    skin_ycrcb = cv2.inRange(im_ycrcb, skin_ycrcb_mint, skin_ycrcb_maxt)

    filtered = cv2.GaussianBlur(skin_ycrcb,(5,5),0.2)
    filtered = cv2.medianBlur(skin_ycrcb, 7)

    cv2.imshow("ycrcb", filtered)
    #cv2.imshow("stream", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
