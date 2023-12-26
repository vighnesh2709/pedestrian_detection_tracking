import cv2 as cv
import time
video=cv.VideoCapture("tracklimits.mp4")#reading the video
haar_cascade=cv.CascadeClassifier('full_body_detect.xml')#putting the human detecting xml file into a variable
per_timeframe=0
new_timeframe=0
while True:
 try:   

    isTrue,frames=video.read() #reading each frame of the program
    frame=cv.resize(frames,(500,500))#resizing the video   
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#converting it to gray scale
    ret,tresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)#tresholdong(i.e checking if the pixel has value over some colour and if its there then it convers the image to black)
    
    cv.imshow('treshold',tresh)
    cv.imshow('fall',frame)
    cv.imshow('gray_vid',gray)
    


    body=haar_cascade.detectMultiScale(tresh,1.9,1)#detecting the human and returns a 4 pixel around the image
    
    new_timeframe=time.time()
    fps=1/(new_timeframe-per_timeframe)
    per_timeframe=new_timeframe
    fps=int(fps)
    cv.putText(frame,str(fps),(8,80),cv.FONT_HERSHEY_TRIPLEX,0.5,(0,0,255),thickness=1)

    for(x,y,w,h) in body:
        cv.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),thickness=3)#drawing the box around the image
        
        if x!=0:
            cv.putText(frame,"DETECTED",(0,126),cv.FONT_HERSHEY_TRIPLEX,0.5,(0,0,255),thickness=1)



    cv.imshow('final',frame)

        

    key=cv.waitKey(20)&0xFF
    if key==ord('d'):
        break
        capture.release
        cv.destroyAllWindows
 except:
    break

