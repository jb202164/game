def base():
    print ("""You arrive at the home of the shade.""")

    def task1():

        def next_step():
            print ("""You are aware of something up ahead.
            push enter when ready """)

            ready=input(">")
            if ready ==(">"):
                goblin()
            else:
                goblin()

        def back2base():
            print ("""You have the Seeds of Shade. You feel the magic of the shade seeds
            pulling you back to the Shade Lords residence. You take a deep breath and
            steel yourself ready to transport back.

            Press enter when ready to transport.""")

            home=input(">")
            if home ==(">"):
                seeds+=1
                base()
            else:
                base()

        def trade1():
            print ("""You sit down, the goblin sits down. You pull out everything you think
            you can trade with the goblin. The goblin places the seeds of shade.

            You offer the Goblin:
            1. Gold
            2. Dust
            3. Your double ration of lunch
            4. A single ration of lunch
            5. You change your mind and attack the Goblin.""")

            trade = input (">")
            if trade ==("1"):
                print ("""The goblin realises it cannot eat gold it refuses your offer.
                offering an asset such as gold to a goblin is pointless. Why not offer
                him bearer bonds instead you idiot!\n""")
                trade1()

            elif trade ==("2"):
                print ("""Anger crosses the goblins face for a second. But it remembers you
                are bigger than it. It shakes its head. It can't eat dust.""")
                trade1()

            elif trade==("3"):
                lunch = 0
                print ("""The goblin nods its head takes your double ration and hands the
                shade seeds to you. Before you can do anything it runs off into the hedge
                and begins scoffing your lunch.""")
                back2base()

            elif trade ==("4"):
                print ("""The goblin looks reluctant and points at all of your lunch.""")
                trade1()

            elif trade ==("5"):
                fight()

            else:
                print (f"""I didn't quite get that {name}, try again. """)
                trade1()

        def speak():
            print ("""The goblin doesn't understand you but it points at its belly and opens
            its mouth.
            You think.
            1. The goblin wants to eat you.
            2. The goblin is hungry
            3. You decide to attack the goblin.\n""")

            speak=input (">")

            if speak =="1":
                print ("You draw your sword but step back.\n")
                fight()

            elif speak =="2":
                trade1()

            elif speak =="3":
                fight()

            else:
                print (f"""I didn't quite get that {name}, try again.\n""")
                speak()

        def goblin():
            print ("""The goblin is looking at you. It draws a knife and starts to move
            away from you looking scared.

            You
            1. Attack the Goblin
            2. Speak to the Goblin\n""")

            goblin= input ("What do you do?")
            if goblin =="1":
                fight()
            else:
                speak()

        def fight():

            goblin_life = 26
            name = ("Goblin")

            def rpt1():
                print(f"Round {i} of 4.")
                attack = int (input("""You hit the goblin with damage, choose a number
                between 1-8"""))+2

                life = goblin_life - attack

                print (f"Goblin life :{life}")
                return life

                print (f"{life}")

            def rpt2():
                print("""Battle over. You take the seeds off of the goblins corpse. As you do
                so you notice a small worthless necklace around its neck. You realise it is
                a drawing of the goblin you have just killed and another goblin arm in arm.
                It must be the goblins partner. They will be very upset when they discover
                this.""")
                back2base()

            for i in range(1,5):
                if goblin_life >0:
                    goblin_life = rpt1()
                else:
                    rpt2()

        def corridor():
            print ("""You arrive from the realm of shade you can sense the Seeds of Shade up ahead.
            you there are trees on both sides and you are on a small path.

            1. Move towards where the Seeds of Shade are
            2. Whistle a happy tune
            3. Have a look around """)

            corridor = input (">")
            if corridor =="1":
                print ("""You move down the path towards to the Seeds of Shade. You
                encounter a goblin.""")
                goblin()

            elif corridor =="2":
                print ("""As you whistle and walk you are approached by a goblin.""")
                goblin ()

            elif corridor =="3":
                print ("""You look around and notice several tracks of some form of
                small humanoid.""")
                next_step()

            else:
                print (f"I didnt quite get that {name}, try again")

        print("""You arrive on your first mission.""")
        corridor()

    def task2():
        print ("""You arrive on your second mission """)

        def entry():
            print ("""You arrive at a village very similar to your own. There is a central square
            a large inn, a market place which is currently empty as well as a church nearby.
            You know you muct plant the seeds just out of the village in a darkened area by
            a tree. You can feel the seeds heating up in your pocket. They seem to be willing
            you towards an area.

            1. Go to the Inn
            2. Follow the seeds
            3.Go to the church. """)

            entry = input (">")
            if entry == "1":
                inn()
            elif entry =="2":
                tree()
            elif entry ==("3"):
                church()
            else:
                print (f"Sorry, {name} I didn't quite catch that.")
                entry()

        def drink():
            print ("""You get a drink. Someone nearby comes over to speak to you. You
            notice that he is wearing the same uniform as the others. You also notice
            that they are all men. As he approaches your head begins to spin you feel
            rather uneasy in their presence.

            1.You engage in conversation
            2. You leave the inn
            3. Ask him about his uniform.""")

            drink = input (">")

            if drink =="1":
                print ("""He asks what you are doing here and says he has an odd feeling about you.
                you also feel uneasy but you do not tell him this. You look around and notice
                everyone in the bar is looking at you. The barman is no-where to be seen.

                1.Tell him about the seeds
                2.Leave the inn
                3.Tell him you are here for a visit and ask him about his uniform.""")
                conv2=input (">")

                if conv2 =="1":
                    death3()

                elif conv2=="2":
                    ("""You tell him that you think you are in the wrong place and go to leave.""")
                    death2()

                elif conv2 =="3":
                    uniform()

            elif drink =="2":
                print ("""They look at you suspiciously. Every eye is looking at you as you leave
                You have the feeling that you are lucky if you make it out alive.""")
                entry()
            elif drink =="3":
                uniform()
            else:
                print ("""They look at you suspiciously. Every eye is looking at you as you leave
                You have the feeling that you are lucky if you make it out alive.""")
                entry()

        def death3():
            print ("""The man looks at you as you begin telling your story. He looks aghast
            as you tell it. When you pause he speaks. "Brothers to arms the bringer of darkness
            has arrived." You try to escape the Inn.""")
            import random
            number = random.randint(1,20)
            print(f"{number}")
            if number >4:
                print ("""You don't make it to the door. Your head is smashed in on a
                bar stool, blood splattering everywhere. The last thing you see is
                blood blinding you
                You are dead. End of game!!

                Your body disappears before it can be hauled up by the men of light. You
                suddenly appear in the ether. Taskmaster Klas is stood infront of you.
                'You fool! What is wrong with you? You must just do your task. Don't do anything
                else! You are under a geas, this will show you the task as it reveals itself
                but it will also save your life. This has cost our lord a lot of energy.
                Now go back and do it properly!' Taskmaster Klas disappears and you find yourself
                floating back to the village. \n """)
                entry()

            else:
                print (""" 'You run out of the inn with them all chasing you'
                Using your shade powers you hide for a while until they have calmed down
                and returned to the inn. """)
                entry()

        def death2():
            import random
            number = random.randint(1,20)
            print(f"{number}")
            if number <4:
                print ("""You don't make it to the door. Your head is smashed in on the
                wooden pew, blood splattering everywhere. The last thing you see is
                blood blinding you
                You are dead. End of game!!

                Your body disappears before it can be hauled up by the men of light. You
                suddenly appear in the ether. Taskmaster Klas is stood infront of you.
                'You fool! What is wrong with you? You must just do your task. Don't do anything
                else! You are under a geas, this will show you the task as it reveals itself
                but it will also save your life. This has cost our lord a lot of energy.
                Now go back and do it properly!' Taskmaster Klas disappears and you find yourself
                floating back to the village. \n """)
                entry()

            else:
                entry()

        def uniform():
            print ("""You get told it belongs to the Lord of Light and that they are here
            waiting for the Shade representative as they are here to kill him and his
            forces
            1. Agree with them politely and leave the bar
            2. Tell them about the seeds
            3. Ask them more about the Lord of Light.""")
            uniform = input (">")
            if uniform =="1":
                entry()
            elif uniform =="2":
                death3()
            elif uniform =="3":
                print ("""The man tells you all about the Lord of Light and how all who
                do not support him are actively are enemies and must be destroyed. He
                is very clear that ALL who do not support him are enemies.

                You
                1.Agree with him politely and leave the bar.
                2. Tell them about the seeds""")
                you=input (">")
                if you =="1":
                    import random
                    number = random.randint(1,20)
                    print(f"{number}")
                    if number <4:
                        print ("""You don't make it to the door. Your head is smashed in on the
                        bar stool, blood splattering everywhere. The last thing you see is
                        blood blinding you
                        You are dead. End of game!!

                        Your body disappears before it can be hauled up by the men of light. You
                        suddenly appear in the ether. Taskmaster Klas is stood infront of you.
                        'You fool! What is wrong with you? You must just do your task. Don't do anything
                        else! You are under a geas, this will show you the task as it reveals itself
                        but it will also save your life. This has cost our lord a lot of energy.
                        Now go back and do it properly!' Taskmaster Klas disappears and you find yourself
                        floating back to the village. \n """)
                        entry()

                    else:
                        print ("""They look at you suspiciously. Every eye is looking at you as you leave
                        You have the feeling that you are lucky if you make it out alive.  """)
                        entry()

                elif you =="2":
                    death3()

                else:
                    print ("""They look at you suspiciously. Every eye is looking at you as you leave
                    You have the feeling that you are lucky if you make it out alive.  """)
                    entry()

        def inn():
            print ("""You enter the inn and notice that the majority of people are wearing
            the same uniform. You feel a dangerous aura coming off of all of them. They
            appear to be in some form of religious robes.
            You
            1. Leave the Inn
            2. Go to the bar and order a drink.
            3. Ask someone about the uniform they are wearing.""")
            inn=input(">")

            if inn=="1":
                entry()

            elif inn=="2":
                drink()

            elif inn=="3":
                uniform()

        def church():
            print ("""You approach the church, as you get closer the seeds start to feel
            colder and colder. They begin to buzz. It is obvious they don't want you to
            go into the church.

            1. Enter the church
            2. Follow the seeds
            3. Go elsewhere """)

            church = input (">")
            if church == ("1"):
                print ("""You enter the church and as you do you notice that the seeds
                completly stop moving. You feel a sudden pain in your head. You sit on a
                pew and wait for the pain to subside.

                1. Decide to leave
                2. Wait until you feel better.""")

                pew=input (">")

                if pew=="1":
                    print ("""As you leave the church, you feel much better and the seeds
                    start pulling you toward a place opposite to the Church.""")
                    entry()

                else:
                    worse()

            elif church ==("2"):
                tree()

            else:
                entry()

        def worse():
            print ("""A man in bright white garments arrives to speak to you. The closer
            he gets the worse you feel. He begins to speak.
            "Are you ok? You look like you are having a tough time."

            1. Speak to the man about the pain
            2. Show the man the seeds
            3. Leave
            4. Ask which church you are in""")

            worse=input (">")

            if worse =="1":
                pain()

            elif worse =="2":
                death()

            elif worse =="3":
                ("""As you leave the church, you feel much better and the seeds
                start pulling you toward a place opposite to the church.""")
                entry()

            elif worse =="4":
                light()

            else:
                print (f""" Sorry {name} I didn't quite catch that.""")
                worse()

        def pain():
            print ("""You tell him that since entering the church you feel pain, and
            you wonder why that is.""")
            light()

            ("""If you are in league with one the Lord of Light does not approve of, now
            is the time to repent of this, embrace the light and fight all others.
            You
            1. Repent, and are rebaptised as a followers of the Lord of Light
            2. You leave wondering if it is really a good idea to fight ALL others
            3. Show him the Seeds of Shade, tell him what you are doing in the Shade Realm""")

            pain=input(">")

            if pain =="1":
                death()

            elif pain =="2":
                ("""As you leave the church, you feel much better and the seeds
                start pulling you toward a place opposite to the church.""")
                entry()

            elif pain =="3":
                death()

        def death():
            print ("""The pain increases. The man yells at you. "A representative from the
            enemy. I purge him in the name of the Lord of Light."

            You
            1. Run
            2. Fight (Are you sure? You are challenging a representative of a God in his
            own church while holding Seeds of Shade from potentially a rival) """)

            death=input(">")

            if death =="1":
                run()

            else:
                fight()

        def run():
            import random
            number = random.randint(1,20)
            print(f"{number}")
            if number <4:
                print ("""You don't make it to the door. Your head is smashed in on the
                wooden pew, blood splattering everywhere. The last thing you see is
                blood blinding you
                You are dead. End of game!!

                Your body disappears before it can be hauled up by the men of light. You
                suddenly appear in the ether. Taskmaster Klas is stood infront of you.
                'You fool! What is wrong with you? You must just do your task. Don't do anything
                else! You are under a geas, this will show you the task as it reveals itself
                but it will also save your life. This has cost our lord a lot of energy.
                Now go back and do it properly!' Taskmaster Klas disappears and you find yourself
                floating back to the village. \n """)
                entry()

            else:
                print ("""You run out of the church and feel much better the seeds
                start pulling you toward a place away from the church you hope you will
                not be followed.""")
                entry()

        def fight():
            import random
            number = random.randint(1,20)
            print(f"{number}")
            if number <4:
                print ("""You manage to kill the man. Covered in blood you stumble out
                of the church in the direction that the seeds pull you. You hope that no
                one has seen you.""")
                tree()
            else:
                print (""" 'You fool, you dare challenge me in my own church?' A mace
                appears in his hands and your head is smashed in. You die, end of game!

                Your body disappears before it can be hauled up by the men of light. You
                suddenly appear in the ether. Taskmaster Klas is stood infront of you.
                'You fool! What is wrong with you? You must just do your task. Don't do anything
                else! You are under a geas, this will show you the task as it reveals itself
                but it will also save your life. This has cost our lord a lot of energy.
                Now go back and do it properly!' Taskmaster Klas disappears and you find yourself
                floating back to the village. \n """)
                entry()

        def light():
            print ("""He tell you that this is the Church of Light. The Light fights the
            Lord of Darkness and all of his allies. Anyone who does not support the Lord of
            Light is against him and will be crushed.

            1. Leave the church as a person who has recently visited the Shade realm
            the Lord of Light was probably not a good idea.
            2. Tell him about your adventures in the realm of shade.""")

            light = input (">")

            if light =="1":
                ("""As you leave the church, you feel much better and the seeds
                start pulling you toward a place opposite to the church.""")
                entry()

            elif light =="2":
                death()

            else:
                print ("""Sorry I didn't quite get that. """)
                light()

        def tree():
            print ("""You are guided to a nearby woods. The seeds begin to buzz as you reach
            a particularly large tree. You know this is where they need planting. You
            also know that you must bury them without being observed. If you are seen then
            you will be stopped. For some reason the seeds need to be planted in secrecy,
            you do not know why.

            1. Begin planting seeds hoping you will not be observed.
            2. Change your mind, go somewhere else.""")

            tree = input(">")

            if tree ==("1"):
                dice_simulate()

            else:
                entry()

        def speak():
            print ("""You chat with the person and bore them with details about how you are
                waiting for your girlfriend and if your dad found out you would be in trouble.
                The passerby leaves you alone in the trees. You soon return to work.""")
            dice_simulate()

        def hide():
            import random
            print ("""You hide behind a nearby tree and wonder if they have seen you. """)
            number = random.randint(1,20)
            print(f"{number}")
            if number <8:
                print ("""You have been spotted they approach you to speak to you.
            1.Stab them to death so you can return to work.
            2.Move out from your hiding place and speak to them""")
            else: dice_simulate()

            fail=input (">")

            if fail =="1":
                print("""You succesfully murder this innocent passerby for no real
                reason and return to work. Their body oozing blood nearby.""")
                dice_simulate()

            elif fail=="2":
                speak()

        def tryagain():
            print("""Someone sees you and approaches. You stop what you are doing and
            1. Stab them to death so you can return to work.
            2. Attempt to hide
            3. Move out to speak to them.""")

            here =input (">")

            if here =="1":
                print("""You succesfully murder this innocent passerby for no real
                reason and return to work. Their body oozing blood nearby.""")
                dice_simulate()

            elif here =="2":
                hide()
                dice_simulate()

            elif here =="3":
                speak()
                dice_simulate()

            else:
                speak()

        def missioncomplete():
            print ("""With the seeds planted you return home. You use the magic from
            the shade seeds to take you back to the realm of shadow.""")
            base()

        def dice_simulate():
            import random
            number = random.randint(1,20)
            print(f"{number}")
            if number <8:
                    print ("""You are seen. You quickly stop planting the seeds.""")
                    tryagain()
            else:
                print ("""You continue to plant the seeds """)

        entry()
        for i in range(0,4):
            dice_simulate()

        missioncomplete()

    def task3():
        print("""You arrive on your third mission.""")

        def moveon():
            print ("""There are only two doors left, you are getting closer to the main hall
            at the end, it is more likely you will be seen this end. There is a door on the left
            and a door on the right. You have no time to inspect the doors as you hear
            someone coming.

            1. You take the door on the right
            2. You take the door on the left """)

            moveon=input (">")

            if moveon=="1":
                 garrison()

            elif moveon =="2":
                prison()

            else:
                print (f"""Sorry {name} I didn't quite get that. """)
                moveon()

        def convince():
            number = random.randint(1,20)
            print(f"{number}")
            if number <4:
                    print (""" 'You think so? I don't believe you.' The guard stands
                    up. He is wearing armour and wielding a sword. """)
                    combat2()
            else:
                print (""" 'Welcome then, you won't be in this room but the one down the
                hall.' You thank them and leave. You go through the only door left.""")
                prison()

        def combat2():
            print ("""You see no way out of this. Looks like you must fight. You have only
            two options
            1. Run
            2. Fight """)
            combat2=input
            if combat2=="1":
                print ("You run out of the room and attempt to wedge the door behind you.")
                number = random.randint(1,20)
                print(f"{number}")
                if number <4:
                        print ("""You fail to close the door and wedge it. You must fight.""")
                        combat()
                else:
                    print ("""You manage to escape and wedge the door behind you. You rush
                    into the only room left.""")
                    prison()
            else:
                combat2()

        def combat():
            print ("time to fight")
            print ("You square up and swing for one another.")
            number = random.randint(1,20)
            print(f"{number}")
            if number <6:
                print ("""You miss your strike and step straight into the guards
                attack. You are impaled on his sword and begin to bleed. Taskmaster
                Klas appears and somehow manages to control your bleeding body.
                You stumble through the door you are yet to go through.

                The room you are in is full of candles you have no time to think.
                You knock over some candles blowing them out. You
                open the box. 'Freedom, brother, you took your time though' A shade is stood
                infront of you. 'You are no brother..yet, but I can sense the shade in you, time
                for us to go' The shade engulfs you and you start to disappear. As you do so
                you hear the guard shouting 'They are escaping.'  """)
                base()

            else:
                print ("""The guard swings his sword, you swing your sword. He misses you duck under
                and run him through. You don't have long though as there is now a bloody body in a
                busy corridor.You go through the only door you can.""")
                prison()

        def prison():
            print ("""You have entered a very bright room. There are candles and mirrors
            all around it means that you cannot cast a shadow. This room gives you a deep
            sense of unease. You notice that there is a box in the light. The lack of
            shadows in the room really annoys you.

            1. Blow out some candles to create shade
            2. Open the box """)

            prison=input(">")

            if prison =="1":
                print ("""You blow out some candles and the reflections stop working.You
                open the box. 'Freedom, brother, you took your time though' A shade is stood
                infront of you. 'You are no brother..yet, but I can sense the shade in you, time
                for us to go' The shade engulfs you and you start to disappear. As you do so
                you hear banging on the door. 'They are escaping.' """)
                base()

            elif prison=="2":
                print("""You hear a screech. 'It burns.. blow the candles out.'
                1. Let the shade burn
                2. Quickly blow the candles out. """)

                burn= input(">")

                if burn =="2":
                    print ("""You blow out some candles and the reflections stop working.You
                    open the box. 'Freedom, brother, you took your time though' A shade is stood
                    infront of you. 'You are no brother..yet, but I can sense the shade in you, time
                    for us to go' The shade engulfs you and you start to disappear. As you do so
                    you hear banging on the door. 'They are escaping.' """)
                    base()

                elif burn =="1":
                    print ("""You realise you are killing the shade you must save. If you
                    leave it for much longer you will be stranded here.

                    1. Continue to watch him burn
                    2. Blow the candles out""")

                    burn2=input(">")

                    if burn2=="1":
                        print ("""Taskmaster Klas has followed you here. He now appears and kills you
                    he uses your corpse to knock the candles over. The room now has both light and
                    dark in it. Taskmaster Klas and the shade escape leaving you behind.
                    End of game!! """)
                        quit()

                    elif burn2=="2":
                        print ("""You blow out some candles and the reflections stop working.You
                    open the box. 'Freedom, brother, you took your time though' A shade is stood
                    infront of you. 'You are no brother..yet, but I can sense the shade in you, time
                    for us to go' The shade engulfs you and you start to disappear. As you do so
                    you hear banging on the door. 'They are escaping.' """)
                        base()

                    else:
                        prison()

                else:
                    prison()

            else:
                prison()

        def garrison():
            print ("""You enter the room and before you can close the door behind you,
            you realise that you have entered a guard room.
            1. Attack them while you have the upper hand.
            2. Chat to them, pretend you are new. """)

            garrison = input(">")

            if garrison =="1":
                print ("""You quickly stab a sleeping guard to death. There are two guards
                left one is in pyjamas and out of bed. The other is in full armour ready for
                battle.""")
                combat()

            elif garrison =="2":
                print ("""'Hi I'm new here, my name is Garth. I was told that I was to bunk
                here'""")
                convince()
            else:
                print (f"""Sorry {name} I didn't quite get that. """)
                garrison()

        def nextdoor():
            print ("""There are markings on this door, the handle looks like it is used
            much more. You listen at the door and hear voices.
            1. Enter the room
            2. Move on this is not where the shade will be hiding. """)

            nextdoor=input(">")

            if nextdoor =="1":
                garrison()

            else:
                moveon()

        def quiet():
            print ("""You look for details at the door. It is locked and there are no
            significant markings on it. You move on to the next set of doors.""")
            nextdoor()

        def entry():
            print ("""You arrive in a maze of halls you have to locate the shade and
            release him from his prison. You are currently at the end of a hallway
            there are doors on your left and right. There is a big hall at the end
            of the corridor.

            1. Listen at the door to the right
            2. Listen at the door to the left
            3. Walk down the corridor towards the doors at the end. """)

            entry =input (">")

            if entry =="3":
                moveon()

            else:
                quiet()

        import random
        entry()

    def chest():
        attack = 0
        life = 26
        dust = 0
        gold = 0
        print (
    """This seems like an ornate chest as far as you can tell.\n The hinges, clasp and joinery seem exquisite\n as this is not your realm though you are
    unsure if the chest has magical properties or not. You open the chest and find it contains.
    A set of basic armour\n a small sword \na small bag with what you guess are coins\a small bag with some form of coarse sand.

        You
        1. Take the armour
        2. Take the sword
        3. Take the bag of coins
        4. Take the small bag of sand.
        5. Take all of them.""")

        chest=input (">")
        if chest =="1":
            life += 5#I want this to give a life bonus of 5 if wearing this
            print (f"""You take the armour and put it on, this gives you increased life.\n""")
            bedroom()

        elif chest =="2":
            attack +=2
            print (f"""You take the sword and belt it complete with scabbard to your waist\n""")
            bedroom()#this will give a +2 damage in a fight

        elif chest =="3":
            gold == 5
            print (f"""
        You don't know about commerce here but you take the coins.\nAfterall they must have been meant for you\n""")
            bedroom()#to bribe a group on task 1,2 or 3

        elif chest =="4":
            dust +=1
            print (f"""You are not really sure if it is sand or not but take it anyway.\n""")
            bedroom()
            #this is to blind an enemy but later on in the game can be used to forge a new sword. A magical shade sword which grows as you do

        elif chest =="5":
            dust += 1
            gold += 5
            life +=5
            attack += 2
            print (f"""You don the armour, tie the sword and scabbard around your waist, take the sand and the money.\n""")
            bedroom()

        else:
            bedroom()

    def speak():#root menu of base.py
        print ("""You are in the main residence of the Shade Lord. What do you do next?
        1. Speak to someone
        2. Have a look around
        3. Retire to your accommodation\n""")

        speak = input ("Enter a number for your action.")
        if speak == "1":
            people()

        elif speak =="2":
            closerlook()

        elif speak == "3":
            bedroom()

        else:
            print(f"Sorry {name} I didn't quite get that, try again\n")
            speak()

    def desk():
        print("""You sit at the desk and look to see what is in the drawers.
        There is some kind of journal. It looks of high quality with a blank front
        cover. You find a pen nearby.
        You
        1. Begin to write in the journal
        2. Leave it for another time.
        3. Do something else.""")

        desk = input (">")

        if desk== "1":
            print("""You write a summary of what has happened so far then close the journal.\n""")#I need to automatically update this somehow
            bedroom()

        elif desk=="2":
            bedroom()

        else:
            bedroom()

    def sleep():#eventually every sleep means you gain +1 living in shade realm.
        print ("""You fall asleep and have an odd dream about the realm of Shade. You
        awaken with a deep sense of foreboding. Was the dream to warn you about the
        realm of shade or to warn you of impending danger? you remain unsure.\n""")
        bedroom()

    def bedroom():
        influence = 0
        print ("""This is the room the Shade Lord has let you use while you stay here\nIn this room there is a bed, a small chest and a desk.\n
        1. Go to sleep
        2. Open the chest
        3. Sit at and look through the desk.
        4. Leave the room.""")

        bedroom = input (">")

        if bedroom == "1":
            influence +=1
            sleep()

        elif bedroom =="2":
            chest()

        elif bedroom=="3":
            desk()

        else:
            speak()

    def majordomo1():
        lunch = 0
        print (""""I can offer you help in anyway. While you stay here with us.
        would you like me do anything?"
        1.Tell the Majordomo you are going on a mission so need some food to take with
        you.
        2. Ask about the locked door.
        3. Ask about the Taskmaster.
        4. Ask about the mysterious person.
        5. Ask the Majordomo about himself.
        6. "It doesn't matter""")

        mdomo1 = input (">")

        if mdomo1 =="1":
            lunch +=2
            print (""""
        I will have it prepared for when you are ready to go. As you leave
        I will make sure you have it. If you are lucky you might get a double portion.
        Is there anything else I can help you with?\n """)
            majordomo1()

        elif mdomo1 =="2":
            print ("""
        The Majordomo says 'The locked door leads to other parts of the house.
        You will not be welcomed to have free range of the Lords estate until you have proven
        yourself to be worthy. Is there something else you wish to know?'\n """)
            majordomo1()

        elif mdomo1 =="3":
            print("""The Majordomo smiles. "You will get used to Klas. He might be grumpy
        towards you but then again he doesn't know you yet. Our master respects his
        view so you'd best not annoy him too much. Is there something else you wish to know?" \n """)
            majordomo1()

        elif mdomo1 =="4":
            print("""
        A recruit much like you. You both have tasks to do before our Master
        decides what happens to you next. She arrived a week before you did, but
        has yet to complete any tasks.\n""")
            majordomo1()

        elif mdomo1=="5":
            print ("""
        Much like all in our world we are sworn to a lord and discharge our duty as
        we see fit. I am in charge of running this house for our lord and he tells me
        what he needs. From what I know of where you are from our lord leads our
        house much like a governor or a mayor would in your village or town.\n""")
            majordomo1()

        elif mdomo1 =="6":
            people()

        else:
            people()

    def morph():
        print ("""You hit the wall with your hand. Nothing happens. You hit it a few
        more times. Finally everyone is staring at you. You decide to give it one
        last blast. You slam the wall as hard as you can. Your hand becomes stuck to
        the wall. Like thick porridge your hand is engulfed.
        "You won't last long! You idiot" The Taskmaster says
        The mysterious figure lets out a chuckle
        The Majordomo moves over to you and removes your hand from the wall.
        'If you would be so kind as to not do that again it would be most appreciated.'
        He then moves away. \n""")

        closerlook()

    def taskchoices():
        print (""" "It's pretty simple. Our lord is helping you and in return you get
        to help him. There are three tasks you must complete. Choose one. I don't really
        care which one you choose. Just get on with it.

        1. Task one
        2. Task two
        3. Task three
        4. You ask for more details about the tasks.""")

        tasks = input (">")

        if tasks =="1":
            print ("""The world swirls around you and you feel yourself being instantly
            transported. While this is happening you feel that you know your task. You
            are being sent to rescue some shade seeds.\n""")
            task1()

        elif tasks =="2":
            print ("""The world swirls around you and you feel yourself being instantly
        transported. While this is happening you feel that you know your task. You
        are to plant some shade seeds without being seen.\n""")
            task2()

        elif tasks =="3":
            print ("""The world swirls around you and you feel yourself being instantly
        transported. While this is happening you feel that you know your task. You are
        to rescue a trapped shade.\n""")
            task3()

        elif tasks =="4":
            print ("""You are new here so will get used to how things work. You choose
            the task and then as you are on your way, you know what to do. You are not
            told, you just know. This stops missions being leaked but it also stops
            you wasting my time.\n""")
            taskchoices()

        else:
            print (f"""Speak up will you {name}.Stop wasting my time.\n""")
            taskchoices()

    def mysterious ():
        print ("""You look at the mysterious person and have no real clue about them.
        You
        1. Ask them their name
        2. Introduce yourself
        3. Poke them""")

        myst= input (">")
        if myst =="1":
            print ("What does it matter to you? They then turn away.")
            speak()

        elif myst=="2":
            print ("""They reply. 'Hi my name is 无名\n' It appears they have little
            interest in speaking to you\n""")
            speak()

        elif myst=="3":
            print ("""Ask you get closer to make contact they appear to have
            moved elsewhere. Only a few inches away but far enough away to realise
            this was a bad idea\n""")
            speak()
            #eventually get this to happen 5 times then they attack you and you suffer damage.
        else:
            speak()

    def shadow():
        print("""You look for your own shadow but in the gloom of this realm you cannot
        see it. You know you are in the realm of shadow. Maybe your shadow has its own
        life here. What if you return home and have no shadow? You realise that the more
        you think about it the more your head hurts.\n""")
        closerlook()

    def water():
        print ("""You look around the room and realise there is no water anywhere.
        perhaps you should try your room to find some.\n""")
        closerlook()

    def reflection():
        print("""You stand infront of a wall and manage to make out your reflection.
        you look darker and longer for some reason, it might be a trick of the light
        or lack of it.\n""")
        closerlook()

    def closerlook():
        print ("""You look around. The colour spectrum here ranges from pitch
        black to light grey. No other colours seem to exist. Everything appears to
        have a transulence to it. But the harder you focus on it the more impenetrable
        it appears to be.

        You
        1. Decide to see what will happen if you attempt to pierce a wall.
        2. Look at your own shadow.
        3. Try to find some water to pour.
        4. Look at your reflection in a wall.
        5. You decide it might be a bad idea.\n""")

        closerlook = input (">")

        if closerlook =="1":
            morph()

        elif closerlook =="2":
            shadow()

        elif closerlook =="3":
            water()

        elif closerlook =="4":
            reflection()

        elif closerlook =="5":
            speak()

        else:
            speak()

    def people():#this is the root to speak to people
        print("""There are three people in this reception area. The Majordomo,
        the Taskmaster and a mysterious person in the corner.

        Who do you speak to?""")

        people = input ("1. Majordomo 2. Taskmaster 3. Mysterious person 4.Don't bother ")

        if people == "1":
            print("""As you look closer you see that the Majordomo clearly is not
            human, he is a shade, but not the type of shade you saw earlier.
            Hello, and welcome, I am here to help you. Please let me know what you need.\n""")
            majordomo1()

        elif people=="2":
            print (f"""
        Ah {name}'Are you ready for your tasks?' Asks a grumpy looking shadow.
        1. Yes
        2. Not yet.""")

            decide=input(">")

            if decide=="1":
                taskchoices()

            else:
                print ("""
        Stop wasting my time then.\n""")
                speak()

        elif people=="3":
            print (
        """You approach this mysterious individual, you are not sure if
        they are human or not, they are wearing a long cloak, so you cannot tell.\n""")
            mysterious()

        elif people =="4":
            speak()

        else:
            print(f"""
        Sorry {name} I didn't quite get that, try again.\n""")
            people()

    name = input("Enter character name: ")
    if name == ("Dave"):
        print ("""Come on is that all you have?
        Next time
        Use your imagination.
        You could be called:
        MAM
        Shade Meister
        or a real world name like:
        David Burt
        Gary Gygax\n """)
        speak()

    elif name ==("dave"):
        print ("""Come on is that all you have?
        Next time
        Use your imagination.
        You could be called:
        Elminster
        Thanos
        or a real world name like:
        Ed Greenwood
        Moxie Marlinspike\n""")
        speak()

    else:
        input("")
        speak()

