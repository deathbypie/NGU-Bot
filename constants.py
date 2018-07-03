"""

Contains coordinates for NGU Idle

"""

class Cords:
    # Sidebars(Includes rebirth,exp)
    class Sidebar:
        basicTraining = (228,43)
        fightBoss = (228,77)
        moneyPit = (228,103)
        adventure = (228,136)
        inventory = (228,167)
        augments = (228,195)
        advancedTraining = (228,227)
        timeMachine = (228,255)
        bloodMagic = (228,285)
        wandoos = (228,311)
        ngu = (228,343)
        yggdrasil = (228,372)
        beards = (228,407)
        rebirth = (85,416)
        spendExp = (85,446)
        
    #Fight Boss
    class FightBoss:
        fight = (621,221)
        nuke = (621, 109)
    #Money Pit - Might add sometime

    #Adventure
    class Adventure:
        backArrow = (321,237)
        forwardArrow = (935,237)
        
    #Inventory - Maybe later

    #Augments - Assumes scrolled up. Might add scrolling later.
    class Augments:
        #Add and remove energy always at same y cords
        xAdd = 540
        xRemove = 572
        #y cords - format of (augment, upgrade)
        scissors = (263,292)
        milk = (325,352)
        cannon = (393,422)
        shoulder = (457,484)
        buster = (518,554)
        
    #Advanced Training
    class AdvancedTraining:
        xAdd = 862
        xRemove = 897
        #y cords
        toughness = 231
        power = 274
        block = 310
        energyDump = 354
        magicDump = 392

    #Time Machine
    class TimeMachine:
        xAdd = 534
        xRemove = 567
        #y cords
        energy = 237
        magic = 334
        
    #Blood Magic - ignores spell casting for nowand assume auto
    class BloodMagic:
        xAdd = 494
        xRemove = 530
        xCap = 568
        #y cords - unnamed rituals. Last one needs unlocking
        yRituals = (228,266,297,332,370,405,435,473)

    #Wandoos
    class Wandoos:
        xAdd = 554
        xRemove = 590
        xCap = 625
        #y cords
        energy = 253
        magic = 349

    #NGU might not matter

    #Yggdrasil - maybe later for long runs

    #Beards can be ignored

    #Rebirth
    class Rebirth:
        rebirth = (537,520)
        rebirthConfirm = (428,315)
        challenges = (695,520) #Might add challenge info.

    #Input Adjusts - only visible in menus where energy/magic is used
    class Input:
        #Just an idea for now. Will add more when needed.
        class Energy:
            half = (501,22)
            quarter = (532,22)
            customFull = (590,46)
