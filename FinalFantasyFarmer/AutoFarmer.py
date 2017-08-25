import win32gui
import win32api
import win32con
import time
import cv2
import numpy as np
from PIL import Image
import pyscreenshot as ImageGrab
import os
import pyautogui









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
ConfirmTemp = cv2.imread('C:\local\FinalFantasyFarmer\ConfirmTemplate.JPG')
DepositGoldTemp = cv2.imread('C:\local\FinalFantasyFarmer\DepositeGoldTemplate.JPG')
WithdrawGoldTemp = cv2.imread('C:\local\FinalFantasyFarmer\WithdrawGoldTemplate.JPG')
CollectTemp = cv2.imread('C:\local\FinalFantasyFarmer\CollectTemplate.JPG')
CollectTemp2 = cv2.imread('C:\local\FinalFantasyFarmer\CollectTemplate2.JPG')
upgradeableTemp = cv2.imread('C:\local\FinalFantasyFarmer\Canupgrade.JPG')
upgradeableTemp2 = cv2.imread('C:\local\FinalFantasyFarmer\Canupgrade2.JPG')
OKTemp = cv2.imread('C:\local\FinalFantasyFarmer\OkTemplate.JPG')
MoreTemp = cv2.imread('C:\local\FinalFantasyFarmer\MoreTemplate.JPG')
TreasuryTemp = cv2.imread('C:\local\FinalFantasyFarmer\TreasuryTemplate.JPG')
QuestCollectTemp = cv2.imread('C:\local\FinalFantasyFarmer\QuestCollectTemplate.JPG')
QuestWaitTemp = cv2.imread('C:\local\FinalFantasyFarmer\QuestWaitingTemplate.JPG')
StartQuestTemp = cv2.imread('C:\local\FinalFantasyFarmer\StartQuestTemplate.JPG')
ClintronTemp = cv2.imread('C:\local\FinalFantasyFarmer\ClintronTemplate.JPG')
HomeTemp = cv2.imread('C:\local\FinalFantasyFarmer\HomeScreenTemplate.JPG')
x1Temp= cv2.imread('C:\local\FinalFantasyFarmer\exit1Temp.JPG')
x2Temp = cv2.imread('C:\local\FinalFantasyFarmer\exit2Temp.JPG')
x3Temp = cv2.imread('C:\local\FinalFantasyFarmer\exit3Temp.JPG')
okTemp = cv2.imread('C:\local\FinalFantasyFarmer\okTemplate.JPG')
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
    im = ImageGrab.grab(bbox=bboxIn) # X1,Y1,X2,Y2
    im_np = np.array(im.getdata(),np.uint8).reshape(im.size[1], im.size[0], 3)
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
        
        #check for citidel upgrade screen, hero up screen, etc.  Lock,
        #gotostore, etc.
    
    return isEmpire
def CheckCanBuild():
    CheckEmpireScreen()
    canBuild, loc , max = checkTemplate((54,136,111,272),BuildTemp, .6)
    isLocked, loc2, maxlock = checkTemplate((54,136,111,272),LockedBuildTemp,.6)
    if canBuild and not isLocked:
        #x = 54+loc[0]+10
        #y = 136+loc[1]+5
        clickPoint(84,160) #click hammer
        clickPoint(84,205) #click hammer
        #clickPoint(84,250) #click hammer
        time.sleep(.7)  
        clickPoint(324,262) #click build/upgrade
        time.sleep(.7)
        clickPoint(309,258)#click upgrade
        clickPoint(242,262)#click upgrade
        time.sleep(.7)
        clickPoint(291,159)#click help
        time.sleep(.1)
        CheckFreeBuild()
    return canBuild
