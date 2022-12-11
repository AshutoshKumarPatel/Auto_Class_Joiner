import pyautogui, time
import cv2
import calendar
from datetime import date

Teams_selected = cv2.imread(r'Assets\Teams-icon-selected.png')
Teams_notselected = cv2.imread(r'Assets\Teams-icon-not-selected.png')

DAA = cv2.imread(r'Assets\DAA-class.png')
DBMS = cv2.imread(r'Assets\DBMS-class.png')
DBMS_Unread = cv2.imread(r'Assets\DBMS-class-unread.png')

Meeting_Started = cv2.imread(r'Assets\Meeting-Started.png')
Join_Button = cv2.imread(r'Assets\Join-button.png')
Mic_On = cv2.imread(r'Assets\Mic-on.png')
Mic_Off = cv2.imread(r'Assets\Mic-off.png')
Join_Now = cv2.imread(r'Assets\Join-now.png')
Class_Name = cv2.imread(r'Assets\Class-Name.png')

Days_3 = ['Monday', 'Wednesday', 'Friday', 'Sunday']
Meeting_Not_Found = True

today_date = date.today()
day_name = calendar.day_name[today_date.weekday()]

def setup():
    if (pyautogui.locateOnScreen(Teams_selected, region=(0, 0, 500, 800))):
        cord = pyautogui.locateCenterOnScreen(Teams_selected, region=(0, 0, 500, 800))
        pyautogui.click(cord)
        pyautogui.click(cord)
    else:
        pyautogui.locateOnScreen(Teams_notselected, region=(0, 0, 500, 800))
        cord = pyautogui.locateCenterOnScreen(Teams_notselected, confidence=0.8)
        pyautogui.click(cord)
        pyautogui.click(cord)

    time.sleep(5)

    if day_name in Days_3:
        if (pyautogui.locateOnScreen(DBMS, confidence=0.8)):
            cord = pyautogui.locateCenterOnScreen(DBMS, confidence=0.8)
            pyautogui.click(cord)
        else:
            if (pyautogui.locateOnScreen(DBMS_Unread, confidence=0.8)):
                cord = pyautogui.locateCenterOnScreen(DBMS_Unread, confidence=0.8)
                pyautogui.click(cord)
    else:
        pyautogui.locateOnScreen(DAA, confidence=0.8)
        cord = pyautogui.locateCenterOnScreen(DAA, confidence=0.8)
        pyautogui.click(cord)

    time.sleep(5)

def check():
    global Meeting_Not_Found   
    while (Meeting_Not_Found):
        if (pyautogui.locateOnScreen(Meeting_Started, confidence=0.7, region = (450, 150, 1290, 690))):
            cord = pyautogui.locateCenterOnScreen(Join_Button, confidence=0.8, region = (450, 150, 1290, 690))
            pyautogui.click(cord)
            time.sleep(2)
            pyautogui.hotkey('win', 'up')
            Meeting_Not_Found = False
            time.sleep(5)
        else:
            time.sleep(5)
            setup()

def checkformic():
    if (pyautogui.locateOnScreen(Mic_On, confidence = 0.7)):
        cord = pyautogui.locateCenterOnScreen(Mic_On, confidence = 0.7)
        pyautogui.click(cord)
        time.sleep(5)

    if (pyautogui.locateOnScreen(Mic_Off, confidence = 0.7)):
        cord = pyautogui.locateCenterOnScreen(Join_Now, confidence = 0.7)
        pyautogui.click(cord)

if __name__ == '__main__':
    setup()
    check()
    checkformic()