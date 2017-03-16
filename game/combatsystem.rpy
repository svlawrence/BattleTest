init 1 python:
    
    #Declarations. Ideally you would set these early in the game. Not completely done.
    Tackle = Moves("Tackle", 35, 0, 0, 35, 100, 0)
    Tail_Whip = Moves("Tail Whip", 35, 0, 0, 0, 100, 1)
    Bubble = Moves("Bubble", 35, 2, 1, 40, 100, 0)
    Charmander = Pokemon("Charmander", 1, 18, 5, 21, 21, 11, 13, 11, 13, 11, 0, 3)
    Bulbasaur = Pokemon("Bulbasaur", 4, 18, 5, 21, 21, 11, 13, 11, 13, 11, 0, 3)
    Squirtle = Pokemon("Squirtle", 2, 18, 5, 20, 20, 11, 11, 13, 12, 10, 0, 100)
    Red = Trainer("Red", 1)
    Blue = Trainer("Blue", 0)
    
    # Catching members. Ignore for now
    Red.catchMember(Charmander)
    Blue.catchMember(Squirtle)

    # Giving pokemon moves
    Red.party[0].addMove(Tackle)
    Red.party[0].addMove(Tail_Whip)
    Blue.party[0].addMove(Tackle)
    Blue.party[0].addMove(Tail_Whip)
    Blue.party[0].addMove(Bubble)
    
    # Number of pokemon in Red's party.
    
    # Setting index for Blue's pokemon
    eCurrPoke = 0
    
    def face_frame(img, **properties):
        ui.frame(xfill=False, yminimum=0, **properties)
        ui.image(img,**properties)

    combat_turn = 0
    
    Red.pokeBalls = 3
    Red.greatBalls = 2
    Red.ultraBalls = 1

