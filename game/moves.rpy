init -997 python:
    
# NORMAL
    Body_Slam = Moves("Body Slam", 0, 0, 60, 100, 26) # 30% chance Paralyze
    Boomburst = Moves("Boomburst", 0, 1, 140, 100, 0, 1) # Multi-target
    Crush_Claw = Moves("Crush Claw", 0, 0, 75, 95, 1) # 50% chance -1 Def
    Cut = Moves("Cut", 0, 0, 50, 95, 0)
    Defense_Curl = Moves("Defense Curl", 0, 0, 0, 100, 11) # Self +1 Def
    Dizzy_Punch = Moves("Dizzy Punch", 0, 0, 70, 100, 0) # 20% chance Confuse
    Double_Team = Moves("Double Team", 0, 0, 0, 100, 0) # +1 Evasion
    Double_Edge = Moves("Double Edge", 0, 0, 120, 100, 0) # Recoil damage
    Explosion = Moves("Explosion", 0, 0, 250, 100, 0, 1) # Multi-target / KO Self
    Extreme_Speed = Moves("Extreme Speed", 0, 0, 80, 100, 0) # Priority
    Facade = Moves("Facade", 0, 0, 70, 100, 0) # Double damage if under status effect
    Flash = Moves("Flash", 0, 0, 0, 100, 0) # -1 Accuracy
    Giga_Impact = Moves("Giga Impact", 0, 130, 90, 100, 0)
    Glare = Moves("Glare", 0, 0, 0, 100, 26) # Paralyze
    Growl = Moves("Growl", 0, 0, 0, 100, 2, 1) # Multi-target / -1 Atk
    Harden = Moves("Harden", 0, 0, 0, 100, 11) # Self +1 Def
    Head_Charge = Moves("Head Charge", 0, 0, 120, 100, 0) # Recoil damage
    Headbutt = Moves("Headbutt", 0, 0, 70, 100, 0) # 30% chance Flinch
    Horn_Attack = Moves("Horn Attack", 0, 0, 65, 100, 0)
    Hyper_Beam = Moves("Hyper Beam", 0, 1, 150, 90, 0)
    Hyper_Voice = Moves("Hyper Voice", 0, 1, 90, 100, 0) # Multi-target
    Leer = Moves("Leer", 0, 0, 0, 100, 1) # Multi-target / -1 Def
    Lovely_Kiss = Moves("Lovely Kiss", 0, 0, 0, 75, 21) # Sleep
    Mega_Kick = Moves("Mega Kick", 0, 0, 120, 75, 0)
    Mega_Punch = Moves("Mega Punch", 0, 0, 90, 85, 0)
    Morning_Sun = Moves("Morning Sun", 0, 0, 0, 100, 0) # 50% max life recovery
    Pound = Moves("Pound", 0, 0, 40, 100, 0)
    Quick_Attack = Moves("Quick Attack", 0, 0, 40, 100, 0) # Priority
    Razor_Wind = Moves("Razor Wind", 0, 1, 80, 100, 0) # Nulti-target / Decreased Priority
    Recover = Moves("Recover", 0, 0, 0, 100, 0) # 50% max life recovery
    Refresh = Moves("Refresh", 0, 0, 0, 100, 0) # Removes status effect
    Scary_Face = Moves("Scary Face", 0, 0, 0, 100, 10) # -2 Spd
    Scratch = Moves("Scratch", 0, 0, 40, 100, 0)
    Screech = Moves("Screech", 0, 0, 0, 85, 6) # -2 Def
    Self_Destruct = Moves("Self-Destruct", 0, 0, 200, 100, 0) # Multi-target / KO Self
    Sing = Moves("Sing", 0, 0, 0, 55, 21) # Sleep
    Skull_Bash = Moves("Skull Bash", 0, 0, 130, 100, 0) # Decreased Priority
    Slack_Off = Moves("Slack Off", 0, 0, 0, 100, 0) # 50$ max life recovery
    Slam = Moves("Slam", 0, 0, 80, 75, 0)
    Slash = Moves("Slash", 0, 0, 70, 100, 0) # Higher crit (12.5%)
    Smokescreen = Moves("Smokescreen", 0, 0, 0, 100, 0) # -1 Accuracy
    Sonic_Boom = Moves("Sonic Boom", 0, 1, 0, 100, 0) # Always 20 Damage
    Splash = Moves("Splash", 0, 0, 0, 100, 0) # "But nothing happened..."
    Stomp = Moves("Stomp", 0, 0, 65, 100, 0) # 30% chance Flinch
    Supersonic = Moves("Supersonic", 0, 0, 0, 55, 0) # Confuse
    Swift = Moves("Swift", 0, 1, 60, 100, 0) # Multi-target / Never misses
    Swords_Dance = Moves("Swords Dance", 0, 0, 0, 100, 17) # Self +2 Atk
    Tackle = Moves("Tackle", 0, 0, 40, 100, 0)
    Tail_Whip = Moves("Tail Whip", 0, 0, 0, 100, 1) # -1 Def
    Take_Down = Moves("Take Down", 0, 0, 90, 85, 0) # Recoil damage
    Teeter_Dance = Moves("Teeter Dance", 0, 0, 0, 100, 0) # Multi-target / Confuse
    Thrash = Moves("Thrash", 0, 0, 120, 100, 0) # Self Confuse
    Vice_Grip = Moves("Vice Grip", 0, 0, 55, 100, 0)

