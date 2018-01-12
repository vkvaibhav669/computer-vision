import cv2


#cascades loading
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(gray , frame):
    faces = face_cascade.detectMultiScale(gray , 1.3 , 5)
    #1.3 is the scale factor or size of reduction of image
    #5 is the minumum number of neighbour
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2 )
        #upper left corner is 2nd argument
        #3rd is lower right
        #4th is 4th arg is colour
        #colour is
        #thickness of rectangle
        roi_gray = gray[y:y+h, x:x+h]#zone of intrest
        roi_color = frame[y:y+h, x:x+h]
        eyes = eye_cascade.detectMultiScale(roi_gray , 1.1 , 3)
        #eyes has to be some colour
        #neighbour and scale factor has to be same
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2 )
    return frame
#detecting video
#video_capture CascadeClassifer
video_capture = cv2.VideoCapture(0)#0 for webcam 1 for external camera
while True:
    _, frame = video_capture.read()#orignal image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)##gray image
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()#turns webcamp off
