#Import libraries
import cv2
import webbrowser
import pyautogui as pag
import time
from pynput import keyboard
from sys import exit

#Have the camera take a picture
camera = cv2.VideoCapture(0)
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('Camera.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()
img = cv2.imread("Camera.jpg")

#Detect QR code and open it
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)

webbrowser.open(f'{data}')        
time.sleep(9)


#While program is running
while True:
    try:
        #Press play and shuffle buttons
        Play = pag.locateCenterOnScreen("playbutton.png", grayscale= False, confidence=0.9)
        x,y = Play
        pag.moveTo(x,y,0)
        pag.leftClick()

        time.sleep(3)

        Shuffle = pag.locateCenterOnScreen("Shuffle.png", grayscale= False, confidence=0.9)
        x,y = Shuffle
        pag.moveTo(x,y,0)
        pag.leftClick()
        break
    except:
        None

#Key presses
def on_press(key):
    #Skip
    if key == keyboard.Key.right:
        try:
            Skip = pag.locateCenterOnScreen("Skip.png", grayscale= False, confidence=0.9)
            x,y = Skip
            if pag.position() != Skip:
                pag.moveTo(x,y,0)
                pag.leftClick()
            else:
                pag.leftClick()
        except:
            None

    #Reverse (if applicable)
    if key == keyboard.Key.left:
        try:
            Back = pag.locateCenterOnScreen("Back.png", grayscale= False, confidence=0.9)
            x,y = Back
            if pag.position() != Back:
                pag.moveTo(x,y,0)
                pag.doubleClick()
            else:
                pag.doubleClick()
        except:
            None

    #Pause
    if key == keyboard.Key.up:
        try:
            Pause = pag.locateCenterOnScreen("Pause.png", grayscale= False, confidence=0.9)
            x,y = Pause
            if pag.position() != Pause:
                pag.moveTo(x,y,0)
                pag.doubleClick()
            else:
                pag.doubleClick()
        except:
            Play = pag.locateCenterOnScreen("playbutton.png", grayscale= False, confidence=0.9)
            x,y = Play
            if pag.position() != Play:
                pag.moveTo(x,y,0)
                pag.doubleClick()
            else:
                pag.doubleClick()
    #Exit the program
    if key == keyboard.Key.esc:
       exit()

#Make sure program is listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()