label splash:

    $ renpy.music.queue("music/battle/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0)
    $ renpy.music.queue("music/battle/KantoTrainerLoop_Rock.ogg", channel='music', loop=True)
    $ numPoke = Red.numPoke()
    image Red_Splash:
        #xpos .20
        ypos 750
        zoom .75
        "/images/red_casual_1024.png"
    
    image Enemy_Splash:
        xpos .80
        ypos 750
        zoom .75
        "/images/blue_casual_1024.png"
        
    image versus:
        ypos 600
        "images/versus.png"
        
    show Red_Splash:
        xalign -1 yalign 1.0
        ease 0.5 xalign -.1
    show Enemy_Splash:
        xalign 2.0 yalign 1.0
        ease 0.5 xalign 1.0
    pause 0.5
    show versus:
        xalign 0.5 yalign -0.5
        ease 0.5 yalign 0.5
    pause 1
    
    hide Red_Splash
    hide Enemy_Splash
    hide versus
    call combat

label combat:
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
        jump pokemon

# Frame update
label fight:

    # Player Stats Frame
    $ stats_frame(pname, plevel, php, pmaxhp, xalign=.17, yalign=.7)
    if Red.party[currPoke].currHP >= round(Red.party[currPoke].maxHP * .75):
        $ face_frame("/images/Portraits/Red Square Casual Happy.png", xalign = 0.02, yalign=.653, zoom=.25)
    if Red.party[currPoke].currHP <= round(Red.party[currPoke].maxHP * .75) and Red.party[currPoke].currHP > Red.party[currPoke].maxHP * .25:
        $ face_frame("/images/Portraits/Red Square Casual Neutral.png", xalign = 0.02, yalign=.653, zoom=.25)
    elif Red.party[currPoke].currHP <= round(Red.party[currPoke].maxHP * .25):
        $ face_frame("/images/Portraits/Red Square Casual Worried.png", xalign = 0.02, yalign=.653, zoom=.25)
    
        
    # Enemy Stats Frame
    $ stats_frame(ename, elevel, ehp, emaxhp, xalign=.83, yalign=.7)
    $ face_frame("/images/Portraits/Blue Square Casual Neutral.png", xalign = 0.98, yalign=.653)
    return
        
# Pokemon update label
label pokemon:
    $ php = Red.party[currPoke].currHP
    $ ehp = Blue.party[eCurrPoke].currHP
    $ pokeImagePath = "/images/" + Red.party[currPoke].name + ".png"
    $ eImagePath = "/images/" + Blue.party[eCurrPoke].name + ".png"
    
    image playerPokemon:
        xalign .02
        yalign .02
        xpos 15
        ypos 180
        pokeImagePath
    show playerPokemon
        
    image enemyPokemon:
        xalign .02
        yalign .02
        xpos 1000
        ypos 180
        eImagePath
    show enemyPokemon
        
    if php != 0:
        $ pname = Red.party[currPoke].name
        $ plevel = Red.party[currPoke].lvl
        $ pmaxhp = Red.party[currPoke].maxHP
        
    if ehp != 0:
        $ ename = Blue.party[eCurrPoke].name
        $ elevel = Blue.party[eCurrPoke].lvl
        $ emaxhp = Blue.party[eCurrPoke].maxHP
            
            
label battle:
    call fight
    $ combat_turn += 1
    $ skillChoice = len(Red.party[currPoke].moves)
    $ numSkill = 0
    $ speedTest = Red.party[currPoke].checkSpeed(Blue.party[eCurrPoke])
    $ switched = False
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
            call fight
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
                    jump battle
            if speedTest == True:
                jump playerAttack
            elif speedTest == False:
                jump enemyAttack
        "Switch":
            menu:
                "[Red.party[0].name]" if numPoke >= 1 and Red.party[0] != Red.party[currPoke]:
                    call fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 0
                    call switch
                    "[Red.name]: Go, [pname]!"
                    jump enemyAttack
                "[Red.party[1].name]" if numPoke >= 2 and Red.party[1] != Red.party[currPoke]:
                    call fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 1
                    call switch
                    "[Red.name]: Go, [pname]!"
                    jump enemyAttack
                "[Red.party[2].name]" if numPoke >= 3 and Red.party[2] != Red.party[currPoke]:
                    call fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 2
                    call switch
                    "[Red.name]: Go, [pname]!"
                    jump enemyAttack
                "[Red.party[3].name]" if numPoke >= 4 and Red.party[3] != Red.party[currPoke]:
                    call fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 3
                    call switch
                    "[Red.name]: Go, [pname]!"
                    jump enemyAttack
                "[Red.party[4].name]" if numPoke >= 5 and Red.party[4] != Red.party[currPoke]:
                    call fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 4
                    call switch
                    "[Red.name]: Go, [pname]!"
                    jump enemyAttack
                "[Red.party[5].name]" if numPoke == 6 and Red.party[5] != Red.party[currPoke]:
                    call fight
                    hide playerPokemon
                    "[Red.name]: [pname], come back!"
                    $ currPoke = 5
                    call switch
                    "[Red.name]: Go, [pname]!"
                    jump enemyAttack
                "Back":
                    jump battle
            call fight
            jump enemyAttack
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
                    jump battle
            $ attemptCatch = Red.tryCatch(Blue.party[eCurrPoke].status, Blue.party[eCurrPoke].currHP, Blue.party[eCurrPoke].maxHP, Blue.party[eCurrPoke].catchRate, bonus)
            if attemptCatch == True:
                 $ switched = True
                 $ Red.catchMember(Squirtle)
                 $ print(len(Red.party))
                 "You caught the Pokemon!"
                 jump e_defeat
            else:
                 $ switched = True
                 "Darn! Didn't catch it!"
                 jump enemyAttack


label hideImage:
    hide playerPokemon

label enemyHideImage:
    hide enemyPokemon
    
label e_defeat:
     scene black with dissolve
     centered "You win!"
     $  Red.partyHeal()
     $  Blue.partyHeal()
     $  renpy.full_restart()

label p_defeat:
     scene black with dissolve
     centered "You lose!"
     $  Red.partyHeal()
     $  Blue.partyHeal()
     $ renpy.full_restart()     
     
label playerAttack:
    call fight
    $ skill_name = Red.party[currPoke].moves[numSkill].name
    $ face_frame("/images/Portraits/Red Square Casual Attacking.png", xalign = 0.02, yalign=.653, zoom=.25)
    "[pname] used [skill_name]!"
    $ Red.party[currPoke].attack(Red.party[currPoke].moves[numSkill], Blue.party[eCurrPoke])
    if Blue.party[eCurrPoke].currHP > 0:
        $ ehp = Blue.party[eCurrPoke].currHP
        call fight
    else:
        $ ehp = 0
        call fight
        
    if Red.party[currPoke].moves[numSkill].effect == 1:
        call fight
        if Blue.party[eCurrPoke].currPDef > Blue.party[eCurrPoke].pDef - 6:
            "You lowered your opponents defense!"
        elif Blue.party[eCurrPoke].currPDef == Blue.party[eCurrPoke].pDef - 6:
            "You can't lower your opponents defense anymore!"

    if Red.party[currPoke].isCrit == True:
        call fight
        "Critical strike!"
    if Red.party[currPoke].dmgMod > 1:
        call fight
        "It's super effective!"

        
    $ checkEHP = Blue.party[eCurrPoke].currHP    
    if checkEHP <= 0:
        $ ehp = 0
        call fight
        "Enemy [ename] fainted!"
        hide enemyPokemon
        $ Blue.knockOut(eCurrPoke)
        $ enemyPoke = Blue.numPoke()
        
        if enemyPoke > 0:
            $ ename = Blue.party[eCurrPoke].name
            "Blue: Go, [ename]!"
            call pokemon
            jump battle
        else:
            call e_defeat
        
    if speedTest == True and switched == False:
        $print (switched)
        jump enemyAttack
    else:
        call pokemon
        jump battle
        
label enemyAttack:
    call fight
    
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
    $ skill = Blue.party[eCurrPoke].moves[pickedMove]
    $ skill_name = Blue.party[eCurrPoke].moves[pickedMove].name
    $ poke_name = Blue.party[eCurrPoke].name
    $ target = Red.party[currPoke]
    $ target_name = target.name
    
    "[poke_name] used [skill_name]!"
    $ Blue.party[eCurrPoke].attack(skill, target)
    if Red.party[currPoke].currHP > 0:
       $  php = Red.party[currPoke].currHP
       call fight
    else:
        $ php = 0
        call fight

    if Blue.party[eCurrPoke].moves[pickedMove].effect == 1:
        call fight
        if Red.party[currPoke].currPDef >= Red.party[currPoke].pDef - 6:
            "Your opponent lowered your defense!"
        elif Red.party[currPoke].currPDef == Red.party[currPoke].pDef - 7:
            "Your defense can't go any lower!"

    if Blue.party[eCurrPoke].isCrit == True:
        call fight
        "Critical strike!"
    if Blue.party[eCurrPoke].dmgMod > 1:
        call fight
        "It's super effective!"
        
    $ checkPHP = Red.party[currPoke].currHP    
    if checkPHP <= 0:
        $ php = 0
        call fight
        "[target_name] fainted!"
        hide playerPokemon
        $ Red.knockOut(currPoke)
        $ numPoke = Red.numPoke()
        if numPoke > 0:
            $ combat_turn = 0
            jump combat
        else:
            call p_defeat
        
    if speedTest == True:
        $ print (speedTest)
        call pokemon
        jump battle
    elif speedTest == False and switched == False:
        jump playerAttack
    elif speedTest == False and switched == True:
        call pokemon
        jump battle
        
label switch:
    $ pname = Red.party[currPoke].name
    $ plevel = Red.party[currPoke].lvl
    $ pmaxhp = Red.party[currPoke].maxHP
    $ php = Red.party[currPoke].currHP
    $ switched = True
    call fight
    $ pokeImagePath = "/images/" + Red.party[currPoke].name + ".png"
    image playerPokemon:
        xalign .02
        yalign .02
        xpos 15
        ypos 180
        pokeImagePath
    show playerPokemon
    call fight
