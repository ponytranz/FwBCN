label city:
    scene bg arcadiastreets with dissolve
    play ambience ambiencecity fadein 3.0
    play music day2 fadein 3.0
    if cityfirstvisit == 0:
        "Wow, the city is as typical as I would have expected. Crowds of people wandering from finely decorated shop to shop."
        "It's far more commercial and urban than the village-like suburbs."
        $ cityfirstvisit = 1
    label citymenu:
        pass
    call screen cityday
    with dissolve
    menu:
        "Where should I go?"
        "Castle":
            label castlecm:
                pass
            if libraryvisit3 == 0:
                "While in the city, the castle ever looms above."
                "However, the guards won't let me in without a permit."
                if libraryvisit1 == 1:
                    "Maybe I could ask Lily to get me one."
                else:
                    "Who could help me get a permit?"
                jump citymenu
            else:
                if auroravisitsetup == 1 and auroravisit1 == 0:
                    jump auroravisit1
                elif auroratalk == 1:
                    "I probably shouldn't bother Aurora twice in a day"
                    jump citymenu
                else:
                    jump castle
        "Music Studio":
            jump musicstudio
        "Art Gallery":
            jump artgallery
        "Nightclub":
            label nightclubcm:
                pass
            if dawnltr == 2:
                jump dawnvisit4
            elif dawnvisit == 2:
                jump dawnvisit3
            elif dawnvisit <= 1:
                "It's closed. Unfortunately it's not a dayclub."
                jump citymenu
            else:
                if dawnshowersex == 0:
                    $ dawnshowersex = 1
                    jump dawnshowersex
                "Ringing the buzzer behind the nightclub, I get no response."
                "I could probably visit Dawn whenever I want, but she's often away for work."
                "I'd have a better chance to catch her in the evening, she seems to sleep here often."
                jump citymenu
        "Church":
            ##"It's just a church, nothing interesting in there."
            ##jump citymenu
            jump church
        "Back":
            play music day fadein 3.0
            if fr == 1:
                jump prefinalworldmap
            jump preworldmap
    label musicstudio:
        if musicstudio == 0 and farmvisit3 == 1 and boutiquevisit3 == 1 and spavisit == 1:
            show bg arcadiastreetsnoui with d
            $ musicstudio = 1
            blossom "Hey! [playername]!"
            show blossom happy with dissolve:
                xpos 250
                ypos 75
            "I turn around to see Blossom, and also..."
            show melody fufufu with dissolve:
                xpos 750
                ypos 75
            melody "Look at you staring around in awe. Looking for some sleezy mares?"
            mc "Why, you offering?"
            show melody happy with dissolve
            melody "Hah! ... Shit... That was a good line..."
            mc "You two off to college?"
            show melody sadistic with dissolve
            melody "Yeah, but we've got time, wanna hang out?"
            show blossom shocked with dissolve
            blossom "Huh? We have time? Well... I like the idea anyway..."
            mc "Sure, I can hang, as long as I'm not keeping you two."
            show melody happy with dissolve
            melody "Pfft it's only 8:00am, Blossom and I were just about to get a coffee and laze around for an hour anyway."
            show blossom neutral with dissolve
            blossom "I thought we were goin-"
            show melody fufufu with dissolve:
                xpos 505
                ypos 75
            melody "Shh... Let's show this lost soul around."
            scene bg black with dissolve
            "Ten minutes later..."
            scene bg arcadiastreetsnoui with dissolve
            show melody happy with dissolve:
                xpos 750
                ypos 75
            melody "And this is my hairdressers, this is how I manage to look so perfect."
            show blossom neutral with dissolve:
                xpos 250
                ypos 75
            blossom "I don't see why you can't just cut your own hair."
            show melody sadistic with dissolve:
            melody "Please Blossom, I have some standards!"
            show melody happy with dissolve:
            melody "Oh, that's my favourite nightclub over there, Bed of Chaos."
            show blossom happy with dissolve
            blossom "I like that one too because it's free entry for students."
            blossom "I heard our sisters go there quite often."
            show melody happy with dissolve:
            melody "Ahh yeah! Every good night starts in the Bed, the drinks are cheap too."
            melody "It's also close to a brothel, did you notice that Blossom? I bet that gets some good evening business."
            show blossom shocked with dissolve
            blossom "Uhm, I know of it... I heard there are gloryholes in there."
            if augustavisit > 0:
                "Are they talking about the church?"
            show melody neutral with dissolve:
            melody "Why would a mare pay to suck off a stranger? If you're going to spend money you might as well get a good dicking."
            mc "Another brothel huh? I didn't realize it was so commonplace."
            show melody fufufu with dissolve:
            melody "Ahah you prude! Our society is far more casual than whatever backwater planet you came from."
            mc "My world is so different, the brothels around here primarily deal with female customers right?"
            melody "Yup, thirsty females that pay for sex because they can't get it elsewhere."
            melody "But we don't have that problem, right Bloss?"
            show blossom embarrassed with dissolve
            blossom "Uhmm, hehe, I guess not."
            "It is strange seeing two close friends from such different backgrounds."
            "A farmer girl and a high class boutique girl. What's even more unusual is they both want to be DJs."
            show melody happy with dissolve:
            melody "And this is our music studio!"
            show blossom happy with dissolve
            blossom "I mean... It's the college's, but we get to use it."
            mc "Hey, this is pretty awesome, you gonna show me inside?"
            melody "Heh, sure, why not?"
            scene bg black with dissolve
            play music inpeace fadeout 3.0
            stop ambience fadeout 2.0
            scene bg musicstudio with dissolve
            show melody happy with dissolve:
                xpos 800
                ypos 75
            show blossom neutral with dissolve:
                xpos 200
                ypos 75
            melody "Hey Claire, I've brought a friend if you don't mind."
            show claire happy with dissolve
            claire "Hmm, who's this?"
            mc "O-Oh! It's you..."
            show claire neutral with dissolve
            claire "It's 'me'? I don't think we've ever met before."
            claire "Hey Melody, would it be okay if I just took your friend to the side for a private conversation?"
            melody "Huh? You've fallen for him already? Of course you can!"
            claire "Tch, your inappropriate remarks aren't appreciated."
            melody "Yeah, yeah..."
            stop music fadeout 3.0
            scene bg musicstudio2 with dissolve
            "The mare called Claire takes me aside to another empty music studio."
            mc "What did you need me for, Claire?"
            show claire neutral with dissolve
            claire "You recognized me, so I have to go through the usual tedious process of explaining that you've never seen me before."
            mc "What do you mean? Are you not the pony from the 'spa' brothel?"
            claire "B-Brothel... Tch..."
            claire "That's owned by my twin sister and her girlfriend."
            mc "Ooohhh... I'm really sorry for getting you two mixed up."
            show claire happy with dissolve
            claire "It doesn't happen too often, but it would be awkward if my students found out."
            mc "I'd worry about them finding out by themselves if I were you."
            show claire neutral with dissolve
            claire "Yeah, you're right... Talk about a difficult situation."
            claire "It's not like I can just tell my sister to stop her vulgar business, but it puts my career in education at risk."
            play sound explosion2
            show claire neutral with hpunch
            pause 1.0
            claire "The fuck was that?"
            hide claire with moveoutleft
            scene bg black with dissolve
            scene bg musicstudio with dissolve
            show blossom shocked with dissolve:
                xpos 200
                ypos 75
            blossom "I-It just blew up!"
            show melody angry with dissolve
            melody "I knew this piece of shit was on its last legs."
            show claire neutral with dissolve:
                xpos 800
                ypos 20
            claire "Oh thank god, it was just the speaker blowing out."
            show melody neutral with dissolve
            melody "It's not just that, the entire sound system went with it."
            claire "Tch... But that was personal equipment! The college won't reimburse us!"
            melody "Eh, don't look at us, we're just poor students. Music ones too, so we're especially poor."
            show blossom sad with dissolve
            blossom "I-I'm really sorry Miss..."
            claire "It-It's my fault... Since this is my own unofficial equipment, it never received the required safety checks."
            show melody angry with dissolve
            melody "It's not just your stuff Claire, the sound system belongs to the school and that still blew the fuck up."
            claire "Ohh jeez... M-Maybe I should contact my sister..."
            "Claire looks at me for a moment, seems like she has a job for me."
            scene bg musicstudio2 with dissolve
            show claire happy with dissolve
            claire "I'll need some monies to get some spare equipment, but I can't just leave work right now."
            claire "Can I entrust you to visit my sister and collect it? I'm going to send a magic mail to let her know you're coming."
            show claire neutral with dissolve
            claire "You know I can't send anyone else..."
            mc "Sure thing, but she will give you the money right?"
            show claire happy with dissolve
            claire "Yeah, she owes me one, now is a better time than ever for her to pay me back."
            claire "And of course, you'll get something out of this too..."
            mc "What's that?"
            show claire neutral with dissolve
            claire "How's 25 monies and a discount at the brothel?"
            mc "Sounds great, I'll leave right now."
            show claire laughing with dissolve
            claire "Perfect! Thank you so much [playername]!"
            scene bg black with dissolve
            play ambience ambienceday
            if fr == 1:
                show bg pgworldmapdialogue
            else:
                show bg worldmapdaynoui with dissolve
            "And so, somehow I've ended up visiting the suburbs spa for work."
            play music boutique fadein 3.0
            show bg sparoom with dissolve
            show spaowner happy with dissolve
            greymare "Good morning sir, please take a look at our menu and- !!!"
            mc "Well, well, you really do look a lot like your sister."
            show spaowner neutral with dissolve
            greymare "You're [playername] right? I just got that magic mail."
            mc "Heh, yeah. Sorry about the trouble, but there's been an incident."
            show spaowner happy with dissolve
            greymare "It's no trouble at all [playername], please follow me."
            hide spaowner with dissolve
            show bg spabedroom with dissolve
            "The mare leads me through a staff only door and up a flight of stairs. We end up in a bedroom of all things. This building is pretty similar to the boutique."
            $ greymare = "Tavi"
            show spaowner happy with dissolve
            greymare "The name's Tavi by the way. I don't usually work on a first name basis with customers, but I already know your name, so there's no harm."
            mc "It's always nice having a name to moan while you're serving me."
            show spaowner laughing with dissolve
            greymare "Hehe... I'm just going to count some money out for Claire, and your extra."
            greymare "But there's one small problem regarding your 'bonus'."
            mc "What's that?"
            show spaowner happy with dissolve
            greymare "Claire said you wanted a discount at the spa, but [playername]... You already have a two for one discount here, remember?"
            mc "Oh yeah... If I buy one service, both you and your girlfriend will do it. Quite the bargain."
            greymare "Yup, we usually spend all day massaging and performing services on other mares. You're the only interspecies male customer we have!"
            greymare "Sure we get one or two stallions a month, but stallions... well... they ejaculate {i}really{/i} quickly. So my girlfriend and I practically jump at the chance to have fun with you."
            mc "Ooohhh... Don't worry about a 'bonus' then. You do enough for me."
            show spaowner laughing with dissolve
            greymare "Actually, I had another idea. How about a free 'visit' ticket?"
            show spaowner happy with dissolve
            mc "A free visit to the spa? Sure, I don't mind something like that."
            greymare "Hehehe, excellent! My sister isn't expecting you back immediately, is she?"
            mc "I suppose not, are you implying what I think?"
            show spaowner laughing with dissolve
            greymare "Hehe, how about we redeem that ticket right now? Lay down on the bed for me."
            "She really wasn't kidding when she said she would practically jump at the chance to have fun with me..."
            "Well, I'm not one to turn down a free 'spa treatment'."
            scene bg black with dissolve
            play music sex1 fadeout 3.0
            show bg spabedroom with None
            show tavi ride1 with dissolve
            "Softly laying me down with her delicate touch, she straddles my waist and gives me an immediate view of her incredibly sexy rear."
            greymare "The two for one deal means I haven't had a chance to enjoy you all for myself."
            mc "Isn't this cheating?"
            greymare "Tch, please... My girlfriend and I work in an 'erotic' spa, we have an open relationship."
            greymare "That way I can get the dick I crave too, hehe."
            "Damn this mare is horny! She must work in the spa purely because she enjoys it."
            "I wonder if Claire has this kind of libido too? Considering she calls this spa a brothel in a derogatory way, I'm not so sure."
            play sound cum
            show tavi ride2 with dissolve
            "Before I can finish my thought Tavi takes my cock in her soft furry grip, aligns it with her moist pussy and sinks down onto it."
            greymare "Ahhh, ahh... That hits the spot..."
            mc "You mares really are like addicts, huh?"
            greymare "Oh shush you, you're the one that agreed to do this for a 'brothel discount' so I don't think you're in a position to judge."
            play ambience sex fadein 2.0
            "*Squish, squish*"
            "She raises her hips once more, before slowly bringing her ass down once again. Slowly, like a massage to the cock, she savours each movement."
            "Her insides mold around my cock, squeezing tightly around my shaft as we make love. Her nether lips particularly gripping tightly with each movement upwards."
            greymare "Ahhh, mmmmphh... I don't get nearly enough male customers, mmmhh..."
            "Moans of pleasure escape her lips and a warm feeling spreads throughout my body as her sensual fucking relaxes my mind."
            "She truly is an excellent masseuse, even in this lustful scenario her movements are practiced and designed to maximise pleasure and relaxation."
            "I may not be as sensual and loving as her, but I decide to return some of Tavi's thrusts with my own passion filled ones."
            greymare "Ohh, f-fuck! Ahh, ahhh, aaaahhhh! Y-You're supposed to let me - aaahhh!"
            "The two of us move in unison as the rutting intensifies and her moans grow louder, only further enticing me and my fervent fucking."
            greymare "Ahhh mmmhh, fuck me harder [playername]! This is the best cock I've had in years! Ahhh, ahh!"
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
            greymare "Haahh... Phew... I never get to go all out like that with a customer..."
            hide tavi with dissolve
            play ambience ambienceday fadein 3.0
            show spaowner laughing with dissolve
            greymare "That was a good fuck! If you want it again though, I'll have to charge, ehehe."
            mc "It's strange how the one time it's free you get to enjoy it the most."
            show spaowner happy with dissolve
            greymare "Mmm, true... If you pay, you're getting a professional service so I can't focus on my own pleasure. It's not the same as fucking for fun."
            show spaowner laughing with dissolve
            greymare "But my business {i}is{/i} sex and erotic services, I can't just give that away for free! *Giggle*"
            mc "Well, I always have your sister."
            show spaowner neutral with dissolve
            greymare "W-Wha? You devil!"
            greymare "Fine, I get it... I had a lot of fun too..."
            show spaowner happy with dissolve
            greymare "I can make you a special customer, just ask me for a 'special' when you arrive. I'll bring you in here and we can forget the spa and just fuck for fun."
            show spaowner neutral with dissolve
            greymare "D-Don't tell my girlfriend though! She'd be so mad if she found out I was... y-yeah..."
            mc "Are you sure you want to make me a special customer?"
            show spaowner happy with dissolve
            greymare "*Sigh*. You can't imagine how horny I get having to pleasure other people for up to six hours a day without a chance to get myself off."
            show spaowner laughing with dissolve
            greymare "I should be the one paying you."
            mc "Don't gimme any ideas, hah!"
            show spaowner happy with dissolve
            greymare "Tch, you really are the devil. Here, take Claire's money."
            $ monies += 25
            greymare "And if you're going to seduce her too, well... I don't wanna hear about it!"
            mc "Thanks Tavi, I'll be seeing you."
            greymare "I'll be looking forward to it, [playername]."
            scene bg black with dissolve
            "..."
            show bg musicstudio with dissolve
            show claire happy with dissolve
            claire "Thank goodness you're here, this is definitely enough money to cover the school's hardware I accidentally fried."
            claire "Although I'll still need to buy replacements of my own things out of my savings."
            mc "Where are the girls?"
            claire "Hm? They're out to lunch right now, you did take quite a while considering it's only a thirty minute walk."
            mc "Sorry about that, I took a break at the spa."
            show claire neutral with dissolve
            claire "A {i}break{/i}? At the brothel?"
            mc "Ah, get your mind out the gutter, I went upstairs and spoke with Tavi personally."
            show claire happy with dissolve
            claire "Ohh, right... It was wrong of me to assume!"
            show claire neutral with dissolve
            claire "Still, I've been thinking... You already knew my sister before you met me."
            claire "What would a man like you be doing at a place like that?"
            mc "Is there something wrong with that?"
            claire "Well, it's just... Have you had sex with my sister before? L-Like, purchased her services?"
            "Uhm, awkward."
            claire "Sorry, sorry! I realize that question is very inappropriate. I shouldn't be sticking my nose into your affairs like that."
            claire "It's just so strange to think that my twin sister is out there doing vulgar things like that."
            claire "She never used to be like that... Well, that was until she met Ivy."
            $ whitemare = "Ivy"
            mc "Is that her girlfriend?"
            claire "Mhm, Ivy was the original masseuse... Ah! Sorry, I'm going to stop rambling now."
            show claire happy with dissolve
            claire "It has been one heck of a day. Thank you so much for your help."
            show melody neutral with dissolve:
                xpos 800
                ypos 75
            melody "Oi! Wormy boy where'd you disappear earlier?"
            show blossom happy with dissolve:
                xpos 200
                ypos 75
            blossom "Did you go to get help?"
            claire "Uhm, [playername] helped me with a small favour."
            show blossom shocked with dissolve
            blossom "I could have done that miss, no need to send [playername], he's very busy."
            mc "No worries Blossom, I got paid."
            show melody sadistic with dissolve
            melody "Oh really?"
            show blossom happy with dissolve
            show melody happy with dissolve
            claire "Now that I've got some monies, I'm going to order some new equipment, do you girls want to help me?"
            show blossom laughing with dissolve
            blossom "Sounds like fun! I want to get the orange speakers this time!"
            melody "No way, the pink ones are the best!"
            claire "Can't we just get the grey ones again?"
            hide claire with dissolve
            blossom "You're so boring, miss!"
            hide blossom with dissolve
            mc "Looks like my job here is done."
            show melody neutral with dissolve
            melody "One more thing, [playername]! My laptop was corrupted during the short circuit, and all my music is on there! Could you help me repair it?"
            mc "Help you? What can I do for it, Mel?"
            show melody happy with dissolve
            melody "Nothing, you'd definitely make it worse if you tried to fix it! But if you gave me some monies I could get it repaired."
            mc "I feel like I'm repairing a lot of your things lately... How much?"
            show melody neutral with dissolve
            melody "I checked this place on the way to lunch, they quoted me for 150 monies!"
            mc "ONE HUNDRED AND FIFTY?! That's almost a week's wages!"
            show melody fufufu with dissolve
            melody "Pfft, sorry, I didn't realize you were so poor! You know bouquets of roses are 80 monies at the market, right?"
            mc "You didn't realize the guy living out of other people's homes and working basic minimum wage jobs wasn't poor?"
            mc "Can't you ask Ruby about this?"
            show melody happy with dissolve
            melody "Well, I was kinda hoping you and Ruby would do more of that cam stuff to earn more money."
            mc "And I have to be the one to pay up?"
            show melody neutral with dissolve
            melody "I want to recover my files, and I have some things I don't want Ruby to see if she were hypothetically in the shop with me."
            mc "I'll consider it. But don't rely on me, alright?"
            show melody happy with dissolve
            melody "If you can do it, we'll be able to listen to some awesome tunes right here, okay? And I'll totally let you frick me!"
            mc "You let me do that anyway..."
            melody "Just come back to the music studio when you have the fat stacks, I'll make it worth your while."
            melody "Here, take a spare key card to get in, just in case."
            mc "Ah, that's pretty useful, thanks."
            show melody sadistic with dissolve
            melody "See? I'm not all bad."
            scene bg black with dissolve
            "..."
            jump evening
        elif musicstudio == 1:
            pass
        else:
            "A music studio? Seems to be part of a local college."
            "The front door requires a student key card. The only way to get in would be to befriend a local student, I guess."
            jump citymenu
        stop ambience fadeout 3.0
        play music inpeace fadeout 3.0
        scene bg musicstudio with dissolve
        show melody happy with dissolve:
            xpos 100
            ypos 85
        $ rand = renpy.random.randint(1,2)
        if rand == 1 and melodycunnilingus == 0:
            $ melodycunnilingus = 1
            "You've unlocked a secret scene! Requirements met: Visit the music studio. 50%% chance."
            jump melodycunnilingus
        show claire happy with dissolve
        if blossomvisit == 1:
            show blossom happy with dissolve:
                xpos 800
                ypos 85
        if musicstudiosex == 1:
            pass
        else:
            if werewolfsex == 1 and clairewwc == 0:
                $ secretsunlocked += 1
                claire "Oh, [playername]! Could I have a minute to talk with you?"
                mc "Of course, Claire."
                stop music fadeout 3.0
                scene bg musicstudio2 with dissolve
                "You found a secret scene! Requirements met: Visit the now cured werewolf."
                show claire neutral with d
                claire "Could we, uh... Not talk about that werewolf incident? I'd rather forget about that whole thing."
                mc "Yeah, of course. I wasn't going to say anything."
                claire "Thanks, [playername]."
                claire "And uhm... Nice dick... Sex with my boyfriend feels a bit lame now."
                mc "Thanks, I think?"
                claire "You wanna, maybe...?"
                mc "Is that not cheating?"
                claire "It's okay. Ever since Lee {i}actually{/i} cheated on me by having sex with the Zebra as a pony, we decided to open up our relationship anyway..."
                claire "I kinda did it because I knew I'd see you again, and... and..."
                mc "You want to have sex with me again?"
                claire "Mhm. For some reason, I can't get you out of my head."
                claire "It's like my brain thinks you're my 'mate', or something. I know it sounds weird; the werewolf thing must have messed with my head."
                menu:
                    "Accept":
                        show claire happy with d
                        claire "Please lay down. I think after your excellent job last time, I should return the favour."
                        jump clairesex
                    "Refuse":
                        claire "Awhhh... Feel free to ask me whenever..."
                        $ clairewwc = 1
                scene bg musicstudio with dissolve
                show claire happy with dissolve
                show melody happy with dissolve:
                    xpos 100
                    ypos 85
                if blossomvisit == 1:
                    show blossom happy with dissolve:
                        xpos 800
                        ypos 85
                jump musicstudiomenub
            claire "Hey [playername], what can I do for ya?"
        $ musicstudionight = 0
        label musicstudiomenu:
            if musicstudionight == 1:
                jump musicstudiomenunight
        menu musicstudiomenub:
            "Listen to Music":
                if melodylaptop == 0:
                    claire "Unfortunately we don't have a lot of music available..."
                    melody "If you fixed my laptop you'd have a lot more!"
                else:
                    melody "Check it out, we've got everything!"
                jump musicgallery
            "Talk" if musicstudiotalk == 0:
                $ musicstudiotalk = 1
                menu:
                    "Talk about Claire":
                        mc "Hey Claire, how did you get into music?"
                        claire "I picked up a guitar when I was younger and transitioned from there. It became 'my thing' that distinguished me from my sister."
                        melody "And she studied here too!"
                        claire "Yep, right here, only a few years ago. I guess the only reason I'm back is because it's a reliable career as a musician."
                        claire "But don't misunderstand, I enjoy teaching. I might not have much of an impact on the industry myself, but I'm sure the hundreds of students I'll teach will go on to do amazing things."
                        mc "That's a great outlook. Do you have any other hobbies?"
                        claire "Yeah, actually. I enjoy hiking through the forests and mountains with my boyfriend."
                        if forestvisit1 == 1:
                            mc "Oh really? I bet you need to come prepared in case you encounter any dangerous flora and fauna."
                        else:
                            mc "It's so beautiful around here, what's that like?"
                        claire "Well, there can be a few encounters with creatures in the forest, but most things ignore you if they're not provoked."
                        claire "It's thrilling to get to the top of those mountains and overlook the city, the journey is worth every step."
                        if blossomvisit == 1:
                            blossom "I wanna go hiking too sometime, you should take us [playername]!"
                        else:
                            melody "I wanna go hiking too sometime, how about it wormy boy?"
                        mc "Sure, I might consider it if we get some time off."
                        jump musicstudiomenu
                    "Talk about Melody and Blossom":
                        mc "How are Melody and Blossom as students? Not causing trouble I hope."
                        claire "They're unique to say the least, particularly you Melody, you have lots of unique ideas when it comes to music."
                        show melody fufufu with dissolve
                        melody "That's because I don't let what sounds 'right' or 'wrong' hold me down."
                        claire "Melody tries to capture energy and adrenaline in her music with drums and bass that you can't help but groove to."
                        claire "Blossom has been very influenced by the style, but prefers a more soft and ambient tone."
                        claire "Both the girls are trying to create music that moves you and gives you goosebumps, but in very different ways."
                        show melody happy with dissolve
                        melody "Our stuff is pretty niche, but some of the videos I've uploaded on the internet have a few hits."
                        claire "A lot of people say that luck is a big factor on succeeding as an artist, but in this internet age if you make something good and put it out there, it'll attract a crowd."
                        claire "And thus anyone can become a musician if they know what they're doing these days."
                        mc "You could say that about anything really, quality art, stories, et cetera."
                        claire "True, we're living in a golden age of creativity!"
                        show melody neutral with dissolve
                        melody "Yeah but, that doesn't mean everyone is going to be successful. Talent alone isn't enough to succeed."
                        melody "For every success there's a dozen or so that are just as good, but didn't have the skills required to succeed. And often, a lot of those skills have very little to do with the product on offer."
                        mc "Do you think you'll be a success?"
                        show melody happy with dissolve
                        melody "Yeah, I will be."
                    "Talk about Teaching Music":
                        mc "I noticed that you give the girls a lot of freedom while teaching. How do you manage to teach music while also allowing students the creative freedom to play the music they want to play?"
                        show claire neutral with dissolve
                        claire "That's a question I've often mulled over. I know of a lot of institutions that try to push an agenda onto their students and show them the 'right way to play', or do whatever for that matter."
                        show claire happy with dissolve
                        claire "The way I teach is by giving every student a hypothetical 'toolbox' and adding useful tools, tips and ideas to that toolbox that they can utilize however they want."
                        claire "This way my teaching is malleable and can suit an entire lecture hall of students that play different genres and instruments."
                        melody "She's a damn good teacher! That's why I signed up to work with her for my final year!"
                        show claire neutral with dissolve
                        claire "Speaking of the final year, there are exams... It's immeasurably difficult to test candidates in music, because on what metric do you assign quality in a medium that's purely subjective?"
                        claire "I mean sure, there are certain things like composition, structure, and lyrics that can be broken down and observed, but a lot of it is still very subjective."
                        claire "That's perhaps why some institutions streamline the system by enforcing 'rights' and 'wrongs', simply because it's easier to teach and test that."
                        claire "But a system like that would abandon a musician like Melody, who creates experimental content that isn't following traditional music trends."
                        melody "Yeah, I don't really try to make my music good, I just try to create a 'mood' and push the development of the music towards that mood."
                        melody "And I know that not everyone is going to like my music, but the people that do like it are going to love it even more because of the extreme lengths  I go."
                        claire "Yeah... A strict system limits freedom and evolution, and I needn't tell even another species such as yourself how much music evolves."
                        show  claire happy with dissolve
                        claire "I like to nurture that creativity, because that very creativity is one of the reasons I fell in love with music."
                jump musicstudiomenu
            "Sex":
                if melodylaptop == 0:
                    "No one wants to have sex with me right now"
                    jump musicstudiomenu
                else:
                    menu:
                        "Melody":
                            $ musicstudiosex = 1
                            "I ask Melody if we can 'talk' in another room, I wink while asking and she knowingly nods."
                            scene bg black with dissolve
                            scene bg musicstudio2 with dissolve
                            play music yanderecomplex
                            show melodyb studiosex
                            show melody studiosex1
                            with dissolve
                            if  melcunnilingustoday == 1:
                                melody "So, licking my pussy wasn't enough for you, eh? I guess I'll let you fuck me for doing such a good job."
                                mc "I can't believe we nearly got caught."
                                melody "Heh, I was keeping an ear out."
                            else:
                                melody "You're a bad influence you know! I was a virgin when we met."
                            "Upon seeing Melody's erotic form and wet snatch, my cock starts to grow in expectation of the upcoming fuck."
                            melody "Oohh, lil' wormy is evolving into big wormy!"
                            mc "And your pussy is drooling like a ravenous... Snake?"
                            melody "Heh, leave the dirty talking to me. Now, let's fuck!"
                            "She fondles her cute breasts while I get into position next to the table she's laying on."
                            play sound cum
                            show melody studiosex2 with dissolve
                            "Eagerly I slide the length of my erection inside her pussy, immediately feeling the tender warmth of her insides."
                            melody "Mmmhh, your cock is really moreish."
                            mc "You're becoming more open to sex, eh? Maybe you're an addict."
                            melody "Pfft, nah! You're my toy until the very end."
                            play ambience sex fadeout 3.0
                            "Desiring to make the most of this, I start to pump into her soaking cunt with reckless abandon."
                            show melody studiosex3 with dissolve
                            "Although Melody isn't surprised, and she braces herself. While she tries to keep the volume of her moans subdued, she can't help but slip the occasional gasp of delight."
                            mc "Shh, Claire will hear you."
                            show melody studiosex2 with dissolve
                            melody "D-Don't tell me what to do, ahh... Mmmphh..."
                            show melody studiosex3 with dissolve
                            "Occasionally she takes her spare hand and moves it between groping her cute breasts and her clit, rubbing to enhance her pleasure."
                            "As I thrust, I can feel her pussy tingle and drool with need. It's even wetter than usual as it occasionally gushes fluids, especially when she rubs her clit."
                            show melody studiosex4 with dissolve
                            melody "F-fuck, your cock makes me squirt, haahh... Mmmhh, mmh!"
                            "Her vagina begins to clench even harder around my throbbing cock as her mare pussy begs to be filled up by my semen."
                            melody "C-Coming! Mmphh, mmmmphh... *Squelch, squish!* *Squirt!*"
                            "I bite my lip as I try to hold back my own orgasm to savour this amazing pleasure for as long as I can."
                            melody "C-Cum for me, [playername]!"
                            "However, Melody's moans and sweet talking tips me over the edge and I begin to orgasm."
                            play sound cum
                            show melody studiosex5 with cum
                            play sound cum
                            show melody studiosex5 with cum
                            play sound cum
                            show melody studiosex5 with cum
                            "I begin to release my load deep inside of her soppy pussy, pumping several jets of cum into her hungry womb."
                            play sound cum
                            show melody studiosex5 with cum
                            play sound cum
                            show melody studiosex5 with cum
                            play sound cum
                            show melody studiosex5 with cum
                            "Her strong legs lock around my waist and pull me in deeper as her pussy continues to gush."
                            show melody studiosex7 with dissolve
                            stop ambience
                            "Eventually my climax dries up and her legs let me go, allowing me to pull my cock out and watch the cum dribble out."
                            show melody studiosex8 with dissolve
                            melody "Mmphh... What a messy fuck. I can always rely on you, eh?"
                            show melody studiosex7 with dissolve
                            melody "Phew, alright. Let's go back."
                            jump musicstudio
                        "Claire" if clairewwc == 1:
                            claire "Ahh. Come with me for a second, [playername]."
                            hide claire with d
                            show melody sadistic with d
                            "Melody knowingly looks on as Claire and I leave the room."
                            scene bg black with dissolve
                            scene bg musicstudio2 with dissolve
                            label clairesex:
                                play music sex1 fadeout 3.0
                                hide claire
                                show tavi ride1
                                with dissolve
                                "Softly laying me down with a familiar delicacy, she straddles my waist and gives me an immediate view of her incredibly sexy rear."
                                claire "Mmm, do you like my pussy? It's very wet for you."
                                "Claire is really horny and eager for some fun. I know this isn't our first time having sex, but I do wonder in the back of my mind why she wants it so much."
                                "Well, it's not my place to think about that. I'll take responsibility for spoiling her werewolf form by coddling her pony form."
                                play sound cum
                                show tavi ride2 with dissolve
                                "Before I can finish my thought Claire takes my cock in her soft furry grip, aligns it with her moist pussy and sinks down onto it."
                                claire "Ahhh, ahh... That's it! Ahhh, so good..."
                                mc "Ohhh, you're so wet!"
                                claire "Mhhmm, especially when you walked in, cutie."
                                play ambience sex fadein 2.0
                                "*Squish, squish*"
                                "She raises her hips once more, before slowly bringing her ass down once again. Slowly, she savours each movement."
                                "Her insides mold around my cock, squeezing tightly around my shaft as we make love. Her nether lips particularly gripping tightly with each movement upwards."
                                claire "Ahhh, mmmmphh... Feels so good, mmmhh..."
                                claire "I wanna do it a bit rough, and primal!"
                                "She begins to speed up her movements. An increasing amount of moans escape her lips as her sensual movements fill us both up with pleasure."
                                "While not as skilled as her sister, her lustful enthusiasm arguably makes up for it. Her eager moans and movements serve to arouse me greatly."
                                claire "I kinda miss being a werewolf; the sex was amazing!"
                                "Rather than laying back and taking it, I decide to return some of Claire's thrusts with my own passion filled ones."
                                claire "Ohh, f-fuck! Ahh, ahhh, aaaahhhh! That's it, keep going! Aaahhh!"
                                "The two of us move in unison as the rutting intensifies and her moans grow louder, only further enticing me and my fervent fucking."
                                claire "Ahhh mmmhh, fuck me harder, [playername]! Ahhh, ahh!"
                                "My lover soon begins to orgasm, causing her pussy to contract rhythmically around my cock, further enhancing the pleasure."
                                "Soon after her own, I feel my climax begin to rise. I rapidly thrust my cock into her pussy as I push myself over the edge."
                                play sound cum
                                show tavi ride3 with cum
                                play sound cum
                                show tavi ride3 with cum
                                "My orgasm is soon unleashed as my cock explodes into Claire, her pussy taking in each and every drop of my thick cum."
                                play sound cum
                                show tavi ride3 with cum
                                play sound cum
                                show tavi ride3 with cum
                                "She finishes me off not as the innocent music teacher I once knew, but as a lustful mare trying to drain my cock of all the pleasure she can."
                                claire "Yesss, yess! Aahhh, ahh! *Squish, squelch!*"
                                stop ambience fadeout 2.0
                                stop music fadeout 3.0
                                "Cum oozes from our point of connection as she comes to a stop."
                                claire "Haahh... Phew... I'm glad I got to go all out with you..."
                                hide tavi with dissolve
                                show claire happy with dissolve
                                claire "Hehehe, I knew I could count on you for a good fuck."
                                claire "Let's uh, quickly head back before Melody notices something's wrong."
                                scene bg musicstudio with dissolve
                                show melody happy with dissolve:
                                    xpos 100
                                    ypos 85
                                if clairewwc == 0:
                                    show melody death1 with d
                                    melody "Did you just... fuck my teacher?"
                                    mc "Uhhh..."
                                    $ clairewwc = 1
                                    show claire happy with dissolve
                                    claire "Everything alright?"
                                    show melody happy with d
                                    melody "Yep, just doing some work!"
                                else:
                                    show claire happy with d
                                if blossomvisit == 1:
                                    show blossom happy with dissolve:
                                        xpos 800
                                        ypos 85
                                jump musicstudiomenub
                        "Back":
                            jump musicstudiomenu
            "Fix Melody's laptop (-150 Monies)" if melodylaptop == 0:
                if monies < 150:
                    "I don't have enough monies!"
                    jump musicstudiomenu
                else:
                    jump melodylaptop
            "Leave":
                jump city
        label musicgallery:
            stop music fadeout 1.0
            if melodylaptop == 0:
                menu:
                    "Day Theme":
                        play music day
                        menu:
                            "Currently listening to That's One Sly Cat - Artificial Music."
                            "Stop":
                                jump musicgallery

                    "Wagon Theme":
                        play music wagon
                        menu:
                            "Currently listening to Abstract Foilage - Artificial Music."
                            "Stop":
                                jump musicgallery

                    "Boutique Theme":
                        play music boutique
                        menu:
                            "Currently listening to Good Day - Low Frequency Music."
                            "Stop":
                                jump musicgallery
                    "Farm Theme":
                        play music farm
                        menu:
                            "Currently listening to Bald Mountain - God Hand"
                            "Stop":
                                jump musicgallery


                    "Back":
                        jump musicstudiomenu

            else:
                    menu musicgalleryp1:
                        "Day Theme 1":
                            play music day
                            menu:
                                "Currently listening to That's One Sly Cat - Artificial Music."
                                "Stop":
                                    jump musicgallery
                        "Day Theme 2":
                            play music day2
                            menu:
                                "Currently listening to Stuck in the Machine - NO MIC."
                                "Stop":
                                    jump musicgallery
                        "Wagon Theme":
                            play music wagon
                            menu:
                                "Currently listening to Abstract Foilage - Artificial Music."
                                "Stop":
                                    jump musicgallery

                        "Boutique Theme":
                            play music boutique
                            menu:
                                "Currently listening to Good Day - Low Frequency Music."
                                "Stop":
                                    jump musicgallery
                        "Farm Theme":
                            play music farm
                            menu:
                                "Currently listening to Hip Jazz - Benjamin Tissot"
                                "Stop":
                                    jump musicgallery
                        "Page 2 ->":
                            jump musicgalleryp2
                        "Back":
                            jump musicstudiomenu
                    menu musicgalleryp2:
                        "Butters' Theme":
                            play music butters
                            menu:
                                "Currently listening to Before you Fall Asleep - Jhove"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp2
                        "Lily's Theme":
                            play music lily
                            menu:
                                "Currently listening to Another Perspective - Idealism."
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp2
                        "Melody's Theme":
                            play music melodytheme
                            menu:
                                "Currently listening to N.ercophillia: it applies to the dead inside now (lorncloudshit) - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp2
                        "Castle Theme":
                            play music castle
                            menu:
                                "Currently listening to La fille aux cheveux de lin by Claude Debussy (1909)"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp2
                        "Danger!":
                            play music danger
                            menu:
                                "Currently listening to Euphoric Filth - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp2

                        "<- Page 1":
                            jump musicgalleryp1
                        "Page 3 ->":
                            jump musicgalleryp3
                        "Back":
                            jump musicstudiomenu
                    menu musicgalleryp3:
                        "Music Studio Theme":
                            play music inpeace
                            menu:
                                "Currently listening to inpeace - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp3
                        "Melody Sex Theme":
                            play music yanderecomplex
                            menu:
                                "Currently listening to Yandere Complex - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp3
                        "Night Theme":
                            play music PeaceSerenity
                            menu:
                                "Currently listening to Another Perspective - Idealism"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp3
                        "Intense":
                            play music prismaserenade
                            menu:
                                "Currently listening to Basic Metal 6 - TeknoAXE"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp3
                        "Cindy's Theme":
                            play music toewizard
                            menu:
                                "Currently listening to Toe Wizard - Sewerslvt (/w Mortem)"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp3
                        "<- Page 2":
                            jump musicgalleryp2
                        "Page 4 ->":
                            jump musicgalleryp4
                        "Back":
                            jump musicstudiomenu
                    menu musicgalleryp4:
                        "Sad Theme 1":
                            play music sad2
                            menu:
                                "Currently listening to Danse Morialta - Kevin MacLeod"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp4
                        "Sad Theme 2":
                            play music sadpiano
                            menu:
                                "Currently listening to Dissociation - Naoya Sakamata"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp4
                        "Library Theme":
                            play music library
                            menu:
                                "Currently listening to Blue Boi - Lakey Inspired"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp4
                        "Comedy":
                            play music challenge
                            menu:
                                "Currently listening to Jazz Organ Trio Cool Blue - Doug Maxwell"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp4
                        "Tension":
                            play music triads
                            menu:
                                "Currently listening to Traids - Unknown"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp4
                        "<- Page 3":
                            jump musicgalleryp3
                        "Page 5 ->":
                            jump musicgalleryp5
                        "Back":
                            jump musicstudiomenu
                    menu musicgalleryp5:
                        "Art of Silence":
                            play music artofsilence
                            menu:
                                "Currently listening to Art of Silence - Uniq"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp5
                        "Hopelessness":
                            play music hopelessness
                            menu:
                                "Currently listening to Hopelessness - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp5
                        "Slow Death":
                            play music uhoh
                            menu:
                                "Currently listening to Slow Death - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp5
                        "Suspense":
                            play music suspense
                            menu:
                                "Currently listening to Secrets - Michael Hildreth"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp5
                        "Epic":
                            play music epic
                            menu:
                                "Currently listening to Fire and Thunder - Cjbeards"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp5
                        "<- Page 4":
                            jump musicgalleryp4
                        "Page 6 ->":
                            jump musicgalleryp6
                        "Back":
                            jump musicstudiomenu
                    menu musicgalleryp6:
                        "Spooky Breathing":
                            play music spookybreathing
                            menu:
                                "Currently listening to Central Square Mall Alternate, 2nd Floor Balcony - Silent Hill 3"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp6
                        "Cream's Baking music":
                            play music inlove
                            menu:
                                "Currently listening to inlove - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp6
                        "Mr. Kill Yourself - Sewerslvt":
                            play music mky
                            menu:
                                "Currently listening to Mr. Kill Yourself - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp6
                        "Seduced by the Queen":
                            play music aurora
                            menu:
                                "Currently listening to Bread - Lukrembo"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp6
                        "Everything's Going Wrong":
                            play music lips
                            menu:
                                "Currently listening to Lips - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp6
                        "<- Page 5":
                            jump musicgalleryp5
                        "Page 7 ->":
                            jump musicgalleryp7
                        "Back":
                            jump musicstudiomenu
                    menu musicgalleryp7:
                        "Rainy theme":
                            play music morrigan
                            menu:
                                "Currently listening to Oni - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp7
                        "Ultimate Battle":
                            play music morriganbattle
                            menu:
                                "Currently listening to The Maw - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp7
                        "Nightclub Rave":
                            play music nightclub
                            menu:
                                "Currently listening to Cyberia lyr3 - Sewerslvt"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp7
                        "Dawn's Theme":
                            play music dawn
                            menu:
                                "Currently listening to Been Here Before - NO MIC"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp7
                        "Church Theme":
                            play music church
                            menu:
                                "Currently listening to Tranquil - Whitesand"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp7
                        "<- Page 6":
                            jump musicgalleryp6
                        "Page 8 ->":
                            jump musicgalleryp8
                        "Back":
                            jump musicstudiomenu

                    menu musicgalleryp8:

                        "Augusta's Theme":
                            play music augusta
                            menu:
                                "Currently listening to Pina Colada - Silent Partner"
                                "Stop":
                                    stop music fadeout 1.0
                                    jump musicgalleryp8
                        "<- Page 7":
                            jump musicgalleryp7
                        "Back":
                            jump musicstudiomenu


        label melodylaptop:
            $ monies -= 150
            $ melodylaptop = 1
            melody "Now we're talkin'! Let's go, champ!"
            stop music fadeout 3.0
            stop ambience fadeout 3.0
            scene bg arcadiastreets with dissolve
            "Melody and I leave the studio and step out into the city streets."
            play ambience ambienceday fadein 2.0
            play music melodytheme fadein 2.0
            show melody happy with dissolve
            melody "The shop's just around the corner, thank you for doing this."
            mc "You're welcome. Either way, you said you were going to 'make it worth my while'."
            show melody fufufu with dissolve
            melody "To make it up to you, I won't be mean to you for an entire day, honest!"
            mc "You're going to be nice to me? I think you've already grown quite a sweet spot for me."
            show melody sadistic with dissolve
            melody "You're gonna make me vomit with that lovey crap."
            mc "Heh, I guess being mean is just an inescapable part of you."
            show melody happy with dissolve
            melody "Not true! I'm adorable, bitch! Alright... I'll think of something to make it up to you, 150 monies is quite a lot."
            mc "Are you saying you didn't have anything in mind?"
            show melody fufufu with dissolve
            melody "Well, I kinda did! Once my laptop is fixed you'll be able to listen to tons of music."
            mc "Right, is that it?"
            show melody happy with dissolve
            melody "Mmm, there was something else on my mind. But that'll have to wait, the shop's right here."
            scene bg black with dissolve
            "It takes about an hour, but the laptop is eventually fixed. On the walk back my satchel feels notably lighter after losing 150 monies."
            "However, rather than immediately entering Claire's room, Melody leads me into an empty studio."
            stop music fadeout 2.0
            stop ambience fadeout 2.0
            show bg musicstudio2 with dissolve
            show melody happy with dissolve
            melody "Alright, we should be left alone in this room."
            mc "Should be alone?"
            show melody fufufu with dissolve
            melody "Well, you never know! We're not exactly strangers to having someone walk in on us..."
            hide melody with dissolve
            "She casually sits on table adjacent to me and gradually gets into an increasingly compromising position."
            mc "Ohh, we're doing that now?"
            play music yanderecomplex
            show melodyb studiosex
            show melody studiosex1
            with dissolve
            melody "Heh, I'm repaying the favour in a manner fit for a perv like you."
            "Upon seeing Melody's erotic form and wet snatch, my cock starts to grow in expectation of the upcoming fuck."
            melody "Oohh, lil' wormy is growing, you're such a peeerv!"
            mc "And your pussy is already drooling like a starving stallion at a banquet."
            melody "Meh, blame it on the heat and lust. Now are you going to admire me, or are you gonna fuck me?"
            "She teases her petite breasts and nipples as I get into position next to the table she's laying on."
            play sound cum
            show melody studiosex2 with dissolve
            "Eagerly I slide the length of my erection inside her pussy, immediately feeling the tender warmth of her insides."
            melody "Mmphh, I think it'll be nice to make you do all the work for once."
            mc "Making me do all the work? And here I was thinking this was a reward."
            melody "This is a reward, ehehe! This marvellous pussy is all yours to enjoy."
            play ambience sex fadeout 3.0
            "Desiring to make the most of this, I start to pump into her soaking cunt with reckless abandon."
            show melody studiosex3 with dissolve
            "Although Melody isn't surprised, and she braces herself. While she tries to keep the volume of her moans subdued, she can't help but slip the occasional gasp of delight."
            mc "If you moan like a bitch, we'll get caught like before."
            show melody studiosex2 with dissolve
            melody "Pfft, you'd hate that, wouldn't you? Ahhah, damn perv... Mmmphh..."
            show melody studiosex3 with dissolve
            "Occasionally she takes her spare hand and moves it between groping her cute breasts and her clit, rubbing to enhance her pleasure."
            "As I thrust, I can feel her pussy tingle and drool with need. It's even wetter than usual as it occasionally gushes fluids, especially when she rubs her clit."
            show melody studiosex4 with dissolve
            melody "F-fuck, I-I'm squirting? Mmmhh, mmh!"
            "Her vagina begins to clench even harder around my throbbing cock as her mare pussy begs to be filled up by my semen."
            melody "C-Coming! Mmphh, mmmmphh... *Squelch, squish!* *Squirt!*"
            "I bite my lip as I try to hold back my own orgasm to savour this amazing pleasure for as long as I can."
            melody "C-Cum for me, [playername]!"
            "However, Melody's moans and sweet talking tips me over the edge and I begin to orgasm."
            play sound cum
            show melody studiosex5 with cum
            play sound cum
            show melody studiosex5 with cum
            play sound cum
            show melody studiosex5 with cum
            "I begin to release my load deep inside of her soppy pussy, pumping several jets of cum into her hungry womb."
            play sound cum
            show melody studiosex5 with cum
            play sound cum
            show melody studiosex5 with cum
            play sound cum
            show melody studiosex5 with cum
            "Her strong legs lock around my waist and pull me in deeper as her pussy continues to gush."
            show melody studiosex7 with dissolve
            stop ambience
            "Eventually my climax dries up and her legs let me go, allowing me to pull my cock out and watch the cum dribble out."
            show melody studiosex8 with dissolve
            melody "Mmphh... What a messy fuck, and... my best one yet, I think... Phew."
            show melody studiosex7 with dissolve
            melody "Hey, how about a second go? I know a good spell."
            show melody studiosex7 with moxiespell
            "Before I even have a chance to agree or disagree, the spell already goes off with a flash and the sensitivity in my cock dissipates."
            melody "Come on, don't be shy... My heat's pretty bad today, so you're going to have to give my pussy a second beating."
            mc "Well, given that you forced me to have another erection, I'm not in a position to argue."
            melody "That's the attitude, you're such a good 'toy', hehe."
            show melody studiosex6 with dissolve
            play ambience sex fadein 2.0
            "With her legs still spread out eagerly, I reposition myself and reinsert my cock. My shaft still slick with her glistening juices."
            "The heat from her juicy cunt once again consumes my member and her legs wrap around my torso as we resume our reckless fuck."
            melody "Mmmphh, fuck yeah..."
            "Melody even begins to thrust and buck against me, trying her best to maximise the euphoric pleasure, although in her position the attempts are awkward."
            show melody studiosex5 with dissolve
            "Recognizing her increasing desire, I forcefully pound her. The pleasure overwhelms Melody as her thighs quiver and her tail thrashes about."
            melody "Ohh, yes, yes... Be a good toy and give it to me! Fuck me harder!"
            "Melody squeals in lustful joy and tries to rut as hard with me as I am with her. She seems to have completely forgotten about trying to be quiet."
            "Her walls contract around my shaft, and another squirt of juices escapes her pussy, signalling that she's having another orgasm."
            play sound cum
            show melody studiosex5 with cum
            play sound cum
            show melody studiosex5 with cum
            "The pure energy and vigor bring me to my second orgasm faster than my first, and my cock unloads a second torrent of thick cum into her womb."
            play sound cum
            show melody studiosex5 with cum
            play sound cum
            show melody studiosex5 with cum
            melody "Mmmphh, mmm... *Squelch, squish...*"
            show melody studiosex8 with dissolve
            stop music fadeout 3.0
            stop ambience
            "Our explosive orgasms slowly come to an end. Spent, Melody slumps over onto the table."
            "Feeling daring, I take advantage of her position to cuddle her. She welcomes the move, and takes it a step further by moving in for a tender kiss."
            melody "Ahh... You're such a catch..."
            "The two of us embrace with satisfaction as we regain our breath."
            hide melody
            hide melodyb
            with dissolve
            "It's Melody that breaks out of the embrace first. She takes a moment to clean up the copius mess we made with some tissues, before returning to sit beside me."

            show melody closehappy
            with dissolve
            melody "That was uhm, fun... I know it doesn't make up for all that money you spent on me, but I hope you know that I appreciate you."
            melody "Even though sometimes I might act a bit mean."
            "I smile and pat Melody on the head."
            mc "I already know that dummy, I wouldn't have given you the money otherwise."
            show melody closefufufu with dissolve
            melody "Pfft... You cute bastard. I'm just glad I chose you to be my sex toy."
            mc "For you, that's almost 'cute'."
            show melody closehappy with dissolve
            melody "Yeah... 'cute'. Anyway... I should get back. Come see me again sometime champ."
            mc "I wouldn't miss it."
            scene bg black with dissolve
            jump evening
        label melodycunnilingus:
            play music yanderecomplex fadein 30.0
            "I step into the music studio and spot Melody alone tinkering on her laptop. Not an unusual activity for Melody to do in her spare time."
            show melody sadistic with d
            melody "Hey worm. Looks like it’s just you and I for the hour."
            mc "Oh really?"
            "Oh shit!"
            show melody fufufu with d
            melody "You know, you never thanked me properly for giving you a key card to get in here."
            mc "Fairly sure I did, actually."
            if melodylaptop == 1:
                mc "And, what about fixing your laptop? That wasn’t cheap you know."
            show melody happy with d
            melody "Mm, mm… Fair point. But I’d quite like it if you were to thank me in another way."
            mc "Is this the part where you pretend I’m a pervert, while getting me to do something perverted for you?"
            show melody satisfied with d
            melody "Hmph, well it’s not very fun when you spell it out. It’s not easy improvising these scenarios you know."
            mc "Hey, just go with the flow. Why skirt around the issue? Just bark orders."
            show melody sadistic with d
            melody "You know what? You’re right! Why am I trying to be subtle? Get on your fucking knees, whelp."
            hide melody with d
            "Oh no. Have I accidentally created a monster?"
            "I’ll play along because these scenarios usually end up benefitting me anyway. Melody is a secret sweetheart like that."
            "I kneel on the ground before Melody, after pretending to debate the issue for a few seconds in my head, causing her to grin."
            show melody closedeath1 with d
            melody "That’s a good little pet. Hmph, it looks like you’re already starting to get slightly aroused, and I haven’t done or said anything lewd yet."
            melody "Yeah, I can see it… Your penis is getting hard just from kneeling before me. Just what kind of disgusting thoughts are you thinking?"
            melody "Do I have to squish your cock with my foot?"
            show melody closesadistic with d
            melody "Or maybe, I have a better idea…"
            melody "Come closer, boy."
            "I shuffle closer."
            show melody closehappy with d
            melody "Clooooser…"
            "Uh, closer?"
            show melody closefufufu with d
            melody "I want your lips to be able to meet mine, understood, worm?"
            mc "Understood."
            scene melodyb cunnilingus
            show melody cunnilingus1
            with d
            "There. Wow, her pussy looks amazing from this angle. I knew playing along would work."
            "She’s also really wet. She really gets off on this femdom stuff."
            melody "I feel like our sex has too much of me doing things to you. Now it’s time for you to show your appreciation."
            mc "Happily."
            "I wrap both my hands around her soft thighs and push my face into her labia. She seems initially embarrassed but soon resumes a more domineering attitude."
            show melody cunnilingus2 with d
            melody "Ahh… You really are a nasty little thing, diving so eagerly into my pussy like that. Do you have no dignity?"
            "Her labia parts slightly with each lick, gently revealing the wet lips nestled between."
            "With a few lazy licks up and down her lips, I turn my attention to her clit and circle my tongue around this sensitive area."
            melody "Mmphh, mm… Well, I can’t insult your tongue work…"
            melody "I bet you’ve been practicing just for this moment. How pitiful!"
            "Hmph, I’ll show her in my own little way. Sure, I’m giving her the power today, but that doesn’t mean I’m entirely out of the dynamic."
            "Gripping her furry thighs slightly more tightly, I suckle at her clit with an intensity that’s sure to blow her mind."
            play ambience blowjob fadein 3.0
            show melody cunnilingus3 with d
            melody "Ahhh, haaahh… Oohh, ohhh, aahhh… It’s not a- ahhh!"
            "Hehe, she likes to pretend she’s in control, but with the right technique you can make a girl come in only a few minutes of this."
            "I alternate between sucking her clit and lashing it with my tongue. Keeping up a pace that’ll tire me out, but will make her come far before then."
            melody "Ahhh… Y-You don’t need to try so hard to impress me, you know!"
            "Sparks of pleasure overwhelm her until she’s nothing but a quivering mess."
            "I actively have to hold her in place due to how much her pelvis squirms."
            "After a few minutes of this treatment, her moans turn into pleasureful squeaks as she’s finally graced with an orgasm."
            show melody cunnilingus4 with d
            melody "Ahh, ahhh! Ahhh… F-Fucking hell!"
            "I keep up the pleasure throughout her entire half a minute climax, and although I’d be more than happy to continue going for another, she decides to tap out."
            show melody cunnilingus5 with d
            stop ambience fadeout 3.0
            melody "*Pant* Where did you learn how to do that?!"
            mc "Amateur lesbian porn."
            melody "Tch. You’re kinda disgusting, you know?"
            mc "Yeah, but you love it."
            show melody cunnilingus1 with d
            melody "Hmph. I want you to do that to me again sometime."
            mc "No problem."
            if crystalballactivated == 1:
                jump cbmenu
            show melody cunnilingus5 with d
            melody "Hey, stand up, quickly!"
            play music inpeace fadeout 3.0
            scene bg musicstudio
            show melody happy with dissolve:
                xpos 100
                ypos 85
            show claire happy with dissolve
            claire "Everyone behaving I hope! Hehe."
            $ secretsunlocked += 1
            $ melcunnilingustoday = 1
            jump musicstudiomenub