# FIRE
    Blast_Burn = Moves("Blast Burn", 1, 1, 150, 90, 0)
    Blaze_Kick = Moves("Blaze Kick", 1, 0, 85, 90, 23) # 10% chance Burn
    Ember = Moves("Ember", 1, 1, 40, 100, 23) # 10% chance Burn
    Fire_Blast = Moves("Fire Blast", 1, 1, 110, 85, 23) # 30% chance Burn
    Fire_Fang = Moves("Fire Fang", 1, 0, 65, 95, 23) # 10% chance Burn / 10% chance Flinch
    Fire_Punch = Moves("Fire Punch", 1, 0, 75, 100, 23) # 10% chance Burn
    Flame_Charge = Moves("Flame Charge", 1, 0, 50, 100, 15) # Self +1 Spd
    Flame_Wheel = Moves("Flame Wheel", 1, 0, 60, 100, 23) # 10% chance Burn
    Flamethrower = Moves("Flamethrower", 1, 1, 90, 100, 23) # 10% chance Burn
    Flare_Blitz = Moves("Flare Blitz", 1, 0, 120, 100, 23) # 10% chance Burn / Recoil damage
    Heat_Wave = Moves("Heat Wave", 1, 1, 95, 90, 23) # Multi-target / 10% chance Burn
    Incinerate = Moves("Incinerate", 1, 1, 60, 100, 0) # Multi-target
    Inferno = Moves("Inferno", 1, 1, 100, 50, 23) # Burn
    Lava_Plume = Moves("Lava Plume", 1, 1, 80, 100, 23) # Multi-target / 30% chance Burn
    Mystical_Fire = Moves("Mystical Fire", 1, 1, 75, 100, 4) # -1 S. Atk
    Will_O_Wisp = Moves("Will-O-Wisp", 1, 0, 0, 85, 23) # Burn

# WATER
    Aqua_Jet = Moves("Aqua Jet", 2, 0, 40, 100, 0) # Priority
    Aqua_Tail = Moves("Aqua Tail", 2, 0, 90, 90, 0)
    Bubble = Moves("Bubble", 2, 1, 40, 100, 5, 1) # Multi-target / 10% chance -1 Spd
    Bubble_Beam = Moves("Bubble Beam", 2, 1, 65, 100, 5) # 10% chance -1 Spd
    Crabhammer = Moves("Crabhammer", 2, 0, 100, 90, 0) # Higher crit (12.5%)
    Hydro_Cannon = Moves("Hydro Cannon", 2, 1, 150, 90, 0)
    Hydro_Pump = Moves("Hydro Pump", 2, 1, 110, 80, 0)
    Muddy_Water = Moves("Muddy Water", 2, 1, 90, 85, 0) # Multi-target
    Razor_Shell = Moves("Razor Shell", 2, 0, 75, 90, 1) # 50% chance -1 Def
    Scald = Moves("Scald", 2, 1, 80, 100, 23) # 30% chance Burn / 100% Defrost
    Surf = Moves("Surf", 2, 1, 90, 100, 0) # Multi-target
    Water_Gun = Moves("Water Gun", 2, 1, 40, 100, 0)
    Water_Pulse = Moves("Water Pulse", 2, 1, 60, 100, 0) # 20% chance Confuse
    Water_Shuriken = Moves("Water Shuriken", 2, 0, 75, 100, 0) # Priority / Greninja ONLY
    Waterfall = Moves("Waterfall", 2, 0, 80, 100, 0) # 20% chance Flinch
    Withdraw = Moves("Withdraw", 2, 0, 0, 100, 11) # Self +1 Def
    
