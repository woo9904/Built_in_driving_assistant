import cv2
import numpy as np
import keyboard
import os
import sys

def perspective_transform(img, pts, x, title):

    pts1 = np.float32([pts[0], pts[1], pts[3], pts[2]])
    
    w1 = abs(pts[3][0] - pts[2][0])
    w2 = abs(pts[1][0] - pts[0][0])
    h1 = abs(pts[1][1] - pts[3][1])
    h2 = abs(pts[0][1] - pts[2][1])
    width = max([int(w1), int(w2)])  
    height = max([int(h1), int(h2)]) 

    pts2 = np.float32([[0, 0], [width , 0], [width , height], [0, height]])

    mtrx = cv2.getPerspectiveTransform(pts1, pts2)
  
    result = cv2.warpPerspective(img, mtrx, (width, height))
    if x==0:
        cv2.imshow(title, result)
    elif x==1:
        return result
    
def getsize(capture1,capture2):
    re_D, img_D = capture2.read()
    re_B, img_B = capture1.read()
    img_D = cv2.resize(img_D, (1280,720))
    img_B = cv2.resize(img_B, (1280,720))
    cv2.imshow("image", img_D)
    for i in range (3):
        while True:
            perspective_transform(img_B, dir[0],0,"tl")
            perspective_transform(img_B, dir[2],0,"tr")
            if keyboard.is_pressed("d"):
                if i==0:
                    dir[i][0][1] = dir[i][0][1] + 10
                    dir[i][2][1] = dir[i][2][1] - 10
                elif i==2:
                    dir[i][1][1] = dir[i][1][1] - 10
                    dir[i][3][1] = dir[i][3][1] + 10
            elif keyboard.is_pressed("w"):
                for j in range (0,4):
                    dir[i][j][1]=dir[i][j][1] + 10
            elif keyboard.is_pressed("a"):
                if i==0:
                    dir[i][0][1] = dir[i][0][1] - 10
                    dir[i][2][1] = dir[i][2][1] + 10
                elif i==2:
                    dir[i][1][1] = dir[i][1][1] + 10
                    dir[i][3][1] = dir[i][3][1] - 10
            elif keyboard.is_pressed("x"):
                for j in range (0,4):
                    dir[i][j][1]=dir[i][j][1] - 10
            if cv2.waitKey() == ord('q'):
                break
    
    np.save('dir.npy', dir)
    cv2.destroyAllWindows()


val=int(sys.argv[1])

if os.path.isfile("./dir.npy")==True:
    dir=np.load('dir.npy')
else :
    right=[[1030,0],[1280,120],[1030,720],[1280,650]]
    left=[[75,120],[350,0],[75,620],[350,720]]
    nom=[[0,0],[0,0],[0,0],[0,0]]
    dir=[left,nom,right]

cap_builtin = cv2.VideoCapture("./Hill_B.mp4")
cap_driver = cv2.VideoCapture("./Hill_D.mp4")
fourcc=cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out=cv2.VideoWriter('v.mp4',fourcc,30.0,(1505,720))

if val==0:
    flag = getsize(cap_builtin,cap_driver)

while cap_builtin.isOpened() and cap_driver.isOpened() :
    ret, frame = cap_builtin.read()
    ret1, frame1 = cap_driver.read()
    rows, cols = frame.shape[:2]

    frame1=cv2.resize(frame1,(1280,720))
    frame=cv2.resize(frame,(1280,720))
    result_l = perspective_transform(frame, dir[0],1,"tl")
    result_r = perspective_transform(frame, dir[2],1,"tr")
    
    img_d=frame1[0:720,150:1130]
    img_con=np.concatenate([result_l,img_d], axis=1)
    img_con1=np.concatenate([img_con,result_r], axis=1)
    
    cv2.namedWindow('show',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('show', width=2000, height=1000)
    cv2.imshow('show',img_con1)
    out.write(img_con1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
cap_builtin.release()
cap_driver.release()
out.release()
cv2.destroyAllWindows()
