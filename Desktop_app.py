from desktop import *
import cv2
import winsound
from pynput.keyboard import Key, Controller
import time

def app():
    speak("What app you want to open sir?")
    value = True
    while value:

        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("I am opening notepad sir.")

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(apath)
            speak("I am opening adobe reader")

        elif "open word" in query:
            speak("Opening word")
            wpath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\Winword.exe"
            os.startfile(wpath)

        elif "open powerpoint" in query:
            speak("Opening powerpoint")
            ppath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ppath)

        elif "code" in query:
            speak("Opening visual studio code")
            cpath = "E:\\Software Document\\Microsoft VS Code\\Code.exe"
            os.startfile(cpath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "play quran" in query:
            speak("Ok sir. Playing Quran.")
            music_dir = "H://Al Quran"
            s = os.listdir(music_dir)
            rd = random.choice(s)
            for song in s:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, rd))

        elif "open browser" in query:
            speak("Opening chromo browser")
            chpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chpath)

        elif 'where' in query:
            speak("you are in app section sir.")
        
        elif 'out' in query:
            value = False
    speak("You are out of the app section sir.")




def camera():
    cam = cv2.VideoCapture(0)
  
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('Granny cam', frame1)
       

def auto():
    keyboard = Controller()
    time.sleep(5)
    Value = True
    while Value:
        query = takecommand().lower()    
        keyboard.press('j')
        keyboard.release('j')

        keyboard.press('l')
        keyboard.release('l')

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
       