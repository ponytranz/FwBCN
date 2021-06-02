label morning:
    stop music fadeout 3.0
    play ambience ambienceday
    scene bg black with dissolve
    $ renpy.pause (1)
    if livingwithmoxie == 1:
        scene bg moxiebedday with dissolve
    elif livingwithbutters == 1:
        scene bg buttersbedday with dissolve
    else:
        pass
    $ rand = renpy.random.randint(1,10)
    if rand == 1:
        "I awaken well rested."
    elif rand == 2:
        "Another wet dream, this place is getting to me."
    else:
        "Ahh, another morning."
    $ rand = renpy.random.randint(1,3)
    if rand == 1:
        "I crawl out of bed and stretch."
    elif rand == 2:
        "After five more minutes of snooze time, I get out of bed and go to shower."
    else:
        "*Yawwwn...* Guess it's time to get out of bed."
    jump afteraltmorning
    label altmorning:
        stop music
        if livingwithmoxie == 1:
            scene bg moxiewagonday with dissolve
            if fr == 1:
                $ rand = renpy.random.randint(1,3)
                if rand == 1:
                    show moxie walthappy with dissolve
                    moxie "Good morning, I was just about to go for a nap. Selene's lessons were really tough!"
                    moxie "See ya later tonight."
                elif rand == 2:
                    "Looks like Moxie is asleep right now. She often sleeps into the afternoon with her evening lessons."
                else:
                    show moxie whorny with dissolve
                    moxie "Look who decided to finally show up! Hahah, you're such a player."
                    mc "You know me, I can't say no."
                    moxie "That's heckin' true! That's how you and I ended up rutting."
                    moxie "Since you can't say no, how about a quickie before I nap and you work?"
                    mc "You're on!"
                    scene bg moxiebedday with dissolve
                    show moxie doggystyle1 with dissolve
                    scene bg black with dissolve
            else:
                $ rand = renpy.random.randint(1,10)
                if rand <5:
                    show moxie2 althappy with dissolve
                    moxie "Oh hey! Glad I got to see you before I left for work, I was just leaving tho'."
                    mc "Hiya Moxie, seeing your grin is a great way to start any day. See you this evening?"
                    show moxie2 laughing with dissolve
                    moxie "See you tonight!"
                    "We hug and she pats me on the butt."
                    hide moxie with dissolve
                elif rand == 10:
                    show moxie happy with dissolve
                    moxie "Just the man I was hoping to see!"
                    mc "Hey Moxie, what's up?"
                    moxie "You've been out all night, so you're probably going to want a shower, right?"
                    mc "Sure am."
                    moxie "Well, I was just about to shower, so how about it?"
                    mc "Sounds efficient."
                    moxie "Efficient isn't quite the word I'd use... Come, come!"
                    hide moxie with dissolve
                    "We fuck in the shower before she leaves for work."
                    scene bg black with dissolve
                elif rand >=5:
                    "Looks like Moxie has already left."
            pass
        elif livingwithbutters == 1:
            scene bg buttershouse with dissolve
            show butters dresshappy with dissolve
            $ rand = renpy.random.randint(1,3)
            if rand == 1:
                butters "Good morning! Guess I better get used to Mr. Popular not appearing some nights."
                mc "Heh, maybe. I'm gonna get a shower."
                butters "Okie dokie, it's all yours."
            elif rand == 2:
                butters "Hello [playername]! I was just about to start a tasty cooked breakfast, if you get a shower now it should be done when you're finished."
                mc "Awh perfect, thanks Butters."
            elif rand == 3:
                butters "Welcome back, hope you weren't having too much fun without me, hehe. My succubus side might end up jealous."
            scene bg buttershouse with dissolve
        else:
            pass
    label afteraltmorning:
        pass
