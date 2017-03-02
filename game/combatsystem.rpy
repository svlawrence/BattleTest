init 1 python:
    #import Objects
    #from random import randint
    #from random import uniform
    
    #Declarations. Ideally you would set these early in the game. Not completely done.
    Tackle = Moves("Tackle", 35, 0, 0, 35, 100, 0)
    Tail_Whip = Moves("Tail Whip", 35, 0, 0, 0, 100, 1)
    Charmander = Pokemon("Charmander", 1, 18, 10, 21, 21, 11, 13, 11, 13, 11, 0)
    Bulbasaur = Pokemon("Bulbasaur", 4, 18, 10, 21, 21, 11, 13, 11, 13, 11, 0)
    Squirtle = Pokemon("Squirtle", 2, 18, 5, 20, 20, 11, 11, 13, 12, 10, 0)
    Red = Trainer("Red", 1)
    Blue = Trainer("Blue", 2)
    
    Red.catchMember(Charmander)
    Blue.catchMember(Squirtle)

    
    Red.party[0].addMove(Tackle)
    Red.party[0].addMove(Tail_Whip)
    Blue.party[0].addMove(Tackle)
    Blue.party[0].addMove(Tail_Whip)
    
    numPoke = Red.numPoke()
    
    eCurrPoke = 0
 
    def stats_frame(name, level, hp, maxhp, **properties):

        ui.frame(xfill=False, yminimum=None, **properties)

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
        jump Pokemon
    else:
        $ php = Red.party[currPoke].currHP
        $ ehp = Blue.party[currPoke].currHP
        
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
            #$ skill_1 = Move1.name
            #$ skill_2 = Move2.name
            
        if ehp != 0:
            $ ename = Blue.party[eCurrPoke].name
            $ elevel = Blue.party[eCurrPoke].lvl
            $ emaxhp = Blue.party[eCurrPoke].maxHP
            
        #$ skill_1 = Red.party[currPoke].moves[0];
        #$ skill_2 = Red.party[currPoke].moves[1];
            
label battle:
    call fight
    $ combat_turn += 1
    $ skillChoice = len(Red.party[currPoke].moves)
    $ numSkill = 0
    
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
                    $ numSkill = 1
                "[skill2_name]" if skillChoice >= 2:
                    $ numSkill = 2
                "[skill3_name]" if skillChoice >= 3:
                    $ numSkill = 3
                "[skill4_name]" if skillChoice >= 4:
                    $ numSkill = 4
                     
            jump use_skill
                 
label use_skill:
    call fight
    if numSkill == 1:
        "[pname] used [skill1_name]!"
        $ Red.party[currPoke].attack(Red.party[currPoke].moves[0], Blue.party[currPoke])
    elif numSkill == 2:
        "[pname] used [skill2_name]!"
        $ Red.party[currPoke].attack(Red.party[currPoke].moves[1], Blue.party[currPoke])

    if Red.party[currPoke].isCrit == True:
        call pokemon
        "Critical strike!"
    if Red.party[currPoke].dmgMod > 1:
        call pokemon
        "It's super effective!"

        
    $ checkEHP = Blue.party[currPoke].currHP    
    if checkEHP <= 0:
        $ ehp = 0
        call fight
        "Enemy [ename] fainted!"
        call enemyHideImage
        scene black with dissolve
        centered "You win!"
        $ renpy.full_restart()
        
    call pokemon    
    jump battle
    
label hideImage:
    hide playerPokemon

label enemyHideImage:
    hide enemyPokemon