def agree():
    print (""""That's great! What I will do is transport you to my home. You will
    use this as a base while you complete some tasks for me. While you are doing
    those tasks I will stop the attack on the village. This will not come without
    consequece to either of us good luck".
    Take a deep breath i'll transport you now.""")

    b=input ("Push enter when you have taken a deep breath")

    if b == ">":
        base()
    else:
        base()

def disagree():
    print ("""If you don't agree then you will have to find another way to
    save the village.

    What do you do now.
    1. Run away
    2. Reluctantly agree.""")

    disagree = input (">")

    if disagree =="1":
        print ("""The shade sighs as you run away. "This is not the first time
        someone has judged me before I can speak" He says as you run away""")
        root()

    elif disagree =="2":
        agree()

    else:
        mission()

def mission ():
    print ("""The shadow tells you that he knows the village is under attack. He wishes
    he could help. He can help, but you need to help him in return.
    "If you help me then I can help you. But my people will be sacrificing themselves
    you need to help us in return. Will you help us, so that we can help you?"

    1. You agree to help the shade although reluctantly.
    2. You eagerly agree to help the shade if he can save the village
    3. You refuse.""")

    mission = input ("Do you agree or find another way to help? Make your choice")

    if mission == "1":
        agree()

    elif mission =="2":
        agree()

    elif mission == "3":
        disagree()

    else:
        print ("""I didn't quite get that.""")
        mission()


