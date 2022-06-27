from colorama import Fore
import keyboard 
import pyautogui
import time

msg = input(Fore.GREEN +"Enter the message: ")
n = input(Fore.GREEN +"How many times ?: ")


print(Fore.GREEN + "Starting In : ")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print(Fore.BLUE +"shr!ke ")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')
	if keyboard.is_pressed('q'):  
            print('shrike papa')
            break  
    
