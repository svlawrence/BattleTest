init -999:
    define n = Character("")

init -998 python:

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
        def __init__(self, name, type1, type2, lvl, base_HP, base_pAtk, base_sAtk, base_pDef, base_sDef, base_speed, catchRate):
            self.name = name
            self.base_HP = base_HP
            self.base_pAtk = base_pAtk
            self.base_sAtk = base_sAtk
            self.base_pDef = base_pDef
            self.base_sDef = base_sDef
            self.base_speed = base_speed
            self.type1 = pokemon_types[type1]
            self.type2 = pokemon_types[type2]
            self.lvl = 5
            self.maxHP = ((2 * base_HP) * self.lvl/100) + 10 + self.lvl
            self.currHP = copy.deepcopy(self.maxHP)
            self.pAtk = (2 * base_pAtk) * (self.lvl/100) + 5
            self.currPAtk = copy.deepcopy(self.pAtk)
            self.sAtk = (2 * base_sAtk) * (self.lvl/100) + 5
            self.currSAtk = copy.deepcopy(self.sAtk)
            self.pDef = (2 * base_pDef) * (self.lvl/100) + 5
            self.currPDef = copy.deepcopy(self.pDef)
            self.sDef = (2 * base_sDef) * (self.lvl/100) + 5
            self.currSDef = copy.deepcopy(self.sDef)
            self.speed = (2 * base_speed) * (self.lvl/100) + 5
            self.currSpeed = copy.deepcopy(self.speed)
            self.status = 0
            self.moves = []
            self.dmgMod = 1
            self.isCrit = False
            self.catchRate = catchRate
            self.badPoison = 1
            
        def addMove(self, move):
            if len(self.moves) < 4:
                self.moves.append(copy.deepcopy(move))
                
        def calcStats(self):
            self.maxHP = ((2 * self.base_HP) * self.lvl/100) + 10 + self.lvl
            self.currHP = copy.deepcopy(self.maxHP)
            self.pAtk = (2 * self.base_pAtk) * (self.lvl/100) + 5
            self.currPAtk = copy.deepcopy(self.pAtk)
            self.sAtk = (2 * self.base_sAtk) * (self.lvl/100) + 5
            self.currSAtk = copy.deepcopy(self.sAtk)
            self.pDef = (2 * self.base_pDef) * (self.lvl/100) + 5
            self.currPDef = copy.deepcopy(self.pDef)
            self.sDef = (2 * self.base_sDef) * (self.lvl/100) + 5
            self.currSDef = copy.deepcopy(self.sDef)
            self.speed = (2 * self.base_speed) * (self.lvl/100) + 5
            self.currSpeed = copy.deepcopy(self.speed)

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

        # Checks pokemon speed to determine order
        def checkSpeedMulti(self, ally, target, target2):
            speeds = [self.speed, ally.speed, target.speed, target2.speed]
            speeds.sort()
            return speeds
                
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
            #print("%f" % dmgMod)
            #print("The move type is: %d")
            return self.dmgMod

        def effectiveMessage(self, move):
            if self.isCrit == True:
                renpy.say(n, "Critical strike!")
            if(self.dmgMod > 1 and move.effect == 0):
                renpy.say(n, "It's super effective!")
            elif(self.dmgMod < 1 and move.effect == 0):
                renpy.say(n, "It's not very effective...")

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
                
        # Determining end of turn messages
        def endTurn(self):
            if self.status == 2:
                renpy.say(n, self.name + " is inflicted by poison!")
                self.poison()
            if self.status == 3:
                renpy.say(n, self.name + " is inflicted by burn!")
                self.burn()
            if self.status == 4:
                call .fight
                renpy.say(n, self.name + " is badly poisoned!")
                self.toxic()
            if self.status == 6:
                self.currSpeed *= curr.speed * 0.5
            
        # Function for attacking enemy. Uses a 1:1 formula with the actual Pokemon damage formula, making attacks
        # 100% identical to their official game counterparts. Also can apply effects, such as defense down, poison,
        # etc
        def attack(self, move, target, trainer=""):
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
                damage = round((((2 * (level + 10)) / 250) * (atk/defe) * move.damage + 2) * (bonus * typeMod * critical * randNum))
                #print("%d" % damage)
                self.dam = damage
                # Subtracts opposing pokemon's HP
                target.currHP -= damage
                if trainer != None:
                    move.determineEffect(target, self, trainer)
                else:
                    move.determineEffect(target, self, None)
                #print("%d/%d" % (target.currHP, target.maxHP))
            # Checks if move just causes an effect
            elif move.damage == 0:
                self.isCrit = False
                self.dmgMod = 0
                if trainer != None:
                    move.determineEffect(target, self, trainer)
                else:
                    move.determineEffect(target, self, None)
                
        def sleep(self):
            if self.status == 1:
                wake = randint(1, 3)
                if wake == 3:
                    self.status = 0
                    return True
                else:
                    return False
            else:
                return 0
                
        def poison(self):
            self.currHP -= round(self.maxHP * .12)
        
        def burn(self):
            self.currHP -= round(self.maxHP * .12)
            self.currPAtk = round(self.pAtk * .5)
            
        def freeze(self):
            if self.status == 5:
                unfreeze = randint(1,5)
                if unfreeze == 1:
                    self.status = 0
                    return True
                else:
                    return False
            else:
                return 0
                
        def paralysis(self):
            if self.status == 6:
                hit = randint(1,4)
                if hit == 4:
                    return False
                else:
                    return True
            
        def toxic(self):
            self.currHP -= round(self.maxHP * (self.badPoison/16))
            self.badPoison += 1

    class Moves(object):

        def __init__(self, name, type, spec, damage, accuracy, effect, multi=0, priority=0):
            self.name = name
            self.type = type
            self.spec = spec
            self.damage = damage
            self.accuracy = accuracy
            self.effect = effect
            self.multi = multi
            self.priority = priority

        def determineEffect(self, target, atker, trainer=""):
            ## Minor Stat Reductions
            # Def
            if self.effect == 1:
                if target.currPDef > target.pDef - 6:
                    target.currPDef -= 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s defense fell!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s defense fell!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s defense stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's defense stat won't go any lower!")
            # Atk            
            elif self.effect == 2:
                if target.currPAtk > target.pAtk - 6:
                    target.currPAtk -= 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s attack fell!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s attack fell!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s attack stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's attack stat won't go any lower!")
            # S Def        
            elif self.effect == 3:
                if target.currSDef > target.sDef - 6:
                    target.currSDef -= 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s sp. defense fell!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s sp. defense fell!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s sp. defense stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's sp. defense stat won't go any lower!")
            # S Atk        
            elif self.effect == 4:
                if target.currSAtk > target.sAtk - 6:
                    target.currSAtk -= 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s sp. attack fell!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s sp. attack fell!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s sp. attack stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's sp. attack stat won't go any lower!")
            # Speed            
            elif self.effect == 5:
                if target.currSpeed > target.speed - 6:
                    target.currSpeed -= 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s speed fell!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s speed fell!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s speed stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's speed stat won't go any lower!")
                        
            ## Major Stat Reductions
            # Def
            elif self.effect == 6:
                if target.currPDef > target.pDef - 6:
                    target.currPDef -= 2
                    if target.currPDef < target.pDef - 6:
                        target.currPDef += 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s defense fell greatly!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s defense fell greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s defense stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's defense stat won't go any lower!")
            #Atk
            elif self.effect == 7:
                if target.currPAtk > target.pAtk - 6:
                    target.currPAtk -= 2
                    if target.currPAtk < target.pAtk - 6:
                        target.currPAtk += 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s attack fell greatly!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s attack fell greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s attack stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's attack stat won't go any lower!")
            # S. Def
            elif self.effect == 8:
                if target.currSDef > target.sDef - 6:
                    target.currSDef -= 2
                    if target.currSDef < target.sDef - 6:
                        target.currSDef += 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s sp. defense fell greatly!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s sp. defense fell greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s sp. defense stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's sp. defense stat won't go any lower!")
            # S. Atk
            elif self.effect == 9:
                if target.currSAtk > target.sAtk - 6:
                    target.currSAtk -= 2
                    if target.currSAtk < target.sAtk - 6:
                        target.currSAtk += 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s sp. attack fell greatly!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s sp. attack fell greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s sp. attack stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's sp. attack stat won't go any lower!")
            # Speed
            elif self.effect == 10:
                if target.currSpeed > target.speed - 6:
                    target.currSpeed -= 2
                    if target.currSpeed < target.speed - 6:
                        target.currSpeed += 1
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s speed fell greatly!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s speed fell greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, target.name + "'s speed stat won't go any lower!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "s's speed stat won't go any lower!")
            ## Minor Stat Improvement
            # def
            if self.effect == 11:
                if atker.currPDef < atker.pDef + 6:
                    atker.currPDef += 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s defense grew!")
                    else:
                        renpy.say(n, atker.name + "'s defense grew!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s defense won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s defense won't go any higher!")
            # atk
            elif self.effect == 12:
                if atker.currPAtk < atker.pAtk + 6:
                    atker.currPAtk += 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s attack grew!")
                    else:
                        renpy.say(n, atker.name + "'s attack grew!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s attack won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s attack won't go any higher!")
            # s def
            elif self.effect == 13:
                if atker.currSDef < atker.sDef + 6:
                    atker.currSDef += 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s sp. defense grew!")
                    else:
                        renpy.say(n, atker.name + "'s sp. defense grew!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s sp. defense won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s sp. defense won't go any higher!")
            # s atk
            elif self.effect == 14:
                if atker.currSAtk < atker.sAtk + 6:
                    atker.currSAtk += 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s sp. attack grew!")
                    else:
                        renpy.say(n, atker.name + "'s sp. attack grew!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s sp. attack won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s sp. attack won't go any higher!")
            # speed
            elif self.effect == 15:
                if atker.currSpeed < atker.speed + 6:
                    atker.currSpeed += 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s speed grew!")
                    else:
                        renpy.say(n, atker.name + "'s speed grew!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s speed won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s speed won't go any higher!")
            ## Major Stat Improvement
            # def
            elif self.effect == 16:
                if atker.currPDef < atker.pDef + 6:
                    atker.currPDef += 2
                    if atker.currPDef > atker.pDef + 6:
                        atker.currPDef -= 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s defense grew greatly!")
                    else:
                        renpy.say(n, atker.name + "'s defense grew greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s defense won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s defense won't go any higher!")
            # atk
            elif self.effect == 17:
                if atker.currPAtk < atker.pAtk + 6:
                    atker.currPAtk += 2
                    if atker.currPAtk > atker.pAtk + 6:
                        atker.currPAtk -= 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s attack grew greatly!")
                    else:
                        renpy.say(n, atker.name + "'s attack grew greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s attack won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s attack won't go any higher!")
            # s def
            elif self.effect == 18:
                if atker.currSDef < atker.sDef + 6:
                    atker.currSDef += 2
                    if atker.currSDef > atker.sDef + 6:
                        atker.currSDef -= 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s sp. defense grew greatly!")
                    else:
                        renpy.say(n, atker.name + "'s sp. defense grew greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s sp. defense won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s sp. defense won't go any higher!")
            # s atk
            elif self.effect == 19:
                if atker.currSAtk < atker.sAtk + 6:
                    atker.currSAtk += 2
                    if atker.currSAtk > atker.sAtk + 6:
                        atker.currSAtk -= 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s sp. attack grew greatly!")
                    else:
                        renpy.say(n, atker.name + "'s sp. attack grew greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s sp. attack won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s sp. attack won't go any higher!")
            # speed
            elif self.effect == 20:
                if atker.currSpeed < atker.speed + 6:
                    atker.currSpeed += 2
                    if atker.currSpeed > atker.speed + 6:
                        atker.currSpeed -= 1
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s speed grew greatly!")
                    else:
                        renpy.say(n, atker.name + "'s speed grew greatly!")
                else:
                    if trainer == "enem": 
                        renpy.say(n, "Enemy " + atker.name + "'s speed won't go any higher!")
                    else:
                        renpy.say(n, atker.name + "'s speed won't go any higher!")
            # sleep
            elif self.effect == 21:
                if target.status == 0:
                    target.status = 1
                    if trainer == "enem":
                        renpy.say(n, target.name + "'s fallen asleep!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s fallen asleep!")
                else:
                    renpy.say(n, "But it failed!")
            # poision
            elif self.effect == 22:
                if target.status == 0:
                    target.status = 2
                    if trainer == "enem":
                        renpy.say(n, target.name + " is now poisoned!")
                    else:
                        renpy.say(n, "Enemy " + target.name + " is now poisoned!")
                else:
                    renpy.say(n, "But it failed!")
            # burn
            elif self.effect == 23:
                if target.status == 0:
                    target.status = 3
                    if trainer == "enem":
                        renpy.say(n, target.name + " is burned!")
                    else:
                        renpy.say(n, "Enemy " + target.name + " is burned!")
                else:
                    renpy.say(n, "But it failed!")
            # bad poison
            elif self.effect == 24:
                if target.status == 0:
                    target.status = 4
                    if trainer == "enem":
                        renpy.say(n, target.name + "'s is now badly poisoned!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s is now badly poisoned!")
                else:
                    renpy.say(n, "But it failed!")
            # freeze
            elif self.effect == 25:
                if target.status == 0:
                    target.status = 5
                    if trainer == "enem":
                        renpy.say(n, target.name + "'s fallen asleep!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s fallen asleep!")
                else:
                    renpy.say(n, "But it failed!")
            # paralysis
            elif self.effect == 26:
                if target.status == 0:
                    target.status = 6
                    if trainer == "enem":
                        renpy.say(n, target.name + "'s fallen asleep!")
                    else:
                        renpy.say(n, "Enemy " + target.name + "'s fallen asleep!")
                else:
                    renpy.say(n, "But it failed!")
                    
                    
    class Trainer(object):
        def __init__(self, name, ID):
            self.name = name
            self.ID = ID
            self.party = []
            self.knockedOut = []
            self.storage = []
            self.pokeBalls = 0
            self.greatBalls = 0
            self.ultraBalls = 0

        def catchMember(self, Pokemon):
            if len(self.party) < 6:
                self.party.append(copy.deepcopy(Pokemon))
            else:
                print("You have too many members in your party! Pokemon sent to the Deposit Box")
                self.storage.append(copy.deepcopy(Pokemon))
                
        def tryCatch(self, status, hp, maxHP, rate, bonus):
            if status == 0:
                status = 1
            catchChance = round((((3*maxHP - 2*hp)*rate*bonus)/(3*maxHP))*status)
            diceRoll = randint(0, 255)
            if (catchChance < diceRoll) and (catchChance < 255):
                return False
            elif (catchChance >= diceRoll and catchChance < 255) or (catchChance >= 255):
                return True

        def numPoke(self):
            return len(self.party)
        
        def knockOut(self, i):
            self.knockedOut.append(self.party[i])
            self.party.pop(i)

        def withdraw(self, num):
            if len(self.party) < 6:
                self.party.append(self.storage[num])
                self.storage.pop(num)
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
                
        def partyHeal(self):
            while len(self.knockedOut) != 0:
                self.party.append(self.knockedOut[0])
                self.knockedOut.pop(0)
            for i in range(len(self.party)):
                self.party[i].currHP = copy.deepcopy(self.party[i].maxHP)
                self.party[i].currPAtk = copy.deepcopy(self.party[i].pAtk)
                self.party[i].currPDef = copy.deepcopy(self.party[i].pDef)
                self.party[i].currSAtk = copy.deepcopy(self.party[i].sAtk)
                self.party[i].currSDef = copy.deepcopy(self.party[i].sDef)
                self.party[i].currSpeed = copy.deepcopy(self.party[i].speed)
                self.party[i].badPoison = 0

        
    def stats_frame(name, level, hp, maxhp, **properties):

        ui.frame(xfill=False, yminimum=0, xminimum=280,**properties)
        ui.hbox() # (name, "HP", bar) from (level, hp, maxhp)
        ui.vbox() # name from ("HP", bar)

        ui.text(name, size=20)

        ui.hbox() # "HP" from bar
        ui.text("HP", size=20)
        ui.bar(maxhp, hp, xmaximum=150)

        ui.close()
        ui.close()

        ui.vbox() # Level from (hp/maxhp)
        
        ui.text("Lv. %d" % level, xalign=0.5, size=20)
        ui.text("%d/%d" % (hp, maxhp), xalign=0.5, size=20)

        ui.close()
        ui.close()


    def face_frame(name, **properties):

        ui.frame(xfill=False, **properties)
        ui.hbox()
        ui.image(name);
        ui.close()
        

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

            

##EFFECTS KEY:

##0: Default

##1: -1 Def

##2: -1 Atk

##3: -1 S. Def

##4: -1 S. Atk

##5: -1 Speed

##6: -2 Def

##7: -2 Atk

##8: -2 S. Def

##9: -2 S. Atk

##10: -2 Speed

##11: +1 Def

##12: +1 Atk

##13: +1 S. Def

##14: +1 S. Atk

##15: +1 Speed

##16: +2 Def

##17: +2 Atk

##18: +2 S. Def

##19: +2 S. Atk

##20: +2 Speed

##21: sleep

##22: poison

##23: burn

##24: bad poison

##25: freeze

##26: paralysis

##27: other