label morningvariables:
    ## Daytime Variables Reset ## Every morning has to pass this ##
    $ days += 1
    $ dawntalk = 0
    if butterspregnanteasteregg > 0:
        $ butterspregnanteasteregg += 1
    if farmvisit3 == 1:
        $ annamilking += 1
    if butterspregnant == 1:
        $ butterspregnant = 2
    if galleryypass == 1:
        $ galleryyear += 1
        if galleryyear == 365:
            "..."
            "Damn, my gallery pass expired."
            "I told you it would."
            $ galleryypass = 0
    $ pauroras = 0
    $ cindysex = 0
    $ arisextoday = 0
    $ sexwithrubytoday = 0
    $ gallerydpass = 0
    $ augustasex = 0
    $ blossomvisit = 0
    $ melodyvisit = 0
    $ lilytalks = 0
    $ honeycrispsex = 0
    $ rubysex = 0
    $ lilysex = 0
    $ spaspecial = 0
    $ spavisited = 0
    $ penelopetalks = 0
    $ auroratalk = 0
    $ selenetalk = 0
    $ aurorasex = 0
    $ selenesex = 0
    $ honeycrisptalks = 0
    $ blossomtalks = 0
    $ rubytalks = 0
    $ melodytalks = 0
    $ surprisetalks = 0
    $ creamsex2 = 0
    $ creamtalks = 0
    $ creamsex = 0
    $ prismatalks = 0
    $ prismasex = 0
    $ rikutalks = 0
    $ rikusex = 0
    $ moxietalks = 0
    $ lilytalks = 0
    $ sundownertalks = 0
    $ butterstalks = 0
    $ succbutterstalks = 0
    $ poyotalks = 0
    $ blossomsex = 0
    $ annatalks = 0
    $ prismamoxiethreesome = 0
    $ musicstudiotalk = 0
    $ musicstudiosex = 0
    $ melcunnilingustoday = 0
    $ persistent.morrigan = 0
    if fr == 1:
        $ worldmap = 3
    else:
        $ worldmap = 1
    if annamilking == 8:
        $ annamilking = 0

    ### Mail
label mail:
    hide moxie with dissolve
    if days >= 20 and bakeryvisits >= 1 and libraryvisit3 == 1 and auroravisitsetup == 0:
        $ auroravisitsetup = 1
        "I have another magic mail, it's usually rare for me to get one of these."
        "It's another mail from Queen Aurora! I would have assumed that she's too busy to even think about me."
        "On the contrary, she's directly inviting me to visit her at the castle."
        "Should I go now?"
        menu:
            "Yeah":
                jump auroravisit1
            "Nah, I got stuff to do. (Visit her manually from the castle)":
                pass
    if days == 3:
        "Looks like I have a magic mail, it's a special type of letter with wings that automatically delivers itself."
        "Woah! This is from Queen Aurora! It even has a fancy seal."
        if augustavisit == 2:
            "I wonder if this is about yesterday?"
            "I timidly unwrap the letter and read it."
            "'Greetings [playername]'"
            "It's weird how she knows about me. She even called me by name yesterday, what's up with that?"
        else:
            "I timidly unwrap the letter and read it."
            "'Greetings [playername]'"
            "She knows my name?"
        "'Your presence within Arcadia has been noted, attached to this letter is a summary of various laws and cultural differences to help you integrate into the world.'"
        if augustavisit == 2:
            "'Please behave yourself, I'm hoping to formally introduce myself to you soon. I apologize for the brief incident with Augusta."
            "Please find the owner of the library, Lily, and talk to her.'"
        else:
            "'Please behave yourself, I'm hoping to meet you one day if possible. Please find the owner of the library, Lily, and talk to her.'"
        "How strange, yet sweet. The goddess of the land has sent me a care-package."
        "There's even a cookie in here, 'baked this morning just for you.'"
        "Thanks Aurora, I'll read through the other things later."
        "Right now I need to get ready for work."
    elif days == 5:
        "I think it's the weekend, but Arcadia doesn't use the same week system like my old world."
        "Indeed, there are no days off in an old-fashioned locale like Arcadia, let's get to work."
    elif days == 7:
        "I've finally been here a week, I admit that time has gone by quickly."
        "I've spent almost every day doing something crazy and exciting."
        "Here's to another wild day!"
    elif days == 14:
        "It has been two weeks since I arrived! Doesn't time fly by?"
        "I wonder what exciting adventure I'll get up to today."
    elif days == 31:
        "I think it's been a month, there's a calendar in here, but I'm not paying enough attention to it as I perhaps should be."
        "What a month it has been, living here has become as natural as my past life. In fact I can barely remember what my life was like before then."
        "I can't imagine any life other than the one I'm living right now."
        "It's a strange sensation, but I know I wake up every morning eager to meet the day."
    if auroravisit1 == 1 and selenevisit1 == 1 and boutiquevisit3 == 1 and farmvisit3 == 1 and barvisit2 == 1 and fr == 0:
        jump finalroute
    if annamilking == 7:
        "Today's the day Anna gets milked at the barn, maybe I should go visit the farm for some fun."
        "If I miss it today, I'll have to wait another week."
    scene bg black with dissolve
    if dawnvisit == 1 and libraryvisit3 == 1 and dawnltr == 0:
        $ dawnltr = 1
        play ambience ambienceday
        if livingwithmoxie == 1:
            scene bg moxiewagonday with dissolve
        elif livingwithbutters == 1:
            scene bg buttershouse with dissolve
        "Ah, I have some mail… Let’s see here…"
        "’Hello Kitten’, ah, it’s from Dawn."
        "Wait, it’s from Dawn?! How did she get my address?"
        dawn "’I’m in need of a handsome man such as yourself, and you may be the only one that can satisfy my urgent desires.’"
        "Is everything an innuendo for this girl?"
        dawn "’Please visit the Bed of Chaos when it suits you and I shall make it more than worth your while…’"
        "Despite the pretext, she obviously isn’t asking for sex, however, it feels like she’s using her sexuality to make me dance in her palm."
        "Saying that, there’s no way I could turn this down."
        "Well, it's morning now. So I'll have to wait until the evening before I go see her."
    if dawnvisit == 3 and dawnltr == 1 and fr == 1:
        $ dawnltr = 2
        play ambience ambienceday
        if livingwithmoxie == 1:
            scene bg moxiewagonday with dissolve
        elif livingwithbutters == 1:
            scene bg buttershouse with dissolve
        "Hm! I have a magic letter… Let’s see here."
        "’Hello, my little kitten! I have a special labour of love that only a man of your abilities can accomplish. Come see me, any morning will do. TTFN, duckling!"
        "Oh hey, she called me kitten and duckling simultaneously this time. I wonder if she just uses both for variety."
        "I’m more than happy to go and see that girl again, I should go as soon as possible."

