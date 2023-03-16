import subprocess
import time
import cv2
import mss
import pyautogui as ag

sct = mss.mss()
monitor = sct.monitors[0]

game_path = "C:\\xampp\\htdocs\\mu-login-bot\\mu\\"

open_game_img = 'openGameTPL.png'
check_open_game_img = 'checkOpenGame.png'
threshold = 0.9

login = 'testelogin'
password = 'testesenha'

# funcao que tira print da tela
def screenshot(monitor, target):
    with sct:
        screenshot = sct.grab(monitor)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output = target)

# funcao que verifica se o game esta rodando
def check_open_game(target, template):
    target = cv2.imread(target)
    template = cv2.imread(template)
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    # print(str(max_val) + " - " + str(max_loc))
    if max_val < threshold:
        print("O jogo está fechado...")
        # abre o game e inicia processo de login
        subprocess.call('main.exe')   # da b.o ao abrir o game
        time.sleep(2)
        ag.click(1252, 773) # start game
        time.sleep(40)
        ag.click(925, 550) # select world
        time.sleep(1)
    else:
        print("O jogo está aberto")



# main loop
while True:
    time.sleep(1)

    # take ss
    screenshot(monitor, check_open_game_img)

    # check game state
    check_open_game(check_open_game_img, open_game_img)

    print(ag.position())


# screen_width, screen_height = ag.size() #1920x1080

# def typeLogin():
#     ag.write(user, .5)

# def typePassword():
#     ag.write(password, .5)



# print(ag.position())

'''
position() # get mouse position
moveTo(x, y) # move mouse
click(x, y) # move mouse and click
doubleClick() # double click the mouse
write(string, interval) # type text with interval between each letter
press(string) # string = key name described in pyautogui.KEY_NAMES
hold(string) # hold a key
with hold(string)
    press([string, string])
hotkey(string, string)
alert(string) # display an alert box
'''