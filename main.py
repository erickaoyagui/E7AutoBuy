# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

from pyautogui import *
import pyautogui
import time
import keyboard

time_to_sleep = 0.6
refresh_button_command = '1'
confirm_refresh_button_command = '2'
confirm_buy_button_command = '4'
scroll_shop_command = '3'
button_x = 1686
friendship_counter = 0
covenant_counter = 0
mystic_counter = 0
skystones_counter = 0

def locate_image(image, button):
    try:
        image_x, image_y = pyautogui.locateCenterOnScreen(image, confidence = 0.93)
        #button_x, button_y = pyautogui.locateCenterOnScreen(button, confidence = 0.90)
        pyautogui.click(x = button_x, y = image_y + 20)
        time.sleep(time_to_sleep)
        pyautogui.press(confirm_buy_button_command)
        time.sleep(time_to_sleep)
        return True
    except Exception as e:
        return False

def locate_and_click_friendship_bookmarks():
    if(locate_image('friendship_bookmarks.png', 'friendship_bookmarks_button.png')):
        global friendship_counter
        friendship_counter += 1


def locate_and_click_covenant_bookmarks():
    if(locate_image('covenant_bookmarks.png', 'covenant_bookmarks_button.png')):
        global covenant_counter
        covenant_counter += 1

def locate_and_click_mystic_bookmarks():
    if(locate_image('mystic_bookmarks.png', 'mystic_bookmarks_button.png')):
        global mystic_counter
        mystic_counter += 1

def locate_and_click_all():
    locate_and_click_mystic_bookmarks()
    locate_and_click_covenant_bookmarks()
    #locate_and_click_friendship_bookmarks()

def refresh_shop():
    pyautogui.press(refresh_button_command)
    time.sleep(time_to_sleep)
    pyautogui.press(confirm_refresh_button_command)
    time.sleep(time_to_sleep)
    global skystones_counter
    skystones_counter += 3

def scroll_shop():
    pyautogui.press(scroll_shop_command)
    time.sleep(time_to_sleep)

def print_all():
    print("Mystic: ", mystic_counter)
    print("Covenant: ", covenant_counter)
    print("Skystones: ", skystones_counter)
    #print("Friendship: ", friendship_counter)

while keyboard.is_pressed('q') == False:
    time.sleep(time_to_sleep)
    try:
        locate_and_click_all()
        time.sleep(time_to_sleep)
        scroll_shop()
        locate_and_click_all()
        time.sleep(time_to_sleep)
        refresh_shop()
        print_all()

    except Exception as e:
        print("Erro:", e)
        #pyautogui.press('2')12

