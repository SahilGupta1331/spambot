from pyautogui import typewrite, press
import pyttsx3
import time

msg = input("Enter the Message: ")
n = input("How Many Times? ")

print("Open the app and click on the text box")

for i in range(5):
	time.sleep(1)

print("FIRREEE!!!")

for i in range(int(n)):
    typewrite(msg)
    press("ENTER")
    press("ENTER")
    time.sleep(0.1)