label events:
    ### events
    if moxieroses == 1 and honeyrubythreesome == 1 and melodylaptop == 1 and doggirl1 == 1 and wolfgirl1 == 1 and midnasexd == 1:
        pass
        if zoe == 2 and arisex == 1 and dawnvisit >= 4 and spaday == 0:
            pass
            if sofiasex == 1 and aure == 0 and sdps == 1 and buttersroses == 1 and cindylum == 1 and spatodo >= 2 and fr == 1:
                $ spaday = 1
                if livingwithbutters == 1:
                    scene bg buttershouse with dissolve
                    play ambience ambienceday
                    show butters dresshappy with d
                    butters "Good morning. I got a magic mail from Lily inviting you and I to an outdoor sauna to have a break."
                    butters "It seems everyone that was involved with Morrigan is invited, and the royal sisters organised it themselves."
                    mc "Awesome, when can we go?"
                    butters "The letter said to meet in the castle. Should we go now?"
                else:
                    scene bg moxiewagonday with dissolve
                    show moxie whappy with d
                    moxie "Morning, tiger! I just got a magic mail from Lily inviting us to an outdoor sauna. Sounds like a perfect opportunity to relax."
                    moxie "And almost everyone from the recent Morrigan incident is invited! The royal sisters organised it themselves."
                    mc "Awesome, when can we go?"
                    moxie "The letter said to meet in the castle. Wanna head out now?"

                "(100%% completion bonus unlocked at the Castle.)"
                "(Activating this bonus will end the game, be sure to have an additional save beforehand.)"
                $ worldmap = 3
                jump prefinalworldmap
    pass
    if livingwithmoxie == 1:
        scene bg moxiewagonday with dissolve
    elif livingwithbutters == 1:
        scene bg buttershouse with dissolve
        play ambience ambienceday
        if butterspregnanteasteregg >= 60:
            jump butterspregnanteasteregg
        if butterspregnant == 2:
            $ butterspregnant = 3
            jump buttersimpregpaizuri
        if buttersimpregintro == 0 and buttersgifts > 1:
            show bg buttershouse with dissolve
            $ buttersimpregintro = 1
            jump buttersimpregintro
        ###
        $ rand = renpy.random.randint(1,2)
        if rand == 1:
            "I finish showering and eat breakfast. As I finish up, Butters gets dressed and joins me in the living room."
        elif rand == 2:
            "I do my morning routine and have breakfast with Butters."
        $ rand = renpy.random.randint(1,3)
        if rand == 1:
            show butters succubus with dissolve
            "Who has incidently turned into a succubus again."
            $ rand = renpy.random.randint(1,2)
            if rand == 1:
                butters "I hope I'm not the only one that woke up with morning wood."
            elif rand == 2:
                butters "This normal food sucks, I want some cum!"
            jump butterssuccmenu
        else:
            show butters dresshappy with dissolve
            $ rand = renpy.random.randint(1,3)
            if rand == 1:
                butters "Any plans for today?"
            elif rand == 2:
                butters "I'm leaving in a few minutes, let me know if you want to come spelunking with me."
            else:
                butters "I always love the morning."
            jump buttersnormalmenu
    else:
        pass
    $ rand = renpy.random.randint(1,3)
    if rand == 1:
        "I do my morning routine and then head out."
    elif rand == 2:
        "After some breakfast, I get ready to go to work. Wherever that may be today."
    else:
        "Well, that's just about everything done for this morning. Where to today?"

    if buttersthirdvisitsetup == 1:
        $ buttersthirdvisitsetup = 0
        jump forestvisit3
    if fr == 1:
        $ worldmap = 3
        jump prefinalworldmap
    $ worldmap = 1
    jump preworldmap
