screen worldmap():
    imagemap:
        ground "bg worldmapday"
        hover "bg worldmaphover"

        hotspot (0, 300, 290, 210) clicked Jump("maplibrary")
        hotspot (895, 305, 140, 140) clicked Jump ("mapwagon")
        hotspot (380, 200, 107, 95) clicked Jump ("mapfarm")
        hotspot (480, 250, 90, 90) clicked Jump ("mapbakery")
        hotspot (575, 360, 75, 75) clicked Jump ("mapbar")
        hotspot (556, 280, 85, 80) clicked Jump ("mapspa")
        hotspot (470, 320, 80, 65) clicked Jump ("mapmarket")
        hotspot (200, 225, 90, 90) clicked Jump ("mapforest")
        hotspot (1130, 270, 150, 175) clicked Jump ("mapboutique")
        hotspot (830, 180, 175, 140) clicked Jump ("mapcity")

        hotspot (920, 0, 108, 125)  action (Jump("todolist"), Hide("worldmap", dissolve))
        hotspot (1025, 0, 138, 125)  clicked Jump ("inventorymenuday")
        hotspot (1165, 0, 108, 125)  action ShowMenu("preferences")
    text "{b}[monies]{/b}":
        xalign 0.22
        yalign 0.0225
    text "{b}Day [days]{/b}":
        xalign 0.065
        yalign 0.0225

label preworldmap:
    play music day fadein 3.0
    play ambience ambienceday fadein 5.0
