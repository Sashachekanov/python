import pyautogui
import time
processingx = 55
processingy = 532
microsoftx = 62
microsofty = 279
chromx = 58
chromy = 408

i = input('Какой файл открыть 1-processing, 2-microsoft, или 3-chrome?')
if i  == '1':
    print(pyautogui.click(1760, 0))
    time.sleep(1)
    print(pyautogui.doubleClick(processingx, processingy))
    time.sleep(1)
    
elif i == '2':
    print(pyautogui.click(1760, 0))
    time.sleep(1)
    print(pyautogui.doubleClick(microsoftx, microsofty))
    time.sleep(1)
    
    
else:
    print(pyautogui.click(1760, 0))
    time.sleep(1)
    print(pyautogui.doubleClick(chromx, chromy))
    time.sleep(1)
    
