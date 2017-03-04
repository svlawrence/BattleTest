init 1 python:
    
    #Declarations. Ideally you would set these early in the game. Not completely done.
    Tackle = Moves("Tackle", 35, 0, 0, 35, 100, 0)
    Tail_Whip = Moves("Tail Whip", 35, 0, 0, 0, 100, 1)
    Charmander = Pokemon("Charmander", 1, 18, 5, 21, 21, 11, 13, 11, 13, 11, 0)
    Bulbasaur = Pokemon("Bulbasaur", 4, 18, 5, 21, 21, 11, 13, 11, 13, 11, 0)
    Squirtle = Pokemon("Squirtle", 2, 18, 5, 20, 20, 11, 11, 13, 12, 10, 0)
    Red = Trainer("Red", 1)
    Blue = Trainer("Blue", 2)
    
    Red.catchMember(Charmander)
    Red.catchMember(Squirtle)
    Blue.catchMember(Squirtle)
    Blue.catchMember(Charmander)

    
    Red.party[0].addMove(Tackle)
    Red.party[0].addMove(Tail_Whip)
    Red.party[1].addMove(Tackle)
    Red.party[1].addMove(Tail_Whip)
    Blue.party[0].addMove(Tackle)
    Blue.party[0].addMove(Tail_Whip)
    Blue.party[1].addMove(Tackle)
    Blue.party[1].addMove(Tail_Whip)
    
    numPoke = Red.numPoke()
    
    eCurrPoke = 0
 
    def stats_frame(name, level, hp, maxhp, **properties):

        ui.frame(xfill=False, xpadding=100, yminimum=None, **properties)

        ui.hbox() # (name, "HP", bar) from (level, hp, maxhp)
        ui.vbox() # name from ("HP", bar)

        ui.text(name, size=20)

        ui.hbox() # "HP" from bar
        ui.text("HP", size=20)
        ui.bar(maxhp, hp,
               xmaximum=150)

        ui.close()
        ui.close()

        ui.vbox() # Level from (hp/maxhp)

        ui.text("Lv. %d" % level, xalign=0.5, size=20)
        ui.text("%d/%d" % (hp, maxhp), xalign=0.5, size=20)

        ui.close()
        ui.close()
init:
    $ combat_turn = 0
    
    $ pauseGame = False
    
label combat:
    $ iter = 0

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

label fight:

    # Player Stats Frame
    $ stats_frame(pname, plevel, php, pmaxhp, xalign=.02, yalign=.7)
        
    # Enemy Stats Frame
    $ stats_frame(ename, elevel, ehp, emaxhp, xalign=.98, yalign=.7)
    return
        
label pokemon:
    
    if pauseGame:
        $ pauseGame = False
    #    jump pokemon
    else:
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
                "Back":
                    jump battle
            $ pokeImagePath = "/images/" + Red.party[currPoke].name + ".png"
            image playerPokemon:
                xalign .02
                yalign .02
                xpos 15
                ypos 180
                pokeImagePath
            show playerPokemon
            $pname = Red.party[currPoke].name
            $plevel = Red.party[currPoke].lvl
            $php = Red.party[currPoke].currHP
            call fight
            jump enemyAttack
           


label hideImage:
    hide playerPokemon

label enemyHideImage:
    hide enemyPokemon
    
label e_defeat:
     scene black with dissolve
     centered "You win!"
     $ renpy.full_restart()

label p_defeat:
     scene black with dissolve
     centered "You lose!"
     $ renpy.full_restart()     
     
label playerAttack:
    call fight
    $ skill_name = Red.party[currPoke].moves[numSkill].name
    "[pname] used [skill_name]!"
    $ Red.party[currPoke].attack(Red.party[currPoke].moves[numSkill], Blue.party[eCurrPoke])
        
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
        #call e_defeat
        
        if enemyPoke > 0:
            call pokemon
            jump battle
        else:
            call e_defeat
        
    if speedTest == True:
        jump enemyAttack
    elif speedTest == False:
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
        call pokemon
        jump battle
    elif speedTest == False:
        jump playerAttack
        


# Old function, replaced with player attack and enemy attack        
label use_skill:
    call fight
    $ skill_name = Red.party[currPoke].moves[numSkill].name
    "[pname] used [skill_name]!"
    $ Red.party[currPoke].attack(Red.party[currPoke].moves[numSkill], Blue.party[currPoke])
        
    if Red.party[currPoke].moves[numSkill].effect == 1:
        call fight
        if Blue.party[currPoke].currPDef > Blue.party[currPoke].pDef - 6:
            "You lowered your opponents defense!"
        elif Blue.party[currPoke].currPDef == Blue.party[currPoke].pDef - 6:
            "You can't lower your opponents defense anymore!"

    if Red.party[currPoke].isCrit == True:
        call fight
        "Critical strike!"
    if Red.party[currPoke].dmgMod > 1:
        call fight
        "It's super effective!"

        
    #$ checkEHP = Blue.party[currPoke].currHP    
    #if checkEHP <= 0:
    #    $ ehp = 0
    #    call fight
    #    "Enemy [ename] fainted!"
    #    call enemyHideImage
    #    call e_defeat
        
    call pokemon
