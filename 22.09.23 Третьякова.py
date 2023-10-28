import pyautogui
import time

pyautogui.FAILSAFE = False
df = int(input("Какую програму открыть?"))
pyautogui.hotkey("winleft","d")
pyautogui.moveTo(800,300)
pyautogui.doubleClick()
time.sleep(2)

if df == 1:
    
    pyautogui.write('hfpevty kb z?')
    pyautogui.press("enter")
elif df == 2:
    pyautogui.write('Ckfdf hj,jnfv!,')
    pyautogui.press("enter")
#elif df == 3:
    #pyautogui.moveTo(1000,300)
    #pyautogui.doubleClick()
#print("Спасибо за использование!")
