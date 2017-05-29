label RedVBlue:
    # This is the beginning of an encounter. This is where things will be set up
    python:
        # Setting appropriate levels
        Squirtle.lvl = 5
        Charmander.lvl = 5
        # Calculating stats
        Squirtle.calcStats()
        Charmander.calcStats()
        
        # Setting up trainers
        Red = Trainer("Red", 1)
        Blue = Trainer("Blue", 2)
        
        # Catching members. Ignore for now
        Red.catchMember(Charmander)
        Red.catchMember(Pikachu)
        Blue.catchMember(Squirtle)
        
        # Giving pokemon moves
        Red.party[0].addMove(Tackle)
        Red.party[0].addMove(Tail_Whip)
        Red.party[0].addMove(Razor_Leaf)
        #Blue.party[0].addMove(Tackle)
        Blue.party[0].addMove(Tail_Whip)
        Blue.party[0].addMove(Water_Gun)
        
        # Number of pokemon in Red's party.
        numPoke = Red.numPoke()
        # Setting index for Blue's pokemon
        eCurrPoke = 0
            
        combat_turn = 0
            
        Red.pokeBalls = 3
        Red.greatBalls = 2
        Red.ultraBalls = 1
    # After initial setup is complete, jump to the splash screen        
    jump .splash

# Splash screen
label .splash:
    # Queue music
    $ renpy.music.queue("music/battle/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0)
    $ renpy.music.queue("music/battle/KantoTrainerLoop_Rock.ogg", channel='music', loop=True)
    
    # Red splash
    image Red_Splash:
        #xpos .20
        ypos 750
        zoom .75
        "/images/red_casual_1024.png"
    
    # Blue splash
    image Blue_Splash:
        xpos .80
        ypos 750
        zoom .75
        "/images/blue_casual_1024.png"
    # vs word    
    image versus:
        ypos 600
        "images/versus.png"
        
    # show Red at these coordinates    
    show Red_Splash:
        xalign -1 yalign 1.0
        ease 0.5 xalign -.1
        
    # show Blue at this coordinates
    show Blue_Splash:
        xalign 2.0 yalign 1.0
        ease 0.5 xalign 1.0
        
    # wait half a second
    pause 0.5
    
    # show the versus symbol
    show versus:
        xalign 0.5 yalign -0.5
        ease 0.5 yalign 0.5
        
    # wait a full second
    pause 1
    
    # hide images
    hide Red_Splash
    hide Blue_Splash
    hide versus
    
    # call the combat label
    call .combat

# "Combat is choosing the first pokemon to use/whenever a pokemon faints
label .combat:
    if combat_turn == 0:
        menu:
            "Choose your Pokemon:"
            "[Red.party[0].name]" if numPoke >= 1:
                $ currPoke = 0
            "[Red.party[1].name]" if numPoke >= 2:
                $ currPoke = 1
            "[Red.party[2].name]" if numPoke >= 3:
                $ currPoke = 2
            "[Red.party[3].name]" if numPoke >= 4:
                $ currPoke = 3
            "[Red.party[4].name]" if numPoke >= 5:
                $ currPoke = 4
            "[Red.party[5].name]" if numPoke == 6:
                $ currPoke = 5
        jump .pokemon

# Frames update
label .fight:

    # Player Stats Frame
    show screen pstats(pname, plevel, php, pmaxhp, .17, .7)
    if Red.party[currPoke].currHP >= round(Red.party[currPoke].maxHP * .75):
        show screen pface("/images/Portraits/Red Square Casual Happy.png", 0.015, .653)
    if Red.party[currPoke].currHP <= round(Red.party[currPoke].maxHP * .75) and Red.party[currPoke].currHP > Red.party[currPoke].maxHP * .25:
         show screen pface("/images/Portraits/Red Square Casual Neutral.png", 0.015, .653)
    elif Red.party[currPoke].currHP <= round(Red.party[currPoke].maxHP * .25):
         show screen pface("/images/Portraits/Red Square Casual Worried.png", 0.015, .653)
    
        
    # Enemy Stats Frame. Will be expanded once rest of portraits are recieved for Blue
    show screen estats(ename, elevel, ehp, emaxhp, .83, .7)
    show screen eface("/images/Portraits/Blue Square Casual Neutral.png", 0.98, .653)
    return
        
# Pokemon update label. Pokemon are set up here
label .pokemon:
    # get HP
    $ php = Red.party[currPoke].currHP
    $ ehp = Blue.party[eCurrPoke].currHP
    # get image paths
    $ pokeImagePath = "/images/pokemon/" + Red.party[currPoke].name + ".png"
    $ eImagePath = "/images/pokemon/" + Blue.party[eCurrPoke].name + ".png"
    
    # Red's pokemon
    image playerPokemon:
        xalign .02
        yalign .02
        xpos 25
        ypos 100
        zoom .75
        pokeImagePath
    show playerPokemon
    
    # Blue's pokemon
    image enemyPokemon:
        xalign .02
        yalign .02
        xpos 850
        ypos 150
        zoom .75
        eImagePath
    show enemyPokemon
    
    # checks if Red's pokemon's HP isn't 0. If it is, problems occur
    if php != 0:
        $ pname = Red.party[currPoke].name
        $ plevel = Red.party[currPoke].lvl
        $ pmaxhp = Red.party[currPoke].maxHP
        
    if ehp != 0:
        $ ename = Blue.party[eCurrPoke].name
        $ elevel = Blue.party[eCurrPoke].lvl
        $ emaxhp = Blue.party[eCurrPoke].maxHP
            
            
label .battle:
    call .fight
    $ combat_turn += 1
    $ skillChoice = len(Red.party[currPoke].moves)
    $ numSkill = 0
    $ speedTest = Red.party[currPoke].checkSpeed(Blue.party[eCurrPoke])
    $ switched = False
    $ print(Red.party[currPoke].speed)
    $ print(Blue.party[eCurrPoke].speed)
    $ print(speedTest)
    
    python:
        if skillChoice >= 1:
             skill1_name = Red.party[currPoke].moves[0].name
        if skillChoice >= 2:
             skill2_name = Red.party[currPoke].moves[1].name
        if skillChoice >= 3:
             skill3_name = Red.party[currPoke].moves[2].name
        if skillChoice >= 4:
             skill4_name = Red.party[currPoke].moves[3].name
    
    menu:
        "What would you like to do?"
        "Fight":
            call .fight
            menu:
                "What should [pname] do?"
                "[skill1_name]" if skillChoice >= 1:
                    $ numSkill = 0
                "[skill2_name]" if skillChoice >= 2:
                    $ numSkill = 1
                "[skill3_name]" if skillChoice >= 3:
                    $ numSkill = 2
                "[skill4_name]" if skillChoice >= 4:
                    $ numSkill = 3
                "Back":
                    jump .battle
            jump .order
        "Switch" if len(Red.party) > 1:
            menu:
                "[Red.party[0].name]" if numPoke >= 1 and Red.party[0] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 0
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .order
                "[Red.party[1].name]" if numPoke >= 2 and Red.party[1] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 1
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .order
                "[Red.party[2].name]" if numPoke >= 3 and Red.party[2] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 2
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .order
                "[Red.party[3].name]" if numPoke >= 4 and Red.party[3] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 3
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .order
                "[Red.party[4].name]" if numPoke >= 5 and Red.party[4] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 4
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .order
                "[Red.party[5].name]" if numPoke == 6 and Red.party[5] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 5
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .order
                "Back":
                    jump .battle
            call .fight
            jump .enemyAttack
        "Catch" if Blue.ID == 0:
            menu:
                "Use Poke Ball ([Red.pokeBalls] left)" if Red.pokeBalls > 0:
                    $ bonus = 1
                    $ Red.pokeBalls = Red.pokeBalls - 1
                "Use Great Ball ([Red.greatBalls] left)" if Red.greatBalls > 0:
                    $ bonus = 2
                    $ Red.greatBalls = Red.greatBalls - 1
                "Use Ultra Ball ([Red.ultraBalls] left)" if Red.ultraBalls > 0: 
                    $ bonus = 3
                    $ Red.ultraBalls = Red.ultraBalls - 1
                "Back":
                    jump .battle
            $ attemptCatch = Red.tryCatch(Blue.party[eCurrPoke].status, Blue.party[eCurrPoke].currHP, Blue.party[eCurrPoke].maxHP, Blue.party[eCurrPoke].catchRate, bonus)
            if attemptCatch == True:
                 $ switched = True
                 $ Red.catchMember(Blue.party[eCurrPoke])
                 $ print(len(Red.party))
                 "You caught the Pokemon!"
                 jump .e_defeat
            else:
                 $ switched = True
                 "Darn! Didn't catch it!"
                 jump .enemyAttack
        "Run Away" if Blue.ID == 0:
            "Got away safely!"
            #jump to the next label
            
label .hideImage:
    hide playerPokemon

label .enemyHideImage:
    hide enemyPokemon
    
label .e_defeat:
     scene black with dissolve
     centered "You win!"
     $  Red.partyHeal()
     $  Blue.partyHeal()
     $  renpy.full_restart()

label .p_defeat:
     scene black with dissolve
     centered "You lose!"
     $  Red.partyHeal()
     $  Blue.partyHeal()
     $ renpy.full_restart()     
     
label .playerAttack:
    call .fight
    if Red.party[currPoke].status == 1:
        $ wokenup = Red.party[currPoke].sleep()
        if wokenup == False:
            call .fight
            "[pname] is asleep!"
            if speedTest == True and switched == False:
                jump .enemyAttack
            else:
                jump .endTurn
        elif wokenup == True:
            call .fight
            "[pname] woke up!"
    $ skill_name = Red.party[currPoke].moves[numSkill].name
    $ face_frame("/images/Portraits/Red Square Casual Attacking.png", xalign = 0.015, yalign=.653, zoom=.25)
    "[pname] used [skill_name]!"
    if Red.party[currPoke].status == 5:
        $ froz = Red.party[currPoke].freeze()
        if froz == False:
            call .fight
            "[pname] is frozen!"
            if speedTest == True and switched == False:
                jump .enemyAttack
            else:
                jump .endTurn
        else:
            call .fight
            "[pname] is frozen no longer!"
    if Red.party[currPoke].status == 6:
        $ para = Red.party[currPoke].paralysis()
        if para == False:
            call .fight
            "[pname] is paralysed! It can't move!"
            if speedTest == True and switched == False:
                jump .enemyAttack
            else:
                jump .endTurn
    $ Red.party[currPoke].attack(Red.party[currPoke].moves[numSkill], Blue.party[eCurrPoke])
    if Blue.party[eCurrPoke].currHP > 0:
        $ ehp = Blue.party[eCurrPoke].currHP
        call .fight
    else:
        $ ehp = 0
        call .fight
       
       
    if Red.party[currPoke].moves[numSkill].effect == 1:
        call .fight
        #if Blue.party[eCurrPoke].currPDef > Blue.party[eCurrPoke].pDef - 6:
        #    "You lowered your opponents defense!"
        #elif Blue.party[eCurrPoke].currPDef == Blue.party[eCurrPoke].pDef - 6:
        #    "You can't lower your opponents defense anymore!"

    $ Red.party[currPoke].effectiveMessage(Red.party[currPoke].moves[numSkill])
        

        
    $ checkEHP = Blue.party[eCurrPoke].currHP    
    if checkEHP < 1:
        $ ehp = 0
        call .fight
        "Enemy [ename] fainted!"
        hide enemyPokemon
        $ Blue.knockOut(eCurrPoke)
        $ enemyPoke = Blue.numPoke()
        
        if enemyPoke > 0:
            $ ename = Blue.party[eCurrPoke].name
            "Blue: Go, [ename]!"
            call .pokemon
            jump .battle
        else:
            call .e_defeat
        
    $ order.pop(0)
    if not order:
        jump .endTurn
    elif(order[0] == 1):
        jump .playerAttack
    elif(order[0] == 2):
        jump .enemyAttack
        
label .enemyAttack:
    $ skill = Blue.party[eCurrPoke].moves[pickedMove]
    $ skill_name = Blue.party[eCurrPoke].moves[pickedMove].name
    
    call .fight
    if Blue.party[eCurrPoke].status == 1:
        $ wokenup = Blue.party[eCurrPoke].sleep()
        if wokenup == False:
            call .fight
            "[ename] is asleep!"
            if speedTest == True and switched == False:
                jump .endTurn
            else:
                jump .playerAttack
        elif wokenup == True:
            call .fight
            "[ename] woke up!"    
        
    "[poke_name] used [skill_name]!"
    if Blue.party[eCurrPoke].status == 5:
        $ froz = Blue.party[eCurrPoke].freeze()
        if froz == False:
            call .fight
            "[ename] is frozen!"
            if speedTest == True and switched == False:
                jump .endTurn
            else:
                jump .playerAttack
        else:
            call .fight
            "[ename] is frozen no longer!"
    if Blue.party[eCurrPoke].status == 6:
        $ para = Blue.party[eCurrPoke].paralysis()
        if para == False:
            call .fight
            "[ename] is paralysed! It can't move!"
            if speedTest == True and switched == False:
                jump .endTurn
            else:
                jump .playerAttack
    $ Blue.party[eCurrPoke].attack(skill, target, "enem")
    if Red.party[currPoke].currHP > 0:
       $  php = Red.party[currPoke].currHP
       call .fight
    else:
        $ php = 0
        call .fight

    if Blue.party[eCurrPoke].moves[pickedMove].effect == 1:
        call .fight
        
        #if Red.party[currPoke].currPDef >= Red.party[currPoke].pDef - 6:
        #    "Your opponent lowered your defense!"
        #elif Red.party[currPoke].currPDef == Red.party[currPoke].pDef - 7:
        #    "Your defense can't go any lower!"

    $ Blue.party[eCurrPoke].effectiveMessage(skill)
    
    
    $ checkPHP = Red.party[currPoke].currHP    
    if checkPHP < 1:
        $ php = 0
        call .fight
        "[target_name] fainted!"
        hide playerPokemon
        $ Red.knockOut(currPoke)
        $ numPoke = Red.numPoke()
        if numPoke > 0:
            $ combat_turn = 0
            jump .combat
        else:
            call .p_defeat
        
    $ order.pop(0)
    if not order:
        jump .endTurn
    elif(order[0] == 1):
        jump .playerAttack
    elif(order[0] == 2):
        jump .enemyAttack

label .endTurn:
    $ Red.party[currPoke].endTurn()

    $ checkPHP = Red.party[currPoke].currHP    
    if checkPHP < 1:
        $ php = 0
        call .fight
        "[target_name] fainted!"
        hide playerPokemon
        $ Red.knockOut(currPoke)
        $ numPoke = Red.numPoke()
        if numPoke > 0:
            $ combat_turn = 0
            jump .combat
        else:
            call .p_defeat
  
    $ Blue.party[eCurrPoke].endTurn()
    
    $ checkEHP = Blue.party[eCurrPoke].currHP    
    if checkEHP < 1:
        $ ehp = 0
        call .fight
        "Enemy [ename] fainted!"
        hide enemyPokemon
        $ Blue.knockOut(eCurrPoke)
        $ enemyPoke = Blue.numPoke()
        
        if enemyPoke > 0:
            $ ename = Blue.party[eCurrPoke].name
            "Blue: Go, [ename]!"
            call .pokemon
            jump .battle
        else:
            call .e_defeat
        
    call .pokemon
    jump .battle

label .switch:
    $ pname = Red.party[currPoke].name
    $ plevel = Red.party[currPoke].lvl
    $ pmaxhp = Red.party[currPoke].maxHP
    $ php = Red.party[currPoke].currHP
    $ numskill = None
    $ switched = True
    call .fight
    $ pokeImagePath = "/images/pokemon/" + Red.party[currPoke].name + ".png"
    hide playerPokemon
    image playerPokemon:
        xalign .02
        yalign .02
        xpos 25
        ypos 100
        zoom .75
        pokeImagePath
    show playerPokemon
    call .fight
    jump .order
    
label .order:
    # Foe picking attack
    # AI section, minimal for Blue right now
    $ numMoves = len(Blue.party[eCurrPoke].moves) - 1
    $ pickedMove = randint(0, numMoves)
    python:
        while 1:
            if Blue.party[eCurrPoke].moves[pickedMove].effect == 0:
                break
            elif Red.party[currPoke].currPDef > Red.party[currPoke].pDef - 6 and Blue.party[eCurrPoke].moves[pickedMove].effect == 1:
                break
            else:
                pickedMove = randint(0, numMoves)
    
    $ eskill = Blue.party[eCurrPoke].moves[pickedMove]
    $ eskill_name = Blue.party[eCurrPoke].moves[pickedMove].name
    $ poke_name = Blue.party[eCurrPoke].name
    $ target = Red.party[currPoke]
    $ target_name = target.name
    
    # Player attack
    if switched == False:
        $ pskill = Red.party[currPoke].moves[numSkill]
    
    python:
        if switched == True:
            order = [ 2 ]
        elif pskill.priority > eskill.priority:
            order = [1 , 2]
        elif pskill.priority < eskill.priority:
            order = [2 , 1]
        elif pskill.priority == eskill.priority:
            if speedTest == True:
                order = [1 , 2]
            else:
                order = [2 , 1]
                
    if(order[0] == 1):
        jump .playerAttack
    elif(order[0] == 2):
        jump .enemyAttack
