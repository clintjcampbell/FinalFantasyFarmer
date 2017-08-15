import win32gui
import win32
import win32ui 
import win32con
from PIL import ImageGrab, Image
import time
import math
import ctypes
from ctypes import windll, Structure, c_long, byref

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
titles = []
gameWindows = []
i = 0
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

class get_wnd_rect(ctypes.Structure):
    _fields_ = [('L', ctypes.c_int),
                ('T', ctypes.c_int),
                ('R', ctypes.c_int),
                ('B', ctypes.c_int)]

#def enumCallback(hwnd, args):
#             if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
#      _, found_pid = win32process.GetWindowThreadProcessId (hwnd)
#      if found_pid == pid:
#        hwnds.append (hwnd)
#    return True
    
#  hwnds = []
#  win32gui.EnumWindows (callback, hwnds)
#  return hwnds

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def getScreenshot(windowname, bboxIn):
    x, y, w, h = callback(".*Blue*.")
    image = ImageGrab.grab(bbox=bboxIn)
    return image

def getWindowPos(hwnd):
   # win_rect = ctypes.wintypes.RECT()
    rect = ctypes.windll.user32.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    bbox = (x,y,x+w, y+h)
    print ("Window %s:" % win32gui.GetWindowText(hwnd))
    print ("\tLocation: (%d, %d)" % (x, y))
    print ("\t    Size: (%d, %d)" % (w, h))
    return x, y, w, h

#def foreach_window(hwnd, lParam):
#    if IsWindowVisible(hwnd):       
#        length = GetWindowTextLength(hwnd)
#        buff = ctypes.create_unicode_buffer(length + 1)
#        GetWindowText(hwnd, buff, length + 1)
#        titles.append((hwnd, buff.value))
#        if 'BlueStacks' in buff.value:
#            ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
#            h = rect.B - rect.T
#            w = rect.R - rect.L
#           # x, y, w, h = getWindowPos(hwnd)
#            ctypes.windll.user32.MoveWindow(hwnd, i*w, 0, w, z, True)
#    return True

win32gui.EnumWindows(enumCallback,'BlueStack')

for i in range(len(titles)):
    if 'BlueStacks' in titles[i][1]:
        gameWindows.append((titles[1][0],titles[i][1]))
win32gui.SetActiveWindow(gameWindows[0][0])
#x, y, w, h, = getWindowPos(gameWindows[0][0])
ctypes.windll.user32.MoveWindow(gameWindows[0][0], 0, 0, 760, 500, True)
ctypes.windll.user32.MoveWindow((gameWindows)[1][0], 0, 0, 760, 500, True)
ctypes.windll.user32.MoveWindow((gameWindows)[2][0], 0, 0, 760, 500, True)

#get image at different locations for check of screen state
#figure out how to sroll through farm spots and upgrade
#go through recommended builds til next citidel, then loop through all farms
#set up request to other farms for supplies
#autosend to specified players or requests when threshold reached
#https://stackoverflow.com/questions/7142342/get-window-position-size-with-python

#get specified window

#def main():
#    win32gui.EnumWindows(callback, None)

#if __name__ == '__main__':
#    main()



#Mouseclicks

#import win32api
#import time
#import math

#for i in range(500):
#    x = int(500+math.sin(math.pi*i/100)*500)
#    y = int(500+math.cos(i)*100)
#    win32api.SetCursorPos((x,y))
#    time.sleep(.01)

#import ctypes

## see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
#ctypes.windll.user32.SetCursorPos(100, 20)
#ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
#ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

#win32gui.GetCursorPos(point)
#This retrieves the cursor's position, in screen coordinates - point = (x,y)

#flags, hcursor, (x,y) = win32gui.GetCursorInfo()
#Retrieves information about the global cursor.






def main():


    bbox = win32gui.EnumWindows(callback, None)    
    pos = queryMousePosition()
    print(pos)

if __name__ == '__main__':
    main()