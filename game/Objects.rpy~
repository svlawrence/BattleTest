init -2 python:

    from __future__ import division
    from random import randint
    from random import uniform
    import copy


    # List of all available types
    pokemon_types = ["normal","fire","water","electric","grass","ice","fighting","poison","ground","flying","psychic","bug","rock","ghost","dragon","dark","steel","fairy", "none"]

    # Chart for calculating type advantages
    battle_chart = [[1,1,1,1,1,1,1,1,1,1,1,1,.5,0,1,1,.5,1,1], #Normal Attacking
                [1,.5,.5,1,2,2,1,1,1,1,1,2,.5,1,.5,1,2,1,1], #Fire Attacking
                [1,2,.5,1,.5,1,1,1,2,1,1,1,2,1,.5,1,1,1,1], #Water Attacking
                [1,1,2,.5,.5,1,1,1,0,2,1,1,1,1,.5,1,1,1,1], #Electric Attacking
                [1,.5,2,1,.5,1,1,.5,2,.5,1,.5,2,1,.5,1,.5,1,1], #Grass Attacking
                [1,.5,.5,1,.5,1,1,.5,2,.5,1,.5,2,1,.5,1,.5,1,1], #Ice Attacking
                [2,1,1,1,1,2,1,.5,1,.5,.5,.5,2,0,.5,1,.5,1,1], #Fighting Attacking
                [1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0,2,1], #Poison Attacking
                [1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2,1,1], # Ground Attacking
                [1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,0.5,1,1], # Flying Attacking
                [1,1,1,1,1,1,2,2,1,1,.5,1,1,1,1,0,.5,1,1], # Psychic Attacking
                [1,0.5,1,1,2,1,0.5,.5,1,.5,2,1,1,.5,1,2,.5,.5,1], #Bug Attacking
                [1,2,1,1,1,2,0.5,1,.5,2,1,2,1,1,1,1,0.5,1,1], # Rock Attacking
                [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,.5,1,1,1], #Ghost Attacking
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,.5,0,1], #Dragon Attacking
                [1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,.5,1,.5,1], # Dark Attacking
                [1,0.5,0.5,0.5,1,2,1,1,1,1,1,1,2,1,1,1,0.5,2,1], # Steel Attacking
                [1,0.5,1,1,1,1,2,.5,1,1,1,1,1,1,2,2,0.5,1,1]] # Fairy Attacking

    # Pokemon object
    class Pokemon(object):

        # Since python doesn't use constructors, this is basically the same thing
        def __init__(self, name, type1, type2, lvl, maxHP, currHP, pAtk, sAtk, pDef, sDef, speed, status):
            self.name = name
            self.type1 = pokemon_types[type1]
            self.type2 = pokemon_types[type2]
            self.lvl = lvl
            self.maxHP = maxHP
            self.currHP = currHP
            self.pAtk = pAtk
            self.currPAtk = copy.deepcopy(pAtk)
            self.sAtk = sAtk
            self.currSAtk = copy.deepcopy(sAtk)
            self.pDef = pDef
            self.currPDef = copy.deepcopy(pDef)
            self.sDef = sDef
            self.currSDef = copy.deepcopy(sDef)
            self.speed = speed
            self.currSpeed = copy.deepcopy(speed)
            self.status = status
            self.moves = []
            self.dmgMod = 1
            self.isCrit = False

        def addMove(self, move):
            if len(self.moves) < 4:
                self.moves.append(copy.deepcopy(move))

        # Checks pokemon speed to determine order
        def checkSpeed(self, target):
            if self.speed > target.speed:
                return True
            elif self.speed < target.speed:
                return False
            elif self.speed == target.speed:
                diceRoll = randint(1,2)
                if diceRoll == 1:
                    return True
                elif diceRoll == 2:
                    return False

        # function for potion use. 1 = normal, 2 is super, and 3 is hyper
        def usePotion(self, type):
            if type == 1:
                self.currHP += 20
            elif type == 2:
                self.currHP += 50
            elif type == 3:
                self.currHP += 200
            if self.currHP > self.maxHP:
                self.currHP = copy.deepcopy(self.maxHP)

        # Determines and calculates type advantages
        def getTypeAdvantage(self, move, target):
            
            moveType = move.type
            targetType1 = pokemon_types.index(target.type1)
            targetType2 = pokemon_types.index(target.type2)
            self.dmgMod = 1
            battleDmg = battle_chart[moveType][targetType1]
            self.dmgMod *= battleDmg
            battleDmg = battle_chart[moveType][targetType2]
            self.dmgMod *= battleDmg
            #print("Move type is %s" % pokemon_types[move.type])
            #print("Target type is %s" % target.type1)
            #print("Target type is %s" % target.type2)
            #if(dmgMod > 1):
                #print("It's super effective!")
            #elif(dmgMod < 1):
                #print("It's not very effective...")
            #print("%f" % dmgMod)
            #print("The move type is: %d")
            return self.dmgMod

        # If the move type is the same as one of the pokemon's two types, gives an additional damage multiplier
        def sameTypeBonus(self, move):
            if self.type1 == move.type or self.type2 == move.type:
                return 1.5
            else:
                return 1

        # Determines if the move is a special or physical attack for calculation purposes
        def getPhysOrSpec(self, move):
            if move.spec == 1:
                return True
            else:
                return False

        # Determines the chance of criticals. Subject to extension due to moves increasing crit chances
        def calcCritChance(self):
            x = self.speed / 2
            chance = randint(0, 255)
            if x < chance:
                self.isCrit = False
                return 1
            elif x > chance or x > 255:
                self.isCrit = True
                #print("Critical strike!")
                return 2
            
        # Function for attacking enemy. Uses a 1:1 formula with the actual Pokemon damage formula, making attacks
        # 100% identical to their official game counterparts. Also can apply effects, such as defense down, poison,
        # etc
        def attack(self, move, target):
            # Checks if move deals damage and/or causes an effect
            if move.damage > 0:
                level = self.lvl
                critical = self.calcCritChance()
                typeMod = self.getTypeAdvantage(move, target)
                bonus = self.sameTypeBonus(move)
                randNum = uniform(0.85, 1.00)
                #Checks if move is physical or special 
                if self.getPhysOrSpec == True:
                    atk = self.currSAtk
                    defe = target.currSDef
                else:
                    atk = self.currPAtk
                    defe = target.currPDef
                # Actual damage calculation
                #damagep1 = (2*level)/5 + 2
                #damagep2 = atk/defe
                #damagep3 = bonus * typeMod * critical * randNum
                #print("%f %f %f" % (damagep1, move.damage, damagep2))
                #damage = ((damagep1 * move.damage * damagep2 / 50))
                damage = round((((2 * (level + 10)) / 250) * (atk/defe) * move.damage + 2) * (bonus * typeMod * critical * randNum))
                
                #print("%d" % damage)
                self.dam = damage
                # Subtracts opposing pokemon's HP
                target.currHP -= damage
                # If move has effect, deals it. Otherwise, does nothing
                move.determineEffect(target)
                #print("%d/%d" % (target.currHP, target.maxHP))
            # Checks if move just causes an effect
            elif move.damage == 0:
                self.isCrit = False
                self.dmgMod = 0
                move.determineEffect(target)

    class Moves(object):

        def __init__(self, name, pp, type, spec, damage, accuracy, effect):
            self.name = name
            self.pp = pp
            self.type = type
            self.spec = spec
            self.damage = damage
            self.accuracy = accuracy
            self.effect = effect

        def determineEffect(self, target):
            if self.effect == 1:
                if target.currPDef > target.pDef - 6:
                    target.currPDef -= 1
                    #print("You lowered your opponents defense!")
                else:
                    return "You can't lower your opponents defense anymore!"
                    #print("You can't lower your opponents defense anymore!")
            elif self.effect == 2:
                target.currPAtk -= 1
            elif self.effect == 3:
                target.currSDef -= 1
            elif self.effect == 4:
                target.currSAtk -= 1
            elif self.effect == 5:
                target.currSpeed -= 1

    class Trainer(object):
        def __init__(self, name, ID):
            self.name = name
            self.ID = ID
            self.party = []
            self.knockedOut = []
            self.storage = []

        def catchMember(self, Pokemon):
            if len(self.party) < 6:
                self.party.append(copy.deepcopy(Pokemon))
            else:
                print("You have too many members in your party! Pokemon sent to the Deposit Box")
                self.storage.append(copy.deepcopy(Pokemon))

        def numPoke(self):
            return len(self.party)
        
        def knockOut(self, i):
            self.knockedOut.append(self.party[i])
            self.party.pop(i)

        def withdraw(self, choice):
            if len(self.party) < 6:
                self.party.append(storage[choice])
                self.storage.pop(choice)
                print("Party Member Added!")
            else:
                print("Your party already has six Pokemon! Please deposit one before withdrawing another.")

        def deposit(self, choice):
            if len(self.party) > 1:
                self.storage.append(party[choice])
                self.party.pop(choice)
                print("You have deposited a pokemon")
            else:
                print("You only have one pokemon! You can't deposit any more!")

        

    ## Old classes previously used for party management. Now this information is stored in the "Trainer" class. A lot
    ## of functions have been ported over to the new class
    ##
    ##class Party(object):
    ##
    ##    def __init__(self):
    ##        self.partyList = []
    ##
    ##    def catchMember(self, Pokemon, Storage):
    ##        if len(self.partyList) < 6:
    ##            self.partyList.append(copy.deepcopy(Pokemon))
    ##        else:
    ##            print("You have too many members in your party! Pokemon sent to the Deposit Box")
    ##            Storage.storageList.append(Pokemon)
    ##
    ##    def chooseMember(self, choice):
    ##        return self.partyList[choice]
    ##
    ##    def numPoke(self):
    ##        return len(self.partyList)
    ##
    ##class Storage(object):
    ##
    ##    def __init__(self):
    ##        self.storageList = []
    ##

            

