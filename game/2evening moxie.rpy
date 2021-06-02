label eveningmoxie:
    stop ambience fadeout 2.0
    stop music fadeout 2.0
    scene bg moxiewagonlamp with dissolve
    play ambience ambiencenight
    if fr == 1:
        show moxie wneutralhappy with dissolve
    else:
        show moxie happyneutral with dissolve
    $ renpy.pause (0.5)
    "After dinner Moxie and I get cozy on her sofa together."
    jump eveningmoxie2
label eveningmoxie1:
    scene bg moxiewagonlamp with None
    if fr == 1:
        show moxie wneutralhappy with dissolve
    else:
        show moxie happyneutral with dissolve
    if livingwithmoxie == 1:
        moxie "Hey, you're back. The nightlife not as good as ol' Mox?"
    elif livingwithbutters == 1:
        moxie "Ohh boy, it's my favourite visitor! Staying a while? I'll break out the booze."
    else:
        pass
    label eveningmoxie2:
        menu eveningmoxie2menu:
            "Go Outside":
                if fr == 1:
                    jump prefinalworldmapnight
                jump preworldmapnight
            "Talk" if moxietalks == 0:
                jump moxietalk
            "Sex":
                if fr == 1:
                    show moxie closewhorny with dissolve
                else:
                    show moxie closehorny with dissolve
                "You ask Moxie if she wants to do something naughty, she nods eagerly and sidles up to you."
                jump moxiesexoptions
            "Give Gift" if chocolates >= 1 or roses >= 1:
                menu:
                    "Chocolates" if moxiechocolates == 0 and chocolates >= 1:
                        $ moxiechocolates = 1
                        $ chocolates -= 1
                        $ moxiegifts += 1
                        mc "By the way, these chocolates here, they're for you."
                        moxie "Hah, wow, here I thought someone else got you those. I was jealous, no one has gotten me chocolates before."
                        mc "It's just a small gift to thank you for everything you've done for me so far."
                        moxie "You're so kind, I don't know what to say, ehehe."
                        moxie "Come on, let's share a few while we watch a movie."
                        "(You've unlocked the Moxie cowgirl position scene.)"
                        if fr == 1:
                            show moxie wneutralhappy with dissolve
                        else:
                            show moxie happyneutral with dissolve
                        $ moxiecowgirl = 1
                        jump eveningmoxie2menu
                    "Roses" if moxieroses == 0 and roses >= 1:
                        $ moxieroses = 1
                        $ roses -= 1
                        $ moxiegifts += 1
                        if fr == 1:
                            show moxie whappyneutral with dissolve
                        else:
                            show moxie happyneutral with dissolve
                        mc "I've got a surprise for you!"
                        if fr == 1:
                            show moxie wembarrassed with dissolve
                        else:
                            show moxie embarrassed with dissolve
                        "I reveal the bouquet of roses causing Moxie to squee."
                        if fr == 1:
                            show moxie closewlaughing with dissolve
                        else:
                            show moxie closelaughing with dissolve
                        "She runs up and hugs me tightly, kissing me on the cheek."
                        moxie "You're way too kind to me."
                        mc "I was worried roses might be too girly for you."
                        if fr == 1:
                            show moxie whappy with dissolve
                        else:
                            show moxie happy with dissolve
                        moxie "Don't be silly, I love them."
                        moxie "I don't even know how I could repay you."
                        mc "No need, you're already giving me so much by letting me stay here and cooking for me."
                        moxie "Hmm... Even so, I think I could do something new that you might enjoy."
                        "(You've unlocked the Moxie anal scene.)"
                        $ moxieanal = 1
                        jump eveningmoxie2menu
                    "Back":
                        jump eveningmoxie2menu
            "Go to Sleep" if livingwithmoxie == 1:
                hide moxie with dissolve
                show bg moxiebednight with dissolve
                "I go to bed and Moxie soon snuggles up beside me and we doze off together."
                jump morning
            "Move back in" if livingwithmoxie == 0:
                moxie "For sure? You're always welcome."
                menu:
                    "For sure!":
                        moxie "Well it's settled then, we're sleep buddies again! Woohoo!"
                        $ livingwithmoxie = 1
                        $ livingwithbutters = 0
                        jump eveningmoxie2menu
                    "On second thought...":
                        jump eveningmoxie2menu
    label moxiesexoptions:
        menu:
            "She starts giving me a handjob as she stares into my eyes lovingly, lustfully and expectantly."
            "Blowjob":
                jump moxieblowjob
            "Sixty-Nine":
                jump moxiesixtynine
            "Doggystyle":
                jump moxiedoggystyle
            "Cowgirl" if moxiecowgirl == 1:
                jump moxiecowgirl
            "Anal" if moxieanal == 1:
                jump moxieanal
            "Missionary" if fr == 1:
                jump moxiemissionary
            "Back":
                if fr == 1:
                    show moxie closewshocked with dissolve
                else:
                    show moxie closeshocked with dissolve
                moxie "Changed your mind already?"
                if fr == 1:
                    show moxie closewalthappy with dissolve
                else:
                    show moxie althappy with dissolve
                jump eveningmoxie2
        label moxieblowjob:
            if fr == 1:
                show moxie closewshy with dissolve
            else:
                show moxie closeshy with dissolve
            stop music fadeout 3.0
            stop ambience fadeout 5.0
            moxie "Mmm, is that what you want? I guess it beats rubbing off alone."
            mc "You can always rub while you suck, in fact you should, it makes it hotter."
            if fr == 1:
                show moxie closewlaughing with dissolve
            else:
                show moxie closelaughing with dissolve
            moxie "Yeah yeah, you're lucky I like sucking your cock anyway, let me at it."
            play music sex1 fadein 3.0
            if fr == 1:
                show moxieb blowjobw
            else:
                show moxieb blowjob
            hide moxie
            show moxie blowjob1
            with dissolve
            play ambience blowjob fadein 3.0
            "I lay back and get comfortable as Moxie kneels between my legs, starting to jack off my cock to get it hard before she begins licking the tip."
            show moxie blowjob2 with dissolve
            moxie "Something about this really turns me on."
            "She starts to masturbate as she sucks on the sensitive tip of my dick."
            show moxie blowjob1 with dissolve
            moxie "Mmph, rubbing feels better while I do this."
            mc "I love the way your tongue feels, keep going."
            show moxie blowjob3 with dissolve
            moxie "Mmphh, yesh *Slurp*"
            "Her tongue swirls around the head and her hand begins to jerk up and down, she definitely has a great technique."
            show moxie blowjob1 with dissolve
            moxie "So hot… Mmmphh *Lick*"
            "She starts to rub herself faster and it won't take much to get her off when she’s this aroused."
            show moxie blowjob3 with dissolve
            "She lowers her head up and down against my cock in short unfocused motions."
            show moxie blowjob1 with dissolve
            moxie "*Slurp* Ahh, gosh…"
            show moxie blowjob3 with dissolve
            mc "Just like that, keep going!"
            moxie "Ahh… I’m nearly… *Slurp* Mmpph."
            "I can see her visibly tense up as she appears to climax, her expression is one of bliss as she lazily wiggles her tongue on my erection, enjoying the moment to the fullest."
            show moxie blowjob1 with dissolve
            moxie "Mmm, okay, your turn, then it’s my turn again! Okay?"
            show moxie blowjob2 with dissolve
            mc "Sure thing, I’m pretty close anyway, your tongue works wonders."
            show moxie blowjob1 with dissolve
            moxie "Wonders you say? How about this?"
            show moxie blowjob3 with dissolve
            "She brings her tongue to the base of my cock and slides it all the way to the tip of my glans multiple times, my cock throbs and my toes wiggle as waves of pleasure surge throughout my entire body."

            moxie "Mmmphh, I love your cock… *Pant, pant*"
            "Once again Moxie takes my entire cock deep into her mouth, wrapping her lips around the shaft and beginning to suck it."
            "She almost gags at the peak of her motions, yet she powers on. Lewd wet sounds keep coming from her mouth, only serving to turn me on even more."

            "I start to stroke her hair as she bobs up and down against my shaft, the sensations are becoming overwhelming."
            moxie "Mmphh… *Slurp* C-Cum!"

            moxie "Cum for me [playername], cum for me! *Lick, slurp*"
            show moxie blowjob4 with cum
            play sound cum
            show moxie blowjob4 with cum
            play sound cum
            "The second she ordered me I couldn’t hold back anymore, I began to orgasm, pouring my load into Moxie’s awaiting mouth as she graciously takes every drop."
            show moxie blowjob4 with cum
            play sound cum
            show moxie blowjob4 with cum
            play sound cum
            "Despite all the sex I’ve been having recently, the orgasm is still so powerful that Moxie struggles to take it all, dribbling some of it down the sides of her mouth and down my dick."
            show moxie blowjob5 with dissolve
            moxie "Ahh, woah… I-I'm gonna come again… Mmph.."
            show moxie blowjob4 with dissolve
            "After swallowing the cum in her mouth, she starts to clean me up using her tongue, all whilst hungrily rubbing at her clit like her life depended on it."
            moxie "Ahh… *Pant*, *Lick*, I’m… Gonna…"
            stop ambience
            show moxie blowjob5 with dissolve
            moxie "Tell me you want me to come, tell me, tell me!"
            mc "Come for me Moxie!"
            moxie "Aahhhhh! Yesss, I'm such a dirty mare! Ahhh, ahh..."
            hide moxieb
            hide moxie
            with dissolve
            "She quickly moves away from my now limp dick, spreads her legs wide and finishes herself off like a champ, it’s quite the sight."
            "She lays down for moment, regaining her breath, before she scurries back up to my side to cuddle."
            if fr == 1:
                show moxie closewlaughing with dissolve
            else:
                show moxie closelaughing with dissolve
            moxie "Hope you enjoyed yourself [playername], you can receive one of Moxie's amazing blowjobs whenever you want, forever!"
            mc "That's a great deal."
            if fr == 1:
                show moxie closewhorny with dissolve
            else:
                show moxie closehorny with dissolve
            moxie "Only the best for you, cutie."
            mc "Let's head to bed?"
            moxie "Sure thing, I'm exhausted."
            stop music fadeout 3.0
            scene bg black with dissolve
            "…"
            if livingwithmoxie == 0:
                scene bg black with dissolve
                show  bg moxiebedday with dissolve
                "In the morning I kiss Moxie goodbye and return home."
                show bg moxiewagonday with dissolve
                scene bg black with dissolve
                "..."
                jump altmorning
            else:
                jump morning
        label moxiesixtynine:
            stop music fadeout 3.0
            stop ambience fadeout 10.0
            if fr == 1:
                show moxie closewlaughing with dissolve
            else:
                show moxie closelaughing with dissolve
            moxie "Ooh, a 69? I love it when you lick me out, and I love your cock deep in my throat, sounds perfect."
            mc "And I love your pussy in my face, come over here and cushion me between your thighs."
            if fr == 1:
                show moxie closewsmug with dissolve
            else:
                show moxie closesmug with dissolve
            play music sex1 fadein 3.0
            if fr == 1:
                show moxieb sixtyninew
            else:
                show moxieb sixtynine
            hide moxie
            show moxie sixtynine1
            with dissolve
            "Moxie does just that, she begins by sitting on my face. I stick my tongue out and start daintily licking her pussy."
            "I can’t see much, but I can imagine she’s staring at my cock right now, watching it slowly grow as blood flows to my nether."
            moxie "Watching it grow is fun, it’s so weird."
            "She clearly couldn’t hold back much longer as she leans over and begins inspecting my cock."
            moxie "Ooh, it’s twitching…"
            mc "That means it wants you to lick it."
            moxie "It has a mind of its own? That explains a lot, ehehe."
            play ambience blowjob fadein 5.0
            show moxie sixtynine1 with dissolve
            "She giggles mischievously before she sticks her tongue out and begins to lick the tip."
            moxie "*Lick* I like the way it reacts when I toy around with it."
            show moxie sixtynine2 with dissolve
            "I lick her clit causing her to squirm in response to the pleasure."
            mc "I like the way you react when I toy around with you."
            moxie "I’d usually have a witty comeback, but this time I just want you to keep licking, because damn that feels good."
            show moxie sixtynine3 with dissolve
            "She lustfully mushes her rear into my face as I eagerly lap at her clit"
            "Simultaneously I could feel the tip of her tongue trailing around my glans, covering my dick in a wet sheen before she eventually took the entire head in her mouth."
            "With every couple of licks to her clit, she’d muffle a cute moan into the blowjob."
            show moxie sixtynine2 with dissolve
            moxie "Mmmphh… *Suck*… Ahh… *Lick*… *Slurp*!"
            show moxie sixtynine3 with dissolve
            "I could tell that she kept losing her concentration to the pleasure of the cunnilingus, before refocusing it back on my cock."
            "Eventually she started to thoroughly fuck my cock with her lips, creating sloppy noises as she drools all over my shaft."
            show moxie sixtynine2 with dissolve
            moxie "Mmphh… *Suck*… *Slurp*… This is… *Suck*… Too good…"
            show moxie sixtynine3 with dissolve
            "I think she's close to coming as her body reacts more vibrantly to my tongue, her back arches and her stifled moans slip out with increasing frequency."
            "Yet she still remained focused on my dick, the way she lustfully moved her head up and down, lashing her tongue around my tip prompted my urge to cum."
            "I held myself back from cumming before her, I kept focusing on her clit and the closer she got to climaxing, the more she’d wriggle around in cute ways"
            "It's almost like we were both holding back to let the other cum first."
            show moxie sixtynine2 with dissolve
            moxie "*Suck*, *Suck*… Mmmphh… I-I’m close… [playername]…"
            show moxie sixtynine3 with dissolve
            "She frantically bobbed her head up and down against my dick, creating lewd noises as she stroked my shaft with her lips and tongue."
            "If she keeps going this fast, she’ll bring me to my limits and make me cum, fortunately it seems she’s about to orgasm any second too."
            moxie "*Slurp*, *Suck* Ahh… Hahhh! Cum with me!"
            show moxie sixtynine4 with cum
            play sound cum
            show moxie sixtynine4 with cum
            play sound cum
            "I can’t hold back, a torrent of cum shoots into her mouth and she seems to climax as well, she grinds on my face as her pussy contracts."
            show moxie sixtynine4 with cum
            play sound cum
            show moxie sixtynine4 with cum
            play sound cum
            moxie "Mmphh… Gehh… *Gulp*, *Gulp*… Ahh!"
            show moxie sixtynine4 with dissolve
            "Moxie gulped down the semen, choking on it slightly and having some of it seep out from the side of her lips. Fortunately, Moxie isn’t a squirter so it’s much easier to handle her orgasm."
            show moxie sixtynine5 with dissolve
            "As my orgasm dissipates and I finally stop cumming. Moxie’s orgasm keeps going for almost twice the duration."
            "She trembles and moans on top of me, all the while I continue to service her with the wet tip of my tongue."
            stop ambience
            moxie "Ah… So good, so good! Mm…"
            hide moxieb
            if fr == 1:
                show moxie closewsatisfied
            else:
                show moxie closesatisfied
            with dissolve
            "Inevitably she settles down and shuffles back off me, snuggling up at my side."
            moxie "Phew… I wish we could go again; I love that one."
            mc "Technically you could just sit on my face, if you wanted."
            if fr == 1:
                show moxie closewsmug with dissolve
            else:
                show moxie closesmug with dissolve
            moxie "Yeah, I could, but it’s not really the same without your cock stuffed in my mouth."
            if fr == 1:
                show moxie closewhorny with dissolve
            else:
                show moxie closehorny with dissolve
            moxie "Surprisingly, one orgasm is enough to satisfy my heat for the night anyway, you’re pretty good with your tongue."
            mc "You too, you’re almost too good. I have to hold myself back so I don’t cum too soon."
            if fr == 1:
                show moxie closewlaughing with dissolve
            else:
                show moxie closelaughing with dissolve
            moxie "Of course! The great Moxie has been researching the best techniques to pleasure a man."
            mc "Really, you did that for me? That’s kinda cute."
            if fr == 1:
                show moxie closewshy with dissolve
            else:
                show moxie closeshy with dissolve
            moxie "Hmph, is not…"
            scene bg black with dissolve
            stop music fadeout 3.0
            "…"
            if livingwithmoxie == 0:
                scene bg black with dissolve
                show  bg moxiebedday with dissolve
                "In the morning I kiss Moxie goodbye and return home."
                show bg moxiewagonday with dissolve
                scene bg black with dissolve
                "..."
                jump altmorning
            else:
                jump morning
        label moxiedoggystyle:
            stop music fadeout 3.0
            moxie "Ooohh… Okay, I can’t argue with that."
            if fr == 1:
                show moxie wdoggystyle1 with dissolve
            else:
                show moxie butt with dissolve
            "She gets on all fours and wiggles her butt enthusiastically as she often does, her pussy is already in an aroused state and has a wet sheen on its folds."
            if fr == 1:
                show moxie wdoggystyle1 with dissolve
            else:
                show moxie buttclitrubmoan with dissolve
            play music sex1 fadein 3.0
            "On my knees, I shuffle closer and start to rub her pussy: spreading her lips, teasing her clit, all the motions that’ll get her ready to  take my cock."
            mc "As usual, you’re dripping wet."
            moxie "Y-yeah… That’s what being around a handsome man like you does to me…"
            moxie "You’re kinda mean continuing to tease me like this."
            mc "Oh, am I mean? I just wanted to make sure you're wet enough to handle this..."
            if fr == 1:
                show moxie wdoggystyle2 with dissolve
            else:
                show moxie doggystyle2 with dissolve
            "I bring the tip of my dick towards her pussy, but instead of entering deeper I glide my tip up and down the length of her vulva."
            moxie "Mmphh… Come on... Teasing me like that is evil! I want it inside me…"
            if fr == 1:
                show moxie wdoggystyle3 with dissolve
            else:
                show moxie doggystyle3 with dissolve
            "As I slowly glided in Moxie let off a cute moan, her insides were soaking wet allowing me to slide all the way in."
            play sound cum
            if fr == 1:
                show moxie wdoggystyle4 with dissolve
            else:
                show moxie doggystyle4 with dissolve
            "I took my time to penetrate her, slowly pushing inwards until her entrance was tightly wrapped around the base of my cock."
            "Once at the hilt, Moxie lets out a soft sigh that's reminiscent of pure bliss."
            moxie "Finally… Ahh… Your dick feels so good…"
            play ambience sex fadein 2.0
            "I begin thrusting, back and forth, slowly sliding my cock almost all the way out, before allowing it to sink back all the way."
            "Her breasts jiggled, and her soft butt slapped against me with each hard thrust."
            if fr == 1:
                show moxie wdoggystyle5 with dissolve
            else:
                show moxie doggystyle5 with dissolve
            moxie "Ahh… *Pant* It feels so hot… Mmm… I could lose my mind to this feeling."
            "I love the way her usual cool demeanour is completely replaced with primal urges and horny ramblings at these times."

            "It's like she's no longer acting as Moxie a person, but just her inner urge to breed."

            "Her body always reacts so vividly to my every action, the pleasure she must feel is beyond imagination."

            "I want to make her feel even better, so I begin to thrust faster."

            moxie "Oh gosh, [playername]… That’s so good, ahhh… It’s so deep… Aaaahhhnn…"

            "Her moans echo throughout the wooden walls of the wagon while lewd wet noises escape from the sex."

            "I kept going, thrusting deep inside her and soon I could feel her vagina tremble and tighten around my throbbing shaft, she must be close, I just have to keep going."

            moxie "Ahhh… It’s good, I’m gonna… I’m gonna… Ahhhhhh, I’m gonna go crazy! Ahaaaaaaaa…"

            moxie "I can’t take it any longer, ahh… I’m gonna come! Ahhhh!"

            "As she climaxes, I can see her tightly grip the sheets, and feel her insides vigorously contract around my penis in an effort to make me cum."

            "I roughly thrust into Moxie’s pussy as she writhed in pleasure below me, getting closer and closer to climax with each push."

            "I can't hold back much longer, and Moxie’s moaning is only driving me further to my limits."

            moxie "Cum for me! I want you… *Pant* to fill my pussy up with your cum… Ahhh!"
            if fr == 1:
                play sound cum
                show moxie wdoggystyle6 with cum
                play sound cum
                show moxie wdoggystyle6 with cum
            else:
                play sound cum
                show moxie doggystyle6 with cum
                play sound cum
                show moxie doggystyle6 with cum
            "My throbbing cock soon exploded deep into her as I orgasmed, her vagina tightly gripped around my shaft, wringing even more cum out of it as we continued to fuck during our climaxes."
            if fr == 1:
                play sound cum
                show moxie wdoggystyle6 with cum
                play sound cum
                show moxie wdoggystyle6 with cum
            else:
                play sound cum
                show moxie doggystyle6 with cum
                play sound cum
                show moxie doggystyle6 with cum
            moxie "Ahhh… I can feel it, oh gosh, there’s so much, it’s so hot… Ahhhhh…"
            if fr == 1:
                pass
            else:
                show moxie doggystyle7 with dissolve
            stop ambience fadeout 3.0
            "I keep thrusting my hips with each load of cum that seeps deep into her vagina and womb, the entire time Moxie moans and rambles incoherently in ecstasy."
            if fr == 1:
                show moxie wdoggystyle8 with dissolve
            else:
                show moxie doggystyle8 with dissolve
            "As my orgasm peaks and fades, I pull myself out of Moxie’s pussy, some of my cum dripping out as I do"
            hide moxie with dissolve
            moxie "Oohh… Ahh *Pant* Wish… Wish I knew the spell so we could go another round straight away…"
            "Even though she says that, she does sink from her all fours position to one of laying on her belly, seemingly exhausted in a melodramatic manner, even though she didn’t actually move."
            if fr == 1:
                show moxie closewsatisfied with dissolve
            else:
                show moxie closesatisfied with dissolve
            "I join her side and she soon embraces me tightly with a goofy grin stuck on her lips."
            mc "Honestly, with how good that felt, I wish I could, I’ll probably have to wait at least ten minutes though."
            if fr == 1:
                show moxie closewshy with dissolve
            else:
                show moxie closeshy with dissolve
            moxie "Mm… I’m gonna be asleep by then, you meanie…"
            mc "How could I be mean? It sounds like you certainly enjoyed yourself."
            if fr == 1:
                show moxie closewsatisfied with dissolve
            else:
                show moxie closesatisfied with dissolve
            moxie "Ohh yes… That one really hit the spot and put my heat back in its place. I’ll be full of energy come tomorrow morning, and by the evening, I’ll be ready for another."
            mc "Sounds about right."
            mc "If we ever both get the chance to have a day off, lets just spend it cuddlefucking."
            if fr == 1:
                show moxie closewalthappy with dissolve
            else:
                show moxie closealthappy with dissolve
            moxie "You’ve got a deal [playername]."
            scene bg black with dissolve
            stop music fadeout 3.0
            "…"
            if livingwithmoxie == 0:
                scene bg black with dissolve
                show  bg moxiebedday with dissolve
                "In the morning I kiss Moxie goodbye and return home."
                show bg moxiewagonday with dissolve
                scene bg black with dissolve
                "..."
                jump altmorning
            else:
                jump morning
        label moxiecowgirl:
            stop music fadeout 3.0
            if fr == 1:
                show moxie closewsmug with dissolve
            else:
                show moxie closesmug with dissolve
            moxie "Ohoho, you're putting me in charge?"
            if fr == 0:
                moxie "Ehehe, let me show you what a mare in heat can do."
                "I'm sure she'd be mad if I told her I've already seen what a mare in heat can do many times."
            play music sex1 fadein 3.0
            show bg moxiebednight with dissolve
            if fr == 1:
                show moxie wcowgirl1 with dissolve
            else:
                show moxie cowgirl1 with dissolve
            "The two of us climb into bed, then she playfully rolls me on my back before mounting me. She wastes no time sinking her puffy mare pussy over my endowment."
            "Moxie's pussy is so pleasant and warm, her insides are stretched perfectly around my cock, yet still squeezing around me like a pleasurable vice."
            moxie "You see how wet I am?"
            moxie "This is because I've been thinking about your cock all day."
            moxie "Now, just sit back and leave everything to me, hehe."
            if fr == 1:
                show moxie wcowgirl2 with dissolve
            else:
                show moxie cowgirl2 with dissolve
            play ambience sex fadein 2.0
            "I'm fairly sure her pussy grips even tighter as she begins to gyrate her hips atop of me."
            "As usual when I offer her sex, she seems consumed with a wholesome lust as she giggles, pants and drools."
            "Now that she's on top; she can take every opportunity to spend that accumulated lust on me."
            moxie "Mmphh yeah, such a good cock!"
            "She squeals in pleasure and happiness as she bounces on my rod, each moan of hers accompanied by the wet splatter of our coupling."
            "I savour every motion as her pussy squeezes and her hips wriggle, her inner walls suck around my cock and stroke against my pleasure points in an irresistible manner."
            moxie "Moreee, more! Ahh, I'm going to come! *Pant*"
            "With each passing second the lust in Moxie's eyes grow, and she holds no resistance when she feels my hips begin to thrust to match  her own."
            "Both our thrusting hips cause my cock to push even deeper inside of her, each thrust going from my glans to the hilt of my cock."
            if fr == 1:
                show moxie wcowgirl3 with dissolve
            else:
                show moxie cowgirl3  with dissolve
            moxie "There it is, I'm coming, I'm coming!"
            "Her eyes roll back and her body rattles with overwhelming pleasure as she experiences a full-body orgasm."
            "Her already tight pussy constricts further with rhythmic convulsions which squeeze and suckle in an attempt to milk my throbbing member."
            "This combined with her frantic fucking brings me closer, and soon I'm unable to hold back."
            moxie "Cum inside me [playername], fill me up!"
            if fr == 1:
                show moxie wcowgirl4 with cum
                play sound cum
                show moxie wcowgirl4 with cum
                play sound cum
            else:
                show moxie cowgirl4 with cum
                play sound cum
                show moxie cowgirl4 with cum
                play sound cum
            "My cock gushes its thick cum deep into her hungry womb."
            if fr == 1:
                show moxie wcowgirl4 with cum
                play sound cum
                show moxie wcowgirl4 with cum
                play sound cum
            else:
                play sound cum
                show moxie cowgirl4 with cum
                play sound cum
                show moxie cowgirl4 with cum
            "All whilst a euphoric Moxie continues her climactic riding, seeming to have yet another orgasm immediately after the first."
            moxie "Fuck yes, ahhhh, aaaahhhh!"
            if fr == 1:
                show moxie wcowgirl5 with dissolve
            else:
                show moxie cowgirl5 with dissolve
            stop ambience fadeout 5.0
            "The two of us make the most of our explosive orgasms before we begin to slow down."
            if fr == 1:
                show moxie closewlaughing with dissolve
            else:
                show moxie closelaughing with dissolve
            "Moxie slumps on top of me and embraces my chest, all whilst my softening cock is still inside her."
            if fr == 1:
                show moxie closewalthappy with dissolve
            else:
                show moxie closealthappy with dissolve
            "I reciprocate her post-coital cuddle and kiss her on the forehead causing her to giggle."
            moxie "That was shoooo good..."
            mc "You really know how to ride, we have to do this more often."
            if fr == 1:
                show moxie closewbashful with dissolve
            else:
                show moxie closebashful with dissolve
            moxie "Ehehe, I love pleasuring you, you always have the cutest reactions."
            if fr == 1:
                show moxie closewlaughing with dissolve
            else:
                show moxie closelaughing with dissolve
            moxie "And those cute reactions make me come even harder,   haha."
            if fr == 1:
                show moxie wcowgirl5 with dissolve
            else:
                show moxie cowgirl5 with dissolve
            "To my surprise, she lifts herself back up."
            moxie "I think it's time for round two, [playername]. If I go slowly at first, it won't be too sensitive, right?"
            mc "Uhh! I guess? Go easy on me!"
            "I knew her libido was extreme, but another round so soon? She must have really enjoyed herself."
            "I could already feel my cock stiffening up again, even though I had just orgasmed a few minutes prior."
            moxie "Ohh, I can feel it grow inside me..."
            "She smirks and begins to very gently ride me again, gauging my reactions with each movement to ensure she doesn't overwhelm me."
            mc "I think you can go faster, I'm surprisingly not that sensitive right now."
            moxie "Hehehe! My pussy is just that good..."
            moxie "I'm not stopping until I'm completely satisfied tonight, so lay back and relax, I'll make this next orgasm even better."
            scene bg black with dissolve
            stop music fadeout 3.0
            "Several orgasms and an hour later, the two of us end up cuddled together sleeping."
            "…"
            if livingwithmoxie == 0:
                scene bg black with dissolve
                show  bg moxiebedday with dissolve
                "In the morning I kiss Moxie goodbye and return home."
                show bg moxiewagonday with dissolve
                scene bg black with dissolve
                "..."
                jump altmorning
            else:
                jump morning
        label moxieanal:
            play music sex1 fadein 3.0
            moxie "How about we try something different?"
            mc "What's that?"
            if fr == 1:
                show moxie wanal1 with dissolve
            else:
                show moxie anal1 with dissolve
            "She grins fiendishly as she leans over and exposes her rear to me."
            "Seductively she lifts her tail in the air, revealing her pussy, which sparkles with lustful desire."
            moxie "How about you try my ass?"
            mc "You sure?"
            moxie "Heh, don't be shy babe. I've experimented with sex toys before, I can take it."
            if fr == 1:
                show moxie wanal2 with dissolve
            else:
                show moxie anal2 with dissolve
            "I stroke my cock, getting it to full hardness as I bring myself into position behind Moxie, she eagerly rubs her clit in anticipation."
            moxie "Go on... Fuck my ass!"
            if fr == 1:
                show moxie wanal3 with dissolve
            else:
                show moxie anal3 with dissolve
            "Spurred on, I line up my cock and press it against her tight pucker, slowly but surely it spreads and I sink inwards."
            "Her sphincter tightly grips against my shaft, it's tight like a velvet vice."
            "As I gently push forward, she grunts and moans until my entire length has finally buried inside of her ass."
            if fr == 1:
                show moxie wanal4 with dissolve
            else:
                show moxie anal4 with dissolve
            moxie "Oohhh, yes! It feels so weird, yet amazing! Gimme a second to relax and you can fuck me."
            "As Moxie's anus slowly adjusts to my girth, she fervently rubs her clit and enjoys the feeling of being filled."
            "When she's ready, I pull back until just my cock's head is left buried inside her, and then with one thrust I push my cock back inside her ass."
            if fr == 1:
                show moxie wanal5 with dissolve
            else:
                show moxie anal5 with dissolve
            "She squeals with pleasure and her pucker constricts tightly. She not only takes it like a champ, but clearly enjoys the feeling!"
            if fr == 1:
                show moxie wanal4 with dissolve
            else:
                show moxie anal4 with dissolve
            moxie "Harder, come on stud!"
            play ambience sex fadein 3.0
            "I pull out, and thrust, then again. I pound away at her asshole for a minute with her ass clamping down on my cock throughout."
            if fr == 1:
                show moxie wanal5 with dissolve
            else:
                show moxie anal5 with dissolve
            moxie "Ohhh, fuck my ass [playername]! This is so good! Ahhh..."
            moxie "I-I think I'm going to cum! Oh my gosh!"
            "We both get closer to orgasm from the intense rutting. Perhaps even faster than regular sex due to the pure lewdity of the situation."
            "Her pussy contracts as she climaxes, her anus getting even tighter in the process, and bringing my inevitable orgasm ever closer."
            moxie "F-Fuck me! Ahhh, aaahh!"
            "Her sanguine moans cause the crashing waves of orgasmic pleasure to reach their heights, threatening to push me over the edge almost immediately."
            if fr == 1:
                play sound cum
                show moxie wanal6 with cum
                play sound cum
                show moxie wanal6 with cum
            else:
                play sound cum
                show moxie anal6 with cum
                play sound cum
                show moxie anal6 with cum
            "I manage to last a few more seconds of pounding before my cock begins to erupt and leak thick ropes of cum deep into her ass."
            if fr == 1:
                play sound cum
                show moxie wanal6 with cum
                play sound cum
                show moxie wanal6 with cum
            else:
                play sound cum
                show moxie anal6 with cum
                play sound cum
                show moxie anal6 with cum
            "*Splurt*, *splurt*!"
            moxie "Aahh, ahhh! Fuck yeah!"
            stop ambience fadeout 1.0
            if fr == 1:
                show moxie wanal7 with dissolve
            else:
                show moxie anal7 with dissolve
            moxie "W-Wow... That was good..."
            if fr == 1:
                show moxie wanal8 with dissolve
            else:
                show moxie anal8 with dissolve
            "I pull my cock out with a pop and some semen oozes and dripples from our point of contact."
            moxie "*Pant*, *pant*... We gotta do that more often!"
            if fr == 1:
                show moxie closewsatisfied with dissolve
            else:
                show moxie closesatisfied with dissolve
            "She falls back onto the sofa with her arms wide, and I lay into her embrace and kiss her."
            "We enjoy each other's warm snuggles until we decide to go to bed."
            scene bg black with dissolve
            "..."
            if livingwithmoxie == 0:
                scene bg black with dissolve
                show  bg moxiebedday with dissolve
                "In the morning I kiss Moxie goodbye and return home."
                show bg moxiewagonday with dissolve
                scene bg black with dissolve
                "..."
                jump altmorning
            else:
                jump morning
        label moxiemissionary:
            scene bg black with dissolve
            "The two of us go to the bedroom for funky times."
            play music sex1 fadein 3.0
            show moxie missionary1 with dissolve
            "Moxie falls back onto the bed and spreads her legs."
            moxie "This position is kinda tame, but I really like watching you while we fuck."
            mc "Awh, that's kinda embarrassing, but I'm doing the same thing."
            moxie "Eep, I hope I pull cute faces."
            "As I get into position, her tail rises up, obscuring her pussy."
            "With a light giggle her tail then playfully swipes at me, bristles of her hair softly rubbing over my tense shaft."
            "I get a nice long view at her soaked sex, her cute clit twitching while I align my cock with her moist cunt."
            show moxie missionary2 with dissolve
            "I press my girthy cock against her entrance and it sinks into the warmth and wetness. It’s immensely pleasurable around my throbbing member, as her insides squeeze and suck my cock."
            play ambience sex fadein 3.0
            "I start to hump her perfect, dripping pussy. Schlicking and sliding back and forth with ease as the cum froths, bubbles and mixes with her juices."
            "Her pussy feels even hotter and wetter than usual, occasional contractions deep inside intensify the pleasure."
            moxie "Ahhhaha, it's crazy how this feels as good as the first time! No, even better!"
            "Moxie moans and squirms as her body racks with pleasure."
            moxie "Oooofft, keep going like that, you're gonna make me come!"
            "Her body ignores her concern as her hips continually wriggle and push into me as a means to maximise the pleasure she receives."
            "With both of our bodies dancing in tune, Moxie's pussy tightens as she begins to orgasm."
            "She lustfully moans throughout, high-pitched squeaks of enjoyment and pleasure constantly spilling from her lips."
            "She writhes and pants, her pristine blue fur growing moist with sweat. At this point she can barely form sentences between her moans."
            moxie "Ooohh, I-I’aahmmm, aahhhh, I-ahh! C-Comminiggghh, agaaainn?! Ahhahaahhh!"
            "Yep, she’s completely inarticulate as she loses herself in the ecstasy of her second orgasm."
            "I thrust hard into her clenching pussy, it squeezes and sucks around my cock relentlessly."
            "Squirts of her juices drip and dribble from her thighs with each body-rocking impact."
            moxie "F-Fuck, ahhhhh, ahhh… It’s so good! I want more! Ahhhh, fuck me more!"
            "As I fuck her faster I'm also getting close to orgasm. Sprinting to the finish, I continue pounding her insides with every ounce of strength my body can muster."
            "Her hips rock with just as much vigour as mine, each of us fucking hard, fast and desperate."
            "I can feel my cock twitching, her consistently clenching pussy combined with my thrusts is too much to endure."
            play sound cum
            show moxie missionary3 with cum
            play sound cum
            show moxie missionary3 with cum
            "Cum erupts from my cock, glazing her hot pussy in complete white; her pussy and womb completely stuffed with my semen."
            play sound cum
            show moxie missionary3 with cum
            play sound cum
            show moxie missionary3 with cum
            stop ambience fadeout 3.0
            moxie "Oohhh, ahhh... It feels so hot, heh..."
            show moxie missionary8 with dissolve
            "I enjoy the feeling of her warm insides for a few seconds longer before pulling out, some cum oozing out from the separation."
            stop music fadeout 3.0
            hide moxie with dissolve
            moxie "Phew... Hahh, wanna go again? I got a spell for that now!"
            mc "Hmm..."
            scene bg black with dissolve
            "About an hour, and many orgasms later, we eventually fall asleep."
            if livingwithmoxie == 0:
                scene bg black with dissolve
                show  bg moxiebedday with dissolve
                "In the morning I kiss Moxie goodbye and return home."
                show bg moxiewagonday with dissolve
                scene bg black with dissolve
                "..."
                jump altmorning
            else:
                jump morning

    label moxietalk:
        if boutiquevisit3 == 1 and moxieboutiquetalk == 0:
            $ moxieboutiquetalk = 1
            $ moxietalks = 1
            moxie "So you've slept with both Melody and Ruby."
            if fr == 1:
                show moxie wlaughing with dissolve
            else:
                show moxie laughing with dissolve
            moxie "Gosh, you're such a player! I thought two those would be innocent and cute."
            moxie "Yet somehow inexplicably you've revealed that they're just as bad as someone like me, ahaha."
            if fr == 1:
                show moxie whappy with dissolve
            else:
                show moxie happy with dissolve
            mc "Haha, honestly I think they're worse than you, they're deviants."
            moxie "Deviants? Oh my."
            mc "You know, in a good way."
            moxie "My, my, all this time I thought Ruby was a prude, and she was running a camshow, ohohoh."
            mc "Remember, you can't tell anyone about that!"
            moxie "My lips are sealed 'darling'."
            jump moxietalkmenu
        pass
        if farmvisit3 == 1 and moxiefarmtalk == 0:
            $ moxiefarmtalk = 1
            $ moxietalks = 1
            moxie "And so, [playername] conquered the farm by sleeping with not only Honeycrisp, but her sister and a cow!"
            if fr == 1:
                show moxie wlaughing with dissolve
            else:
                show moxie laughing with dissolve
            moxie "You're such an animal, hehe."
            if fr == 1:
                show moxie wneutralhappy with dissolve
            else:
                show moxie happyneutral with dissolve
            mc "You're gonna make me blush."
            if fr == 1:
                show moxie wlaughing with dissolve
            else:
                show moxie laughing with dissolve
            moxie "When I challenged you to sleep with so many people, I wasn't expecting you to succeed so amazingly."
            mc "Am I making you jealous?"
            if fr == 1:
                show moxie wneutralhappy with dissolve
            else:
                show moxie happyneutral with dissolve
            moxie "Naahhh, haha. I'm not interested in sleeping around, I just think it's hilarious."
            moxie "You ever thought about settling down, or are you gonna go for more mares?"
            mc "Well, you know I'm still young..."
            moxie "Hehe, I like your style."
            jump moxietalkmenu
        pass
        if forestvisit2 == 1 and moxieforesttalk == 0:
            $ moxieforesttalk = 1
            $ moxietalks = 1
            moxie "I still can't believe you got through to Butters."
            if fr == 1:
                show moxie wneutral with dissolve
            else:
                show moxie neutral with dissolve
            moxie "She's always been that one person I've never been able to connect with, other than Lily a little."
            mc "She doesn't seem to like ponies very much, although I think she'll be more open in the future."
            if fr == 1:
                show moxie whappy with dissolve
            else:
                show moxie happyneutral with dissolve
            moxie "Ohh, really? Did you encourage her to come out more?"
            mc "Yeah, you might even see her at the bar."
            if fr == 1:
                show moxie wlaughing with dissolve
            else:
                show moxie laughing with dissolve
            moxie "A few drinks of Honey's cider is enough to get anyone talking."
            if fr == 1:
                show moxie wsmug with dissolve
            else:
                show moxie smug with dissolve
            moxie "I bet she's a total lightweight too."
            mc "I think she might surprise you."
            moxie "It's settled then, we're gonna go to the bar and drink with Butters. I'll make it my goal to befriend her."
            if barvisit2 == 1:
                mc "You looking for another threesome?"
                moxie "Eep, no! I think Prisma and you are enough for me."
            jump moxietalkmenu
        pass
        if libraryvisit3 == 1 and moxielibrarytalk == 0 and fr == 0:
            $ moxielibrarytalk = 1
            $ moxietalks = 1
            moxie "Be honest, did you fuck Lily?"
            mc "Fuck her? Do you really think she's the type that would be interested in that?"
            if fr == 1:
                show moxie wneutral with dissolve
            else:
                show moxie neutral with dissolve
            moxie "Hmm, I'm not sure..."
            moxie "There's a saying though. 'It's always the quiet ones'."
            if fr == 1:
                show moxie wlaughing with dissolve
            else:
                show moxie laughing with dissolve
            moxie "Not to mention she's a lonely bugger, so she's sexually repressed for sure."
            mc "I see what you mean, but she's so shy."
            if fr == 1:
                show moxie whappyneutral with dissolve
            else:
                show moxie happyneutral with dissolve
            moxie "True... Alright, don't tell me if you slept with Lily, I'll leave that one up to my imagination."
            moxie "Of course, I wouldn't mind if you did, I think it'd be hilarious that the person I created went and sexually dominated a girl that hated me."
            moxie "Regardless if you did or not, there's one mare you'll never be able to sleep with, and that's Penelope."
            mc "Ah yeah, she only likes mares, doesn't she?"
            moxie "Yup, sorry [playername], but you don't stand a chance!"
            moxie "I won't hold it against you in our little challenge though, hehe."
            "If only she knew."
            jump moxietalkmenu
        menu moxietalkmenu:
            "How's work going lately?":
                moxie "Really great! I've been feeling super motivated and happy lately."
                mc "Anything to do with me?"
                if fr == 1:
                    show moxie wlaughing with dissolve
                else:
                    show moxie laughing with dissolve
                moxie "Eheh, maybe, you make me happy... I work better when I'm happy."
                mc "I guess you're going to continue performing while you study?"
                if fr == 1:
                    show moxie whappy with dissolve
                else:
                    show moxie happy with dissolve
                moxie "Actually I think I'll stop soon. Studying will be a full-time commitment after all, especially in the later years."
                moxie "I'm saving up as much money as I can right now for food and essentials."
                mc "Sounds like a good plan, I need to get myself one of those."
                if fr == 1:
                    show moxie whappyneutral with dissolve
                else:
                    show moxie happyneutral with dissolve
                moxie "I think you're doing great, keep working and making connections. Eventually good opportunities will arise for you."
            "Could you tell me about the college?":
                mc "I'm not really sure how college works in Arcadia, could you tell me more?"
                moxie "Hmm, you were a college student, weren't you?"
                mc "I was, yeah."
                moxie "I'm hoping it's similar. You choose a topic of study and you study it for a few years. Then you graduate with a qualification that lets you get a great job."
                mc "Ah, that's simple enough, what are you going to study?"
                if fr == 1:
                    show moxie wlaughing with dissolve
                else:
                    show moxie laughing with dissolve
                moxie "I'm gonna study cosmic magic."
                mc "What's that?"
                if fr == 1:
                    show moxie whappyneutral with dissolve
                else:
                    show moxie happyneutral with dissolve
                moxie "Like uhm, how do I explain it..."
                moxie "It's a school of magic that utilises the power of your surroundings to cast magic that is otherwise more powerful than you'd be able to use by yourself."
                moxie "Only problem is that a tiny, tiny amount of the unicorn population can tap into that."
                mc "And you?"
                if fr == 1:
                    show moxie whappy with dissolve
                else:
                    show moxie happy with dissolve
                moxie "Hehe, yup, that's how I do the invisibility spell really well."
                if fr == 1:
                    show moxie whappyneutral with dissolve
                else:
                    show moxie happyneutral with dissolve
                moxie "It's still difficult for me though."
                moxie "Fortunately, that's what study is for! The entry exam doesn't require any actual experience with cosmic magic."
                mc "What other types of magic are there?"
                if fr == 1:
                    show moxie whappy with dissolve
                else:
                    show moxie happy with dissolve
                moxie "Oh plenty, the actual categories are vague because there are so many different overlapping types."
                moxie "At the Arcadian college you can study cosmic magic, mystical magic, alteration magic, and white magic."
                if fr == 1:
                    show moxie wneutral with dissolve
                else:
                    show moxie neutral with dissolve
                moxie "There's also black magic which you can't study, that focuses on using magic to cause pain and destruction, bad!"
                if fr == 1:
                    show moxie whappyneutral with dissolve
                else:
                    show moxie happyneutral with dissolve
                moxie "I bet there are other types too, but alteration is the most common form of magic, as you can imagine the uses for that are quite extreme."
                moxie "Fairly sure most buildings in Arcadia are made using that, apart from the suburbs that is."
                moxie "The suburbs are actually older than the castle because they're remnants of pre-unicorn society."
                mc "This is all incredibly interesting. Could you tell me what Lily and Penelope are studying?"
                moxie "Of course, I think it's awesome to have someone new to talk to about this stuff."
                moxie "Lily is doing a science of magic extended course, that's a special course which is far beyond me."
                moxie "And Penelope is studying mysticism, with some extra modules in alteration."
                "We spend a surprising amount of time talking about magic. I still can't get over how awesome it is to be living in a world where magic is real."
                "I'm really interested to see all the faucets of how a modern society is affected by magic."
            "Can you tell me more about magic?":
                mc "Can you tell me more about magic?"
                moxie "This again? You're obsessed ahah."
                mc "Well, ever since I was young I always wanted to do magic."
                moxie "Yeaahhh, it's pretty cool!"
                label moxiemagictalk:
                    menu:
                        "Tell me about Mysticism.":
                            if fr == 1:
                                show moxie whappyneutral with dissolve
                            else:
                                show moxie happyneutral with dissolve
                            moxie "I think mysticism is just generally a catch-all for fancy magic stuff that doesn't fit into the other categories."
                            moxie "Mysticism is to use magic to manipulate the rules of nature."
                            moxie "It's the ability to reflect spells, raise the undead, telekinesis and even levitation."
                            moxie "It's essentially doing things with magic that are otherwise impossible, and have no real standing in science."
                            moxie "You can also use spells to manipulate your physics, perception or abilities."
                            mc "Kinda like a buff in a video game?"
                            moxie "Yeah, most video game buffs are mystical spells."
                            jump moxiemagictalk
                        "Tell me about Alteration.":
                            if fr == 1:
                                show moxie whappyneutral with dissolve
                            else:
                                show moxie happyneutral with dissolve
                            moxie "This is arguably the most useful school of magic. It can be used to change the fundamental chemistry of objects."
                            moxie "You could use it to say, turn clay into bricks, or sand into glass."
                            moxie "It's useful for food production, health and safety, construction. Just depends on where you specialise I guess."
                            mc "I guess that's the reason fancy architecture is the standard."
                            moxie "Yep, heck, the tree library was made entirely from alteration magic."
                            jump moxiemagictalk
                        "Tell me about White Magic.":
                            moxie "This is an incredibly challenging school of magic that is closely linked to medical courses."
                            moxie "In a nutshell, it's healing magic. But the long of it is that healing is incredibly complicated."
                            moxie "You can't just cast a healing spell on someone and assume everything will be okay, a profound understanding of biology and medicine is required to be effective."
                            mc "Awh, nothing is ever as simple as the games."
                            if fr == 1:
                                show moxie wlaughing with dissolve
                            else:
                                show moxie laughing with dissolve
                            moxie "Afraid not kiddo."
                            jump moxiemagictalk
                        "Tell me about Cosmic Magic.":
                            if fr == 1:
                                show moxie whappyneutral with dissolve
                            else:
                                show moxie happyneutral with dissolve
                            moxie "This is magic like teleportation, invisibility, detecting creatures around you, absorbing spells and creating portals."
                            moxie "Most of these spells require you to utilize external energies, because they're beyond basic magical ability."
                            mc "Why's that?"
                            if fr == 1:
                                show moxie wneutral with dissolve
                            else:
                                show moxie neutral with dissolve
                            moxie "Well, basically... If you're creating a portal for example, you'll need to cast magic to create a portal in front of you. You can do that on your own."
                            moxie "But the only way to get a portal to link to somewhere else, is to use cosmic energy to form that portal on the other side."
                            mc "Sounds... complicated..."
                            if fr == 1:
                                show moxie walthappy with dissolve
                            else:
                                show moxie althappy with dissolve
                            moxie "Yeah, if time travel magic ever becomes a thing, it'll definitely be under this school."
                            mc "Wait, so why is invisiblity cosmic? Surely that's mysticism?"
                            if fr == 1:
                                show moxie wlaughing with dissolve
                            else:
                                show moxie laughing with dissolve
                            moxie "Ahah, so you're paying attention, good!"
                            if fr == 1:
                                show moxie whappy with dissolve
                            else:
                                show moxie happy with dissolve
                            moxie "Invisibility is not what it appears to be. It's not an optical illusion, true invisibility is the act of casting away your physical form and replacing it with an ethereal one."
                            moxie "The physical form has to go somewhere during that time, you know?"
                            mc "Uh, I don't think I know."
                            if fr == 1:
                                show moxie walthappy with dissolve
                            else:
                                show moxie althappy with dissolve
                            moxie "Awh, don't worry about it too much."
                            jump moxiemagictalk
                        "That's all, thank you!":
                            pass
            "Talk about Moxie's past":
                mc "Can you tell me more about your past? I don't know much about where you used to live."
                if fr == 1:
                    show moxie whappyneutral with dissolve
                else:
                    show moxie happyneutral with dissolve
                moxie "Sure thing. I come from a village far to the east. I was travelling and performing all across the country on my way to Arcadia, where I wanted to settle."
                moxie "It was genius in retrospect; I'd perform my shows and live off the road using the money."
                moxie "Performing in new places is always lucrative, even these days sometimes I travel outside of Arcadia to perform. I'll be back in the evenings though, so no need to worry."
                moxie "Before that I was at school, I'm only just nineteen I'll have you know."
                if fr == 1:
                    show moxie wlaughing with dissolve
                else:
                    show moxie laughing with dissolve
                moxie "I lived in Sylvania and grew up with a single mother. There was no father, I was born through magic, so I guess that means I'm a clone of my mom."
                if fr == 1:
                    show moxie whappyneutral with dissolve
                else:
                    show moxie happyneutral with dissolve
                moxie "Life in the village was surprisingly similar to the Arcadian suburbs; I however, was different!"
                if fr == 1:
                    show moxie wsatisfied with dissolve
                else:
                    show moxie satisfied with dissolve
                moxie "Oh sheesh, I was a spoilt child, it brings a tear to my eye."
                if fr == 1:
                    show moxie walthappy with dissolve
                else:
                    show moxie althappy with dissolve
                moxie "Alright, your turn now, I want to know about you."
                mc "Fair enough, we haven't talked about that since the day after I arrived."
                "We spend a while talking about my past life, my friends, family and everyday life."
            "Ask Moxie what she thinks about Arcadia":
                mc "How's life in Arcadia treating you?"
                moxie "I loooove it! I hope you do too."
                if fr == 1:
                    show moxie wsad with dissolve
                else:
                    show moxie sad with dissolve
                moxie "I'm still really sorry about what happened."
                mc "It's fine, I'm over that stuff now. I've come to terms with the fact you somehow cloned me."
                if fr == 1:
                    show moxie wshocked with dissolve
                else:
                    show moxie shocked with dissolve
                moxie "Ehehe... Sorry, sorry!"
                mc "Haha, come on, answer my question from before."
                if fr == 1:
                    show moxie whappyneutral with dissolve
                else:
                    show moxie happyneutral with dissolve
                moxie "Ohh right! I've made tons of friends here, almost all thanks to Penelope."
                moxie "We used to go to the bar together in the evening, and that's where I got very close to Prisma."
                moxie "Being friends with the person that runs the largest bar in the suburbs is handy, because she knows a lot about Arcadia and its people."
                moxie "Before I knew it, I had a gang of friends including all those that you're working for."
                moxie "I hope they're treating you just as kindly as they treated me."
                mc "Definitely, if it wasn't for the kindness of everyone here, I don't think I could have adapted to this new life as easily."
                if fr == 1:
                    show moxie wbashful with dissolve
                else:
                    show moxie bashful with dissolve
                moxie "Phew, thank Aurora for that."
                if fr == 1:
                    show moxie whappyneutral with dissolve
                else:
                    show moxie happyneutral with dissolve
                "We spend some time gossiping, I guess I've picked up that habit from spending so much time around girls."
            "Back":
                jump eveningmoxie2menu
        $ moxietalks = 1
        jump eveningmoxie2menu
