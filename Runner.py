'''
Created on Feb 16, 2013

@author: mzhong
'''
import cv, time
import handdetect

def getGesture(gesture, nth):
    global startTime
    if nth == 1:
        while time.time() - startTime < 6: 
            frame = cv.QueryFrame(capture)
            cv.ShowImage('w1', frame)
        cv.SaveImage(gesture + ".jpg", frame)
    else:
        while time.time() - startTime < 6*nth + 2*(nth-1):
            frame = cv.QueryFrame(capture)
            if(time.time()-startTime > 6*(nth-1) + 2*(nth-1)):
                cv.ShowImage('w1', frame)
        cv.SaveImage(gesture + ".jpg", frame)
    validatePassword(gesture, frame)

def validatePassword(gesture, frame):
    frame = getSkin(gesture, frame)
    mass = getMass(frame)
    center = getCenterOfMass(frame)
    xLength = getXLength(frame)
    yLength = getYLength(frame)
    
def getSkin(gesture, frame):
    #handdetect came from black box solution via https://raw.github.com/thisismyrobot/gnomecam/master/hand-detect.py
    frame = handdetect.get_hands(frame) 
    cv.SaveImage(gesture + ".jpg", frame)
    return frame

def getMass(frame):
    return cv.CountNonZero(frame)

def getCenterOfMass(frame):
    pass
def getYLength(frame):
    pass
def getXLength(frame):
    pass

if __name__ == '__main__':
    #configure frame
    cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
    capture = cv.CaptureFromCAM(0) 
    startTime = time.time()
    getGesture("fist1", 1)
    getGesture("palm", 2)
    getGesture("fist2", 3)