# ELECTRIC
    Charge_Beam = Moves("Charge Beam", 3, 1, 50, 90, 14) # 70% chance Self +1 S. Atk
    Discharge = Moves("Discharge", 3, 1, 80, 90, 26) # Multi-target / 30% chance Paralyze
    Nuzzle = Moves("Nuzzle", 3, 0, 20, 100, 26) # Paralyze
    Shock_Wave = Moves("Shock Wave", 3, 1, 60, 100, 0) # Never misses
    Spark = Moves("Spark", 3, 0, 65, 100, 26) # 30% chance Paralyze
    Thunder = Moves("Thunder", 3, 1, 110, 70, 26) # 30% chance Paralyze
    Thunder_Fang = Moves("Thunder Fang", 3, 0, 65, 95, 26) # 10% chance Paralyze / 10% chance Flinch
    Thunder_Punch = Moves("Thunder Punch", 3, 0, 75, 100, 26) # 10% chance Paralyze
    Thunder_Shock = Moves("Thunder Shock", 3, 1, 40, 100, 26) # 10% chance Paralyze
    Thunder_Wave = Moves("Thunder Wave", 3, 0, 0, 100, 26) # Paralyze
    Thunderbolt = Moves("Thunderbolt", 3, 1, 90, 100, 26) # 10% chance Paralyze
    Volt_Tackle = Moves("Volt Tackle", 3, 0, 120, 100, 26) # 10% chance Paralyze / Recoil damage / Pikachu ONLY
    Wild_Charge = Moves("Wild Charge", 3, 0, 90, 100, 0) # Recoil damage
    Zap_Cannon = Moves("Zap Cannon", 3, 1, 120, 50, 26) # Paralyze
    
# GRASS
    Absorb = Moves("Absorb", 4, 1, 20, 100, 0) # Life draining
    Cotton_Guard = Moves("Cotton Guard", 4, 0, 0, 100, 16) # Self +2 Def
    Cotton_Spore = Moves("Cotton Spore", 4, 0, 0, 100, 10) # Multi-target / -2 Spd
    Energy_Ball = Moves("Energy Ball", 4, 1, 90, 100, 3) # 10% chance -1 S. Def
    Frenzy_Plant = Moves("Frenzy Plant", 4, 1, 150, 90, 0)
    Giga_Drain = Moves("Giga Drain", 4, 1, 75, 100, 0) # Life draining
    Grass_Whistle = Moves("Grass Whistle", 4, 0, 0, 55, 21) # Sleep
    Horn_Leech = Moves("Horn Leech", 4, 0, 75, 100, 0) # Life draining
    Leaf_Blade = Moves("Leaf Blade", 4, 0, 90, 100, 0) # Higher crit (12.5%)
    Leaf_Tornado = Moves("Leaf Tornado", 4, 1, 65, 90, 0) # 50% chance -1 Accuracy
    Magical_Leaf = Moves("Magical Leaf", 4, 1, 60, 100, 0) # Never misses
    Mega_Drain = Moves("Mega Drain", 4, 1, 40, 100, 0) # Life draining
    Petal_Blizzard = Moves("Petal Blizzard", 4, 0, 90, 100, 0) # Multi-target
    Petal_Dance = Moves("Petal Dance", 4, 1, 120, 100, 0) # Self Confuse
    Power_Whip = Moves("Power Whip", 4, 0, 120, 85, 0)
    Razor_Leaf = Moves("Razor Leaf", 4, 0, 55, 95, 0) # Multi-target / Higher crit (12.5%)
    Seed_Bomb = Moves("Seed Bomb", 4, 0, 80, 100, 0)
    Sleep_Powder = Moves("Sleep Powder", 4, 0, 0, 75, 21) # Sleep
    Solar_Beam = Moves("Solar Beam", 4, 1, 120, 100, 0) # Decreased Priority
    Solar_Blade = Moves("Solar Blade", 4, 0, 125, 100, 0) # Decreased Priority / Lurantis ONLY
    Spore = Moves("Spore", 4, 0, 0, 100, 21) # Sleep
    Stun_Spore = Moves("Stun_Spore", 4, 0, 0, 75, 26) # Paralyze
    Synthesis = Moves("Synthesis", 4, 0, 0, 100, 0) # 50% max life recovery
    Vine_Whip = Moves("Vine Whip", 4, 0, 45, 100, 0)
    Wood_Hammer = Moves("Wood Hammer", 4, 0, 120, 100, 0) # Recoil damage
    
