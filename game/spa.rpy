    label mapspa:
        if spavisited == 1:
            "I've already been to the spa today, I'd look pretty weird if I went back-to-back."
            if fr == 1:
                jump finalworldmap
            jump worldmap
        show bg spa with dissolve
        "Here's the spa, time for indulgence."
        if spavisit == 0:
            $ spavisit += 1
            greymare "Ohh, a male customer! What a treat. You're our first all week!"
            whitemare "An interspecies no less, we can get wild with you, big boy."
            if monies < 50:
                mc "Sorry ladies, I can't afford anything, just looking."
            if monies > 50:
                mc "It's quite expensive here."
            whitemare  "For you? We could do a two for one special."
            greymare "Hehe, buy one service, and we'll both do it."
            mc "You ladies have a deal."
        menu spamenu:
            "I have [monies] monies available."
            "Massage with Happy Ending - 50 monies":
                if monies < 50:
                    "I can't afford this treatment."
                    jump spamenu
                "I pay the ladies at the reception and step into a private massage room."
                $ monies -= 50
                $ spatodo += 1
                jump spa1
            "Massage with Blowjob - 75 monies":
                if monies < 75:
                    "I can't afford this treatment."
                    jump spamenu
                "I pay the ladies at the reception and step into a private massage room."
                $ monies -= 75
                $ spatodo += 1
                jump spa2
            "Sex - 100 monies":
                if monies < 100:
                    "I can't afford the sex treatment."
                    jump spamenu
                "I pay the ladies at the reception and step into a private massage room."
                $ monies -= 100
                $ spatodo += 1
                jump spa3
            "Special Customer? (Sex with Tavi) - Free" if musicstudio == 1:
                if spaspecial == 1:
                    "I've already had sex with Tavi today, I probably shouldn't pester her again."
                    "I'm sure she'd be more than happy to take my money for another treatment though."
                    jump spamenu
                "I ask Tavi for the special treatment and she leads me up to her room alone."
                scene bg black with dissolve
                jump spaspecial
            "Nothing":
                if fr == 1:
                    jump finalworldmap
                jump worldmap
    label spa1:
        $ spavisited = 1
        show bg black with dissolve
        play music sex1 fadein 25.0
        "..."
        show spa1 with dissolve
        "I lay on my back and the girls soon join me in the massage room."
        whitemare "Alright, let's get to it."
        "She says as she cracks her knuckles whilst the softer grey mare places a towel over my buttocks."
        greymare  "My, my, this is one aching back, just close your eyes and relax."
        whitemare "Mhm, imagine the sound of waves crashing against the shore."
        "The girls begin by working their hands into my back, pushing hard and resulting in some initial pain."
        "The pain doesn't last long as it is eventually subsided with a sensation of pure relief and relaxation."
        "Even though I'm sure they're pressing even harder than before, I feel immensely satisfied instead of pained."
        "After only ten of the full thirty minutes, I feel so completely, yet pleasantly numb, as if floating on a cloud."
        "This is when the girls start applying a strange soothing massage oil, applying it in circular motions on my back."
        show bg black with dissolve
        hide spa1 with dissolve
        "About half way into my massage I turn over and they begin to work on my front. The sights are far more erotic from this position, leading to an erection, and before I even realize what's happening..."
        play ambience sex fadein 3.0
        show spa11 with dissolve
        "For the happy ending, the two girls have pincered my cock and begun to mush our sexes together in a most erotic sight."
        whitemare "Mmphh, this is good..."
        "They had applied massage oil to my cock thoroughly  before mounting me, so their movements are slick and smooth against my glistening cock."
        greymare "Hehe, this was supposed to be a handjob, how'd this happen?"
        whitemare "The rules state that happy endings are non-penetrative, and I don't see anything penetrative about this."
        greymare "Ohh, true! I did it with my boobs once..."
        "There's a surprisingly snug tightness between the indents of their labia and thighs, the sensation around my cock is like an extremely erotic and wet boob job."
        whitemare "If we keep going like this... I might even come too! Mmm..."
        "The mares buck their hips faster, pressing against my cock with more pressure as they exert themselves."
        "The massage had already peaked my sexual desires and served as sufficient foreplay, so it won't take much longer for me to cum now."
        whitemare "Oh gosh, I'm actually coming, I'm coming..."
        greymare "Ahhh, ahh..."
        "Both mares have already lost themselves to the pure pleasure and lust of my hard cock."
        "The white mare orgasms as her eyes roll back, and the grey mare eagerly grinds faster as her tongue lolls and drools out of her mouth."
        greymare "Ah-Ahm coming too!"
        "As their movements get faster and faster they build up to my release."
        "And soon enough I begin to reach climax."
        show spa11cum with cum
        play sound cum
        show spa11cum with cum
        play sound cum
        "My hips start to grind back and forth, ending in a final thrust that releases my thick cum."
        show spa11cum with cum
        play sound cum
        show spa11cum with cum
        play sound cum
        "All the sexual tension that has been building for almost a full twenty minutes has lead up to this moment. It's like a spectacular fountain of cum, all erupting from my tip."
        "And this thick whiteness covers the ladies."
        "The girls delight in the feeling of my ejaculate, continuing to grind as droplets of my cum cover their thighs and pelvis."
        stop ambience fadeout 3.0
        stop music fadeout 3.0
        "The three of us stay in place for a few moments, catching our breath as the tension dissipates."
        scene bg black with dissolve
        "The two girls clean me up graciously with their tongues before giving me some privacy."
        "My body feels utterly euphoric after both massage and orgasm."
        if fr == 1:
            scene bg pgworldmapday with dissolve
        else:
            scene bg worldmapdaynoui with dissolve
        "And as I leave the spa, the cool air hits my smooth moisturised skin, adding to that great feeling."
        "The massage only took thirty minutes, so it's just after eight in the morning, if I hurry I can still get to work."
        if fr == 1:
            jump prefinalworldmap
        jump preworldmap
    label spa2:
        $ spavisited = 1
        show bg black with dissolve
        play music sex1 fadein 25.0
        "..."
        show spa1 with dissolve
        "I lay on my back and the girls soon join me in the massage room."
        whitemare "Alright, let's get to it."
        "She says as she cracks her knuckles whilst the softer grey mare places a towel over my buttocks."
        greymare  "My, my, this is one aching back, just close your eyes and relax."
        whitemare "Mhm, imagine the sound of waves crashing against the shore."
        "The girls begin by working their hands into my back, pushing hard and resulting in some initial pain."
        "The pain doesn't last long as it is eventually subsided with a sensation of pure relief and relaxation."
        "Even though I'm sure they're pressing even harder than before, I feel immensely satisfied instead of pained."
        "After only ten of the full thirty minutes, I feel so completely, yet pleasantly numb, as if floating on a cloud."
        "This is when the girls start applying a strange soothing massage oil, applying it in circular motions on my back."
        show bg black with dissolve
        hide spa1 with dissolve
        "About half way into my massage I turn over and they begin to work on my front. The sights are far more erotic from this position, leading to an erection, and before I even realize what's happening..."
        play ambience blowjob fadein 3.0
        show spa blowjob1 with dissolve
        "The girls diligently pincer attack my erection, stroking it with their hands and trailing their tongues over different areas."
        "The grey mare expertly focuses on the tip, sending shivers of pleasure throughout my body."
        "The white mare suckles and licks my balls, it's the first time I've ever felt something like this, and it adds so much more to the blowjob."
        "As my cock stiffens and throbs, the girls get bolder. I moan encouragingly as one of the mares takes my cock into her mouth and begins to suck on the head."
        "Both of their tongues continuing to stroke and lick their respective areas, filling me up with double the normal pleasure."
        "The experience of having two mares servicing my cock is difficult to describe, it's almost like receiving two blowjobs at once."
        "The grey mare clearly has the deep throating experience as she  takes my cock inside her mouth, I can feel the tip bumping against the back of her throat."
        "In clean, expert motions she firmly pulls back and forth, her lips tightly wrapped around my shaft in a choke-hold that's designed to bring me to a powerful climax."
        "All whilst the white mare's tongue adds an additional tantalising pleasure which pushes me closer and closer."
        "The stimulus is incredible, I groan as the churning pleasure growing deeper inside my body boils to a climax."
        play sound cum
        show spa blowjob2 with cum
        play sound cum
        show spa blowjob2 with cum
        "Without even a chance to react, my cum splatters into the grey mare's waiting mouth."
        play sound cum
        show spa blowjob2 with cum
        play sound cum
        show spa blowjob2 with cum
        "She gulps every drop down valiantly, and as I finally finish she releases my cock with a wet pop."
        stop ambience fadeout 3.0
        stop music fadeout 3.0
        "The two mares make out amongst themselves with a cum-laden kiss over my cock, before they return to my now sensitive pecker and delicately clean up a few loose droplets of cum."
        greymare "Mmm, what a delicious cock."
        whitemare "I think I have a new favourite customer, he lasts much longer than stallions, hehe."
        greymare "Come on, let's finish massaging his front."
        scene spa1 with dissolve
        "And then seamlessly, with ten minutes remaining, the two masseuse continue to massage my front."
        show bg black with dissolve
        "My body feels utterly euphoric after both massage and orgasm."
        if fr == 1:
            scene bg pgworldmapday with dissolve
        else:
            scene bg worldmapdaynoui with dissolve
        "And as I leave the spa, the cool air hits my smooth moisturised skin and it only adds to that great feeling."
        "It's just past eight in the morning, if I hurry I can still get to work."
        if fr == 1:
            jump prefinalworldmap
        jump preworldmap
    label spa3:
        $ spavisited = 1
        stop ambience fadeout 3.0
        greymare "Well, this should be fun!"
        whitemare "I guess we oughta stick to the whole two-for-one thing we proposed."
        greymare "Hey, I’m up for it, aren’t you?"
        whitemare "S’long as I get to ride him first! Calling dibs!"
        greymare "No fair, there’s only enough time for one round!"
        whitemare "Oh yeah? Ride his face then."
        greymare "Oohh, that’s an idea…"
        mc "Um, girls? Are we gonna do this?"
        whitemare "Oh, uh, yeah! Totally! We were just planning our strategy of attack."
        mc "Attack?"
        greymare "She means, our strategy of making sure you’re as relaxed as possible."
        menu:
            "Sounds like you were planning a strategy to relax yourselves.":
                whitemare "Meh, guess we’ll start with the usual massage."
            "Alright then ladies, show me what you've got.":
                greymare "Let's sooth you with the usual massage first; it'll make you more sensitive."
        show bg sparoom with dissolve
        "The three of us wander to the massage room."
        "Usually they'd allow me some time alone to lay down and get ready, but they're so eager that they followed me straight in."
        "I get on the comfortable massage table and lay on my back"
        show spa1 with dissolve
        play music sex1 fadein 3.0
        whitemare "Alright, let's get to it."
        "She says as she cracks her knuckles whilst the other lover places a towel over my buttocks."
        greymare "My, my, this is one aching back. Just close your eyes and relax."
        whitemare "Mhm, imagine the sound of waves crashing against the shore."
        "The girls begin by working their hands into my back, pushing hard and resulting in some initial pain."
        "The pain doesn't last long however, it's eventually subsided with a sensation of pure relief and relaxation."
        "Even though I'm sure they're pressing even harder than before, I feel immensely satisfied instead of pained."
        "After only ten of the full thirty minutes, I feel so completely, yet pleasantly numb, like dancing on a cloud."
        "This is when the girls start applying a strange soothing massage oil, applying it in circular motions on my back."
        scene bg sparoom with dissolve
        "About half way into my massage I turn over, and they begin to work on my front. The sights are far more erotic from this position, leading to an erection, and before I even realize what's happening..."
        show spa threesome1 with dissolve
        "Fluffy thighs encompass my face and hips. A double straddle!"
        "Before I can even fully comprehend the situation, there’s a dripping wet vulva in my face, and the tip of my cock is prodding against another."
        "… Hot!"
        "The softness of their bodies is extremely enticing. My tongue readily swipes at the grey mare’s clit, while my cock throbs in anticipation of penetration."
        "A soft hand grasps my member and guides me down until she’s poised to sink right in."
        "I gasp as she lowers her supple hips, sliding her wet pussy forward and taking me to the hilt in an instant motion."
        whitemare "Aahhaaah… First of the day is always the best."
        greymare "We’re lucky to even get a man on some days. Ooohh, he’s so good with his tongue too…"
        "My cock is so fucking hard right now, I can feel every millimetre of her lips parted around my cock, squeezing and throbbing."
        whitemare "Lie still, lover boy."
        play ambience sex fadein 3.0
        "She commands lewdly as her hips begin to buck. Her technique is every bit as fantastic as you’d expect a professional sex worker in this type of fantasy world."
        "I can’t help but actively push my hips forward in tandem with her movements, needily trying to thrust deeper into her tantalising wetness."
        "Despite asking me to stay still, she gracefully plays into the rhythm of my thrusts, and turns our rutting into an erotic dance of bucking and riding hips."
        "All whilst my tongue erratically flickers over the grey mare’s cute twitching clit."
        greymare "Mmmmphh yeah, right on my love button, babe..."
        whitemare "Heh, keep talking like that and you'll make me jealous."
        greymare "Oh shush, you. I'm already jealous that you're riding that delicious, fat cock."
        whitemare  "Come here you slut... *Kiss*"
        greymare "Mmphh, mmmm... *Kiss, kiss*"
        "I can’t quite see what the girls are doing with this fat ass on my face, but the lewd wet sounds of a kiss combined with muffled moans only serve to arouse me further as they fully indulge into the act of sex."
        "While I may be a paying customer, these mares are missing no opportunity to fully enjoy the moment, and I love it."
        "The riding mare moans with pleasure as she pounds her ass against me, frantic for more of my cock."
        "The massage has lowered my guard against climax significantly, such as my orgasm hurtles towards finality far faster than I could have anticipated."
        "Although the orgasm of each mare isn’t too far behind me either, as their increasingly energetic moans and grinding show."
        greymare "Ohh, ahhh, yes, yes, keep licking! Just like that! You’re gonna make me-!!"
        whitemare "Ahhhh, I’m gonna come too, come with me! Both of you! Ahhh, ahhh!"
        play sound cum
        show spa threesome2 with cum
        play sound cum
        show spa threesome2 with cum
        "My teeth grit as my cock explodes, blasting the white mare’s pussy excessively with cum."
        play sound cum
        show spa threesome2 with cum
        play sound cum
        show spa threesome2 with cum
        "Riding the hardest so far, she throws her head back, moaning as her vaginal insides clamp down on my shaft and for the briefest of moments causes my vision to go totally white from pleasure."
        "Some light squirting from the mare riding my face refocuses my attention, as everyone fucks out the remainder of their strong orgasms in utter bliss."
        stop ambience
        whitemare "Haahh… You have such an excellent cock. I could go for a second round if I didn’t have other responsibilities, hehe."
        scene bg sparoom with dissolve
        whitemare "Hey, Tavs, you’ve got cleaning covered, right? I’m gonna cuddle with our client, part of the package."
        greymare "Yeah, whatever."
        "Me and the white mare lie together for some time, I wasn’t anticipating her to start making out with me, but I welcome her tongue into my mouth as she lustfully presses her breasts against my chest."
        "All while Tavi cleans the residue of cum and pussy juice from my cock, naturally I find myself getting another erection."
        "And while I’m distracted by the kiss…"
        play ambience blowjob
        greymare "Mmphh, mmm… *Lick, slurp*"
        "… I’m already receiving a blowjob."
        "These crazy horny mares..."
        "Well, I guess we do have about five minutes left..."
        stop ambience fadeout 3.0
        scene bg black with dissolve
        stop music fadeout 3.0
        "..."
        "A little longer than five minutes later..."
        scene bg sparoom with dissolve
        "My body feels utterly euphoric after both massage and orgasm."
        if fr == 1:
            scene bg pgworldmapday with dissolve
        else:
            scene bg worldmapdaynoui with dissolve
        "And as I leave the spa, the cool air hits my smooth moisturised skin and it only adds to that great feeling."
        "It's just past eight in the morning, if I hurry, I can still get to work."
        if fr == 1:
            jump prefinalworldmap
        jump preworldmap
    label spaspecial:
        $ spavisited = 1
        $ spaspecial = 1
        play music sex1 fadeout 3.0
        show bg spabedroom with None
        show tavi ride1 with dissolve
        "Softly laying me down with her delicate touch, she straddles my waist and gives me an immediate view of her incredibly sexy rear."
        greymare "Like what you see? I can massage you with my pussy too, hehe."
        "As usual, Tavi is really horny and eager for some fun. I can't begin to imagine how much pent up frustration she builds throughout the day."
        "After all, it's not her place to focus on her own pleasure in this spa, bless her."
        play sound cum
        show tavi ride2 with dissolve
        "Before I can finish my thought Tavi takes my cock in her soft furry grip, aligns it with her moist pussy and sinks down onto it."
        greymare "Ahhh, ahh... That hits the spot..."
        mc "Ohhh, you're so wet!"
        greymare "Mhhmm, especially when you walked in babe."
        play ambience sex fadein 2.0
        "*Squish, squish*"
        "She raises her hips once more, before slowly bringing her ass down once again. Slowly, like a massage to the cock, she savours each movement."
        "Her insides mold around my cock, squeezing tightly around my shaft as we make love. Her nether lips particularly gripping tightly with each movement upwards."
        greymare "Ahhh, mmmmphh... Feels so good, mmmhh..."
        "Moans of pleasure escape her lips and a warm feeling of relaxation spreads throughout my body due to her sensual movements."
        "She truly is an excellent masseuse, even in this lustful scenario her movements are practiced and designed to maximise pleasure and relaxation."
        "I may not be as sensual and loving as her, but I decide to return some of Tavi's thrusts with my own passion filled ones."
        greymare "Ohh, f-fuck! Ahh, ahhh, aaaahhhh! Y-You're supposed to let me - aaahhh!"
        "The two of us move in unison as the rutting intensifies and her moans grow louder, only further enticing me and my fervent fucking."
        greymare "Ahhh mmmhh, fuck me harder [playername]! Ahhh, ahh!"
        "The grey mare soon begins to orgasm causing her pussy to contract rhythmically around my cock, further enhancing the pleasure."
        "Soon after her own, I feel my climax begin to rapidly rise. I rapidly thrust my cock into her pussy as I push myself over the edge."
        play sound cum
        show tavi ride3 with cum
        play sound cum
        show tavi ride3 with cum
        "My orgasm is soon unleashed as my cock explodes into Tavi, her pussy taking in each and every drop of my thick cum."
        play sound cum
        show tavi ride3 with cum
        play sound cum
        show tavi ride3 with cum
        "Tavi finishes me off not as a sensual masseuse, but as a lustful mare trying to drain my cock of all the pleasure she can."
        greymare "Yesss, yess! Aahhh, ahh! *Squish, squelch!*"
        stop ambience fadeout 2.0
        stop music fadeout 3.0
        "Cum oozes from our point of connection as she comes to a stop."
        greymare "Haahh... Phew... I'm glad I get to go all out with you..."
        hide tavi with dissolve
        show spaowner happy with dissolve
        greymare "Hehehe, I hope you enjoyed this special service, thank you [playername]!"
        greymare "Do come again, but not {i}tooooo{/i} often!"
        if fr == 1:
            jump prefinalworldmap
        jump preworldmap