def table_smash():
    print ("""You tap the table a few times but nothing happens. You decide to
    smash it as hard as you can. The solid table becomes some form of sticky goo.
    The shade looks at you. "You're rather rude." He then continues speaking.""")
    mission()

def details():
    print ("""As you look closer at the table you realise it is some form of
    solid shimmering shadow which is somehow condensed into a solid. If you stare
    at the table you can see it is slowly swishing as if it is liquid encased in
    glass.

    1. Listen to what the shade has to say.
    2. Attempt to smash the table to see what happens.
    3. When you actually see a shade in real life you are so scared you run off.""")

    details = input ("What do you do?")

    if details == "1":
        mission ()

    elif details == "2":
        table_smash()

    elif details =="3":
        print ("""The shade sighs as you run away. "This is not the first time
        someone has judged me before I can speak" He says as you run away""")
        root()

    else:
        print ("""I didn't quite get that""")
        details()

def shadecave():
    print ("""You make your way to the entrace. You are naturally apprehensive.
    People who have been to this cave have a tendency to never return. Those who
    do tell stories of a powerful shade. Perhaps he can help you.

    As you tentatively step into the cave you. See a table with two chairs.
    there is a fire burning too. But it seems odd.

    1. You look closer to make out details.
    2. You realise you have made a huge mistake and decide to leave.
    3. You try to look for a torch to light the room up.""")

    cave1 = input (">")

    if cave1 == "1":
        details()

    elif cave1 =="2":
        root()

    elif cave1 == "3":
        print ("""A voice speaks "You don't want to do that. Think about it
        I am a shade. Striking light in here is not really what I want.
        Take a seat." The shade points to a chair.""")
        mission()

    else:
        print ("I didn't quite get that.")
        root()

def root():
    print ("""You awaken at night to sounds of battle in your village.
    You quickly throw some clothes on. You wonder how you can help.
    As you leave the house smells of smoke assail you.
    Screams and the sounds of fighting surround you.
    You see the first attacker. A huge demon easily as big as the shed in your
    garden you know there is no way you can fight these enemies.
    You think of the places you could go to get help.

    3. The cave of shade the otherside of the village.""")

    root = input (">")

    if root == "3":
        shadecave()
    else:
        root()

root()