label worldmap:
    hide screen todolist with qd
    if worldmap == 2:
        stop music
        play ambience ambiencenight
        jump worldmapnight
    elif worldmap == 3:
        jump finalworldmap
    elif worldmap == 4:
        stop music
        play ambience ambiencenight
        jump finalworldmapnight
    $ worldmap = 1
    scene bg worldmapday
    call screen worldmap
    with qd
    label mapwagon:
        jump wagon
    label mapmarket:
        show bg market with dissolve
        if dawnltr == 3:
            $ dawnvisit += 1
            $ dawnltr += 1
            show dawn2 happy with dissolve:
                xalign 0.5
                ypos 20
            play music dawn
            "Aha, there's a familar face."
            mc "Hey Dawn, how's it going?"
            show dawn2 neutral with dissolve
            dawn2 "Oh, hello! I'm sorry, do I know you? I feel like I'd recognize you if I did."
            "Oh fuck, this isn't the Dawn I know, is it? The hair should have tipped me off."
            mc "Uhm, it's uh, I'm [playername], a friend of Lily's."
            show dawn2 happy with dissolve
            dawn2 "Oohhh, is that where you know me from?"
            show dawn2 neutral with dissolve
            dawn2 "Goodness! You're... You're one of the people that was involved in defeating Morrigan, right?"
            "The news about Morrigan's attack is only very vaguely public. It makes sense that she wouldn't know much about it."
            mc "Yeah, and all I have to show for it is this nifty scar on my chest."
            show dawn2 laughing with dissolve
            dawn2 "Awwhhh, darling... I must say, the scar is an attractive quality."
            mc "Oh, well, thank you so much Dawn."
            show dawn2 happy with dissolve
            dawn2 "Are you here to purchase anything? I just finished shopping myself..."
            dawn2 "If you were to be such a gentleman as to help a lady carry her bags home, you'd be welcome to a delicious cup of tea with me. I'd love to hear more about how you defeated the evil Morphling Queen."
            menu:
                "Yeah, let me just buy something quickly.":
                    $ dawnltr = 5
                    dawn2 "Okay, I'll come with you, but take your time."
                    show dawn2 happy with dissolve:
                        linear 1.0 xalign 0.1
                    jump marketmenu2
                "I'm in no rush, let me help you.":
                    mc "Here, let me take the heavy bag."
                    show dawn2 laughing with dissolve
                    dawn2 "Thank you so much, dearie."
                "Oh my god.":
                    show dawn2 neutral with dissolve
                    dawn2 "Hm? Did I say something alarming, dearie?"
                    mc "Sorry, I was just processing what you said."
                    show dawn2 horny with dissolve
                    dawn2 "Oh dear... Was I too forward?"
                    mc "No, no... I'll help you, here, let me take the heavy bag."
            label dawnvisit5setup:
                jump dawnvisit5

        "There's a market here, I wonder what I can buy?"
        label marketmenu:
            scene bg market with dissolve
        menu marketmenu2:
            "Equipment":
                if midnadiscount == 1:
                    show midna happy with dissolve
                    midna "Heyy, do you want something on sale, or do you want me?"
                    midna "Don't forget about that discount, I've docked my prices just for you."
                    if dawnltr == 5:
                        dawn2 "Huh, you're kinda popular, aren't you [playername]?"
                    menu  discountmenu:
                        "I have [monies] monies."
                        "Hook and Ropes - 50 monies" if rope == 0:
                            if monies < 50:
                                "I can't afford that."
                                jump equipmentshop
                            $ forestmonies += 10
                            $ rope = 1
                            $ monies -= 50
                            mc "I'll buy the hooks and ropes."
                            midna "Perfect choice, these reliable babies will get you down and deep where the good shit is."
                            mc "What's the good shit, may I ask?"
                            midna "Ores and gemstones, lover, that's where the mother lode is."
                            mc "I see..."
                            "I wonder if I'm in the wrong business."
                            jump equipmentshop
                        "Leather Armor - 130 monies" if leatherarmor == 0:
                            if monies < 130:
                                "I can't afford that."
                                jump equipmentshop
                            $ forestmonies += 10
                            $ leatherarmor = 1
                            $ monies -= 130
                            mc "This armor seems like it'll fit me, I'll get it."
                            midna "The ideal armor, allows great flexibility and mobility."
                            midna "Precisely what you need against an unpredictable foe."
                            mc "Yeah, definitely want to stay agile in the caves."
                            midna "Exactly, metal shit is just gonna echo and make you a target."
                            jump equipmentshop
                        "Scimitar - 240 monies" if scimitar == 0:
                            if monies < 240:
                                "I can't afford that."
                                jump discountmenu
                            $ forestmonies += 10
                            $ scimitar = 1
                            $ monies -= 240
                            mc "This weapon seems decent but not overkill, I'll take it."
                            midna "Ah yes, this weapon is the perfect balance of 'fuck off, I'm dangerous' and 'easy to carry'."
                            midna "Trust me, flash this baby and no basic bitch creature within an eight mile radius will want anything to do with you."
                            mc "Seems perfect, I'm not actually looking for a fight."
                            midna "Aye, I'm with you on that one. Much easier to shine silver and go separate ways."
                            jump discountmenu
                        "You" if midnayou == 0:
                            $ midnayou = 1
                            midna "Heh, you're such a perv 'master'."
                            midna "Try asking again if you see me at the bar."
                            jump discountmenu
                        "Back":
                            hide midna with dissolve
                            jump marketmenu2
                if marketequipmentvisit == 0 and buttersforestvisit4 == 1:
                    $ marketequipmentvisit = 1
                    $ midnaflirt = 0
                    "This is where Butters wanted me to get some equipment, let's see what's on offer."
                    show midna with dissolve
                    merchant "You gonna buy anything, or just waste my time?"
                    mc "Hey, got anything good for cave spleunking?"
                    merchant "For a punk like you? Cave diving isn't a leisurely walk in the park, even around 'Cadia."
                    mc "Yeah, I know. Looking for ways to get deeper and fend off slimes and other pests."
                    if dawnltr == 5:
                        dawn "Cave diving should be easy for [playername]! Just check out his fancy scars from a past battle."
                    merchant "Hmm, actually... You seem like you know your shit."
                    merchant "Here, I've got some good stuff under the counter, not just ropes, I mean weapons."
                    merchant "Slime girl or insect girl sees you with one of these? They'll flee without fight."
                    merchant "S'not like they've got hospitals down there mate."
                    mc "I like your style, what's your name?"
                    midna "Name's Midna, and you?"
                    mc "[playername], we'll be doing business a few times, so it's good to get acquainted."
                    jump equipmentshop
                elif marketequipmentvisit == 1:
                    show midna with dissolve
                    midna "Hey again, need something?"
                else:
                    "There're weapons and armor here, I have no use for that, I think."
                    jump marketmenu2
                label equipmentshop:
                    if rope == 1 and leatherarmor == 1 and scimitar == 1:
                        midna "Well shit, you bought everything I could possibly offer ya."
                        midna "Good luck out there man."
                    else:
                        pass
                menu equipmentshopmenu:
                    "I have [monies] monies."
                    "Hook and Ropes - 60 monies" if rope == 0:
                        if monies < 60:
                            "I can't afford that."
                            jump equipmentshop
                        $ forestmonies += 10
                        $ rope = 1
                        $ monies -= 60
                        mc "I'll buy the hooks and ropes."
                        midna "Perfect choice, these reliable babies will get you down and deep where the good shit is."
                        mc "What's the good shit, may I ask?"
                        midna "Ores and gemstones my friend, that's where the mother lode is."
                        mc "I see..."
                        "I wonder if I'm in the wrong business."
                        jump equipmentshop
                    "Leather Armor - 140 monies" if leatherarmor == 0:
                        if monies < 140:
                            "I can't afford that."
                            jump equipmentshop
                        $ forestmonies += 10
                        $ leatherarmor = 1
                        $ monies -= 140
                        mc "This armor seems like it'll fit me, I'll get it."
                        midna "The ideal armor, allows great flexibility and mobility."
                        midna "Precisely what you need against an unpredictable foe."
                        mc "Yeah, definitely want to stay agile in the caves."
                        midna "Exactly, metal shit is just gonna echo and make you a target."
                        jump equipmentshop
                    "Scimitar - 250 monies" if scimitar == 0:
                        if monies < 250:
                            "I can't afford that."
                            jump equipmentshop
                        $ forestmonies += 10
                        $ scimitar = 1
                        $ monies -= 250
                        mc "This weapon seems decent but not overkill, I'll take it."
                        midna "Ah yes, this weapon is the perfect balance of 'fuck off I'm dangerous' and 'easy to carry'."
                        midna "Trust me, flash this baby and no basic bitch creature within an eight mile radius will want anything to do with you."
                        mc "Seems perfect, I'm not actually looking for a fight."
                        midna "Aye, I'm with you on that one. Much easier to shine silver and go separate ways."
                        jump equipmentshop
                    "Flirt with Midna" if midnaflirt == 0:
                        if dawnltr == 5:
                            "I would love to flirt with Midna, but in front of Dawn? Nah..."
                            jump equipmentshopmenu
                        $ midnaflirt = 1
                        mc "You're cute, want to hang out sometime?"
                        midna "Cute? Come on, that's such basic shit, be honest with me."
                        mc "I like your aggressive and pushy attitude, I think you'd be fun to bash horns with."
                        midna "Hell yeah brother, meet me in the bar sometime, I'll buy you a drink, and we'll talk."
                        $ midnabar = 1
                        jump equipmentshop
                    "Back":
                        hide midna with dissolve
                        jump marketmenu2
            "Gifts":
                if dawnltr == 5:
                    jump pregiftshop
                elif agathasoniathreesome == 1 and arisex == 0:
                    label arisex:
                        pass
                    $ arisex == 1
                    show ari neutral with dissolve
                    ari "Hey, whatchu buyi-haaaaaaah!"
                    ari "It’s you!"
                    mc "Huh? Do you have something to say to me?"
                    ari "Yeh! I’ve got a mouthful for you… Grrr…"
                    ari "Grrrrrr…"
                    "Hmm… She’s just growling at me. I must have really pissed her off… What did I do?"
                    show ari sad with dissolve
                    ari "I can’t believe you slept with my sisters!"
                    mc "S-Sisters?! Wait, so…"
                    show ari neutral with dissolve
                    ari "T-That was incestuous! Unforgivable, you god damn player!"
                    ari "Devil, seducer, incubus! I can’t believe it!"
                    mc "I’m sorry, I didn’t realize you were all related!"
                    show ari sad with dissolve
                    ari "Yes, we are! You can’t just go around sleeping with whoever you want and not expect consequences!"
                    "My tail chasing ways have finally caught up to me, is this the end? ( T n T )"
                    show ari neutral with dissolve
                    ari "Grrr… I was the one interested in you the most, I wanted to sleep with you first! It’s not fair! Why do the good men always sleep with those two sleazy sluts over me!"
                    mc "Wait… WHAT?!"
                    show ari sad with dissolve
                    ari "This is unforgivable, you must take responsibility and make things right. Otherwise, my heart may remain cracked forever…"
                    "..?"
                    "What kinda tsundere shit is this? This girl refused all my advances before!"
                    show ari neutral with dissolve
                    ari "*Sigh* Must I instigate everything?"
                    ari "There’s a back alley over there, wanna do it?"
                    menu:
                        "The ol' fuck and chuck. Alright, sure.":
                            pass
                        "Sounds like you're taking the idea of being a cum dumpster literally.":
                            show ari sad with dissolve
                            ari "Come on, you already cucked me with both of my sisters."
                            mc "Uuuuhhhhh… Alright, fine."
                        "Fuck in an alleyway? Even I have higher standards than that.":
                            show ari horny with dissolve
                            ari "Don't you like the thrill of almost getting caught? I bet it'll be exciting."
                            "She raises a good point, I've slept with a lot of mares, but I've never tried anything in public."
                            mc "Uuuuhhhhh… Alright, fine."
                    "Have I always been this much of a degenerate?"
                    show ari happy with dissolve
                    ari "Hey Midna, can you watch over my stall for a few minutes?"
                    show midna happy with dissolve:
                        xpos 100
                        ypos 25
                    midna "Ayy, don’t have too much fun!"
                    stop music fadeout 3.0
                    scene bg arcadiaalley with dissolve
                    "Ari smiles almost lovingly as she takes my hand and leads me to a nearby alleyway near the river."
                    play music sex1 fadein 3.0
                    show ari horny with dissolve
                    "Taking advantage of a small nook behind a house, Ari presents herself to me with such glee it’s almost like we haven’t given up our dignity."
                    ari "I’ve been waiting for this moment, big boy…"
                    mc "Have you really?"
                    show ari sad with dissolve
                    ari "Well… Now that my sisters beat me to the punch, yeah! I was saving you like damn fine wine, and they just had to go and fucking blow off the cork."
                    ari "Now I gotta finish you off before you go flat."
                    "Am I being objectified?!"
                    "Unsure of who’s taking advantage of who, I position myself behind her bountiful rear."
                    "If someone were to look in the alley, they could probably see, but I’ve already committed."
                    show ari happy with dissolve
                    ari "Mmm, I would have liked better circumstances, but if it’s with you… I don’t mind…"
                    "Why is she so happy? Her heart melting smile totally doesn’t fit this trashy situation."
                    "I bring a finger to her crotch and start to rub her labia, as I anticipated she isn’t wet enough yet."
                    "Even though she’s a lustful mare, this turn of events was quite sudden, so she needs some gentle loving to warm her up."
                    "So here I am, rubbing a mare’s pussy in the back of an alley. She leans back into my rubbing fingers, bites her lip and groans."
                    show ari horny with dissolve
                    ari "Ahh… F-Foreplay? Mmphh… If you insist, ehehe!"
                    "She plays with her breasts, squeezing her perky nipples; while I rub her clit for about thirty seconds, inducing thigh quivering pleasure within her."
                    "Gauging whether she’s ready, I move to sink a single finger inside her warm pussy…"
                    "She’s… really tight! As I slide the finger deeper inside, I’m met with some resistance."
                    mc "Ah- Are you a virgin?"
                    show ari sad with dissolve
                    ari "Mmmh… N-No! It’s just… I don’t do it very often…"
                    "She relaxes a little, and my second finger slips in. I take the opportunity to gently finger her as she slowly eases to the girth. Just a little more and she’ll be ready for my cock."
                    show ari sad with dissolve
                    ari "I’m not like my sisters, you know! I don’t go to the nightclub and pick up men… I’m not good enough at socialising to do that, I don’t know how to pick up on social cues very well…"
                    mc "If you’re not like them, then why are we here in the alley...?"
                    show ari horny with dissolve
                    ari "S-So that’s why, when you came up to me at the market, I thought maybe you could be a special guy... Someone I’d finally have all to myself, without my sisters behaving like… well… my sisters…"
                    show ari sad with dissolve
                    ari "Agatha thinks she’s a damn succubus seductress, and Sonia? She’s just stupid and sleazy…"
                    mc "Mm… You should have been clearer in your intentions…"
                    ari "S-Sorry… I-I’m kinda overtalking…"
                    ari "Truth is, a lot of this happened in my head. However, in reality… I acted cold and aloof as a defense mechanism."
                    show ari horny with dissolve
                    ari "Uuuhh, I wanted you, but… Heh, it’s a little twisted, but I-I would have never been able to get you if it wasn’t for my sister’s acting first."
                    ari "Their dumbassery gave me the courage to make a move."
                    "She could have picked a better first move… Throughout this small conversation her pussy has gotten a little warmer and a lot wetter. I think she’s ready."
                    show ari happy with dissolve
                    ari "I don’t care about them anymore. I’m going to focus on myself, and finally do what I want!"
                    mc "That’s the spirit, use this as a stepping stone to overcome your weakness."
                    show ari horny with dissolve
                    ari "Mmhm… S-So, that’s why I want you to take my virginity…"
                    stop music fadeout 1.0
                    "She's a virgin?!"
                    menu:
                        "What?!":
                            show ari sad with dissolve
                            ari "C-Come on, you’re not getting cold feet, are you?"
                        "You said you weren't a virgin!":
                            show ari sad with dissolve
                            ari "What difference does it make? I still want this!"
                        "You lied to me!":
                            show ari sad with dissolve
                            ari "It was just a little white lie, please don't be mad..."
                    "Why did this have to be in an alleyway? It’d be hot if it was Moxie or someone more experienced, but I can’t help but pity this girl."
                    mc "Sorry Ari, I… I can’t do it."
                    ari "B-But… W-What about the stepping stone?!"
                    "Ahh, she’s going to cry!"
                    mc "Wouldn’t you prefer to have your first time in a bed?"
                    show ari neutral with dissolve
                    ari "Mmm… But I need to tend to my stall, I can only expect Midna to watch over it for so long…"
                    menu:
                        "An alleyway is no place to lose your virginity, least not with a stranger.":
                            show ari sad with dissolve
                            ari "What's wrong with it? It's just... y'know, sex."
                        "I don't want you to regret this.":
                            show ari sad with dissolve
                            ari "Eugh, don't look down on me just because I'm inexperienced. This is something I really want to do."
                        "Sheesh, you really are impatient. But I like that.":
                            show ari horny with dissolve
                            ari "So... Do you want me to bend over?"
                    mc "Hm…. I have an idea. There’s a wagon near here, and a nice bed..."
                    if fr == 1:
                        "Fortunately, Moxie is with Lily today, so the wagon should be free."
                    else:
                        "Moxie is out right now, so I take Ari to the wagon."
                    scene bg black with dissolve
                    "..."
                    play music sex1 fadein 3.0
                    show arib sex
                    show ari sex1
                    with dissolve
                    ari "Mm… This bed is really comfy… But, is this really okay?"
                    mc "Of course, I want you to have the best experience for your first…"
                    "Especially after she hyped it up so much."
                    "Wow, she’s really wet now. I guess that ol’ horny mare thing finally kicked in, should be pretty easy to penetrate her now."
                    ari "Okie, I’m ready for you!"
                    "I kneel down beside her butt and grab hold of the horny mare’s hips to pull her a little closer."
                    "My cock was already anticipating the act and had been growing hard ever since we entered the bedroom."
                    play sound cum
                    show ari sex2 with dissolve
                    "In a mere moment the tip of my erection is pressed up against her lustful virgin pussy. Pushing forward, I feel her nether lips part around my girth."
                    "Ari gasps and squirms slightly, her fingers digging into the bedsheets as she happily watches the action."
                    "I push myself to the hilt and allow my lover’s tightness to ease around my shaft, her pussy constantly clenching and squeezing around me as she grows comfortable with the sensation."
                    ari "Mmm, it feels pretty good… I’m getting really turned on, hehe…"
                    mc "You mares sure take your first times well."
                    ari "And are you speaking from experience? Hmm? Hehe. I think I'm ready for you to start moving."
                    play ambience sex fadein 3.0
                    "Going steady, I start to rock back and forth. Her pussy gradually yields and my cock becomes slick with her juices, allowing me to increase the pace of each thrust."
                    "She rubs and spreads her ass slightly with her left hand as she gives into the pleasure, moaning and giggling alongside each thrust."
                    ari "Ahh, ahhh… ahhh! Hehe, it’s starting to feel really, really good!"
                    "I keep working my hips… *Thwap, slap, thwap* Now fucking with enough intensity that my skin slaps  against her butt, and her body rocks up and down the bed."
                    "The feeling of her insides become even more pleasurable over time as they become warmer and wetter. The point of our connection squelching with the lewd sounds of her juices as her tight lips grip around my shaft."
                    "I start to rub her swollen clit while fucking her simultaneously, upping the sex from merely pleasureful, to electrifyingly euphoric for my lover."
                    show ari sex3 with dissolve
                    ari "Hehe, heh, w-woah! I-I’m gonna c-come if you k-keep- ahh, haah!"
                    "She moans happily and her pussy squeezes my cock tightly as she begins to come hard."
                    "The tightness in turn causes my cock to throb and stiffen, almost creating a feedback loop that intensifies my pleasure."
                    "With a familiar tension building in my groin, I methodically pound Ari’s pussy as I push for my climax."
                    play sound cum
                    show ari sex4 with cum
                    play sound cum
                    show ari sex4 with cum
                    "My cock pulsates as my pleasure peaks; my vision goes white and my cock unleashes a spray of hot cum into the once virgin."
                    play sound cum
                    show ari sex4 with cum
                    play sound cum
                    show ari sex4 with cum
                    stop ambience fadeout 6.0
                    ari "Aahh, ahhh! Y-Yes, cum in me! F-Fuck! Ahh, aaahhh!"
                    "Ari moans even more, almost as if the realisation of being creampied had intensified her own orgasm."
                    "Her entire body quivers as we fuck out the rest of our orgasms until I’ve unloaded every ounce of my cum into her."
                    stop music fadeout 3.0
                    show ari sex5 with dissolve
                    "With the act done, I lay down on the other pillow of the double bed and we both catch our breath in the afterglow."
                    ari "Hehe, I can feel it drip…"
                    mc "Mm? The cum?"
                    ari "Yeah… I really enjoyed that, [playername]…"
                    ari "Thank you for making my first time so great. Your consideration… it made me really happy."
                    mc "Awwhh… Come here."
                    "We spend a few minutes snuggling together, although I know she can’t stay long."
                    ari "I’m sorry for being such a pain…"
                    mc "Don’t apologize for giving me a good time."
                    ari "You’re so sweet. I better go back to my stall, but, uhm…"
                    mc "Hm? Do you want to do this again sometime?"
                    ari "Actually, I want you to come back to the market with me."
                    mc "Oh? Sure, let’s make tracks then."
                    scene bg black with dissolve
                    play ambience ambienceday fadein 3.0
                    play music day fadein 3.0
                    scene bg market with dissolve
                    "She stays suspiciously hush yet happy as we return to the market stall, she doesn’t keep her intentions hidden for very long though."
                    show ari happy with dissolve
                    ari "Here, this is for you."
                    "She picks out a bouquet of roses and gives it to me."
                    mc "For me? That’s so kind of you!"
                    ari "Am I kind, hm? Perhaps I’m selfish, because I just wanted to see you smile again, hehe."
                    ari "L-Look... I know I saw you with Moxie before, and I know about the things you did with Sonia and Agatha…"
                    ari "So I’d like for you to perhaps pass these roses on to someone you care about, to share the love and happiness."
                    menu:
                        "Sure thing, I'll spread the love.":
                            $ roses += 1
                            pass
                        "Is keeping them not an option?":
                            $ roses += 1
                            ari "That’s also acceptable, hehe…"
                        "You should keep the roses, I don't want you getting the wrong idea.":
                            show ari neutral with dissolve
                            ari "I understand my position quite well. I haven't fallen for you, this is only a gesture of kindness."
                            ari "Perhaps you have the 'wrong idea'?"
                            ari "Well, whatever. I'll keep the roses. They'll be bought and love will be shared regardless."
                            "She's showing that colder side again."
                    show ari horny with dissolve
                    ari "Maybe we can do this again sometime…"
                    mc "Maybe... If that’s something you’d like, but it’d just be for fun."
                    show ari neutral with dissolve
                    ari "Mm, fun… You know, I never really thought I’d turn out to be like my sisters, but we’re cut from the same cloth I guess."
                    ari "Those two were bragging a lot about sleeping with ‘that furless man’, and how good you were in bed…"
                    "Has she had that chewing gum in her mouth this entire time?"
                    mc "You can still have fun like that while sticking to your morals. There’s a difference between sleeping around and having a normal sex life."
                    mc "What you need to ask yourself is, ‘what do you want out of life?’, and ‘what are you comfortable doing?’. From there, you can choose to live a fulfilling life."
                    mc "Although, if you ask me, sex is just a small thing that makes life a little more interesting. I wouldn’t worry about it too much, Ari."
                    show ari happy with dissolve
                    ari "Hm… I guess you’re right. You really were a stepping stone to help me understand myself a little better."
                    ari "Thank you, [playername]."
                    mc "You're welcome, Ari."
                    ari "Now then, back to business. Before you head out, is there anything you'd like to buy? You came here earlier and I didn't even give you the chance to ask."
                    $ arisex = 1
                    $ arisextoday = 1
                    jump giftshop
                if marketfirstvisit == 0:
                    "The market is mostly basic essentials that Moxie already purchases, although I recognize someone at one of the stalls."
                    show ari with dissolve
                    merchant "Hey, whatcha buying?"
                    mc "Hey, do I recognise you?"
                    merchant "Uhh, beats me, I certainly don't recognise you."
                    mc "Oh wait, you were with those other girls that were flirting with me."
                    merchant "Sonya and Agatha? Sounds about right."
                    mc "I'm [playername], I'm new around here and it's nice to meet you, what's your name?"
                    merchant "Trust me, if you're looking to flirt with a girl, I'm far harder work than those two."
                    mc "I was just asking for your name."
                    ari "Oh, well... I'm Ari."
                    ari "You looking to buy anything?"
                    mc "Sure, let's see what you've got."
                    ari "Lots of gifts this time of year, check it out."
                    $ marketfirstvisit += 1
                    jump giftshop
                else:
                    label pregiftshop:
                        pass
                    show ari with dissolve
                    if arisex == 1:
                        ari "Hey cutie, whatcha buying?"
                        if dawnltr == 5:
                            dawn2 "Cutie, huh?"
                            ari "Oh, uh... Hey, you're cute too."
                            dawn2 "Awwhhhh."
                    else:
                        ari "Hey, whatcha buying?"
                    menu giftshop:
                        "I have [monies] monies."
                        "Fancy Chocolates - 30 monies":
                            if monies < 30:
                                "I can't afford the chocolates."
                                jump giftshop
                            $ chocolates += 1
                            ari "Thanks champ."
                            $ monies -= 30
                            jump giftshop
                        "Bouquet of Roses - 75 monies":
                            if monies < 75:
                                "I can't afford the roses."
                                jump giftshop
                            $ roses += 1
                            ari "Thanks champ."
                            $ monies -= 75
                            jump giftshop
                        "Sex at the Wagon" if arisex == 1 and arisextoday == 0:
                            if dawnltr == 5:
                                "Dawn is with me right now, that's a really bad idea..."
                                jump giftshop
                            $ arisextoday = 1
                            ari "Sure... I could use a five minute break."
                            mc "I feel like there are better excuses at 8:00am."
                            ari "Come on, let's hurry before customers start to arrive!"
                            scene bg black with dissolve
                            "..."
                            play music sex1 fadein 3.0
                            show arib sex
                            show ari sex1
                            with dissolve
                            ari "Mm… I kinda feel bad for Moxie, using her bed like this."
                            mc "Ahh, it's okay. She practically encourages it."
                            ari "Hmm... I must admit, it's rather arousing to be fucked on a bed that you fuck other mares on."
                            "That was a strange comment... Anyway, she’s really wet now. Even though she's quite tight, it should be pretty easy to penetrate her now."
                            ari "Okie, I’m ready for you!"
                            "I kneel down beside her butt and grab hold of the horny mare’s hips to pull her a little closer."
                            "My cock was already anticipating the act and had been growing hard ever since we agreed to it."
                            play sound cum
                            show ari sex2 with dissolve
                            "In a mere moment the tip of my erection is pressed up against her lustful pussy. Pushing forward, I feel her nether lips part around my girth."
                            "Ari gasps and squirms slightly, her fingers digging into the bedsheets as she happily watches the action."
                            "I push myself to the hilt and allow my lover’s tightness to ease around my shaft, her pussy constantly clenching and squeezing around me as she grows comfortable with the sensation."
                            ari "Mmm, it feels pretty good… You really turn me on, hehe…"
                            play ambience sex fadein 3.0
                            "Going steady, I start to rock back and forth. Her pussy gradually yields and my cock becomes slick with her juices, allowing me to increase the pace of each thrust."
                            "She rubs and spreads her ass slightly with her left hand as she gives into the pleasure, moaning and giggling alongside each thrust."
                            ari "Ahh, ahhh… ahhh! Hehe, it’s feels really, really good!"
                            "I keep working my hips… *Thwap, slap, thwap* Now fucking with enough intensity that my skin slaps  against her butt, and her body rocks up and down the bed."
                            "The feeling of her insides become even more pleasurable over time as they become warmer and wetter. The point of our connection squelching with the lewd sounds of her juices as her tight lips grip around my shaft."
                            "I start to rub her swollen clit while fucking her simultaneously, upping the sex from merely pleasureful, to electrifyingly euphoric for my lover."
                            show ari sex3 with dissolve
                            ari "Hehe, heh, w-woah! I-I’m gonna c-come if you k-keep- ahh, haah!"
                            "She moans happily and her pussy squeezes my cock tightly as she begins to come hard."
                            "The tightness in turn causes my cock to throb and stiffen, almost creating a feedback loop that intensifies my pleasure."
                            "With a familiar tension building in my groin, I methodically pound Ari’s pussy as I push for my climax."
                            play sound cum
                            show ari sex4 with cum
                            play sound cum
                            show ari sex4 with cum
                            "My cock pulsates as my pleasure peaks; my vision goes white and my cock unleashes a spray of hot cum into her eager fuckhole."
                            play sound cum
                            show ari sex4 with cum
                            play sound cum
                            show ari sex4 with cum
                            stop ambience fadeout 6.0
                            ari "Aahh, ahhh! Y-Yes, cum in me! F-Fuck! Ahh, aaahhh!"
                            "Ari moans even, almost as if the realisation of being creampied had intensified her own orgasm."
                            "Her entire body quivers as we fuck out the rest of our orgasms until I’ve unloaded every ounce of my cum into her."
                            stop music fadeout 3.0
                            show ari sex5 with dissolve
                            "With the act done, I lay down on the other pillow of the double bed and we both catch our breath in the afterglow."
                            ari "Hehe, I can feel it drip…"
                            mc "Mm? The cum?"
                            ari "Yeah… I really enjoyed that, [playername]…"
                            ari "Mmm... As much as I'd like to cuddle, I think we both have somewhere to be..."
                            ari "Let's quickly head back."
                            scene bg black with dissolve
                            "..."
                            play music daytheme fadein 3.0
                            play ambience ambienceday fadein 3.0

                            scene bg market with dissolve
                            show ari happy with dissolve
                            ari "Don't expect a free bouquet every time."
                            jump giftshop
                        "Flirt with Ari.":
                            if dawnltr == 5:
                                "It just doesn't feel right flirting with Ari in front of Dawn... Sorry Ari!"
                                jump giftshop
                            if arisextoday == 1:
                                show ari horny with dissolve
                                ari "Oohh, we've already had sex today! Teasing me more is just bullying! Hehe."
                                jump giftshop
                            if arisex == 1:
                                show ari happy with dissolve
                                ari "Oooh, hehe... Stahp it you!"
                                ari "If you wanna bang me, just let me know instead of teasin'."
                                jump giftshop
                            if ariflirtcounter <= 1:
                                menu:
                                    "Wow, you could grate cheese on those abs!":
                                        "She rolls her eyes when she hears my literally cheesy attempt at flirting."
                                        ari "Oh, really?"
                                        ari "Come on, this is nothing, you're over exaggerating."
                                        ari "I'm nothing like those farmer girls that deliver crops here."
                                        $ ariflirtcounter += 1
                                    "Your hair is gorgeous!":
                                        "She shrugs and flicks her hair around to show off her absurdly long twintails."
                                        ari "You think?"
                                        ari "It takes me a long time to get it looking this nice every morning."
                                        ari "Thank you I guess."
                                        $ ariflirtcounter += 1
                                    "You have nice boobs.":
                                        "She seems briefly surprised by my sudden comment, before looking down at her bosom and nodding."
                                        ari "I do, don't I? Not too big, not too small."
                                        $ ariflirtcounter += 1
                                jump giftshop
                            else:
                                ari "You clearly seem interested in me judging by your flirting, but I'm busy working."
                                ari "And anyway, you don't seem like you'd be much fun. I-Idiot..."
                                ari "Maybe you should go bother Agatha and Sonia instead..."
                                "I guess she's not interested. Oh well, can't have them all."
                                "Agatha and Sonia, are those the other mares that were with her when we first encountered?"
                                jump giftshop
                        "Back":
                            hide ari with dissolve
                            jump marketmenu2
            "Muffins":
                scene bg market with dissolve
                if bavcl == 1 and sandysex == 0:
                    jump doubledragon
                elif cindymet == 0:
                    jump cindymeet
                elif cindysex == 1 and bavcl == 0:
                    "Cindy has flown away. She’ll probably be back tomorrow, especially if I keep giving her lucrative opportunities."
                    jump marketmenu
                elif bakeryvisit1 == 1 and cindylum == 1:
                    if bavcl == 0:
                        play music toewizard
                        $ bavcl = 1
                        show cream happy:
                            xpos 200 ypos 40
                        show cindyb:
                            xpos 550 ypos 40
                        show cindy happy:
                            xpos 550 ypos 40
                        with dissolve
                        cream "Yup; no quota either. if they sell, they sell, if they don’t, I simply didn’t make them tasty enough!"
                        cream "Oh, hey [playername]! It’s so great to see you! Would you like to be our first customer?"
                        mc "Hey you two. Whatcha selling? Muffins, by any chance?"
                        ci "[playername]! I’m a full-time muffin employee for Cream now!"
                        mc "That was quick. So, you’re just out here selling some of her products?"
                        ci "Yup! And the pay is consistent! This should be much better than my own failed venture."
                        cream "Yeah, I thought it’d be a good idea to have a quick and easy alternative than coming in to the bakery. It’s like a drive through!"
                        ci "That’s right! How about it, want a muffin? They’re super tasty, I’d know, I just tried one!"
                        mc "I may just! Thank you, girls."
                        cream "No problemo! I’m going to open up the bakery now, I’ll see you two beauties later."
                        mc "Later!"
                        ci "Byeee!"
                        hide cream with dissolve
                        ci "So, muffins, or me? I'm free, hehe."
                        jump cimuffinmenu2
                    else:
                        play music toewizard
                        show cindyb
                        show cindy happy
                        with dissolve
                        ci "Hey, want some muffins?"
                        menu cimuffinmenu2:
                            "(There is literally no reason to actually buy muffins)."
                            "Blueberry Muffin – 5 Monies" if monies > 4:
                                $ monies -= 5
                                ci "Thanks for your purchase!"
                                "They certainly taste nice."
                                jump cimuffinmenu2
                            "Raisin Muffin – 5 Monies" if monies > 4:
                                $ monies -= 5
                                ci "Thanks for your purchase!"
                                "They certainly taste nice."
                                jump cimuffinmenu2
                            "Sex":
                                ci "I suppose I could spare a few minutes. Wouldn’t want to get overheated in this hot sun!"
                                menu:
                                    "Reverse Cowgirl":
                                        jump cindyrcg
                                    "Lingerie Leg up Missionary":
                                        jump cindylum
                                    "Changed my mind":
                                        ci "Oookay then."
                                        jump cimuffinmenu2
                            "Back":
                                ci "Later!"
                                play music daytheme fadeout 3.0
                                jump marketmenu

                show cindyb
                show cindy happy
                with dissolve
                play music toewizard
                ci "Hey, want some muffins?"
                menu cimuffinmenu:
                    "Blueberry – (Reverse Cowgirl) – 50 Monies" if mhag == 0 and monies >= 50:
                        $ monies -= 50
                        jump cindyrcg
                    "Raisin – (Lingerie Leg Up Missionary) – 75 Monies" if mhag == 0 and cindyrcg == 1 and monies >= 75:
                        $ monies -= 75
                        jump cindylum
                    "Blueberry – (Reverse Cowgirl) – 45 Monies" if mhag == 1 and monies >= 45:
                        $ monies -= 45
                        jump cindyrcg
                    "Raisin – (Lingerie Leg Up Missionary) – 67 Monies" if mhag == 1 and cindyrcg == 1 and monies >= 67:
                        $ monies -= 67
                        jump cindylum
                    "Back":
                        ci "Awh, later!"
                        play music daytheme fadeout 3.0
                        jump marketmenu
                label cindymeet:
                        $ cindymet = 1
                        stop music fadeout 1.0
                        "There’s a stall that sells muffins over here, they look kinda tasty too!"
                        "But that’s not what caught my eye…"
                        show cindyb
                        show cindy neutral
                        with dissolve
                        "Is the person running this stall, a dragon?"
                        "I take a few moments to admire her form. Starting from the horns at the top, I drink in every detail of her wings, scales, abdomen…"
                        play music toewizard fadein 5.0
                        show cindy angry with dissolve
                        unknown "Hey, shop with your money, not your eyes!"
                        mc "Ah… Sorry, I’ve just never seen a dragon before. You are a dragon, right?"
                        show cindy neutral with dissolve
                        ci "*Sigh*… Yup, I’m Cindy… Can’t say I’ve ever seen whatever you’re supposed to be either, enlighten me?"
                        mc "I’m [playername], a human."
                        show cindy happy with dissolve
                        ci "A human! I guess we’re both seeing a first today."
                        mc "I see you sell some delicious things, but you don’t mind if I just get to know you a little, do you?"
                        show cindy laughing with dissolve
                        ci "Not at all, in fact that’s great! You can ask me anything you’d like."
                        $ cibn = 0
                        $ ciwf = 0
                        $ cifl = 0
                        label cindytalkmenu1:
                            show cindy happy with dissolve
                            if cibn == 1 and ciwf == 1 and cifl == 1:
                                jump postcindytalkmenu1
                        menu:
                            "If you’re a dragon, why do you have breasts and nipples?" if cibn == 0:
                                $ cibn = 1
                                show cindy angry with dissolve
                                ci "Have you been staring at them?"
                                "She nonchalantly squeezes them together and winks at me."
                                show cindy neutral with dissolve
                                ci "These tiny milkers are used to feed our young, just like any other mammal."
                                ci "I’m not producing any milk right now, but it’s still fun to have people suck on them."
                                mc "Dragons are mammals? Interesting!"
                                jump cindytalkmenu1
                            "Where are you from?" if ciwf == 0:
                                $ ciwf = 1
                                show cindy neutral with dissolve
                                ci "I’m from the Dragon Lands. Land of dragons. It’s about a three hour’s fly away."
                                show cindy happy with dissolve
                                ci "Although I actually live in Dragon Town C, which is an hour flying away to the east."
                                show cindy neutral with dissolve
                                ci "We dragons aren’t exactly known for our naming conventions. Our culture likes to keep language simple."
                                mc "I can tell. There’s some merit in that simplicity, though."
                                mc "And you fly for an hour just to come and set up a market stall here?"
                                show cindy laughing with dissolve
                                ci "Yep! I just started when heat season began."
                                show cindy happy with dissolve
                                ci "I’m here to try and make the big bucks. 50 monies here is like 100 dragon dollars, so I want to make some money providing my services to help out my family."
                                mc "Hey, that’s a pretty good idea."
                                show cindy neutral with dissolve
                                ci "Yeah, things are a little rough at the moment though… Not many customers."
                                jump cindytalkmenu1
                            "(Flirt with Cindy)" if cifl == 0:
                                mc "I bet you and I are going to get along like a furnace."
                                show cindy neutral with dissolve
                                ci "A furnace?"
                                mc "Because when we get turned on, there’s bound to be flames."
                                show cindy horny with dissolve
                                ci "Oohhh… That was good, maybe even the best pickup line I’ve received…"
                                ci "Maybe I’ll let you get bizzy with the lizzy…"
                                show cindy laughing with dissolve
                                ci "Don’t be expecting a freebie from my stall though!"
                                $ cifl = 1
                                jump cindytalkmenu1
                            "(Conclude conversation)":
                                pass
                        label postcindytalkmenu1:
                            "As we chat and I get to know the dragon girl, no other customers seem to be interested."
                            if bakeryvisit1 == 1:
                                "And while I keep my thoughts to myself, selling muffins can’t be easy with such an amazing bakery seconds away."
                            show cindy neutral with dissolve
                            ci "Seems like it'll be another quiet day… Thanks for giving me some brief company."
                            show cindy happy with dissolve
                            ci "So, what about you? Care for a muffin, [playername]?"
                            mc "They look pretty tasty, how much?"
                            "I say they look tasty, but up close they actually look pretty stale."
                            show cindy laughing with dissolve
                            ci "I have a special offer on right now! Fifty monies each!"
                            mc "Fifty?! That’s so overpriced! What gives?"
                            show cindy angry with dissolve
                            ci "Overpriced? Well excuuuuuse me!"
                            mc "What kind of special offer is that? Buy one pay twice?"
                            show cindy neutral with dissolve
                            ci "What are you talking about? You idiot! If you buy one, you get to have sex with me!"
                            mc "Oohh… Muffin prostitution…?"
                            show cindy angry with dissolve
                            ci "Hmph, I just don’t get it! I heard that interspecies creatures are supposed to be ‘popular’ here, but I haven’t had a single person buy any yet."
                            ci "At this rate, I won’t be able to cover the cost of the stall…"
                            mc "I think you’ve misunderstood, {i}male{/i} creatures are popular in Arcadia."
                            show cindy neutral with dissolve
                            ci "Male? Damnit… What am I going to do with all these muffins now?"
                            "Fifty monies to sleep with a dragon? Hmm…"
                            $ mhag = 0
                            menu:
                                "(Haggle her down)":
                                    $ mhag = 1
                                    mc "Maybe if you lower your prices, people would be more interested. Like, me for instance."
                                    show cindy angry with dissolve
                                    ci "Lower my prices? But…"
                                    show cindy neutral with dissolve
                                    ci "Well… What if you had a ten percent discount?"
                                    mc "Sounds agreeable. What was on the menu, again?"
                                    show cindy happy with dissolve
                                    ci "Uhmm, just muffins, and me!"
                                    jump cimuffinmenu
                                "I’ll buy your muffins; I couldn’t resist the opportunity to sleep with a dragon.":
                                    show cindy happy with dissolve
                                    ci "Thank you! At this price, I only need to sell two of them to make a profit!"
                                    jump cimuffinmenu
                                "Well, good luck finding some customers.":
                                    show cindy neutral with dissolve
                                    ci "Thanks…. If you ever change your mind, I’ll be here trying to recoup costs for a while."
                                    play music daytheme fadeout 3.0
                                    jump marketmenu
                label cindyrcg:
                        $ cindysex = 1
                        $ cindyrcg = 1
                        if cindyrcg1 == 0:
                            show cindyb:
                                xalign 0.5 yalign 0
                            show cindy laughing:
                                xalign 0.5 yalign 0
                            with dissolve
                            ci "*Gasp* Finally! My first customer!"
                            "Cindy hands me a single blueberry muffin, while she quickly puts the others into a lockbox, and padlocks it under the market stall."
                            "The muffin isn’t very fresh, it’s probably not even edible, so I just leave it on the stall. Cindy doesn’t seem to mind as she walks to my side and nods."
                            show cindyb:
                                linear 0.5 xalign 0.1
                            show cindy happy:
                                linear 0.5 xalign 0.1
                            with dissolve
                            ci "Okay, let’s go wander over there, we’ll get some privacy."
                            "She points in the general direction of the forest."
                            mc "We’re going to do it outside?"
                            show cindy laughing with dissolve
                            ci "Where else? There’s no way I can carry you while I fly home."
                            mc "Hm…"
                            show cindy happy with dissolve
                            ci "No refunds!"
                            mc "Guess I’ve committed, so lead the way."
                            show bg arcadiasuburbs
                            show cindy laughing
                            with dissolve
                            ci "Are you excited to sleep with a dragon? I know I am! Excited- about, uh, not sleeping with a dragon, but having a customer!"
                            mc "Yeah, I’ve never even met a dragon before you, there’s no way I can miss this chance."
                            show cindy happy with dissolve
                            ci "It’ll be worth every money, I promise!"
                        else:
                            show cindy laughing with dissolve
                            ci "Great! Let’s get off then, shall we?"
                            mc "We certainly shall be getting off! Lead the way."

                        scene bg forest with dissolve
                        "Cindy and I arrive at a comfortable area that’s just deep enough into the forest to ensure no one stumbles upon us."
                        show cindyb
                        show cindy happy
                        with dissolve
                        ci "Okay, lie down for me and I’ll do my thing!"
                        play music sex1 fadein 3.0
                        show cindy rcg1 with dissolve
                        "Despite requesting me to do so, she takes charge by gently lowering me onto my back. The further I fall the better the view I get of her puffy pussy."
                        "Her nether lips already blossoming with desire, and dripping with some lustful residue."
                        "She kneels down over me, and initially brings a hand between her legs to gauge her wetness, moaning as she fervently schlicks."
                        ci "Oh fuck... I'm so wet."
                        "Not one to forget about my involvement, her breasts are pushed into my face. I take one of her perky nipples and start to suckle it."
                        ci "Ooohh, oooo… Okay, I’m ready for that thick cock."
                        mc "And it’s ready for you. Show me what you’ve got, dragon girl."
                        ci "You’re gonna get it, human man!"
                        "She shifts her body into a position where her lustful labia drips warm fluid over my hardening member."
                        "Each drip isn’t just warm, but arguably hot, and as the soft scaly labia presses against my slick shaft the true nature of the warmth is realised."
                        if cindyrcg1 == 0:
                            "The core temperature of a dragon must be leagues above a typical human, as simply having my cock resting against her wet lips is equivalent to a hot bath, at a temperature I can just barely handle."
                        else:
                            "The core temperature of the dragoness is leagues beyond a typical human, and simply having my cock resting against her wet lips feels like a hot bath."
                        "Needless to say, but the hot touch only serves to arouse me further, as the tip of my cock leaks with some precum. This heat isn’t just a unique sensation, it promises to feel fantastic."
                        if cindyrcg1 == 0:
                            "Touch isn’t the only sense that is overwhelming, my eyes also have several beautiful sights to enjoy. My first ever view of a dragon’s vulva, and it’s notably different to a mare’s."
                        else:
                            "Touch isn’t the only sense that is overwhelming, my eyes also have several beautiful sights to enjoy. The gorgeous view of her soft, supple vulva nestled amidst her abdomen."

                        "Between her purple scales, a leotard like abdomen reaches all the way from her neck to her tail, perfectly accentuating her ass with a heart."
                        "This incredibly soft abdomen also encompasses her genitalia, giving her a cute innie pussy in which her pussy lips barely escape."
                        "And this wet softness is pushed against my cock as she teasingly grinds back and forth."
                        play sound cum

                        show cindy rcg2 with dissolve
                        "Almost entranced, I gasp as she raises her supple hips and immediately sinks herself down my shaft. Immediately accepting me with ease."
                        "My cock throbs and stiffens as the hot hug of her pussy encapsulates the entirety of my member. The heat of her pussy seemingly increasing the sensitivity, as I can feel each ridge and bump of her insides."
                        if cindyrcg1 == 0:
                            ci "Ooohh… The contrasting temperature… That feels pretty good, actually…"
                            "With all my thoughts as to how hot she feels, I hadn’t considered that I’d feel cold to her. It seems like we’ll both be able to enjoy these unusual hot/cold sensations together."
                        else:
                            ci "Ooohh… It’s like a cooling rod for my overheating cunt, ahaha…"
                        play ambience sex fadein 3.0
                        "Splaying her wings out as a theatrical counterbalance, she begins to shift her pussy up and down my member. All the way from the tip, to the hilt. With precision, she fucks herself on every inch of my cock."
                        "Despite how well she took my cock, her tightness is immense. Her lips just keep squeezing and constricting, and it takes me a while to realize that’s the pull of her abdomen every time she wags her tail back and forth."
                        if cindyrcg1 == 0:
                            "Additionally, her vaginal lubricants are so atypical from what I’ve seen before. As if to handle the intense heat of her pussy, the juices are thick, gooey and hot. Sliding down my cock like a viscous honey, but providing a great amount of give rather than stick."
                            "Having sex with a dragon is nothing like fucking a mare! This was worth every money."
                        else:
                            "Her thick, gooey and hot juices slide down my cock like a viscous honey, providing a great amount of give as she rides me faster and faster."
                            "As before, Cindy definitely makes this worth every penny. Dragonesses are awesome fucks."

                        if cindyrcg1 == 0:
                            ci "Ohh, look at your goofy faces… You’re really enjoying this, aren’t you?"
                            mc "I could say the same about you, Cindy."
                            ci "M-My faces aren’t goofy! Idiot! I’ll show you…"
                            "She begins to accelerate her riding as a way to ‘get back at me’. Her gooey girl cum splattering outwards with more intensity, and revealing just how much enjoyment she’s getting out of this."
                        else:
                            ci "It felt nice having your cum in me last time, so I want you to fill me with lots again today, okay?"
                            "She begins to accelerate her riding. Her gooey girl cum splattering outwards with more intensity and perhaps revealing just how much enjoyment she’s getting out of this."

                        "Her cute breasts rock in tandem with each thrust. At the tip of each breast she plays with her fully erect nipples, squeezing and tweaking them as a means to get herself off."
                        "Bouncing on me harder and faster, her breathing becomes noticeably ragged and her facial expression scrunches up as she seems to get closer to climaxing."
                        "First her thighs clench around me, then as she speeds up her riding, her pussy throbs and tightens as she pushes herself to a high."
                        ci "Ohh, ohhh lord… I'm coming… Ooohh…"
                        "My shaft is wrung by internal contractions as her blissfully hot pussy convulses wildly. All whilst she maintains an intense pace, bolstered by her flapping wings."
                        "Her pussy squelches with each rock of her hips, mixing with the sound of her supple abdomen slapping against my skin."
                        "My cock feels harder than ever as she repeatedly pounds against my pelvis, throbbing more and more, I can feel the weight of an orgasm rise in my loins."
                        "I give into the powerful urge to ejaculate. Letting my guard down, I allow that feeling to rise and consume my body in a feeling of hot euphoria."
                        play sound cum
                        show cindy rcg3 with cum
                        play sound cum
                        show cindy rcg3 with cum
                        "I throw my head back into the grass as I grab onto the dragoness’s hips and pump her full of cum."
                        play sound cum
                        show cindy rcg3 with cum
                        play sound cum
                        show cindy rcg3 with cum
                        stop music fadeout 5.0
                        ci "Ohhh, by the lords, yesss… Some cool soothing cum in my pussy! Ooohh, ohh…"
                        "Almost perfectly, my lover humps her hips back and forth to completely maximise the pleasure of my sensational orgasm."
                        stop ambience fadeout 3.0
                        "As the built tension of my orgasmic bliss fades, my release is combined with an instant coolness of air, as my cock is released from the vice-like grip of the dragoness’s warm insides."
                        show cindy rcg4 with dissolve
                        play music toewizard fadein 3.0
                        if cindyrcg1 == 0:
                            $ cindyrcg1 = 1
                            "She pulls out with a happy sigh, I half expect cum to drip from her nether, but the runny cum seems to have mixed with her thick juices preventing it from escaping the vagina… A clever little evolutionary quirk!"
                            ci "That feels so refreshing and cooling, ahhh… I was getting a little overheated."
                            mc "You’re telling me, I wasn’t expecting you to be that warm."
                            ci "Oh? Ehehe… Sorry about that, I should have mentioned how hot dragonesses can get in heat, especially since you’ve never met one before."
                            show cindyb cum
                            show cindy satisfied
                            with dissolve
                            "She stands up and stretches, so I wipe some sweat from my forehead and sit up."
                            "I expected us to cuddle for a while, but it seems we developed a bizarre relationship of sex before snuggling. Guess I did just pay for sex from a stranger."
                            show cindy happy with dissolve
                            ci "Alright. Is that everything? I guess I’ll head back."
                            mc "I guess so. I hope you had fun."
                            show cindy laughing with dissolve
                            ci "I certainly did! Maybe my luck is finally turning around."
                            show cindy happy with dissolve
                            ci "Hmm… If I get another customer, I’ll officially have my market stall paid off!"
                            ci "Hopefully, I'll have enough money for my sister soon."
                            show cindy laughing with dissolve
                            ci "You will come back, right? Ohh, I know!"
                            ci "I’ll invest some of the monies you gave me into some sexy lingerie. Next time, I’ll have something even better for you."
                            mc "Is that so? Well, with my interest piqued, I’ll have no choice but to come back."
                            show cindy happy with dissolve
                            ci "Woohoo!"
                            scene bg forest with dissolve
                            "Cindy takes off, flying away for the day. I guess she’s leaving her stall closed up."
                            "Seems like she only needs a single customer a day to keep herself going. Makes sense considering I basically paid her double my typical wage."
                            "But it's no wonder that she isn't getting any customers with a business operation like that."
                        elif bakeryvisit1 == 1 and cindylum1 == 1:
                            "She pulls out with a happy sigh, I half expect cum to drip from her nether, but the runny cum has mixed with her thick juices preventing it from escaping the vagina."
                            ci "That feels so refreshing and cooling, ahhh… Like a soft drink!"
                            mc "Speaking of which…"
                            "I wipe some sweat from my brow."
                            mc "I would love a cold, refreshing soft drink right now."
                            ci "Oh? Ehehe… Sorry about that, but no freebies! Maybe I’ll ask Cream to let me sell drinks."
                            "She stands up, stretches and I mimic her within a few seconds."
                            show cindyb cum
                            show cindy satisfied
                            with dissolve
                            ci "Alright. Is that everything? I guess I’ll head back."
                            mc "Yeah, hope you had fun."
                            show cindy happy with dissolve
                            ci "I certainly did! My luck has really turned around since I met you, thanks!"
                            mc "Is that so? I’m glad I could help you."
                            ci "Later [playername]."
                            scene bg forest with dissolve
                            "Cindy takes off, flying back to her stall."
                        else:
                            "She pulls out with a happy sigh, I half expect cum to drip from her nether, but the runny cum has mixed with her thick juices preventing it from escaping the vagina."
                            ci "That feels so refreshing and cooling, ahhh… Like a soft drink!"
                            mc "Speaking of which…"
                            "I wipe some sweat from my brow."
                            mc "I would love a cold, refreshing soft drink right now."
                            ci "Oh? Ehehe… Sorry about that!"
                            "She stands up, stretches and I mimic her within a few seconds."
                            show cindyb cum
                            show cindy satisfied
                            with dissolve
                            ci "Alright. Is that everything? I guess I’ll head back."
                            mc "I guess so. I hope you had fun."
                            show cindy happy with dissolve
                            ci "I certainly did! You might be my only customer, but my luck is turning around!"
                            mc "Is that so? I’m glad I can help you."
                            ci "Later [playername]."
                            scene bg forest with dissolve
                            "Cindy takes off, flying away for the day. I guess she’s leaving her stall closed up."
                        play music daytheme fadeout 5.0
                        jump worldmap
                label cindylum:
                        $ cindysex = 1
                        $ cindylum = 1
                        if cindylum1 == 0:
                            show cindy laughing with dissolve
                            ci "Yesss! My luck has turned around ever since I met you! So, I decided that this one is going to be a real treat!"
                            show cindy happy with dissolve
                            ci "Like uhm, a member’s special bonus!"
                            mc "That sounds exciting, show me what you’ve got."
                            hide cindyb
                            hide cindy
                            with dissolve
                            "Cindy momentarily dips out of sight and under the wooden market stall, fumbling around with a small lockbox."
                            "She’s sure taking a while… What is she doing behind there?"
                            "And then she pops up!"
                            show cindyb lingerie
                            show cindy laughing
                            with dissolve
                            ci "Ta-da! What do you think? I bought it with the money from last time. Pretty snazzy, right? And totally fire proof!"
                            mc "Wow! That looks pretty nice."
                            "Admittedly it doesn’t really suit the dragoness, but the lingerie itself is nice, and the gesture is appreciated."
                            show cindy happy with dissolve
                            ci "Okie dokie, you know what’s up. Let’s go somewhere quiet."
                            "Awkwardly, we walk together to the woods while she nonchalantly wears the lingerie. No doubt catching the gaze of a few passing ponies."
                            hide cindyb
                            hide cindy
                            show midna
                            with dissolve
                            pause 0.5
                            hide midna with dissolve
                            show ari with dissolve
                            pause 0.5
                            hide ari with dissolve
                            "Oh my gosh, this is so awkward."
                            show spaowner neutral with dissolve
                            pause 0.5
                            hide spaowner with dissolve
                            show rikub
                            show riku embarrassed
                            with dissolve
                            pause 0.5
                            hide rikub
                            hide riku
                            with dissolve
                            "Gimmie a break…"
                        else:
                            show cindy laughing with dissolve
                            ci "Great! Let’s get off then, shall we? I’ll bring the lingerie with me."
                            mc "We certainly shall be getting off! Lead the way."

                        scene bg forest
                        show cindyb lingerie
                        show cindy happy
                        with dissolve
                        "Cindy and I arrive at a comfortable area that’s just deep enough in the forest to ensure no one stumbles upon us."
                        ci "Okay… This time I’ll lay down, and you can do {i}your{/i} thing to me."
                        play music sex1 fadeout 3.0
                        hide cindyb
                        show cindy legsup1
                        with dissolve
                        "She finds a comfortable patch of grass among the trees and lays down for me, raising her legs and then peeling her panties upwards to reveal her lustful labia."
                        "Her nether lips already blossoming with desire, and dripping with her wetness."
                        if cindylum1 == 0:
                            mc "You have such a nice pussy, you know that?"
                            ci "Hehe, no one has ever told me that, no…"
                            "She blushes and bashfully looks away."
                            ci "But I had another offer, since you paid me so much monies…"
                            ci "I’ll let you stick it in my butt, if you want…"
                            mc "You certainly could have said that more eloquently, but you definitely have me considering it."
                            ci "Pfft, sorry I’m not as smooth talking as you are, would you rather I say it like this:"
                            ci "Dearie, I’ll grace you with the privilege to ravish my derriere."
                            if boutiquevisit2 == 1:
                                mc "You know, I have friends that’d say something like that."
                                ci "Yeah yeah… Womanizer…"
                            else:
                                mc "Not bad; I can make a lady out of you yet!"
                                ci "Pfft, then hurry up and fuck me… You’re on a thirty-minute timer, ya dick."
                        else:
                            ci "Okie, wanna try the other option this time?"

                        menu:
                            "Vaginal":
                                "She takes a deep breath; I swear that some steam blows off her nose, as she grins and keeps her legs hoisted upwards for me."
                                "Using a hand to leverage her legs up, she uses it to spread her pussy slightly revealing some of her usually hidden pink lips."
                                "Straddling her thick tail, I position myself and my cock just before the upside-down heart of her butt."
                                if cindylum1 == 0:
                                    ci "C’mon! You’re moving slowly on purpose!"
                                    mc "Just admiring the view. With a body as sublime as this, you really have to savour every inch."
                                    ci "O-Ohh… Smooth talker…"
                                else:
                                    ci "You sure like staring at my pussy… So embarrassing, heh…"
                                    mc "There’s no reason to be ashamed of something so beautiful."
                                "She blushes and the tip of my cock brushes against her lips. As before, it’s extremely hot to the touch."
                                play sound cum
                                show cindy legsupv1 with dissolve

                                "I recoil initially, but bravely push onwards and force myself to adapt to the heat. Guiding my cock forwards, I sink into the heat of her warm pussy, grasping her ass at the area her scales turn into soft flesh as I do."
                                "Her pussy is even warmer inside, as it squeezes and envelopes my entire being. Plunging inwards to the hilt, I let out a satisfied sigh as if entering a bath of perfect temperature for the first time; this feeling really is something else."
                                "And Cindy feels the exact opposite, a satisfying cooling sensation emanating from her hot cunt, her muscles already contracting around my cock in response to the pleasure."
                                if cindylum1 == 0:
                                    ci "Oooohhh … I may need to start paying you at this rate… It’s sooo nice…"
                                    mc "Don’t give me any ideas, Cindy, heh."
                                    ci "Give it to me, I want you to make this worth every money, heh…"
                                else:
                                    ci "Oooohhh… I really want you to give me all you’ve got…"
                                play ambience sex fadein 3.0
                                "I nod as I grip her hips and begin fucking her pussy. Her tail coils around my hips affectionately while my lover moans out among the chirping birds and rustling wind."
                                "Fucking missionary with her legs up like this makes her pussy feel even tighter, her walls squishing against my cock with every deep thrust which immensely adds to the elicited pleasure."
                                "This position also allows me to easily play with her breasts, or clit, and I graciously take the opportunity to toy with any area of her body that draws my attention."
                                "First her nipples, stiff and poking through the velvety lingerie. Stiff, but the soft abdomen flesh gives way under the touch of my fingers. Living among fur-covered mares has made this simple sensation a rare one, one to be savoured."
                                "And then her clit, which has fully swollen and occasionally peaks through her innie labia as we rut. I push my thumb partially inside, find the nub and begin to rub."
                                "This causes Cindy to throw her head back against the grass, her back arching slightly as her eyes scrunch up with delight."
                                show cindy legsupv2 with dissolve
                                ci "Oooohhoohhhhh… My clit is so sensitive, ahhh, not too fast! Ooohhh…"
                                "As she gets increasingly aroused and stimulated over the course of our copulation, her copious, hot, gooey fluids increasingly coat my cock, allowing me to fuck comfortably at any pace I’d like."
                                "And as I pick up the pace, thrusting repeatedly into her hot depths, she moans and squirms under me with increasing intensity as the building euphoria engulfs her."
                                "With my constant rubbing on her clit, that pleasure soon overwhelms her and transforms into a potent orgasm that wracks her body and mind."
                                ci "Oohhh gosh, by the lords, ooohhh… Too good…"
                                "As she indulges in her bliss, I begin to focus on my own pleasure as I accelerate the movement of my hips. A familiar feeling in my loins signals the beginning of an orgasmic rise."
                                "More and more, this pleasure boils up as I fuck the dragon’s hot pussy. My body grows tense, and my cock throbs as my climax gets ever closer."
                                ci "Cum in me, knock this slutty dragon up! Ooohh, oooo…"
                                "I grit my teeth as the finality of my orgasm consumes me, turning my mind to white as with one mighty thrust I finally cum."
                                play sound cum
                                show cindy legsupv3 with cum
                                play sound cum
                                show cindy legsupv3 with cum
                                "Not stopping our coition for a second, I messily release my load deep into her pussy. My cum and her juice squelch and bubble loudly as the thick liquids mix together."
                                play sound cum
                                show cindy legsupv3 with cum
                                play sound cum
                                show cindy legsupv3 with cum
                                "Cooling load after load, I bring the temperature of this dragon’s pussy down a notch as we both cherish this immense pleasure."
                                ci "Yessshhh… Yeesss… Ooohh… Oh…"

                            "Anal":
                                "She takes a deep breath; I swear that some steam blows off her nose, as she grins and keeps her legs hoisted upwards for me."
                                "Using a hand to leverage her legs up, she uses it to spread her pussy slightly revealing some of her usually hidden pink lips. But I’m a lot more interested in what lies below as I eye up her soft pucker."
                                "Straddling her thick tail, I position myself and my cock just before the upside-down heart of her butt."
                                if cindyanal1 == 0:
                                    mc "Have much experience with anal, then?"
                                    ci "This’ll be my first, so go easy on me!"
                                else:
                                    mc "Ready for it in your ‘derriere’, again?"
                                    ci "Oohh, yes! Give it your best shot."

                                "She blushes and the tip of my cock brushes against her anus. Even this part of her body is hot to the touch, but perhaps less so than her pussy."
                                "I’ll probably need a small bit of lubrication, and saliva really won’t cut it. Fortunately, the dragoness’s natural lubricants have proven to be more than efficient enough."
                                play sound cum
                                show cindy legsupv1 with dissolve
                                "So, I take the opportunity to tentatively press my cock against her pussy lips, pushing myself inwards and temporarily fucking her pussy."
                                if cindyanal1 == 0:
                                    ci "Heyy, that’s not anal!"
                                    mc "Have some patience Cindy, I need to get my cock wet first."
                                    ci "Ooh? That makes a lot of sense, actually…"
                                else:
                                    ci "Mmm… My gooey pussy will get your cock nice and wet."
                                show cindy legsup1 with dissolve
                                "After fucking her pussy for about half a minute, I pull out and my cock is slick with her pussy juices. A liquid that won’t dissolve even in her internal heat."
                                "I press the dripping tip of my cock against her pucker, the dragoness initially twitches and tenses at the sensation."
                                play sound cum
                                show cindy legsupa1 with dissolve
                                "Pushing onwards, I guide my cock inside, slowly sinking into the heat of her warm ass. Grasping her hips at the area her scales turn into soft flesh for leverage."
                                "Plunging inwards, I eventually get to the hilt. Her ass isn’t quite as warm inside, which is somewhat reliving."
                                "Cindy coos and wriggles under the feeling of my thick cock sliding deep into her, the bizarre feeling exciting her in new and unusual ways."
                                "Her sphincter squeezes and envelopes my entire being, tightly squeezing around my cock like a tight fist."
                                "Her muscles are constantly contracting around my cock in response to her pleasure. And as I pull out, I have to fight for almost every inch as her squeezing almost pulls me back in."
                                if cindyanal1 == 0:
                                    "She doesn’t gasp, wince, or exhibit any signs of pain despite the fact it's her first. All she’s showing is delight and desire. It’s quite clear that dragonesses are tough bitches."
                                if cindylum1 == 0:
                                    ci "Oooohhh… That feels really good, I may need to start paying you at this rate… It’s sooo nice…"
                                    mc "Don’t give me any ideas, Cindy, heh."
                                    ci "Give it to me, I want you to make this worth every money, heh…"
                                else:
                                    ci "Oooohhh… I really want you to give me all you’ve got…"
                                play ambience sex fadein 3.0
                                "I nod as I grip her hips and begin fucking her ass, initially slowly, but as she gradually adjusts to my girth, I hump her faster."
                                "Her tail constricts around my hips affectionately, while my lover moans passionately among the chirping birds and rustling wind."
                                "Fucking missionary with her legs up like this makes her ass feel even tighter, and her insides squishing against my cock with every deep thrust immensely adds to the elicited pleasure."
                                ci "Ooohhh, fuck my ass, yesss!"
                                "This position also allows me to easily play with her breasts, or clit, and I graciously take the opportunity to toy with any area of her body that draws my attention."
                                "First her nipples, stiff and poking through the velvety lingerie. Stiff, but the soft abdomen flesh gives way under the touch of my fingers. Living among fur-covered mares has made this simple sensation a rare one, one to be savoured."
                                "And then her clit, which has fully swollen and peaks through her innie labia as we rut. I push my thumb partially inside, find the nub and begin to rub."
                                "This causes Cindy to throw her head back against the grass, her back arching slightly as her eyes scrunch up with delight."
                                show cindy legsupa2 with dissolve
                                ci "Oooohhoohhhhh… My clit too? Ooohhh… You know just how to make me come!"
                                "As she gets increasingly aroused and stimulated over the course of her copulation, her copious, hot, gooey fluids increasingly drip out of her pussy."
                                "She gets wet to such a degree that it meets our point of sex around the anus, adding even more lubricants to the mix and allowing me to fuck comfortably at any pace I’d like."
                                "And as I pick up the pace, thrusting repeatedly into her hot depths, she moans and squirms under me with increasing intensity as the building euphoria engulfs her."
                                "With my constant rubbing on her clit, that pleasure soon overwhelms her and transforms into a potent orgasm that wracks her body and mind."
                                ci "Oohhh gosh, by the lords, ooohhh… Too good…"
                                "As she indulges in her bliss, I begin to focus on my own pleasure as I accelerate the movement of my hips. A familiar feeling in my loins signals the beginning of an orgasmic rise."
                                "More and more, this pleasure boils up as I fuck the dragon’s hot ass. My body grows tense, and my cock throbs as my climax gets ever closer."
                                ci "Cum in me, cum in this slutty dragon’s butt! Ooohh, oooo…"
                                "I grit my teeth as the finality of my orgasm consumes me, turning my mind to white as with one mighty thrust I finally cum."
                                play sound cum
                                show cindy legsupa3 with cum
                                play sound cum
                                show cindy legsupa3 with cum
                                "Not stopping our coition for a second, I messily release my load deep into her ass, while her contracting sphincter wrings me."
                                play sound cum
                                show cindy legsupa3 with cum
                                play sound cum
                                show cindy legsupa3 with cum
                                "Cooling load after load, I bring the temperature of this dragon’s butt down a notch as we both cherish this immense pleasure."
                                ci "Yessshhh… Yeesss… Ooohh… Oh…"
                                $ cindyanal1 = 1
                        stop ambience fadeout 1.0
                        stop music fadeout 3.0
                        show cindy legsupcum with dissolve
                        "As the pleasure dissipates, I pull out of my lover and her legs immediately fall down as she exhaustively starts panting on the ground."
                        "I soon join her in that exhaustion, having built up quite the sweat after fucking her."
                        "Together, we lay on the grass beside each other for a while, enjoying the cooling breeze."
                        play music toewizard fadein 3.0
                        scene bg forest with dissolve
                        show cindyb lingeriecum
                        show cindy laughing
                        with dissolve
                        if cindylum1 == 0:
                            "Cindy is the first to break the silence with a giggle."
                            if cindyanal1 == 1:
                                ci "Anal… That was… interesting…"
                                mc "Interesting ‘good’, or interesting ‘bad’?"
                            show cindy happy with dissolve
                            ci "That was good… maybe… too good?"
                            mc "Too good? Want me to dial it back a little? Hah."
                            show cindy neutral with dissolve
                            ci "No I mean… How am I supposed to charge you, when I enjoy it so much? It just doesn’t feel right…"
                            mc "Hm? Well… I don’t know…"
                            $ cindylum1 = 1
                            show cindy happy with dissolve
                            ci "I have enough money now, anyway… I think I’ll stop charging you."
                            mc "Oh, wait, help me figure this out… You’re going to stop charging me, but you’re still going to keep doing that muffin thing?"
                            show cindy laughing with dissolve
                            ci "Hmm… I’m probably going to stop that special offer… I think I’ll just sell normal muffins for a normal price instead!"
                            if bakeryvisit1 == 1:
                                mc "Why don’t you ask Cream to help you? She's the mare that owns the bakery, and she's interested in expanding. Maybe you could be a subsidiser that sells her product, or at least work a deal out so you can use her kitchen."
                                show cindy happy with dissolve
                                ci "That’s a great idea, I’ll definitely do that! Thank you for the suggestion, [playername]."
                        elif bavcl == 1:
                            ci "Alright!"
                            "She stands up, stretches and I mimic her within a few seconds."
                            show cindy happy with dissolve
                            ci "I’m gotta get back to work, and quick! See you [playername]!"
                            mc "Yeah, see you Cindy."
                            scene bg forest with dissolve
                            "Cindy takes off, flying back to the stall before she gets told off for slacking."
                            "Although, considering that Cream would do the exact same thing with me, I think Cindy will be just fine."
                            play music daytheme fadeout 3.0
                            jump worldmap
                        ci "Alright!"
                        ci "I’m going to fly back home now, see you around [playername]."
                        mc "Yeah, see you Cindy."
                        scene bg forest with dissolve
                        "Cindy takes off, flying away for the day."
                        "She’ll be leaving her stall closed up for the rest of the day."
                        if bakeryvisit1 == 1:
                            "But I imagine if she reaches out to Cream tomorrow, she’ll be working full time soon."
                        play music daytheme fadeout 3.0
                        jump worldmap
            "Leave":
                if dawnltr == 5:
                    $ dawnltr = 6
                    show dawn2 happy with dissolve:
                        linear 1.0 xalign 0.5
                    dawn2 "All done?"
                    mc "Yeah, it was quite nice shopping with you."
                    jump dawnvisit5setup
                if fr == 1:
                    jump finalworldmap
                jump worldmap
    label mapfarm:
        if fr == 1:
            show bg pgworldmapdialogue with dissolve
        else:
            show bg worldmapdialogue with dissolve
        menu:
            "Honeycrisp's farm"
            "Visit the Farm":
                jump farm
            "Go back":
                if fr == 1:
                    jump finalworldmap
                jump worldmap
    label mapboutique:
        if fr == 1:
            show bg pgworldmapdialogue with dissolve
        else:
            show bg worldmapdialogue with dissolve
        menu:
            "Ruby's boutique"
            "Visit the boutique":
                jump boutique
            "Go back":
                if fr == 1:
                    jump finalworldmap
                jump worldmap
        if fr == 1:
            jump finalworldmap
        jump worldmap
    label maplibrary:
        if fr == 1:
            show bg pgworldmapdialogue with dissolve
        else:
            show bg worldmapdialogue with dissolve
        menu:
            "Lily's library"
            "Visit the library":
                jump library
            "Go back":
                if fr == 1:
                    jump finalworldmap
                jump worldmap
    label mapbakery:
        if fr == 1:
            show bg pgworldmapdialogue with dissolve
        else:
            show bg worldmapdialogue with dissolve
        menu:
            "Cream's bakery"
            "Visit the bakery":
                jump bakery
            "Go back":
                if fr == 1:
                    jump finalworldmap
                jump worldmap
    label mapbar:
        if fr == 1:
            show bg pgworldmapdialogue with dissolve
        else:
            show bg worldmapdialogue with dissolve
        menu:
            "The Riding Mare bar"
            "Visit the bar":
                if barvisit1 == 1 and maiddressbought == 0:
                    "Riku is going to be my slave for a day, so I better prepare. I want to buy some 'slave' clothes for her from the boutique."
                    if fr == 1:
                        jump finalworldmap
                    jump worldmap
                jump bar
            "Go back":
                if fr == 1:
                    jump finalworldmap
                jump worldmap
    label mapforest:
        if fr == 1:
            show bg pgworldmapdialogue with dissolve
        else:
            show bg worldmapdialogue with dissolve
        menu:
            "Butters' home"
            "Visit Butters":
                jump forest
            "Go back":
                if fr == 1:
                    jump finalworldmap
                jump worldmap
    label mapcity:
        jump city
