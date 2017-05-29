label RedLeafVMayBrendan:
    
    python:   
        #Declarations. Ideally you would set these early in the game. Not completely done.
        
        # Moves: name, type, spec, damage, accuracy, effect
        Tackle = Moves("Tackle", 0, 0, 35, 100, 0, 0)
        Tail_Whip = Moves("Tail Whip", 0, 0, 0, 100, 1, 0)
        Bubble = Moves("Bubble", 2, 1, 40, 100, 0, 0)
        Thunder_Shock = Moves("Thunder Shock", 3, 1, 40, 100, 0, 0)
        Razor_Leaf = Moves("Razor Leaf", 3, 1, 55, 100, 0, 0)
        
        Red = Trainer("Red", 1)
        Leaf = Trainer("Leaf", 3)
        May = Trainer("May", 4)
        Brendan = Trainer("Brendan", 5)
        
        # Catching members. Ignore for now
        Red.catchMember(Charmander)
        Leaf.catchMember(Squirtle)
        May.catchMember(Squirtle)
        Brendan.catchMember(Squirtle)
        
        # Giving pokemon moves
        Red.party[0].addMove(Tackle)
        Red.party[0].addMove(Tail_Whip)
        Red.party[0].addMove(Razor_Leaf)
        #May.party[0].addMove(Tackle)
        May.party[0].addMove(Tail_Whip)
        May.party[0].addMove(Bubble)
        
        # Number of pokemon in Red's party.
        numPoke = Red.numPoke()
        # Setting index for May's pokemon
        aCurrPoke = 0
        eCurrPoke = 0
        e2CurrPoke = 0
        
        movePriority = 0
        combat_turn = 0
            
        Red.pokeBalls = 3
        Red.greatBalls = 2
        Red.ultraBalls = 1
            
    jump .splash

