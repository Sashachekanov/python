import pyautogui
import time

pyautogui.FAILSAFE = False
df = input("Во сколько приём у врача?,")
dh = input("Когда?")
pyautogui.hotkey("winleft","d")
pyautogui.moveTo(800,300)
pyautogui.doubleClick()
time.sleep(2)
pyautogui.write(df)
pyautogui.write(dh)
