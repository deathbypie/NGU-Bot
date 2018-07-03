import time
import win32api, win32con
from PIL import ImageOps
from numpy import *
import constants
import keystrokes

# ------------------
# Bot to automate parts of NGU IDLE - https://www.kongregate.com/games/somethingggg/ngu-idle#

#All coordinates assume a screen resolution of 1920*1080, and Firefox 
#maximized with the Bookmarks Toolbar enabled.
#Browser scrolled all the way to top left.
#xPad = 319
#yPad = 345
#Play area =  xPad+1, yPad+1, 959, 601


# Globals
# ------------------
 
xPad = 319
yPad = 345

xSize = 959
ySize = 601

box = (xPad + 1,yPad + 1,xPad + xSize,yPad + ySize)

#region Screen Grabs
def screenGrab():
    im = ImageGrab.grab(box)
    ##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def grabColours():
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a

#endregion

#region Clicks
def DoLeftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Left Click.")

def LeftClick(cords = None):
    if cords is not None:
        MousePos(cords)
        time.sleep(0.1)
    DoLeftClick()
    DoLeftClick() # two clicks might help the clicks that don't register. Nothing in NGU Idle responds differently to double click

def DoRightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    print("Left Click.")

def RightClick(cords = None):
    if cords is not None:
        MousePos(cords)
        time.sleep(0.1)
    DoRightClick()
    DoRightClick()
#endregion

#region Positioning
def MousePos(cord):
    win32api.SetCursorPos((xPad + cord[0], yPad + cord[1]))
    time.sleep(0.1)
    #print("Mouse moved")
    
def GetCords():
    x,y = win32api.GetCursorPos()
    x = x - xPad
    y = y - yPad
    print(x,y)
#endregion

#region tasks

###
#
###
def QuickRun(rebirth = 0):
    """
    Quick runs of 15 minutes. Should allow different lengths to test optimal length.
    Assumes rebirth has just started. Does things every 10 seconds for simplicity.
    rebirth number can be specified for a bit of fine tuning"""
    minutes = 15 # times will need adjusting if minutes is changed
    duration = minutes * 60
    startTime = time.time()
    elapsed = 0
    count = 1
    cords = constants.Cords
    time.sleep(5)
    FightBoss(rebirth)
    AdvanceAdventureZone()
    stage = 1

    while elapsed < duration:
        #Spend first 5 minutes just powering up time machine.
        if(elapsed < 5 * 60 and rebirth > 0):
            Navigate(cords.Sidebar.timeMachine)
            AddTimeMachine()
        # Then do some augments and after 5 minutes
        elif(elapsed < 12 * 60 and rebirth > 0):
            Navigate(cords.Sidebar.augments)
            if(stage < 2):
                RecallBoth()
                stage = 2
                SelectQuarterEnergy()
                AddAugment(cords.Augments.buster, True, True) # upgrade of augment

            SelectFullInput()
            AddAugment(cords.Augments.buster, False, True)


            Navigate(constants.Cords.Sidebar.bloodMagic)
            Navigate(cords.Sidebar.bloodMagic)
            # Imperfect gold-wise for now, but good enough to start. Just attempt to cap all.
            for i in range(7):
                AddBloodMagic(i, True, False)
            
        # End with wandoos
        else:
            if(stage < 3):
                RecallBoth()
                stage = 3
            Navigate(cords.Sidebar.wandoos)
            AddWandoos(False)
        if(count % 5 == 0):
            print("Fighting Boss iteration %s" % count)
            FightBoss() # fight boss very ~50 seconds
            AdvanceAdventureZone()

        elapsed = time.time() - startTime
        print('Time elapsed: %s' % elapsed)
        time.sleep(30)
        count += 1

    if(rebirth == 0):
        AddAugment(cords.Augments.shoulder)

    FightBoss()
    return elapsed

def DoRuns(rebirth = 0):
    """
    Do multiple runs. Much more to add. Requires ctrl + C to cancel
    """
    elapsed = 0
    while(True):
        elapsed += QuickRun(rebirth)
        rebirth += 1

        print("Starting rebirth %s" % rebirth)
        print("Total elapsed time: %s" % elapsed)
        Rebirth()

def AddTimeMachine(navigate = True):
    if navigate:
        Navigate(constants.Cords.Sidebar.timeMachine)
    cords = constants.Cords.TimeMachine
    LeftClick((cords.xAdd, cords.energy))
    LeftClick((cords.xAdd, cords.magic))

def AddAugment(augment, upgrade=False, navigate = True):
    # Expects cords from constants.Cords.Augments ie: Augments.scissors as input
    #Assumes augment window already scrolled up
    if navigate:
        Navigate(constants.Cords.Sidebar.augments)
    yCord = augment[0] if not upgrade else augment[1]
    LeftClick((constants.Cords.Augments.xAdd, yCord))

def AddWandoos(type = "normal", navigate = True):
    #type parameter to be added later to change wandoos os if needed
    if navigate:
        Navigate(constants.Cords.Sidebar.wandoos)
    cords = constants.Cords.Wandoos
    
    LeftClick((cords.xAdd, cords.energy))
    LeftClick((cords.xAdd, cords.magic))

def AddBloodMagic(ritual, cap = False,navigate = True):
    if navigate:
        Navigate(constants.Cords.Sidebar.bloodMagic)
    cords = constants.Cords.BloodMagic
    x = cords.xCap if cap else cords.xAdd
    y = cords.yRituals[ritual]
    LeftClick((x,y))

def FightBoss(rebirth = 1):
    Navigate(constants.Cords.Sidebar.fightBoss)
    cords = constants.Cords.FightBoss
    LeftClick(cords.nuke)
    time.sleep(rebirth * 1 if rebirth < 10 else 10)
    for i in range(5):
        LeftClick(cords.fight)
        time.sleep(0.5)

def Rebirth():
    Navigate(constants.Cords.Sidebar.rebirth)
    time.sleep(0.5)
    cords = constants.Cords.Rebirth
    LeftClick(cords.rebirth)
    time.sleep(0.5)
    LeftClick(cords.rebirthConfirm)

def AdvanceAdventureZone(navigate = True):
    if navigate:
        Navigate(constants.Cords.Sidebar.adventure)

    RightClick(constants.Cords.Adventure.forwardArrow)

def SelectQuarterEnergy():
    LeftClick(constants.Cords.Input.Energy.quarter)

def SelectHalfEnergy():
    LeftClick(constants.Cords.Input.Energy.half)

def SelectFullInput():
    LeftClick(constants.Cords.Input.Energy.customFull)

def RecallEnergy(navigate = True):
    # Navigate to ensure focus is on game window
    if navigate:
        Navigate(constants.Cords.Sidebar.timeMachine)
    keystrokes.press('r')
    print('Energy recalled')
    time.sleep(0.1)

def RecallMagic(navigate = True):
    # Navigate to ensure focus is on game window
    if navigate:
        Navigate(constants.Cords.Sidebar.timeMachine)
    keystrokes.press('t')
    print('Magic recalled')
    time.sleep(0.1)

def RecallBoth(navigate =  True):
    RecallEnergy(navigate)
    RecallMagic(navigate)

def Navigate(cord):
    LeftClick(cord)
    time.sleep(0.2)
  
#endregion

def test():
    time.sleep(2)
    
    Navigate(constants.Cords.Sidebar.wandoos)
                   
#GetCords()
#DoRuns()
DoRuns(0)
