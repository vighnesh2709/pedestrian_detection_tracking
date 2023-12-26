import cv2 as cv
import matplotlib.pyplot as plt
video=cv.VideoCapture('walking.mp4')
haar_cascade=cv.CascadeClassifier('full_body_detect.xml')
while True:
    
    isTrue,frames=video.read() #reading each frame of the program
    frame=cv.resize(frames,(500,500))#resizing the video   
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#converting it to gray scale
    ret,tresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
    cv.imshow('treshold',tresh)
    cv.imshow('fall',frame)
    cv.imshow('gray_vid',gray)
    gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
    plt.figure()
    plt.title('histogram')
    plt.xlabel('Bins')
    plt.ylabel('pixels')
    plt.plot(gray_hist)
    plt.xlim([0,256])
    plt.show()
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
video.release()
cv.destroyAllWindows()