label .splash:

    $ renpy.music.queue("music/battle/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0)
    $ renpy.music.queue("music/battle/KantoTrainerLoop_Rock.ogg", channel='music', loop=True)
    image Red_Splash:
        #xpos .20
        ypos 750
        zoom .75
        "/images/red_casual_1024.png"
    
    image May_Splash:
        xpos .80
        ypos 750
        zoom .75
        "/images/May_casual_1024.png"
        
    image versus:
        ypos 600
        "images/versus.png"
        
    show Red_Splash:
        xalign -1 yalign 1.0
        ease 0.5 xalign -.1
    show May_Splash:
        xalign 2.0 yalign 1.0
        ease 0.5 xalign 1.0
    pause 0.5
    show versus:
        xalign 0.5 yalign -0.5
        ease 0.5 yalign 0.5
    pause 1
    
    hide Red_Splash
    hide May_Splash
    hide versus
    call .combat

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
    
        
    # Enemy Stats Frame
    show screen estats(ename, elevel, ehp, emaxhp, .83, .7)
    show screen eface("/images/Portraits/May Square Casual Neutral.png", 0.98, .653)
    return
        
# Pokemon update label
label .pokemon:
    $ php = Red.party[currPoke].currHP
    $ ehp = May.party[eCurrPoke].currHP
    $ pokeImagePath = "/images/pokemon/" + Red.party[currPoke].name + ".png"
    $ eImagePath = "/images/pokemon/" + May.party[eCurrPoke].name + ".png"
    
    image playerPokemon_RedvMay:
        xalign .02
        yalign .02
        xpos 25
        ypos 100
        zoom .75
        pokeImagePath
    show playerPokemon_RedvMay
        
    image enemyPokemon_RedvMay:
        xalign .02
        yalign .02
        xpos 850
        ypos 150
        zoom .75
        eImagePath
    show enemyPokemon_RedvMay
        
    if php != 0:
        $ pname = Red.party[currPoke].name
        $ plevel = Red.party[currPoke].lvl
        $ pmaxhp = Red.party[currPoke].maxHP
        
    if ehp != 0:
        $ ename = May.party[eCurrPoke].name
        $ elevel = May.party[eCurrPoke].lvl
        $ emaxhp = May.party[eCurrPoke].maxHP
            
            
label .battle:
    call .fight
    $ combat_turn += 1
    $ skillChoice = len(Red.party[currPoke].moves)
    $ numSkill = 0
    $ speedTest = Red.party[currPoke].checkSpeedMulti(May.party[eCurrPoke], )
    $ switched = False
    $ print(Red.party[currPoke].speed)
    $ print(Red.party[eCurrPoke].speed)
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
            if speedTest[movePriority] == Red.party[currPoke].speed:
                jump .playerAttack
            elif speedTest[movePriority] == Leaf.party[aCurrPoke].speed:
                jump .allyAttack
            elif speed[movePriority] == May.party[eCurrPoke].speed:
                jump .enemyAttack
            elif speed[movePriority] == Brendan.party[e2CurrPoke].speed:
                jump .enemy2Attack
        "Switch":
            menu:
                "[Red.party[0].name]" if numPoke >= 1 and Red.party[0] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 0
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .enemyAttack
                "[Red.party[1].name]" if numPoke >= 2 and Red.party[1] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 1
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .enemyAttack
                "[Red.party[2].name]" if numPoke >= 3 and Red.party[2] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 2
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .enemyAttack
                "[Red.party[3].name]" if numPoke >= 4 and Red.party[3] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 3
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .enemyAttack
                "[Red.party[4].name]" if numPoke >= 5 and Red.party[4] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 4
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .enemyAttack
                "[Red.party[5].name]" if numPoke == 6 and Red.party[5] != Red.party[currPoke]:
                    call .fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 5
                    call .switch
                    "[Red.name]: Go, [pname]!"
                    jump .enemyAttack
                "Back":
                    jump .battle
            call .fight
            jump .enemyAttack
        "Catch" if May.ID == 0:
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
            $ attemptCatch = Red.tryCatch(May.party[eCurrPoke].status, May.party[eCurrPoke].currHP, May.party[eCurrPoke].maxHP, May.party[eCurrPoke].catchRate, bonus)
            if attemptCatch == True:
                 $ switched = True
                 $ Red.catchMember(May.party[eCurrPoke])
                 $ print(len(Red.party))
                 "You caught the Pokemon!"
                 jump .e_defeat
            else:
                 $ switched = True
                 "Darn! Didn't catch it!"
                 jump .enemyAttack
        "Run Away" if May.ID == 0:
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
     $  May.partyHeal()
     $  renpy.full_restart()

label .p_defeat:
     scene black with dissolve
     centered "You lose!"
     $  Red.partyHeal()
     $  May.partyHeal()
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
    $ Red.party[currPoke].attack(Red.party[currPoke].moves[numSkill], May.party[eCurrPoke])
    if May.party[eCurrPoke].currHP > 0:
        $ ehp = May.party[eCurrPoke].currHP
        call .fight
    else:
        $ ehp = 0
        call .fight
       
       
    if Red.party[currPoke].moves[numSkill].effect == 1:
        call .fight
        #if May.party[eCurrPoke].currPDef > May.party[eCurrPoke].pDef - 6:
        #    "You lowered your opponents defense!"
        #elif May.party[eCurrPoke].currPDef == May.party[eCurrPoke].pDef - 6:
        #    "You can't lower your opponents defense anymore!"

    if Red.party[currPoke].isCrit == True:
        call .fight
        "Critical strike!"
    if Red.party[currPoke].dmgMod > 1:
        call .fight
        play audio "/se/supereffective.ogg"
        "It's super effective!"
    if Red.party[currPoke].dmgMod < 1 and Red.party[currPoke].dmgMod != 0:
        call .fight
        play audio "/se/notveryeffective.ogg"
        "It's not very effective..."
    if Red.party[currPoke].dmgMod == 1:
        play audio "/se/normaldamage.ogg"
        call .fight
        

        
    $ checkEHP = May.party[eCurrPoke].currHP    
    if checkEHP < 1:
        $ ehp = 0
        call .fight
        "Enemy [ename] fainted!"
        hide enemyPokemon
        $ May.knockOut(eCurrPoke)
        $ enemyPoke = May.numPoke()
        
        if enemyPoke > 0:
            $ ename = May.party[eCurrPoke].name
            "May: Go, [ename]!"
            call .pokemon
            jump .battle
        else:
            call .e_defeat
        
    if speedTest == True and switched == False:
        jump .enemyAttack
    else:
        jump .endTurn
        
        
# May Attack        
label .enemyAttack:
    call .fight
    if May.party[eCurrPoke].status == 1:
        $ wokenup = May.party[eCurrPoke].sleep()
        $ print(wokenup)
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
            
    $ numMoves = len(May.party[eCurrPoke].moves) - 1
    $ pickedMove = randint(0, numMoves)
    
    $ pEnemyType1 = Red.party[currPoke].type1
    $ pEnemyType2 = Red.party[currPoke].type2
    
    $ aEnemyType1 = Leaf.party[aCurrPoke].type1
    $ aEnemyType2 = Leaf.party[aCurrPoke].type2
    
    # battle_chart[moveType][targetType1]
    
    python:
        for i in range(len(May.party[eCurrPoke].moves)):
            dmg = battle_chart[May.party[eCurrPoke].moves[i]][pEnemyType1]
            dmg *= battle_chart[May.party[eCurrPoke].moves[i]][pEnemyType2]
            if dmg > 2:
                print("blah blah blah")
                # set move as priority move
    
    
        
    
    $ move = pickedMove = randint(0, numMoves)
    
    python:
        while 1:
            if May.party[eCurrPoke].moves[pickedMove].effect == 0:
                break
            elif Red.party[currPoke].currPDef > Red.party[currPoke].pDef - 6 and May.party[eCurrPoke].moves[pickedMove].effect == 1:
                break
            else:
                pickedMove = randint(0, numMoves)
                
                
    $ skill = May.party[eCurrPoke].moves[pickedMove]
    $ skill_name = May.party[eCurrPoke].moves[pickedMove].name
    $ poke_name = May.party[eCurrPoke].name
    $ target = Red.party[currPoke]
    $ target_name = target.name
    
    "[poke_name] used [skill_name]!"
    if May.party[eCurrPoke].status == 5:
        $ froz = May.party[eCurrPoke].freeze()
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
    if May.party[eCurrPoke].status == 6:
        $ para = May.party[eCurrPoke].paralysis()
        if para == False:
            call .fight
            "[ename] is paralysed! It can't move!"
            if speedTest == True and switched == False:
                jump .endTurn
            else:
                jump .playerAttack
    $ May.party[eCurrPoke].attack(skill, target, "enem")
    if Red.party[currPoke].currHP > 0:
       $  php = Red.party[currPoke].currHP
       call .fight
    else:
        $ php = 0
        call .fight

    if May.party[eCurrPoke].moves[pickedMove].effect == 1:
        call .fight
        
        #if Red.party[currPoke].currPDef >= Red.party[currPoke].pDef - 6:
        #    "Your opponent lowered your defense!"
        #elif Red.party[currPoke].currPDef == Red.party[currPoke].pDef - 7:
        #    "Your defense can't go any lower!"

    if May.party[eCurrPoke].isCrit == True:
        call .fight
        "Critical strike!"
    if May.party[eCurrPoke].dmgMod > 1:
        call .fight
        play audio "/se/supereffective.ogg"
        "It's super effective!"
    if May.party[eCurrPoke].dmgMod < 1 and May.party[eCurrPoke].dmgMod != 0:
        call .fight
        play audio "/se/notveryeffective.ogg"
        "It's not very effective..."
    if May.party[eCurrPoke].dmgMod == 1:
        call .fight
        play audio "/se/normaldamage.ogg"
        
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
        
    if speedTest == True:
        jump .endTurn
    elif speedTest == False and switched == False:
        jump .playerAttack
    elif speedTest == False and switched == True:
        jump .endTurn

label .endTurn:
    if Red.party[currPoke].status == 2:
        call .fight
        "[pname] is inflicted by poison!"
        $ Red.party[currPoke].poison()
    if Red.party[currPoke].status == 3:
        call .fight
        "[pname] is inflicted by burn!"
        $ Red.party[currPoke].burn()
    if Red.party[currPoke].status == 4:
        call .fight
        "[pname] is badly poisoned!"
        $ Red.party[currPoke].toxic()
    if Red.party[currPoke].status == 6:
        $ Red.party[currPoke].currSpeed *= .5

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
  
    if May.party[eCurrPoke].status == 2:
        call .fight
        "[ename] is inflicted by poison!"
        $ May.party[eCurrPoke].poison()
    if May.party[eCurrPoke].status == 3:
        call .fight
        "[ename] is inflicted by burn!"
        $ May.party[eCurrPoke].burn()
    if May.party[eCurrPoke].status == 4:
        call .fight
        "[ename] is badly poisoned!"
        $ May.party[eCurrPoke].toxic()
    if May.party[eCurrPoke].status == 6:
        $ May.party[eCurrPoke].currSpeed *= .5

    $ checkEHP = May.party[eCurrPoke].currHP    
    if checkEHP < 1:
        $ ehp = 0
        call .fight
        "Enemy [ename] fainted!"
        hide enemyPokemon
        $ May.knockOut(eCurrPoke)
        $ enemyPoke = May.numPoke()
        
        if enemyPoke > 0:
            $ ename = May.party[eCurrPoke].name
            "May: Go, [ename]!"
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
    $ switched = True
    call .fight
    $ pokeImagePath = "/images/" + Red.party[currPoke].name + ".png"
    image playerPokemon:
        xalign .02
        yalign .02
        xpos 15
        ypos 180
        pokeImagePath
    show playerPokemon
    call .fight
