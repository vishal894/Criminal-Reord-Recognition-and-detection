import cv2
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root@123", db="demo")
mycursor = mydb.cursor()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

cap = cv2.VideoCapture(0)

while True:
    ret, Criminal = cap.read()
    gray = cv2.cvtColor(Criminal, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:

        roi_gray = gray[y:y + h, x:x + w]

        id_, conf = recognizer.predict(roi_gray)
        print(id_)
        if conf >= 40 and conf <= 70:

            mycursor.execute("SELECT * FROM criminal_record where id='1'")
            #mycursor.execute("""SELECT * FROM `criminal_record` WHERE `name`='{}'""".format(name))

            user = mycursor.fetchone()
            #for i in result:
                #a = i

            name = user[1]
            print(name)
            cv2.rectangle(Criminal, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.rectangle(Criminal, (x, y+h - 35), (x+w, y+h), (0, 255, 0), cv2.FILLED)
            cv2.putText(Criminal, name, (x , y+h-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            cv2.putText(Criminal, "Criminal Record Of Victim", (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

            cv2.line(Criminal, (32, 38), (500, 38), (0, 0, 255), 2)
            cv2.putText(Criminal, user[1], (30, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

            cv2.putText(Criminal, str(user[2]), (30, 280), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 1)

            cv2.putText(Criminal, user[3], (30, 130), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

            cv2.putText(Criminal, user[4], (30, 160), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

            cv2.putText(Criminal, user[5], (30, 190), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            cv2.putText(Criminal, str(user[6]), (30, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            cv2.putText(Criminal, user[7], (30, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    cv2.imshow('Criminal', Criminal)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()