label wagon:
    scene bg moxiewagonday with dissolve
    menu daywagonmenu:
        "Take a day off.":
            stop music fadeout 3.0
            "Feeling exhausted, I lay down and take a nap vowing to take a day off."
            scene bg black with dissolve
            if fr == 1:
                "I nap with Moxie, and we fuck sometime during the afternoon; it's fun having her stay at home during the day."
                "Eventually we both get up after nightfall."
            else:
                "Eventually night falls and Moxie returns."
            pause 0.5
            if livingwithmoxie == 1:
                jump evening
            elif fr == 1:
                scene bg moxiewagonlamp with None
                show moxie whappy with dissolve
                play ambience ambiencenight
                $ rand = renpy.random.randint(1,4)
                $ rand2 = renpy.random.randint(1,4)
                moxie "What's the plan for tonight then, [playername]? Are you crashing here for a bit longer, or are you going to Butters' place?"
                jump eveningmoxie2
            else:
                scene bg moxiewagonlamp with None
                show moxie shocked with dissolve
                play ambience ambiencenight
                $ rand = renpy.random.randint(1,4)
                $ rand2 = renpy.random.randint(1,4)
                moxie "Oh! [playername], I wasn't expecting you to be here."
                mc "Sorry for crashing, it's just so peaceful and comfy in here."
                show moxie althappy with dissolve
                moxie "Oh [playername]... You know you're always welcome here..."
                moxie "Want to stay the night?"
                jump eveningmoxie2
        "Crystal Ball" if crystalball == 1:
            stop music fadeout 2.0
            stop ambience fadeout 2.0
            play music PeaceSerenity
            scene bg crystalball with dissolve
            "Looking through the crystal ball, anything I imagine appears in deep, vivid colour."
            "Staring deeply into it, I almost lose myself in the memories."
            jump cbmenu2
            label cbmenu:
                $ persistent.morrigan = 0
                $ crystalballdayactivated = 0
                $ crystalballactivated = 0
                stop music fadeout 2.0
                stop ambience fadeout 2.0
                play music PeaceSerenity
                scene bg crystalball with dissolve
            menu cbmenu2:
                "The Crystal Ball allows you to replay scenes without affecting time."
                "Prologue":
                    menu:
                        "Prologue Day 0 (Note: You'll be able to change your name)":
                            $ crystalballdayactivated = 1
                            jump prologueday1
                        "Prologue Day 1":
                            $ crystalballdayactivated = 1
                            jump prologueday2
                        "The Sixty-Nine":
                            $ crystalballactivated = 1
                            show bg moxiewagonlamp with dissolve
                            jump intro69
                        "The Doggystyle Sex":
                            show bg moxiewagonday with dissolve
                            $ crystalballactivated = 1
                            jump introdoggystyle
                        "Back":
                            jump cbmenu2
                "Farm" if farmvisit3 == 1:
                    menu cbmenufarm:
                        "Visits":
                            menu:
                                "Visit 1 - Meeting Honey and Blossom":
                                    $ crystalballdayactivated = 1
                                    jump farmvisit1
                                "Visit 2 - Meeting and Milking Anna":
                                    $ crystalballdayactivated = 1
                                    jump farmvisit2
                                "Visit 3 - The Climax":
                                    $ crystalballdayactivated = 1
                                    jump farmvisit3
                                "Back":
                                    jump cbmenufarm
                        "Sex Scenes":
                            menu:
                                "Milking and Paizuri with Anna":
                                    $ crystalballactivated = 1
                                    show bg barnblur with dissolve
                                    jump annamilking
                                "Anna and Honey threesome":
                                    $ crystalballactivated = 1
                                    jump honeyannathreesome
                                "Milk-Fueled sex with Blossom":
                                    $ crystalballactivated = 1
                                    jump blossomcowgirl
                                "Back":
                                    jump cbmenufarm
                        "Back":
                            jump cbmenu2
                "Boutique" if boutiquevisit3 == 1:
                    menu cbmenuboutique:
                        "Visits":
                            menu:
                                "Visit 1 - Meeting Ruby and Melody":
                                    $ crystalballdayactivated = 1
                                    jump boutiquevisit1
                                "Visit 2 - The Camshow":
                                    $ crystalballdayactivated = 1
                                    jump boutiquevisit2
                                "Visit 3 - Personal Assistant":
                                    $ crystalballdayactivated = 1
                                    jump boutiquevisit3
                                "Back":
                                    jump cbmenuboutique
                        "Sex Scenes":
                            menu:
                                "Melody Handjob and Voyeur":
                                    $ crystalballactivated = 1
                                    jump melodyhandjob
                                "Ruby Photoshoot and Camshow":
                                    $ crystalballactivated = 1
                                    jump rubyphotoshoot
                                "Melody Blowjob":
                                    $ crystalballactivated = 1
                                    jump melodyblowjob
                                "Melody Cowgirl Position":
                                    $ crystalballactivated = 1
                                    jump melodycowgirl
                                "Back":
                                    jump cbmenuboutique
                        "Back":
                            jump cbmenu2
                "Library" if libraryvisit3 == 1:
                    menu cbmenulibrary:
                        "Visits":
                            menu:
                                "Visit 1 - Meeting Lily.":
                                    $ crystalballdayactivated = 1
                                    jump libraryvisit1
                                "Visit 2 - Sex for Breakfast, Lunch and Dinner":
                                    $ crystalballdayactivated = 1
                                    jump libraryvisit2
                                "Visit 3 - Meeting the Royal Sisters.":
                                    $ crystalballdayactivated = 1
                                    jump libraryvisit3
                                "Back":
                                    jump cbmenulibrary
                        "Sex Scenes":
                            menu:
                                "Lily Thigh-Job into Sex into Facial":
                                    $ crystalballactivated = 1
                                    scene bg librarylab with dissolve
                                    show lilyb lab
                                    show lily horny
                                    with dissolve
                                    jump lilytj
                                "Lily Standing Sex":
                                    $ crystalballactivated = 1
                                    scene bg librarylab with dissolve
                                    show lilyb lab
                                    show lily horny
                                    jump lilystandingsex
                                "Lily Legs-Up Missionary":
                                    $ crystalballactivated = 1
                                    scene bg dusklightbedroom with dissolve
                                    show lilyb
                                    show lily horny
                                    with dissolve
                                    jump lilylegsupmissionary
                                "Penelope Cunnilingus and Facesitting":
                                    $ crystalballactivated = 1
                                    show bg peneloperoom with dissolve
                                    show penelope closehorny with dissolve
                                    jump penelopecunnilingus
                                "Penelope Rubbing and Scissoring":
                                    $ crystalballactivated = 1
                                    show bg peneloperoom with dissolve
                                    show penelope closehorny with dissolve
                                    jump peneloperubbing
                                "Back":
                                    jump cbmenulibrary
                        "Back":
                            jump cbmenu2
                "Bar" if barvisit2 == 1:
                    menu cbmenubar:
                        "Visits":
                            menu:
                                "Meeting Riku":
                                    $ crystalballdayactivated = 1
                                    jump barvisit1
                                "Making Riku a Maid":
                                    $ crystalballdayactivated = 1
                                    jump barvisit2
                                "Back":
                                    jump cbmenubar
                        "Sex Scenes":
                            menu:
                                "Riku Truth or Dare into Doggystyle":
                                    $ crystalballactivated = 1
                                    scene bg barupstairs with dissolve
                                    with dissolve
                                    jump cbrikutod
                                "Riku Maid Blowjob":
                                    $ crystalballactivated = 1
                                    scene bg moxiewagonday with dissolve
                                    show rikub
                                    show riku horny
                                    with dissolve
                                    jump rikumaidblowjob
                                "Riku and Moxie Threesome":
                                    $ crystalballactivated = 1
                                    scene bg moxiebedday with dissolve
                                    jump rikuthreesome
                                "Back":
                                    jump cbmenubar

                        "Back":
                            jump cbmenu2
                "Forest":
                    menu cbmenuforest:
                        "Visits":
                            menu:
                                "Visit 1 - Meeting Butters and the Slime":
                                    $ crystalballdayactivated = 1
                                    jump forestvisit1
                                "Visit 2 - Meeting the Plant Girl":
                                    $ crystalballdayactivated = 1
                                    jump forestvisit2
                                "Visit 3 - Meeting SuccuButters":
                                    $ crystalballdayactivated = 1
                                    jump forestvisit3
                                "Back":
                                    jump cbmenuforest

                        "Sex Scenes":
                            menu:
                                "Butters and the original Slime":
                                    $ crystalballactivated = 1
                                    show bg cavepool with dissolve
                                    jump buttersandslime
                                "Butters and the Alraune":
                                    $ crystalballactivated = 1
                                    show bg caveovergrown with dissolve
                                    show bg cavehole with dissolve
                                    jump buttersandalraune
                                "SuccuButters Cowgirl Position":
                                    $ crystalballactivated = 1
                                    show bg buttershousered with dissolve
                                    play music danger fadein 3.0
                                    jump succubuttersmeet
                                "Back":
                                    jump cbmenuforest
                        "Back":
                            jump cbmenu2
                "Bakery" if bakeryvisit2 == 1:
                    menu cbmenubakery:
                        "Visits":
                            menu:
                                "Visit 1 - Meeting Cream and Party":
                                    $ crystalballdayactivated = 1
                                    jump bakeryvisit1
                                "Visit 2 - Meeting the Whole Gang":
                                    $ crystalballdayactivated = 1
                                    jump bakeryvisit2
                                "Back":
                                    jump cbmenubakery
                        "Sex Scenes":
                            menu:
                                "Quickie":
                                    $ crystalballactivated = 1
                                    scene bg bakerykitchen with dissolve
                                    show cream happy with dissolve
                                    jump creamquickie
                                "Missionary":
                                    $ crystalballactivated = 1
                                    scene bg black with dissolve

                                    jump creamvmissionary
                                "Gangbang":
                                    $ crystalballactivated = 1
                                    scene bg black with dissolve

                                    jump creamgangbang
                                "Back":
                                    jump cbmenubakery
                        "Back":
                            jump cbmenu2
                "Page 2 ->":
                    jump cbmenu3
                "Back":
                    scene bg moxiewagonday
                    play music day fadein 3.0
                    jump daywagonmenu
            menu cbmenu3:
                "Dawn" if dawnvisit > 4:
                    menu:
                        "Visits":
                            menu:
                                "Dawn Upstairs in the Club":
                                    $ crystalballdayactivated = 1
                                    scene bg nightclub with dissolve
                                    play music nightclub
                                    jump dawnvisit2
                                "Travelling to the Human Universe":
                                    $ crystalballdayactivated = 1
                                    jump dawnvisit3
                                "Spa Day":
                                    $ crystalballdayactivated = 1
                                    jump dawnvisit4
                                "Meeting Dawn, again?":
                                    scene bg market
                                    $ crystalballdayactivated = 1
                                    jump dawnvisit5
                                "Back":
                                    jump cbmenu3
                        "Sex Scenes":
                            menu:
                                "Blowjob":
                                    scene bg dawnsroomnight with dissolve
                                    $ crystalballactivated = 1
                                    jump dawnv2bj
                                "Reverse Cowgirl":
                                    scene bg dawnsroomnight with dissolve
                                    $ crystalballactivated = 1
                                    jump dawnv3sex

                                "The Long Threesome with Lily":

                                    $ crystalballactivated = 1
                                    jump dawnv4threesome
                                "Doggystyle":

                                    $ crystalballactivated = 1
                                    jump dawnv5ds
                                "Principal Aurora's First Scene":
                                    scene bg humanoffice with dissolve
                                    $ crystalballactivated = 1
                                    jump ppclsex
                                "Back":
                                    jump cbmenu3

                        "Back":
                            jump cbmenu3
                "Castle":
                    menu cbmenucastle:
                        "Visits":
                            menu:
                                "Visiting Selene" if selenevisit1 == 1:
                                    $ crystalballdayactivated = 1
                                    jump selenevisit
                                "Visiting Aurora" if auroravisit1 == 1:
                                    $ crystalballdayactivated = 1
                                    jump auroravisit1
                                "Back":

                                    jump cbmenucastle
                        "Sex Scenes":
                            menu:
                                "Selene Blowjob and Cowgirl" if selenevisit1 == 1:
                                    $ crystalballactivated = 1
                                    show bg selenebedroom with dissolve
                                    show selene closehorny with dissolve
                                    jump selenesex
                                "Aurora Missionary" if auroravisit1 == 1:
                                    $ crystalballactivated = 1
                                    show bg castlelivingroom with dissolve
                                    jump auroravsex



                                "Back":
                                    jump cbmenucastle
                        "Back":
                            jump cbmenu2
                "Morrigan's Route" if fr == 1:
                    menu:
                        "Replay - You can cancel the replay at any time by visiting the wagon.":
                            $ crystalballactivated = 1
                            $ clibvisit = 0
                            $ cbakvisit = 0
                            $ cforvisit = 0
                            $ cbarvisit = 0
                            $ cbouvisit = 0
                            $ cfarvisit = 0
                            $ clibcom = 0
                            $ cbakcom = 0
                            $ cbarcom = 0
                            $ cboucom = 0
                            $ cfarcom = 0
                            jump finalroute
                        "Back":
                            jump cbmenu2
                "Secret Scenes" if secretsunlocked > 0:
                    menu cbmenus1:
                        "Werewolf Hunting" if werewolfsex == 1:
                            $ crystalballdayactivated = 1
                            jump werewolfhunting
                        "Female Werewolf Sex Only" if devilsex == 1:
                            scene bg forestnight with d
                            $ crystalballactivated = 1
                            jump werewolfsex
                        "Sandy Threesome" if sandysex == 1:
                            scene bg market with d
                            $ crystalballactivated = 1
                            jump doubledragon
                        "Double Doggos" if doubledog == 1:
                            $ crystalballactivated = 1
                            jump doubledoggo
                        "Honeycrisp Outside" if honeycrispoutsidesex == 1:
                            $ crystalballactivated = 1
                            scene bg farm2 with d
                            jump farmsexduringwork
                        "Cream Lingerie" if creamlingeriesex == 1:
                            $ crystalballactivated = 1
                            jump creamlingeriesex
                        "Next Page ->":
                            jump cbmenus2
                        "Back":
                            jump cbmenu3
                    menu cbmenus2:
                        "Ruby Lingerie Doggystyle" if rubylingeriesex == 1:
                            $ crystalballactivated = 1
                            jump rubylingeriesex
                        "Riku Climbing Sex" if rikuclimbingsex == 1:
                            $ crystalballactivated = 1
                            jump rikuclimbingsex
                        "Lily Splits Sex" if lilysplitsex == 1:
                            $ crystalballactivated = 1
                            jump lilysplitsex
                        "Dawn Shower Sex" if dawnshowersex == 1:
                            $ crystalballactivated = 1
                            jump dawnshowersex
                        "Melody Cunnilingus" if melodycunnilingus == 1:
                            $ crystalballactivated = 1
                            jump melodycunnilingus
                        "Succubutters Work Sex" if succworksex == 1:
                            $ crystalballactivated = 1
                            jump succworksex
                        "<- Previous Page":
                            jump cbmenus1
                        "Back":
                            jump cbmenu3
                "<- Page 1":
                    jump cbmenu2
        "Enter Cheat":
                $ password = renpy.input("Enter Password")
                if password == ("ibeat0.2"):
                    "This cheat will reset your money to 200, and the days to 6. It'll automatically complete the boutique and farm routes."
                    menu:
                        "Are you sure?"
                        "Yes":
                            pass
                        "Nah":
                            jump daywagonmenu
                    "Success"
                    $ monies = 200
                    $ days = 6
                    $ boutiquevisits = 4
                    $ boutiquevisit1 = 1
                    $ boutiquevisit2 = 1
                    $ boutiquevisit3 = 1
                    $ farmvisits = 4
                    $ farmvisit1 = 1
                    $ farmvisit2 = 1
                    $ farmvisit3 = 1
                    jump daywagonmenu
                elif password == ("moneymoneymoney"):
                    "This cheat will give you 9999 monies, enough for anything in the game."
                    menu:
                        "Are you sure?"
                        "Yes":
                            pass
                        "Nah":
                            jump daywagonmenu
                    "Success"
                    $ monies = 9999
                    jump daywagonmenu
                elif password == ("ibeat0.4"):
                    "This cheat will beat the Forest, Library, Boutique and Farm routes, set your monies to 360 and set the number of days to 12."
                    menu:
                        "Are you sure?"
                        "Yes":
                            $ monies = 360
                            $ days = 12
                            $ boutiquevisits = 4
                            $ boutiquevisit1 = 1
                            $ boutiquevisit2 = 1
                            $ boutiquevisit3 = 1
                            $ farmvisits = 4
                            $ farmvisit1 = 1
                            $ farmvisit2 = 1
                            $ farmvisit3 = 1
                            $ libraryvisits = 4
                            $ forestvisits = 4
                            $ forestvisit1 = 1
                            $ forestvisit2 = 1
                            $ forestvisit3 = 1
                            $ libraryvisit1 = 1
                            $ libraryvisit2 = 1
                            $ libraryvisit3 = 1
                            jump daywagonmenu
                        "Nah":
                            jump daywagonmenu
                elif password == ("ibeat0.6"):
                    "This cheat will beat Selene's route, Bar, Forest, Library, Boutique and Farm routes, set your monies to 450 and set the number of days to 15."
                    menu:
                        "Are you sure?"
                        "Yes":
                            $ monies = 450
                            $ days = 15
                            $ boutiquevisits = 4
                            $ boutiquevisit1 = 1
                            $ boutiquevisit2 = 1
                            $ boutiquevisit3 = 1
                            $ farmvisits = 4
                            $ farmvisit1 = 1
                            $ farmvisit2 = 1
                            $ farmvisit3 = 1
                            $ libraryvisits = 4
                            $ forestvisits = 4
                            $ forestvisit1 = 1
                            $ forestvisit2 = 1
                            $ forestvisit3 = 1
                            $ libraryvisit1 = 1
                            $ libraryvisit2 = 1
                            $ libraryvisit3 = 1
                            $ barvisits = 3
                            $ barvisit1 = 1
                            $ barvisit2 = 1
                            $ selenevisit1 = 1
                            $ maiddressbought = 1
                            jump daywagonmenu
                        "Nah":
                            jump daywagonmenu
                elif password == ("changemyname"):
                    python:
                        playername = renpy.input("What is your first name?")
                        playername = playername.strip()
                        if not playername:
                            playername = "Anon"
                    jump daywagonmenu
                elif password == ("ibeatallroutes"):
                    "This cheat will beat all main character main routes, give you 550 monies and set the day to 21."
                    menu:
                        "Are you sure?"
                        "Yes":
                            $ monies = 550
                            $ days = 21
                            $ boutiquevisits = 4
                            $ boutiquevisit1 = 1
                            $ boutiquevisit2 = 1
                            $ boutiquevisit3 = 1
                            $ farmvisits = 4
                            $ farmvisit1 = 1
                            $ farmvisit2 = 1
                            $ farmvisit3 = 1
                            $ libraryvisits = 4
                            $ forestvisits = 4
                            $ forestvisit1 = 1
                            $ forestvisit2 = 1
                            $ forestvisit3 = 1
                            $ libraryvisit1 = 1
                            $ libraryvisit2 = 1
                            $ libraryvisit3 = 1
                            $ barvisits = 3
                            $ barvisit1 = 1
                            $ barvisit2 = 1
                            $ selenevisit1 = 1
                            $ auroravisit1 = 1
                            $ bakeryvisit1 = 1
                            $ bakeryvisit2 = 1
                            $ bakeryvisits = 2
                            $ maiddressbought = 1
                            $ auroravisitsetup = 1
                            $ cityfirstvisit = 1
                            jump daywagonmenu
                        "Nah":
                            jump daywagonmenu
                elif password == ("ibeat0.8"):
                    "This cheat will beat all routes and skip Morrigan's invasion. You'll also get 1500 monies and the day will be set to 22."
                    menu:
                        "Are you sure?"
                        "Yes":
                            $ monies = 1500
                            $ days = 22
                            $ boutiquevisits = 4
                            $ boutiquevisit1 = 1
                            $ boutiquevisit2 = 1
                            $ boutiquevisit3 = 1
                            $ farmvisits = 4
                            $ farmvisit1 = 1
                            $ farmvisit2 = 1
                            $ farmvisit3 = 1
                            $ libraryvisits = 4
                            $ forestvisits = 4
                            $ forestvisit1 = 1
                            $ forestvisit2 = 1
                            $ forestvisit3 = 1
                            $ libraryvisit1 = 1
                            $ libraryvisit2 = 1
                            $ libraryvisit3 = 1
                            $ barvisits = 3
                            $ barvisit1 = 1
                            $ barvisit2 = 1
                            $ selenevisit1 = 1
                            $ auroravisit1 = 1
                            $ bakeryvisit1 = 1
                            $ bakeryvisit2 = 1
                            $ bakeryvisits = 2
                            $ maiddressbought = 1
                            $ auroravisitsetup = 1
                            $ cityfirstvisit = 1
                            $ fr = 1
                            jump daywagonmenu
                        "Nah":
                            jump daywagonmenu

                else:
                    "Failure"
                jump daywagonmenu
        "Leave":
            if fr == 1:
                jump finalworldmap
            jump worldmap

