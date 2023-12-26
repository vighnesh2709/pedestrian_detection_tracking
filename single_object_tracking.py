import cv2 as cv                                            
teList={"csrt"      : cv.TrackerCSRT_create,
        "kcf"       : cv.TrackerKCF_create, #kcf doesnt work
        "mil"       : cv.TrackerMIL_create,#mil too slow 
        'boosting'  : cv.legacy.TrackerBoosting_create,
        'medianflow' : cv.legacy.TrackerMedianFlow_create,
        'mosse'     : cv.legacy.TrackerMOSSE_create}              
#boosting, TDL,MOSSE,Medianflow are not recognised

tracker=teList['mosse']()

video=cv.VideoCapture('football.mp4')
ret,frame=video.read()  #reads first frame of the video
cv.imshow('frame',frame)
bb=cv.selectROI('frame',frame) #used to put a box around the object to be tracked (ROI is region of interest)
''' IDEA: basically, bb hold value of the 4 points around the object being detected, so now if we input the bb value to that of the object detected using haar cascading will/should it not track?'''
tracker.init(frame,bb)#used to initalize the tracker

while True:
    try:
        blah,frame=video.read()
        (success,box)=tracker.update(frame) #(bool,boundingBo),true if the targer was located based on the initalizec box and the bounding box returns the pixels of the box formed for the object, for images from frames
        if success:
            (x,y,w,h)=[int(a) for a in box]# it might return float values so we need to convert it to int and assign the values
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            cv.imshow('POOP',frame)
            key=cv.waitKey(5)&0xFF
            if key==ord('d'):
                break
                capture.release
                cv.destroyAllWindows
        else:
            print('video ended')
            break
    except:
        break