# ICE
    Aurora_Beam = Moves("Aurora Beam", 5, 1, 65, 100, 2) # 10% chance -1 Atk
    Blizzard = Moves("Blizzard", 5, 1, 110, 70, 25) # Multi-target / 10% chance Freeze
    Ice_Beam = Moves("Ice Beam", 5, 1, 90, 100, 25) # 10% chance Freeze
    Ice_Fang = Moves("Ice Fang", 5, 0, 65, 95, 25) # 10% chance Freeze / 10% chance Flinch
    Ice_Punch = Moves("Ice Punch", 5, 0, 75, 100, 25) # 10% chance Freeze
    Ice_Shard = Moves("Ice Shard", 5, 0, 40, 100, 0) # Priority
    Icicle_Crash = Moves("Icicle Crash", 5, 0, 85, 90, 0) # 30% chance Flinch
    Icy_Wind = Moves("Icy Wind", 5, 1, 55, 95, 5) # Multi-target / -1 Spd
    Powder_Snow = Moves("Powder Snow", 5, 1, 40, 100, 25) # 10% chance Freeze

# FIGHTING
    Aura_Sphere = Moves("Aura Sphere", 6, 1, 80, 100, 0) # Never misses
    Brick_Break = Moves("Brick Break", 6, 0, 75, 100, 0)
    Cross_Chop = Moves("Cross Chop", 6, 0, 100, 80, 0) # Higher crit (12.5%)
    Drain_Punch = Moves("Drain Punch", 6, 0, 75, 100, 0) # Life draining
    Dynamic_Punch = Moves("Dynamic Punch", 6, 0, 100, 50, 0) # Confuse
    Flying_Press = Moves("Flying Press", 6, 0, 100, 95, 0) # Hawlucha ONLY
    Focus_Blast = Moves("Focus Blast", 6, 1, 120, 70, 3) # 10% chance -1 S. Def
    Force_Palm = Moves("Force Palm", 6, 0, 60, 100, 26) # 30% chance Paralyze
    High_Jump_Kick = Moves("High Jump Kick", 6, 0, 130, 90, 0) # note: 50% max life recoil damage if miss / if this is too difficult to do, then just normal recoil damage on hit
    Karate_Chop = Moves("Karate_Chop", 6, 0, 50, 100, 0) # Higher crit (12.5%)
    Low_Sweep = Moves("Low Sweep", 6, 0, 60, 100, 5) # -1 Spd
    Mach_Punch = Moves("Mach Punch", 6, 0, 40, 100, 0) # Priority
    Power_Up_Punch = Moves("Power-Up Punch", 6, 0, 40, 100, 12) # Self +1 Atk
    Rock_Smash = Moves("Rock Smash", 6, 0, 40, 100, 1) # 50% chance -1 Def
    Rolling_Kick = Moves("Rolling Kick", 6, 0, 60, 85, 0) # 30% chance Flinch
    Sky_Uppercut = Moves("Sky Uppercut", 6, 0, 85, 90, 0)
    Submission = Moves("Submission", 6, 0, 80, 80, 0) # Recoil damage
    Vacuum_Wave = Moves("Vacuum Wave", 6, 1, 40, 100, 0) # Priority
    
