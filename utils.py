from win32con import IDC_APPSTARTING, IDC_ARROW, IDC_CROSS, IDC_HAND, \
IDC_HELP, IDC_IBEAM, IDC_ICON, IDC_NO, IDC_SIZE, IDC_SIZEALL, \
IDC_SIZENESW, IDC_SIZENS, IDC_SIZENWSE, IDC_SIZEWE, IDC_UPARROW, IDC_WAIT
import pyautogui, sys, random, time
from win32gui import LoadCursor, GetCursorInfo

def get_current_cursor():
    curr_cursor_handle = GetCursorInfo()[1]
    return Cursor.from_handle(curr_cursor_handle)

class Cursor(object):
    @classmethod
    def from_handle(cls, handle):
        for cursor in DEFAULT_CURSORS:
            if cursor[1].handle == handle:
                return cursor[0] #DEFAULT_CURSORS.index(cursor) , Cursor.__init__
        return cls(handle=handle)

    def __init__(self, cursor_type=None, handle=None):
        if handle is None:
            handle = LoadCursor(0, cursor_type)
        self.type = cursor_type
        self.handle = handle

DEFAULT_CURSORS = (('APPSTARTING',Cursor(IDC_APPSTARTING)), ('ARROW',Cursor(IDC_ARROW)), ('CROSS',Cursor(IDC_CROSS)), ('HAND',Cursor(IDC_HAND)), \
       ('HELP',Cursor(IDC_HELP)), ('IBEAM',Cursor(IDC_IBEAM)), ('ICON',Cursor(IDC_ICON)), ('NO',Cursor(IDC_NO)), ('SIZE',Cursor(IDC_SIZE)),\
       ('SIZEALL', Cursor(IDC_SIZEALL)),('SIZENESW', Cursor(IDC_SIZENESW)), ('SIZENS',Cursor(IDC_SIZENS)), ('SIZENWSE',Cursor(IDC_SIZENWSE)),\
        ('SIZEWE', Cursor(IDC_SIZEWE)), ('UPARROW', Cursor(IDC_UPARROW)), ('WAIT',Cursor(IDC_WAIT)))

def check_if_in_clubpenguin():
    try:
        x, y = pyautogui.locateCenterOnScreen("./images/penguin_action.png")
    except TypeError:
        try:
            x, y = pyautogui.locateCenterOnScreen("./images/penguin_action2.png")
        except TypeError:
            print("PENGUIN ACTION NOT ON SCREEN, ENDING FARM IN 5 SECONDS")
            time.sleep(5)
            sys.exit()
    try:
        x, y = pyautogui.locateCenterOnScreen("./images/puffle_action.png")
    except TypeError:
        print("PUFFLE ACTION NOT ON SCREEN, ENDING FARM IN 5 SECONDS")
        time.sleep(5)
        sys.exit()
    try:
        x, y = pyautogui.locateCenterOnScreen("./images/mine_point.png")
    except TypeError:
        print("MINE POINT NOT ON SCREEN, ENDING FARM IN 5 SECONDS")
        time.sleep(5)
        sys.exit() 

def get_point_of_mine():
    x, y = pyautogui.locateCenterOnScreen("./images/mine_point.png")
    min_x, min_y = x - 200, y + 200
    max_x, max_y = min_x + 150, min_y + 150
    point_x, point_y = random.randint(min_x, max_x), random.randint(min_y, max_y)
    pyautogui.moveTo(point_x, point_y)
    while get_current_cursor() != "ARROW":
        point_x, point_y = random.randint(min_x, max_x), random.randint(min_y, max_y)
        pyautogui.moveTo(point_x, point_y)
    return point_x, point_y