label nightcity:
    stop music fadeout 2.0
    scene bg arcadianight with dissolve
    play ambience ambiencecity fadeout 3.0
    if citynightfirstvisit == 0:
        "Even at night, the city is thriving."
        "But in a completely different way, it's like I'm at a red-light district or something."
        "Time for some fun. I bet I could pick up some girls at the nightclub."
        "Or rather, they'll be picking me up. I almost guarantee that."
        $ citynightfirstvisit = 1
    label nightcitymenu:
        pass
    call screen nightcity
    with dissolve

    menu:
        "Where should I go?"
        "Castle":
            label castlencm:
                pass
            if libraryvisit3 == 0:
                "The guards won't let me in without a permit, even if it's night time. And no, I don't want to sneak in."
                if libraryvisit1 == 1:
                    "Maybe I could ask Lily to get me one."
                else:
                    "Who could help me get a permit?"
                jump nightcitymenu
            elif selenevisit1 == 1:
                "It's a little late to visit the city, but maybe I could visit Selene."
                menu:
                    "Visit Princess Selene?"
                    "Visit":
                        jump selene
                    "Back":
                        jump nightcitymenu
            elif selenevisitready == 0:
                "It's a little late to visit the castle."
                jump nightcitymenu
            else:
                "It's a little late to visit the castle, but maybe I could visit Selene."
                menu:
                    "Visit Princess Selene?"
                    "Visit":
                        jump selene
                    "Back":
                        jump nightcitymenu
        "Music Studio":
            label musicstudioncm:
                pass
            if musicstudio == 0:
                "I can't get in without a key card."
                jump nightcitymenu
            $ musicstudionight = 1
            scene bg musicstudio with dissolve
            "Empty, but I can still listen to music."
            menu musicstudiomenunight:
                "Listen to Music":
                    stop ambience fadeout 2.0
                    if melodylaptop == 0:
                        "Unfortunately there isn't much music available..."
                        "If I fixed Melody's laptop there'd be a lot more."
                    jump musicgallery
                "Leave":
                    $ musicstudionight = 0
                    play ambience ambiencenight fadein 3.0
                    jump nightcity
        "Art Gallery":
            jump artgallery
        "Nightclub":
            label nightclubncm:
                pass
            if nightclubmenuintro == 0:
                $ nightclubmenuintro = 1
                "Is that a nightclub? Ah, it's called ‘Bed of Chaos’"
                "This place is the closest to home. It also seems to be the largest and most popular."
                "I should make sure I have some monies before I go in. Not only is there an entry fee, but if it's anything like home, the drinks'll be overpriced."
            menu:
                "Pay Entry Fee (-5 Monies)":
                    if monies < 5:
                        "Shoot, I can't afford even 5 monies... That's embarrassing."
                        jump nightcitymenu
                    $ monies -= 5
                    jump nightclub
                "Nah":
                    jump nightcitymenu
        "Back":
            if fr == 1:
                $ worldmap = 4
            else:
                $ worldmap = 2
            jump worldmap
    label nightclub:
        stop ambience fadeout 1.0
        scene bg nightclub with dissolve
        play music nightclub fadein 1.0
        if nightclubintro == 0:
            $ nightclubintro = 1
            $ dawnvisit += 1
            "Well, I wasn’t exactly planning on visiting a nightclub tonight, but here we go!"
            "Lots of people drinking, dancing and having an overall great time."
            "Yep, this is a nightclub alright. It’s not particularly different from what I’ve seen in my own world."
            "Although I’d bet that everyone here came with friends, I must look pretty lonely."
            show dawn dresshorny with dissolve
            dawnunknown "Ooohhh, what do we have here? Another scrumptious young plaything straight out of life and into my club?"
            show dawn dresslaughing with dissolve
            dawnunknown "Mmm… you smell new, little boy, like fabric softener dew on freshly mowed Astroturf."
            show dawn dresshorny with dissolve
            dawnunknown "Oh, I’m not frightening you, am I, duckling?"
            "I think I’m supposed to say ‘frightening isn’t the word I’d use… exciting is more like it.'"
            "That aside, what is this girl wearing? Out of every single person in the entire club, her dress is what stood out to me the most. She probably caught me staring."
            mc "Hey, did you just say this is your club? It’s really nice."
            show dawn dresshappy with dissolve
            dawnunknown "Fantastic work, detective kitten. You’ve stumbled upon my den of debauchery. The word ‘sin’ means nothing here."
            dawnunknown "Is there anything else you’d like to investigate? Perhaps you’re more of a ‘private’ investigator… I could show you some truly criminal acts…"
            "Woah, she’s intense…"
            menu:
                "Uhm, it's nice to meet you too.":
                    pass
                "I can tell you and I are going to get along.":
                    show dawn dresshorny with dissolve
                    dawnunknown "Ohh, I’d just love to see what trouble we could get into together. Believe it or not, I’m a good girl, but for you, I could be really, really bad…"
                "If the acts are criminal, then surely I’ll need some handcuffs.":
                    show dawn dresshorny with dissolve
                    dawnunknown "Mmmheheh… If you keep talking like that, you’ll make me drip, sweetheart. But kitten, you misunderstand my intentions, the handcuffs would be for you."

            show dawn dresslaughing with dissolve
            dawnunknown "What’s your name, duckling? It’s not every day such a striking and handsome new face wanders onto my web."
            menu:
                "[playername], what’s your name?":
                    pass
                "[playername] is what you’ll want to moan.":
                    show dawn dresshorny with dissolve
                    dawnunknown "My, my, and I’m supposing you’ll want to know what to moan next? I like it when a man is vocal in bed, so remember this well…"
                "Names are fleeting, you can keep calling me kitten.":
                    show dawn dresshorny with dissolve
                    dawnunknown "Ahh? Very well, kitten. Your obedience is making me somewhat gooey inside, or is that gooey outside? Perhaps I’ll have you check, mmmhehe."
            show dawn dresshappy with dissolve
            dawn "I am Dawn. But I foresee us getting to know each other a lot more after the sun has set."
            show dawn dresshorny with dissolve
            dawn "This little bed of chaos is mine, and while I’d love to introduce myself to each faucet of your body, I have business to attend to."
            show dawn dresssatisfied with dissolve
            dawn "But I haven’t finished sinking my teeth into you yet, be sure to think of me tonight."
            hide dawn with dissolve
            "She winks before catwalking away, even though she’s the most dressed in the entire room, right now she’s easily the sexiest…"
            "Hmm… Damn, I’m pretty horny right now. Maybe I should try and pick someone up from the nightclub."
            "Let’s see here…"
        $ rand = renpy.random.randint(1,3)
        menu nightclubmenu:
            "There are plenty of sexy ladies here. But partying ain't cheap, if I'm going to spend time here, I'll be buying drinks."
            "Pink and Yellow Mares (-10 Monies)" if ariflirtcounter >= 1 and monies >= 10 and agathasoniathreesome == 0 and rand < 3:
                $ monies -= 10
                jump agathasoniathreesome
            "Agatha and Sonia (-10 Monies)" if arisex == 1 and monies >= 10 and rand > 1:
                $ monies -= 10
                jump agathasoniathreesome
            "Honeycrisp and Ruby (-10 Monies)" if boutiquevisit2 == 1 and farmvisits >= 4 and monies >= 10 and rand < 3:
                $ monies -= 10
                jump honeycrisprubythreesome
            "Mare with Pink Hair (-10 Monies)" if monies >= 10 and rand > 1 and sofiasex == 0:
                $ monies -= 10
                jump sofiasex
            "Sofia  (Free)" if rand > 1 and sofiasex == 1:
                jump sofiasex
            "Dawn (Free)" if dawnltr >= 1:
                jump dawntalksex
            "Leave (No Refunds!)":
                stop music fadeout 1.0
                play ambience ambiencenight fadein 2.0
                jump nightcity

        jump citymenu

        label agathasoniathreesome:
            if agathasoniathreesome == 1:
                jump agathasoniathreesome2
            $ agathasoniathreesome = 1
            "Ah, I recognize those two girls. A yellow mare, and a pink mare dancing about ten feet away from me."
            "I have their flirty glares burned into my retinas. They’re friends of that merchant, Ari."
            "Uhhmm… Sonia and Agatha, right?"
            "Approaching two girls... it’s immensely intimidating…"
            "Alright! I’ll buy a drink first. If I get a little inebriated, I’ll have more courage."
            "I wander up to the bar and order their most alcoholic drink. ‘Blue Magic’, three shots of Vodka and it’s uh, really blue!"
            "The bar is pretty crowded, and it only gets more crowded as two ladies sidle up beside me."
            "E-Eh?!"
            show agatha neutral with dissolve:
                xpos 300
                ypos 30
            agatha "Oh? Sorry love."
            mc "Ahh, uhh... It-It's okay!"
            show agatha happy with dissolve
            agatha "Oh? You seem surprised, do I know you from some- OH!"
            show sonia happy with dissolve:
                xpos 700
                ypos 30
            sonia "Ohmigosh, it’s the guy that was eating ice cream with Moxie! Ahaha, funny bumping into you here."
            mc "Ahh, you ladies know Moxie? She and I are good friends."
            show agatha horny with dissolve
            agatha "Heh, we know of Moxie. She’s often performing when we visit the market."
            show sonia neutral with dissolve
            sonia "Yup, and she aaaallllwaaayyss says her name outloud! The fantastical and amazing Moxie, or sumthin'! Hehehe."
            "This is my chance! The ice is broken! Moxie, holy shit, you are the best wingwoman!"
            mc "Ladies, would you like a drink?"
            show agatha neutral with dissolve
            sonia "Oohhh? Woah… I like a man that’s forward."
            show sonia horny with dissolve
            agatha "Both of us? I see… he’s that kind of man, we’ll need a blue magic each then, right Sonia?"
            show agatha horny with dissolve
            sonia "Mhm, mhm! This calls for advanced intoxication!"
            "Huh? Have I accidentally performed some kind of unspoken ritual by asking that?"
            mc "Uhm, three ‘Blue Magics’ please…"
            stop music fadeout 3.0
            scene bg black with dissolve
            "…"
            "Three hours later..."
            "Woah… I wasn’t expecting this… Well, maybe a little."
            play music sex1 fadein 3.0
            show agathasoniab sex
            show agathasonia sex1
            with dissolve
            "The two girls drunkenly fumble onto the bed together and start making out, their breasts squishing together as their desire for intimacy surpasses any eloquence the mares once had."
            "God damn, Agatha has a voluptuous ass, I’ve been eyeing it up all night."
            "And Sonia’s pussy is so plump and juicy, I can only imagine how amazing my cock would feel inside her."
            "So… This is why they wanted to get extra drunk. When I asked them if they {i}both{/i} wanted to drink, they presumed I was trying to hook up with both of them simultaneously."
            "From the moment we started mingling, their intentions with me became obvious. It’s as if I had sealed my fate from the moment I asked about that drink…"
            show agathasonia sex2 with dissolve
            agatha "Ohhh baby, my pussy is so wet and ready for that cock… I was simply throbbing on the walk home, please tease me no more…"
            sonia "Mm… But I’m really horny too…"
            agatha "Wait your turn, pest!"
            "Agatha flicks her tail to the side and graciously presents her butt with a wiggle."
            "From where I am, the two glistening pussies are overwhelmingly enticing. The alcohol swimming in my brain prevents me from looking away."
            "Unable to wait, I stumble towards the most easily accessible fuckable object. Ultimately prodding the tip of my cock against Agatha’s juicy labia."
            "She coos and grinds up and down on my shaft, making it harder for me to actually insert it in my drunken state."
            play sound cum
            show agathasonia sex3 with dissolve
            play ambience sex fadein 3.0
            "Ah- I find the entrance and slide into her slick warm insides with ease, grabbing on to her ass to stabilise myself before I begin to pound away."
            agatha "Oohh, oooohhhh! You really were a grow’er, not a show’er! Ahhaahh…"
            mc "H-Hey! Das rude, I’ve got a big dick!"
            agatha "Ahh-ahh-ahhhh! That’s what I just said, dummy!"
            sonia "Hehe, you’re talking too much Agi."
            show agathasonia sex4 with dissolve
            "Sonia surprises Agatha with a deep kiss. Agi’s ass begins to sway back and forth in tandem with my thrusts, she clearly wants more."
            "The two mares begin a long, drawn-out kiss while I grab Agatha’s hips and start ramming my cock repeatedly into the quivering mare."
            "I fuck her hard and fast, it’s very hard to focus on anything other than trying to get as much raw pleasure as possible. I’m eager to get both of these horny girls squirting for me."
            "The girls get increasingly touchy with each other as their hands caress anything they can get a hold of."
            "Sonia occasionally squeezing and spreading Agi’s amazing ass, while Agi rubs Sonia’s puffy pussy."
            show agathasonia sex3 with dissolve
            agatha "Ahhh, you’re gonna make me come! Rub my clit, Sonia! Ahh."
            sonia "Ah- I can’t reach, dumbass!"
            "Sonia instead teases her sensitive nipples, as Agi’s hips buck faster; her moans becoming louder and almost squeaky."
            "She finally achieves orgasm as her pussy begins to contract around each inch of my shaft, and with her thighs together like this, Agi’s pussy feels amazingly tight."
            "With my pleasure instincts taking over, I double my efforts and pound her so much she can’t even hold herself up and falls into Sonia."
            agatha "Ayyyahhhh! S-Such intensity, aaaaaahhh! I’ll let you cum in me, so fill me up, you sexy bastard!"
            "She almost drools between gasps and moans, too drunk on orgasmic pleasure to care. It doesn’t help that Sonia finally has an angle to reach down and start rubbing her clit."
            "Agatha, the poor girl, can barely handle the pleasure she’s receiving right now. With increasing tightness around my cock, I can feel my own potent orgasm bubbling, rising…"
            "The need to cum is almost overpowering as my balls quake, my cock bulges, and…"
            play sound cum
            show agathasonia sex5 with cum
            play sound cum
            show agathasonia sex5 with cum
            "Finally like a pressurized tank being released, my cock ejaculates many thick loads of hot cum into the pink mare."
            play sound cum
            show agathasonia sex5 with cum
            play sound cum
            show agathasonia sex5 with cum
            agatha "Oh gods, yes! Give it to me! Ahh aahhh!"
            "My cum plasters and paints her insides, but also oozes out recklessly as I continually fuck her squirming body."
            show agathasonia sex6 with dissolve
            "She eventually goes lax as her climax subsides, and I find myself pulling out around the same time. Each of us completely satisfied as we snuggle together."
            stop music fadeout 1.0
            stop ambience fadeout 1.0
            scene bg black with dissolve
            "..."
            sonia "Uhm… Hello? Aren’t you forgetting something?"
            "..."
            sonia "Guys? Don't fall asleep on me!"
            "..."
            play music sex1 fadein 3.0
            agatha "Sheesh... You're so needy. Fine."
            "It took us a while to recover, but Agatha and I were still horny and rearing to go; I pounded Sonia's plump pussy while Agatha sat on her face."
            play sound cum
            show agathasoniab sex
            show agathasonia sex7
            with cum
            play sound cum
            show agathasonia sex7 with cum
            stop music fadeout 3.0
            "After three more well enjoyed orgasms, we slept like a bundle of rocks."
            scene bg black with dissolve
            "By the time it was morning, I only vaguely remembered the events."
            "Sonia wanted to have some morning sex, but there wasn’t enough time since the ladies had to get ready for work. Instead they gave me their contact info in case I ever wanted to have some more fun."
            "They often visit the nightclub too in case I ever catch them in there."
            "…"
            jump altmorning
        label agathasoniathreesome2:
                "I spy Agatha and Sonia... Although, now I know that they're sisters..."
                "Sisters that made out, caressed each other's breasts, rubbed their pussies."
                "Agatha even sat on Sonia's face!"
                "Am I a bad influence, or is it --"
                show agatha neutral with dissolve:
                    xpos 300
                    ypos 30
                agatha "Fooouunnd yoouuu..."
                show sonia happy with dissolve:
                    xpos 700
                    ypos 30
                sonia "Wanna hang out again? Last time was so much fun!"
                "... It's them, they're the ones out of touch."
                mc "Ahh, uhh... Okay!"
                stop music fadeout 3.0
                scene bg black with dissolve
                "…"
                "Three hours later..."
                "This again... I wonder if they'd fuck each other if I wasn't here..."
                play music sex1 fadein 3.0
                show agathasoniab sex
                show agathasonia sex1
                with dissolve
                "The two girls drunkenly fumble onto the bed together and start making out, their breasts squishing together as their desire for intimacy surpasses any eloquence the mares once had."
                "God damn, Agatha has a voluptuous ass, I’ve been eyeing it up all night."
                "And Sonia’s pussy is so plump and juicy, I can only imagine how amazing my cock would feel inside her."
                "No wonder they want to fuck each other, they're so hot..."
                "From the moment we started mingling, their intentions with me became obvious. It’s as if I had sealed my fate from the moment I said I'd hang out with them…"
                show agathasonia sex2 with dissolve
                agatha "Ohhh baby, my pussy is so wet and ready for that cock… I was simply throbbing on the walk home, please tease me no more…"
                sonia "Mm… But I’m really horny too…"
                agatha "Wait your turn, pest!"
                "Agatha flicks her tail to the side and graciously presents her butt with a wiggle."
                "From where I am, the two glistening pussies are overwhelmingly enticing. The alcohol swimming in my brain prevents me from looking away."
                "Unable to wait, I stumble towards the most easily accessible fuckable object. Ultimately prodding the tip of my cock against Agatha’s juicy labia."
                "She coos and grinds up and down on my shaft, making it harder for me to actually insert it in my drunken state."
                play sound cum
                show agathasonia sex3 with dissolve
                play ambience sex fadein 3.0
                "Ah- I find the entrance and slide into her slick warm insides with ease, grabbing on to her ass to stabilise myself before I begin to pound away."
                agatha "Oohh, oooohhhh! Such a good cock. Ooohh yes!"
                show agathasonia sex4 with dissolve
                "Sonia surprises Agatha with a deep kiss. Agi’s ass begins to sway back and forth in tandem with my thrusts, she clearly wants more."
                "The two sisters begin a long, drawn-out kiss while I grab Agatha’s hips and start ramming my cock repeatedly into the quivering mare."
                "I fuck her hard and fast, it’s very hard to focus on anything other than trying to get as much raw pleasure as possible. I’m eager to get both of these horny girls squirting for me."
                "The sisters get increasingly touchy with each other as their hands caress anything they can get a hold of."
                "Sonia occasionally squeezing and spreading Agi’s amazing ass, while Agi rubs Sonia’s puffy pussy."
                "I pay a little more attention than the first time... Their movements, and comfort in performing those actions, implies a sexual history between these two..."
                "Or I'm overthinking. Either way, it's fucking hot."
                show agathasonia sex3 with dissolve
                agatha "Ahhh, you’re gonna make me come! Rub my clit, Sonia! Ahh."
                sonia "Ah- I can’t reach, dumbass!"
                "Sonia instead teases her sensitive nipples, as Agi’s hips buck faster; her moans becoming louder and almost squeaky."
                "She finally achieves orgasm as her pussy begins to contract around each inch of my shaft, and with her thighs together like this, Agi’s pussy feels amazingly tight."
                "With my pleasure instincts taking over, I double my efforts and pound her so much she can’t even hold herself up and falls into Sonia."
                agatha "Ayyyahhhh! S-Such intensity, aaaaaahhh! I’ll let you cum in me, so fill me up, you sexy bastard!"
                "She almost drools between gasps and moans, too drunk on orgasmic pleasure to care. It doesn’t help that Sonia finally has an angle to reach down and start rubbing her clit."
                "Agatha, the poor girl, can barely handle the pleasure she’s receiving right now. With increasing tightness around my cock, I can feel my own potent orgasm bubbling, rising…"
                "The need to cum is almost overpowering as my balls quake, my cock bulges, and…"
                play sound cum
                show agathasonia sex5 with cum
                play sound cum
                show agathasonia sex5 with cum
                "Finally like a pressurized tank being released, my cock ejaculates many thick loads of hot cum into the pink mare."
                play sound cum
                show agathasonia sex5 with cum
                play sound cum
                show agathasonia sex5 with cum
                agatha "Oh gods, yes! Give it to me! Ahh aahhh!"
                "My cum plasters and paints her insides, but also oozes out recklessly as I continually fuck her squirming body."
                show agathasonia sex6 with dissolve
                "She eventually goes lax as her climax subsides, and I find myself pulling out around the same time. Each of us completely satisfied as we snuggle together."
                stop ambience fadeout 1.0
                "It took us a while to recover, but Agatha and I were still horny and rearing to go; I pounded Sonia's plump pussy while Agatha sat on her face."
                play sound cum
                show agathasonia sex7
                with cum
                play sound cum
                show agathasonia sex7 with cum
                stop music fadeout 3.0
                "After three more well enjoyed orgasms, we slept like a bundle of rocks."
                scene bg black with dissolve
                play ambience ambienceday fadein 3.0
                "By the time it was morning..."
                show arib sex
                show ari sex1
                with s
                "Huh?!"
                "How'd I end up here?"
                ari "Good morning..."
                mc "Uhh... Wha...?"
                ari "Thanks for sleeping with me too last night. It was nice to be considered amongst my sisters for once."
                "Oh god, I don't remember fucking Ari at all."
                mc "Uhm, could you jog my memory? I have some morning brain fog."
                ari "Oh? I saw you stumbling around looking for the bathroom, then you took me right there in the hallway."
                ari "It was very hot."
                mc "I... see..."
                "I gotta say, I'm impressed drunk me had the stamina. Kudos."
                scene bg black with dissolve
                "After talking with Ari to trace back my memories, I returned home."
                jump altmorning
        label honeycrisprubythreesome:
            if honeyrubythreesome == 1:
                jump honeyrubythreesome2
            $ honeyrubythreesome = 1
            "Is that…? It is! It’s Honey and Ruby talking in a corner together."
            "Having all these girls crowded in one room really shows you how tall and well-built Honey is. I wonder if she’s popular with the ladies."
            "They’re on the other side of the room, and as I approach, something takes me off guard."
            "Hah, they started making out, tongues and all!"
            "Oh, and there goes Ruby’s thigh wrapping around Honey…"
            "I feel a bit awkward watching here on the side."
            "I should probably leave these girls to it- "
            "A glimmer shines in Ruby’s eye, as she briefly opens them amidst the French kiss, and spots me."
            "Not breaking the kiss for a second, Ruby gives me a come-hither hand gesture. It’s captivating enough to make me forget I was ever planning on leaving."
            "And so, I close the distance between the girls."
            show honeycrisp nchorny with dissolve:
                xpos 300
                ypos 10
            show ruby horny with dissolve:
                xpos 600
                ypos 45
            mc "Room for one more?"
            show ruby laughing with dissolve
            ruby "Heh, as if my clit needed any more reason to tingle."
            show honeycrisp nchappy with dissolve
            honeycrisp "Well I’ll be, [playername]! How’s it going, ya stud?"
            mc "I’m great tha- ah?! Mmphh-"
            show ruby closelaughing with dissolve:
                xpos 600
                ypos 85
            "Ruby cuts me off with a French kiss."
            show honeycrisp nclaughing with dissolve
            honeycrisp "Yep, there’s room for one more. This night just got a lot more fun."
            ruby "Mmphh, mmm… Darling… Mmphmm... mmm…"
            "Holy crap, she’s really drunk, and really horny."
            show ruby horny with dissolve:
                xpos 600
                ypos 45
            ruby "Let me buy you a drink darling, it’s the least I can do after everything you’ve done for us."
            mc "Bribing me already? Alright, I’ll stick around with you two tonight."
            ruby "Don't disappear on me, both of you! Haha."
            hide ruby with dissolve
            mc "You'd have to actively bribe me to make me leave after what Ruby just did."
            show honeycrisp nchappy with dissolve
            honeycrisp "That’s the spirit. With the three of us, it’ll be a great time guaranteed."
            honeycrisp "And I enjoy the opportunity to not use my strap-on too."
            mc "Oh? Is that how you’ve been rutting Ruby?"
            show honeycrisp nchorny with dissolve
            honeycrisp "Sure do, I’ve been pounding her for longer than I remember."
            "Woooow... Honeycrisp is not usually {i}this{/i} forthcoming. I guess she's pretty drunk too."
            show honeycrisp nchappy with dissolve
            honeycrisp "Heh, you’re making me nostalgic. I remember the first time… Me and Ruby didn’t see eye to eye at first, since we come from such different backgrounds."
            mc "Oh yeah? I can see that, a farmer gal and a more pampered boutique owner."
            show honeycrisp nclaughing with dissolve
            honeycrisp "Heh, yeah, that’s right! It was Lily that made us have a sleepover to try and rekindle a friendship."
            show honeycrisp ncneutral with dissolve
            honeycrisp "The library only has two bedrooms though, so both Ruby and I had to use Penelope’s. That was before Penelope moved 'ere!"
            mc "And I’m assuming you shared a bed? How’d you go from not seeing eye to eye to fuckin’ so fast?"
            show honeycrisp nchappy with dissolve
            honeycrisp "Well… We’d been arguing all day, we really didn’t get along. The tension was at its peak during the evening."
            honeycrisp "Lily felt defeated, she tried everything she could to get us to play nice. Bless ‘er."
            show honeycrisp nclaughing with dissolve
            honeycrisp "But for some reason, as soon as we got into bed together… Something clicked."
            mc "… Wha?! But it sounds like you didn’t like each other at all."
            show honeycrisp nchappy with dissolve
            honeycrisp "Lily had the same reaction."
            show honeycrisp nchorny with dissolve
            honeycrisp "It certainly felt spontaneous, but later we realized the symptoms that lead to it."
            honeycrisp "Ruby is pretty submissive. While we were arguing, she was getting somewhat aroused... That's just the type of gal she is, aha!"
            mc "Yeah, that does sound like her… Even though she’s a pampered gal, she has some serious sexual urges."
            show honeycrisp nchappy with dissolve
            honeycrisp "Mhm, she loves to be degraded and dominated. Who better to do that than her opposite, the farmer gal?"
            show honeycrisp nclaughing with dissolve
            honeycrisp "And me? Well, I ain’t gonna play with ya. I like my girls, and it’s no secret that I think Rube’s is a beauty."
            show honeycrisp ncangry with dissolve
            honeycrisp "But not just any beauty… When she argued with me, I saw a challenge to be conquered…"
            honeycrisp "I wanted her to submit to me. I wanted the irate girl that kept challenging with me to finally submit, and what better way than sexually?"
            honeycrisp "It was only a fantasy at the time, little did I know that she felt the same way… A part of her may have been trying to rile me up for that exact purpose."
            show honeycrisp nchorny with dissolve
            honeycrisp "On that night when we had to share a bed, we finally had some quiet, some intimacy."
            honeycrisp "In truth, she had refused to talk to me. I don’t remember why; it was after an argument about something that probably didn’t matter."
            show honeycrisp nchappy with dissolve
            honeycrisp "She got into bed first… And in that vulnerable state, I saw her differently..."
            honeycrisp "I saw a serene beauty lying in bed, her hair slightly messy, her nipples erect, thighs rubbing slightly."
            show honeycrisp nchorny with dissolve
            honeycrisp "I got into bed beside her, staring eye to eye... And as natural as it could be, my hand found its way onto her thigh."
            honeycrisp "She welcomed the touch... Her breathing quickened, her expression lustful, her legs gently opening..."
            honeycrisp "Then the next thing either of us knew, that hand was between her legs, and our lips were locked in a kiss."
            honeycrisp "At that moment, we dropped all ego and finally understood each other."
            show honeycrisp nclaughing with dissolve
            honeycrisp "And all that ‘tension’, well… Turns out, it could be released as sexual tension."
            show ruby horny with dissolve:
                xpos 600
                ypos 45
            ruby "Talking about our first, darling? *Giggle* I remember in the morning, Lily was so shocked that we were getting along. Hehe, we never did tell her what happened, did we Honey?"
            show honeycrisp nchappy with dissolve
            honeycrisp "Ahh, hey Rubes. I guess we didn’t. But we’ve been doing this for so long now, I bet a smart girl like her can figure it out."
            "Ruby hands me my drink and winks."
            mc "What a great story, you two make a cute cou- ohh… Uhh, thanks for the drink."
            "That’s right… They’re not a couple… I wonder why?"
            show ruby laughing with dissolve
            ruby "Cute coup, hm? Or maybe 'couple'?"
            show honeycrisp nclaughing with dissolve
            honeycrisp "Heh, we’re just friends."
            show ruby happy with dissolve
            ruby "I don’t think I’m ready to settle, but perhaps one day."
            show honeycrisp nchorny with dissolve
            honeycrisp "Hard to say, there’s so much fun to be had in the world, and only so much time to experience it all."
            "Honey sips her drink. I think I realized the problem; she’s stuck between two girls. Anna and Ruby."
            "She doesn’t want to disappoint either of them, so she’s balancing them both as friends with benefits… I wouldn’t want to be in her shoes when one of them puts their foot down."
            show ruby horny with dissolve
            ruby "Well darlings, I want to experience both of you tonight. Show me what you’ve got."
            show honeycrisp nchappy with dissolve
            honeycrisp "Drink up, [playername]. It’ll be a long night."
            stop music fadeout 3.0
            scene bg black with dissolve
            "…"
            "We had some drinks, we danced… It’s a bit of a blur…"
            "But for some reason, I’m really conscious right now… I can probably figure out why too."
            play music sex1 fadein 3.0
            show honeyrubyb spanking
            show honeyruby spanking1
            with dissolve
            play sound spank
            ruby "Fuck yes, darling! Ahh, spank me harder! Ahhh!"
            honeycrisp "I gotta teach y’all some manners. Inviting me clubbing, only to make out with [playername] right in front of me, aha!"
            honeycrisp "And yer in big trouble now mah spankin' hand has healed up!"
            ruby "How did I ever go those months without your touch? Hehe."
            play sound spank
            "The three of us were all on bed a moment ago, fondling each other and making out."
            "As Ruby and I were making out, she was giving me a handjob. But before we could go any further, she was almost stolen away by Honey who began to discipline her with some butt rippling spanks."
            "Even now, lust utterly emanates from Ruby. She not only sticks her ass out, but her pussy is also purposely presented, oozing with almost excessive wetness."
            play sound spank
            honeycrisp "Y’all such a naughty slut that you need two people to satisfy ya, eh?"
            ruby "Y-Yeah! I’m a nasty slut! *Giggle* Ahh, ahhh!"
            play sound spank
            "Between spanks, Honey uses her finger and thumb to tease and squish Ruby’s vulva and clit."
            "She’s clearly extremely sensitive, her entire body spasms and moans escape her mouth, while Honey’s thumb plays her like an instrument."
            "I noticed Ruby keeps looking back at something, and then it clicks. She’s staring at my cock, which I had been nonchalantly jerking while watching. Perhaps it’s time for me to get involved."
            "I stand up and stroke the side of Ruby’s plump ass. Perched on Honey’s knees, she’s actually the perfect height for me to fuck right now."
            show honeyruby spanking2 with dissolve
            honeycrisp "Good idea Stud, let’s give this slut more than she bargained for, eh? Haha."
            ruby "Yeeesss, pleeeaasee! *Wiggle, wiggle*"
            "Her plump, puffy labia looks so perfect from this angle, it even squishes and indents as I poke my cock at her teasingly."
            "The view gets even better as Honey smirks and uses two fingers to part the petals of her flower with an audible ‘schlick’."
            menu:
                "Vaginal":
                    "Her pussy is so enticing, it’s so pristine and seemingly perfect. I’ve been thinking about it ever since she first made out with me in the club."
                    "Eager to dive in, I prod the tip against her vaginal entrance, slowly and teasingly. She’s so wet that the simple action of rubbing up and down against her wet vulva coats my glans in her slick lubricants."
                    play sound cum
                    show honeyruby spankingv1 with dissolve
                    "I can’t tease myself anymore. I push forward, my hips easily meeting her butt in a single, perhaps overly enthusiastic thrust."
                    ruby "Ohhh, f-fuck… I needed that, ahh…"
                    honeycrisp "I bet; you’ve been dripping since we got into the club. Such a slutty mare."
                    play ambience sex fadein 3.0
                    "I pull back and thrust back into Ruby’s plump pussy, as usual she tenses her internal muscles to increase the feeling on my cock."
                    "And as if that wasn’t enough already, Honey raises her hand, and… *Spank!* Her internal muscles clench around my cock, intensifying the pleasure."
                    ruby "Ooftt, go easy on me, darling!"
                    mc "So, she gets tighter when she’s spanked… Interesting."
                    play sound spank
                    honeycrisp "Oh, yeah? Let’s try that again! *Spank*"
                    play sound spank
                    "As Honeycrisp spanks Ruby’s ass, her pussy tightens around my shaft again as I thrust in."
                    "The sudden squeeze upon each spank is dangerously pleasureful, she tightens around all the most sensitive areas of my glans, I feel like if I let my guard down I could immediately cum."
                    show honeyruby spankingv2 with dissolve
                    ruby "Oohhh… This feels so fucking good…"
                    honeycrisp "Y’all haven’t seen anything yet… Let’s see how you handle this…"
                    "With a thumb, Honey teases at Ruby’s clit. At roughly the same time, I pull back and thrust back in, causing Ruby to squeak."
                    ruby "Eep! Ahh, ahhhh… T-Th-That’s fucking ah-mazing! Harder, fuck harder!"
                    mc "With pleasure."
                    "Starting with a brisk pace, I fuck Ruby while she lays on the knees of one of her best friends. Can’t say I woke up this morning expecting this."
                    play sound spank
                    "*Spank* Honey has all reign over Ruby’s body, she can tease her breasts, she can toy with her ass, she can play with her clit."
                    "And Honey takes full advantage of this, Ruby has been merely reduced to a toy."
                    "Not only that, but Honey acts as somewhat of a voyeur to the act of being fucked, feeding deeply into Ruby’s own aberrant fetishes."
                    play sound spank
                    "With each spank, or tease, I can feel Ruby’s nethers tighten and tense around my member. Adding more and more to the already intense pleasure."
                    "I have to actively concentrate to not let my orgasm prematurely escape, however, as Honey keeps focusing on the clit, it would seem Ruby’s already getting pretty close to hers."
                    ruby "Ahh, ahhhh… Oohh, fuck me! Ahhaaaaaaiiee! Kyaaahhh!"
                    "As Ruby starts to orgasm, her entrance tightens around my shaft, intensifying the pleasure and signalling to me that I can let my guard down and fill this mare up with cum."
                    "Gripping tightly on to her fluffy butt for leverage, I start to pound her almost recklessly as I surge forward towards an explosive orgasm."
                    ruby "Ahh, ahh- ahh- ahhh! Yes, yes, fuck me, fuck!"
                    honeycrisp "Hell yeah, partner! Fill ‘er up!"
                    "I can’t hold back any longer!"
                    play sound cum
                    show honeyruby spankingv3 with cum
                    play sound cum
                    show honeyruby spankingv3 with cum
                    "My orgasm erupts, huge loads of thick cum splatter her pussy whilst I maintain my vigorous pace throughout."
                    play sound cum
                    show honeyruby spankingv3 with cum
                    play sound cum
                    show honeyruby spankingv3 with cum
                    stop ambience fadeout 3.0
                    "Pulling out briefly near the end, I ice her butt with a few last blasts of jism."
                    "Ruby is utterly out of breath, but absolutely satisfied as cum drips from her sloppy pussy, no longer looking as pretty and pristine as ten minutes prior."
                    show honeyruby spankingcum with dissolve
                    honeycrisp "Mmm, that was hot!"
                    ruby "Ahh… I hope Melody didn’t hear me, I got really loud…"
                    "She totally heard us…"
                "Anal":
                    "But I have an even better idea… I’ve been eyeing up that cute tight pucker for a while. It’s so pristine and seemingly perfect."
                    "I prod my tip against her vaginal entrance, assisted by Honey as I collect a generous amount of lubrication."
                    "And then I pull her slightly closer towards me, hence lowering her anus to the level of my cock."
                    "Honey giggles, immediately our plans align as the two fingers she had been using to spread her pussy move up to spread her pucker."
                    ruby "Ohhh, f-fuck… I’ve never done it in there with a guy before… Only buttplugs."
                    honeycrisp "First time for everything, eh? Maybe you can take my anal virginity too, hah."
                    play sound cum
                    show honeyruby spankinga1 with dissolve
                    "Honey unceremoniously drools onto the slightly spread pucker, that combined with the slick pussy juices, my dick inserts almost immediately into the anus."
                    "I grit my teeth as I push inwards, her ass slowly sucking and squeezing in my throbbing member."
                    ruby "Ooftt, go easy on me, darling!"
                    play sound spank
                    honeycrisp "Or… not! Aha! *Spank*"
                    "As Honeycrisp spanks Ruby’s ass, her pucker tightens around my shaft while I’m pushing in, almost locking me in place."
                    "So, she gets tighter when she’s spanked… Interesting."
                    "I push forward until I’m fully hilted, and I wait to allow Ruby to adjust to my girth. The near painful tightness of her ass slowly easing."
                    ruby "Oohhh… It feels so different…"
                    honeycrisp "Don’t worry Rubes, I’m not going to let your clit get lonely."
                    play ambience sex fadein 3.0
                    "With a thumb, Honey teases at Ruby’s clit. At roughly the same time, I pull back and thrust back in, causing Ruby to squeak."
                    show honeyruby spankinga2 with dissolve
                    ruby "Eep! Ahh, ahhhh… T-That’s good, you can go harder…"
                    mc "With pleasure."
                    "Starting with a gentle pace, I fuck Ruby’s virgin asshole while she lays on the knees of one of her best friends. Can’t say I woke up this morning expecting this."
                    play sound spank
                    "*Spank* Honey has all reign over Ruby’s body, she can tease her breasts, she can toy with her ass, she can play with her clit."
                    "And Honey takes full advantage of this, Ruby has been merely reduced to a toy."
                    "Not only that, but Honey acts as somewhat of a voyeur to the act of being fucked, feeding deeply into Ruby’s own aberrant fetishes."
                    play sound spank
                    "With each spank, or tease, I can feel Ruby’s anus tighten and tense around my member. Adding more and more to the already intense pleasure."
                    "I have to actively concentrate to not let my orgasm prematurely escape, however, as Honey keeps focusing on the clit, it would seem Ruby’s already getting pretty close to hers."
                    ruby "Ahh, ahhhh… Oohh, fuck me! Ahhaaaaaaiiee! Kyaaahhh!"
                    "As Ruby starts to orgasm, her pucker tightens around my shaft, intensifying the pleasure and signalling to me that I can let my guard down and fill this mare up with cum."
                    "Gripping tightly on to her fluffy butt for leverage, I start to pound her ass almost recklessly as I surge forward towards an explosive orgasm."
                    ruby "Ahh, ahh- ahh- ahhh! Yes, yes, fuck me, fuck!"
                    honeycrisp "Hell yeah, partner! Fill ‘er up!"
                    "I can’t hold back any longer!"
                    play sound cum
                    show honeyruby spankinga3 with cum
                    play sound cum
                    show honeyruby spankinga3 with cum
                    "My orgasm erupts, huge loads of thick cum splatter her ass whilst I maintain my vigorous pace throughout."
                    play sound cum
                    show honeyruby spankinga3 with cum
                    play sound cum
                    show honeyruby spankinga3 with cum
                    stop ambience fadeout 3.0
                    "Pulling out briefly near the end, I ice her ass with a few last blasts of jism."
                    "Ruby is utterly out of breath, but absolutely satisfied as cum drips from her used pucker."
                    show honeyruby spankingcum with dissolve
                    honeycrisp "Mmm, that was hot!"
                    ruby "Ahh… I hope Melody didn’t hear me, I got really loud…"
                    "She totally heard us…"
            stop music fadeout 3.0
            honeycrisp "My turn. Stud, your dick may be out of commission, but put that tongue to good use. I want you both between my legs."
            "Eh?! I wasn’t expecting to be the submissive one tonight!"
            "But Honey is just far too dominant!"
            scene bg black with dissolve
            "The three of us love each other long into the early hours of the morning, I don’t even remember how it ended."
            "The three of us just sorta passed out in a writhe of limbs and lewdity."
            "In the morning..."
            scene bg rubybedroom with dissolve
            "Honey is the first to wake up, and her movements stir both Ruby and I."
            "After a short and sweet conversation, she kisses us both on the forehead, and heads out early to work at her farm."
            "This leaves Ruby and I to spend the morning cuddling together. Cuddling with a soft mare is the best thing in the world…"
            scene bg boutiquekitchen with dissolve
            "About an hour later, we both wake up. Ruby treats me to some delicious pancakes before I take my leave."
            jump altmorning

            label honeyrubythreesome2:
                "Well, well, well… The devious duo are back at it again."
                "Honeycrisp does have quite an appetite when it comes to her mares, with her regular flings with Anna and Ruby."
                "And of Ruby? I guess she’s just horny for general loving."
                "This time they’re on the dance floor, so I jive my way over and I’m welcomed with a cheer."
                show honeycrisp nchorny with dissolve:
                    xpos 300
                    ypos 10
                show ruby horny with dissolve:
                    xpos 600
                    ypos 35
                honeycrisp "Look who showed up again, you sure are reliable!"
                show ruby laughing with dissolve
                ruby "It’s so nice to see you, darling! You’re the life of the party."
                mc "What can I say, I can’t resist two beautiful mares on the dance floor."
                show honeycrisp nchappy with dissolve
                honeycrisp "Y’all keep him occupied Rubes, I’m going to get stud here a strong drink. Lord knows he needs one to handle you when you’re drunk."
                hide honeycrisp ncwith dissolve
                "Keep me occupied? Uh oh, here she comes, she’s going to make out with me- mmph."
                hide ruby with None
                show ruby closelaughing with dissolve
                ruby "Mmphh, mmm… Mmmphh-aaahh…"
                show ruby closehorny with dissolve
                ruby "Oohh, dearie… Did you get an erection?"
                mc "Ahh... almost... That’s your fault…"
                show ruby closehappy with dissolve
                ruby "It’s okay darling, I can hide that…"
                mc "Huh?"
                show ruby closelaughing with dissolve
                "She closes in for another kiss on the dancefloor, lifting her thigh over me, sliding my shaft between her legs and against something warm, moist."
                ruby "Mm, mmmmpphh… Mmmphh-aaahh…"
                "My erection is certainly hidden between her thighs, but it’ll never go away if she keeps fucking grinding on it!"
                show ruby closehorny with dissolve
                ruby "You should angle it up, slip it in… Hehe…"
                show ruby closelaughing with dissolve
                mc "I know you’re a voyeur, but on the dance floor? That is taking it too far…"
                show ruby closehorny with dissolve
                ruby "How about you let me sit on your lap in the corner over there, then?"
                "She points to a fairly dark corner, just obscure enough for her to actually do what she’s implying discreetly…"
                hide ruby with dissolve
                "I begrudgingly nod, partly because I want to get off the dance floor before anyone notices I have a fucking erection."
                scene bg nightclub2 with dissolve
                play music nightclub2 fadeout 2.0
                "Fortunately, Ruby does a pretty good job of obscuring my crotch with her rear, as she leads me by hand to the seating area."
                show ruby closelaughing with dissolve:
                    xpos 100
                    ypos 85
                "I cover my crotch and sit down, and eloquently Ruby crosses her legs and sits… on my erection!"
                play sound cum
                "*Schlick*, straight to the hilt in a single motion. Like a fuckin' trained professional."
                show ruby closehorny with dissolve
                ruby "Ooohh… I like this, I like this a lot…"
                mc "As long as it’s not obvious…"
                "My cock throbs, it twitches. And it doesn’t help that Ruby purposely tenses her pussy just to tease me."
                show ruby closelaughing with dissolve
                "With her thighs clamped, so leans into my chest and begins to make out with me."
                ruby "Mmphh, ahhh, mmm! Ahhh… Mmphh, mmm…"
                "From a distance, we’d just look like an ordinary couple making out with the girl sat on my lap."
                "Although I guess without clothes it’d be pretty obvious to anyone anatomically informed that I’d have an erection from this."
                show honeycrisp neutral with dissolve:
                    xpos 800
                    ypos 20
                honeycrisp "Well… I couldn’t have gotten that stiff drink to you sooner, [playername]. Y’all might want to down this one."
                mc "No kidding, you were right about needing to be drunk to handle Ruby."
                show ruby closehorny with dissolve
                ruby "Hahh, I-I think I just came…"
                honeycrisp "Come on now Rubes, let’s keep the sex in private."
                show ruby laughing with dissolve:
                    xpos 200
                    ypos 25
                play sound cum
                "She stands up with a schlick, fortunately the two girls are blocking anyone else’s view, so I have at least some discretion while waiting for my erection to go."
                show ruby horny with dissolve
                ruby "It-It’s fine, that was quite a strong orgasm… I think I’ll be able to control myself for at least an hour, hehe…"
                "A strong orgasm? You gotta be kidding me…"
                stop music fadeout 3.0
                scene bg black with dissolve
                "…"
                "We had some drinks, we danced… It’s a bit of a blur…"
                "But for some reason, I’m really conscious right now… I can probably figure out why too."
                play music sex1 fadein 3.0
                scene honeyrubyb spanking
                show honeyruby spanking1
                with dissolve
                ruby "Fuck yes, darling! Ahh, spank me harder! Ahhh!"
                honeycrisp "I gotta teach y’all some manners. Having sex with [playername] in public like that!"
                "The three of us were all on bed a moment ago, fondling each other and making out."
                "As Ruby and I were making out, she was giving me a hand job. But before we could go any further, she was almost stolen away by Honey who began to discipline her with some butt rippling spanks."
                "Even now, lust utterly emanates from Ruby. She not only sticks her ass out, but her pussy is also purposely presented. Oozing with almost excessive wetness."
                honeycrisp "Y’all such a naughty slut that you need two people to satisfy ya, eh?"
                ruby "Y-Yeah! I’m a nasty slut! *Giggle* Ahh, ahhh!"
                "Between spanks, Honey uses her finger and thumb to tease and squish Ruby’s vulva and clit."
                "She’s clearly extremely sensitive, her entire body spasms and moans escape her mouth as Honey’s thumb plays her like an instrument."
                "I noticed Ruby keeps looking back at something, and then it clicks. She’s staring at my cock, which I had been nonchalantly jerking while watching. Perhaps it’s time for me to get involved."
                "I stand up and stroke the side of Ruby’s plump ass. Perched on Honey’s knees, she’s actually the perfect height for me to fuck her right now."
                show honeyruby spanking2 with dissolve
                honeycrisp "Good idea Stud, let’s give this slut more than she bargained for, eh? Haha."
                ruby "Yeeesss, pleeeaasee! *Wiggle, wiggle*"
                "Her plump, puffy labia looks so perfect from this angle, it even squishes and indents as I poke my cock at her teasingly."
                "The view gets even better as Honey smirks and uses two fingers to part the petals of her flower with an audible ‘schlick’."
                menu:
                    "Vaginal":
                        "Her pussy is so enticing, it’s so pristine and seemingly perfect. I’ve been thinking about it ever since she first made out with me in the club."
                        "Eager to dive in, I prod the tip against her vaginal entrance, slowly and teasingly. She’s so wet that the simple action of rubbing up and down against her wet vulva coats my glans in her slick lubricants."
                        play sound cum
                        show honeyruby spankingv1 with dissolve
                        "I can’t tease myself anymore. I push forward, my hips easily meeting her butt in a single, perhaps overly enthusiastic thrust."
                        ruby "Ohhh, f-fuck… I needed that, ahh…"
                        honeycrisp "I bet; you’ve been dripping since we got into the club. Such a slutty mare."
                        play ambience sex fadein 3.0
                        "I pull back and thrust back into Ruby’s plump pussy, as usual she tenses her internal muscles to increase the feeling on my cock."
                        "And as if that wasn’t enough already, Honey raises her hand, and… *Spank!* Her internal muscles clench around my cock, intensifying the pleasure."
                        ruby "Ooftt, go easy on me, darling!"
                        mc "So, she gets tighter when she’s spanked… Interesting."
                        honeycrisp "Oh, yeah? Let’s try that again! *Spank*"
                        "As Honeycrisp spanks Ruby’s ass, her pussy tightens around my shaft again as I thrust in."
                        "The sudden squeeze upon each spank is dangerously pleasureful, she tightens around all the most sensitive areas of my glans, I feel like if I let my guard down I could immediately cum."
                        show honeyruby spankingv2 with dissolve
                        ruby "Oohhh… This feels so fucking good…"
                        honeycrisp "Y’all haven’t seen anything yet… Let’s see how you handle this…"
                        "With a thumb, Honey teases at Ruby’s clit. At roughly the same time, I pull back and thrust back in, causing Ruby to squeak."
                        ruby "Eep! Ahh, ahhhh… T-Th-That’s fucking ah-mazing! Harder, fuck harder!"
                        mc "With pleasure."
                        "Starting with a brisk pace, I fuck Ruby while she lays on the knees of one of her best friends. Can’t say I woke up this morning expecting this."
                        "*Spank* Honey has all reign over Ruby’s body, she can tease her breasts, she can toy with her ass, she can play with her clit."
                        "And Honey takes full advantage of this, Ruby has been merely reduced to a toy."
                        "Not only that, but Honey acts as somewhat of a voyeur to the act of being fucked, feeding deeply into Ruby’s own aberrant fetishes."
                        "With each spank, or tease, I can feel Ruby’s nethers tighten and tense around my member. Adding more and more to the already intense pleasure."
                        "I have to actively concentrate to not let my orgasm prematurely escape, however, as Honey keeps focusing on the clit, it would seem Ruby’s already getting pretty close to hers."
                        ruby "Ahh, ahhhh… Oohh, fuck me! Ahhaaaaaaiiee! Kyaaahhh!"
                        "As Ruby starts to orgasm, her entrance tightens around my shaft, intensifying the pleasure and signalling to me that I can let my guard down and fill this mare up with cum."
                        "Gripping tightly on to her fluffy butt for leverage, I start to pound her almost recklessly as I surge forward towards an explosive orgasm."
                        ruby "Ahh, ahh- ahh- ahhh! Yes, yes, fuck me, fuck!"
                        honeycrisp "Hell yeah, partner! Fill ‘er up!"
                        "I can’t hold back any longer!"
                        play sound cum
                        show honeyruby spankingv3 with cum
                        play sound cum
                        show honeyruby spankingv3 with cum
                        "My orgasm erupts, huge loads of thick cum splatter her pussy whilst I maintain my vigorous pace throughout."
                        play sound cum
                        show honeyruby spankingv3 with cum
                        play sound cum
                        show honeyruby spankingv3 with cum
                        stop ambience fadeout 3.0
                        "Pulling out briefly near the end, I ice her butt with a few last blasts of jism."
                        "Ruby is utterly out of breath, but absolutely satisfied as cum drips from her sloppy pussy, no longer looking as pretty and pristine as ten minutes prior."
                        show honeyruby spankingcum with dissolve
                        honeycrisp "Mmm, that was hot!"
                        ruby "Ahh… I hope Melody didn’t hear me, I got really loud…"
                        "She totally heard us…"

                    "Anal":
                        "But I have an even better idea… I’ve been eyeing up that cute tight pucker for a while. It’s so pristine and seemingly perfect."
                        "I prod my tip against her vaginal entrance, assisted by Honey as I collect a generous amount of lubrication."
                        "And then I pull her slightly closer towards me, hence lowering her anus to the level of my cock."
                        "Honey giggles, immediately our plans align as the two fingers she had been using to spread her pussy move up to spread her pucker."
                        ruby "Ohhh, f-fuck… Are you really going to put it in there?"
                        honeycrisp "I don’t blame him; you have a really cute butthole."
                        ruby "Psshh, shush…"
                        play sound cum
                        show honeyruby spankinga1 with dissolve
                        "Honey unceremoniously drools onto the slightly spread pucker, that combined with the slick pussy juices, my dick inserts almost immediately into the anus."
                        "I grit my teeth as I push inwards, her ass slowly sucking and squeezing in my throbbing member."
                        ruby "Ooftt, go easy on me, darling!"
                        honeycrisp "Or… not! *Spank* Haha!"
                        "As Honeycrisp spanks Ruby’s ass, her pucker tightens around my shaft while I’m pushing in, almost locking me in place."
                        "So, she gets tighter when she’s spanked… Interesting."
                        "I push forward until I’m fully hilted, and I wait to allow Ruby to adjust to my girth. The near painful tightness of her ass slowly easing."
                        show honeyruby spankinga2 with dissolve
                        ruby "Oohhh… It feels so different…"
                        honeycrisp "Don’t worry Rubes, I’m not going to let your clit get lonely."
                        play ambience sex fadein 3.0
                        "With a thumb, Honey teases at Ruby’s clit. At roughly the same time, I pull back and thrust back in, causing Ruby to squeak."
                        ruby "Eep! Ahh, ahhhh… T-That’s good, you can go harder…"
                        mc "With pleasure."
                        "Starting with a gentle pace, I fuck Ruby’s asshole while she lays on the knees of one of her best friends. Can’t say I woke up this morning expecting this."
                        "*Spank* Honey has all reign over Ruby’s body, she can tease her breasts, she can toy with her ass, she can play with her clit."
                        "And Honey takes full advantage of this, Ruby has been merely reduced to a toy."
                        "Not only that, but Honey acts as somewhat of a voyeur to the act of being fucked, feeding deeply into Ruby’s own aberrant fetishes."
                        "With each spank, or tease, I can feel Ruby’s anus tighten and tense around my member. Adding more and more to the already intense pleasure."
                        "I have to actively concentrate to not let my orgasm prematurely escape, however, as Honey keeps focusing on the clit, it would seem Ruby’s already getting pretty close to hers."
                        ruby "Ahh, ahhhh… Oohh, fuck me! Ahhaaaaaaiiee! Kyaaahhh!"
                        "As Ruby starts to orgasm, her pucker tightens around my shaft, intensifying the pleasure and signalling to me that I can let my guard down and fill this mare up with cum."
                        "Gripping tightly on to her fluffy butt for leverage, I start to pound her ass almost recklessly as I surge forward towards an explosive orgasm."
                        ruby "Ahh, ahh- ahh- ahhh! Yes, yes, fuck me, fuck!"
                        honeycrisp "Hell yeah, partner! Fill ‘er up!"
                        "I can’t hold back any longer!"
                        play sound cum
                        show honeyruby spankinga3 with cum
                        play sound cum
                        show honeyruby spankinga3 with cum
                        "My orgasm erupts, huge loads of thick cum splatter her ass whilst I maintain my vigorous pace throughout."
                        play sound cum
                        show honeyruby spankinga3 with cum
                        play sound cum
                        show honeyruby spankinga3 with cum
                        stop ambience fadeout 3.0
                        "Pulling out briefly near the end, I ice her ass with a few last blasts of jism."
                        "Ruby is utterly out of breath, but absolutely satisfied as cum drips from her used pucker."
                        show honeyruby spankingcum with dissolve
                        honeycrisp "Mmm, that was hot!"
                        ruby "Ahh… I hope Melody didn’t hear me, I got really loud…"
                        "She totally heard us…"
                stop music fadeout 3.0
                honeycrisp "My turn. Stud, your dick may be out of commission, but you know what to do."
                honeycrisp "Ruby, how about you get between my thighs, and [playername], you can enjoy Ruby even more?"
                "Hm?! She wants me to lick Ruby out even though she's dripping with cum?"
                "Ah… Whatever, I know I can’t refuse Honey at this point, she’s definitely the alpha in this threesome."
                scene bg black with dissolve
                "The three of us love each other long into the early hours of the morning, I don’t even remember how it ended."
                "The three of us just sorta passed out in a writhe of limbs and lewdity."
                "In the morning..."
                scene bg rubybedroom with dissolve
                "Honey is the first to wake up, and her movements stir both Ruby and I."
                "After a short and sweet conversation, she kisses us both on the forehead, and heads out early to work at her farm."
                "This leaves Ruby and I to spend the morning cuddling together. Cuddling with a soft mare is the best thing in the world…"
                scene bg boutiquekitchen with dissolve
                "About an hour later, we both wake up. Ruby treats me to some delicious pancakes before I take my leave."
                jump altmorning
        label sofiasex:
            if sofiasex == 1:
                jump sofiasex2
            $ sofiasex = 1
            "There’s another lady wearing a dress. It’s a little less decorated than Dawn’s, but it certainly stands out."
            show sofia dresshappy with dissolve
            "Ah- she caught me staring, and she smiled at me."
            "I guess that’s my cue. Confident or not, I’m going to talk to this girl."
            mc "Hey, that’s a pretty nice dress you’re wearing."
            "Fuck, is that really the first thing that came to mind? I have no game at all."
            show sofia dresshorny with dissolve
            unknown "Certainly, but I think you’d be more interested in what’s under the dress, am I right?"
            "Holy shit, this girl has more game than me."
            "I keep forgetting that this is a culture where the ladies pick up the men."
            if dawnvisit > 3:
                mc "You sure? I thought dresses meant you weren’t interested…"
                show sofia dresslaughing with dissolve
                unknown "It’s true, I’m in heat, so I can't let myself get swept off my feet by a stallion, hehehe."
                unknown "But that doesn’t matter with you, does it?"
                mc "Hmm… It doesn’t matter, you’re right. But if there are girls in heat here, why are you the only one in a dress?"
                show sofia dresshorny with dissolve
                unknown "Some ladies have better self-control than others, hehehe."
                "Oh, this girl is thirsty!"
                show sofia dresshappy with dissolve
                unknown "I’m also wearing some really sexy undergarments. I’d love to show you, hehehe."
            else:
                pass
            mc "I hope you’re not a mind reader, because I’ve started to have far dirtier thoughts than just that."
            show sofia dresshorny with dissolve
            unknown "I like the sound of that. We can go through your dirty thoughts like a list."
            show sofia dresslaughing with dissolve
            unknown "Got a name, handsome?"
            mc "It’s [playername], and you?"
            show sofia dresshappy with dissolve
            sofia "Call me ‘Sofia’. It's not my real name, but doesn't it just roll off the tongue?"
            show sofia dresshorny with dissolve
            sofia "Come dance with me, [playername], I'll be all yours tonight."
            stop music fadeout 3.0
            scene bg black with dissolve
            "Sofia and I get our freak on, dancing and getting more drunk."
            "Almost impatiently and spontaneously, she leads me away from the dancefloor, inviting me to her place after only an hour."
            scene bg fleurbedroom with dissolve
            "Drunkenly, I find myself alone in her bedroom while she prepares in the bathroom, from where I hear her calling out to me."
            sofia "Handsome, I have one question!"
            sofia "Would you prefer panties, or stockings?"
            "Hm? Panties or stockings? Is she going to wear one of those?"
            menu:
                "Panties":
                    sofia "Perfect…"
                    sofia "Darling, close your eyes! Hehehe."
                    "Close my eyes? Alright, I’ll play along."
                    scene bg black with dissolve
                    mc "Closed!"
                    play sound movement
                    "Almost immediately I hear the bathroom door click, along with the ruffling of clothes as she approaches the bed."
                    sofia "Alright, open your eyes."
                    play music sex1 fadein 3.0
                    scene sofia panties1 with dissolve
                    "As I do, I’m greeted with a beautiful sight."
                    "The lighting in her bedroom was already gorgeous, and perfectly set the mood. However, seeing her teasingly gripping the sides of her dress and scrunching it up almost takes my breath away."
                    "Each of her soft, white thighs, leading up to her voluptuous ass, perfectly accentuated by a velvety purple thong."
                    "I think this is my first time seeing panties in this world, naturally they’re designed to accommodate the tail which Sofia holds back to give me the best view possible."
                    "Her very wetness drips from the panties in a manner that can only be called obscene. Now I’m beginning to understand why she was so eager to bring me back."
                    sofia "Babe, I want you to savour every inch…"
                    "I shimmy closer, first bringing my hands to her soft thighs and running my fingers through her flawless fur."
                    "She shivers and coos as I reach her hips, I find the strap keeping her panties in place and playfully slip my fingers underneath, feigning removal."
                    "Although I have a more experimental plan, as I close the distance between her crotch and my face, bringing my tongue to the wetness of the soft fabric."
                    sofia "Yeahh… Ooohhh, that’s it… We’ve got all night…"
                    "With only a few licks, I can already see the outline of her vulva forming in the damp fabric, my cock is already throbbing at the sight."
                    "No longer satisfied just licking her panties, I grip a particularly loose piece of fabric with my teeth and begin to remove her panties almost entirely with just my mouth."
                    show sofia panties2 with dissolve
                    "I don’t know what drunk me was expecting, but they don’t come off as easily as I’d expect. Luckily my fingers are already in place to help loosen the panties, as they shift and fall to her knees."
                    "Satisfied, all that’s left is a wet trail between her wet folds and privates. Her pussy is delightfully plump and fully bloomed with arousal."
                    "I bury my face back into her crotch, my tongue quickly finding her clit while my other senses are bombarded with lewd sights, sounds and smells."
                    sofia "Oohhh, ahhaaa… I’m in heat, so I want you to make me come lots and lots, okay?"
                    "Hard to argue from this position, I’m completely enamoured by this gorgeous mare. Nibbling, sucking and licking at her tantalising vulva, the increasing intensity of her moans indicating that she may already be approaching her first orgasm."
                    "I focus intently on her clit for over a minute, until her pleasure finally boils over. Her entire body shivers, her fur almost standing on end as her pussy visibly starts to contract."
                    "Lovingly, I lap at the milk of Sofia as she has a sensational orgasm, her rear pushing even further against my face, soaking my lips and even my nose slightly."
                    sofia "Mmm… What a wonderful start, usually I have to ask the man to do that… Hehehe, you’re such a gentleman."
                    sofia "Well, you don’t have to be gentle anymore… I want you to rut me like a bitch in heat."
                    "She hoists the rim of her skirt up further, and bends over even more as she presents herself to me fully, her pussy perfectly angled for penetration."
                    "My cock is practically drooling precum, and I’m more than ready to fuck her hard."
                    play sound cum
                    show sofia panties3 with dissolve
                    "I press the tip against her soaking pussy, and it immediately sinks in, almost sucked in."
                    "She’s so wet, I easily plunge deeply until my hips meet her rear. Yet, she still manages to feel wonderfully tight around my throbbing member, some internal twitching adding to the pleasure."
                    sofia "Oooohhh! Fuck me! That’s goooood!"
                    "Her pussy squeezes as I pull back, as if it’s automatically trying to suck me back. With a few more practiced thrusts, I adopt a speedy pace, pounding her pussy hard causing a few enchanting moans to slip from her mouth."
                    "She feels so soft, both internally and externally, as I hold her hips and my own regularly meet with her fluffy butt."
                    "I’m guessing she has an amazing conditioner, because as I grab her tail and pull it to the side like pulling a human woman’s hair, that too feels immensely soft."
                    "It genuinely feels like I’m fucking a princess; the sights, the sounds, the smells. It’s all so fragrant and exquisite."
                    "Yet, as her pussy squelches, the inescapable vulgarity of the situation consumes us both in absolute ecstasy."
                    "And I’m going to fill up this pussy soon. I’m going to unload into this sophisticated mare’s pussy."
                    sofia "Aahhaa, I’m coming! Ahh… Aahh! Your cock is so amazing! Ahh!"
                    "I can’t hold myself back much longer, and as her pussy clings even tighter around my tense throbbing member, I can almost feel the surge of cum rising through my loins."
                    "Giving into the heavenly orgasm, I fuck deeply as my cock releases load after load of hot thick cum into this mare’s pussy."
                    play sound cum
                    show sofia panties4 with cum
                    play sound cum
                    show sofia panties4 with cum
                    "My vision briefly whitens as I lose myself to pure pleasure, and no doubt my sexual partner is too as her eyes scrunch and her orgasmic moaning intensifies."
                    play sound cum
                    show sofia panties4 with cum
                    play sound cum
                    show sofia panties4 with cum
                    stop ambience fadeout 3.0
                    stop music fadeout 3.0
                    "I fill the mare I met less than two hours ago to the brim, before eventually we come down from our lustful highs and pull away."
                    scene bg black with dissolve
                    scene bg fleurbedroom with dissolve
                    "Sofia tosses aside the dress and panties, having only kept it on to make the sex more interesting, and then pulls me into a cuddle on her bed."
                    show sofia happy with dissolve:
                        xalign 0.5
                        ypos 200
                    mc "You’re quite forceful, aren’t you?"
                    show sofia laughing with dissolve
                    sofia "A lady has to be in Arcadia, how do you think I get what I want? Hehehe."
                    "Her legs wrap around me, and almost as if the exact positioning of me relative to her was pre-planned I can feel her wet vulva against my shaft, trying to coax another erection out of me."
                    show sofia horny with dissolve
                    sofia "Now… How long does it take for your species to get hard again?"
                    show sofia laughing with dissolve
                    "Before I can even reply, she entraps me with a beguiling kiss."
                    hide sofia with dissolve
                    "Not literally, but the moment our lips touch, my fate is already sealed. I’m fucking her again, I know it, she knows it."
                    "We’re gonna fuck again."
                    scene bg black with dissolve
                    "…"
                    "Turns out, ‘again’ was an understatement. I was so naïve when I thought we’d just do it twice and call it a great night together."
                    "We fucked not once more, but another two times more. Three times total in the evening, and once in the morning for good measure."
                    "I’m fairly certain she had eight orgasms in total."
                    "In the morning, she actually trusts me enough to leave me in her apartment while she leaves for work."
                    "She’s a maid at the castle, go figure. It’s one of the few professions in Arcadia that wears a dress to work, that’ll be why she owns a few in the first place."
                    "Despite permission to stay, I find myself leaving at the same time as her as I return home for breakfast and a shower."
                    "Not before exchanging magic mail addresses though, she says she wants to see me again sometime."
                    "…"
                    jump altmorning

                "Stockings":
                    sofia "Ahh, you’re that kind of man?"
                    sofia "Darling, close your eyes! Hehehe."
                    "Close my eyes? Alright, I’ll play along."
                    scene bg black with dissolve
                    mc "Closed!"
                    play sound movement
                    "Almost immediately I hear the bathroom door click, along with the ruffling of clothes as she approaches the bed."
                    sofia "Alright, open your eyes."
                    play music sex1 fadein 3.0
                    scene sofia stockings1 with dissolve
                    "As I do, I’m greeted with a beautiful sight."
                    "The lighting in her bedroom was already gorgeous, and perfectly set the mood. However, seeing her teasingly gripping the sides of her dress and scrunching it up almost takes my breath away."
                    "Each of her soft thighs, leading up to her voluptuous ass, perfectly accentuated by sheer dark stockings."
                    "I think this is my first time seeing pantyhose in this world, naturally they’re designed to accommodate the tail which Sofia holds back to give me the best view possible."
                    "Her very wetness drips from the stockings in a manner that can only be called obscene. Now I’m beginning to understand why she was so eager to bring me back."
                    sofia "Darling, I want you to savour every inch…"
                    "I shimmy closer, first bringing my hands to her soft thighs and running my fingers over the velvety fabric."
                    "She shivers and coos as I reach her ass, using my fingers to part her cheeks slightly, I can hear a wet schlick as the folds of her vulva part."
                    "I close the distance between her crotch and my face, bringing my tongue to the wetness of the soft fabric."
                    sofia "Yeahh… Ooohhh, that’s it… We’ve got all night…"
                    scene sofia stockings2 with dissolve
                    "No longer satisfied just licking through the stockings, I grip a bit of the fabric with my teeth and make a small tear."
                    sofia "Oh? Oh my, how sexy... As long as you keep the holes under the dress, go wild, babe."
                    "I use my fingers to play with her labia as I gradually make the hole in the stockings larger. Soon her entire pussy is exposed to the cool bedroom air. Her pussy is delightfully plump and fully bloomed with arousal."
                    "I bury my face back into her crotch, my tongue quickly finding her clit while my other senses are bombarded with lewd sights, sounds and smells."
                    sofia "Oohhh, ahhaaa… I’m in heat, so I want you to make me come lots and lots, okay?"
                    "Hard to argue from this position, I’m completely enamoured by this gorgeous mare. Nibbling, sucking and licking at her tantalising vulva, the increasing intensity of her moans indicating that she may already be approaching her first orgasm."
                    "I focus intently on her clit for over a minute, until her pleasure finally boils over. Her entire body shivers, her fur almost standing on end as her pussy visibly starts to contract."
                    "Lovingly, I lap at the milk of Sofia as she has a sensational orgasm, her rear pushing even further against my face, soaking my lips and even my nose slightly."
                    sofia "Mmm… What a wonderful start, usually I have to ask men to do that… Hehehe, you’re such a gentleman."
                    sofia "Well, you don’t have to be gentle anymore… I want you to rut me like a bitch in heat."
                    "She hoists the rim of her skirt up further, and bends over even more as she presents herself to me fully, her pussy perfectly angled for penetration."
                    "My cock is practically drooling precum, and I’m more than ready to fuck her hard."
                    play sound cum
                    scene sofia stockings3 with dissolve
                    "I press the tip against her soaking pussy, and it immediately sinks in, almost sucked in."
                    "She’s so wet, I easily plunge deeply until my hips meet her rear. Yet, she still manages to feel wonderfully tight around my throbbing member, some internal twitching adding to the pleasure."
                    sofia "Oooohhh! Fuck me! That’s goooood!"
                    "Her pussy squeezes as I pull back, as if it’s automatically trying to suck me back. With a few more practiced thrusts, I adopt a speedy pace, pounding her pussy hard causing a few enchanting moans to slip from her mouth."
                    "She feels so soft, both internally and externally, as I hold her hips and my own regularly graze against her velvety stockings."
                    "I’m guessing she has an amazing conditioner, because as I grab her tail and pull it to the side like pulling a human woman’s hair, that too feels immensely soft."
                    "It genuinely feels like I’m fucking a princess; the sights, the sounds, the smells. It’s all so fragrant and exquisite."
                    "Yet, as her pussy squelches, the inescapable vulgarity of the situation consumes us both in absolute ecstasy."
                    "And I’m going to fill up this pussy soon. I’m going to unload into this sophisticated mare’s pussy."
                    sofia "Aahhaa, I’m coming! Ahh… Aahh! Your cock is so amazing! Ahh!"
                    "I can’t hold myself back much longer, and as her pussy clings even tighter around my tense throbbing member, I can almost feel the surge of cum rising through my loins."
                    play sound cum
                    scene sofia stockings4 with cum
                    play sound cum
                    scene sofia stockings4 with cum
                    "Giving into the heavenly orgasm, I fuck deeply as my cock releases load after load of hot thick cum into this mare’s pussy."
                    play sound cum
                    scene sofia stockings4 with cum
                    play sound cum
                    scene sofia stockings4 with cum
                    stop ambience fadeout 3.0
                    stop music fadeout 3.0
                    "My vision briefly whitens as I lose myself to pure pleasure, and no doubt my sexual partner is too as her eyes scrunch and her orgasmic moaning intensifies."
                    scene bg black with dissolve
                    scene bg fleurbedroom with dissolve
                    "I fill the mare I met less than two hours ago to the brim, before eventually we fall down from our lustful highs and fall down onto the bed."
                    "Sofia tosses aside the dress and stockings, having only kept it on to make the sex more interesting, and then pulls me into a cuddle."
                    show sofia happy with dissolve:
                        xalign 0.5
                        ypos 200
                    mc "You’re quite forceful, aren’t you?"
                    show sofia laughing with dissolve
                    sofia "A lady has to be in Arcadia, how do you think I get what I want? Hehehe."
                    "Her legs wrap around me, and almost as if the exact positioning of me relative to her was pre-planned I can feel her wet vulva against my shaft, trying to coax another erection out of me."
                    show sofia horny with dissolve
                    sofia "Now… How long does it take for your species to get hard again?"
                    show sofia laughing with dissolve
                    "Before I can even reply, she entraps me with a beguiling kiss."
                    "Not literally, but the moment our lips touch, my fate is already sealed. I’m fucking her again, I know it, she knows it."
                    "We’re gonna fuck again."
                    scene bg black with dissolve
                    "…"
                    "Turns out, ‘again’ was an understatement. I was so naïve when I thought we’d just do it twice and call it a great night together."
                    "We fucked not once more, but another two times more. Three times total in the evening, and once in the morning for good measure."
                    "I’m fairly certain she had eight orgasms in total."
                    "In the morning, she actually trusts me enough to leave me in her apartment while she leaves for work."
                    "She’s a maid at the castle, go figure. It’s one of the few professions in Arcadia that wears a dress to work, that’ll be why she owns a few in the first place."
                    "Despite permission to stay, I find myself leaving at the same time as her as I return home for breakfast and a shower."
                    "Not before exchanging magic mail addresses though, she says she wants to see me again sometime."
                    "…"
                    jump altmorning
            label sofiasex2:
                "There’s Sofia again, and she seems to still be wearing her dress."
                "Flashbacks to our night together play in my head as I close the distance to her."
                show sofia dresshappy with dissolve
                mc "Hey Sofia, time for an encore?"
                show sofia dresslaughing with dissolve
                sofia "Hehehe, aren’t you presumptuous?"
                mc "Ah, my bad for assuming you’d be up for it again. My head was in the clouds."
                "She shakes her head and giggles."
                show sofia dresshorny with dissolve
                sofia "You misunderstand me, an ‘encore’ is the end of a concert, right? As far as I’m concerned, I’ll never stop wanting to perform with you, hehehe."
                mc "Easy! Don’t give me a boner in the club"
                show sofia dresslaughing with dissolve
                sofia "Wanna go back to my place? Then I can give you all the erections you’d like, sexy…"
                mc "Already? But it’s so early."
                show sofia dresshorny with dissolve
                sofia "Exactly, ever more time to mate with you. Come on, make me yours."
                "Ah shit, here we go again."
                stop music fadeout 3.0
                scene bg black with dissolve
                scene bg fleurbedroom with dissolve
                "I find myself alone in her bedroom once again, but this time I’m completely sober."
                sofia "Daaarliinngg, do you want panties or stockings?"
                "She sure is accommodating, let’s see, what does my dick want today?"
                menu:
                    "Panties":
                        sofia "Perfect…"
                        sofia "Darling, close your eyes! Hehehe."
                        "Close my eyes again? Alright, I’ll play along."
                        scene bg black with dissolve
                        mc "Closed!"
                        play sound movement
                        "Almost immediately I hear the bathroom door click, along with the ruffling of clothes as she approaches the bed."
                        sofia "Alright, open your eyes."
                        play music sex1 fadein 3.0
                        scene sofia panties1 with dissolve
                        "As I do, I’m greeted with a beautiful sight."
                        "The gorgeous lighting in her bedroom perfectly sets the mood. However, seeing her teasingly gripping the sides of her dress and scrunching it up almost always takes breath away."
                        "Each of her soft, white thighs, leading up to her voluptuous ass, perfectly accentuated by a velvety purple thong."
                        "Her panties are so gorgeous, naturally they’re designed to accommodate the tail which Sofia holds back to give me the best view possible."
                        "Her very wetness drips from the panties in a manner that can only be called obscene. Now I’m beginning to understand why she was so eager to bring me back."
                        sofia "Darling, I want you to savour every inch…"
                        "I shimmy closer, first bringing my hands to her soft thighs and running my fingers through her flawless fur."
                        "She shivers and coos as I reach her hips, I find the strap keeping her panties in place and playfully slip my fingers underneath, feigning removal."
                        "Although I have a more experimental plan, as I close the distance between her crotch and my face, bringing my tongue to the wetness of the soft fabric."
                        sofia "Yeahh… Ooohhh, that’s it… Your tongue feels amazing…"
                        "With only a few licks, I can already see the outline of her vulva forming in the damp fabric, my cock is already throbbing at the sight."
                        "No longer satisfied just licking her panties, I grip a particularly loose piece of fabric with my teeth and begin to remove her panties almost entirely with just my mouth."
                        show sofia panties2 with dissolve
                        "Sober, I manage to peel the panties off pretty well. At a certain point they simply fall down to her knees."
                        "Satisfied, all that’s left is a wet trail between her wet folds and privates. Her pussy is delightfully plump and fully bloomed with arousal."
                        "I bury my face back into her crotch, my tongue quickly finding her clit while my other senses are bombarded with lewd sights, sounds and smells."
                        sofia "Oohhh, ahhaaa… I want you to make me come lots and lots, okay?"
                        "Hard to argue from this position, I’m completely enamoured by this gorgeous mare. Nibbling, sucking and licking at her tantalising vulva, the increasing intensity of her moans indicating that she may already be approaching her first orgasm."
                        "I focus intently on her clit for over a minute, until her pleasure finally boils over. Her entire body shivers, her fur almost standing on end as her pussy visibly starts to contract."
                        "Lovingly, I lap at the milk of Sofia as she has a sensational orgasm, her rear pushing even further against my face, soaking my lips and even my nose slightly."
                        sofia "Mmm… Hehehe, you’re always such a gentleman."
                        sofia "Well, you don’t have to be gentle anymore… I want you to rut me like a bitch in heat. Fuck me just like last time, you fiend, hehehe."
                        "She hoists the rim of her skirt up further, and bends over even more as she presents herself to me fully, her pussy perfectly angled for penetration."
                        "My cock is practically drooling precum, and I’m more than ready to fuck her hard."
                        play sound cum
                        show sofia panties3 with dissolve
                        "I press the tip against her soaking pussy, and it immediately sinks in, almost sucked in."
                        "She’s so wet, I easily plunge deeply until my hips meet her rear. Yet, she still manages to feel wonderfully tight around my throbbing member, some internal twitching adding to the pleasure."
                        sofia "Oooohhh! Fuck me! That’s goooood!"
                        "Her pussy squeezes as I pull back, as if it’s automatically trying to suck me back. With a few more practiced thrusts, I adopt a speedy pace, pounding her pussy hard causing a few enchanting moans to slip from her mouth."
                        "She feels so soft, both internally and externally, as I hold her hips and my own regularly meet with her fluffy butt."
                        "I grab her tail and pull it to the side like pulling a human woman’s hair, it’s pretty fun pulling a mare’s tail while fucking them."
                        "It genuinely feels like I’m fucking a princess; the sights, the sounds, the smells. It’s all so fragrant and exquisite."
                        "Yet, as her pussy squelches, the inescapable vulgarity of the situation consumes us both in absolute ecstasy."
                        "And I’m going to fill up this pussy soon. I’m going to unload into this sophisticated mare’s pussy."
                        sofia "Aahhaa, I’m coming! Ahh… Aahh! Your cock is so amazing! Ahh!"
                        "I can’t hold myself back much longer, and as her pussy clings even tighter around my tense throbbing member, I can almost feel the surge of cum rising through my loins."
                        "Giving into the heavenly orgasm, I fuck deeply as my cock releases load after load of hot thick cum into this mare’s pussy."
                        play sound cum
                        show sofia panties4 with cum
                        play sound cum
                        show sofia panties4 with cum
                        "My vision briefly whitens as I lose myself to pure pleasure, and no doubt my sexual partner is too as her eyes scrunch and her orgasmic moaning intensifies."
                        play sound cum
                        show sofia panties4 with cum
                        play sound cum
                        show sofia panties4 with cum
                        stop ambience fadeout 3.0
                        stop music fadeout 3.0
                        "I fill her to the brim, before eventually we come down from our lustful highs and pull away."
                        scene bg black with dissolve
                        scene bg fleurbedroom with dissolve
                        "Sofia tosses aside the dress, having only kept it on to make the sex more interesting, and then pulls me into a cuddle on her bed."
                        show sofia happy with dissolve:
                            xalign 0.5
                            ypos 200
                        mc "Fifteen minutes, then you can be on top."
                        show sofia laughing with dissolve
                        sofia "Deal, hehehe. Maybe we could try another position after that?"
                        mc "I like the sound of that."
                        show sofia horny with dissolve
                        sofia "Maybe another hole? Hehehe."
                        scene bg black with dissolve
                        "Before I can even reply, she entraps me with a beguiling kiss."
                        "Not literally, but the moment our lips touch, my fate is already sealed."
                        "…"
                        "In the morning, we go our separate ways after a quickie. This girl officially has a libido that puts me to shame."
                        jump altmorning
                    "Stockings":
                        sofia "Ahh, you’re that kind of man?"
                        sofia "Darling, close your eyes! Hehehe."
                        "Close my eyes again? Alright, I’ll play along."
                        scene bg black with dissolve
                        mc "Closed!"
                        play sound movement
                        "Almost immediately I hear the bathroom door click, along with the ruffling of clothes as she approaches the bed."
                        sofia "Alright, open your eyes."
                        play music sex1 fadein 3.0
                        scene sofia stockings1 with dissolve
                        "As I do, I’m greeted with a beautiful sight."
                        "The gorgeous lighting in her bedroom already perfectly sets the mood. However, seeing her teasingly gripping the sides of her dress and scrunching it up always takes my breath away."
                        "Each of her soft thighs, leading up to her voluptuous ass, perfectly accentuated by sheer dark stockings."
                        "I don’t think she was wearing stockings earlier, so she must have put on a new pair. Naturally they’re designed to accommodate the tail which Sofia holds back to give me the best view possible."
                        "Her very wetness drips from the stockings in a manner that can only be called obscene. Now I’m beginning to understand why she was so eager to bring me back."
                        sofia "Darling, I want you to savour every inch…"
                        "I shimmy closer, first bringing my hands to her soft thighs and running my fingers over the velvety fabric."
                        "She shivers and coos as I reach her ass, using my fingers to part her cheeks slightly, I can hear a wet schlick as the folds of her vulva part."
                        "I close the distance between her crotch and my face, bringing my tongue to the wetness of the soft fabric."
                        sofia "Yeahh… Ooohhh, that’s it… Your tongue feels exquisite!"
                        scene sofia stockings2 with dissolve
                        "No longer satisfied just licking through the stockings, I grip a bit of the fabric with my teeth and make a small tear."
                        "I use my fingers to play with her labia as I gradually make the hole in the stockings larger. Soon her entire pussy is exposed to the cool bedroom air. Her pussy is delightfully plump and fully bloomed with arousal."
                        "I bury my face back into her crotch, my tongue quickly finding her clit while my other senses are bombarded with lewd sights, sounds and smells."
                        sofia "Oohhh, ahhaaa… I want you to make me come lots and lots, okay?"
                        "Hard to argue from this position, I’m completely enamoured by this gorgeous mare. Nibbling, sucking and licking at her tantalising vulva, the increasing intensity of her moans indicating that she may already be approaching her first orgasm."
                        "I focus intently on her clit for over a minute, until her pleasure finally boils over. Her entire body shivers, her fur almost standing on end as her pussy visibly starts to contract."
                        "Lovingly, I lap at the milk of Sofia as she has a sensational orgasm, her rear pushing even further against my face, soaking my lips and even my nose slightly."
                        sofia "Mmm… What a wonderful start… Hehehe, you’re always such a gentleman."
                        sofia "Well, you don’t have to be gentle anymore… I want you to rut me like a bitch in heat. Fuck me hard, just like last time."
                        "She hoists the rim of her skirt up further, and bends over even more as she presents herself to me fully, her pussy perfectly angled for penetration."
                        "My cock is practically drooling precum, and I’m more than ready to fuck her hard."
                        play sound cum
                        scene sofia stockings3 with dissolve
                        "I press the tip against her soaking pussy, and it immediately sinks in, almost sucked in."
                        "She’s so wet, I easily plunge deeply until my hips meet her rear. Yet, she still manages to feel wonderfully tight around my throbbing member, some internal twitching adding to the pleasure."
                        sofia "Oooohhh! Fuck me! That’s goooood!"
                        "Her pussy squeezes as I pull back, as if it’s automatically trying to suck me back. With a few more practiced thrusts, I adopt a speedy pace, pounding her pussy hard causing a few enchanting moans to slip from her mouth."
                        "She feels so soft, both internally and externally, as I hold her hips and my own regularly graze against her velvety stockings."
                        "I grab her tail and pull it to the side like pulling a human woman’s hair, pulling a mare’s tail is a lot of fun, and Sofia definitely loves it."
                        "It genuinely feels like I’m fucking a princess; the sights, the sounds, the smells. It’s all so fragrant and exquisite."
                        "Yet, as her pussy squelches, the inescapable vulgarity of the situation consumes us both in absolute ecstasy."
                        "And I’m going to fill up this pussy soon. I’m going to unload into this sophisticated mare’s pussy."
                        sofia "Aahhaa, I’m coming! Ahh… Aahh! Your cock is so amazing! Ahh!"
                        "I can’t hold myself back much longer, and as her pussy clings even tighter around my tense throbbing member, I can almost feel the surge of cum rising through my loins."
                        play sound cum
                        scene sofia stockings4 with cum
                        play sound cum
                        scene sofia stockings4 with cum
                        "Giving into the heavenly orgasm, I fuck deeply as my cock releases load after load of hot thick cum into this mare’s pussy."
                        play sound cum
                        scene sofia stockings4 with cum
                        play sound cum
                        scene sofia stockings4 with cum
                        stop ambience fadeout 3.0
                        stop music fadeout 3.0
                        "My vision briefly whitens as I lose myself to pure pleasure, and no doubt my sexual partner is too as her eyes scrunch and her orgasmic moaning intensifies."
                        scene bg black with dissolve
                        scene bg fleurbedroom with dissolve
                        "I fill her to the brim, before eventually we come down from our lustful highs and pull away."
                        "Sofia tosses aside the dress, having only kept it on to make the sex more interesting, and then pulls me into a cuddle on her bed."
                        show sofia happy with dissolve:
                            xalign 0.5
                            ypos 200
                        mc "Fifteen minutes, then you can be on top."
                        show sofia laughing with dissolve
                        sofia "Deal, hehehe. Maybe we could try another position after that?"
                        mc "I like the sound of that."
                        show sofia horny with dissolve
                        sofia "Maybe another hole? Hehehe."
                        scene bg black with dissolve
                        "Before I can even reply, she entraps me with a beguiling kiss."
                        "Not literally, but the moment our lips touch, my fate is already sealed."
                        "…"
                        "In the morning, we go our separate ways after a quickie. This girl officially has a libido that puts mine to shame."
                        jump altmorning

