import pyautogui
speed= -100
sleepTime= 1
pyautogui.time.sleep(3)
i = 0;
while 0<100:
	pyautogui.scroll(speed)
	pyautogui.time.sleep(sleepTime)
	i+=1
	if i==20:
		exit()
