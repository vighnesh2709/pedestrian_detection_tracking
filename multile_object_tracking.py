import cv2 as cv
teList={"csrt"      : cv.TrackerCSRT_create,
        "kcf"       : cv.TrackerKCF_create, #kcf doesnt work
        "mil"       : cv.TrackerMIL_create,#mil too slow 
        'boosting'  : cv.legacy.TrackerBoosting_create,
        'medianflow': cv.legacy.TrackerMedianFlow_create,
        'mosse'     : cv.legacy.TrackerMOSSE_create,
        'GOTURN'    :cv.TrackerGOTURN_create}#it is not able to open the file  

trackers=cv.legacy.MultiTracker_create()
video=cv.VideoCapture('football.mp4')
boo,frame=video.read()
cv.imshow('frame',frame)
for i in range(2):
    bbi=cv.selectROI('frame',frame)
    tracker_i=teList['csrt']()
    trackers.add(tracker_i,frame,bbi)

while True:
    try:
        ha,frame=video.read()
        if ha==False:
            break
        (success,boxes)=trackers.update(frame)
        for box in boxes:
            [x,y,w,h]=[int (a) for a in box]
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            cv.imshow('video',frame)
        key=cv.waitKey(5)& 0xFF
        if key==ord('d'):
            break
            capture.release
            cv.destroyAllWindows
    except:
        break    


    