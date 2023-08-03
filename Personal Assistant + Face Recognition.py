import face_recognition
import cv2
import os
import numpy as np
import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib

video_capture = cv2.VideoCapture(0)


person_image = face_recognition.load_image_file(r"ADD YOUR PICTURE HERE")
person_face_encoding = face_recognition.face_encodings(person_image)[0]

known_face_encodings = [

    person_face_encoding
]
known_face_names = [

    "PERSON NAME"
]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:

    ret, frame = video_capture.read()


    if process_this_frame:

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)


        rgb_small_frame = small_frame[:, :, ::-1]


        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"


            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

            if name == "Unknown":
            
                print("Not Authorized")
                quit()

            else:
                process_this_frame = not process_this_frame


                for (top, right, bottom, left), name in zip(face_locations, face_names):

                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4


                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


                cv2.imshow('Video', frame)


                if cv2.waitKey(1) & 0xFF == ord('q'):
                    quit()


                video_capture.release()
                cv2.destroyAllWindows()

                engine = pyttsx3.init("sapi5")
                voices = engine.getProperty('voices')

                engine.setProperty('voices', voices[1].id)
                engine.setProperty('rate', 150)

                webbrowser.register('chrome',
                                    None,
                                    webbrowser.BackgroundBrowser(
                                        "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))


                def speak(audio):
                    engine.say(audio)
                    print(audio)
                    engine.runAndWait()


                def take_command():

                    r = sr.Recognizer()
                    my_mic = sr.Microphone(device_index=1)
                    with my_mic as source:
                        print("Listening...")
                        r.pause_threshold = 12
                        audio = r.listen(source, timeout=11, phrase_time_limit=10)
                        print(r.recognize_google(audio))
                        try:
                            print("Recognizing...")
                            query = r.recognize_google(audio, language='en-in')
                            print(f'User said:{query}\n')


                        except Exception as e:
                            print("Say that again please")
                            return "None"
                        return query


                def wishMe():
                    hour = int(datetime.datetime.now().hour)
                    if hour >= 0 and hour < 12:
                        speak("Good Morning!")


                    elif hour >= 12 and hour < 18:
                        speak("Good Afternoon!")

                    else:
                        speak("Good Evening!")

                    speak("I am Vision, Your Personal Assistant")
                    speak("How may I help you?")


                def sendEmail(to, content):
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login('SENDER EMAIL', 'ENTER THE APP PASSWORD')
                    server.sendmail('SENDER EMAIL', to, content)
                    server.close()


                if __name__ == "__main__":
                    wishMe()
                    while True:
                        query = take_command().lower

                        if 'youtube' in query():
                            url1 = 'https://youtube.com//'
                            webbrowser.get('chrome').open_new(url1)
                            quit()

                        if 'middle east college' in query():
                            url2 = 'https://mec.edu.om/meckathon2022//'
                            webbrowser.get('chrome').open_new(url2)
                            quit()



                        if "school gmail" in query():
                            url7 = 'https://mail.google.com/mail/u/2/#inbox'
                            webbrowser.get('chrome').open_new(url7)
                            quit()

                        if "personal gmail" in query():
                            url8 = 'https://mail.google.com/mail/u/0/#inbox'
                            webbrowser.get('chrome').open_new(url8)
                            quit()

                        if "stack overflow" in query():
                            url4 = 'https://stackoverflow.com/'
                            webbrowser.get('chrome').open_new(url4)
                            quit()

                        if "bing" in query():
                            url5 = 'https://bing.com//'
                            webbrowser.get('chrome').open_new(url5)
                            quit()

                        

                        if "microsoft edge" in query():
                            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
                            quit()

                        if "control panel" in query():
                            os.startfile(
                                r"directory of Control Panel.lnk")
                            quit()

                        if "word" in query():
                            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE.EXE")
                            quit()

                        if "excel" in query():
                            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
                            quit()

                        if "command prompt" in query():
                            os.startfile(r"C:\Windows\system32\cmd")
                            quit()

                        if "file explorer" in query():
                            os.startfile(
                                r"directory of file explorer")
                            quit()

                        if "python" in query():
                            os.startfile(r"directory of python")
                            quit()


                        if "email" in query():
                            try:
                                speak("what should I say sir?")
                                content = take_command().lower()
                                d = {"Person 1": "EMAIL ADDRESS OF RECIEVER 1", "PERSON 2": "EMAIL ADDRESS OF RECIEVER 2"}
                                print("Email can be sent to: 1.Person 1 , 2. Person 2")
                                speak("enter the name of the person to whom the email should be sent:")
                                p = take_command().lower()
                                if p in d:
                                    to = d[p]
                                sendEmail(to, content)
                                speak("Email has been sent to person.")

                            except Exception as e:
                                print(e)
                                speak("sorry, email could not be sent")

                        if "thanks" or "thankyou" or "bye" in query():
                            speak("Thankyou for using Vision")
                            quit()

            
 
