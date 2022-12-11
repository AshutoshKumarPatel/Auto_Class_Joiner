import pyautogui, time

while True:
    x, y = pyautogui.position()
    string = 'X:' + str(x) + 'Y:' + str(y)
    print(string, end="")
    print('\b'* len(string), end = '')
    time.sleep(1)