# POISON
    Acid = Moves("Acid", 7, 1, 40, 100, 3) # 10% chance -1 S. Def
    Acid_Armor = Moves("Acid Armor", 7, 0, 0, 100, 16) # Self +2 Def
    Acid_Spray = Moves("Acid Spray", 7, 1, 40, 100, 8) # -2 S. Def
    Cross_Poison = Moves("Cross Poison", 7, 0, 70, 100, 22) # 10% chance Poison / Higher crit (12.5%)
    Gunk_Shot = Moves("Gunk Shot", 7, 0, 120, 80, 22) # 30% chance Poison
    Poison_Fang = Moves("Poison Fang", 7, 0, 50, 100, 24) # 50% chance Bad Poison
    Poison_Gas = Moves("Poison Gas", 7, 0, 0, 90, 22) # Multi-target / Poison
    Poison_Jab = Moves("Poison Jab", 7, 0, 80, 100, 22) # 30% chance Poison
    Poison_Powder = Moves("Poison Powder", 7, 0, 0, 75, 22) # Poison
    Poison_Sting = Moves("Poison Sting", 7, 0, 15, 100, 22) # 30% chance Poison
    Poison_Tail = Moves("Poison Tail", 7, 0, 50, 100, 22) # 10% chance Poison / Higher crit (12.5%)
    Sludge = Moves("Sludge", 7, 1, 65, 100, 22) # 30% chance Poison
    Sludge_Bomb = Moves("Sludge Bomb", 7, 1, 90, 100, 22) # 30% chance Poison
    Sludge_Wave = Moves("Sludge Wave", 7, 1, 95, 100, 22) # Multi-target / 10% chance Poison
    Smog = Moves("Smog", 7, 1, 30, 70, 22) # 40% chance Poison
    Toxic = Moves("Toxic", 7, 0, 0, 90, 24) # Bad Poison
    Venoshock = Moves("Venoshock", 7, 1, 65, 100, 0) # Double damage to poisoned target
    
# GROUND
    Bulldoze = Moves("Bulldoze", 8, 0, 60, 100, 5) # Multi-target / -1 Spd
    Drill_Run = Moves("Drill Run", 8, 0, 80, 95, 0) # Higher crit (12.5%)
    Earth_Power = Moves("Earth Power", 8, 1, 90, 100, 3) # 10% chance -1 S. Def
    Earthquake = Moves("Earthquake", 8, 0, 100, 100, 0) # Multi-target
    High_Horsepower = Moves("High Horsepower", 8, 0, 95, 95, 0)
    Mud_Bomb = Moves("Mud Bomb", 8, 1, 65, 85, 0) # 30% chance -1 Accuracy
    Mud_Shot = Moves("Mud Shot", 8, 1, 55, 95, 5) # -1 Spd
    Mud_Slap = Moves("Mud-Slap", 8, 1, 20, 100, 0) # -1 Accuracy
    Sand_Attack = Moves("Sand Attack", 8, 0, 0, 100, 0) # -1 Accuracy

# FLYING
    Aerial_Ace = Moves("Aerial Ace", 9, 0, 60, 100, 0) # Never misses
    Air_Cutter = Moves("Air Cutter", 9, 1, 60, 95, 0) # Higher crit (12.5%)
    Air_Slash = Moves("Air Slash", 9, 1, 75, 95, 0) # 30% chance Flinch
    Beak_Blast = Moves("Beak Blast", 9, 0, 85, 90, 23) # 30% chance Burn / Decreased Priority
    Bounce = Moves("Bounce", 9, 0, 85, 90, 26) # 30% chance Paralyze / Decreased Priority
    Brave_Bird = Moves("Brave Bird", 9, 0, 120, 100, 0) # Recoil damage
    Drill_Peck = Moves("Drill Peck", 9, 0, 80, 100, 0)
    Feather_Dance = Moves("Feather Dance", 9, 0, 0, 100, 7) # -2 Atk
    Fly = Moves("Fly", 9, 0, 90, 100, 0) # Decreased Priority
    Gust = Moves("Gust", 9, 1, 40, 100, 0)
    Hurricane = Moves("Hurricane", 9, 1, 110, 70, 0) # 30% chance Confuse
    Peck = Moves("Peck", 9, 0, 35, 100, 0)
    Roost = Moves("Roost", 9, 0, 0, 100, 0) # 50% max life recovery
    Sky_Attack = Moves("Sky Attack", 9, 0, 140, 90, 0) # Decreased Priority
    Wing_Attack = Moves("Wing Attack", 9, 0, 60, 100, 0)
    
