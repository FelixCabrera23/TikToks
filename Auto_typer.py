import pyautogui
import time
import keyboard

def auto_typing(text, delay =0.1):
    # This is the Auto typing function
       
    for char in text:
        # This is for stoping the program for any reason
        
        if keyboard.is_pressed('esc'):
            print('Autotype stoped')
            break
        if char == '~' :
            # This is so when writing in IDE the code can look good
            pyautogui.press('backspace')
        else:
            pyautogui.write(char)
            time.sleep(delay)
            
# To run program form terminal
if __name__ == "__main__" :
    print ("Auto tpying begining in 5 seconds ...")
    time.sleep(5)
    # This opens our file
    with open('to_write.txt') as text:
        for line in text:
            auto_typing(line,delay=0.05)