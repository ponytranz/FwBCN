label evening:
    stop ambience fadeout 2.0
    stop music fadeout 2.0
    scene bg black with dissolve

    $ rand = renpy.random.randint(1,4)
    $ rand2 = renpy.random.randint(1,4)
    if prismamoxiethreesome == 1:
        scene bg black with dissolve
        show bg moxiewagonlamp with dissolve

        if fr == 1:
            show moxie whappyneutral with dissolve
        else:
            show moxie happyneutral with dissolve
        "I arrive at Moxie's wagon, and let her know that Riku will be a guest tonight. I don't mention the threesome, but Moxie's pervy enough to anticipate that."
        scene bg black with dissolve
        "..."
        jump rikumoxiethreesome
    pass
    ## SELENE SETUP##
    if barvisit2 == 1 and forestvisit2 == 1 and libraryvisit3 == 1 and selenevisit1 == 0 and selenevisitready == 0:
        if livingwithbutters == 1:
            play ambience ambiencenight fadein 3.0
            show bg buttershousenight with dissolve
            show butters succsurprised with dissolve
            butters "Hey [playername], I just got a magic mail from Moxie, she wants you to go and see her urgently!"
            mc "Urgently? Sure, see you later Butters."
            show butters succsad with dissolve
            butters "U-Uhm, y-you're leaving?"
            mc "Well, yeah. It's urgent."
            butters "Darn, I'll just masturbate or something then..."
            scene bg black with dissolve
        show bg moxiewagonlamp with dissolve
        play music wagon fadein 3.0
        show moxie shocked with dissolve
        moxie "[playername] [playername]! I just got a magic mail from Princess Selene!"
        moxie "A-And you got one too!"
        mc "Awesome, what’s it about?"
        show moxie happy with dissolve
        moxie "She wants to interview me!"
        show moxie closealthappy with dissolve
        moxie "Here, read yours."
        mc "Hmm… She wants to see me as soon as possible, I guess it’s too important for a normal letter?"
        show moxie closeneutral with dissolve
        moxie "Ohh, uhm. I dunno?"
        mc "When should I go see her?"
        moxie "It has to be the evening, she’s nocturnal, so around midnight."
        mc "Oh right? Should I go tonight? I’ve already done quite a lot today."
        show moxie closelaughing with dissolve
        moxie "If I were in your position, I’d already be walking out the wagon."
        mc "But it’s not even that late, you’d be arriving hours early."
        moxie "Exactly, hours early! I love Selene so much."
        menu:
            "Go tonight":
                mc "Okay, I’ll go tonight."
                $ selenevisitready = 1
                jump selenevisit
            "Visit another night":
                show moxie closeneutral with dissolve
                moxie "Hmm... Okay, but don't keep her waiting!"
                stop music fadeout 2.0
                scene bg black with dissolve
                "…"
                $ selenevisitready = 1
    ####

    if livingwithmoxie == 1:
        jump eveningmoxie
    elif livingwithbutters == 1:
        jump eveningbutters
    else:
        pass

label sleep:
    if livingwithmoxie == 1:
        scene bg black with dissolve
        show bg moxiebednight with dissolve
        "When I arrive home, Moxie is already in bed. I snuggle up with her and soon doze off."
        jump morning
    elif livingwithbutters == 1:
        scene bg black with dissolve
        show bg buttersbednight with dissolve
        "When I arrive home, Butters is already in bed. I snuggle up with her and soon doze off."
        jump morning
    else:
        pass