# PSYCHIC
    Agility = Moves("Agility", 10, 0, 0, 100, 20) # Self +2 Spd
    Amnesia = Moves("Amnesia", 10, 0, 0, 100, 18) # Self +2 S. Def
    Barrier = Moves("Barrier", 10, 0, 0, 100, 16) # Self +2 Def
    Confusion = Moves("Confusion", 10, 1, 50, 100, 0) # 10% chance Confuse
    Extrasensory = Moves("Extrasensory", 10, 1, 80, 100, 0) # 10% chance Flinch
    Hypnosis = Moves("Hypnosis", 10, 0, 0, 60, 21) # Sleep
    Meditate = Moves("Meditate", 10, 0, 0, 100, 12) # Self +1 Atk
    Psybeam = Moves("Psybeam", 10, 1, 65, 100, 0) # 10% chance Confuse
    Psychic = Moves("Psychic", 10, 1, 90, 100, 3) # 10% chance -1 S. Def
    Psycho_Cut = Moves("Psycho Cut", 10, 0, 70, 100, 0) # Higher crit (12.5%)
    Rest = Moves("Rest", 10, 0, 00, 100, 0) # 100% max life recovery / Self Sleep
    Zen_Headbutt = Moves("Zen Headbutt", 10, 0, 80, 90, 0) # 20% chance Flinch

# BUG
    Bug_Bite = Moves("Bug Bite", 11, 0, 60, 100, 0)
    Bug_Buzz = Moves("Bug Buzz", 11, 1, 90, 100, 3) # 10% chance -1 S. Def
    First_Impression = Moves("First Impression", 11, 0, 90, 100, 0) # Priority / Golisopod ONLY
    Leech_Life = Moves("Leech Life", 11, 0, 80, 100, 0) # Life draining
    Lunge = Moves("Lunge", 11, 0, 75, 100, 2) # -1 Atk
    Megahorn = Moves("Megahorn", 11, 0, 120, 85, 0)
    Signal_Beam = Moves("Signal Beam", 11, 1, 75, 100, 0) # 10% chance Confuse
    Steamroller = Moves("Steamroller", 11, 0, 60, 100, 0) # 30% chance Flinch
    String_Shot = Moves("String Shot", 11, 0, 0, 95, 10) # Multi-target / -2 Spd
    Struggle_Bug = Moves("Struggle Bug", 11, 1, 50, 100, 4) # Multi-target / -1 S. Atk
    X_Scissor = Moves("X-Scissor", 11, 0, 80, 100, 0)
    
# ROCK
    Head_Smash = Moves("Head Smash", 12, 0, 150, 80, 0) #Recoil damage
    Power_Gem = Moves("Power Gem", 12, 1, 80, 100, 0)
    Rock_Polish = Moves("Rock Polish", 12, 0, 0, 100, 20) # Self +2 Spd
    Rock_Slide = Moves("Rock Slide", 12, 0, 75, 90, 0) # 30% chance Flinch / Multi-target
    Rock_Throw = Moves("Rock Throw", 12, 0, 50, 90, 0)
    Rock_Tomb = Moves("Rock Tomb", 12, 0, 60, 95, 5) # -1 Spd
    Rock_Wrecker = Moves("Rock Wrecker", 12, 0, 120, 90, 0)
    Stone_Edge = Moves("Stone Edge", 12, 0, 100, 80, 0) # Higher crit (12.5%)
    
# GHOST
    Astonish = Moves("Astonish", 13, 0, 30, 100, 0) # 30% chance Flinch
    Confuse_Ray = Moves("Confuse Ray", 13, 0, 0, 100, 0) # Confuse
    Hex = Moves("Hex", 13, 1, 65, 100, 0) # Double damage to status effected
    Lick = Moves("Lick", 13, 0, 30, 100, 26) # 30% chance Paralyze
    Shadow_Ball = Moves("Shadow Ball", 13, 1, 80, 100, 3) # 20% chance -1 S. Def
    Shadow_Claw = Moves("Shadow Claw", 13, 0, 70, 100, 0) # Higher crit (12.5%)
    Shadow_Punch = Moves("Shadow Punch", 13, 0, 60, 100, 0) # Never misses
    Shadow_Sneak = Moves("Shadow Sneak", 13, 0, 40, 100, 0) # Priority
    