def CheckCanBuild2():
    CheckEmpireScreen()
    canBuild, loc , max = checkTemplate((50,215,450,720),upgradeableTemp, .6)
    canBuild2, loc2 , max = checkTemplate((50,215,450,720),upgradeableTemp2, .6)
    #isLocked, loc2, maxlock = checkTemplate((54,136,111,272),LockedBuildTemp,.6)
    if canBuild :
        x = 50 + loc[0] - 15
        y = 215 + loc[1]
        clickPoint(x,y)
        time.sleep(.7)  
        clickPoint(324,262) #click build/upgrade
        time.sleep(.7)
        clickPoint(309,258)#click upgrade
        clickPoint(242,262)#click upgrade
        time.sleep(.9)
        clickPoint(291,159)#click help
        time.sleep(.1)
        CheckFreeBuild()
    if canBuild2 :
        x = 50 + loc2[0] - 15
        y = 215 + loc2[1]
        clickPoint(x,y)
        time.sleep(.7)  
        clickPoint(324,262) #click build/upgrade
        time.sleep(.7)
        clickPoint(309,258)#click upgrade
        clickPoint(242,262)#click upgrade
        time.sleep(.9)
        clickPoint(291,159)#click help
        time.sleep(.1)
        CheckFreeBuild()
    
    return canBuild
def CheckFreeBuild():
    CheckEmpireScreen()
    free, loc , max = checkTemplate((234,134,355,255),FreeTemp, .8)
    canSpeedup, loc2, max2 = checkTemplate((234,134,355,255),SpeedupTemp, .9)
    if free and max > max2 :
        x = 234 + loc[0] + 10
        y = 134 + loc[1] + 5
        clickPoint(x,y) #click Free
def checkHelpChances():
    CheckEmpireScreen()
    NeedHelp, loc , max = checkTemplate((390,635,466,720),guildHelpTemp, .8)
    if NeedHelp:
        clickPoint(435,681)
        time.sleep(.7)
        clickPoint(435,681)
        time.sleep(.7)
        clickPoint(52,821)#exit to main screen
        time.sleep(.8)
def checkSecretGift():
    CheckEmpireScreen()
    clickPoint(114,646)
    time.sleep(.5)
    collect, loc , max = checkTemplate((135,509,334,567),CollectTemp2, .75)
    ok, loc2 , max = checkTemplate((128,469,357,528),OKTemp, .75)
    if collect:
        clickPoint(231,537)
        time.sleep(1.3)
        return
    if ok:
        clickPoint(234,496)
def checkQuests():
    clickPoint(124,818) #click quests tab
    time.sleep(1)
    clickPoint(269,619) #click guild quests
    time.sleep(1)
    clickQuests()
    clickPoint(124,818) #click quests tab
    time.sleep(1)
    clickPoint(269,546) #click Hero quests
    time.sleep(1)
    clickQuests()
def clickQuests():
    collect, locC , maxC = checkTemplate((240,123,466,340),QuestCollectTemp, .6)
    wait, locD , maxD = checkTemplate((240,123,466,340),QuestWaitTemp, .8)
    if wait:
        return
    if collect:
        clickPoint(374,196)
        time.sleep(1)
    start, locC , maxC = checkTemplate((240,123,466,340),StartQuestTemp, .7)
    if start:
        clickPoint(374,196)
        time.sleep(1)
    
    time.sleep(1)
def checkforGold():
    More, loc , max = checkTemplate((356,757,461,870),MoreTemp, .8)
    if More:
        clickPoint(418, 818)#click more button
        time.sleep(.5)
        
        #clickDrag(430,713,430,306)
        x0, y0 = win32api.GetCursorPos()
        pyautogui.moveTo(430, 309, duration = 0.1)
        
        pyautogui.dragTo(430,150, duration = .2)
        win32api.SetCursorPos((x0,y0))
        time.sleep(.5)
        #time.sleep(1.5)
        Treasury, loc , max = checkTemplate((23,200,450,750),TreasuryTemp, .8)
        if Treasury:
            clickPoint(loc[0] + 23, loc[1] + 200)
            time.sleep(1)
            collectGold, locC , maxC = checkTemplate((0,640,466,740),CollectGoldTemp, .8)
            depositGold, locD , maxD = checkTemplate((0,640,466,740),DepositGoldTemp, .8)
        #withdrawGold, locW , maxW= checkTemplate((0,640,466,740),WithdrawGoldTemp,
        #.9)
    
            if collectGold:
                clickPoint(269,687)
                time.sleep(1.7)
                depositGold = True
            if depositGold:
                clickPoint(278,691)
                time.sleep(.8)
        else:
            clickDrag(340,620,340,299)
        clickPoint(43,812)
    CheckEmpireScreen()