label doubledragon:
    show cindyb
    show cindy laughing
    with d
    play music toewizard fadein 3.0
    ci "Hey [playername]! There’s something really exciting that I want to talk to you about."
    mc "Good morning Cindy, do tell."
    show cindy happy with d
    ci "Thanks to you paying for my previous ‘services’, and helping to establish me as a franchised bakery, I managed to pay for my sister’s medical treatments back in Dragon Town C!"
    ci "She really wanted to meet you, and thank you! So, if you’d like, I can take you there."
    menu:
        "Visit Cindy’s sister.":
            $ sandysex = 1
            "You found a secret scene! Requirements met: Help Cindy earn enough money for her sister."
        "I’d really love to, but I can’t right now.":
            $ cindysistervisitprep = 1
            ci "That’s okay, but you better come back the next chance you have!"
            mc "Of course."
            if crystalballactivated == 1:
                jump cbmenu
            jump cimuffinmenu2

    mc "One question though, how exactly do we get there?"
    show cindy laughing with d
    ci "Why, we fly of course. How else?"
    mc "Fly? But you’re even smaller than I am!"
    show cindy happy with d
    ci "I’m pretty tough though, just look at my muscles!"
    show cindy horny with d
    ci "I was thinking I could just hold your hands…  Aahh, uhm… Is that too lewd?"
    mc "I guess that could work… But what about on your back?"
    show cindy angry with d
    ci "My back? But my wings are on there, I need those to fly!"
    mc "True. I guess we’ll be holding hands."
    ci "Grr, shoulda brought a cage to carry you in."
    ci "Alright, here you go…"
    stop music fadeout 5.0
    "She turns away, blushing slightly as she presents her open palms. I tentatively take them, only for her to very firmly grip in response."
    show cindy happy with d
    ci "Don’t worry about not letting go, because I absolutely won’t."
    mc "Uhm, yes ma’am?"
    play music epic fadein 3.0
    play sound woosh
    scene bg farm4 with d
    play ambience ambiencewind fadein 3.0
    "Her wings suddenly spread, and with one aggressive movement she launches the two of us several meters into the sky."
    "Seamlessly she takes that momentum and continues to soar higher and higher; flapping her wings until she has enough height to glide."
    "She wasn’t kidding. She’s a tough bitch; carrying me, and flying with such ease."
    mc "We probably shouldn’t have done that in the market, everyone was staring."
    ci "Yeah, they were staring at how awesome we were, heh!"
    mc "Oh yeah, we looked really awesome holding hands and taking off."
    ci "Guh- shut up! Don’t make me drop you!"
    mc "You got it, I’m shutting up."
    "I can’t really talk anyway. She’s flying so fast that I need to keep my mouth closed due to the wind gusts."
    mc "How long is this journey going to take?"
    ci "Just an hour. No worries, right?"
    mc "An hour there and back? Ah... Can I get some goggles for the return journey? My eyes are getting dry."
    ci "Hah. Just close them, you wuss. That’s what I do."
    mc "You’re not flying with your eyes closed, are you?"
    ci "Haha, nope! That was a joke, dolt."
    show bg ocean with s
    "The thought occurs to me that this is the furthest I’ve ever been from Arcadia, and the completely alien scenery drives that point home as we pass over what appears to be an entire ocean."
    mc "I had no idea there was an ocean here, sheesh!"
    ci "Ohh, if I dropped you here, you’d probably survive, right?"
    mc "Uhh, probably not."
    ci "Yeahh, you’re right, the sharks would get you."
    mc "Sharks? Scary!"
    mc "Can I submit some feedback to the pilot? I think I’d enjoy this ride a lot more if you stopped joking about dropping me."
    ci "Noted, I’ll forward the feedback in 2-3 business days."
    ci "My sister is really looking forward to seeing you."
    stop music fadeout 3.0
    mc "So she knows who I am?"
    ci "Of course, how could I not mention someone as cool as you? You’ve helped the two of us out so much."
    ci "I think we both felt like repaying your generosity in some way."
    mc "A repayment? I wasn’t expecting anything like that."
    ci "Oh, that’s good, because we haven’t prepared anything, hehe."
    play music sadpiano fadein 5.0
    ci "There is one thing you should know. My sister, Sandy... is rather unwell."
    ci "To be truthful, she's struggled with her health since she was a whelp. However, recently it seems that her health is on a particular decline."
    ci "She was bedridden before I bought her the treatment you had afforded me."
    ci "She's well now. Able to walk around and do things by herself, but those moments always seem so brief."
    ci "That's one of the reasons I left so quickly after we had sex. I'd go back to check on her."
    mc "I'm so sorry to hear that. Mind if I ask what's ailing her?"
    ci "Her immune system is barely existent. So... anything is capable of bringing her down."
    mc "Is it really okay to bring me into the house, then?"
    ci "That's the struggle. She can't live locked up inside forever. That frustrates her, because she still wants to live her life to the fullest."
    ci "So... While she's briefly feeling well, I want her to have as much fun as she can..."
    ci "While she's still around. You know?"
    mc "I... see..."
    mc "You don't think this is something that'll pass?"
    ci "I'm afraid not. A lot of people have suggested asking a unicorn doctor to help, but we've tried everything."
    ci "There's no magical treatment to improve your immune system."
    mc "That really sucks."
    ci "I don't want this to be a dreary visit. It's not like she's dying, she's just often bedridden,"
    ci "So... Smiles all around if possible."
    mc "I understand."
    ci "Could I ask something of you? I know, it's a little selfish of me, but..."
    mc "Please, ask away."
    ci "Do you think we could have a threesome? With her condition, there might never be a better chance."
    mc "Ah... Potentially, although... Aren't you two related?"
    ci "We are. However, she'd probably never get to sleep with a non-dragon without my interference."
    mc "Alright, I'll do it if she's okay with it."
    ci "Thank you, [playername]..."
    stop music fadeout 10.0
    show bg forestsky with s
    "The blue ocean under me is gradually replaced with sandy beaches, and then forests. We even pass several smaller settlements."
    "Seeing everything from up here really puts this vast world into perspective. Arcadia is but a drop in the puddle of this planet."
    stop ambience fadeout 3.0
    scene bg black with d
    "It is indeed a long morning journey to Dragon Town C, but plenty of pleasant chatter with Cindy serves to pass the time."
    play ambience ambienceday fadein 3.0
    show bg dragontown1 with d
    "Soon enough, we arrive at a quaint town of which the majority of the inhabitants are dragons. There are also many other species, of which I believe I see Kobolds, Snakes, and various Reptiles."
    "I don’t have much time to gawk however, as I’m led to a particularly small cottage in a more residential area."
    show bg dragontown2 with d
    "Cindy opens the door and invites me in."
    play music toewizard fadein 20.0
    show cindyb:
        xpos 150
        ypos 30
    show cindy laughing:
        xpos 150
        ypos 30
    with d
    ci "Hey Sandy, I’m home!"
    "Cindy and Sandy? Jeez, those are similar names."
    show sandy happy:
        xpos 600
        ypos 75
    with d
    sa "Oh goodness. Hello Cindy. I wasn’t expecting you back so soon."
    show cindy neutral with d
    ci "Is Mindy not around?"
    "Cindy, Mindy & Sandy? You’ve got to be kidding!"
    show sandy neutral with d
    sa "No, she left for work a while ago."
    sa "Is this gentleman the friend you mentioned?"
    show cindy laughing with d
    ci "He sure is! Well, he’s no gentleman, but he saved my ass when I wasn’t getting any other customers!"
    mc "Hello, my name is [playername], nice to meet you."
    show sandy laughing with d
    sa "Goodness, it’s so nice to meet you. Cindy may act a little brash at times, but she’s spoken so highly of you."
    show cindy neutral with d
    ci "Pfft, have not… Maybe like, speaking mediumly."
    show sandy happy with d
    sa "I’m so glad you enjoyed my sister’s baking, she worked so hard on those cupcakes."
    mc "Mmm, baking… Yeah."
    "Does Sandy not know what Cindy was really doing in Arcadia?"
    mc "How was your treatment, Sandy? I hope you're feeling better."
    show sandy neutral with d
    sa "Ahh, I’ve always been very weak and sickly… But Cindy has always looked after me, she's great."
    sa "I recently caught a particularly bad flu, but thanks to you, Cindy was able to pay for some excellent treatment."
    mc "I’m really glad my money went towards helping you, Sandy."
    show cindy happy with d
    ci "Ohh, I just got an idea!"
    ci "Hey, we should do something special for [playername] to thank him for helping us."
    show sandy happy with d
    sa "What do you have in mind?"
    show cindy horny with d
    ci "Well…"
    ci "What if we had {i}sex{/i} with [playername], the two of us!"
    "Well shit, I didn’t think she’d just ask outright."
    show sandy horny with d
    sa "Ahh- goodness me… I may be single, but… To sleep with a man I barely know…"
    show cindy happy with d
    ci "Sandy, you’ve got to, I’m serious! Having sex with someone that isn’t a dragon feels amazing. It’s really soothing and cooling, like drinking a refreshing soda, or taking a cold bath!"
    sa "[playername], what do you think?"
    menu:
        "Why not? Try everything once for fun.":
            show sandy laughing with d
            sa "Hmm… Cindy is always encouraging me to be more playful."

        "Do what makes you feel comfortable.":
            show sandy laughing with d
            sa "Mm… With Cindy and you looking out for me, I should be okay, right?"

        "An incestuous dragon threesome? Sounds like a dream come true.":
            show sandy laughing with d
            sa "It would be a lot of fun… I think I need as much of that as I can get right now."

        "You shouldn’t do it if you don’t want to.":
            show sandy laughing with d
            sa "[playername]… You’re very sweet and thoughtful."
            sa "Maybe you’re the type of man that I’d be happy to be with."

    show cindy laughing with d
    ci "Definitely!"
    ci "What do you say, Sandy? You can just lay down, and we’ll make you feel great."
    show sandy horny with d
    sa "Mmm… I think I’d like that… Can you promise to make me feel {i}really, really{/i} good?"
    show cindy happy with d
    ci "Yes, absolutely! Right, [playername]?"
    mc "Of course, I see no problem with that."
    scene bg dragontown3 with d
    "Sandy nods and smiles sweetly. Gesturing for me to follow, the two dragonesses lead me to Sandy’s bedroom, the biggest room in the small building it seems."
    show cindyb:
        xpos 200
        ypos 250
    show cindy laughing:
        xpos 200
        ypos 250
    show sandy happy:
        xpos 500
        ypos 300
    with d
    ci "Just you lay down here, and we’ll take good care of you, Sandy."
    "Cindy lays her sister down on the bed before straddling her hips. From her vantage, she slowly massages Sandy from the shoulders down, gradually easing her into it."
    "She seems to be very affectionate towards her sister. Although openly having a threesome with her is a crazy concept… Maybe it’s a cultural thing."
    if fr == 1:
        "Am I really going to have yet another threesome with two sisters?"
        "I’ve always wondered that maybe I have a super power, and I just didn’t know about it yet. Maybe getting two sisters to have sex with me {i}is{/i} my super power."

    "Rather than simply standing by, I take a proactive approach and move beside Sandy. We kiss, and I feel her warm hand wrap around my growing cock, giving me a snug hand job."
    sa "Oooh, it feels nice!"
    "Cindy’s hands also begin to massage Sandy’s chest, caressing her breasts and tweaking her sensitive, erect nipples."
    "I had wondered how far she’d go, and it would appear the sisters have no qualms about pleasuring each other."
    show sandy horny with d
    sa "Aaahhh... Ahh, ahh..."
    "However, it would seem the girls aren’t just enjoying an erotic massage together, but they’re also scissoring."
    "Gradually I get harder, and the girls’ wetter. The temperature in the room heats up as the three of us build up to sex."
    show cindy happy with d
    ci "Hey, cold stuff. I think she’s ready. How do you want to do this?"
    show sandy laughing with d
    sa "I think it’d be quite nice to try it doggystyle, would that be okay?"
    show cindy horny with d
    ci "Ohh, face down in the pillow. Let’s make it happen."
    scene sandyb sex
    show sandy sex1
    with d
    play music sex1 fadeout 30.0
    "Sandy assumes the position, while Cindy cheekily lays down beside her and lavishly spreads herself before me, leaning a leg over Sandy’s back."
    ci "Look at all this eye candy. Sandy’s amazing ass, and my pretty pussy."
    sa "You shouldn’t be calling your own sister’s ass amazing…"
    ci "Any ass related to mine is obviously amazing!"
    mc "I’d typically say you’re a braggart, but you do both have amazing asses."
    "I reply as I fondle Sandy’s ass. Trailing my fingers across her rougher scales and onto her soft supple abdomen."
    "She coos and shivers under the touch of my fingers. Gradually they near her pussy. It emanates heat and drips thick wetness."
    "Already fully standing to attention, I bring my cock to her pussy and teasingly grind it up and down the length of her labia."
    sa "Oooohhh, it’s so… so cool…"
    ci "Ahaha, she liked that. Keep it going, [playername]!"
    "With some of her hot grool coating the tip of my cock, I prod and tease her vaginal entrance."
    "I toy with the idea of pushing inside, applying pressure to her pussy, but never quite enough to slip in. The heat surrounding my cock intensifies as I dare to push further in."
    sa "Mmmphh… T-This is going to feel crazy, isn’t it?"
    ci "Yep! Crazy good, hehe."
    "Cindy bites her lip slightly as she watches us, closely anticipating the moment of penetration. Her fingers have been constantly rubbing her clit, and briefly speed up whenever she gets excited."
    mc "Ready?"
    sa "Oohh yes…"
    ci "Ooohh, yes!"
    play sound cum
    show sandy sex2 with d
    "I push forward. Sandy’s wet, plush folds yield easily as I sink into her hot pussy. The entire area around her pelvic abdomen indenting slightly as I push to the hilt."
    "Both the lips of her pussy and the thick, plush lips of her labia squeezing and squishing around my shaft respectively."
    "Overall, this results in an extremely pleasureful sensation whenever I thrust in or out. Her dragon pussy stimulates my glans just right to maximise every touch."
    "Needless to mention the fiery feeling around my cock, which seems to make me more sensitive to each and every slight movement or squeeze inside her."
    sa "Ooohhh… It’s so… soothing… That feels so good…"
    ci "I told ya! Dragons are always too hot, get it, [playername]? So you’re like a refreshing cold drink, but in sex form!"
    mc "Am I being objectified as a drink?"
    sa "You are so much more than that, dear… Please, plow me!"
    ci "Just you wait until he cums! Now that’s the real refreshment."
    play ambience sex fadein 3.0
    "I resist the temptation to roll my eyes, but I don’t resist picking up the pace and fucking this delectable pussy."
    "While Sandy doesn’t move in rhythm for me, she keeps her body supple and flexible, allowing me to really rail into her with hard hitting thrusts."
    "Each time I bring my cock from hilt to base. One thing I’ve noticed is that dragons seem to love it when you fuck them deeply, so I aim each thrust to pleasure her."
    "Sandy’s body language indicates a complete success. Her entire body shivers with delight, her moans which were initially reserved are escaping in full force."
    sa "Ahh, aaahhh… Yes… You really are amazing, [playername]… Haahhh…"
    "The moans echo in combination with the slapping of her abdomen against my skin. The mixture of visual and auditory stimulation clearly gets Cindy going."
    "She masturbates fervently, twisting her head to get a better peek at the penetration. Her honeypot utterly oozing with juices as she begins to finger herself."
    "Speaking of thick dragon fem-cum, it effectively lubricates Sandy’s pussy, allowing me to gradually speed up, despite the tightness."
    "However, I may be moving too fast to hold back much longer. With the immense pleasure this pussy is capable of outputting, I find my orgasm sneaking up on me."
    sa "Ooohh, oh my gosh… I’m going to come!"
    "I think that’s my signal to go all out. Gripping tightly on her butt, I push forward with a series of fast thrusts, pummelling her pussy until we’re both on the absolute edge of orgasming."
    "Cindy seems to be keeping pace as well, her eyes rolling back and her thighs twitching as she reaches the heights of pleasure."
    sa "C-Coming! Ooohh, ooohhh! Oh my gosh…"
    "Her orgasmic moans push me over the edge. My cock rapidly swells as I feel cum surge through my loins. Here it comes!"
    play sound cum
    show sandy sex3 with cum
    play sound cum
    show sandy sex3 with cum
    "Almost in unison, the three of us indulge in the powerful pleasures of our climax. Thick loads of semen launching deep into my dragon lover’s squelching wet pussy."
    play sound cum
    show sandy sex3 with cum
    play sound cum
    show sandy sex3 with cum
    "The loads erupt from my tip until the cum almost spills from her packed pussy."
    stop ambience fadeout 3.0
    show sandy sex4 with d
    "As the heightened sense of euphoria from our orgasms gradually fade away, our movements grow to a halt, until we finally fall down onto the bed sheets panting."
    "My entire body is slightly sweaty due to the intense heat of my lover. She on the other hand seems positively perky."
    sa "Phew! That was truly something else! Mmm, I can feel the semen…"
    stop music fadeout 10.0
    scene bg dragontown3
    show cindyb:
        xpos 200
        ypos 250
    show cindy horny:
        xpos 200
        ypos 250
    show sandy horny:
        xpos 500
        ypos 300
    with d
    "Sandy lays there in post-coital bliss, gently rubbing her tummy."
    ci "I told ya, you’ll feel that in your tummy all day."
    show sandy laughing with d
    sa "Heyy, I have an idea… Have you given [playername] a blowjob before?"
    "Cindy perks up, and peeks over at me."
    mc "Oh, so you’re the one propositioning now, Sandy? I hadn’t expected that."
    show sandy horny with d
    sa "Oho, I apologize if that was unladylike of me to propose. But I am truly curious at how such a thing feels. It must be like… ice cream."
    mc "Was the ice creampie not enough? Hah."
    show cindy laughing with d
    ci "That was so lame. You definitely owe us a blowjob for that one."
    mc "Owe you? But-…"
    "Brain: Silence, they’re offering to suck your dick."
    "Ah, woops! Thanks brain."
    show sandy neutral with d
    sa "How about some refreshments first? Our male friend looks all hot and bothered."
    mc "That’d be very appreciated."
    scene bg black with d
    "So, I spent the day with the dragon girls."
    show sandyb sex
    show sandy sex5
    with d
    "And they spent a long time ‘thanking’ me."
    "They gave me a double blowjob, and later I had sex with Cindy before she carried me back home."
    "It took all day because I needed long breaks between each orgasm. There’s something really tiring about having sex with a dragon. The heat just saps all your energy."
    "But that’s not so bad, I got to learn a lot about Cindy and Sandy. It’s always fun making friends in this new world."
    scene bg black with d
    if crystalballactivated == 1:
        jump cbmenu

    $ secretsunlocked += 1
    jump evening
