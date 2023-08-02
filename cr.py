import pyautogui as pg
import keyboard, sys, time, random

#card    1    2     3    4, change to your positions !!!
cards = [860, 958, 1051, 1149]
cardY = 896

while True:
	if keyboard.is_pressed('s'):
		#start
		while True:
			if keyboard.is_pressed('q'):
				sys.exit()
			else:
				#choose cards
				time.sleep(0.9)
				pg.click(random.choice(cards), cardY)
				#send cards
				time.sleep(0.1)
				#change to your positions !!!
				pg.click(random.randint(725, 1141), random.randint(512, 774))
				#repeat
		