def sendResources():
    clickPoint(266,819)
    time.sleep(1)
    clickPoint(238,574)
    time.sleep(1)
    for i in range(3):
        Clintron, locD , maxD = checkTemplate((15,89,235,729),ClintronTemp, .9)
        if Clintron:
            clickPoint(408,locD[1]+89)
            time.sleep(1.2)
            clickPoint(325,186)
            time.sleep(.3)
            clickPoint(325,273)
            time.sleep(.3)
            clickPoint(325,360)
            time.sleep(.3)
            clickPoint(325,448)
            time.sleep(.3)
            clickPoint(325,535)
            time.sleep(.3)
            clickPoint(243,679)
            time.sleep(.3)
            clickPoint(324,360)
            time.sleep(1)
            clickPoint(52,821)#exit to main screen
            time.sleep(.4)
        else: 
            x0, y0 = win32api.GetCursorPos()
            pyautogui.moveTo(430, 309, duration = 0.1)
            pyautogui.dragTo(430,150, duration = .2)
            win32api.SetCursorPos((x0,y0))
            time.sleep(.7)
def checkRestartEngineNeeded(hwnd):
    atHome, locD , maxD = checkTemplate((30,74,193,211),HomeTemp, .8)
    if atHome:
        clickPoint(689,21)
        time.sleep(.3)
        clickPoint(719,150)
        time.sleep(.3)
        clickPoint(497,319)
        time.sleep(30)
        win32gui.MoveWindow(i[0],0,0, 350,900, True)
        clickPoint(286,144)
        return
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    while True:
        for j in range(3):
            for i in top_windows:
                if 'BlueStacks' in i[1]:
                    print(i)
                    #win32gui.ShowWindow(i[0],5)
                    win32gui.SetForegroundWindow(i[0])
                    win32gui.MoveWindow(i[0],0,0, 350,900, True)
                    #checkRestartEngineNeeded(i[0])
                    
                    collect, loc, max = checkTemplate((37,541,441,846),CollectTemp,.7)
                    if collect:
                        clickPoint(230, 783)
                    Hero, loc, max = checkTemplate((23,741,288,852),ConfirmTemp,.7)
                    if Hero:
                        clickPoint(128,790)
                    x3, loc, max = checkTemplate((3,35,457,637),x3Temp,.7)
                    if x3:
                        clickPoint(loc[0]+12,loc[1] + 45)
                    x2, loc, max = checkTemplate((3,35,457,637),x2Temp,.7)
                    if x2:
                        clickPoint(loc[0]+12,loc[1] + 45)
                    x1, loc, max = checkTemplate((3,35,457,637),x1Temp,.7)
                    if x1:
                        clickPoint(loc[0]+12,loc[1] + 45)
                    ok, loc, max = checkTemplate((37,179,457,637),OKTemp,.7)
                    if ok:
                        clickPoint(loc[0]+37,loc[1] + 179)
                    #sendResources()
                    CheckEmpireScreen()
                    CheckEmpireScreen()
                    CheckFreeBuild()
                    #do the list of things to check and do while on this
                    #screent
                    #check for help chances
                    checkHelpChances()
                    checkHelpChances()
                    checkforGold()
                    
                   
                    #CheckCanBuild2()  # use this to build up farm area
                    #CheckCanBuild2()  # use this to build up farm area
                    #CheckCanBuild2()  # use this to build up farm area
                    #CheckCanBuild2()  # use this to build up farm area
                    CheckCanBuild2()  # use this to build up farm area
                    CheckCanBuild()  # use this for general level up
                    
                    
                    #check for research
                    #
                    #check for secret gifts
                    
                    checkSecretGift()
                    checkQuests()
                if 'BlueStacks A1' in i[1]:   
                    sendResources()
                if 'BlueStacks A2' in i[1]:   
                    sendResources()
                if 'BlueStacks A3' in i[1]:   
                    sendResources()
                #if 'BlueStacks A4' in i[1]:   
                #    sendResources()
                if 'BlueStacks A6' in i[1]:   
                    CheckCanBuild2()  # use this to build up farm area
                    CheckCanBuild()  # use this for general level up
        

           

#import pyautogui
#pyautogui.moveTo(100, 150)
#pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
#pyautogui.dragTo(100, 150)
#pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down