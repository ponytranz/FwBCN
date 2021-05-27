label eveningbutters:
    stop ambience fadeout 2.0
    stop music fadeout 2.0
    scene bg buttershousenight with dissolve
    play ambience ambiencenight
    $ forestvisit3 = 1
    $ renpy.pause (0.5)
    $ rand = renpy.random.randint(1,3)
    if rand == 1:
        show butters succubus with dissolve
        "Sometime during the evening, Butters slowly turned into her succubus form. Does she really need to get undressed every time?."
        butters "OH HOOONEYY! I'M HOOOOME!"
        jump eveningbutterssuccmenu
    else:
        show butters dresshappy with dissolve
        "Me and Butters get cozy as we spend the evening together."
        jump eveningbuttersmenu
    label eveningbutters1:
        scene bg buttershousenight with dissolve
        if buttersimpregintro == 0 and buttersgifts >= 1 or buttersimpregintro == 0 and butterschocolates == 1:
            $ buttersimpregintro = 2
            jump buttersimpregintro
        if livingwithbutters == 1:
            show butters dresshappy with dissolve
            butters "Back from your walk honey?"
            jump eveningbuttersmenu
        else:
            if rand == 1:
                show butters succsadistic with dissolve
                butters "Perfect, the midnight snack has arrived."
                jump eveningbutterssuccmenu
            else:
                show butters dresshappy with dissolve
                butters "Good evening, what brings you here at this time?"
                jump eveningbuttersmenu
        label eveningbutterssuccmenu:
            menu:
                "Go Outside":
                    show butters succsurprised with dissolve
                    butters "Wha? Wait, don't go!"
                    if fr == 1:
                        jump prefinalworldmapnight
                    jump preworldmapnight
                "Talk" if succbutterstalks == 0:
                    show butters succsurprised with dissolve
                    butters "You wanna talk with me? I was kinda hoping for some action, but okay."
                    jump eveningbutterssucctalk
                "Sex":
                    show butters closesucchorny with dissolve
                    "You ask SuccuButters if she wants to do anything naughty, she nods eagerly and mounts you."
                    butters "What do you want from me, big boy?"
                    jump eveningbutterssuccsex
                "Visit Poyo":
                    "I try to enter Poyo's room, but the door is locked. She must be hiding from Butters."
                    jump eveningbutterssuccmenu
                "Go to Sleep" if livingwithbutters == 1:
                    butters "Can I suck your dick while you sleep?"
                    mc "Yeah sure, as long as you don't wake me up."
                    butters "Fuck yeah."
                    scene bg buttersbednight with dissolve
                    "I go to bed. Butters soon snuggles up beside me and we doze off together."
                    jump morning
        label eveningbuttersmenu:
            menu:
                "Go Outside":
                    if fr == 1:
                        jump prefinalworldmapnight
                    jump preworldmapnight
                "Talk" if butterstalks == 0:
                    jump eveningbutterstalk
                "Sex":
                    show butters closedresshorny with dissolve
                    "You ask Butters if she wants to do something naughty, she nods eagerly and flashes you a tiddy."
                    jump eveningbutterssex
                "Give Gift" if chocolates >= 1 or roses >= 1:
                    menu:
                        "Chocolates" if butterschocolates == 0 and chocolates >= 1:
                            $ butterschocolates = 1
                            $ chocolates -= 1
                            $ buttersgifts += 1
                            mc "By the way, these chocolates here, they're for you."
                            show butters dresslaughing with dissolve
                            butters "Really, for me? That's so kind of you [playername], thank you so much!"
                            mc "It's just a small gift to thank you for everything you've done for me so far."
                            show butters dresshappy with dissolve
                            butters "You're so kind, I don't know what to say, ehehe."
                            butters "Let's share them while we watch something!"
                            "You've unlocked the Butters reverse cowgirl scene."
                            jump eveningbuttersmenu
                        "Roses" if buttersroses == 0 and roses >= 1:
                            $ buttersroses = 1
                            $ roses -= 1
                            $ buttersgifts += 1
                            show butters dresshappy with dissolve
                            mc "I've got a surprise for you!"
                            show butters dresssurprised with dissolve
                            "I reveal the bouquet of roses causing Butters to squee."
                            show butters closedresslaughing with dissolve
                            "She runs up and hugs me tightly, kissing me on the lips."
                            show butters dresshappy with dissolve
                            butters "I love roses, thank you so much!"
                            butters "I'll get them water straight away."
                            mc "Just a small show of appreciation, I really enjoy spending time with you."
                            butters "Oh [playername], you're making me swoon in heart and heat."
                            show butters dresslaughing with dissolve
                            butters "I can think of a few ways to reward you for being such an amazing housemate."
                            "You've unlocked the Butters Leg-Up Doggystyle scene."
                            jump eveningbuttersmenu
                        "Back":
                            jump eveningbuttersmenu
                "Visit Poyo":
                    scene bg poyobedroom with dissolve
                    "I go into Poyo's room."
                    show slimegirl with dissolve
                    $ rand = renpy.random.randint(1,3)
                    if rand == 3:
                        "And catch her masturbating."
                        poyo "Eek! You shoulda knocked, perv!"
                    elif rand ==2:
                        "She's playing some video games, gamer girl confirmed?"
                        poyo "What's up?"
                    else:
                        "She's on a laptop. I hope she doesn't get too much slime on it."
                        poyo "Hey, wanna hang out?"
                    menu poyomenu:
                        "Talk" if poyotalks == 0:
                            jump poyotalk
                        "Sex":
                            jump poyosex
                        "Leave":
                            scene bg buttershousenight with dissolve
                            show butters dresshappy with dissolve
                            jump eveningbuttersmenu
                "You mentioned I could live here?" if livingwithbutters == 0:
                    show butters dresslaughing with dissolve
                    butters "If you'd like to stay, of course you'd be welcome."
                    show butters dresshappy with dissolve
                    butters "Would you like to live here? Rent free, naturally."
                    menu:
                        "Sure thing.":
                            $ livingwithbutters = 1
                            $ livingwithmoxie = 0
                            butters "This is going to be so much fun!"
                            show butters dresslaughing with dissolve
                            butters "You're going to love it here!"
                            if livingwithbuttersfirsttime == 0:
                                $ livingwithbuttersfirsttime = 1
                                "Guess I need to break the news to Moxie."
                                scene bg black with dissolve
                                "..."
                                stop music fadeout 3.0
                                play ambience ambiencenight fadein 3.0
                                show bg moxiewagonlamp with dissolve
                                if fr == 1:
                                    show moxie whappyneutral with dissolve
                                else:
                                    show moxie happyneutral with dissolve
                                play music wagon fadein 3.0
                                moxie "You're going to stay with Butters? Of course, I'm happy for you."
                                moxie "She's a bit of an oddball, but if she isn't charging rent, I'd say go for it."
                                moxie "You're only a walk away after all, you can visit me any time you want, and hey, maybe I'll visit you too!"
                                mc "Are you sure? I feel a bit guilty about this."
                                if fr == 1:
                                    show moxie wlaughing with dissolve
                                else:
                                    show moxie laughing with dissolve
                                moxie "Oh please, you're a grown man, and I don't even feel a tiny bit jealous, or sad."
                                mc "Really?"
                                if fr == 1:
                                    show moxie whappyneutral with dissolve
                                else:
                                    show moxie happyneutral with dissolve
                                moxie "Really, really! I always wanted you to outgrow this tiny place."
                                if fr == 1:
                                    show moxie wlaughing with dissolve
                                else:
                                    show moxie laughing with dissolve
                                moxie "But do visit, you are special to me aaannnddd, I wanna fuck you at least once a week."
                                mc "Deal!"
                                if fr == 1:
                                    show moxie whorny with dissolve
                                else:
                                    show moxie horny with dissolve
                                moxie "Actually, uhm..."
                                stop music fadeout 3.0
                                scene bg black with dissolve
                                pause 1.5
                                show bg moxiebednight with dissolve
                                pause 0.75
                                play music sex1
                                if fr == 1:
                                    show moxie wdoggystyle4 with dissolve
                                else:
                                    show moxie doggystyle4 with dissolve
                                play ambience sex
                                moxie "Oh yeah, yeah, yeah! I'll always be your number one bad bitch, aahh haaah!"
                                play sound cum
                                if fr == 1:
                                    show moxie wdoggystyle6 with dissolve
                                else:
                                    show moxie doggystyle6 with dissolve
                                moxie "Aaahhh fuck yeah! Fill me up! Mmmphhh..."
                                stop ambience fadeout 2.0
                                scene bg black with dissolve
                                "..."
                                "Moxie and I aggressively and energetically rut long into the night, until we doze off together."
                                stop music fadeout 3.0
                                show bg moxiebedday with dissolve
                                "In the morning I kiss Moxie goodbye and make my way to my new home."
                                show bg moxiewagonday with dissolve
                                scene bg black with dissolve
                                "..."
                                jump altmorning
                            else:
                                jump eveningbuttersmenu
                        "I'll pass, but thanks for your offer.":
                            jump eveningbuttersmenu
                "Go to Sleep" if livingwithbutters == 1:
                    hide butters with dissolve
                    show bg buttersbednight with dissolve
                    "I go to bed and Butters soon snuggles up beside me and we doze off together."
                    jump morning
    label eveningbutterssex:
        menu:
            "Cowgirl":
                stop music fadeout 3.0
                scene bg buttersbednight with dissolve
                show butters happy with dissolve
                "The two of us saunter over to the bedroom and she promptly undresses, while I lay down on the bed, prepared to get the ride of a life time."
                show butters closehorny with dissolve
                "After folding her clothes, she seductively wiggles her hips as she approaches and mounts me."
                show butters cowgirl1 with dissolve
                play music sex1 fadein 3.0
                butters "I like to take things sensually and slow, if that's okay?"
                mc "Of course, let's make love."
                "My body grows hot at the display and my cock grows to point upwards against her belly, her feminine lubricant dripping down my shaft as she begins to grind against it."
                show butters cowgirl2 with dissolve
                "But Butters doesn't waste any time with foreplay, she arches her back while sliding her plush pussy onto my cock."
                "She sinks down with a deliberate slowness, not once breaking eye contact."
                "Her insides squeeze as her pussy spreads until she's finally at the hilt, fully impaled by every inch of my length."
                butters "Oohh, it fills me up perfectly, let's have some fun..."
                play ambience sex fadein 3.0
                "She coos and rubs her clit for a few seconds while her hips begin to grind back and forth."
                "Her tight wet pussy squeezes and sucks around my cock in rhythmic motions as if her pussy is trying to drain me dry."
                "Even her 'normal' form still has powerful succubus sex qualities which are apparent by the immense pleasure"
                "She bites her lip when she notices my hips rocking to match her own pace, bouncing her up and down and making her large pillowy tits jiggle as the intensity increases."
                butters "Haahh, this feels really good, I want to feel your thick load inside me..."
                "Her movements are adept as she takes my entire cock from glans to hilt in her rapid assault of thrusts."
                "In no time at all, my cock is feeling tight and full, almost ready to burst into Butters's dribbling cunt."
                "She strokes my cheek knowingly and smiles."
                butters "It's okay if you cum prematurely darling, my succubus side will always make it so you'll have to cum for me."
                show butters cowgirl3 with dissolve
                butters "Are you ready, baby? My womb is waiting..."
                play sound cum
                show butters cowgirl4 with cum
                play sound cum
                show butters cowgirl4 with cum
                "My body tenses and my mind is overwhelmed with euphoria as my orgasm is unleashed and a torrent of hot cum erupts deep into Butters's eager pussy."
                play sound cum
                show butters cowgirl4 with cum
                play sound cum
                show butters cowgirl4 with cum
                butters "Ahhh, ahhh, yes! Don't hold back, [playername]!"
                "She quivers, riding with increased passion as her womb is filled up. Her eyes rolling back as her own orgasm takes control."
                "Butters's tongue hangs lewdly from her mouth as she's pumped with multiple loads of my cum, far more than I should ever let out in a regular orgasm."
                stop music fadeout 3.0
                stop ambience fadeout 3.0
                hide butters with dissolve
                "We're both left panting as she flops off me, grinning blissfully and rubbing her curse mark satisfied."
                show butters closesatisfied with dissolve
                butters "Mmm... Proper sex feels far too good, I'm so glad I met you."
                "She gives me a wet kiss as we embrace and slowly fall asleep."
                scene bg black with dissolve
                "..."
                if livingwithbutters == 0:
                    scene bg black with dissolve
                    show  bg buttersbed with dissolve
                    "In the morning I kiss Butters goodbye and return home."
                    scene bg black with dissolve
                    "..."
                    jump altmorning
                else:
                    jump morning
            "Reverse-Cowgirl" if butterschocolates == 1:
                scene bg buttersbednight with dissolve
                play music sex1 fadein 3.0
                "The two of us saunter over to the bedroom and she promptly undresses, while I lay on the bed."
                show butters closehorny with dissolve
                "Butters turns around and blushes as she sees me laid on my back, she skips the distance between us and gets on the bed."
                "She begins to stroke my cock with one hand with a lecherous grin."
                butters "Ohh, you got erect so quickly, you were ready for this..."
                butters "I'm ready too [playername], just lay down and I'll make it all better."
                show butters reversecowgirl1 with dissolve
                "She coos as she kisses the tip of my cock, before straddling me and slowly lowering herself, sliding down my cock until hilt in one smooth motion."
                "With my cock fully buried inside of her, I spread her pillowy cheeks with my hands and get a good view of her dripping wet pussy."
                "Given her innocence, it's easy to forget Butter's natural succubus charms as they beguile my mind and stiffen my cock, enhancing each and every sensation."
                butters "Mmm, your cock feels so good... Ahhh..."
                "She begins to grind her hips back and forth, occasionally thrusting up and down as she energetically rides me."
                butters "Ahhh, I'm gonna savour this..."
                "In response, I rock my hips into her movements, causing her ass to thwap against with the force of us both in our rut."
                "Butters moans with glee as she lecherously gyrates and bounces against me for long salacious minutes that leave us both in euphoria."
                "Eventually she reaches her peak speed, her entire body rocking up and down, and her big bouncy breasts rocking back and forth as she fully commits to her intensive riding."
                "Her thighs quiver, and back arches as she gets closer and closer to an orgasm, her tight succubus pussy trying to milk me more aggressively by the second."
                butters "Ooohh, I-I'm coming! Ahh, ahh..."
                "She orgasms, perhaps not her first, but she keeps slowing down to prevent me from ejaculating before she's satisfied."
                "I never anticipated Butters to be one to deny my orgasms, but she keeps riding and edging me until she's had hers, like a true mare in heat."
                "Eventually shes takes mercy and her slick, wet pussy rides me fast enough to push me over the edge."
                butters "I want you to fill up my womb, ahh, haaah..."
                "All the teasing causes my cock to throb intensely, my body preparing for a powerful release."
                play sound cum
                show butters reversecowgirl2 with cum
                play sound cum
                show butters reversecowgirl2 with cum
                "I finally climax in unison with her as a torrent of my semen unloads into her waiting womb."
                play sound cum
                show butters reversecowgirl2 with cum
                play sound cum
                show butters reversecowgirl2 with cum
                butters "Aahh, mmphhh, fill me up! Ahhh..."
                "Several more loads of semen unload into the deepest reaches of her pussy until I'm finally spent."
                stop music fadeout 3.0
                stop ambience fadeout 3.0
                hide butters with dissolve
                "After the peak, she collapses backwards and cuddles into my chest. We lie together and embrace like lovers, falling asleep into the night."
                scene bg black with dissolve
                "..."
                if livingwithbutters == 0:
                    scene bg black with dissolve
                    show  bg buttersbed with dissolve
                    "In the morning I kiss Butters goodbye and return home."
                    scene bg black with dissolve
                    "..."
                    jump altmorning
                else:
                    jump morning
            "Leg-Up Doggystyle" if buttersroses == 1:
                scene bg buttersbednight with dissolve
                play music sex1 fadein 3.0
                butters "You wanna be in control? Okay, let's do it!"
                hide butters with dissolve
                "She wanders to the bedroom with a skip in her step before cartoonishly diving onto the bed, face first into a pillow."
                show butters legupdoggy1 with dissolve
                "And then in an incredibly erotic display, her rump raises, followed by one of her legs, her soaking wet and ready pussy on full display."
                butters "Mmm, I'm all yours, baby..."
                "I bring one hand under her raised leg, and another to her hip as I brush the tip of my cock against the lips of her vulva."
                butters "No teasing, fuck me hard!"
                show butters legupdoggy2 with dissolve
                "Her rump pushes back into me slightly and I respond by pushing into her even harder, pushing my cock all the way into her warm, inviting pussy in one smooth motion."
                show butters legupdoggy2deep with dissolve
                butters "Aahh! Mmmphhh, so good... Ahhh..."
                show butters legupdoggy2 with dissolve
                show butters legupdoggy2deep with dissolve
                "I grip her hips and leg and begin thrusting into her soft pillowy ass, pulling out as far as I can before slamming myself back into her needy pussy."
                show butters legupdoggy2 with dissolve
                show butters legupdoggy2deep with dissolve
                "Her eyes roll back as I slam into her, each thrust elicits a moan of pleasure from my horny lover."
                show butters legupdoggy2 with dissolve
                show butters legupdoggy2deep with dissolve
                "She squirms and groans under my assault, her pussy contracting as her easily earned orgasms start to overwhelm her body with pleasure."
                show butters legupdoggy3 with dissolve
                show butters legupdoggy4 with dissolve
                "As she climaxes, her insides squeeze down around my shaft and she cries with pleasure."
                show butters legupdoggy3 with dissolve
                show butters legupdoggy4 with dissolve
                "Her back arches, and her tits mash against the bed sheets below as her body quivers in response to the overpowering sensations."
                show butters legupdoggy3 with dissolve
                show butters legupdoggy4 with dissolve
                "I continue to fuck her for a few minutes, and she comes a few times, turning from a dignified mare into a slutty mess."
                show butters legupdoggy3 with dissolve
                show butters legupdoggy4 with dissolve
                "My cock throbs and my orgasm teeters on the edge, her pussy just feels too good."
                butters "C-Cum inside me, please!"
                play sound cum
                show butters legupdoggy5 with cum
                show butters legupdoggy5deep with dissolve
                play sound cum
                show butters legupdoggy5 with cum
                show butters legupdoggy5deep with dissolve
                "I grit my teeth and with one last, mighty thrust, my cock swells and begins to launch several blasts of thick cum into her."
                play sound cum
                show butters legupdoggy5 with cum
                show butters legupdoggy5deep with dissolve
                play sound cum
                show butters legupdoggy5 with cum
                show butters legupdoggy5deep with dissolve
                butters "Aahh, yes! Fill me up! Mmmm..."
                show butters legupdoggy6 with dissolve
                stop music fadeout 3.0
                stop ambience fadeout 3.0
                "Exhausted, I pull out my cock, along with a glop of sex fluids."
                "She smiles behind the pillow and enjoys the feeling of my hot cum dripping out of her pussy before we snuggle together."
                "My eyes feel heavy as we cuddle and slowly drift off into a peaceful sleep."
                scene bg black with dissolve
                "..."
                if livingwithbutters == 0:
                    scene bg black with dissolve
                    show  bg buttersbed with dissolve
                    "In the morning I kiss Butters goodbye and return home."
                    scene bg black with dissolve
                    "..."
                    jump altmorning
                else:
                    jump morning
            "Missionary (Impregnation Version)" if buttersmissionaryunlock == 1 and butterspregnant == 0:
                $ butterspregnant = 1
                show butters dresshappy with dissolve
                butters "Ooohh, thank you so much! This is really exciting."
                "She quickly undresses, yet still finds time to fold up her clothes and place them down sensibly."
                show butters horny with dissolve
                butters "And arousing too! I mean… I do have a thing for impregnation…"
                mc "Heh, so that’s why you weren’t so bothered about the slime."
                show butters neutral with dissolve
                butters "I spent a lot of time masturbating that night, ehehe."
                hide butters with dissolve
                "My eager lover grabs a pinkish alchemical potion and gulps the entire thing."
                "Usually she always brews two servings, but she wastes no drop as she finishes the entire bottle."
                show butters happy with dissolve
                butters "Ahhh... Now I should be fertile. At least until I pee a few times."
                mc "Will I need to cum inside you a lot, then?"
                show butters laughing with dissolve
                butters "Nuh-uh, only a single load of cum should be sufficient."
                mc "Sheesh, that’s {i}really{/i} fertile!"
                show butters horny with dissolve
                butters "We can go for extra rounds if you’d like!"
                mc "I wouldn’t be against that."
                scene bg black with dissolve
                play music sex1 fadein 3.0
                stop ambience fadeout 3.0
                show butters missionary1 with dissolve
                "We walk to the bedroom where Butters readily presents herself to me on the bed."
                "She looks beautiful right now. A cast of moonlight shimmers, through the mountains, and peers through the window to illuminate her body."
                "All this beauty, and I’m lucky enough for her to offer it to me."
                butters "Hah... [playername]..."
                "She’s so wet, she’s clearly in a very lustful mood. Her legs are already splayed open as she eagerly awaits penetration."
                "I approach the bed, drinking in every detail of her beautiful form."
                show butters missionary2 with dissolve
                "Her tail flickers excitedly as I kneel before her and pull her hips slightly closer."
                butters "Oh my…"
                "She blushes a little as I close the distance and lean close over her in a traditional missionary position."
                "My lover is no doubt horny, but she still deserves to be treated with love. I brush my fingers through her messy locks of silken hair while I kiss her."
                "With one hand I massage her large soft breasts, while I masturbate my growing erection with the other."
                "Once fully erect and ready to go, I bring myself back upright with my eyes on the prize."
                "Butters takes a deep breath and shivers in anticipation of my touch, her tail practically curling around my thigh needily."
                butters "Ahh, I-I’m all yours."
                "With her cheeks flushed in desire, I grin as I take the head of my cock and rub it up and down her vulva."
                play sound cum
                show butters missionary3 with dissolve
                "She’s dripping wet, causing my tip to glisten in the glow of the sun. Having teased her enough, I line up with her entrance and push inwards."
                "I slide myself deeply into my lover, strings of sticky wetness connect us as my shaft pushes into the deepest reaches of her nether."
                butters "Aahhh, aahhh… It seems the potion has made it feel even better than usual."
                "The walls of her pussy clamp down around my member, enveloping me in warmth and squeezing pleasantly around every nerve ending."
                play ambience sex fadein 3.0
                "I groan and she moans with pleasure as I slide back out, and push back deeply into the hilt of her inviting insides."
                "With each thrust, Butters large breasts and juicy ass jiggle, and an adorable moan escapes her mouth."
                "Finding a pace of deep and sensual fucking, indecent squelching noises mix with the moans each time our bodies come together."
                "It would seem that the potion had some side effects beyond fertility, because I’m sure Butters isn’t usually this wet."
                "It’s also impossible to deny the pleasure she’s feeling, as she throws her arms and head back into the pillow, her tongue lolling slightly as her mind blanks from the powerful erotic sensations."
                butters "Ooohh, keep going… I’m getting close. Ahh, ahh…"
                "I continue my rutting, using her plump thighs as leverage in order to pump her deeply and hard. As she’s getting closer and closer, she wraps her legs around my hips and pushes me closer."
                show butters missionary4 with dissolve
                butters "Yeahh, yesss… Oh, [playername], I’m going to come! Ahh, ahh!"
                "She moans aloud as her eyes roll back in the wake of a full body orgasm."
                "As her pussy contracts and sucks around my shaft, I redouble my passion-filled fucking and pound her pussy with determination to fill it with my cum."
                "Her sloppy cunt squeezes even tighter around my cock, causing me to throb and drip precum. It doesn’t take long for the familiar sense of impending orgasm to arrive."
                "My muscles grow tense, and my cock stiffens as my climax swells up deep inside. The constant moaning and shifting of my partner pushing me over the edge as she beckons me to cum."
                butters "Cum for me, cum for me [playername]! I want you to fill my womb, impregnate me!"
                play sound cum
                show butters missionary5 with cum
                play sound cum
                show butters missionary5 with cum
                "And just like an orgasm switch was pressed, the pressure reaches breaking point, my cock swells and I unload copious amounts of cum deep into my highly fertile lover."
                play sound cum
                show butters missionary5 with cum
                play sound cum
                show butters missionary5 with cum
                "Butters seems to orgasm a second time in a row, indulging in the euphoria of being filled with hot, thick semen."
                play sound cum
                show butters missionary5 with cum
                play sound cum
                show butters missionary5 with cum
                "My orgasm is more powerful than I anticipated, and the volume of cum her pussy wrings out is a far larger quantity than usual."
                play sound cum
                show butters missionary5 with cum
                play sound cum
                show butters missionary5 with cum
                "Three loads, six, nine, twelve?! The potion must have had a residual effect on my semen."
                "There’s so much that it drips and splatters outwards, splattering our point of connection."
                "Butters enjoys her orgasm and the moment so much, that she doesn’t unwrap her legs and let me stop fucking until my cock started to get sensitive."
                show butters missionary6a with dissolve
                stop ambience
                stop music fadeout 3.0
                "We both pant as she unwraps her legs and I pull back, some more cum oozing over her pussy. There’s so much cum that you can’t even see her vulva."
                "She looks up to me, seemingly exhausted, but smiling with glee."
                "I wonder if that got her pregnant? If this was a hentai game, I'd probably see one of those egg fertilisation cut-ins. Heh, what a ridiculous thought."
                play ambience ambiencenight fadein 5.0
                mc "So, how’d I do?"
                butters "Haahhh… It’ll take a while, but I think you successfully put a bun in the oven, hehe!  *Pant*"
                if bakeryvisit1 == 1:
                    mc "Hah, I’d expect that type of comment from Cream, not you!"
                else:
                    pass
                butters "I’m so excited. I’m finally going to be a mother, after all these years!"
                mc "Congratulations. If in a few months there’s no baby bump, be sure to gimmie a call."
                butters "Aha, I hope you’ll cum inside me a lot more regardless."
                scene bg black with dissolve
                "We cuddle lovingly for the next five minutes, just enjoying the feeling of each other’s softness. Her fur, contrasting against my supple skin."
                show bg buttersbednight with dissolve
                butters "Mmm… I really enjoyed this."
                butters "Maybe we can do this again later. You should definitely visit me tomorrow in any case! I think I’ll take one more load of cum just in case."
                mc "Sure thing, I’ll happily donate my cum to any mare in Arcadia."
                butters "Awhh, you’re such a perv! Come on, let me treat you to some dinner"
                scene bg black with dissolve
                "..."
                scene bg buttershousenight with dissolve
                show butters dresshappy with dissolve
                jump eveningbuttersmenu
            "Missionary (Standard Version)" if buttersmissionaryunlock == 1:
                    show butters dressneutral with dissolve
                    butters "Ooohh, I usually try to avoid sex before dinner, but I’m so horny lately..."
                    mc "Well, I better fuck it out of you before you turn Succubus on me."
                    butters "True! Let's do it."
                    scene bg black with dissolve
                    play music sex1 fadein 3.0
                    stop ambience fadeout 3.0
                    show butters missionary1 with dissolve
                    "We walk to the bedroom where Butters readily presents herself to me on the bed."
                    "She looks beautiful right now. Moonlight shimmers through the mountains, and peers through the window to illuminate her body."
                    "All this beauty, and I’m lucky enough for her to offer it to me."
                    butters "Hah... [playername]..."
                    "She’s so wet, she’s clearly in a very lustful mood. Her legs are already splayed open as she eagerly awaits penetration."
                    "I approach the bed, drinking in every detail of her beautiful form."
                    show butters missionary2 with dissolve
                    "Her tail flickers excitedly as I kneel before her and pull her hips slightly closer."
                    butters "Oh my…"
                    "She blushes a little as I close the distance and lean close over her in a traditional missionary position."
                    "My lover is no doubt horny, but she still deserves to be treated with love. I brush my fingers through her messy locks of silken hair while I kiss her."
                    "With one hand I massage her large soft breasts, while I masturbate my growing erection with the other."
                    "Once fully erect and ready to go, I bring myself back upright with my eyes on the prize."
                    "Butters takes a deep breath and shivers in anticipation of my touch, her tail practically curling around my thigh needily."
                    butters "Ahh, I-I’m all yours."
                    "With her cheeks flushed in desire, I grin as I take the head of my cock and rub it up and down her vulva."
                    play sound cum
                    show butters missionary3 with dissolve
                    "She’s dripping wet, causing my tip to glisten in the glow of the sun. Having teased her enough, I line up with her entrance and push inwards."
                    "I slide myself deeply into my lover, strings of sticky wetness connect us as my shaft pushes into the deepest reaches of her nether."
                    butters "Aahhh, aahhh… I’m so horny lately. Don’t hold back, I need you to knock some sense into me, heh."
                    "The walls of her pussy clamp down around my member, enveloping me in warmth and squeezing pleasantly around every nerve ending."
                    play ambience sex fadein 3.0
                    "I groan and she moans with pleasure as I slide back out, and push back deeply into the hilt of her inviting insides."
                    "With each thrust, Butters large breasts and juicy ass jiggle, and an adorable moan escapes her mouth."
                    "Finding a pace of deep and sensual fucking, indecent squelching noises mix with the moans each time our bodies come together."
                    "It’s also impossible to deny the pleasure she’s feeling, as she throws her arms and head back into the pillow, her tongue lolling slightly as her mind blanks from the powerful erotic sensations."
                    butters "Ooohh, keep going… I’m getting close. Ahh, ahh…"
                    "I continue my rutting, using her plump thighs as leverage in order to pump her deeply and hard. As she’s getting closer and closer, she wraps her legs around my hips and pushes me closer."
                    show butters missionary4 with dissolve
                    butters "Yeahh, yesss… Oh, [playername], I’m going to come! Ahh, ahh!"
                    "She moans aloud as her eyes roll back in the wake of a full body orgasm."
                    "As her pussy contracts and sucks around my shaft, I redouble my passion-filled fucking and pound her pussy with determination to fill it with my cum."
                    "Her sloppy cunt squeezes even tighter around my cock, causing me to throb and drip precum. It doesn’t take long for the familiar sense of impending orgasm to arrive."
                    "My muscles grow tense, and my cock stiffens as my climax swells up deep inside. The constant moaning and shifting of my partner pushing me over the edge as she beckons me to cum."
                    butters "Cum for me, cum for me [playername]! Fill up my pussy!"
                    play sound cum
                    show butters missionary5 with cum
                    play sound cum
                    show butters missionary5 with cum
                    "And just like an orgasm switch was pressed, the pressure reaches breaking point, my cock swells and I unload copious amounts of cum deep into my highly fertile lover."
                    play sound cum
                    show butters missionary5 with cum
                    play sound cum
                    show butters missionary5 with cum
                    "Butters seems to orgasm a second time in a row, indulging in the euphoria of being filled with hot, thick semen."
                    "There’s so much that it drips and splatters outwards, splattering our point of connection."
                    "Butters enjoys her orgasm and the moment so much, that she doesn’t unwrap her legs and let me stop fucking until my cock started to get sensitive."
                    show butters missionary6b with dissolve
                    stop ambience
                    stop music fadeout 3.0
                    "We both pant as she unwraps her legs and I pull back, some more cum oozing over her pussy."
                    "She looks up to me, seemingly exhausted, but smiling with glee."
                    play ambience ambiencenight fadein 5.0
                    scene bg black with dissolve
                    "We cuddle lovingly for the next five minutes, just enjoying the feeling of each other’s softness. Her fur, contrasting against my supple skin."
                    show bg buttersbednight with dissolve
                    butters "Mmm… I really enjoyed this."
                    butters "Every time with you is like my first, it’s truly special."
                    mc "I could say the same with you. You have some qualities that no mare in Arcadia can match."
                    butters "Awhh, you’re such a flatterer."
                    scene bg black with dissolve
                    "..."
                    scene bg buttershousenight with dissolve
                    show butters dresshappy with dissolve
                    jump eveningbuttersmenu
            "Milky Paizuri" if milkypaizuriunlocked == 1:
                play music sex1 fadein 3.0
                stop ambience fadeout 2.0
                butters "You wanna play with my boobs?"
                scene bg buttersbedday with dissolve
                "She wanders to the bedroom with a skip in her step, before cartoonishly diving onto the bed and jiggling her tits."
                show butters paizuri2 with dissolve
                "I like her playful side."
                "I position myself below her on the bed, and lay down between her thighs. Butters takes it upon herself to sit on my thighs, her nude figure arousing me to the point of erection."
                "With little hesitation, she begins to stroke my shaft until my tip throbs and dribbles with precum. Some drops of milk splattering onto my skin."
                "Once she’s satisfied, she lowers her entire body and prepares to put her pillowy bosom to good work."
                show butters paizuri3 with dissolve
                butters "I really enjoy doing paizuri with you. Even though I'm usually too horny and just want it in my pussy, hehe…"
                show butters paizuri2 with dissolve
                butters "My nipples and breasts aren't quite as sensitive as they were before, so I don't think I'll be able to orgasm from just breast stimulation."
                butters "But I think I'll have no problem getting you off..."
                "My cock throbs at her lewd words, prodding her boobs and causing her to giggle."
                play ambience blowjob fadein 3.0
                "She eases her breasts around my shaft, and then uses her arms to squish them together, squashing my member surprisingly effectively."
                "There were already a few droplets of milk around my cock, creating a warmth and a wetness that lubricates us slightly."
                "She begins to rise and fall, catching the skin of my shaft and pulling it back and forth over my glans eliciting pleasureful sensations despite the otherwise simple and slow motions."
                "Butters wasn’t joking, her breasts really are splaying more milk, her nipples now fully standing to attention as my pelvis dampens with a slight glisten of milk."
                show butters paizuri3 with dissolve
                butters "Ahh, this is hot... Haha, I’m getting really wet, both up here and down there."
                "Suddenly I feel a warmth hit my cock, as a trail of drool slathers over the tip and wettens my entire member as it’s caught within the motion of the titfuck."
                "And just like that, she’s moving even faster. The fur between her chest becoming not only damp, but slick and shiny, rubbing faster and faster."
                "The feeling has slowly devolved from fluffy and cute to moist and erotic."
                show butters paizuri2 with dissolve
                butters "*Drool* Haahh, it feels good when it slides against me."
                mc "Wow, your breasts are that sensitive?"
                butters "Yeah, they’re like one big erogenous zone right now, I can even feel you throbbing."
                "As if she’d been saving a trick, her tongue slithers downwards and starts to tease the most sensitive area of my tip at the peak of each thrust."
                "The effectiveness of her movements makes it arguably even more pleasurable than a standard blowjob. The squeeze of her breasts combined with her tongue is immensely euphoric."
                show butters paizuri4 with dissolve
                "And as she focuses more into the boobjob, the milk sputtering out of her nipples borders on excessive. The now rapid movements of her breasts causing it to splatter and splash everywhere."
                "To the untrained eye, it’d appear as if I’d already ejaculated and coated her breasts with whiteness."
                show butters paizuri5 with dissolve
                "Oh fuck, she’s getting even faster, and clearly trying to make me cum. I can’t focus on anything except the immense pleasure anymore."
                "I relax and give into the pleasure, not holding back my building orgasm a modicum. Before I know it, my cock throbs as a surge of euphoria ascends through my body."
                play sound cum
                show butters paizuri6 with cum
                play sound cum
                show butters paizuri6 with cum
                "Butters keeps her tongue trained on my sensitive tip throughout my entire orgasm, creating a mess of cum that launches over her face, eyes and breasts."
                play sound cum
                show butters paizuri6 with cum
                play sound cum
                show butters paizuri6 with cum
                stop ambience fadeout 3.0
                "I buck my hips against her tight warm breasts throughout my entire orgasm, until the very last load of my cum shoots out, this one landing at the roof of her mouth."
                show butters paizuri7 with dissolve
                butters "Eheh, I'm so horny right now... Think you can return the favour and give me an orgasm?"
                mc "Hmm… Clean up all this milk and cum, and I’ll fuck you good enough for two orgasms."
                butters "You have a deal… *Lick, lick*"
                hide butters with dissolve
                "Butters sets to cleaning up all the cum and milk. Surprisingly efficiently, she enjoys each second."
                show butters legupdoggy1 with dissolve
                "Then she bends over, and I know what to do…"
                show butters legupdoggy2 with dissolve
                play sound cum
                show butters legupdoggy4 with dissolve
                "I pound her pussy intensely until we’re both cumming again."
                stop music fadeout 3.0
                play ambience ambienceday fadein 3.0
                scene bg black with dissolve
                "Afterwards, we spend some time cuddling together and catching our breath."
                "My eyes feel heavy as we cuddle and slowly I drift off into a peaceful sleep."
                scene bg black with dissolve
                "..."
                if livingwithbutters == 0:
                    scene bg black with dissolve
                    show  bg buttersbed with dissolve
                    "In the morning I kiss Butters goodbye and return home."
                    scene bg black with dissolve
                    "..."
                    jump altmorning
                else:
                    jump morning
            "Back":
                jump eveningbuttersmenu
        jump eveningbuttersmenu
    label eveningbutterstalk:
        menu:
            "What's the craziest potion you've ever brewed or tried?":
                show butters dresshappy with dissolve
                butters "Most of my ingredients are natural and local, so I have a limited scope on potion capabilities."
                butters "It'd be hard to make abstract magical effects such as 'lockpicking' when I only have natural ingredients."
                butters "Additionally all potions need to be drunk and digested, so I can't create objects out of thin air."
                butters "So they may not be as 'crazy' as you might anticipate."
                butters "But... One time I accidentally created a potion that let me breathe fire!"
                mc "F-Fire? That sounds dangerous."
                show butters dressneutral with dissolve
                butters "Oh it was! That's the last time I use ash as an ingredient."
                show butters dresslaughing with dissolve
                butters "Thankfully it didn't hurt, nor was there any damage, but it was quite a surprise when I sneezed."
            "What's the most interesting adventure you've ever had?":
                mc "You seem quite experienced with cave diving, and adventures. What was the most interesting thing you've done?"
                butters "You see, I live in Arcadia due to its safety and ideal ingredients, particularly the ones you helped me get."
                butters "But before I moved here, I used to be more ambitious and adventurous."
                butters "Using my wings I could fly anywhere I wanted, be it a jungle, a desert, high mountains and more."
                mc "Ahah, you really are experienced."
                show butters dresslaughing with dissolve
                butters "I've had many fun adventures, even when we were cave diving I would have protected us from any real danger."
                show butters dressneutral with dissolve
                butters "I was just trying to be reserved because I didn't want you to know I was a succubus..."
                mc "So you just let the slime and Alraune mess with us?"
                show butters dresshappy with dissolve
                butters "Hehe, the slime got me fair and square. She was really agile and I wasn't expecting that."
                butters "And the Alraune? She exploited my biggest weakness."
                butters "Sometimes on my journeys I may run into colonies of various species, most are friendly but some are territorial and aggressive."
                show butters dressneutral with dissolve
                butters "Once while I was camping between journeys I was ambushed by imps."
                show butters dressangry with dissolve
                butters "They all had their dicks out, planned on making a fun night out of me. My succubus side immediately went ballistic and terrified them away."
                butters "My succubus side is a good fail-safe, always rears when I'm in danger."
                butters "Still, ever since that night I never camp out in the open."
                mc "Sounds dangerous, where was that?"
                show butters dressneutral with dissolve
                butters "Far, far away from here, in wilder and untamed lands."
            "Any plans for the future now that you're mortal?":
                mc "Any plans for the future?"
                show butters dressneutral with dissolve
                butters "I'm not sure, I've been living in limbo for so long, it's still hard to acknowledge that I'm 'normal' again."
                butters "I know I mentioned a partner and potentially children, but..."
                butters "With you, Poyo and Devil, it feels like I have everything right now."
                mc "Well, none of us are... 'official'."
                show butters dresshappy with dissolve
                butters "I know that, but it makes me so happy I could cry."
                butters "I don't want to worry about the future anymore, I've worried about that my whole life."
                show butters dresslaughing with dissolve
                butters "From now on, I'll live in the present and enjoy each day like it's the best day."
                mc "Awh, come here."
                "Butters and I cuddle."
            "What kind of potions are you making now you're cured?":
                mc "I notice you still go hunting for ingredients every day, what kind of potions are you making now?"
                butters "Potions that sell, since alchemy is still very hush-hush there aren't many customers, but they pay well."
                butters "The only commercial potion I can sell to the public is a lust-reducing potion, no one even realizes that's a potion, they just think it's a herbal remedy."
                butters "Same with pain-reducing potions, although I don't produce those as much because it's hard to compete against real medicine."
                butters "Other than that, I take very expensive potion commissions and also have a catalogue that people can buy from me."
                mc "What's the most popular product?"
                show butters dressneutral with dissolve
                butters "As you can probably imagine, it's a happiness potion. It basically leaves you feeling great, and happy, with few negative effects."
                mc "Huh, that sounds great."
                show butters dresssad with dissolve
                butters "I don't think we should have any though."
                mc "Why's that?"
                show butters dressneutral with dissolve
                butters "Something that makes you feel that good is going to make everything else just a little bit worse."
                show butters dresssad with dissolve
                butters "Sure, the potion makes you feel great and it's a popular product, but it has a habit of sapping some joy from all other aspects of life."
                mc "Huh... That sounds psychologically harmful."
                show butters dressneutral with dissolve
                mc "Isn't that like a drug? Don't you feel guilty selling that?"
                butters "A drug? No, no... They're just potions of magical happiness. In that sense, how is it different from selling a sugary drink that makes you feel good?"
                show butters dresshappy with dissolve
                butters "All things in moderation, [playername]."
                mc "Ever tried one?"
                show butters dresssatisfied with dissolve
                butters "Yeah, naturally I've tested and perfected my main product."
                mc "How did you deal with the psychological effects?"
                show butters dresshappy with dissolve
                butters "It's never really bothered me because I'm always happy anyway, but if you have too much it can mess up your hormones for a day or so."
                butters "It's best used to enhance other things, like sex, a movie, or a video game."
            "Back":
                jump eveningbuttersmenu
        $ butterstalks = 1
        jump eveningbuttersmenu
    label eveningbutterssuccsex:
        menu eveningbutterssuccsexmenu:
            "Cowgirl":
                stop music fadeout 3.0
                scene bg buttersbednight with dissolve
                show butters succhappy with dissolve
                "The two of us saunter over to the bedroom and I lay down on the bed, prepared to get the ride of a life time."
                show butters closesucchorny with dissolve
                "She seductively wiggles her hips as she approaches and mounts me."
                show butters succubussex1 with dissolve
                play music sex1 fadein 3.0
                butters "I'm not like my other side, I like to get down to business, got it?"
                mc "Of course, let's rut like sex-crazed maniacs."
                "My body grows hot at the display and my cock grows to point upwards against her belly, her feminine lubricant dripping down my shaft as she lustfully grinds against it."
                show butters succubussex2 with dissolve
                "Butters doesn't waste any time with foreplay, she arches her back while sliding her plush pussy onto my cock."
                "She sinks down with a deliberate slowness, not once breaking eye contact."
                "Her insides squeeze as her pussy spreads until she's finally at the hilt, fully impaled by every inch of my length."
                butters "Oohh, I love how your cock fills every inch of my pussy... We're gonna have some fun..."
                play ambience sex fadein 3.0
                "She coos and rubs her clit for a few seconds while her hips begin to grind back and forth."
                "Her tight, wet pussy squeezes and sucks around my cock in rhythmic motions as if her pussy is trying to drain me dry."
                "Her powerful succubus sex qualities tingle through my body and deliver immense pleasure, beyond the standards of any other mare."
                "She bites her lip when she notices my hips rocking to match her own pace, bouncing her up and down and making her large pillowy tits jiggle as the intensity increases."
                butters "Haahh, this feels really good. I think it's time you let me have a taste of your cum, right darling?"
                "Her movements are adept as she takes my entire cock from glans to hilt in her rapid assault of thrusts."
                "In no time at all, my cock is feeling tight and full, almost ready to burst into Butters's dribbling cunt."
                play sound cum
                show butters succubussex4 with cum
                play sound cum
                show butters succubussex4 with cum
                "My cock swells and suddenly releases a torrent of seed deep into her pussy and womb, sending the riding succubus into a fit of ecstasy and almost immediately making her come too."
                play sound cum
                show butters succubussex4 with cum
                play sound cum
                show butters succubussex4 with cum
                butters "Ohh fuck yeah! Mmmphh, ahhh, aaahhh!"
                "She continues to ride my cock eagerly, never satisfied with just one load of cum."
                "After a few minutes of more rapid thrusts, this time bubbling and squelching with cum I feel close to a second orgasm."
                show butters succubussex5 with dissolve
                butters "Are you ready, baby? My womb is waiting..."
                play sound cum
                show butters succubussex4 with cum
                play sound cum
                show butters succubussex4 with cum
                "My body tenses and my mind is overwhelmed with euphoria as my orgasm is unleashed; a second torrent of hot cum erupts deep into Butters's eager pussy."
                play sound cum
                show butters succubussex4 with cum
                play sound cum
                show butters succubussex4 with cum
                butters "Ahhh, ahhh, yes! Don't hold back, [playername]!"
                "She quivers, riding with increased passion as her womb is filled up. Her eyes rolling back as she has another powerful orgasm."
                "Butters's tongue hangs lewdly from her mouth as she's pumped with multiple loads of my cum, far more than I should ever let out in a regular orgasm, let alone my second in a row."
                stop music fadeout 3.0
                stop ambience fadeout 3.0
                hide butters with dissolve
                "We're both left panting as she flops off me, grinning blissfully and rubbing her curse mark satisfied."
                show butters closesuccsatisfied with dissolve
                butters "Mmm... Proper sex feels far too good, so glad I don't have to just masturbate and fuck the occasional plant."
                "She gives me a wet kiss as we embrace and slowly fall asleep."
                scene bg black with dissolve
                "..."
                if livingwithbutters == 0:
                    scene bg black with dissolve
                    show bg buttersbed with dissolve
                    "In the morning I kiss Butters goodbye and return home."
                    scene bg black with dissolve
                    "..."
                    jump altmorning
                else:
                    jump morning
            "Reverse-Cowgirl" if butterschocolates == 1:
                label succbuttersrcg:
                    pass
                scene bg buttersbednight with dissolve
                play music sex1 fadein 3.0
                "The two of us saunter over to the bedroom and she pushes me down onto the bed."
                show butters closesucchorny with dissolve
                butters "Oh yeah, I'm gonna fuck you real good."
                "Butters turns around and wiggles her butt with a lecherous grin, while she begins to stroke my cock."
                butters "Ohh, you got erect so quickly, I didn't even need to use any succubus trickery to get you rock hard..."
                mc "Hey, you're hot, no trickery needed."
                butters "Heh, you flatter me... And I flatten you..."
                show butters succreversecowgirl1 with dissolve
                "She coos and kisses the tip of my cock to give it a little bit of succubus magic, before straddling me and lustfully lowering herself, sliding down my cock in one smooth motion."
                "With my cock fully buried inside of her, I spread her pillowy cheeks with my hands and get a good view of her dripping wet pussy."
                butters "Ooo, getting touchy are we? I wouldn't be able to resist either if I were you, tehehe."
                "She begins to grind her hips back and forth, occasionally thrusting up and down as she energetically rides me."
                butters "Ahhh, ahhh... I'm glad you're my partner [playername], I bet there's no cock quite like yours..."
                mc "It's true!"
                "In response, I rock my hips into her movements, causing her ass to thwap against with the force of us both in our rut."
                "Butters giggles and moans with glee as she lecherously gyrates and bounces against me for long salacious minutes that leave us both in euphoria."
                "Her succubus pussy is even more pleasureful than her regular form, forcing my cock to cum far sooner."
                play sound cum
                show butters succreversecowgirl2 with cum
                play sound cum
                show butters succreversecowgirl2 with cum
                butters "Ohh, ohhh! That came outta nowhere! Mmmphh..."
                "She doesn't stop riding for a second, and thanks to her succubus magic my cock stays rock hard in her pussy."
                "With my cum dripping inside of her, she orgasms too, her pussy constricting around my cock with purpose."
                "She continues to ride for a further few minutes, basking in the glory of yet anonther orgasm while denying me mine."
                "Eventually shes takes mercy and her slick, wet pussy rides me fast enough to push me over the edge."
                play sound cum
                show butters succreversecowgirl2 with cum
                play sound cum
                show butters succreversecowgirl2 with cum
                "I finally climax in unison with her as a torrent of my semen unloads into her waiting womb."
                play sound cum
                show butters succreversecowgirl2 with cum
                play sound cum
                show butters succreversecowgirl2 with cum
                butters "Mmmm, mmphhh, fill my impure womb! Ahhh, aahhhh!"
                hide butters with dissolve
                stop music fadeout 3.0
                stop ambience fadeout 3.0
                "After the peak, she collapses backwards and cuddles into my chest. Her horn narrowly almost bashing me in the head with her carelessness."
                "We lie together and embrace like lovers, falling asleep into the night."
                scene bg black with dissolve
                "..."
                if livingwithbutters == 0:
                    scene bg black with dissolve
                    show  bg buttersbed with dissolve
                    "In the morning I kiss Butters goodbye and return home."
                    scene bg black with dissolve
                    "..."
                    jump altmorning
                else:
                    jump morning
            "Leg-Up Doggystyle" if buttersroses == 1:
                scene bg buttersbednight with dissolve
                play music sex1 fadein 3.0
                butters "You wanna be in control? Think you can handle being on-top with a succubus? Ahaha."
                hide butters with dissolve
                "She hovers to the bedroom with her wings before seductively kneeling down onto the bed, face first into a pillow."
                show butters succlegupdoggy1 with dissolve
                "In an incredibly erotic display, her rump raises, followed by one of her legs."
                "Her soaking wet and ready pussy drips down onto the bed sheets, and the tip of her succubus tail flicks back and forth."
                butters "Mmm, I'm all yours, baby..."
                "I bring one hand under her raised leg, and another to her hip as I brush the tip of my cock against the lips of her vulva."
                butters "No teasing, fuck me hard!"
                show butters succlegupdoggy2 with dissolve
                "Her rump pushes back into me slightly and I respond by pushing into her even harder, pushing my cock all the way into her warm, inviting pussy in one smooth motion."
                show butters succlegupdoggy2deep with dissolve
                "Immediately it constricts around me, squeezing and tightening around my shaft."
                butters "Aahh! Mmmphhh, w-wow, it feels weird not being on top... Ahhh..."
                show butters succlegupdoggy2 with dissolve
                show butters succlegupdoggy2deep with dissolve
                "I grip her hips and leg and begin thrusting into her soft pillowy ass, pulling out as far as I can before slamming myself back into her needy pussy."
                show butters succlegupdoggy2 with dissolve
                show butters succlegupdoggy2deep with dissolve
                "Her eyes roll back as I slam into her, each thrust elicits a moan of pleasure from my horny lover."
                show butters succlegupdoggy2 with dissolve
                show butters succlegupdoggy2deep with dissolve
                "She squirms and groans under my assault, her pussy contracting as her easily earned orgasms start to overwhelm her body with pleasure."
                show butters succlegupdoggy3 with dissolve
                show butters succlegupdoggy4 with dissolve
                "As she climaxes, her insides squeeze down around my shaft and she cries with pleasure."
                show butters succlegupdoggy3 with dissolve
                show butters succlegupdoggy4 with dissolve
                "Her back arches, and her tits mash against the bed sheets below as her body quivers in response to the overpowering sensations."
                show butters succlegupdoggy3 with dissolve
                show butters succlegupdoggy4 with dissolve
                "My cock erupts inside of her and we both cum in unison, both losing our minds in the primal heat of the moment."
                play sound cum
                show butters succlegupdoggy5 with cum
                show butters succlegupdoggy5deep with dissolve
                butters "Aahh, ahhh... Y-You're really good at this... I should have expected it from the alpha that fucks all the local mares..."
                show butters succlegupdoggy6 with dissolve
                butters "Mmphh... Don't think I'm satisfied with just one load... Keep going lady-killer."
                "I continue to fuck her cum filled pussy for a few minutes, and she comes a few times turning this once dominant succubus into a slutty submissive mess."
                show butters succlegupdoggy5 with dissolve
                show butters succlegupdoggy5deep with dissolve
                "My cock throbs and my orgasm teeters on the edge, her pussy just feels too good."
                butters "Fill me up again! So much delicious cum!"
                play sound cum
                show butters succlegupdoggy5 with cum
                show butters succlegupdoggy5deep with dissolve
                play sound cum
                show butters succlegupdoggy5 with cum
                show butters succlegupdoggy5deep with dissolve
                "I grit my teeth and with one last, mighty thrust, my cock swells and begins to launch several blasts of thick cum into her."
                play sound cum
                show butters succlegupdoggy5 with cum
                show butters succlegupdoggy5deep with dissolve
                play sound cum
                show butters succlegupdoggy5 with cum
                show butters succlegupdoggy5deep with dissolve
                stop music fadeout 3.0
                stop ambience fadeout 3.0
                butters "Aahh, so much... Oooo..."
                show butters succlegupdoggy6 with dissolve
                "Exhausted, I pull out my cock, along with a glop of sex fluids."
                "She grins behind the pillow and enjoys the feeling of my hot cum dripping out of her pussy before we snuggle together."
                "My eyes feel heavy as we cuddle and slowly drift off into a peaceful sleep."
                scene bg black with dissolve
                "..."
                if livingwithbutters == 0:
                    scene bg black with dissolve
                    show  bg buttersbed with dissolve
                    "In the morning I kiss Butters goodbye and return home."
                    scene bg black with dissolve
                    "..."
                    jump altmorning
                else:
                    jump morning
            "Back":
                butters "Sorry love, but I don't accept take-backsies."
                jump eveningbutterssuccsexmenu
    label eveningbutterssucctalk:
            menu:
                "Who are you exactly?":
                    mc "Who are you exactly?"
                    show butters succsadistic with dissolve
                    butters "Hard to say. I've asked myself that question a few times too."
                    butters "Am I the spirit of another? Am I merely a dark alternate personality of Butters?"
                    butters "I killed the only person that could answer that in a fit of lust."
                    mc "You do act a lot like Butters sometimes, don't you think?"
                    show butters succangry with dissolve
                    butters "I've been stuck here for a very long time [playername], she rubs off on me."
                    show butters succneutral with dissolve
                    butters "But I actually agree with you, my theory is that I'm simply a succubus version of Butters."
                    butters "Whatever I am, I'm a part of her now, she can't get rid of me."
                    mc "Don't worry, you're not exactly a priority."
                    mc "As long as you're not a nuisance."
                    show butters succsatisfied with dissolve
                    butters "I know my place, if I act too wild Butters would be thrown in jail and I'd be stuck too."
                    show butters succfufufu with dissolve
                    butters "So you ain't gotta worry about little ol' me."
                    mc "Sure, don't think I forgot that you tried to kill me once though."
                    show butters succangry with dissolve
                    butters "But I told you I'd try to avoid killing you!"
                    mc "That you did, but it doesn't change the fact."
                    butters "Well... I'm not apologising, that's just who I am."
                    mc "Guess we're at a stand-still then."
                "What do you want out of life?":
                    mc "So... What's your end-goal here? How are you trying to live a fulfilling life?"
                    show butters succangry with dissolve
                    butters "Don't say that existential crap, it's bad enough living as an alternate personality."
                    mc "What do you want out of life though?"
                    show butters succneutral with dissolve
                    butters "Whatever makes Butters happy, makes me happy, vice versa."
                    mc "Oh really?"
                    show butters succhappy with dissolve
                    butters "Yep, so I guess the meaning of my life is simply to make Butters happy."
                    mc "That's quite sweet."
                    butters "Not a lot else I can do, you're the only person I can talk to, and have sex with."
                    mc "Is that why you've started appearing when I'm around?"
                    show butters succneutral with dissolve
                    butters "Guess so, I appreciate the company."
                    butters "Keep giving it to me, and we can make Butters double happy."
                    mc "I don't think it works like that. But I don't mind spending time with you to make {i}you{/i} happy."
                    show butters succhappy with dissolve
                    butters "Well damn, you're gonna make this black heart swoon."
                "Ever catch Butters doing anything weird?":
                    mc "You're always observing Butters' actions, right?"
                    butters "More or less, we share a memory."
                    mc "That means she's observing your actions too?"
                    butters "Yep, once I turn back after a good nap, sex or a whack to the head, she'll remember everything."
                    mc "Huh, interesting... Ever catch Butters doing something weird?"
                    show butters succlaughing with dissolve
                    butters "Ahaha, she'd hate me if I told you, but when she masturbates she says your name."
                    mc "Really? How long has she been doing that?"
                    show butters succhappy with dissolve
                    butters "It's a recent thing, guess we know what she's imagining."
                    butters "I'll let you in on another secret, I imagine the same thing too."
                    mc "Why me? You two have a crush or something?"
                    butters "I guess we do, but we're not exactly subtle about it."
                    show butters succneutral with dissolve
                    butters "I mean she offered to dedicate her life to you, you could practically ask her to marry you and she'd say yes."
                    butters "Don't you dare break her heart though, I know you have 'business' with other mares."
                    mc "Yeah, I'm not ready to settle quite yet."
                    show butters succlaughing with dissolve
                    butters "Well, when you are ready, why settle for one personality when you can have two? Right?"
                    mc "One personality and one nuisance that begs for sex."
                    show butters succneutral with dissolve
                    butters "But it's great sex, you can't deny that."
                    mc "That I can't..."
                "Back":
                    jump eveningbutterssuccmenu
            $ succbutterstalks = 1
            jump eveningbutterssuccmenu

            #$ rand = renpy.random.randint(1,2)
            #if rand == 1:
            #    show butters closesucchorny with dissolve
            #    butters "Enough blue-balling me [playername], are you gonna let me ride that cock, or what?"
            #    menu:
            #        "Sure":
            #            jump eveningbutterssuccsexmenu
            #        "Not tonight":
            #            show butters closesuccangry with dissolve
            #            butters "..."
            #if livingwithbutters == 0:
            #    "I thank Butters for the conversation, kiss her goodbye with tongue, and return home before it gets too late."
            #    scene bg black with dissolve
            #    "..."
            #    jump sleep
            #else:
            #    hide butters with dissolve
            #    "After our chat-filled evening, we both go to bed."
            #    if rand == 1:
            #        "As SuccuButters kisses me goodnight, I suddenly realize my mistake as my body responds with pure arousal."
            #        play music danger fadein 2.0
            #        "She just beguiled me! The bitch!"
            #        show butters succubussex2 with dissolve
            ##        butters "Did you really think you could refuse me?"
            #        butters "Hahahaha, I'm gonna fuck you anyway!"
            #        play ambience sex
            #        scene bg black with dissolve
            #        show butters succubussex4 with dissolve
            #        butters "Fuck yeah, your cock feels so good!"
            #        butters "Fill up my impure womb with your cock milk!"
            #        stop ambience fadeout 5.0
            #        "She fucks me energetically for at least an hour before we go to bed."
            #        stop music fadeout 3.0
            #        scene bg black with dissolve
            #    show bg buttersbednight with dissolve
            #    jump morning
    label poyotalk:
        menu:
            "How did you develop so quickly?":
                poyo "I'm not exactly the most interesting person to talk to, I'm young and have barely any life experience."
                mc "You developed so quickly though, you can talk and look after yourself. What's up with that?"
                poyo "Us slime girls fully develop after only 24 hours, pretty easy to do since we're essentially clones."
                mc "Do you have any idea why you developed so fast?"
                poyo "Do ya think I went to slime school in the short time I've been alive? Sheesh, gimmie a break dad!"
                mc "You say that, but you're incredibly intelligent for such a young creature."
                poyo "It's prolly evolution or something."
                poyo "I took a lot of brain knowledge stuff from my mom."
                "Poyo and I talk about the intricacies of slime biology for a few moments before she gets bored."
            "Talk about Poyo's mom":
                poyo "What exactly did you do with my mom?"
                mc "It's more what she did with us, she launched herself at Butters and started mating with her."
                poyo "And you fertilised me, right? That's what Butters said."
                mc "Yeah, but I didn't actually have sex with your mom, there was no vaginal penetration."
                mc "Although as to what extent a slime girl can have a vagina, I'm not sure."
                poyo "Half the fun of slime sex is using your imagination."
                mc "You say that as if you're experienced."
                poyo "I have a few memories from my mom, but I'm not exactly gasping for sex like she seemed to be."
                mc "You share some memories of hers?"
                poyo "Eh, kinda... It's mostly in my head, sometimes I know things that I shouldn't yet, cos she knew them."
                poyo "But it's also her mom, and her mom's mom, there's a whole line of knowledge and instinct that gets passed down."
                "Poyo and I talk about her lineage for a few moments before she gets bored."
            "Ask Poyo about her plans":
                mc "Are you really planning on living here?"
                poyo "Not forever, just while I grow up, in a few weeks I'll be ready to spread my seed and breed too."
                poyo "I don't want to use you and Butters as hosts, so I'll need to go somewhere else."
                mc "So you'll be ready to breed in a few weeks... What exactly is the lifespan of a slime?"
                poyo "I don't think we die, but we do get an overwhelming desire to pass on the best parts of our DNA before nature wears and tears us."
                mc "That must have been the stage of life your mother was at then."
                poyo "Oh yeah, the horny hoe."
                mc "Why did you decide to stay here instead of living with other slimes?"
                poyo "The same reason as Devil the bunny stays here instead of living in the wild, even when given the choice she would return."
                poyo "It's safe, it's low energy and I get all my needs satisfied."
                mc "I can't argue with that, I guess."
            "Back":
                jump poyomenu
        $ poyotalks = 1
        jump poyomenu
    label poyosex:
        poyo "Y-You wanna have sex with me? But I'm basically your adoptive daughter!"
        menu:
            "Do you wanna do it, or not?":
                poyo "Well, duh! Of course I wanna do it..."
                poyo "H-How about I just give you a blowjob?"
                menu:
                    "Sure":
                        jump poyoblowjob
                    "Nah":
                        jump poyomenu
            "Doesn't that make it even better?":
                poyo "I-I mean... Yeah... It's rather arousing..."
                poyo "How about I suck you off?"
                menu:
                    "Sure":
                        jump poyoblowjob
                    "Nah":
                        jump poyomenu
            "You're right, my bad.":
                jump poyomenu
        label poyoblowjob:
            stop music fadeout 3.0
            "Am I really going to do this? The lengths a man will go to get some."
            play music sex1 fadein 3.0
            poyo "I'll never turn down the opportunity for some delicious nutrients, even if it's from you..."
            "The slime girl opens her mouth and waggles her tongue back and forth in a way I must assume is flirtatious, but it comes across as silly."
            hide slimegirl with dissolve
            show poyo blowjob with dissolve:
                xpos 300
                ypos 0
            "I jack myself off until I get an erection and allow Poyo to take it in her hand and direct it into her gelatinous mouth."
            play sound cum
            "I press the tip of my cock against a soft wall inside, it’s more of a fake mouth to give the illusion, only one inch inside there’s a barrier of slime that I have to push through."
            play ambience blowjob
            "Regardless my cock sinks in deeper, and a makeshift tongue starts to coil and drool over my shaft."
            "The insides of the slimy pseudo-mouth are warm, and the constricting slime around my shaft is very tight and pleasureful."
            poyo "Mmphhh, I bet my blowjobs are the best!"
            "She wasn’t wrong, the slime inside her is sucking me like it’s trying to milk an udder. While her lips wrap around my cock and slide up and down my shaft providing two simultaneous sensations."
            "Poyo is starting to speed up, she's sucking my cock inhumanly fast, with a fantastic technique."
            "It's like Poyo has full control over every inch of her body, so she can expertly massage, and focus on each inch of my shaft with precision."
            poyo "Mmmhh, ahh, I want your cummies daddy."
            "My cock throbs at her woefully lewd words, it won't take me long to explode inside of her."
            "Poyo also constantly adapts, she responds to my body language and focuses its pleasure around the neck of my glans and other sensitive areas, it’s like having a blowjob and sex simultaneously."
            poyo "Cum for me, cum for me daddy..."
            "I’m extremely close after only a few minutes but I don’t have much choice with this slime girl, evolved to make people cum."
            "I can't hold back any more, I can feel a pressure in my loins and it’s building up extremely quickly."
            play sound cum
            show poyo blowjob2 with cum
            play sound cum
            show poyo blowjob2 with cum
            "The slime milks my cock like a pro, and after mere minutes of sucking, I’m cumming loads into this amorphous sex blob."
            stop ambience fadeout 2.0
            "It’s a strange sensation to see my cum drift through this see-through slime creature, I guess there’s no question on whether or not she swallows."
            hide poyo with dissolve
            "After I cum, I pull back with a satisfying pop."
            show slimegirl with dissolve
            poyo "Mmm, so delicious..."
            poyo "I'll put these nutrients to good use. Thanks daddy!"
            stop music fadeout 3.0
            jump poyoend
    label poyoend:
        if livingwithbutters == 0:
            "I say goodbye to Poyo and return home before it gets too late."
            scene bg black with dissolve
            "..."
            jump sleep
        else:
            scene bg buttersbednight with dissolve
            "After spending the evening with Poyo, I return to Butters's room and snuggle into bed with her."
            jump morning
    label buttersimpregintro:
        $ buttersmissionaryunlock = 1
        play music butters fadein 3.0
        show butters happy with dissolve
        mc "Oh hey, you're in the nude, that's unusual for you."
        show butters laughing with dissolve
        butters "Hey [playername], you almost caught me in the act."
        mc "The act? Were you masturbating, or something?"
        show butters neutral with dissolve
        butters "Mmm, yeah... I've been really horny, lately..."
        butters "Uhm... Could we talk for a moment?"
        mc "Hm? Isn’t that exactly what we were going to do anyway?"
        show butters angry with dissolve
        butters "Yeah, but I want to be a little extra serious for a second."
        mc "You don’t need my permission for that, go for it."
        show butters neutral with dissolve
        butters "Well… It’s just… I really, really like you [playername]."
        butters "Maybe even… l-love? I know we’re not dating, and I’m totally okay with that! But my heart flutters with happiness whenever I see you."
        mc "That’s really sweet, Butters. I’d say I feel pretty similarly."
        show butters happy with dissolve
        butters "I would be completely okay serving you as a maid, you just need to say the word! I’m yours, in body and mind!"
        mc "Yeah… I already told you that’s not necessary though. I like you as you are right now."
        show butters neutral with dissolve
        butters "I see… You’re so kind, [playername]."
        butters "But… can you hear out my one selfish request?"
        mc "What’s that?"
        show butters horny with dissolve
        butters "I want you to… impregnate me… I’d like to have a child, and I want you to be the father."
        mc "…"
        mc "That’s… intense…"
        show butters neutral with dissolve
        butters "You may be the father, but I’ll look after the child… It’s a bit selfish, but this is more for me than you…"
        mc "I think I understand. You want a raise a child, alone or with a partner, and you want me to act as the sperm donor?"
        show butters happy with dissolve
        butters "Yeah, I think so! I don’t want to push any responsibility onto you, you’ll be a surrogate."
        mc "Okay, but how am I going to get you pregnant? Humans and ponies are incompatible."
        show butters laughing with dissolve
        butters "I made a potion just for that, it’s called the 'interspecies fertility' potion."
        butters "It converts all sperm that enters the womb into a type that can fertilise the egg."
        mc "So… What species would the child be?"
        show butters happy with dissolve
        butters "I'm fairly sure the child will have my exact DNA, almost like a clone."
        butters "So it’d be a regular ol’ earth pony. Maaaaybe with batwings, I’m not quite sure."
        mc "Hmm… That’s a big decision you’re pushing on me."
        show butters neutral with dissolve
        butters "I know… I’m sorry… What do you think?"
        menu:
            "Yeah, I’ll impregnate you.":
                jump buttersimpregmissionary
            "I’ll think about it.":
                pass
            "No, I’m not interested in that.":
                show butters sad with dissolve
                butters "Ahh, that’s a shame… I understand though."
        show butters neutral with dissolve
        butters "If you decide to, just let me know. I won’t pester you about it."
        show butters horny with dissolve
        butters "Although, would you like to have sex regardless? I’ve been thinking about this a lot and it has made me insatiably horny lately, hehe."
        "(You’ve unlocked missionary position with Butters.)"
        menu:
            "Fuck her now":
                jump buttersnonimpregmissionary
            "Maybe later… (Accessible from the sex menu)":
                show butters happy with dissolve
                butters "Okie, if you need anything, just let me know!"
                butters "Give me a moment, I'm going to get redressed."
                if buttersimpregintro == 1:
                    scene bg buttershouse with dissolve
                    show butters dresshappy with dissolve
                    jump buttersnormalmenu
                else:
                    scene bg buttershousenight with dissolve
                    show butters dresshappy with dissolve
                    jump eveningbuttersmenu

        ## buttersimpregmissionary
        label buttersimpregmissionary:
            $ butterspregnant = 1
            show butters happy with dissolve
            butters "Ooohh, thank you so much! This is really exciting."
            show butters horny with dissolve
            butters "And arousing too! I mean… I do have a thing for impregnation…"
            mc "Heh, so that’s why you weren’t so bothered about the slime."
            show butters neutral with dissolve
            butters "I spent a lot of time masturbating that night, ehehe."
            hide butters with dissolve
            "My eager lover grabs a pinkish alchemical potion and gulps the entire thing."
            "Usually she always brews two servings, however, not a single drop goes to waste as she finishes the entire bottle."
            show butters happy with dissolve
            butters "Ahhh... Now I should be fertile. At least until I pee a few times."
            mc "Will I need to cum inside you a lot, then?"
            show butters laughing with dissolve
            butters "Nuh-uh, only a single load of cum should be sufficient."
            mc "Sheesh, that’s {i}really{/i} fertile!"
            show butters horny with dissolve
            butters "We can go for extra rounds if you’d like!"
            mc "I wouldn’t be against that."
            scene bg black with dissolve
            play music sex1 fadein 3.0
            stop ambience fadeout 3.0
            show butters missionary1 with dissolve
            "We walk to the bedroom where Butters readily presents herself to me on the bed."
            if buttersimpregintro == 1:
                "She looks beautiful right now. A cast of light shimmers from the rising sun, through the mountains, and peers through the window to illuminate her body."
            else:
                "She looks beautiful right now. A cast of moonlight shimmers through the mountains, and peers through the window to illuminate her body."
            "All this beauty, and I’m lucky enough for her to offer it to me."
            butters "Hah... [playername]..."
            "She’s so wet, she’s clearly in a very lustful mood. Her legs are already splayed open as she eagerly awaits penetration."
            "I approach the bed, drinking in every detail of her beautiful form."
            show butters missionary2 with dissolve
            "Her tail flickers excitedly as I kneel before her and pull her hips slightly closer."
            butters "Oh my…"
            "She blushes a little as I close the distance and lean close over her in a traditional missionary position."
            "My lover is no doubt horny, but she still deserves to be treated with love. I brush my fingers through her messy locks of silken hair while I kiss her."
            "With one hand I massage her large soft breasts, while I masturbate my growing erection with the other."
            "Once fully erect and ready to go, I bring myself back upright with my eyes on the prize."
            "Butters takes a deep breath and shivers in anticipation of my touch, her tail practically curling around my thigh needily."
            butters "Ahh, I-I’m all yours."
            "With her cheeks flushed in desire, I grin as I take the head of my cock and rub it up and down her vulva."
            play sound cum
            show butters missionary3 with dissolve
            "She’s dripping wet, causing my tip to glisten in the glow of the sun. Having teased her enough, I line up with her entrance and push inwards."
            "I slide myself deeply into my lover, strings of sticky wetness connect us as my shaft pushes into the deepest reaches of her nether."
            butters "Aahhh, aahhh… It seems the potion has made it feel even better than usual."
            "The walls of her pussy clamp down around my member, enveloping me in warmth and squeezing pleasantly around every nerve ending."
            play ambience sex fadein 3.0
            "I groan and she moans with pleasure as I slide back out, and push back deeply until I'm at the hilt of her inviting insides."
            "With each thrust, Butters' large breasts and juicy ass jiggle, and an adorable moan escapes her mouth."
            "Finding a pace of deep and sensual fucking, indecent squelching noises mix with the moans each time our bodies come together."
            "It would seem that the potion had some side effects beyond fertility, because I’m sure Butters isn’t usually this wet."
            "It’s also impossible to deny the pleasure she’s feeling, as she throws her arms and head back into the pillow, her tongue lolling slightly as her mind blanks from the powerful erotic sensations."
            butters "Ooohh, keep going… I’m getting close. Ahh, ahh…"
            "I continue my rutting, using her plump thighs as leverage in order to pump her deeply and hard. As she’s getting closer and closer, she wraps her legs around my hips and pull me deeper."
            show butters missionary4 with dissolve
            butters "Yeahh, yesss… Oh, [playername], I’m going to come! Ahh, ahh!"
            "She moans aloud as her eyes roll back in the wake of a full body orgasm."
            "As her pussy contracts and sucks around my shaft, I redouble my passion-filled fucking and pound her pussy with determination to fill it with my cum."
            "Her sloppy cunt squeezes even tighter around my cock, causing me to throb and drip precum. It doesn’t take long for the familiar sense of impending orgasm to arrive."
            "My muscles grow tense, and my cock stiffens as my climax swells up deep inside. The constant moaning and shifting of my partner pushing me over the edge as she beckons me to cum."
            butters "Cum for me, cum for me [playername]! I want you to fill my womb, impregnate me!"
            play sound cum
            show butters missionary5 with cum
            play sound cum
            show butters missionary5 with cum
            "And just like an orgasm switch was pressed, the pressure reaches breaking point, my cock swells and I unload copious amounts of cum deep into my highly fertile lover."
            play sound cum
            show butters missionary5 with cum
            play sound cum
            show butters missionary5 with cum
            "Butters seems to orgasm a second time in a row, indulging in the euphoria of being filled with hot, thick semen."
            play sound cum
            show butters missionary5 with cum
            play sound cum
            show butters missionary5 with cum
            "My orgasm is more powerful than I anticipated, and the volume of cum her pussy wrings out is a far larger quantity than usual."
            play sound cum
            show butters missionary5 with cum
            play sound cum
            show butters missionary5 with cum
            "Three loads, six, nine, twelve?! The potion must have had a residual effect on my semen."
            "There’s so much that it drips and splatters outwards, splattering our point of connection."
            "Butters enjoys her orgasm and the moment so much, that she doesn’t unwrap her legs and let me stop fucking until my cock started to get sensitive."
            show butters missionary6a with dissolve
            stop ambience
            stop music fadeout 3.0
            "We both pant as she unwraps her legs and I pull back, some more cum oozing over her pussy. There’s so much cum that you can’t even see her vulva."
            "She looks up to me, seemingly exhausted, but smiling with glee."
            "I wonder if that got her pregnant? If this was a hentai game, I'd probably see one of those egg fertilisation cut-ins. Heh, what a ridiculous thought."
            if buttersimpregintro == 1:
                play ambience ambienceday fadein 5.0
            else:
                play ambience ambiencenight fadein 5.0
            mc "So, how’d I do?"
            butters "Haahhh… It’ll take a while, but I think you successfully put a bun in the oven, hehe!  *Pant*"
            if bakeryvisit1 == 1:
                mc "Hah, I’d expect that type of comment from Cream, not you!"
            else:
                pass
            butters "I’m so excited. I’m finally going to be a mother, after all these years!"
            mc "Congratulations. If in a few months there’s no baby bump, be sure to gimmie a call."
            butters "Aha, I hope you’ll cum inside me a lot more regardless."
            scene bg black with dissolve
            "We cuddle lovingly for the next five minutes, just enjoying the feeling of each other’s softness. Her fur, contrasting against my supple skin."
            if buttersimpregintro == 1:
                show bg buttersbedday with dissolve
            else:
                show bg buttersbednight with dissolve
            show butters closelaughing with dissolve
            butters "Mmm… I really enjoyed this."
            butters "Maybe we can do this again later. You should definitely fuck me again tomorrow! I think I’ll take one more load of cum just in case."
            menu:
                "Sure thing, I’ll happily donate my cum to any mare in Arcadia.":
                    butters "Awhh, you’re such a perv!"
                "Anything for you, darling.":
                    butters "You're such a sweetheart..."
            if buttersimpregintro == 1:
                butters "Well, we best get ready to face the day."
                scene bg black with dissolve
                "..."
                scene bg buttershouse with dissolve
                show butters dresshappy with dissolve
                jump buttersnormalmenu
            else:
                butters "Awhh, you’re such a perv! Come on, let me treat you to some dinner"
                scene bg black with dissolve
                "..."
                scene bg buttershousenight with dissolve
                show butters dresshappy with dissolve
                jump eveningbuttersmenu
        ## buttersnonimpregmissionary
        label buttersnonimpregmissionary:
            show butters neutral with dissolve
            if buttersimpregintro == 1:
                butters "Ooohh, I usually try to avoid sex in the morning, but I’m so horny lately..."
            else:
                butters "Ooohh, I usually try to avoid sex before dinner, but I’m so horny lately..."
            mc "It must be that maternal instinct finally kicking in now that you’re cured."
            show butters horny with dissolve
            butters "Yeah… I do really like the idea of getting impregnated, it’s really arousing."
            mc "Heh, so that’s why you weren’t so bothered about the slime."
            show butters laughing with dissolve
            butters "I spent a lot of time masturbating that night, ehehe."
            butters "Either way, I guess I won’t be needing this."
            show butters neutral with dissolve
            "Butters puts away a near glowing bottle of pinkish liquid, she shrugs as she turns to me."
            show butters happy with dissolve
            butters "That’s the ‘super-fertile’ fluid. Although I suppose I won’t need it if you’re not interested."
            scene bg black with dissolve
            play music sex1 fadein 3.0
            stop ambience fadeout 3.0
            show butters missionary1 with dissolve
            "We walk to the bedroom where Butters readily presents herself to me on the bed."
            if buttersimpregintro == 1:
                "She looks beautiful right now. A cast of light shimmers from the rising sun, through the mountains, and peers through the window to illuminate her body."
            else:
                "She looks beautiful right now. A cast of reflected light shimmers from the moon, through the mountains, and peers through the window to illuminate her body."
            "All this beauty, and I’m lucky enough for her to offer it to me."
            butters "Hah... [playername]..."
            "She’s so wet, she’s clearly in a very lustful mood. Her legs are already splayed open as she eagerly awaits penetration."
            "I approach the bed, drinking in every detail of her beautiful form."
            show butters missionary2 with dissolve
            "Her tail flicks excitedly as I kneel before her and pull her hips slightly closer."
            butters "Oh my…"
            "She blushes a little as I close the distance and lean close over her in a traditional missionary position."
            "My lover is no doubt horny, but she still deserves to be treated with love. I brush my fingers through her messy locks of silken hair while I kiss her."
            "With one hand I massage her large soft breasts, while I masturbate my growing erection with the other."
            "Once fully erect and ready to go, I bring myself back upright with my eyes on the prize."
            "Butters takes a deep breath and shivers in anticipation of my touch, her tail practically curling around my thigh needily."
            butters "Ahh, I-I’m all yours."
            "With her cheeks flushed in desire, I grin as I take the head of my cock and rub it up and down her vulva."
            play sound cum
            show butters missionary3 with dissolve
            "She’s dripping wet, causing my tip to glisten in the glow of the sun. Having teased her enough, I line up with her entrance and push inwards."
            "I slide myself deeply into my lover, strings of sticky wetness connect us as my shaft pushes into the deepest reaches of her nether."
            butters "Aahhh, aahhh… I’m so horny lately. Don’t hold back, I need you to knock some sense into me, heh."
            "The walls of her pussy clamp down around my member, enveloping me in warmth and squeezing pleasantly around every nerve ending."
            play ambience sex fadein 3.0
            "I groan and she moans with pleasure as I slide back out, and push back deeply into the hilt of her inviting insides."
            "With each thrust, Butters large breasts jiggle, and an adorable moan escapes her mouth."
            "Finding a pace of deep and sensual fucking, indecent squelching noises mix with the moans each time our bodies come together."
            "It’s also impossible to deny the pleasure she’s feeling, as she throws her arms and head back into the pillow, her tongue lolling slightly as her mind blanks from the powerful erotic sensations."
            butters "Ooohh, keep going… I’m getting close. Ahh, ahh…"
            "I continue my rutting, using her plump thighs as leverage in order to pump her deep and hard. As she’s getting closer and closer, she wraps her legs around my hips and pulls me closer."
            show butters missionary4 with dissolve
            butters "Yeahh, yesss… Oh, [playername], I’m going to come! Ahh, ahh!"
            "She moans aloud as her eyes roll back in the wake of a full body orgasm."
            "As her pussy contracts and sucks around my shaft, I redouble my passion-filled fucking and pound her pussy with determination to fill it with my cum."
            "Her sloppy cunt squeezes even tighter around my cock, causing me to throb and drip precum. It doesn’t take long for the familiar sense of impending orgasm to arrive."
            "My muscles grow tense, and my cock stiffens as my climax swells up deep inside. The constant moaning and shifting of my partner pushing me over the edge as she beckons me to cum."
            butters "Cum for me, cum for me, [playername]! Fill up my pussy!"
            play sound cum
            show butters missionary5 with cum
            play sound cum
            show butters missionary5 with cum
            "And just like an orgasm switch was flipped, the pressure reaches breaking point, my cock swells and I unload copious amounts of cum deep into my highly fertile lover."
            play sound cum
            show butters missionary5 with cum
            play sound cum
            show butters missionary5 with cum
            "Butters seems to orgasm a second time in a row, indulging in the euphoria of being filled with hot, thick semen."
            "There’s so much that it drips and splatters outwards on our point of connection."
            "Butters enjoys her orgasm and the moment so much, that she doesn’t unwrap her legs and let me stop fucking until my cock started to get sensitive."
            show butters missionary6b with dissolve
            stop ambience
            stop music fadeout 3.0
            "We both pant as she unwraps her legs and I pull back, some more cum oozing over her pussy."
            "She looks up to me, seemingly exhausted, but smiling with glee."
            if buttersimpregintro == 1:
                play ambience ambienceday fadein 5.0
            else:
                play ambience ambiencenight fadein 5.0
            scene bg black with dissolve
            "We cuddle lovingly for the next five minutes, just enjoying the feeling of each other’s softness. Her fur, contrasting against my supple skin."
            if buttersimpregintro == 1:
                show bg buttersbedday with dissolve
            else:
                show bg buttersbednight with dissolve
            butters "Mmm… I really enjoyed this."
            butters "Every time with you is like my first, it’s truly special."
            mc "I could say the same with you. You have some qualities that no mare in Arcadia can match."
            butters "Awhh, you’re such a flatterer."
            butters "If you ever make up your mind about impregnating me, just say the word."
            mc "I'll think about it..."
            butters "I don’t think I’ll find a candidate as amazing as you for a long time, but please don’t feel pressured."
            mc "Yeah, I understand."
            scene bg black with dissolve
            "..."
            if buttersimpregintro == 1:
                scene bg buttershouse with dissolve
                show butters dresshappy with dissolve
                jump buttersnormalmenu
            else:
                scene bg buttershousenight with dissolve
                show butters dresshappy with dissolve
                jump eveningbuttersmenu
    label buttersimpregpaizuri:
        $ butterspregnanteasteregg = 1
        $ milkypaizuriunlocked = 1
        play music butters fadein 3.0
        show butters dresshappy with dissolve
        if livingwithbutters == 1:
            butters "Good morning [playername]! I just got out the shower, and I have great news!"
        else:
            butters "Good morning [playername]! Ohh, I’m so happy to see you! I have great news!"
        mc "What’s that?"
        show butters dresslaughing with dissolve
        butters "I’m definitely pregnant! I think!"
        "Huh? She confirmed that already? That didn’t even cross my mind as being the ‘great news’."
        mc "What figures?"
        show butters dressneutral with dissolve
        butters "Well, ahh, uhmm… Well… Allow me to strip."
        mc "S-Strip?"
        hide butters with dissolve
        "Before I can even protest, the mare humbly tosses her dress aside. I know nudity isn’t than unusual in Arcadia, but I’d be extremely surprised if her pregnancy was already showing."
        "Oh, but it isn’t. In fact, her belly is completely normal. Her breasts on the other hand..."
        show butters milkyhappy with dissolve
        butters "See? My breasts are milky!"
        mc "They’re… leaking?"
        show butters milkylaughing with dissolve
        butters "Hehe, they’re leaking…"
        mc "That doesn’t seem normal. It has been less than one percent of your pregancy, and you’re already producing milk?"
        show butters milkyhappy with dissolve
        butters "This isn’t too unusual of a phenomenon… Alchemy potions can have a lot of side effects, particularly associated with their main effect."
        butters "It would seem that in addition to fertility, the potion also enabled me in other ‘areas’."
        butters "In other words, my body is hyper-ready for a child."
        mc "I… see…"
        mc "Nice…"
        show butters milkyneutral with dissolve
        butters "There’s a small problem though! *Drip, drip*"
        mc "Yeah, yeah. There might be."
        show butters milkyhappy with dissolve
        butters "Until the potion wears off, I’m going to be leaking rather excessively. Could I… possibly ask you to help me again?"
        mc "Oh? You want me to drink it?"
        show butters milkyneutral with dissolve
        butters "N-No! That’d be a terrible idea! If you drank this milk, you’d get the potion’s effects too."
        if fr == 1:
            mc "Ohh, just like the mares I ‘came’ in were cured from Morrigan’s brainwashing?"
        else:
            mc "Really? The milk carries enough residual potion to do that?"
        butters "Mhm… If you digest the milk, the effects will be strong enough for you to get any mare pregnant."
        mc "*Gulp*"
        mc "What can I do then? Am I going to milk you like a cow... girl?"
        show butters milkyhorny with dissolve
        butters "While that’s certainly an option, I had an idea that’d make it fun for you too."
        butters "You see, if I’m aroused, the milk flows a little more freely when I squeeze my boobs."
        butters "So, paizuri should be a fun way to empty my jugs. Want to give it a try? It’ll probably get quite milky and messy."
        menu:
            "Milky Paizuri? Hell yeah.":
                pass
            "It's too early in the morning for sexy times.":
                show butters milkyneutral with dissolve
                butters "*Sigh* Yeah… You’re right, I was thinking with my pussy and not my head."
                butters "I’ll go have a shower and milk myself there, I’ll be back in ten minutes."
                hide butters with dissolve
                "Hmm… I wonder how long she’ll have to struggle with excessive milk."
                "I stick around for a few minutes chatting with Poyo and playing with Devil, eventually Butters returns."
                show butters dresslaughing with dissolve
                butters "Ahhh, my new diet is working great, I lost a few pounds! Ahaha."
                mc "A few pounds of milk?! Jeez…"
                show butters dresshappy with dissolve
                jump buttersnormalmenu
            "Can’t you just milk it yourself? You’re being somewhat melodramatic by asking me.":
                show butters milkyneutral with dissolve
                butters "*Sigh* Yeah… You’re right, I was thinking with my pussy and not my head."
                butters "I’ll go have a shower and milk myself there, I’ll be back in ten minutes."
                hide butters with dissolve
                "Hmm… I wonder how long she’ll have to struggle with excessive milk."
                "I stick around for a few minutes chatting with Poyo and playing with Devil, eventually Butters returns."
                show butters dresslaughing with dissolve
                butters "Ahhh, my new diet is working great, I lost a few pounds! Ahaha."
                mc "A few pounds of milk?! Jeez…"
                show butters dresshappy with dissolve
                jump buttersnormalmenu
        scene bg buttersbedday with dissolve
        "The two of us move to the bedroom and splay a towel on the bed. And then another, for good measure."
        play music sex1 fadein 3.0
        show butters paizuri1 with dissolve
        "Kneeling on the bed, Butters squishes her breasts together, and the milk already starts spitting and dripping."
        butters "See how bad it is? It gets even worse when I’m turned on."
        butters "Come here and let mommy milk you too."
        "Oh god, is she going to be referring to herself as mommy a lot from now on?"
        menu:
            "Call yourself mommy, that’s hot.":
                butters "Oh? Do you want to call me mommy too?"
                menu:
                    "Uhhmm… Sure, mommy.":
                        butters "Oohh, I think I just got a new fetish…"
                    "That’s probably a bad idea.":
                        butters "Hehe, yeah, you’re right. Sorry!"

            "Avoid calling yourself mommy, it’s somewhat uncanny.":
                butters "Ohh, sorry! I didn’t mean it in a sexual context, I’m just very happy about my pregnancy."
        show butters paizuri2 with dissolve
        "I position myself below her on the bed, and lay down between her thighs. Butters takes it upon herself to sit on my thighs, her nude figure arousing me to the point of erection."
        "With little hesitation, she begins to stroke my shaft until my tip throbs and dribbles with precum. Some drops of milk splattering onto my skin."
        "Once she’s satisfied, she lowers her entire body and prepares to put her pillowy bosom to good work."
        show butters paizuri3 with dissolve
        butters "I’ve always wanted to try paizuri, but usually I’m too horny and just want it in my pussy, hehe…"
        show butters paizuri2 with dissolve
        butters "My nipples and even my breasts are extra sensitive now though, so I’m excited to finally do it."
        "My cock throbs at her lewd words, prodding her boobs and causing her to giggle."
        play ambience blowjob fadein 3.0
        "She eases her breasts around my shaft, and then uses her arms to squish them together, squashing my member surprisingly effectively."
        "There were already a few droplets of milk around my cock, creating a warmth and a wetness that lubricates us slightly."
        "She begins to rise and fall, catching the skin of my shaft and pulling it back and forth over my glans eliciting pleasureful sensations despite the otherwise simple and slow motions."
        "Butters wasn’t joking, her breasts really are splaying more milk, her nipples now fully standing to attention as my pelvis dampens with a slight glisten of milk."
        show butters paizuri3 with dissolve
        butters "Ahh, this is hot... Haha, I’m getting really wet, both up here and down there."
        "Suddenly I feel a warmth hit my cock, as a trail of drool slathers over the tip and wettens my entire member as it’s caught within the motion of the titfuck."
        "And just like that, she’s moving even faster. The fur between her chest becoming not only damp, but slick and shiny, rubbing faster and faster."
        "The feeling has slowly devolved from fluffy and cute to moist and erotic."
        show butters paizuri2 with dissolve
        butters "*Drool* Haahh, it feels good when it slides against me."
        mc "Wow, your breasts are that sensitive?"
        butters "Yeah, they’re like one big erogenous zone right now, I can even feel you throbbing."
        "As if she’d been saving a trick, her tongue slithers downwards and starts to tease the most sensitive area of my tip at the peak of each thrust."
        "The effectiveness of her movements makes it arguably even more pleasurable than a standard blowjob. The squeeze of her breasts combined with her tongue is immensely euphoric."
        show butters paizuri4 with dissolve
        "And as she focuses more into the boobjob, the milk sputtering out of her nipples borders on excessive. The now rapid movements of her breasts causing it to splatter and splash everywhere."
        "To the untrained eye, it’d appear as if I’d already ejaculated and coated her breasts with whiteness."
        show butters paizuri5 with dissolve
        "Oh fuck, she’s getting even faster, and clearly trying to make me cum. I can’t focus on anything except the immense pleasure anymore."
        "I relax and give into the pleasure, not holding back my building orgasm a modicum. Before I know it, my cock throbs as a surge of euphoria ascends through my body."
        play sound cum
        show butters paizuri6 with cum
        play sound cum
        show butters paizuri6 with cum
        "Butters keeps her tongue trained on my sensitive tip throughout my entire orgasm, creating a mess of cum that launches over her face, eyes and breasts."
        play sound cum
        show butters paizuri6 with cum
        play sound cum
        show butters paizuri6 with cum
        stop ambience fadeout 3.0
        "I buck my hips against her tight warm breasts throughout my entire orgasm, until the very last load of my cum shoots out, this one landing at the roof of her mouth."
        show butters paizuri7 with dissolve
        butters "Mmmphh… I… I think mommy came, hahah."
        mc "Really? From just that?"
        butters "Eheh, it was only a little orgasm… I still kinda want a proper one."
        mc "Hmm… Clean up all this milk and cum, and I’ll fuck you good enough for two orgasms."
        butters "You have a deal… *Lick, lick*"
        hide butters with dissolve
        "With surprising efficiency, Butters sets to cleaning up all the cum and milks, and she seems to enjoy each second."
        show butters legupdoggy1 with dissolve
        "Then she bends over, and I know what to do…"
        show butters legupdoggy2 with dissolve
        play sound cum
        show butters legupdoggy4 with dissolve
        "I pound her pussy intensely until we’re both cumming again."
        stop music fadeout 3.0
        play ambience ambienceday fadein 3.0
        scene bg black with dissolve
        "Afterwards, we spend some time cuddling together and catching our breath."
        "…"
        butters "So… It’s true, you knocked me up?"
        scene bg buttersbedday with dissolve
        mc "Ahh… AH!?"
        play music danger fadein 3.0
        show butters closesuccfufufu with dissolve
        mc "Don't transform while I have my eyes closed..."
        mc "But, yeah."
        "She must have turned during our post-coital cuddling."
        show butters closesucclaughing with dissolve
        butters "That’s pretty lewd, I guess. Ahahaha, I didn’t know you had it in you, [playername]!"
        "Playfully toying with her nipples, she grins as they drip with milk."
        mc "You’re not going to ask me to have sex with you again, are you?"
        show butters closesucchappy with dissolve
        butters "Fear not, our libidos are connected, so I am quite satisfied indeed…"
        show butters closesuccsatisfied with dissolve
        butters "In fact, I have an overwhelming urge to be cuddled. Come on, wrap your arms around me."
        mc "Alright, but only five more minutes. We’ve got work."
        show butters closesuccneutral with dissolve
        butters "Fiiine…"
        scene bg black with dissolve
        "…"
        "Five minutes later."
        show bg buttershousered with dissolve
        show butters succubus with dissolve
        jump butterssuccmenu
    label butterspregnanteasteregg:
        scene bg buttershouse with dissolve
        play ambience ambienceday
        show butters dresssad with dissolve
        butters "*Sigh*..."
        butters "Morning [playername]..."
        butters "Bad news. I don't think I'm pregnant at all."
        mc "No luck? Weren't you lactating a lot, though?"
        show butters dressangry with dissolve
        butters "Yeah... I think I made a lactation potion, not a fertility potion."
        mc "Hmm... Damn... Are you going to try again?"
        show butters dressneutral with dissolve
        butters "I think so. It'll take a while to collect all the ingredients. Would you still be willing to be the sperm donor?"
        menu:
            "You can count on me":
                show butters dresslaughing with dissolve
                butters "Thanks [playername], I truly do adore you."
            "Fill you with cum? Anytime.":
                show butters dresshorny with dissolve
                butters "Ohh, I could do that right now..."
                butters "But, eh-hem, work first."
            "Depends on my relationship situation.":
                show butters dresssad with dissolve
                butters "I understand. Perhaps you could simply donate some sperm samples rather than input it manually."
                mc "I suppose that's an option too. Although at that point, why not just use another man?"
                show butters dressneutral with dissolve
                butters "Heh... I dunno, I find it hard to fall in love..."
                "Mmm, so she fell in love with me? She probably wants me to marry her and raise the child together."
        show butters dresshappy with dissolve
        $ butterspregnanteasteregg = 0
        jump buttersnormalmenu