screen cityday():
    imagemap:
        ground "bg arcadiastreets"
        hover "bg arcadiastreetshover"

        hotspot (0, 285, 560, 345) clicked Jump("nightclubcm")
        hotspot (0, 645, 135, 78) clicked Jump("preworldmap")
        hotspot (772, 350, 195, 300) clicked Jump("musicstudio")
        hotspot (622, 330, 154, 300) clicked Jump("artgallery")
        hotspot (978, 235, 325, 425) clicked Jump("church")
        hotspot (0, 0, 906, 269) clicked Jump("castlecm")



    text "{b}[monies]{/b}":
        xalign 0.22
        yalign 0.0225
    text "{b}Day [days]{/b}":
        xalign 0.065
        yalign 0.0225
screen nightcity():
    imagemap:
        ground "bg arcadianight"
        hover "bg arcadianighthover"

        hotspot (0, 285, 560, 345) clicked Jump("nightclubncm")
        hotspot (0, 645, 135, 78) clicked Jump("worldmap")
        hotspot (772, 350, 195, 300) clicked Jump("musicstudioncm")
        hotspot (622, 330, 154, 300) clicked Jump("artgallery")
        hotspot (0, 0, 800, 325) clicked Jump("castlencm")



    text "{b}[monies]{/b}":
        xalign 0.22
        yalign 0.0225
    text "{b}Day [days]{/b}":
        xalign 0.065
        yalign 0.0225
