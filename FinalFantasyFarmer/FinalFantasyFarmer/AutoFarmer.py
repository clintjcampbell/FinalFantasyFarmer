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
CollectTemp = cv2.imread('C:\local\FinalFantasyFarmer\CollectTemplate.JPG')
upgradeableTemp = cv2.imread('C:\local\FinalFantasyFarmer\Canupgrade.JPG')
OKTemp = cv2.imread('C:\local\FinalFantasyFarmer\OkTemplate.JPG')
MoreTemp = cv2.imread('C:\local\FinalFantasyFarmer\MoreTemplate.JPG')
TreasuryTemp = cv2.imread('C:\local\FinalFantasyFarmer\TreasuryTemplate.JPG')
QuestCollectTemp = cv2.imread('C:\local\FinalFantasyFarmer\QuestCollectTemplate.JPG')
QuestWaitTemp = cv2.imread('C:\local\FinalFantasyFarmer\QuestWaitingTemplate.JPG')
StartQuestTemp = cv2.imread('C:\local\FinalFantasyFarmer\StartQuestTemplate.JPG')
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
        clickPoint(84,200) #click hammer
        #clickPoint(84,250) #click hammer
        time.sleep(.7)  
        clickPoint(324,262) #click build/upgrade
        time.sleep(.7)
        clickPoint(309,258)#click upgrade
        clickPoint(242,262)#click upgrade
        time.sleep(.7)
        clickPoint(291,159)#click help
        time.sleep(.1)

    return canBuild
def CheckCanBuild2():
    CheckEmpireScreen()
    canBuild, loc , max = checkTemplate((50,215,500,720),upgradeableTemp, .6)
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
        time.sleep(.7)
        clickPoint(291,159)#click help
        time.sleep(.1)

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
    NeedHelp, loc , max = checkTemplate((390,635,466,720),guildHelpTemp, .9)
    if NeedHelp:
        clickPoint(435,681)
        time.sleep(.7)
        clickPoint(435,681)
        time.sleep(.7)
        clickPoint(52,821)#exit to main screen
        time.sleep(.4)
def checkSecretGift():
    clickPoint(114,646)
    time.sleep(.5)
    collect, loc , max = checkTemplate((135,509,334,567),CollectTemp, .9)
    ok, loc2 , max = checkTemplate((128,469,357,528),OKTemp, .9)
    if collect:
        clickPoint(231,537)
        return
    if ok:
        clickPoint(234,496)
def checkQuests():
    clickPoint(124,818) #click quests tab
    time.sleep(1)
    clickPoint(269,619) #click guild quests
    time.sleep(1)
    clickPoint(124,818) #click quests tab
    time.sleep(1)
    clickQuests()
    clickPoint(269,546) #click Hero quests
    time.sleep(1)
    clickQuests()
def clickQuests():
    collect, locC , maxC = checkTemplate((240,123,466,340),QuestCollectTemp, .7)
    wait, locD , maxD = checkTemplate((240,123,466,340),QuestWaitTemp, .7)
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
    More, loc , max = checkTemplate((356,757,461,870),MoreTemp, .9)
    if More:
        clickPoint(418, 818)#click more button
        time.sleep(.5)
        #clickDrag(430,713,430,306)
        #time.sleep(1.5)
        Treasury, loc , max = checkTemplate((23,571,134,691),TreasuryTemp, .9)
        if Treasury:
            clickPoint(62, 619)
            time.sleep(1)
            collectGold, locC , maxC = checkTemplate((0,640,466,740),CollectGoldTemp, .9)
            depositGold, locD , maxD = checkTemplate((0,640,466,740),DepositGoldTemp, .9)
        #withdrawGold, locW , maxW= checkTemplate((0,640,466,740),WithdrawGoldTemp,
        #.9)
    
            if collectGold:
                clickPoint(269,687)
                time.sleep(.8)
                depositGold = True
            if depositGold:
                clickPoint(278,691)
                time.sleep(.8)
        else:
            clickDrag(340,620,340,299)
    CheckEmpireScreen()
    
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    while True:
        for j in range(5):
            for i in top_windows:
                if 'BlueStacks' in i[1]:
                    print(i)
                    #win32gui.ShowWindow(i[0],5)
                    win32gui.SetForegroundWindow(i[0])
                    win32gui.MoveWindow(i[0],0,0, 350,900, True)
                    collect, loc, max = checkTemplate((43,744,458,852),CollectTemp,.9)
                    if collect:
                        clickPoint(236, 787)
                    CheckEmpireScreen()
                    CheckFreeBuild()
                    #do the list of things to check and do while on this
                    #screent
                    #check for help chances
                    checkHelpChances()
                    
                    #check for building
                    CheckCanBuild()  # use this for general level up
                    #CheckCanBuild2()  # use this to build up farm area
                    CheckEmpireScreen()
                    
                    #check for research
                    #
                    #check for secret gifts
                    if j % 5  == 0:
                       checkSecretGift()
                       checkQuests()
                    if j== 0:
                       checkforGold()
        

           