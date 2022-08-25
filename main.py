import pyautogui, time, utils

print("STARTING FARM IN 5 SECONDS")
time.sleep(1)
print("STARTING FARM IN 4 SECONDS")
time.sleep(1)
print("STARTING FARM IN 3 SECONDS")
time.sleep(1)
print("STARTING FARM IN 2 SECONDS")
time.sleep(1)
print("STARTING FARM IN 1 SECONDS")
time.sleep(1)
print("STARTING FARM")

while True:
    utils.check_if_in_clubpenguin()

    x, y = pyautogui.locateCenterOnScreen("./images/puffle_action.png")
    pyautogui.moveTo(x, y)
    pyautogui.leftClick()
    try:
        treasure_x, treasure_y = pyautogui.locateCenterOnScreen("./images/puffle_treasure.png")
    except TypeError:
        treasure_x, treasure_y = None, None

    if treasure_x is not None and treasure_y is not None:
        pyautogui.moveTo(treasure_x, treasure_y)
        pyautogui.leftClick()
    else:
        pyautogui.moveTo(x + 200, y + 200)

    x, y = utils.get_point_of_mine()
    pyautogui.moveTo(x, y)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.press("d")

    time.sleep(5)
