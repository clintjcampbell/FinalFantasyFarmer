import win32gui
import win32api
import win32con
import time
import cv2
import numpy as np
from PIL import Image
import pyscreenshot as ImageGrab
guildHelpTemp = cv2.imread('C:\local\FinalFantasyFarmer\GuildHelpTemplate.JPG')
BuildTemp = cv2.imread('C:\local\FinalFantasyFarmer\BuildTemplate.JPG')
ResearchTemp = cv2.imread('C:\local\FinalFantasyFarmer\ResearchTemplate.JPG')
TrainTemp = cv2.imread('C:\local\FinalFantasyFarmer\TrainTemplate.JPG')
TrapsTemp = cv2.imread('C:\local\FinalFantasyFarmer\TrapsTemplate.JPG')
EmpireTemp = cv2.imread('C:\local\FinalFantasyFarmer\EmpireTemplate.JPG')
MapTemp = cv2.imread('C:\local\FinalFantasyFarmer\MapTemplate.JPG')
HeroTemp = cv2.imread('C:\local\FinalFantasyFarmer\HeroTemplate.JPG')
LockedBuildTemp = cv2.imread('C:\local\FinalFantasyFarmer\LockBuildTemplate.JPG')
FreeTemp = cv2.imread('C:\local\FinalFantasyFarmer\FreeTemplate.JPG')
SpeedupTemp = cv2.imread('C:\local\FinalFantasyFarmer\Speedup2Template.JPG')
CollectGoldTemp = cv2.imread('C:\local\FinalFantasyFarmer\CollectGoldTemplate.JPG')
DepositGoldTemp = cv2.imread('C:\local\FinalFantasyFarmer\DepositeGoldTemplate.JPG')
WithdrawGoldTemp = cv2.imread('C:\local\FinalFantasyFarmer\WithdrawGoldTemplate.JPG')
def clickPoint(x,y):
    x0, y0 = win32api.GetCursorPos()
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)
    time.sleep(.01)
    win32api.SetCursorPos((x0,y0))
def clickDrag(x,y, a, b):
    x0, y0 = win32api.GetCursorPos()
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    time.sleep(.1)
    win32api.SetCursorPos((a,b))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,a,b)
    time.sleep(.01)
    win32api.SetCursorPos((x0,y0))
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
def checkTemplate(bboxIn,template, threshold):
    im=ImageGrab.grab(bbox=bboxIn) # X1,Y1,X2,Y2
    im_np =   np.array(im.getdata(),np.uint8).reshape(im.size[1], im.size[0], 3)
    im_np = im_np[...,[2,1,0]]
    im_np = cv2.cvtColor(im_np, cv2.COLOR_BGR2GRAY)
    templategray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(im_np,templategray,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #while (True):
    #    cv2.imshow('window',im_np)
    #    cv2.imshow('window2',template)
    #    if cv2.waitKey(25) & 0xFF == ord('q'):
    #        cv2.destroyAllWindows()
    #        break
    if (max_val > threshold):
        return True, max_loc, max_val
    else:
        return False, max_loc, max_val
def CheckEmpireScreen():
    isEmpire, loc, max = checkTemplate((0,779,95,862),EmpireTemp, .9)
    if isEmpire:
        clickPoint(43,812)
        
        #check for citidel upgrade screen, hero up screen, etc. Lock, gotostore, etc.
    
    return isEmpire
def CheckCanBuild():
    CheckEmpireScreen()
    canBuild, loc , max= checkTemplate((54,136,111,272),BuildTemp, .5)
    isLocked, loc2, maxlock = checkTemplate((54,136,111,272),LockedBuildTemp,.6)
    if canBuild and  not isLocked:
        #x = 54+loc[0]+10
        #y = 136+loc[1]+5
        clickPoint(84,160) #click hammer
        clickPoint(84,210) #click hammer
        #clickPoint(84,250) #click hammer
        time.sleep(1)  
        clickPoint(324,262) #click build/upgrade
        time.sleep(1)
        clickPoint(309,258)#click upgrade
        clickPoint(242,262)#click upgrade
        time.sleep(1)
        clickPoint(291,159)#click help
        time.sleep(.2)

    return canBuild
def CheckFreeBuild():
    CheckEmpireScreen()
    canBuild, loc , max= checkTemplate((234,134,355,255),FreeTemp, .9)
    canSpeedup, loc2, max2 = checkTemplate((234,134,355,255),SpeedupTemp, .9)
    if canBuild and max > max2 :
        x = 234+loc[0]+10
        y = 134+loc[1]+5
        clickPoint(x,y) #click Free
def checkHelpChances():
    CheckEmpireScreen()
    NeedHelp, loc , max= checkTemplate((390,635,466,720),guildHelpTemp, .8)
    if NeedHelp:
        clickPoint(435,681)
        time.sleep(.8)
        clickPoint(435,681)
        time.sleep(1)
        clickPoint(52,821)#exit to main screen
        time.sleep(.4)
def checkSecretGift():
    clickPoint(114,646)
    time.sleep(1)
    clickPoint(234,537)
    clickPoint(234,507)
def checkforGold():
    clickPoint(418, 818)#click more button
    time.sleep(.5)
    #clickDrag(430,713,430,306)
    #time.sleep(1.5)
    
    clickPoint(62, 619)
    time.sleep(2)
    collectGold, locC , maxC= checkTemplate((0,640,466,740),CollectGoldTemp, .9)
    depositGold, locD , maxD= checkTemplate((0,640,466,740),DepositGoldTemp, .9)
    #withdrawGold, locW , maxW= checkTemplate((0,640,466,740),WithdrawGoldTemp, .9)
    
    if collectGold:
        clickPoint(269,687)
        time.sleep(.8)
        depositGold = True
    if depositGold:
        clickPoint(278,691)
        time.sleep(.8)
    clickPoint(43,812)
    CheckEmpireScreen()
    
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    while True:
        for j in range(20):
            for i in top_windows:
                if 'BlueStacks' in i[1]:
                    print( i)
                    #win32gui.ShowWindow(i[0],5)
                    win32gui.SetForegroundWindow(i[0])
                    win32gui.MoveWindow(i[0],0,0, 350,900, True)
                    CheckEmpireScreen()
                    #do the list of things to check and do while on this screent
                    #check for help chances
                    checkHelpChances()
                    #check for quests
                    #check for building
                    CheckCanBuild()
                    CheckFreeBuild()
                    #check for research
                    #
                    #check for secret gifts
                    if j == 0:
                       checkSecretGift()
                       checkforGold()
        

           