# DRAGON
    Draco_Meteor = Moves("Draco Meteor", 14, 1, 130, 100, 0) # Self -2 S. Atk
    Dragon_Breath = Moves("Dragon Breath", 14, 1, 60, 100, 26) # 30% chance Paralyze
    Dragon_Claw = Moves("Dragon Claw", 14, 0, 80, 100, 0)
    Dragon_Pulse = Moves("Dragon Pulse", 14, 1, 85, 100, 0)
    Dragon_Rage = Moves("Dragon Rage", 14, 1, 0, 100, 0) # Always 40 Damage
    Dragon_Rush = Moves("Dragon Rush", 14, 0, 100, 75, 0) # 20% chance Flinch
    Outrage = Moves("Outrage", 14, 0, 120, 100, 0) # Self Confuse
    Twister = Moves("Twister", 14, 1, 40, 100, 0) # 20% chance Flinch / Multi-target
    
# DARK
    Bite = Moves("Bite", 15, 0, 60, 100, 0) # 30% chance Flinch
    Brutal_Swing = Moves("Brutal Swing", 15, 0, 60, 100, 0) #Multi-target
    Crunch = Moves("Crunch", 15, 0, 80, 100, 1) # 20% chance -1 Def
    Dark_Pulse = Moves("Dark Pulse", 15, 1, 80, 100, 0) # 20% chance Flinch
    Fake_Tears = Moves("Fake Tears", 15, 0, 0, 100, 8) # -2 S. Def
    Feint_Attack = Moves("Feint Attack", 15, 0, 60, 100, 0) # Never misses
    Nasty_Plot = Moves("Nasty Plot", 15, 0, 0, 100, 17) # Self +2 Atk
    Night_Daze = Moves("Night Daze", 15, 1, 85, 95, 0) # 40% chance -1 Accuracy
    Night_Slash = Moves("Night Slash", 15, 0, 70, 100, 0) # Higher crit (12.5%)
    Snarl = Moves("Snarl", 15, 1, 55, 95, 4) # -1 S. Atk
    
# STEEL
    Autotomize = Moves("Autotomize", 16, 0, 0, 100, 20) # Self +2 Spd
    Bullet_Punch = Moves("Bullet Punch", 16, 0, 40, 100, 0) # Priority
    Flash_Cannon = Moves("Flash Cannon", 16, 1, 80, 100, 3) # 10% chance -1 S. Def
    Iron_Defense = Moves("Iron Defense", 16, 0, 0, 100, 16) # Self +2 Def
    Iron_Head = Moves("Iron Head", 16, 0, 80, 100, 0) # 30% chance Flinch
    Iron_Tail = Moves("Iron Tail", 16, 0, 100, 75, 1) # 30% chance -1 Def
    Magnet_Bomb = Moves("Magnet Bomb", 16, 0, 60, 100, 0) # Never misses
    Metal_Claw = Moves("Metal Claw", 16, 0, 50, 95, 12) # 10% chance Self +1 Atk
    Metal_Sound = Moves("Metal Sound", 16, 0, 0, 85, 6) # -2 Def
    Meteor_Mash = Moves("Meteor Mash", 16, 0, 90, 90, 6) # 20% chance Self +1 Atk
    Mirror_Shot = Moves("Mirror Shot", 16, 1, 65, 85, 0) # 30% chance -1 Accuracy
    Steel_Wing = Moves("Steel Wing", 16, 0, 70, 90, 11) #10% chance Self +1 Def
    
# FAIRY
    Baby_Doll_Eyes = Moves("Baby Doll Eyes", 17, 0, 0, 100, 2) # Priority / -1 Atk
    Charm = Moves("Charm", 17, 0, 0, 100, 2) # -2 Atk
    Dazzling_Gleam = Moves("Dazzling Gleam", 17, 1, 80, 100, 0) # Multi-target
    Disarming_Voice = Moves("Disarming Voice", 17, 1, 40, 100, 0) # Never misses
    Draining_Kiss = Moves("Draining Kiss", 17, 1, 50, 100, 0) # Life draining
    Fairy_Wind = Moves("Fairy Wind", 17, 1, 40, 100, 0)
    Moonblast = Moves("Moonblast", 17, 1, 95, 100, 4) # 30% chance -1 S. Atk
    Moonlight = Moves("Moonlight", 17, 0, 0, 100, 0) # 50% max life recovery
    Play_Rough = Moves("Play Rough", 17, 0, 90, 90, 2) # 10% chance -1 Atk
    Sweet_Kiss = Moves("Sweet Kiss", 17, 0, 0, 75, 0) # Confuse