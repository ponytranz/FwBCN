label boutique:
    $ boutiquevisits += 1
    if boutiquevisits == 1:
        $ monies += 25
        $ boutiquevisit1 = 1
        jump boutiquevisit1
    elif boutiquevisits == 2:
        $ monies += 80
        $ boutiquevisit2 = 1
        jump boutiquevisit2
    elif boutiquevisits == 3:
        $ monies += 25
        $ boutiquevisit3 = 1
        jump boutiquevisit3
    else:
        jump boutiqueafter
    label boutiquevisit1:
        stop music fadeout 3.0
        $ boutiquevisit1 = 1
        "Ah, the boutique. I’m not exactly sure what I’ll be doing there, but I’m curious. I've heard that the girl running this boutique is beautiful."
        "It's practically the closest building to the wagon so it's really hard to miss."
        "Even the directions Moxie left for me are just 'walk forward'."
        "Additionally, this building is one of the largest in the suburbs. Combining both the shop-like ground floor with the living quarters of a regular house, it towers over the traditional homes."
        show bg boutiquedoor with dissolve
        "As I knock on the door I can hear ruffling on the other side which opens to reveal a serene beauty."
        play music boutique fadein 5.0
        show ruby shocked with dissolve
        ruby "Ah, it’s Moxie's new friend! Sorry, we’re not open yet."
        mc "Hello, I'm actually here in response to Penelope's letter, I hear you have some work for me?"
        show ruby neutral with dissolve
        ruby "Goodness me…  I almost forgot about that. Well, I… This is quite a surprise."
        mc "Don’t worry, I’m slowly getting used to that initial shock. I know I look a bit different, but I’m just like anyone else, happy to help and able to take orders."
        show ruby happy with  dissolve
        ruby "Ah please, do come in. My name is Ruby, it’s my pleasure darling."
        mc "I’m [playername], the pleasure is mine."
        hide ruby with dissolve
        show bg boutiqueinside with dissolve
        "I step into the boutique, and while I was expecting a shop floor it seems more like a messy warehouse. It’s chaotic to say the least."
        "There are some mannequins outfitted with beautiful designer clothes, and  some with unfinished rags."
        "There are also bags of material strewn out over the shop floor."
        show ruby shy with dissolve
        ruby "It's nice to see you, however it's important to reiterate that this is a favour. Truth is, I’m stretched thin, so I won’t be able to pay you much."
        mc "Stretched thin you say? Hopefully I can help you out with that."
        show ruby neutral with dissolve
        ruby "No, not really, this is a designer boutique. I design the clothes, you’ll just have meagre tasks to complete."
        if barvisit1 == 1 and maiddressbought == 0:
            mc "Speaking of which, are you selling clothes too? I'd like to buy something."
            "I need to get a 'slave' outfit for Riku's truth or dare punishment."
            show ruby shocked with dissolve
            ruby "Oh? W-Well we're not open but... what would you like to buy?"
            mc "I'm looking for a maid dress."
            show ruby laughing with dissolve
            ruby "Of course darling... Hmm, Melody had a maid dress for halloween once..."
            ruby "Ah, there it is."
            "She walks over to a rack and takes one out to show me, it's perfect."
            show ruby neutral with dissolve
            ruby "Naturally this dress fits Melody's small figure and bosom, is that okay?"
            mc "Yeah that's perfect, how much is it?"
            show ruby happy with dissolve
            ruby "Second hand? 50 monies should cover it."
            menu rubymaidmenu1:
                "I have [monies] monies."
                "Buy the dress (-50 Monies)" if monies >= 50:
                    if monies < 50:
                        "I can't afford it."
                        jump rubymaidmenu1
                    $ monies -= 50
                    $ maiddressbought = 1
                    ruby "Pleasure doing business with you darling."
                    mc "By the way, can you leave the dress here?"
                    ruby "Here? Do you want to pick it up at a later time?"
                    mc "Yes, you'll see."
                "Maybe later":
                    ruby "Okay darling, maybe another time."
            mc "Anyway, I'm here to work too. Do you have something for me?"
        else:
            mc "Yeah, that makes sense. I’ll do anything, genuinely I’m just here to help."
        show ruby neutral with dissolve
        ruby "Gosh, I didn’t really think this through, I’ve never worked with another pony before… Hmm…"
        show ruby shocked with dissolve
        ruby "Wait here a few moments and I’ll think of something... Oh, would you like some tea?"
        mc "Yeah, tea would be great, thanks."
        hide ruby with dissolve
        "I sit down on what seems to be the only chair that doesn’t have a mound of material or clothes bundled atop of it."
        "This room… it reminds me of a girl’s untidy bedroom. It’s like she got out all her toys, but she seldom puts them back."
        "While I’m waiting, I might as well have a closer look at the clothes she has designed. They each have a certain elegance to them, a certain royal charm."
        "To my ignorance they appear quite high-end and respectable."
        "As I step closer and get a good look though, I can’t help but notice how dusty it is in here. It’s one thing for dust to accumulate in the crevices of the room, but on the clothes? It must have been sitting here untouched for months."
        "Perhaps this is just an old design that has been already been approved and mass produced for a clothes shop, I can’t really say, I don’t know how it works in Arcadia. While it's similar in some aspects of my world, in other areas there’s a notable disconnect."
        "Ruby soon returns with a decorated cup of black tea in both hands, placing them both on a clearing atop a dressing table."
        show ruby happy with dissolve
        mc "Thank you for the tea, Ruby."
        ruby "You're welcome, dearie. I have decided that you can clean up around here. I don’t exactly have any hard rules, and it’s not exactly a science, I just want everything neater in here."
        ruby "Place materials in bags, fold up clothes neatly, dust surfaces, if there’s anything you genuinely don’t know what to do with, place it on that large table over there and I’ll sort it out later."
        show ruby laughing with dissolve
        ruby "Super simple, I'm honestly embarrassed that you came when it's so bad, I should never have let it get this messy anyway."
        show ruby shy with dissolve
        ruby "But… this is a good excuse to get it cleaned up, sorry to make you that excuse."
        menu:
            "That sounds so boring...":
                show ruby neutral with dissolve
                ruby "Boring as it may be, it's that or leave empty-handed."
                mc "Yeah, I'll do it, don't worry."
                mc "It shouldn't take longer than an hour."
            "Sounds great, I'll get started now.":
                show ruby laughing with dissolve
        ruby "Wonderful to hear darling, I have some work to do upstairs, I’m afraid that’s a do not disturb situation."
        mc "Alright, what if I need to ask a question, or something? Like… I don’t even know where anything is."
        show ruby happy with dissolve
        ruby "If you really need me, call my name and I’ll come down when I’m ready. For everything else, the kitchen and downstairs bathroom are on the left of that hallway, plenty of cleaning utensils there."
        mc "Hmm, guess I’ll start by putting everything in neat piles."
        show ruby laughing with dissolve
        ruby "Fabulous, now, I must be off, a mare must work hard to make waves in the industry these days."
        hide ruby happy with dissolve
        "She claps her hands together, smiling as she takes her leave and goes upstairs."
        "Now that she's gone, I can't help but feel like there's something wrong here."
        stop ambience fadeout 3.0
        stop music fadeout 3.0
        "Wasn't she acting a little strange?"
        "As I clean around the room I look at some of her beautiful clothing designs."
        "It must be hard making waves in a clothing industry when no one wears clothes..."
        play music ambientinterlude fadein 30.0
        "Perhaps Ruby would be more successful in my old world."
        "It’s surprising just how similar some of these clothing designs are to clothes in my world, yet simultaneously some designs seem to be completely abstract."
        "It's genuinely hard to tell if some of the pieces are lingerie, or it just appear to be lingerie because it shows off genitalia, which isn’t a taboo in this society."
        "I assume she has another room for designing clothes, perhaps a textiles room, because honestly this place can’t be anything more than a warehouse considering its upkeep."
        "Oh well, it’s my job to clean right now, not ask questions. It’s not exactly lavish work but I wasn’t expecting a free ride throughout my time here in Arcadia."
        "If I truly don’t enjoy it, I can just work somewhere else instead."
        "I start by organising all the materials, then bags, and then all the loose clothes."
        "Once all loose items are accounted for, I can finally start to brush down the surfaces, and then sweep."
        "This is… really boring."
        "As boring as it may be, it’s not exactly taking a long time, there’s not a chance this is going to fill up the expected eight hours of a full workday."
        "Brushing, dusting… A sip of tea, it’s still warm."
        "I’m surprised by how easy this task turned out to be. The room’s size made it seem like it’d be a gargantuan task at first, but all I’ve had to do is pick up and move some things."
        "It’s actually become quite apparent that this room isn’t actually messy, it’s just incredibly disorganised."
        "Ruby could have done this herself and it wouldn’t have taken that long. It’s just like my old room back at home whenever it’s messy, it only takes about five minutes to actually tidy up, it’s just exerting the effort to actually get off my ass."
        "Alright, I’m done. This place looks much better, the room even feels bigger."
        "If Ruby isn't here working, what is this room even used for?"
        "Surely this room must be a shop floor, where customers enter, try on clothes and then see how they look in the mirror. No need for changing rooms when everyone walks around naked."
        "Maybe I just came here when the boutique was closed, but that wouldn’t explain the mess or dust."
        "Alright, I've had enough pondering. Something is wrong, and I’m curious."
        "Nothing about this situation adds up, and my inner detective is going to find out the truth."
        "I know Ruby told me not to bother her upstairs, but I have to tell her I've finished cleaning, so I'll intentionally accidentally peep upstairs and see what's going on."
        "Perhaps she’s just making clothes, maybe she’s in a cult gangbang, or secretly a demon."
        show bg boutiqueupstairs with dissolve
        "I tiptoe upstairs and it leads to a hallway that shoots off to a few rooms that fill out the top floor."
        "The second floor is still quite large; I imagine there’s more than just bedrooms and a bathroom up here. I’m not sure what room Ruby is in though, and I don’t really feel like yelling."
        "I peek into the first room and it's just an empty cutesy bedroom, the colour scheme is pink and white. I don’t go inside so the only notable object I can make out through the crack in the door is a musical keyboard."
        "A completely normal bedroom... I feel guilty now, I'm probably being petty and nosy."
        menu:
            "What should I do?"
            "Keep going, I need to talk to Ruby anyway.":
                "Yeah, I need to tell her I'm done, so I'll push onward."
                "Wait, I just heard something."
                "Was that Ruby’s voice? I can’t make out what she’s saying, but she talks again. Is she talking to herself?"
            "Turn back, this feels weird.":
                "Yeah, I should just wait downstairs..."
                "Just as I'm turning to leave, I hear Ruby’s distinctive voice. Did she just talk to me?"
                "I can’t make out what she’s saying, but she talks again. Is she talking to herself?"
                "Well I'm here now, I'll tell her I'm done."
        show  bg boutiqueupstairs2 with dissolve
        ruby "… Yeah, you like…"
        "I peek into this room and at a glance I can see a similar cutesy bedroom, I can definitely hear Ruby from this room."
        ruby "Ahhh, yeahh… Thank you Bigs221"
        stop music fadeout 8.0
        "Bigs221? what? Wait, I can hear her moaning."
        "Is she masturbating?"
        "Getting slightly closer, I peek through the crack in the door"
        show ruby camming with dissolve
        play ambience sex fadein 10.0
        pause 0.5
        "From behind I can see her legs spread open before a laptop, it seems she’s streaming herself masturbating."
        "She's a camgirl!"
        "I… really shouldn’t be spying on this, this is way too personal and perverse."
        "I’m going to head back to the kitchen and pretend I didn’t see this, else I’ll end up in pony jail for being a peeping tom."
        hide ruby camming with dissolve
        pause 0.5
        "As soon as I turn around however, busted! There’s someone RIGHT there, making me jump. In a hushed voice she whispers to me."
        play music melodytheme
        show melody fufufu with dissolve
        unknown "What’s this I spy, a rat peeping on my sister?"
        menu:
            "It's a misunderstanding, I didn't know.":
                show melody sadistic with dissolve
                unknown "Ohoho, you didn't know? Let me guess, your dick just followed the trail of moans and your brain didn't catch on?"
            "Who are you?":
                show melody sadistic with dissolve
                unknown "I'm the pest control."
            "Yeah, I was watching.":
                show melody happy with dissolve
                unknown "I like your honesty. Perhaps you're not a rat after all."
        unknown "You enjoyed it didn’t you? Watching such a regal lush mare touching herself in lewd ways."
        show melody death1 with dissolve
        menu:
            "Of course, she's beautiful.":
                unknown "Gross, gross, gross! You really are just a sick pervert."
                unknown "I'm glad I caught you before you started masturbating to her."
                show melody fufufu with dissolve
                mc "What? I wouldn't do that."
                unknown "Wouldn't you?"
            "Maybe, what's it to you?":
                unknown "I bet you get excited watching innocent mares like her touch herself."
                unknown "You may be better suited to being one of her lonely orbiters that donate to her every day."
            "No, I didn't.":
                unknown "Liar, I saw you tip-toeing up to the door, limp dick swaying back and forth."
        "I don’t even know what to say. I’m somewhat paralyzed, I just hope she doesn’t blow my cover."
        "As we whisper to each other in the hallway, I can still hear Ruby masturbating"
        "If I can hear that, then she could hear the two of us any second."
        mc "I was just returning to the kitchen, we shouldn't exacerbate the problem by staying here."
        show melody fufufu with dissolve
        unknown "What's that, we shouldn't masturbate the problem?"
        unknown "Oh? Is that why your little guy down there is growing?"
        mc "W-Wha, it is not!"
        show melody sadistic with dissolve
        unknown "Ohoh suuure, first you spy on my sister masturbating, and now you’re ogling my breasts and pussy."
        unknown "Admit it, you've looked at my boobs and pussy already."
        menu:
            "You're naked, it's only natural.":
                show melody happy with dissolve
                unknown "Of course, it's only natural for you to love these breasts."
            "Yeah, you have a nice body.":
                show melody satisfied with dissolve
                unknown "I'll take the compliment, you perv."
                show melody sadistic with dissolve
                unknown "In fact, for being so kind, how about a closer look?"
            "Nope, eye contact only.":
                unknown "Oh please, I saw your eyes move at the mere mention of my tiny titties."
        show melody closesadistic with dissolve
        unknown "Come on, come touch them, they're as soft as they look."
        show melody closehappy with dissolve
        unknown "Or are you an ass man? Maybe you want to feel my pussy? It's mating season so it's nice and wet."
        "Damnit, now my penis is starting to stiffen slightly. I don’t know what this girl’s trying to do, but she has managed to beguile me."
        show melody fufufu with dissolve
        unknown "Oh disgusting, your thing moved on its own, like a worm. Oh, by Aurora, it’s growing."
        "I feel humiliated, but I have enough pride to not cover myself up at least. I can tell what she’s trying to do, she’s trying to psych me out and bully me, I’ll call her bluff."
        show melody happy with dissolve
        unknown "All that growth because you saw me and my sister, hm? You have a thing for tasty mares like us?"
        menu:
            "I sure do, especially horny girls in heat like you.":
                show melody sadistic with dissolve
                unknown "Aren't I just charming?"
                unknown "Heat or not, I'm not one of your easy mare sluts."
            "I prefer you over your sister, how about we go to your room?":
                show melody death1 with dissolve
                unknown "Wow, trying to sleep with a mare you met a few minutes ago?"
                unknown "I knew it, you really are a pig."
            "You're not a tasty mare, but your sister is.":
                show melody fufufu with dissolve
                unknown "It truly breaks my heart to know you wouldn't spy on me masturbating."
                show melody death1 with dissolve
                unknown "Kehehe."
        show melody fufufu with dissolve
        unknown "Why would either of us ever have sex with you though?"
        unknown "Heheh, look at you, pushed down into a cleaning errand boy."
        unknown "Imagine if you were more charismatic, charming and good looking, you could have seduced my sister by now, but instead she's ignoring you and masturbating for strangers."
        unknown "At this rate, you'll always be  ignored, just like your little worm, although it's not exactly little anymore..."
        show melody closesadistic with dissolve
        "Ah crap, I may have half an erection. Guess I’m still not used to hanging around naked girls, not when they tease me at least."
        "Additionally, this entire time I can hear wet sounds from Ruby masturbating in the background."
        mc "Yeah I got stuck cleaning, but that’s what I’m here to do. I'm not here to seduce or sleep with anyone, I just want to get paid."
        unknown "You want to fuck though, don’t you?"
        mc "Huh? You?"
        show melody closedeath2 with dissolve
        unknown "Certainly not me, gross!"
        show melody closefufufu with dissolve
        $ melodyhandjob = 0
        jump melodyhandjob2
        label melodyhandjob:
            play music melodytheme fadein 3.0
            show bg boutiqueupstairs with dissolve
            show melody closefufufu with dissolve
            stop ambience fadeout 3.0
        label melodyhandjob2:
            unknown "Heheh, my sister… bet you want to ravage her…"
        "She gets really close, whispering in my ear, I can feel her hot breath against my skin. Every so often I can hear Ruby moan too. This is a nightmare situation I’ve stumbled into, perhaps this is karma."
        unknown "Go on, look at her, she's really desperate to have men look at her..."
        hide melody with dissolve
        show ruby camming2 with dissolve
        pause 1.0
        menu:
            "You're right, she's camming because she wants people to see.":
                unknown "Hehe, she also wants to earn money, if you want to keep watching her you'll have to pay up."
            "You're wrong, watching her like this is an invasion of privacy.":
                unknown "You may think that, but how could you possibly know what she thinks? Maybe she's really enjoying it..."
                mc "Doubt it..."
        hide ruby camming with None
        show ruby camming2 with dissolve:
            xpos 0
            ypos 0
        show melody fufufu with dissolve:
            xpos 800
            ypos 75
        unknown "My sister is always so needy for male attention, heheh, that’s the only reason she’d ever hire you…"
        "She’s walking circles around me, it’s quite unnerving."
        show melody death1 with dissolve
        unknown "But… Look at you, what kind of laboratory test tube did you stumble out of? Hmph."
        mc "Okay, that was a bit mean."
        show melody sadistic with dissolve
        unknown "Oohh, boohoo… Here, let me make it all better…"
        hide melody
        show melodyb handjob:
            xpos 725
            ypos 0
        show melody handjob2:
            xpos 725
            ypos 0
        with dissolve
        "She pushes me back against the wall and kneels down beside my erection, she leers at it with intrigue before daintily wrapping her cold fingers around my cock."
        unknown "Heheh, nice cock, I give it an 8/10."
        "Her cold fingers start to rub back and forth around my shaft all whilst she rubs herself."
        "What's more is I can still see Ruby through a crack in her door."
        show melody handjob1 with dissolve
        unknown "Mmm… I bet you want to slide this thing deep inside of her…"
        "I don’t resist, not because I’m enjoying myself, more because I’m surprised and bewildered."
        show melody handjob2 with dissolve
        unknown "She’s in heat you know… I bet her pussy is begging for it…"
        "I look down to see her hand grazing my shaft in slow teasing motions. My eyes then look up and once again through the crack of the door."
        "Ruby is enjoying herself a lot more with the vibrator this time, with her little sister's silence all I can hear are Ruby's cute moans."
        show melody handjob1 with dissolve
        unknown "Come on, admit it…"
        mc "Eugh… Admit what?"
        show melody handjob3 with dissolve
        unknown "You wanna fuck my sister, don’cha?"
        "She continues to make sadistic and smug faces while she teases me.."
        mc "Yeah…"
        unknown "Gross, gross! You’re no better than the stallions, always thinking with the head of their cock instead of the head of their body."
        "Her hand speeds up around my cock, like… really speeds up, she seems giddy. She's masturbating too, I can see them both masturbating..."
        show melody handjob2 with dissolve
        unknown "I can make it happen though…"
        mc "You can?"
        "I’m too distracted by her hand job to really form long sentences, it feels annoyingly good."
        show melody handjob1 with dissolve
        unknown "That’s right wormy boy, if you want, I’ll let you fuck my sister… All you need to do is accept a deal from me"
        mc "What’s the catch? Why would you let me?"
        show melody handjob3 with dissolve
        unknown "Come on now, I’m not so sinister that I’d need a catch… Heheh, what I have planned will benefit us both."
        mc "What's your plan?"
        show melody handjob2 with dissolve
        unknown "That's a secret, all you need to do is agree… Hehe"
        "I wait a few seconds before replying, not because I’m deliberating whether to go along with her or not, I’ve already decided. The wait is just in petty protest, the hand job doesn’t stop either, so that’s nice."
        menu:
            "It feels like I may be signing a deal with the devil."
            "I agree, what do you want me to do?":
                show melody handjob1 with dissolve
                unknown "Hehe, good boy..."
            "I'd much prefer to sleep with you.":
                show melody handjob1 with dissolve
                unknown "Hehe, your cock doesn't deserve this virgin pussy."
                unknown "Accept the deal however, and maybe I'll reconsider."
                mc "Okay, I accept."
                unknown "Hehe, good boy..."
            "I disagree, I'll sleep with Ruby, but I don't want your help.":
                show melody handjob3 with dissolve
                unknown "Fufufu, we have a troublemaker."
                unknown "Fine, do it your way, I'm excited to see the results."
        show melody handjob1 with dissolve
        unknown "Now close your eyes, and imagine this hand is Ruby's tight pussy."
        "She starts to speed up the hand job to an overwhelming degree."
        show melody handjob2 with dissolve
        unknown "Good boy, I want you to cum for me..."
        "If she keeps going like this, I’ll cum."
        unknown "Come on, come on, fill her pussy up!"
        "I can feel my orgasm welling up. I want to tell her to stop but it feels far too good."
        show melody handjob5 with cum
        play sound cum
        show melody handjob5 with cum
        play sound cum
        "Before I know it my vision is going white, my cock throbs and I start to ejaculate."
        show melody handjob5 with cum
        play sound cum
        show melody handjob5 with cum
        play sound cum
        "In her cool yet pleasant grip, my cock starts to shoot several loads onto the white carpet below. Generously of her, she keeps jacking me off throughout my entire orgasm, I’m ashamed to admit it feels fantastic."
        show melody handjob3 with dissolve
        unknown "You came so much… All onto our white carpet… Heheh, so pathetic…"
        scene bg boutiqueupstairs2
        show melodyb handjob
        show melody handjob1
        with dissolve
        stop ambience fadeout 10.0
        unknown "All this cum while spying and listening to my sister, gross!"
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        menu:
            "Actually, I was watching you rub your pussy.":
                unknown "Kehehe, were you now?"
                unknown "I hoped you enjoyed the show, I know I sure did. Although I think I'll finish up alone in my room."
            "I can't wait to fuck Ruby.":
                unknown "Kehehe, let me work my magic and you'll be balls deep in her."
        hide melodyb
        show melody happy
        with dissolve
        "She takes a step back away from me, removing her hand from my now flaccid penis; there isn't a single drop of cum on her."
        "To my surprise, she doesn't say anything else, she just stands there smiling."
        "Her smile isn’t infectious at all; it’s almost intimidating to wonder just what exactly she’s planning."
        unknown "We'll talk soon, 'kay?"
        hide melody with dissolve
        "She slinks away back into the cute pink and white room I’d seen previously, closing the door behind her with a distinct click."
        "… Uh, I’m not really sure what to do now."
        stop music fadeout 5.0
        "Though, in the corner of my eye, none other than Ruby appears with a somewhat bewildered expression."
        show ruby shocked with dissolve
        ruby "I- uh, thought I heard someone… You… must be… done?"
        mc "Finished, yes, I finished cleaning, I just came up to call for you."
        show ruby shy with dissolve
        play music boutique fadein 5.0
        ruby "Ah… I see."
        "She looks somewhat distressed, no doubt she’s worried whether I saw her masturbating on camera."
        show ruby embarrassed with dissolve
        ruby "I was just going to make some lunch, come with me, darling."
        mc "Sure thing, that sounds great."
        show ruby happy with dissolve
        "She takes a step forward, stepping onto the carpet where I had just ejaculated. Oh, come on, what kind of ridiculous series of unfortunate events is this?"
        "Thankfully she doesn’t notice at all."
        show bg boutiquekitchen with dissolve
        "We go downstairs to her kitchen; I finally have a chance to honestly breathe clearly. It felt like I was holding my breath that entire time."
        "I practically slump back in one of Ruby’s kitchen chairs and peek at the trees outside while she makes sandwiches. Not exactly the meal I was expecting, but grateful nonetheless, she even cuts the sandwich into rectangles, cute."
        show ruby shy with dissolve
        ruby "Did you see anything?"
        mc "Hm, you mean while cleaning up?"
        show ruby embarrassed with dissolve
        ruby "No, darling, I mean upstairs…"
        "Hadn’t anticipated her confronting me like this, I hope she doesn’t have a pension for sadism like her little sister. Gosh, it just occurred to me that I didn’t even catch that demon’s name."
        "Either way, I hadn’t prepared an excuse for this and my growing silence is all too showing."
        mc "Well… I saw your sister, I guess."
        show ruby shocked with dissolve
        ruby "Melody? I wasn’t expecting her back this early."
        "That’s a surprisingly sweet name for evil incarnate."
        show ruby shy with dissolve
        ruby "*Sigh*, how unfortunate, both you and Melody were there? I left my door slightly open just in case you called for me but…"
        mc "No, no, she didn’t see much, she went straight to her room in fact, I walked up to your room alone."
        "Is it really my place to lie here? Just to make Ruby feel better..."
        show ruby angry with dissolve
        ruby "Well, as long as Melody didn’t see or hear anything. I can tell you’re hiding something though, it’s written on your face."
        "She has a sharp mind, there's no hiding this from her."
        mc "Yeah, I may have briefly caught a glimpse of something."
        show ruby sad with dissolve
        ruby "I see... I was half tempted to tell you anyway."
        ruby "I was doing a cam show, a show where I masturbate on camera and people can donate money or something..."
        mc "I see… I’m somewhat familiar with those."
        show ruby neutral with dissolve
        ruby "Yes… I'm sorry you had to see a lady like me doing something so… vulgar."
        ruby "When Penelope mentioned she had a male that needed work, I figured that’d be the perfect opportunity to try and lift my feeble camgirl career off the ground."
        show ruby shy with dissolve
        if bakeryvisit1 == 1:
            ruby "When I saw you at the party, I chickened out... I misread Penelope's letter and thought you were..."
        else:
            ruby "I chickened out when I saw you darling, I misread the letter and thought you were…"
        ruby "Well, a stallion..."
        mc "I guess I’m a unique flavour, isn’t that a good thing for a cam stream though?"
        show ruby neutral with dissolve
        ruby "I’m not entirely sure, it’s a new and scary experience for a lady like myself."
        "Today is a rollercoaster, with twist after twist."
        "First I discovered that Ruby was a camgirl."
        "Then Melody offered me that deal, somehow she'll make Ruby sleep with me."
        "Oh, and she jacked me off onto the carpet, what the heck was that all about? It was hot though."
        "Then Ruby found out that I saw her show."
        "And now I'm discovering that she initially hired me to take part in the show, but she had a change of heart last second."
        "Where do I even begin, I have plenty of questions now."
        mc "You don’t mind if I ask a few questions right, Ruby?"
        show ruby shy with dissolve
        ruby "Not at all darling, it’s the least I can do after dragging you here and wasting your time."
        mc "I was under the impression that you were a designer, running a boutique, is that not the case?"
        show ruby neutral with dissolve
        ruby "Hmm… *Sigh*, it was the case, it somewhat is the case. Unfortunately, I’m ahead of my time, I design luxurious clothes but there’s no pony to wear them."
        ruby "I’ve tried to shimmy my way into the tight echelons of upper-class pony society, but my name isn’t particularly recognised or respected… yet…"
        show ruby shy with dissolve
        ruby "I do work here and there, a few days a week, but it doesn’t pay the rent."
        mc "That’s really unfortunate, so the camgirl business is to pay the rent?"
        show ruby angry with dissolve
        ruby "Yep, a lady like myself, masturbating on a camera for the public to enjoy, just to try and pay my bills. You must think of me as repugnant."
        mc "Not at all, I highly respect what you’re doing."
        show ruby sad with dissolve
        ruby "Respectable? It’s laughable honestly; no one watches me, I only have five regular viewers."
        "It took a few seconds for all the puzzle pieces to connect in my head. Camgirls in my world are highly successful, but in this world, who’s their audience? The tiny in-demand population of men? Not likely."
        "I certainly wouldn't watch a camgirl in this world, I'd just go outside."
        "In this world, the audience for cam shows is going to be predominantly female. So there are probably a lot more camguys than camgirls."
        "No wonder she wanted to hire me, a lone girl camming won’t be in demand, but a straight sex stream. That’s the mother lode."
        mc "Are you not earning enough?"
        show ruby shy with dissolve
        ruby "It’s… tight. It’s barely enough, but I’m living paycheck to paycheck."
        mc "That’s rough, I wish there was a way I could help."
        show ruby neutral with dissolve
        ruby "Ah, it’s fine… Just let it be known that I can’t pay you much."
        mc "I understand, you probably won’t want me to come back, then."
        show ruby sad with dissolve
        ruby "Yeah, sorry for wasting your time, darling."
        ruby "Here, I’ll give you 5 monies for cleaning up, you did a wonderful job."
        "She hands me a rather measly pay; this is barely enough to cover groceries. I don’t mind though; I can’t exactly ask her for more."
        hide ruby sad with dissolve
        stop music fadeout 5.0
        "Ruby says her goodbyes and returns upstairs, presumably to continue her camming, sandwich and tea in hand."
        "I was tempted to ask if I could cam with her, but she would have let me if that's what she wanted."
        "I finish my tea and sandwich, and I guess it’s about time I headed out. I wonder if I can go work somewhere else for half a day to earn a little more, maybe Honeycrisp’s farm? Her schedule would be the most flexible."
        show bg boutiqueinside with dissolve
        "I get up to leave and as I walk into the main room that I had tidied up earlier, I spot the sinister girl from before. Melody sat at a table on a laptop."
        play music melodytheme fadein 5.0
        show melody closesadistic with dissolve
        melody "Ohh, finished preying on my sister? You dirty lil’ perv."
        mc "Preying? You’re the one with a self-proclaimed plan to get us to have sex, and I think I figured out why."
        show melody closefufufu with dissolve
        melody "Mhm, I guess that post-ejaculation clarity helped you figure it out."
        show melody closesatisfied with dissolve
        melody "We're both struggling financially, so like I said before, my plan will benefit both of us."
        melody "You live across from us with Moxie right? You don't even own a house... You'll probably want some extra money then."
        if livingwithbutters == 1:
            "I'm actually lodging with Butters right now, but I don't tell her that."
        show melody closeneutral with dissolve
        melody "So I want you to take this, and come back the next time you’re available."
        "She leans over into her bag and empties her purse, totalling 20 monies which she hands me."
        "I’m shocked at her sudden generosity, this is four times the amount Ruby gave me."
        mc "Uhm… Thank you, that's really kind, Melody."
        show melody closehappy with dissolve
        melody "Don’t thank me, this is a bribe to get you to come back. I heard what you said to Ruby."
        show melody closefufufu with dissolve
        melody "You will come back and play, won’t you?"
        mc "Yeah, I’ll be back, any idea what will happen? I'm assuming I'll be helping Ruby with her stream."
        show melody closehappy with dissolve
        melody "Shh, that’s the secret, be a good boy and just come."
        "She’s making me nervous, yet I have 25 monies in my hand right now, I’m in a situation where I can’t refuse, can I?"
        show melody closefufufu with dissolve
        melody "What’s the matter, cat got your tongue?"
        mc "Sorry, I was just thinking."
        show melody closesadistic with dissolve
        melody "Want me to come over and sit on your lap? Would that get the blood flowing into your brain?"
        "I can’t help but peek at her butt and imagine what it’d be like if her soft cute ass was nestled against me. As evil as she is, she’s extremely attractive like her sister. She keeps her legs crossed though, so I don’t see much else."
        show melody closedeath1 with dissolve
        melody "Oh Aurora, I can feel your lecherous gaze all over my body, so gross, gross!"
        show melody closefufufu with dissolve
        melody "It is a nice butt though, isn't it?"
        "I wonder what would happen if I actually called this girl’s bluff."
        mc "Does that mean you’re not going to sit on my lap?"
        melody "Do you want me to?"
        mc "Sure."
        show melody closedeath2 with dissolve
        melody "Heheh… So disgusting! I can’t believe you’d think I’d do something like that, I can even see your gross little worm getting bigger, there’s no way I’m sitting on that!"
        "So, she definitely bluffs, for the first time all day her insults fall rather flat and feel somewhat forced. Even a girl like this is fallible."
        "She was right about one thing though, I’m annoyingly getting erect again. I can't stop thinking of that handjob she gave me, that was hot."
        show melody closesadistic with dissolve
        melody "You should leave but… If you leave now everyone will see your pathetic little worm in its half erect state…"
        mc "Oh yeah, are you going to do something about it?"
        show melody closesadistic with dissolve
        melody "I think I’d prefer to just watch you squirm honestly, in a perpetual state of being unable to get soft and leave but unable to get off either."
        mc "That’s rather sadistic, are you just gonna sit there and bully me this entire time while browsing the internet?"
        show melody closehappy with dissolve
        melody "I just like the cute ways you squirm. You’re so pitiful."
        show melody closesatisfied with dissolve
        melody "I bet you’re only here hoping you can sleep with some mares in heat, I know your type."
        mc "That’s not true, I’m trapped here from another world. Anyway, you’re being a hypocrite."
        show melody closesurprised with dissolve
        melody "Trapped? Another world? Don’t tell me you’re crazy too."
        mc "You’re a unicorn, you tell me. I was teleported here from a faraway place by Moxie."
        show melody closesatisfied with dissolve
        melody "Hmm, don’t care."
        mc "… Well, what about the fact you’re a hypocrite, letting me sleep with your sister?"
        show melody closefufufu with dissolve
        melody "Pfft… Is that the only thing you can keep talking about? Sleep with my sister, sex this, sex that. You’re kind of disgusting."
        mc "I just mentioned something else and you told me you don't care."
        mc "I don’t get you at all."
        show melody closedeath1 with dissolve
        melody "No, and you will never get me, I’m way out of your league, wormy boy."
        "In my frustration I seem to have gone totally flaccid, so I’ll take this opportunity to dip out and go back home."
        mc "I’m leaving."
        show melody closedeath2 with dissolve
        melody "Do come back…"
        hide melody with dissolve
        show bg worldmapdialogue with dissolve
        stop music fadeout 3.0
        play ambience ambienceday fadein 3.0
        "I head out of the boutique in a huff."
        "This was not the experience I was expecting when I decided to work there. It felt pointless, humiliating and frustrating."
        "The serene princess-like beauty and politeness of Ruby contrasted with that she-devil. Well, actually Ruby wasn’t that polite, but in contrast to Melody anyone can seem polite."
        "Yet… I grasp in my right hand, 25 monies. Why in that brief moment was Melody so generous? And why did she give me a handjob?"
        "She seems like someone that always has an ulterior motive, so despite this generosity I can’t take it as genuine good grace."
        "Even so, just for a moment, the look in her eyes and her voice was so sincere..."
        "I need to talk to someone about this, clear my head."
        show bg black with dissolve
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        "…"
        if livingwithmoxie == 1:
            play music day2
            show bg worldmapdialogue with dissolve
            "Turns out I have hours and hours before Moxie gets back, so I decide to fill the time by going on a walk."
            "Moxie wasn’t lying when I said I might get approached by girls, I've had a few passing conversations with curious strangers and even been asked on a date."
            "But I’m not particularly in the mood for a fling with a random mare... At least not right now."
            show bg farm2 with dissolve
            "I just want a relaxing walk to clear my head, so I step out of the suburbs and take a walk around the surrounding fields and wooded areas."
            show bg farm4 with dissolve
            pause 1.5
            stop music fadeout 3.0
            play ambience ambiencenight fadein 3.0
            show bg farm6night1 with dissolve
            pause 3.0
            play music wagon fadein 3.0
            show bg moxiewagonlamp with dissolve
            "When I return to the wagon, I’m feeling much better."
            "When Moxie returns, I have to take a moment to really consider whether or not I should tell her about the oddity that was today."
            show moxie closelaughing with dissolve
            moxie "Hey tiger, how was work today?"
            "If I can’t be honest with her, I can’t be honest with anyone."
            mc "Today was strange, I went to the boutique but Ruby ended up telling me to go home because there was no work to do."
            show moxie closeneutral with dissolve
            moxie "Ah… So, you didn’t get paid?"
            mc "That’s the weird thing; I did get paid, but not by Ruby, by her little sister."
            show moxie closeshy with dissolve
            moxie "Little sister, hmm... Her name escapes me, I know she goes to the college I’m trying to apply for."
            show moxie closeneutral with dissolve
            moxie "That's weird though, what happened?"
            mc "Her name is Melody and yeah it’s weird because… I didn’t do anything. She just gave me the money and told me to come back, even though Ruby has no work for me."
            show moxie closehappy with dissolve
            moxie "Heh, the way I see it, money is money! Mares can get weird around guys sometimes, I act pretty weird when I’m around you too, got me thinking."
            show moxie closelaughing with dissolve
            moxie "The way I act around you doesn’t obey my usual personality or the self-image of myself, yet naturally I act differently around you, more open and honest than I ever have been before."
            "Usual personality… That’s right, there was a brief moment Melody seemed kind and sympathetic earlier today; if Moxie naturally acts differently around me, maybe Melody does too."
            "After all, Ruby gave me no cause for concern in regards to Melody’s behaviour, it seemed to be a wholly unique treatment towards me. There’s only one way to find out though."
            mc "What do you know about Melody, like, everything?"
            show moxie closeneutral with dissolve
            moxie "Uhm, what I know is residues from conversation with Honeycrisp and Riku. I know she studies music, I think she’s quite sweet too, gets along with everyone, has plenty of friends."
            show moxie closealthappy with dissolve
            moxie "If she’s at that college then there’s no doubt she’s talented in some way."
            mc "Ohh, I see, that’s quite inspiring."
            "It’s clear I’m not getting the full picture. Obviously Melody has a motive, but I doubt it’s a malicious supervillain motive, she’s just frustrating to be around."
            "I feel like I’ve overlooked one crucial detail for a while now just because it was so alien to me, but the hand job she gave me was perhaps the strangest experience in my life."
            mc "You mentioned you get woozy around me earlier, and you said some mares do get weak at the knees when around a man during this season, but have you ever heard of girls getting aggressive?"
            show moxie closeangry with dissolve
            moxie "Aggressive? Is Melody causing you trouble? I’ll kick her ass."
            mc "No, no trouble, she’s just behaving in an unusual way."
            show moxie closeembarrassed with dissolve
            moxie "Uhm, well I don’t know, arousal and horniness aren’t really emotions, they may influence emotions, perhaps make certain ones stronger or weaker."
            mc "I think Melody wants me back for some kind of scheme of hers, should I be careful?"
            show moxie closehappy with dissolve
            moxie "Nah, if she’s messing around with you it’s probably just in harmless jest, I haven’t heard anything bad about those two. At most she’s horny and wants a cute boy like you around again, I’d say go for it."
            mc "Hmm, maybe she’s horny, but she’ll just tease and mess me around."
            show moxie closealthappy with dissolve
            moxie "It’s up to you whether you want to go down that rabbit hole, I know for a fact that my curiosity would get the best of me in a situation like that, I say go for it."
            scene bg black with dissolve
            "…"
            jump evening
        elif livingwithbutters == 1:
            play music day2
            show bg worldmapdialogue with dissolve
            "Turns out I have hours and hours before Moxie gets back, so I decide to fill the time by going on a walk."
            "Moxie wasn’t lying when I said I might get approached by girls, I've had a few passing conversations with curious strangers and even been asked on a date."
            "But I’m not particularly in the mood for a fling with a random mare."
            show bg farm2 with dissolve
            "I just want a relaxing walk to clear my head, so I step out of the suburbs and take a walk around the surrounding fields and wooded areas."
            show bg farm4 with dissolve
            pause 1.5
            stop music fadeout 3.0
            play ambience ambiencenight fadein 3.0
            show bg farm6night1 with dissolve
            pause 3.0
            play music butters fadein 3.0
            show bg buttershousenight with dissolve
            "When I return to the wagon, I’m feeling much better."
            "When Butters returns, I have to take a moment to really consider whether or not I should tell her about the oddity that was today."
            show butters closedresslaughing with dissolve
            butters "Hey [playername], how was work today?"
            "If I can’t be honest with her, I can’t be honest with anyone."
            mc "Today was strange, I went to the boutique but Ruby ended up telling me to go home because there was no work to do."
            show butters closedressneutral with dissolve
            butters "Ah… So, you didn’t get paid?"
            mc "That’s the weird thing; I did get paid, but not by Ruby, by her little sister."
            butters "You mean Melody? Why did she give you money?"
            mc "Yeah it’s weird because… I didn’t do anything. She just gave me the money and told me to come back, even though Ruby has no work for me."
            show butters closedresshappy with dissolve
            butters "That's interesting... Maybe it's something to do with her heat?"
            mc "Do you think she's using me as a prostitute?"
            butters "Hehe no, no... Heat's weird, I've even noticed some differences in my personality when I'm around you."
            show butters closedresslaughing with dissolve
            butters "The way I act around you in heat isn't always 'me'. I can't help but act differently around you, less shy than ever before.."
            "That’s right, there was a brief moment Melody seemed kind and sympathetic earlier today; if Butters naturally acts differently around me, maybe Melody does too."
            "After all, Ruby gave me no cause for concern in regards for Melody’s behaviour, it seemed to be a wholly unique treatment towards me. There’s only one way to find out though."
            mc "What do you know about Melody, like, everything?"
            show butters closedressneutral with dissolve
            butters "Uhm, I don't know much, even though I was quite close friends with Ruby. I know she studies music, I think she’s quite sweet too, and has plenty of friends."
            show butters closedresshappy with dissolve
            butters "If she’s at that college then there’s no doubt she’s talented in some way."
            mc "Ohh, I see, that’s quite aspiring."
            "It’s clear I’m not getting the full picture. Obviously Melody has a motive, but I doubt it’s a malicious supervillain motive, she’s just frustrating to be around."
            "I feel like I’ve overlooked one crucial detail for a while now just because it was so alien to me, but the hand job she gave me was perhaps the strangest experience in my life."
            mc "You mentioned you get woozy around me earlier, and you said some mares do get weak at the knees when around a man during this season, but have you ever heard of girls getting aggressive?"
            show butters closedressangry with dissolve
            butters "Aggressive? Was Melody aggressive?"
            mc "No, not aggressive, she’s just behaving in an unusual way."
            show butters closedresssurprised with dissolve
            butters "Uhm, well I don’t know, arousal and horniness aren’t really emotions. But I know they can certainnly influence emotions, perhaps make certain ones stronger or weaker."
            mc "I think Melody wants me back for some kind of scheme of hers, should I be careful?"
            show butters closedresshappy with dissolve
            butters "If she’s messing around with you it’s probably harmless, I haven’t heard anything bad about those two. At most she’s horny and wants a cute boy like you around again, I’d say go for it."
            mc "It can't be any more dangerous than cave diving with you."
            butters "Heh, I told you that's not dangerous!"
            mc "Yeah, yeah..."
            scene bg black with dissolve
            "…"
            jump evening
        else:
            pass
    label boutiquevisit2:
        "Down the rabbit hole, let’s see what Melody and Ruby are up to at the boutique."
        "They live right next to the wagon, so it’d be nice to become good friends with them."
        "I honestly have no idea what to expect."
        stop music fadeout 5.0
        show bg boutiquedoor with dissolve
        "As I go to knock on the door, I dread Ruby opening the door and asking me what I’m doing back. Worst case scenario I go somewhere else with my non-existent tail tucked between my legs. I wonder if that saying works in this world."
        "It sounds ridiculous, but right now I’d much rather talk to Melody and figure out what she wants."
        play sound knock
        play sound knock
        play sound knock
        "I knock on the door and Ruby is the one that greets me rather cheerfully."
        play music boutique fadein 5.0
        show ruby laughing with dissolve
        ruby "Oh goodness, it’s you. Darling, I’m so glad you came."
        show ruby happy with dissolve
        ruby "We got off to such a bad start, I’m so sorry. Come on in! Allow me to make you a drink."
        "Woah, okay... I haven’t even said anything yet and I’m having admiration and positivity thrown my way. This is the direct opposite to her dreary attitude last time."
        "And again, just like last time, I can tell there’s something wrong here."
        mc "Hello Ruby, I uh…"
        "Crap, I didn’t even prepare anything to say, I cut myself short just before I said I’m here to work for the day. I can’t just admit I’m here because Melody told me."
        mc "Uh… I’d love some tea, thank you so much."
        hide ruby with dissolve
        show bg boutiqueinside with dissolve
        "I head through the main room which has basically been untouched, I can’t discern a single change since the last time I was here."
        if barvisit1 == 1 and maiddressbought == 0:
            mc "Hey Ruby, before get any tea, I'm looking to buy something."
            "I need to get a 'slave' outfit for Riku's truth or dare punishment."
            show ruby shocked with dissolve
            ruby "Oh! You're here as a customer, I didn't realize."
            mc "Well uh, what else would I be here for?"
            show ruby laughing with dissolve
            ruby "Ahah, of course darling! I may even throw in a discount for a dear such as yourself. What would you like to buy?"
            mc "I'm looking for a maid dress."
            show ruby happy with dissolve
            ruby "Of course darling... Hmm, Melody had a maid dress for halloween once, ah, here it is."
            "She walks over to a rack and takes one out to show me, it's perfect."
            ruby "Naturally this dress fits Melody's small figure and bosom, is that okay?"
            mc "Yeah that's perfect, how much is it?"
            ruby "Second hand? 50 monies should cover it."
            menu rubymaidmenu2:
                "I have [monies] monies."
                "Buy the dress (-50 Monies)" if monies >= 50:
                    if monies < 50:
                        "I can't afford it."
                        jump rubymaidmenu2
                    $ maiddressbought = 1
                    ruby "Pleasure doing business with you darling."
                    mc "By the way, can you leave the dress here?"
                    ruby "Here? Do you want to pick it up at a later time?"
                    mc "Yes, you'll see."
                "Maybe later":
                    ruby "Okay darling, maybe another time."
            hide ruby with dissolve
            "With that matter sorted, the two of us make our way to the kitchen."
        else:
            pass
        show bg boutiquekitchen with dissolve
        "In the kitchen, Ruby begins making a pot of tea. Before she had only made cups, so I can only assume she plans to talk to me for a little longer than before."
        "That being said, I truly have prepared nothing to say."
        show ruby embarrassed with dissolve
        ruby "Make yourself at home darling, you did a wonderful job tidying up, it was shameful of me to not even notice and thank you properly last time."
        show ruby shy with dissolve
        ruby "I was so preoccupied with my stupid cam show that I wasn’t focusing on what was right in front of me all along."
        mc "It's okay, you don't need to worry yourself over my well-being."
        show ruby happy with dissolve
        ruby "Oh dear, look at me getting ahead of myself."
        show ruby shy with dissolve
        ruby "My friend, you stepped into my boutique, offered yourself to me. And yet I refused, sending you home."
        show ruby happy with dissolve
        ruby "I realize that was a mistake."
        "I didn’t really offer myself to her, but I’ll play along."
        mc "What are you getting at, Ruby? What do you want me to do?"
        "She takes a sip of her tea, she has a smug yet regal aura, although simultaneously she seems fidgety."
        show ruby laughing with dissolve
        ruby "I need a photographer, to take pictures of me while I’m modelling, it’s something I can’t do effectively myself."
        mc "That sounds easy enough, why didn’t you ask me to do that last time?"
        show ruby happy with dissolve
        ruby "I was too nervous darling; my modelling and cam-show are closely held secrets."
        show ruby horny with dissolve
        ruby "But you already discovered my little secret, so I have nothing to lose."
        mc "Makes sense to me. I recall you mentioned you were tight on cash, so I hope I can earn you some money."
        show ruby happy with dissolve
        ruby "I’m sure you will, darling."
        "I take a sip of tea and ponder the situation. This change of heart must be Melody’s influence."
        "Never thought I’d do something like photographing a model. Seems easy enough."
        "Has Melody really done it? Is Ruby really going to have sex with me?"
        show ruby laughing with dissolve
        ruby "Okay dearie, lets take our tea upstairs and prepare the set."
        "Oh my gosh, this is really happening."
        hide ruby laughing with dissolve
        pause 0.3
        show bg boutiqueupstairs with dissolve
        pause 0.5
        show bg rubybedroom with dissolve
        pause 0.5
        stop ambience fadeout 60.0
        "We go upstairs and settle in her bedroom, she doesn’t bother turning on the lights, there’s just a blue glow coming from her laptop."
        "She starts moving some cushions around and generally tidying up. Surprisingly it’s not that messy in here compared to the state the ground floor was when I first arrived."
        "I spot a camera on a desk, I’m guessing this must be the one I’ll be using, so I fiddle around with it and get a feel for its controls."
        "I watch through the lens as Ruby dresses herself in some lingerie stockings and evening gloves. Despite the fact she’s now wearing clothes, it’s admittedly sexier."
        show ruby lingerieembarrassed with dissolve
        ruby "Ah, perfect, you already have the camera. Uhm, hmm…"
        mc  "Wow, I love your lingerie, Ruby."
        show ruby lingerielaughing with dissolve
        ruby "Thank you darling, this is my own design."
        mc "Are these photos for modelling your clothing, or for your… well, more vulgar purposes?"
        show ruby lingeriehorny with dissolve
        ruby "Modelling and vulgar purposes darling, I’m going to sell naughty pictures of myself to try and earn some more money while showing off some clothes I made myself."
        show ruby lingerielaughing with dissolve
        ruby "Ohoho, delightfully devilish Ruby, killing two birds with one stone, they’re sure to eat this one up."
        mc "I’m not really sure what to do, but I’ll try to take some artsy shots. Ready?"
        show ruby lingeriehappy with dissolve
        ruby "Ah, yes. Sorry, I don't have much experience with lewd photography, other than silly selfies for my ex. I’m not really sure how I should pose."
        ruby "Why not take a picture now?"
        mc "Of you standing? Alright."
        show ruby lingeriehorny with cum
        show ruby lingeriehorny with cum
        "Ruby doesn’t move much while I take a few pictures of her."
        "The result is a few simple shots that show off her lingerie."
        $ rubyphotoshoot = 0
        jump rubyphotoshoot2
        label rubyphotoshoot:
            show bg rubybedroom with dissolve
            stop ambience fadeout 10.0
            play music boutique fadein 3.0
        label rubyphotoshoot2:
            show ruby lingerielaughing with dissolve
        ruby "Okay, uhm… How about my boobs, can you get a close up?"
        mc "Sure, just let me figure out which button zooms in…"
        show ruby lingerieembarrassed with dissolve
        ruby "No, don’t zoom in, come closer dearie."
        show ruby boobs with dissolve
        pause 1.0
        "I get much closer to her and look directly at her breasts, her nipples are erect, but I imagine that’s fairly normal."
        "Up close she smells pleasantly sweet and fruity."
        show ruby boobs with cum
        show ruby boobs with cum
        "*Snap*, some more pictures of her breasts, simple enough. I guess this isn’t too different from erotic modelling in my world."
        ruby "Okay, you’ll have to get lower too, to take a picture of my… you know, lady parts."
        mc "A close up down here too? Sure thing."
        show ruby pussy with dissolve
        pause 1.0
        "I kneel down and start taking pictures of her pelvic area. Being so close to her pussy is rather intoxicating but I stay professional."
        show ruby pussy with cum
        show ruby pussy with cum
        "It takes some willpower to not get an erection."
        hide ruby pussy with dissolve
        show ruby lingeriehorny with dissolve
        mc "There we go. Now we’ve had some closeups, are you going to do some poses now?"
        show ruby lingerielaughing with dissolve
        ruby "Wonderful idea, [playername]! I don’t know many poses, I haven’t prepared but, I think… Ah, come over here darling, on my bed."
        hide ruby with dissolve
        "Despite the fact she told me she was penny pinching; her bed is ridiculously nice."
        "I’ve never seen a bed with curtains before, seems cosy. It’s the kind of bed I’d assume you’d see in a castle."
        show bg rubybedroom2 with dissolve
        show ruby photoshoot2 with dissolve
        "I’m somewhat distracted by her bed, when I return my view to Ruby she’s posing most erotically, her legs spread with her pussy on full display."
        "I’d be lying if I said I didn’t feel aroused."
        ruby "How’s this pose? All my naughty bits are on display, perfect for turning on any men watching me."
        mc "Just lift your right leg up a bit more… "
        ruby "Ohoho, I feel so exposed right now darling... How's this?"
        mc "Perfect."
        show ruby photoshoot2 with cum
        show ruby photoshoot2 with cum
        "*Snap*, *Snap* I take a few pictures, capturing a few angles."
        ruby "Ahh… Make sure you get a good shot of my vulva darling; I don’t mind if you get up close and personal."
        show ruby pussy2 with dissolve
        "I’m tempted to get remarkably close and personal. It’s dark but it’s rather apparent that she’s wet."
        mc "If I get too close, I won’t be able to pull myself away."
        show ruby pussy2 with cum
        show ruby pussy2 with cum
        "Giving in, I take some close ups of her naughtiest parts. While taking a close up shot of her vulva I can definitely feel the blood pumping in my nethers. If this kept going, I’ll become uncontrollably erect."
        ruby "Don’t worry if this turns you on darling, it's perfectly normal for a man such as yourself to feel that way near a lady such as myself..."
        mc "Looks like you’re getting turned on too."
        show ruby photoshoot2 with dissolve
        ruby "A lady doesn’t tell!"
        hide ruby with dissolve
        ruby "Let’s keep going, another pose."
        show bg rubybedroom with dissolve
        show ruby photoshoot1 with dissolve
        "Ruby energetically bounces off the bed and up to a mirror. She looks back and spreads her rear as I walk over to join her."
        ruby "Backside picture this time, could you kneel down and get a good shot from below? It’ll make my derrière look even bigger."
        mc "Your ass looks great either way."
        show ruby photoshoot1 with cum
        show ruby photoshoot1 with cum
        "I kneel down to get a dynamic shot from below, her ass looks amazing from this angle."
        "Her pussy is so wet; it's dripping."
        "It looks so tight too. I can't even imagine how good it'd feel to sink my cock deep into her."
        ruby "Come on sweetie, take the picture."
        mc "Sorry, you caught me admiring."
        show ruby photoshoot1 with cum
        show ruby photoshoot1 with cum
        stop music fadeout 10.0
        ruby "Oh, you flatter me, darling."
        "As I take a few more pictures, it’s apparent that I’ve become erect, and she’s aroused too. Sex is certainly inevitable."
        "I catch her trying to take a sneaky peek at my erection, she bites her lip as she does."
        ruby "You really like my ass… Don’t you?"
        mc "I think you see something you like too."
        ruby "Mmm, ‘like’ would be an understatement, darling."
        ruby "I love it when people get turned on looking at my body."
        ruby "Don’t you want to rub your cock while you watch? I bet you do; this must be torture…"
        "She’s right, I really do. I bring my hand to my shaft and start masturbating while Ruby seductively jiggles her butt right in front of me."
        ruby "I feel the same way too, you know... I want to touch myself while you watch."
        ruby "Everyone thinks I’m an innocent mare, but really I’m just a dirty slut that gets off on being watched."
        ruby "I know you heard and saw me while I was doing my cam show."
        ruby "The idea that a man was in my house watching me masturbate… It turned me on so much, I needed you back so I could play with you."
        mc "Oh yeah? Show me what you’ve got."
        ruby "Oh I will darling, we're not done yet."
        ruby "Lay down on my bed with the camera."
        hide ruby with dissolve
        "I follow her instructions and she brings her laptop with her as she seductively catwalks to the bed."
        play music sex1 fadein 10.0
        show ruby lingeriehorny with dissolve
        ruby "Truth is, when Penelope told me there was a man that wanted work, I was filled with lustful thoughts."
        ruby "I want you to record me while I ride your cock, can you do that for me, [playername]?"
        mc "Absolutely…"
        hide ruby with dissolve
        show bg rubybedroom2 with dissolve
        "..."
        show ruby sexlipbite with dissolve
        play sound cum
        "As she sinks that tight pussy over my cock, it feels as good as I imagined."
        ruby "Hit record now, love."
        "I lay down comfortably with a pillow on my head and point the camera at our point of contact."
        ruby "Just sit back and relax dear, I’ll be teasing you a lot, try not to cum prematurely."
        play ambience sex fadein 3.0
        show ruby sexofacedeep with dissolve
        show ruby sexoface with dissolve
        "Ruby rides my cock up and down slowly, it’s more teasing than pleasureful."
        ruby "Oh gosh, this is making me horny."
        ruby "Hornier than I already was… *Pant*"
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        "She starts to grind against my shaft more vigorously, some precum oozes from the point of our contact causing my cock to glisten."
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        "I can tell she has some experience. However, she still feels remarkably tight, her inner walls squeezing and sucking around my throbbing shaft."
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        ruby "Ohoh gosh, I-I forgot how… Ahhh, I forgot how good this is!"
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        "She works my cock with her ass, sliding herself up and down in slow sensual erotic motions that are enough to send bolts of potent pleasure surging throughout my body."
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        "I definitely wasn’t wrong about Ruby having sexual experience, her motions and technique is exquisite. Rather than a sloppy fuck it feels like her pussy is expertly massaging my shaft in smooth, passionate motions."
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        ruby "Mmmphh… You’re so thick, far better than a stallion…"
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        ruby "Tell me darling, be honest, just how much did you see when you were watching me through my doorframe?"
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        "Seems like a strange thing to ask while she’s riding my cock. I guess she did mention she gets off on being watched."
        show ruby sexofacedeep with dissolve
        show ruby sexofaceaction with dissolve
        mc "I saw everything, I watched you use your vibrator. I could see your legs were spread wide open."
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        "She speeds up slightly, these thoughts seemingly getting her even more excited."
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        ruby "Ohh, so dirty… Ahhh, ahh… ah! Did… Did that turn you on?"
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        mc "Yeah, I had an erection while watching."
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        ruby "Oh gosh, oh… fuck. That’s hot, ahh… T-The same erection I’m riding right now, haah… I’m living out my own fantasy."
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        "That really got her going, now she’s fucking me vigorously, I try my best to keep the camera steady as she relentlessly rides my cock."
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        "I don’t know how long this video has been recording, but I feel close to cumming. I try to hold back for as long as possible, but Ruby is unyielding in her expert riding technique and her speed."
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        ruby "Ahh, I-I think I’m actually coming! D-Darling… Ahhh."
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        "I can feel her tighten as she climaxes, and despite her orgasm, she doesn’t miss a beat while riding me."
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        ruby "Ahh, so good! *Slap* *Slap* *Slap*"
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        show ruby sexahegaodeep with dissolve
        show ruby sexahegaoaction with dissolve
        "The combination of her moans and her contractions are pushing me over the edge, I can’t hold back any longer."
        show ruby sexahegaocumdeep with cum
        show ruby sexahegaoactioncum with dissolve
        show ruby sexahegaocumdeep with cum
        show ruby sexahegaoactioncum with dissolve
        "I orgasm, ejaculating inside of her while she continues to ride me, causing a sloppy mess of my cum that bubbles and seeps out of her."
        show ruby sexahegaocumdeep with cum
        show ruby sexahegaoactioncum with dissolve
        show ruby sexahegaocumdeep with cum
        show ruby sexahegaoactioncum with dissolve
        ruby "Ohh, yes… Mmm…"
        show ruby sexlipbitecum with dissolve
        stop ambience fadeout 3.0
        "She slowly comes to a stop and catches her breath as I stop recording."
        ruby "Hehe, look how much you came..."
        ruby "Darling, you are a wonderful sex partner…"
        mc "You were amazing too; you played my cock with your ass like it was a musical instrument."
        show ruby sexpccum with dissolve
        "She takes the camera from me and plugs it into the laptop, copying the video files over. Although this doesn't stop her from remaining sat on my cock."
        ruby "You lasted so much longer than those one-pump-dump stallions. I actually came during penetration; I wasn’t expecting that."
        mc "What are you going to do with the video?"
        show ruby sexlipbitecum with dissolve
        ruby "I’ll probably take a screenshot of the video, maybe a five second preview, and try to sell it. Hopefully it should appeal to a larger market than my cam shows."
        mc "Yeah, I’ll appeal to that massive female audience. That’s the important one."
        show ruby sexpccum with dissolve
        ruby "Hmm… Cam shows and female audience…"
        show ruby sexlipbitecum with dissolve
        ruby "Darling, how long are you here to work for?"
        mc "Ideally from 9 till 5. I guess that’s a lot of time to fill if you were only planning on taking some pictures and videos to sell."
        ruby "I usually start my cam show at this time; if I paid you, would you join me on the cam show?"
        mc "Thing is, I’m quite recognizable, so I’d absolutely need to hide my face."
        ruby "But of course darling, all I need is your... heh, you know."
        ruby "It’s quite a lucrative opportunity, I’ll be sure to pay you what you deserve."
        mc "Alright, I’d be happy to do it."
        show ruby sexpccum with dissolve
        "Everything in the past ten minutes just happened so fast, it only just occured to me that I had sex with Ruby, and Melody was likely successful in her part making it happen."
        "Melody's plan was clearly to use me to earn some money."
        "When I came to work at a boutique, I wasn’t expecting to become the star of a cam show, but at this point I’m so wrapped up in the schemes of both Melody and Ruby that I’m not surprised it’s come to this."
        show ruby sexlipbitecum with dissolve
        ruby "Okay darling, I assume your species needs a break between ejaculations, so I’ll setup the stream."
        show ruby sexpccum with dissolve
        ruby "Just stare at my butt until you're hard and ready to go again."
        "That’s easy, getting paid to have sex with an extremely attractive lady. It's an unusual experience for sure."
        "I don’t even think I’d get tired of this after seven hours, as long as we take breaks."
        show ruby sexlipbitecum with dissolve
        ruby "Okay, there we go, the stream is on.  There's less competition for straight streams than male or female, so we should get a few viewers."
        show ruby sexpccum with dissolve
        ruby "Goodness, 10 viewers already, that’s… a record… How embarrassing."
        "I have an erection again at this point, softly snug in Ruby's folds."
        mc "Hey babe, I'm ready to go, ride it a little for the viewers."
        show ruby sexlipbitecum with dissolve
        ruby "Good idea, mmm, just sit back and I’ll make everything feel great."
        "Her rump starts to teasingly gyrate back and forth around my cock, pleasuring me in ways I didn't know were possible with a vagina."
        camshowaudience "'Woah sex!' – 'That’s hot, I want that cock' – 'wtf kind of dick is that?' – 'fuck it!' – 'what species is that' – 'omg it’s a dragon'"
        "I can see the chat room from where I’m laying down, and the chat seems to be full of ladies loving the show so far."
        camshowaudience "'Twist60 has donated 5 monies' – 'keep going!' – 'NotPrincessAurora has donated 10 monies' – 'XAshleeX has donated 10 monies.'"
        show ruby sexpccum with dissolve
        ruby "Mmphh, the heck, that’s so much monie. Here, let me set a sex goal, how about… 50?"
        camshowaudience "'ponyluv has donated 25 monies.'"
        ruby "Ah, thank youuu. I don’t know what to say, this is so much."
        "I don’t know what to say either, I guess I’m popular, or my dick is anyway."
        mc "How many viewers do we have?"
        show ruby sexlipbitecum with dissolve
        ruby "Uhm, 120, wow!"
        mc "Alright, well they met that sex goal rather quickly, lets give them a show."
        ruby "Of course darling, are you ready to go again?"
        mc "Yeah, no need to hold back."
        show ruby sexofacecumdeep with dissolve
        show ruby sexofaceactioncum with dissolve
        "Ruby sits down on my cock, taking my entire shaft inside her, her insides are still lubricated with residue of my cum."
        show ruby sexofacecumdeep with dissolve
        show ruby sexofaceactioncum with dissolve
        "She begins to ride me up and down as before, her vagina squeezing and sucking around my throbbing cock."
        show ruby sexofacecumdeep with dissolve
        show ruby sexofaceactioncum with dissolve
        ruby "Mmm, thank you for another donation, Jenxi. I knew this would be a hit, but I didn’t anticipate how much of a hit it would be."
        stop ambience fadeout 2.0
        stop music fadeout 2.0
        hide ruby with dissolve
        show bg black with dissolve
        "…"
        "The two of us play along with the cam show for hours, taking breaks to drink tea and eat lunch. We agree that after lunch we’ll do our last sex show because I’m starting to grow tired."
        "…"
        play music boutique fadein 20.0
        show ruby sexofacemorecum with dissolve
        "About halfway into the last sex show, Ruby is once again expertly riding me. Mentally, I'd never get tired of this, physically, my thighs are starting to cramp a little."
        if farmvisit3 == 1:
            "Wouldn't want another cramp incident like Blossom's."
        "Ruby however just keeps riding. I’m impressed at her lack of fatigue, she seems to be as full of energy as when we started."
        ruby "Ahhh, your cock is crazy good darling. Ahh, ahahhhh, aaaahhhhhhhh!"
        "I’m a little less energetic than the first time, but it’s still unfathomably pleasurable. I’ve thoroughly enjoyed being a sex toy on the whims of a horny mare in heat, although it’s probably not something I’d want to try every day."
        "Whilst it does feel good, my orgasm is building up much slower than my previous ones."
        "In the corner of my eye I spot something moving, it’s between the cracks of the door frame, briefly reminding me of where I stood with Melody."
        "Low and behold, Melody is watching with a smug grin on her face."
        "I’m not sure whether I should grimace or grin back. She smiles and winks at me though, so I give her a sly thumbs up."
        show ruby sexahegaoactionmorecum with dissolve
        ruby "Ahh, ohh, I-I’m close, darling!"
        "Ruby starts to ride me even faster, pounding into me over and over. *Slap*, *Slap*, *Slap*. I’m getting really close to cumming."
        ruby "*Pant* Coming, I’m coming! Ahh, cum inside me… Ahhh!"
        show ruby sexahegaoactionmorecum with cum
        show ruby sexahegaoactionmorecum with cum
        "The pleasure is far too overwhelming causing me to close my eyes as I start to cum again."
        "Despite being several orgasms in, I’m sure this is one of the more powerful ones of the day. I fill up Ruby with many more loads of my hot cum, a sensation that I’ll never grow tired of."
        "As my climax fades and I open my eyes, Melody was already gone. I’ll be sure to pay her a visit before I leave though."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        hide ruby with dissolve
        show bg rubybedroom with dissolve
        "Ruby raises herself and my cum oozes out of her en masse. Even though I’ve sat here and not done much, I’m exhausted."
        ruby "Thanks for watching everyone, you’ve all been wonderful, bye byeee!"
        show ruby lingerieembarrassed with dissolve
        ruby "Melody is going to be back home soon, so I try to stop my cam show before that happens. I couldn’t bare the thought of her hearing me, how embarrassing!"
        "Indeed, wouldn’t that be a shame."
        "She turns off the stream and we both enjoy a well deserved cuddle. I haven’t known Ruby that long really, this all happened quite fast."
        show ruby lingeriehappy with dissolve
        "Despite that, after the hours we’d spent together today, there was an undeniable bond between us."
        mc "How much did we end up earning, Ruby?"
        show ruby lingerielaughing with dissolve
        ruby "A lot more than I expected, we’re up around 300 monies. That’s a wild amount, I'll  have plenty of time to focus on designing some new clothes."
        mc "Anything you’re designing in particular?"
        show ruby lingeriehappy with dissolve
        ruby "I’m designing something ambitious, it’s a long flowing dress, it’s my second attempt at a wedding themed garment."
        "I always thought it was strange that Ruby was designing clothes for a species that is predominantly nude, but a wedding dress seems to make sense."
        show ruby lingerielaughing with dissolve
        ruby "I hope it gets accepted. I need to finish it first, but I’m excited to get back to work."
        show ruby lingerieembarrassed with dissolve
        ruby "Ah, I’ll pay you kindly for your services today, I know I couldn’t have done it without you."
        mc "You don’t need to pay me much; I don't have too much use for money."
        show ruby lingeriehappy with dissolve
        ruby "Mmm, in that case at least let me pay you enough to make your life here more luxurious, by all means you deserve it, darling."
        show ruby lingeriehorny with dissolve
        ruby "Of course, if you ever return, you’re more than welcome to do another show with me. I appreciate it’s not something you’ll perhaps want to do every day, but the offer is there and the money is good."
        "She ends up giving me 80 monies, not bad if I say so myself."
        "With that resolved, I only have one more thing left to do before I head home."
        stop music fadeout 10.0
        hide ruby with dissolve
        show bg boutiqueupstairs with dissolve
        "I part ways with Ruby and as I leave her bedroom, I take note that the door to Melody’s room is apart slightly."
        show bg boutiqueupstairs2 with dissolve
        "I peek inside and there is indeed a cute white mare laying on the bed. She idily kicks her legs in the air as she browses on her laptop."
        show bg melodybedroom with dissolve
        "To be polite, I gently knock on the door as I let myself in and close it behind me."
        play music melodytheme
        show melody closeneutral with dissolve
        melody "Make yourself at home why don’t you."
        mc "You know why I’m here."
        show melody closesadistic with dissolve
        melody "Actually I’m not so sure, are you here to try and perv on me too?"
        mc "Don’t act like you’re better than me, I saw you."
        show melody closefufufu with dissolve
        melody "Well duh, you were supposed to see me, I was teasing you. Shoulda seen your face, haha."
        melody "I guess it’s true then, you may not be a stallion, but you’re just the same, all you care about is sex."
        "I don’t have a retort for that, she’s probably right."
        show melody closesadistic with dissolve
        melody "Did you enjoy sliding that pitiful wormy penis deep into my sister?"
        mc "Nothing pitiful about this cock, she had a great time."
        show melody closehappy with dissolve
        melody "Hmph, touché. I bet you’re here because you want to know what my amazing plan was, right?"
        melody "I bet you're impressed, I did what I said."
        mc "Yeah, how did you manage that? It’s like her opinion of me completely changed. She was so indifferent when I first met her, but this time she hung off my every word."
        show melody closesadistic with dissolve
        melody "You see, I have a way of reading and influencing people."
        show melody closefufufu with dissolve
        melody "Her opinion didn’t change at all, I just inspired her to be more open about her perverted nature. I sowed the seeds of sexual indulgence and monetary success within her."
        mc "Sounds manipulative."
        show melody closehappy with dissolve
        melody "You say manipulative, I say supportive. She wanted to do those things with you anyway, but that girl is too much of a softie, not like me at all. I’m a girl that gets what I want, she just shyly twiddles her thumbs and hopes it comes to her."
        "She may say that, but I’ve noticed that the two sisters are surprisingly similar, even in their differences."
        mc "What did you say to her specifically?"
        "Melody stops tapping at her laptop and sits up to face me, her usual teasing demeanour is lost, I guess she’s not in the mood for that."
        show melody closeneutral with dissolve
        melody "I made some passing comments, said that you were cute, and it’s mating season. Even though we are sisters we do talk about those personal things. I told her that if she wants to sleep with you, she should."
        mc "You essentially acted as a wingman for me, that seems remarkably kind of you, what I’m wondering is what do you have to gain from such a seemingly selfless act?"
        show melody closesatisfied with dissolve
        melody "Meh, come here, look at this."
        show melody closesad with dissolve
        "She stands up and moves over to her keyboard. She turns it on and taps at the keys, but no sounds come out."
        melody "Busted, and we’re broke so Ruby can’t afford to buy me a new one."
        mc "Ah, I was told that you study music, so you had some real passion behind this plan."
        show melody closesadistic with dissolve
        melody "You see I’m a smart gal, I didn’t just encourage Ruby to sleep with you, I also decided to make a fuss about getting a new keyboard."
        show melody closefufufu with dissolve
        melody "Usually when we argue Ruby shrinks into herself like a turtle, getting sad and mopey. Not this time though, she was sly, she had a plan."
        "This girl is scary."
        melody "She remembered that cute male that came to work for her and realized how much of a money making opportunity you were."
        show melody closehappy with dissolve
        melody "See? Everyone wins!"
        mc "So you used us both to get something you wanted, but you simultaneously got both me and Ruby something we wanted too."
        mc "Maybe you're not so bad after all... Rather benevolent in your own special way."
        show melody closefufufu with dissolve
        melody "Mhm, I’m an absolute delight."
        mc "Well… I wouldn’t go that far."
        show melody closesadistic with dissolve
        melody "Ohh, maybe I could convince you… I still need to give you a reward."
        mc "My reward? Wasn’t that having sex with Ruby?"
        show melody closehappy with dissolve
        melody "Hehe, no, that’s not the reward. But do tell me, what was it like being my sister’s sex toy for the day?"
        mc "It was great, she definitely has an edge of experience when it comes to pleasing men."
        show melody closefufufu with dissolve
        melody "Is that so? That would explain those weird faces you were making."
        melody "You looked so ridiclous! No wonder she had her back to you, hehe."
        menu:
            "You're such a bully.":
                show melody closehappy with dissolve
                melody "Me? Oh no, not me."
                melody "When I fuck you, I'll make eye contact."
                mc "You're gonna fuck me?"
                show melody closedeath2 with dissolve
                melody "Ahaha, you wish."
            "You're the one that keeps pulling weird faces.":
                show melody closesad with dissolve
                melody "You mean like this?"
                show melody closedeath2 with dissolve
                mc "Yeah, like that."
                show melody closefufufu with dissolve
                melody "Hehe, I've taken acting classes you know, don't take me too seriously when I'm acting melodramatic."
                melody "Otherwise I'll just walk all over you, and even a sadist like myself prefers a man that can stand on their own two feet."
                mc "Noted..."
        show melody closefufufu with dissolve
        melody "You seemed to enjoy the handjob from before, did it turn you on?"
        mc "In a weird way, yeah."
        show melody closehappy with dissolve
        melody "Ewie, I can feel your lecherous gaze crawling over me, feels tingly."
        mc "It’s hard not to stare when you bring attention to yourself."
        show melody closefufufu with dissolve
        melody "I’m not as well-endowed as my sister, but a pervert like you doesn’t care about that, right?"
        menu:
            "I prefer flat chests.":
                show melody closehappy with dissolve
                melody "Awh heck yeah, maybe you are redeemable after all, wormy boy."
            "I prefer big boobs.":
                show melody closesatisfied with dissolve
                melody "Mm yeah, something to play with right?"
            "All body types have their perks.":
                show melody closesad with dissolve
                melody "Yeah, a shallow incel like yourself would say that to try and get as many women possible."
        show melody closehappy with dissolve
        melody "Who needs tits anyway? I have a great butt!"
        show melody butt with dissolve
        "She's not lying, she has a great butt as she turns around and shows me in a surprisingly lewd fashion."
        melody "I bet if I offered myself to you right now, you’d sleep with me, wouldn’t you?"
        melody "Bent over, pussy exposed, begging for it, you’d fuck me where I stood."
        mc "I’ve had a lot of sex today, so if you’re trying to tease me, you’ll have to try harder than that."
        "I was bluffing; I could feel blood going towards my nethers. Perhaps due to genuine arousal, or perhaps due to her pheromones."
        "I could tell what she was doing, she was trying to give me an erection so she could tease me again."
        "I don’t know why, I guess it’s a fetish of hers."
        "Unfortunately for her I’m not exactly horny."
        show melody closefufufu with dissolve
        melody "Fine, you and I both know you weren't getting this ass anyway."
        mc "I know what you’re trying to do this time, you won’t catch me off guard."
        melody "Playing hard to get? I guess that makes sense if you’ve already had so much action."
        show melody closesatisfied with dissolve
        melody "I’ll be honest, I wasn’t expecting you to have so much sex…"
        mc "Me neither actually. I tell you what though, I feel like I could have sex one more time."
        show melody closesadistic with dissolve
        melody "Are you implying what I think you’re implying? How disgusting, I won’t sleep with a pervert like you."
        mc "You were just teasing me about bending over and getting fucked where you stood."
        show melody closeneutral with dissolve
        melody "Well yeah but… That was hypothetical."
        mc "Just like that hypothetical handjob."
        mc "What do you want to do with me this time? Let's cut to the chase."
        show melody closeangry with dissolve
        melody "Eugh, you’re no fun, you’re not fun at all!"
        melody "I’m pissed off now."
        "Finally, I've busted her angsty façade. Only question is, what do I do now?"
        mc "What about my reward? I’ll still gladly accept it."
        "She huffs and looks at my semi-erection."
        show melody closeneutral with dissolve
        stop music fadeout 3.0
        melody "Only if you shut up."
        mc "Alright, you have a deal."
        hide melody with dissolve
        "She turns around for a few seconds, remaining silent."
        show melody closesad with dissolve
        melody "Eugh, I'm out of character now, you’ve ruined it."
        mc "Character?"
        show melody closefufufu with dissolve
        $ melodyblowjob = 0
        jump melodyblowjob2
        label melodyblowjob:
            show bg melodybedroom
            show melody closefufufu with dissolve
            stop music fadeout 3.0
            stop ambience fadeout 3.0
        label melodyblowjob2:
            melody "Eh-hem, you do want to fuck me, don’t you?"
        mc "Hmm…"
        show melody closehappy with dissolve
        melody "Slide this cock, deep inside me… Mmm."
        hide melody
        show melodyb handjob
        show melody handjob1
        with dissolve
        "Melody's fingers coil around my shaft and begin to jerk it back and forth with a hidden enthusiasm that she'd never admit to."
        "Her cool grip and movements quickly cause my cock to stiffen and throb."
        "She looks at my cock with surprising admiration."
        "I can tell deep down that she was looking forward to this."
        melody "I’m just a naughty mare in heat, I'm gasping for cock..."
        melody "I can’t control myself you know, I get so wet around men..."
        show melody handjob3 with dissolve
        melody "Heheh, that was my Ruby impression. Didya like it?"
        melody "I for one am able to perfectly control myself."
        mc "Is that so?"
        "Her fingers lock around my cock and start to jack me off even faster."
        "The rubbing fingers between her own legs also speed up, she even stifles a few moans as she gets more excited."
        show melody handjob1 with dissolve
        melody "Ooohh, your wormy cock is so hard thinking about me, how gross!"
        mc "What are you going to do?"
        melody "Mmm… It would be boring to just jack you off again..."
        melody "And that would hardly be a good reward..."
        play ambience blowjob
        show melodyb blowjob
        show melody blowjob1
        with dissolve
        "She kneels down bringing her face level with my cock. She then begins idly licking it with her tongue."
        melody "Mmphh, how about I clean up your dirty attitude with my pristine tongue… *Lick*, *Lick*"
        "I wasn’t expecting this, I don’t know what I was expecting actually, anything could have happened, and it still would have surprised me."
        show melody blowjob2 with dissolve
        "Her tongue slides around my shaft, leaving a wet sheen and sparks of pleasure in its deft licks."
        "She doesn't hold back at all as she twirls her tongue around the tip of my cock, licking off any precum as it drips."
        mc "That feels--"
        show melody blowjob3 with dissolve
        melody "Shhh, shh… No talking."
        mc "Mm..."
        show melody blowjob4 with dissolve
        melody "Yeahh, you just stand there and take it like a good boy."
        "Her hand continues rubbing her pussy quickly as her long tongue swipes from my glans to the base with ease."
        "I wonder if she had already fantasised about this before I arrived."
        show melody blowjob2 with dissolve
        melody "Mmmh, you’re just a sex toy for a fine lady like me… That’s right…"
        "Even though I've already had many orgasms today, Melody's movements cause another one to well up."
        "My cock tightens and throbs as I get closer and closer to cumming in her mouth."
        show melody blowjob4 with dissolve
        melody "Ohh, it’s throbbing, does that mean you’re going to cum soon?"
        mc "Bit faster…"
        show melody blowjob1 with dissolve
        melody "Shh! Alright…"
        show melody blowjob2 with dissolve
        "Graciously she speeds up, not sparing a second to tease me as her lips pull back and forth along my glans like a fucking motion."
        "All whilst her tongue dances around the tip, overwhelming me with two distinctly pleasurable stimuli."
        "With each thrust I can feel myself getting closer to my orgasm, until finally she pushes me over the edge and I release my load into her mouth."
        play sound cum
        show melody blowjob2 with cum
        play sound cum
        show melody blowjob2 with cum
        "Until she finally pushes me to the limit, her tongue and hand cause me to start cumming into her mouth."
        play sound cum
        show melody blowjob2 with cum
        play sound cum
        show melody blowjob2 with cum
        melody "Aahhh, ahh, aahhh..."
        melody "Your hot sticky cum, so gross…"
        "I came surprisingly fast!"
        "It felt great too."
        show melody blowjob1 with dissolve
        stop ambience
        melody "… You didn’t cum much…"
        show melody blowjob2 with dissolve
        melody "It doesn’t taste good either…"
        show melody blowjob1 with dissolve
        melody "Icky, at least we didn't make a mess this time."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        scene bg melodybedroom with dissolve
        mc "You know, you’re not good at keeping up your tough girl front."
        show melody closeneutral with dissolve
        melody "Be quiet, meanie."
        melody "Go get me a glass of water from the bathroom, I want to wash this gross taste from the back of my throat."
        hide melody with dissolve
        show bg boutiqueupstairs with dissolve
        pause 0.5
        "I abide and sneak over to an adjacent room to fill up a glass."
        show bg melodybedroom with dissolve
        pause 0.3
        show melody closesatisfied with dissolve
        pause 0.3
        melody "I’m so frustrated that you didn’t play along with me this time."
        mc "Play along? The first time we met all my reactions were genuine."
        mc "I don’t know what changed, but it felt like you didn’t come across as strongly this time."
        show melody closesad with dissolve
        melody "Eh, I caught you off guard last time. I like playing with boys like that."
        show melody closesurprised with dissolve
        melody "Not that I do it often! I'm not like my sister..."
        mc "Uhh, right."
        show melody closeangry with dissolve
        melody "I have half a mind to sit on your face right now."
        melody "Do I have to be meaner? Maybe more insults?"
        mc "Melody, why are you trying to front this mean girl persona?"
        mc "I've noticed that everyone else thinks you’re lovely. So why are you cruel to me?"
        show melody closesad with dissolve
        melody "Meh… It’s not you, you’re actually alright, I think. It’s just men."
        mc "I don’t think I follow?"
        melody "I’ve been pissed off ever since Mom ran away with a random dude."
        show melody closeangry with dissolve
        melody "Mom left me and Ruby alone to struggle."
        show melody closesatisfied with dissolve
        melody "I couldn’t really blame my Mom, so… It must have been the stallion, right?"
        show melody closeangry with dissolve
        melody "Yeah, I was angry, harboured a resentment to all stallions."
        show melody closeneutral with dissolve
        melody "But then you’re not a stallion, are you?"
        mc "I guess not, I’m not sure what the difference would be though."
        show melody closesad with dissolve
        melody "Hmph, me neither."
        show melody closeangry with dissolve
        melody "All I know is that I’ll never let myself become the plaything of a man. I’ll always make sure I’m the dominant one, I want the power."
        show melody closeneutral with dissolve
        melody "Well whatever, that's my life story. Sorry to bore you with that."
        show melody closesatisfied with dissolve
        melody "We're all problem childs in this era though, so what of it?"
        "This certainly explains her personality. Doesn’t explain that weird hand job when we met though, but I guess I can use my imagination to fill those gaps."
        mc "You know… I actually respect that, but I have something important I feel like I need to say."
        show melody closeneutral with dissolve
        melody "What’s that, wormy boy?"
        mc "You’re confusing being a strong, independent figure with toxicity and nastiness."
        show melody closesurprised with dissolve
        melody "Ah-… I am?"
        mc "Yeah, it’s possible to exude that healthy dominance and independence without being rude to everyone else."
        mc "It’s possible to get what you want, when you want it, through kindness, not rudeness."
        mc "Maybe keep the insults in the bedroom when you’re actively trying to talk dirty and be dominant."
        show melody closeneutral with dissolve
        melody "You’ve got a point..."
        show melody closesatisfied with dissolve
        melody "I have noticed that I tend to be bad-mannered in day-to-day conversation."
        show melody closesad with dissolve
        melody "I'd rather not turn that into a habit. I felt good about myself when you said other people think I'm lovely."
        melody "I’ve been pretty frustrated lately over money, as pathetic as that sounds. However, it seems like you helped bring a healthy influx of cash into the household, am I right?"
        mc "You may be right, there was a large sum of monies."
        show melody closeneutral with dissolve
        melody "Once my piano is fixed or replaced, I’ll be in your debt… [playername]…"
        mc "So you do know my name."
        melody "Yeah, yeah… I do pay attention"
        mc "Anyway... Wasn’t expecting the blowjob, but I enjoyed that, hope you did too."
        mc "You mentioned face-sitting? I wouldn't mind returning the favour."
        show melody closesurprised with dissolve
        melody "That was a joke!"
        melody "Maybe another time though..."
        mc "Alright, in that case, I won't keep you any longer."
        melody "Wait, one more thing."
        show melody closehappy with dissolve
        melody "Come back, I want to see you again."
        show melody closedeath2 with dissolve
        melody "When you do, trust me, I’ll have my meaniest girl attitude possible!"
        mc "Awh come on, didn’t you just hear what I said?"
        show melody closefufufu with dissolve
        melody "Only in the bedroom darling, hehehe."
        hide melody with dissolve
        stop music fadeout 3.0
        show bg black with dissolve
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu

        "…"
        if livingwithmoxie == 1:
            show bg moxiewagonday with dissolve
            play music wagon fadein 3.0
            "I head back to the wagon a little earlier than usual so I can have a nap. Can’t believe those two ended up draining me dry, Moxie is probably going to want some later tonight too. The mind is willing, but the body is weak."
            scene bg black with dissolve
            show bg moxiewagonlamp with dissolve
            play ambience ambiencenight fadein 1.5
            "I can still recall Melody’s plight, after seeing her true personality I’m interested to see her slather on the cute mean girl attitude thick next time we meet."
            "I’ll play along next time, just for fun."
            "It doesn’t take too long for Moxie to return from work."
            show moxie2 laughing with dissolve
            moxie "Hey tricks, how’s it going?"
            mc "Went to the boutique again today, if you recall there was some kind of scheme, turns out it involved a lot more sex than I anticipated."
            show moxie2 shocked with dissolve
            moxie "Awh please, you’ll make me jealous. Which I’m not! Not jealous..."
            show moxie2 closesmug with dissolve
            moxie "Do divulge the details though."
            "Moxie having prepared a drink for herself and I, we sit down on the sofa, and relax."
            mc "I think I mentioned before that Ruby…"
            show moxie2 closeshy with dissolve
            moxie "Ruby...?"
            mc "I’m actually not sure if I should tell you, because I’d be sharing one of Ruby’s secrets"
            show moxie2 closeshocked with dissolve
            moxie "Whaaat? Why would you trick me like this…?"
            moxie "You just told me you had sex, what could be more secretive than that?"
            mc "I can trust you right? You’ve been an angel since I met you, so I’m sure I can."
            show moxie2 closealthappy with dissolve
            moxie "Of course you can trust me, dummy! I’d be mad if you didn’t just call me an angel and make me feel all cute and warm inside."
            mc "Okay, okay, truth is, Ruby kinda works in the porn industry and I helped her out."
            show moxie2 closeembarrassed with dissolve
            moxie "Woah, what? What if someone saw your face? Should I be mad? I’ve never had to react to a situation like this before."
            mc "Nah, don’t worry, no one saw my face."
            show moxie2 closebashful with dissolve
            moxie "Yeah… But… You’re a teeny bit recognizable even from the waist down..."
            mc "Lights were off though; I could have been anything, right? All they could see was my pelvic area."
            show moxie2 closeangry with dissolve
            moxie "Mehhh, try to be careful you dummy."
            moxie "You’re the only you in this world, and porn is popular with the women, someone might recognize you."
            mc "Of course I’ll be careful; I don’t particularly want to become a porn star here."
            show moxie2 closeembarrassed with dissolve
            moxie "Anyway… Ruby does that kind of thing?"
            mc "Yeah, alone with little success, greater success with me."
            show moxie2 closealthappy with dissolve
            moxie "Makes sense, I can see why she asked you to help her out."
            show moxie2 closehappyneutral with dissolve
            moxie "Oh, and how did that little scheme of little Melody’s end up playing out?"
            mc "Ah well, having sex with Ruby was her scheme. She wanted me to help the household earn some cash with my ‘assets’."
            show moxie2 closesad with dissolve
            moxie "Really? I’ll admit, that's a bit weird."
            mc "You don’t know the half of it, Melody has this dominatrix like personality where she always teases and messes around with me."
            show moxie2 closeshy with dissolve
            moxie "Really? That kinda pisses me off, I don’t want anyone treating you poorly."
            mc "Don’t get mad, it’s complicated. She isn’t doing it to be nasty."
            mc "I think it’s kinda like… a fetish thing. She’s able to snap back to a kinder side, that I’m assuming is the side everyone else sees."
            show moxie2 closeneutral with dissolve
            moxie "I can’t relate to that much, but I can connect the dots in my head."
            moxie "Personally, I much prefer men to dominate me. Speaking of which, how about it, are we gonna rut?"
            mc "Aww man, I’ve had so much sex today…"
            show moxie2 closeangry with dissolve
            moxie "Bruh, I warned you about not saving enough for me."
            moxie "Let's have dinner first and we'll see how you feel after that."
            scene bg black with dissolve
            "..."
            jump evening
        elif livingwithbutters == 1:
            show bg buttershouse with dissolve
            play music butters fadein 3.0
            "I head back home, a little earlier than usual so I can have a nap. Can’t believe those two ended up draining me dry, Butters is probably going to want some later tonight too. The flesh is willing, but the body is weak."
            show bg buttershousenight with dissolve
            play ambience ambiencenight fadein 1.5
            "I can still recall Melody’s plight, after seeing her true personality I’m interested to see her slather on the cute mean girl attitude thick next time we meet."
            "I’ll play along next time, just for fun."
            "It doesn’t take too long for Butters to come back home from whatever she may have been doing today."
            show butters dresslaughing with dissolve
            butters "Hello [playername], did you have a good day?"
            mc "Went to the boutique again today, if you recall there was some kind of scheme, turns out it involved a lot more sex than I anticipated."
            show butters dresssurprised with dissolve
            butters "Awh please, you’ll make me jealous... I'm not used to sharing, hehe."
            "Butters having prepared a drink for herself and I, we sit down on a sofa, and relax."
            show butters closedressneutral with dissolve
            butters "Oh, and how did that little scheme of little Melody’s end up playing out?"
            mc "Ah well, having sex with Ruby was her scheme. She wanted me to help the household earn some cash with my ‘assets’."
            show butters closedresssad with dissolve
            butters "Really? I’ll admit, that's a bit weird."
            mc "You don’t know the half of it, Melody has this dominatrix like personality, she always teases and messes around with me."
            show butters closedressneutral with dissolve
            butters "I hope no one's treating you poorly, my succubus side will beat them up."
            mc "Don’t get mad, it’s complicated. She isn’t doing it to be nasty."
            mc "I think it’s kinda like… a fetish thing. She’s able to snap back to a kinder side, that I’m assuming is the side everyone else sees."
            butters "Fetish? I can’t relate to that much, but I think I understand."
            butters "I'm much more into getting dominated."
            mc "Well, half of the time."
            show butters closedresshappy with dissolve
            butters "How about we roll that dice after dinner?"
            scene bg black with dissolve
            "..."
            jump evening
        else:
            pass
    label boutiquevisit3:
        "I’ll return to the boutique."
        stop music fadeout 10.0
        "Even though there’s always an aura of uncertainty about going there."
        "Every single day a completely different set of events can happen. It’s both exciting, and somewhat uncomforting."
        "Will Melody tease me and try to jack me off?"
        "Will Ruby tease me and try to make me a part of her cam show?"
        "The more I think about these two, the more similarities I spot than differences."
        "Yet, they are so different. Siblings can be weird like that."
        show bg boutiquedoor with dissolve
        "When I arrive, I see Melody at the door, just about to leave."
        play music melodytheme
        show melody surprised with dissolve
        melody "Wait, [playername], what are you doing here?"
        mc "Good morning to you too, Melody."
        show melody sad with dissolve
        melody "Y-You can’t go in today, Ruby is just going to use you for her cam show, you should come in later instead and just see me."
        mc "Are you being blatantly jealous? That’s unlike you."
        show melody angry with dissolve
        melody "No, it’s not unlike me at all. You’re just awful at understanding women, dumbass."
        mc "I don’t get it, weren’t you the one that helped me sleep with Ruby in the first place?"
        show melody sad with dissolve
        melody "Meh… I’m leaving."
        mc "Wait, I won’t do it then."
        show melody angry with dissolve
        melody "Do whatever you want, jerk."
        hide melody with dissolve
        stop music fadeout 10.0
        "She stomps off after her unreasonably childish remark."
        "Seems like she only wanted me to sleep with Ruby before because she was getting something out of it."
        play music boutique fadein 2.0
        show bg boutiqueinside with dissolve
        "I step into the boutique and close the door behind me, the entire room is lit up, and it’s clear that there has been a lot of busy work happening in here, which is remarkable considering it hasn’t been that long since I was last here."
        "Immediately I spot Ruby with a satisfied expression. She is sipping coffee next to a sewing machine."
        mc "Hey Ruby, it’s nice to see you busy down here."
        show ruby closelaughing with dissolve
        ruby "Ohh darling, darling, darling!"
        show ruby happy with dissolve
        "She bounces up from her chair and hugs me."
        show ruby happy with dissolve
        ruby "I can’t thank you enough for your help, things are really looking up."
        mc "Awh please, I barely did anything, it was all you."
        "What’s with this girl, her personality is completely different every time I arrive."
        show ruby horny with dissolve
        ruby "Aha, apologies dear, I’m a little wired on caffeine."
        show ruby laughing with dissolve
        ruby "Thanks to the lil’ cash boost you gave us, I decided to take a quick break from camming and instead go crazy with the designing."
        if barvisit1 == 1 and maiddressbought == 0:
            mc "That's wonderful, think I can buy something?"
            "I need to get a 'slave' outfit for Riku's truth or dare punishment."
            show ruby shocked with dissolve
            ruby "Oh? Of course darling! What would you like?"
            mc "I'm looking for a maid dress."
            show ruby laughing with dissolve
            ruby "Ooo, a maid dress? I wonder who for! *Giggle* Hmm, Melody had a maid dress for halloween once, ah, here it is."
            "She walks over to a rack and takes one out to show me, it's perfect."
            show ruby neutral with dissolve
            ruby "Naturally this dress fits Melody's small figure and bosom, is that okay?"
            mc "Yeah that's perfect, how much is it?"
            show ruby happy with dissolve
            ruby "Second hand? 50 monies should cover it."
            menu rubymaidmenu3:
                "I have [monies] monies."
                "Buy the dress (-50 Monies)" if monies >= 50:
                    if monies < 50:
                        "I can't afford it."
                        jump rubymaidmenu3
                    $ maiddressbought = 1
                    ruby "Pleasure doing business with you darling."
                    mc "By the way, can you leave the dress here?"
                    ruby "Here? Do you want to pick it up at a later time?"
                    mc "Yes, you'll see."
                "Maybe later":
                    ruby "Okay darling, maybe you can earn some money to put towards the dress."
            mc "Anyway, what have you been working on? You seem exhausted."
        else:
            mc "That’s wonderful, got anything in particular that you’re working on?"
        show ruby happy with dissolve
        ruby "Mhm, I’ve been up all night, and some of the morning to finish a wedding dress design."
        show ruby shy with dissolve
        ruby "I finally finished it and sent the design to my contacts this morning. I’m most nervous, I hope it gets accepted."
        mc "What will happen then?"
        ruby "If they like the design, they’ll produce and sell it."
        ruby "It’ll earn me quite a lot of residues if it’s successful."
        show ruby happy with dissolve
        ruby "A few hits like that means I’d be able to design full time again instead of doing cam shows."
        show ruby laughing with dissolve
        ruby "The designing industry is all about getting your foot in the door. I need people to recognize my brand and its quality, so companies are more eager to manufacture my products."
        mc "Ahh, so you don’t want to be a cam girl, that’s just a means to an end."
        show ruby horny with dissolve
        ruby "Mmm not quite, I do genuinely enjoy doing the cam shows."
        show ruby happy with dissolve
        ruby "I’ll probably continue to do those in the evenings, heh… I masturbate in the evenings anyway, so…"
        mc "Does that mean there’s nothing for me to do here?"
        ruby "Ohh gosh, I forgot! You're obviously here to work, not chit-chat."
        show ruby laughing with dissolve
        ruby "This is perfect though, I’m trying to get as much work done as possible."
        ruby "I hate to reduce you to an errand boy again, but if you could help me with lots of simple fetching tasks while I design. It’ll make the working process far easier for me."
        show ruby happy with dissolve
        ruby "Hehe, I can even pay you this time, with that money you helped earn!"
        mc "Sounds perfect, I don’t mind at all. Just tell me what to do, and I’ll do it."
        ruby "Excellent, I’m actually quite tired, but there’s no way I could rest while I’m waiting for the confirmation of that dress, so I’m going to stay up until its confirmed and then nap afterwards."
        ruby "For now, could you make me a coffee? That would definitely help. I like it sweet, two sugars."
        if farmvisit2 == 1:
            "I'm going to assume she wants it black considering milk is an aphrodisiac in this world."
        else:
            mc "Any milk?"
            show ruby laughing with dissolve
            ruby "Goodness no darling, not now hahah."
        stop music fadeout 3.0
        hide ruby with dissolve
        show bg black with dissolve
        "…"
        show bg boutiqueinside with dissolve
        play music castle fadein 3.0
        "This is an unexpected yet exciting turn of events."
        "I spend the day helping Ruby with rather basic yet important things allowing her to focus on designing, stitching, sewing while I hand her things, make her drinks."
        "She even asks for my opinion a few times but I’m woefully underqualified to help her in that department. All her designs look gorgeous to me."
        "There’s quite a lot of downtime, so I make myself a drink and spend a lot of time browsing the strange PonyWeb on Ruby’s laptop for fun."
        "I’m using the laptop so I can keep an eye on Ruby’s email. I guess I’m acting as a personal assistant."
        "Specifically I’m waiting for an email from the clothes manufacturer she sent her design to."
        "The day feels surprisingly long, I’m honestly in awe as Ruby works like a maestro for hours on end, seldom taking breaks."
        "…"
        "Even as the afternoon drags on there’s no email response. Ruby looks utterly exhausted at this point, I even learnt that she barely slept last night too."
        show melody surprised with dissolve:
            xpos 700
            ypos 75
        "It’s around 3:30pm when Melody steps through the door and awkwardly stares at us from the doorway."
        melody "Uh, hi."
        show ruby closeembarrassed with dissolve:
            xpos 100
            ypos 88
        ruby "Hey sweetie... Gosh, is it that time already? And still no email?"
        mc "Hey Melody. I’m afraid I’ve got no emails, Ruby."
        ruby "I feared as much, they usually get back to me quickly but… Well, I guess I’ll be patient."
        show ruby sad with dissolve:
            xpos 150
            ypos 50
        ruby "I’m exhausted though, I’m at the point where I’m struggling to stay awake, so I’m going to nap."
        show melody happy with dissolve
        melody "Rest well Ruby, you deserve it after all your hard work."
        stop music fadeout 2.5
        hide ruby with dissolve
        hide melody with dissolve
        "Ruby heads off leaving me and Melody alone downstairs."
        show melody fufufu with dissolve
        play music melodytheme fadein 2.0
        mc "Ahh, she forgot to pay me. Guess I’ll wait…"
        melody "Pay you for what, hmm? Being a rampant sex pest again?"
        mc "Calm yourself, we’ve been working on clothes all day. Check out that mannequin over there, she finished that one today."
        show melody happy with dissolve
        melody "Ohh my gosh, it’s so cute! I love these frills."
        show melody sadistic with dissolve
        melody "Alright, I’ll let you off this time, [playername]."
        show melody closeneutral with dissolve
        "She walks to the table I’m sat at and sits next to me."
        show melody closesad with dissolve
        melody "Guess I gotta reluctantly babysit the furless alien while Ruby naps."
        mc "Furless alien? That's harsh."
        mc "You were mean this morning too. Why are you so irate at the moment?"
        show melody closesurprised with dissolve
        melody "Irate? I’m not, you’re just…"
        show melody closesatisfied with dissolve
        melody "It’s because Ruby hasn’t shut up about you ever since that stupid cam show."
        show melody closesurprised with dissolve
        melody "She’s always talking about you, like..."
        show melody closesad with dissolve
        melody "’He helped us out so much’, ‘I do wish that cute boy comes back again’, ‘I’ll show him a good time’."
        show melody closeangry with dissolve
        melody "Bleh, gross! Did you brainwash her?"
        mc "Melody… You’re the one that encouraged her to be open about her feelings towards me."
        show melody closesad with dissolve
        melody "Ahh, but… I’m not ready to face the consequences for my actions."
        mc "You got exactly what you wanted; you’re just being melodramatic now."
        mc "How about taking your own advice and be open too?"
        "She rolls her eyes and slumps over the table."
        melody "Don’t wanna!"
        show melody closesatisfied with dissolve
        melody "It’s too embarrassing to admit I actually like you too."
        mc "W-Wha-Tch… But you just did admit it."
        show melody closesad with dissolve
        melody "Nuh uh, I didn’t, you’re just projecting because you’re a perv."
        mc "Alright, let’s say I am a perv. Do you wanna be a perv with me?"
        show melody closedeath1 with dissolve
        melody "Hmm… No, I don’t wanna stoop down to your level of degeneracy..."
        show melody closehappy with dissolve
        melody "But... Why don’t we chill in my bedroom instead?"
        hide melody with dissolve
        "This girl is a headache. I heard sex is a great cure for headaches though."
        show bg black with dissolve
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        "…"
        show bg melodybedroom with dissolve
        play music yanderecomplex
        "We head up to Melody’s room. There’s only one chair so we both choose to lay around on her bed instead."
        show melody closefufufu with dissolve
        $ melodycowgirl = 0
        jump melodycowgirl2
        label melodycowgirl:
            show bg melodybedroom with dissolve
            play music yanderecomplex
            show melody closefufufu with dissolve
            stop ambience fadeout 3.0
        label melodycowgirl2:
            melody "Alright dumbass, let me get into character."
        mc "Wait, what are we doing?"
        show melody closehappy with dissolve
        melody "Y-you know… Gross stuff."
        mc "Right now? Without any build up?"
        show melody closefufufu with dissolve
        melody "Pfft, you didn’t need any build up when I jacked you off, utter perv."
        melody "I’m horny as fuck, alright?"
        show melody closefufufu with dissolve
        melody "I don’t know if you’ve noticed, but only you and Ruby have gotten any action lately."
        show melody closesadistic with dissolve
        melody "Yeah sure, I sucked you off and jerked you off, but that didn’t do anything for me, just left me blue balled."
        mc "Well you could have-"
        show melody closehappy with dissolve
        melody "No, no, don’t tell me what I coulda or shoulda. I wasn’t ready then, but I am now."
        mc "I guess the only thing I’m left wondering is why now?"
        show melody closeangry with dissolve
        melody "Why are you resisting, aren’t you supposed to be drooling over me or something?"
        mc "I’m not a sex zombie, I’m genuinely curious. Why do you want to sleep with me?"
        melody "I already told you, it’s because Ruby wouldn’t shut up about you."
        show melody closesatisfied with dissolve
        melody "And lately I’ve been so horny because of you hanging around that I spend my evenings masturbating into a stupor."
        show melody closesad with dissolve
        melody "Heat sucks already, but it’s unbearably sucky when my sister is drooling over the cute boy that she fucked."
        "Awhh, she thinks I’m cute."
        show melody closedeath1 with dissolve
        melody "I’ve had it. I’m sick of being in everyone’s shadow. I’m independent too, I can do whatever I want!"
        mc "What are you going to do about it?"
        show melody closesadistic with dissolve
        melody "I’m going to fuck you. Don’t misunderstand, {i}you’re{/i} not going to fuck {i}me{/i}, I’M going to fuck YOU."
        hide melody
        show melodyb sex
        show melody sex1
        with dissolve
        "With a single hand, she pushes down my chest, causing me to lay down on her bed as she crawls over the top of me, positioning her hips above my rapidly growing member."
        melody "That’s right, I’m going to quell those sick twisted fantasies of yours."
        melody "I saw the glimmer in your eyes when you met me, the way your eyes darted between my legs then to my chest."
        melody "I got to thinking, why would a guy like you ever want to work at a boutique?"
        mc "Well you know, I just thought it’d be fun."
        melody "Fun… Fun… Right."
        "At this point I’m fully erect in between Melody’s thighs and my tip can feel her wetness. However, she refuses to lower herself and instead teases me with the idea of penetration."
        melody "I guess it would be pretty fun if you had thoughts of fucking the mares working there, hehe, how gross."
        melody "Because let's face it, the only reason a guy with no experience in this industry would want to work at a boutique is because of all the girls."
        mc "I am here to work though; I need the money."
        melody "Yet you still jumped at the chance of every single sexual encounter presented to you."
        melody "I even caught you staring at Ruby masturbating. You had an erection."
        mc "That was an accident, I would never do something like that without consent."
        melody "But, you did… You watched while I gave you a hand job, you could have stopped me any time you wanted."
        "I can feel her starting to grind against my shaft, her nether lips mushing against my skin leaving a glistening wetness in its movements."
        mc "Yeah… I guess we’re both bad people in that regard, I’m just lucky that Ruby ended up seeing the best out of that moment."
        melody "Tch, Ruby this, Ruby that. Is she special, or is she just another of your fuck and chucks?"
        menu:
            "Honestly, she's not that special.":
                melody "…"

                play sound cum
                show melody sex2 with dissolve
                "I’m taken off guard by her silence, but I can feel her slowly lowering herself onto my cock, after all this teasing she’s finally sliding it inside her."
            "I've already fucked other mares here, Ruby's just another on that list.":
                melody "And me...?"

                play sound cum
                show melody sex2 with dissolve
                "I can feel her slowly lowering herself onto my cock, after all this teasing she’s finally sliding it inside her."
            "Yeah, she's special.":
                melody "Yet here you are, fucking her sister..."
                melody "Wow [playername]..."

                play sound cum
                show melody sex2 with dissolve
                "I’m taken off guard by her reply, but I can feel her slowly lowering herself onto my cock, after all this teasing she’s finally sliding it inside her."
        "She’s immensely tight, her insides suck and squeeze at every inch of my shaft causing me to shiver with desire."
        melody "You’re such a fucking pervert, I love it."
        play ambience sex
        "With her hands leaning back onto my thighs, she slowly rides me up and down."
        "She seems notably less experienced than Ruby but her enthusiasm makes up for it."
        "Her movements eventually becoming gliding motions as my shaft is lubricated by her wetness and she gets used to the penetration."
        "At the peak of each thrust, she can’t help but muffle an adorable squeaky moan totally unfitting of her cold femdom demeanour"
        melody "Mmphh, I can feel your cock inside my pussy. Savour this moment you’ve awaited so long, you filthy pervert."
        mc "Even now, you’re keeping up this act?"
        "She grinned as she once again sat down on my cock, I can’t say the feeling of being dominated wasn’t oddly arousing."
        melody "Hehe… Say whatever you like, you’re the one that keeps getting completely erect at my admonishments."
        melody "And to me, that's hot as fuck."
        "She leaned back slightly, so I had a better view of our sexes. She was so tight her skin would indent slightly as she took me all the way in, it was an erotic sight only made more erotic with the squelching wet sounds."
        "Using her hands on my thighs to support her, she bounced up and down at a growing pace."
        "In a lecherous tone, I could hear her whisper..."
        show melody sex3 with dissolve
        melody "Don’t you think love takes many forms?"
        "Her eyes locked with mine as she licked her lips seductively."
        mc "… What are you trying to say?"
        melody "Be honest with yourself, you love being my toy."
        "Her hips started to grind back and forth as well as ride."
        "I imagine this is her first time and she’s finally gotten used to the motions of riding a cock. Her movements only get more sensual and confident."
        "She’s a quick learner too, she slows down when she notices my erection throb and stiffen."
        "She’s paying close attention to my facial expressions which she is using to read me like a book."
        mc "For a girl in heat, you’re managing to tease me a lot. Isn’t this unsatisfying for you?"
        "Her hips gyrated around while occasionally lifting up and down, stroking the entire length of my shaft with her pussy in shallow, unsatisfying pumps."
        melody "I don’t know what you’re talking about toy, this feels heavenly to me."
        show melody sex4 with dissolve
        melody "I love the way your cock feels, grinding deep inside my pussy. It’s definitely going to make me come."
        "Melody’s lustful words filled my ears clouding my mind with the combined seduction and pleasure."
        "I want to protest and tell her ‘I’m not your toy’, but from her commanding position it feels pointless."
        "She starts speeding up in intervals, bouncing up and down my cock at an immensely pleasurable rate before slowing down and gyrating again."
        show melody sex3 with dissolve
        melody "Hehe, when I go fast, I can feel the tip grow. I can’t let my toy cum before I do though…"
        "She had total control over my body, and my orgasm."
        melody "I’m not letting you cum that easily, this is my pussy you broke in after all…"
        melody "Yeah, that’s right. It’s almost unbelievable to think I was a virgin before."
        show melody sex4 with dissolve
        "Her fingers dig into my skin as she starts to ride me faster, her face ecstatic with pleasure. I think she’s on the edge of coming and can’t hold herself back any longer."
        melody "Gehehe, your dick is throbbing in my pussy, I love it…"
        play sound cum
        "*Squish*, *Squish*, *Grind, grind*, *Hump, hump*!"
        melody "Ah! Does that mean you’re gonna cum?"
        "She moved her hips up and down at an increasing pace, stroking the entirety of my cock with her insides. I could feel my climax rapidly drawing nearer."
        melody "Ahh, mm… I bet you wanna cum, right?"
        "As Melody seemed to orgasm in her frenetic motions, I could feel her pussy contract and tighten around my shaft, pleasuring me more and more."
        melody "Aaahhh… Aaaahhh! Aauuuuhhhhhh…… Haaahhhaaaaaaaa!"
        melody "Mmmphh, Cum inside my filthy, wet pussy…"
        "I could barely hold back another second, my cock was seconds away from bursting."
        melody "Ahh, ah! Cum, you fucking pervert!"
        show melody sex5 with cum
        play sound cum
        show melody sex5 with cum
        play sound cum
        "That’s it, I couldn’t hold back anymore. I unloaded deep into Melody as my eyes rolled back and my body was rattled with euphoric sensation."
        show melody sex5 with cum
        play sound cum
        show melody sex5 with cum
        play sound cum
        "Her pussy tightly clenched around my cock as she rode me throughout the entire orgasm, milking my cock for every drop of semen it could."
        show melody sex5 with dissolve
        stop ambience fadeout 3.0
        "As the rush of lust slowly dissipated between the two of us, we were both left panting, with her on top of me."
        show melody sex7 with dissolve
        play sound cum
        "She raises herself from my cock and grimaces as it flops out with a blob of cum."
        melody "Ahh shit… I lost myself in the moment and made you cum too soon."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        melody "I was hoping to use you with a few org- AH!"
        scene bg melodybedroom with dissolve
        stop music fadeout 2.0
        "At that moment, something took us both by surprise as someone burst into the room, making us both jump."
        "We didn’t freak out, or try to cover ourselves. Both me and Melody were in such a compromising position, we could do nothing but stare, frozen in shock."
        show ruby shocked with dissolve:
            xpos 800
            ypos 25
        play music challenge
        ruby "Oh, oh dear."
        show ruby sad with dissolve
        ruby "I-uh, I guess I’ll…"
        show melody closesatisfied with dissolve:
            xpos 75
            ypos 70
        melody "No, no, it’s whatever, you can stay."
        mc "Wait, she can?"
        show melody closesad with dissolve
        "Melody gets off me and kneels down on the bed facing Ruby. Leaving me to quickly cover myself up."
        show ruby shocked with dissolve
        ruby "Oh my…"
        mc "Isn’t this weird? Am I in trouble?"
        melody "Don’t be ridiculous, we’re all grown adults here."
        show ruby laughing with dissolve
        ruby "Single too, nothing wrong with mingling as they say."
        mc "I- uh, right. Don’t you care at all, Ruby?"
        show ruby horny with dissolve
        ruby "What do you mean, darling?"
        "Is she really so out of touch that she can’t see how weird this situation is?"
        show melody closesatisfied with dissolve
        melody "I know where this is going…"
        show melody closesurprised with dissolve
        melody "Don’t expect a threesome you pervert."
        mc "Easy now, I didn’t say anything like that."
        show ruby shocked with dissolve
        ruby "Pervert… You think [playername] is a pervert?"
        show melody closedeath1 with dissolve
        melody "Well yeah, he slept with both of us, how gro-o-oh… Hmm…"
        show melody closeneutral with dissolve
        melody "Maybe I should stop saying it’s gross now."
        show ruby laughing with dissolve
        ruby "If he’s perverted, what does that make us?"
        ruby "Sisters that secretly planned to share and sleep with him, hehe."
        mc "Wait, what?"
        show melody closesatisfied with dissolve
        show ruby horny with dissolve
        ruby "We’ve just been using you to live out our naughtiest fantasies, we’re the perverted ones."
        "I’m at a complete loss for words… It wasn’t just Melody this entire time, they’re both evil scheming demons."
        "It completely makes sense too, Ruby lived out her voyeurism fantasies while Melody lived out her fem-dom fantasies."
        show melody closehappy with dissolve
        melody "He enjoyed it, so we’re like a trio of proud pervs."
        show ruby sad with dissolve
        ruby "My apologies darling, I thought you were at least somewhat aware."
        mc "I guess I was; I just didn’t realize to what extent."
        show melody closeneutral with dissolve
        melody "ANYWAY, what’s the big idea, why did you barge in here?"
        show melody closeangry with dissolve
        melody "I bet you knew that we were fuckin’! You’re so gross, sis! I didn't think your voyeurism extended to your little sister!"
        show ruby shocked with dissolve
        ruby "Oh please, I knew nothing of the sort. I’m here because I have simply magnificent news that I had to share immediately."
        show ruby laughing with dissolve
        ruby "My dress, it was accepted! I just got the mail!"
        show melody closehappy with dissolve
        melody "Awesome! That’s so great, sis!"
        show ruby laughing with dissolve:
            xpos 800
            ypos 25
        show melody happy with dissolve:
            xpos 200
            ypos 70
        "Melody bounces up off the bed, and they hug in an overjoyed and ecstatic way that I’m sure only girls can replicate."
        scene bg boutiquekitchen with dissolve
        "Then the three of us head downstairs to celebrate with some red wine."
        show melody happy with dissolve:
            xpos 200
            ypos 70
        melody "You can finally focus on making dresses now, right Ruby?"
        melody "Oh, and perhaps a certain piano?"
        show ruby happy with dissolve:
            xpos 800
            ypos 25
        ruby "That’s the idea, Mel."
        "Did she just call Melody, Mel? That's adorable!"
        ruby "Oh and [playername], you’re still looking for work right? You can always come back."
        ruby "In fact, I implore you, do come back."
        show melody fufufu with dissolve
        melody "No way, he should come back for me, not you!"
        show ruby laughing with dissolve
        ruby "We’ll take turns, is that alright, darling?"
        "Bloody hell."
        stop music fadeout 3.0
        scene bg black with dissolve
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu

        "…"
        if livingwithmoxie == 1:
            play ambience ambiencenight fadein 3.0
            play music wagon fadein 13.0
            show bg moxiewagonlamp with dissolve
            "Filled with satisfaction after a wholesome day of work, I get paid 25 monies, and I return to the wagon with the knowledge that I’ll always be welcome back."
            "Where I’ll be endlessly victim to their lustful schemes, but hey, who doesn’t like being teased by cute girls every now and then?"
            "I settle down back at the wagon and Moxie soon joins me with her uplifting, perky personality that acts as the perfect cherry on top of any day."
            show moxie laughing with dissolve
            moxie "Heyy! How’s it going man?"
            mc "Ah you know, same old, same old."
            show moxie happyneutral with dissolve
            moxie "Where’d you go today?"
            mc "It was the boutique again, everything turned out quite sweet, so you don’t have to worry about that teasing stuff I mentioned before."
            show moxie happy with dissolve
            moxie "I’m glad to hear that. I was genuinely worried that some weird mare would harass you, hopefully that’ll never happen though."
            mc "Hey, I’ve got a question. Just how perverted is the average mare? Would anyone actually harass me?"
            show moxie shocked with dissolve
            moxie "Uhhhh, could you define perverted?"
            mc "Hmm... Sexually forward, promiscuous, et cetera."
            show moxie neutral with dissolve
            moxie "From the gist I've gathered, I can definitely claim the women in this world are far more sexually forward than you’ll be used to."
            mc "You can say that again."
            show moxie angry with dissolve
            moxie "Of course, being more sexually forward also may come with some toxic behaviours like cat-calling or inappropriate touching."
            mc "Sheesh, how do you even help creeps like that?"
            show moxie neutral with dissolve
            moxie "I think they just need to be aware that what they’re doing is unacceptable and they should move that energy into more positive and productive things."
            mc "Positive and productive things?"
            show moxie shy with dissolve
            moxie "You know, if they’re really that repressed and frustrated, they should put that energy into going on dates, or something."
            show moxie althappy with dissolve
            moxie "That’s what I did, I was frustrated and tried to summon a familiar with that spell."
            mc "I like your introspection, that’s good advice."
            show moxie happy with dissolve
            moxie "Why thank you, now how about I cook us up something even better than my shoddy advice."
            hide moxie with dissolve
            scene bg black with dissolve
            "..."
            jump evening
        elif livingwithbutters == 1:
            play ambience ambiencenight fadein 3.0
            play music butters fadein 13.0
            show bg buttershousedark with dissolve
            "Filled with satisfaction after a wholesome day of work, I return to the cottage with the knowledge that I’ll always be welcome back."
            "Where I’ll be endlessly victim to their lustful schemes, but hey, who doesn’t like being teased by cute girls every now and then?"
            "I settle down on a sofa at the cottage, and Butters soon joins me with her uplifting, wholesome personality that acts as the perfect cherry on top of any day."
            show butters dresslaughing with dissolve
            butters "Heyy! How's it going [playername]?"
            mc "Ah you know, same old, same old."
            show butters dresshappy with dissolve
            butters "Look what I got! A dewblossom! It doesn't sting me anymore! Hehe."
            mc "That's great news! Congratulations."
            butters "Where’d you go today?"
            mc "It was the boutique again, everything turned out quite sweet, so you don’t have to worry about that teasing stuff I mentioned before."
            butters "I’m glad to hear that. I wouldn't want anyone to ruin your experience in this lovely world."
            mc "Hey, I’ve got a question. Just how perverted is the average mare? Would anyone actually harass me?"
            show butters dresssurprised with dissolve
            butters "Perverted? Probably somewhere between me and my succubus."
            mc "Hmm... That sounds bad..."
            show butters dressneutral with dissolve
            butters "You told me you're from another world, it sounds like the girls in this world are hornier."
            mc "You can say that again."
            show butters dressangry with dissolve
            butters "But harassing? That's only among a few nasty individuals, even in such a lovely town like Arcadia there are some."
            butters "Umbra was one of those, thankfully I haven't had to deal with any creeps since him, but I'm good at noticing the red flags."
            mc "Sheesh, how do you even help creeps like that."
            show butters dressneutral with dissolve
            butters "I think they just need to be aware that what they’re doing is unacceptable and they should move that energy into more positive and productive things."
            mc "Positive and productive things?"
            show butters dresssad with dissolve
            butters "You know, if they’re really that repressed and frustrated, they should put that energy into something else."
            show butters dresshappy with dissolve
            butters "That’s what I did, when I was distracted by my lusts, I'd distract myself with work."
            mc "I like your introspection, that’s good advice."
            show butters dresshappy with dissolve
            butters "Thank you babe, how about I cook us up something even better than my advice."
            hide butters with dissolve
            scene bg black with dissolve
            "..."
            jump evening
        else:
            pass
    label boutiqueafter:
        scene bg boutiquedoor with dissolve
        scene bg boutiqueinside with dissolve
        show ruby happy with dissolve
        play music boutique fadein 3.0
        if boutiqueaftervisit1 == 0:
            $ boutiqueaftervisit1 = 1
            ruby "Good morning darling! Here to work, buy, or perhaps something else?"
            mc "Wow, look at this place, it's so tidy and organised now! You really turned this place around, I'm proud."
            show ruby laughing with dissolve
            ruby "Oh, darling, this is all thanks to your superb help."
            ruby "My dress has gone on to be a wonderful success! You and I made a great team."
            show ruby happy with dissolve
            ruby "Of course, we can still do those fun shows later on if that's what you'd like."
        else:
            ruby "Good morning darling! Here to work, buy, or perhaps something else?"
        menu boutiqueaftermenu:
            "Shop":
                if maiddressbought == 1:
                    "There's nothing I need to buy here, maybe later."
                    jump boutiqueaftermenu
                else:
                    menu:
                        "Maid Dress (50 Monies)" if maiddressbought == 0 and monies >= 50:
                            if monies < 50:
                                "I can't afford that."
                                jump boutiqueaftermenu
                            else:
                                ruby "Pleasure doing business with you!"
                                mc "By the way, can you leave the dress here?"
                                ruby "Here? Do you want to pick it up at a later time?"
                                mc "Yes, you'll see."
                                $ monies -= 50
                                $ maiddressbought = 1
                                jump boutiqueaftermenu
                        #"Lingerie (100 Monies)" if lingeriebought == 0:
                        #    if monies < 100:
                        #        "I can't afford that."
                        #        jump boutiqueaftermenu
                        #    else:
                        #        ruby "Pleasure doing business with you!"
                        #        $ monies -= 50
                        #        $ lingeriebought = 1
                        #        jump boutiqueaftermenu
                        "Back":
                            jump boutiqueaftermenu
            "Talk" if rubytalks == 0:
                menu:
                    "Talk to Ruby about being friends with benefits":
                            show ruby closelaughing with dissolve
                            ruby "So darling, I don't mean to pry too much into your personal life. However, I imagine you must get a lot of action, yes?"
                            mc "I-uh, what makes you say that?"
                            show ruby closeneutral with dissolve
                            ruby "Needless to say, you slept with both my sister and I. There must be others, right?"
                            mc "Yeah, I'll admit that much, although you two came onto me."
                            show ruby closehorny with dissolve
                            ruby "Ahaha, sorry about that. It's just that you're such a juicy morsel."
                            mc "Now I feel like I was you and your sister's prey."
                            show ruby closelaughing with dissolve
                            ruby "Anyway, I know we're friends with benefits, but I wanted to ask. I was wondering if it would be okay if I slept with others too?"
                            menu:
                                "Yeah of course, I sleep around with enough girls as is.":
                                    mc "It would be unfair if I didn't let you do the same."
                                    show ruby closehappy with dissolve
                                    ruby "How delightful, I'll tell her right away."
                                    mc "Her? Who's that?"
                                    show ruby closeembarrassed with dissolve
                                    ruby "Oh! It's a secret!"
                                    mc "I see, I won't pry then."
                                    "How curious, Ruby has a lesbian love interest? Maybe it's a female fan of her camshows."
                                    "Maybe it's someone I know."
                                "Nah... I like it when it's just you and I. I wouldn't be against a third participant, though.":
                                    show ruby closeneutral with dissolve
                                    ruby "Awh darling... I guess I understand, a lady shouldn't sleep around, right?"
                                    mc "Well, I kinda feel bad now. Aren't you worried about pregnancy?"
                                    show ruby closehappy with dissolve
                                    ruby "You've got a point. But you're right. I'm more of a voyeur than someone that does the sleeping anyway."
                                    ruby "I just thought I'd ask out of curiosity more than anything."
                    "Talk to Ruby about sleeping with Melody":
                            mc "There's something on my mind."
                            ruby "What's that darling?"
                            mc "I'm just wondering why you're so nonchalant about letting me sleep with your little sister?"
                            show ruby closeembarrassed with dissolve
                            ruby "Is that a problem? She's even feistier than I am, so there's nothing to worry about."
                            mc "Yeah that's true, but I think you're missing the point. We have this strange two-sister one-man love triangle, don't you think that's strange?"
                            show ruby closehappy with dissolve
                            ruby "Perhaps it's a little weird, but I like to think of it as a happy accident where the three of us are mature enough to settle this like adults."
                            ruby "Think of all the moments in great literature where an attractive man incidently seduced both lady and sister."
                            show ruby closelaughing with dissolve
                            ruby "What a tragedy it would be if either one of us were selfish enough to cut off that joy, rather than share in it."
                            mc "Uhh... Yeah, okay."
                            ruby "It also fits into my interests as a voyeur."
                            mc "Fits your interest? I hope you aren't implying you watch us do it."
                            show ruby closesad with dissolve
                            ruby "Never darling! B-But I may be able to hear sometimes..."
                            mc "You can hear us?"
                            show ruby closeneutral with dissolve
                            ruby "Well, the walls are awfully thin darling..."
                            mc "Do you masturbate to the sounds?"
                            show ruby closeembarrassed with dissolve
                            ruby "I-uh, n-no! Never!"
                            "She's such a bad liar."
                    "Ask Ruby about her mother":
                            mc "Melody briefly mentioned your mother ran away, could you tell me what she meant?"
                            show ruby closeneutral with dissolve
                            ruby "Oh, her... That woman infuriates me."
                            show ruby closeangry with dissolve
                            ruby "She's such a delusional narcissist, acts like she's better than everyone else, and I'm worried a part of her believes it."
                            ruby "She actually ran away a long time ago, I'm surprised Melody mentioned it."
                            mc "What happened?"
                            show ruby closeneutral with dissolve
                            ruby "Never wanting to work a day in her life, she'd just try to hitch rides with richer stallions by looking pretty and acting dumb."
                            ruby "Through her first divorce we actually managed to get enough money to buy one of the largest houses in the suburbs."
                            show ruby closesad with dissolve
                            ruby "That stallion was me and Mel's father, the breakup wasn't pretty so we were estranged for awhile. But more recently we've started visiting more often."
                            ruby "Turned out I have a little brother, I had no idea."
                            mc "Why did they divorce?"
                            show ruby closeneutral with dissolve
                            ruby "Cheating... My mother cheated and stayed with the new guy for a few years until I was about sixteen."
                            ruby "And then they just vanished, leaving me to look after Melody who was only eleven at the time."
                            mc "That's awful..."
                            show ruby closesad with dissolve
                            ruby "It's like she didn't even love us, we were just tools to get what she wanted, and the moment we stopped being useful she just left us."
                            ruby "I can't even imagine how anyone could think that about their own family."
                            mc "Me neither, that's twisted as fuck."
                            show ruby closeneutral with dissolve
                            ruby "Yeah... I'd rather not leave the story on a sad note, but unfortunately not much good has come out of my family."
                    "Ask Ruby about her voyeurism fetish":
                            mc "So Ruby, you're obviously a big voyeur, how'd that happen?"
                            ruby "Hmm... How did I get a fetish? That's a difficult question darling."
                            mc "I think we were all vanilla once, just think back to where it all began."
                            ruby "Mmmm... When I first started watching pornography on the internet, I'd like to watch it as a third party."
                            ruby "Rather than imagining myself as the girl in the sex scenes, I'd imagine myself watching. Not as a cuckold mind you, as a voyeur."
                            show ruby closehappy with dissolve
                            ruby "Perhaps watching porn for me was a natural path to voyeurism?"
                            mc "You like being watched too, right?"
                            show ruby closelaughing with dissolve
                            ruby "Ohoh definitely darling! That one's a little easier to explain."
                            show ruby closehappy with dissolve
                            ruby "Some of my earlier boyfriends were long distance, I liked having people watch me on the web camera and that must have become a fetish."
                            "This girl is so far off from my first impression."
                            "Guess you can never judge someone by how they act or look."
                            "In fact, you can probably never truly know someone in and out, not even the person you're closest to."
                    "Back":
                        jump boutiqueaftermenu
                $ rubytalks = 1
                show ruby happy with dissolve
                jump boutiqueaftermenu
            "Work":
                mc "Got any work for me?"
                show ruby laughing with dissolve
                ruby "Plenty, how about you start by making us both a drink?"
                "I work as Ruby's personal assistant all day at the boutique and earn 25 monies."
                $ monies += 25
                $ rand = renpy.random.randint(1,2)
                if rand == 1 and rubylingeriesex == 0:
                    $ rubylingeriesex = 1
                    jump rubylingeriesex
                else:
                    pass
                jump rubyafternoon
            "Sex" if saruby == 0:
                $ saruby = 1
                ruby "I'd love to, but only after work. Sorry darling!"
                "Looks like Ruby will only have sex with me after work."
                jump boutiqueaftermenu
            "Visit Melody" if boutiqueafteramv == 0:
                $ boutiqueafteramv = 1
                ruby "You wanna see Mel?"
                ruby "Sorry, you missed her. She always leaves for college early, she likes to spend an hour studying before class, bless her heart."
                ruby "You should come back in the evening, she'll be here then."
                jump boutiqueaftermenu
            "Leave":
                jump preworldmap
    label rubyafternoon:
        scene bg black with dissolve
        stop music fadeout 3.0
        play ambience ambiencenight fadein 3.0
        show bg boutiquekitchen with dissolve
        show ruby closehappy with dissolve
        ruby "What a productive day, smashing work, [playername]."
        mc "Never underestimate how much an assistant can help you out."
        menu rubyeveningmenu:
            "Talk" if rubytalks == 0:
                menu:
                    "Talk to Ruby about being friends with benefits":
                        show ruby closelaughing with dissolve
                        ruby "So darling, I don't mean to pry too much into your personal life. However, I imagine you must get a lot of action, yes?"
                        mc "I-uh, what makes you say that?"
                        show ruby closeneutral with dissolve
                        ruby "Needless to say, you slept with both my sister and I. There must be others, right?"
                        mc "Yeah, I'll admit that much, although you two came onto me."
                        show ruby closehorny with dissolve
                        ruby "Ahaha, sorry about that. It's just that you're such a juicy morsel."
                        mc "Now I feel like I was you and your sister's prey."
                        show ruby closelaughing with dissolve
                        ruby "Anyway, I know we're friends with benefits, but I wanted to ask. I was wondering if it would it be okay if I slept with others too?"
                        menu:
                            "Sure":
                                mc "Yeah of course, I sleep with enough girls as is. It would be unfair if I didn't let you do the same."
                                show ruby closehappy with dissolve
                                ruby "How delightful, I'll tell her right away."
                                mc "Her? Who's that?"
                                show ruby closeembarrassed with dissolve
                                ruby "Oh! It's a secret!"
                                mc "I see, I won't pry then."
                                "How curious, Ruby has a lesbian love interest? Maybe it's a female fan of her camshows."
                                "Maybe it's someone I know."
                            "Nah":
                                mc "Nah... I would feel better if it was just you and I."
                                show ruby closeneutral with dissolve
                                ruby "Awh darling... I guess I understand, a lady shouldn't sleep around, right?"
                                mc "Well, I kinda feel bad now. Aren't you worried about pregnancy?"
                                show ruby closehappy with dissolve
                                ruby "You've got a point. But you're right. I'm more of a voyeur than someone that does the sleeping anyway."
                                ruby "I just thought I'd ask out of curiosity more than anything."
                    "Talk to Ruby about sleeping with Melody":
                        mc "There's something on my mind."
                        ruby "What's that darling?"
                        mc "I'm just wondering why you're so nonchalant about letting me sleep with your little sister?"
                        show ruby closeembarrassed with dissolve
                        ruby "Is that a problem? She's even feistier than I am, so there's nothing to worry about."
                        mc "Yeah that's true, but I think you're missing the point. We have this strange two-sister one-man love triangle, don't you think that's strange?"
                        show ruby closehappy with dissolve
                        ruby "Perhaps it's a little weird, but I like to think of it as a happy accident where the three of us are mature enough to settle this like adults."
                        ruby "Think of all the moments in great literature where an attractive man incidently seduced both lady and sister."
                        show ruby closelaughing with dissolve
                        ruby "What a tragedy it would be if either one of us were selfish enough to cut off that joy, rather than share in it."
                        mc "Uhh... Yeah, okay."
                        ruby "It also fits into my interests as a voyeur."
                        mc "Fits your interest? I hope you aren't implying you watch us do it."
                        show ruby closesad with dissolve
                        ruby "Never darling! B-But I may be able to hear sometimes..."
                        mc "You can hear us?"
                        show ruby closeneutral with dissolve
                        ruby "Well, the walls are awfully thin darling..."
                        mc "Do you masturbate to the sounds?"
                        show ruby closeembarrassed with dissolve
                        ruby "I-uh, n-no! Never!"
                        "She's such a bad liar."
                    "Ask Ruby about her mother":
                        mc "Melody briefly mentioned your mother ran away, could you tell me what she meant?"
                        show ruby closeneutral with dissolve
                        ruby "Oh, her... That woman infuriates me."
                        show ruby closeangry with dissolve
                        ruby "She's such a delusional narcissist, acts like she's better than everyone else, and I'm worried a part of her believes it."
                        ruby "She actually ran away a long time ago, I'm surprised Melody mentioned it."
                        mc "What happened?"
                        show ruby closeneutral with dissolve
                        ruby "Never wanting to work a day in her life, she'd just try to hitch rides with richer stallions by looking pretty and acting dumb."
                        ruby "Through her first divorce we actually managed to get enough money to buy one of the largest houses in the suburbs."
                        show ruby closesad with dissolve
                        ruby "That stallion was me and Mel's father, the breakup wasn't pretty so we were estranged for awhile. But more recently we've started visiting more often."
                        ruby "Turned out I have a little brother, I had no idea."
                        mc "Why did they divorce?"
                        show ruby closeneutral with dissolve
                        ruby "Cheating... My mother cheated and stayed with the new guy for a few years until I was about sixteen."
                        ruby "And then they just vanished, leaving me to look after Melody who was only eleven at the time."
                        mc "That's awful..."
                        show ruby closesad with dissolve
                        ruby "It's like she didn't even love us, we were just tools to get what she wanted, and the moment we stopped being useful she just left us."
                        ruby "I can't even imagine how anyone could think that about their own family."
                        mc "Me neither, that's twisted as fuck."
                        show ruby closeneutral with dissolve
                        ruby "Yeah... I'd rather not leave the story on a sad note, but unfortunately not much good has come out of my family."
                    "Ask Ruby about her voyeurism fetish":
                        mc "So Ruby, you're obviously a big voyeur, how'd that happen?"
                        ruby "Hmm... How did I get a fetish? That's a difficult question darling."
                        mc "I think we were all vanilla once, just think back to where it all began."
                        ruby "Mmmm... When I first started watching pornography on the internet, I'd like to watch it as a third party."
                        ruby "Rather than imagining myself as the girl in the sex scenes, I'd imagine myself watching. Not as a cuckold mind you, as a voyeur."
                        show ruby closehappy with dissolve
                        ruby "Perhaps watching porn for me was a natural path to voyeurism?"
                        mc "You like being watched too, right?"
                        show ruby closelaughing with dissolve
                        ruby "Ohoh definitely darling! That one's a little easier to explain."
                        show ruby closehappy with dissolve
                        ruby "Some of my earlier boyfriends were long distance, I liked having people watch me on the web camera and that must have become a fetish."
                        "This girl is so far off from my first impression."
                        "Guess you can never judge someone by how they act or look."
                        "In fact, you can probably never truly know someone in and out, not even the person you're closest to."
                    "Back":
                        jump rubyeveningmenu
                $ rubytalks = 1
                jump rubyeveningmenu
            "Sex" if rubysex == 0:
                menu:
                    "Threesome" if fr == 1:
                        $ rubysex = 1
                        show ruby closehappy with dissolve:
                            xpos 250
                            ypos 720
                        ruby "Ooohh, what a great idea! I had a lot of fun last time."
                        show melody closeangry with dissolve:
                            xpos 600
                            ypos 100
                        melody "No, no, no, no, no, no no, no, no, no, no."
                        melody "Nononononononononononono!"
                        melody "That's too gross!"
                        "Looks like I'll have to convince Melody, like a boss battle?"
                        "If I pick the wrong choices, she'll refuse and I'll have to try again another day."
                        menu:
                            "You overreact, but I know you enjoyed it Melody.":
                                show melody closeneutral with dissolve
                                melody "Yeah, but... I was totally brainwashed! I was spouting all sorts of bullshit nonsense filth that I didn't believe!"
                            "But Ruby really likes it, can't you do it for her?":
                                show melody closeangry with dissolve
                                melody "Is there something wrong with your head? Are you ill? Perhaps mentally?"
                                melody "I'm going up to my room."
                                hide melody with dissolve
                                ruby "Awhh... That kinda killed the mood."
                                jump rubyeveningmenu
                        melody "It's so wrong to assume that's me!"
                        menu:
                            "Actually, the brainwashing doesn't change your personality at all, I know that for a fact. Melody, I {b}KNOW{/b} you enjoyed the threesome.":
                                melody "N-No way?! You knew that?!"
                            "Come on, don't pretend you don't love my cock all of a sudden, this tsundere side doesn't suit you.":
                                show melody closeangry with dissolve
                                melody "Foolish fool! I only use you for my pleasure."
                                melody "Don't pretend I'm the one sucking up to you, when you're always sucking up to me."
                                melody "Gah! Shit! I'm outta here, come visit me later if you want me to fuck you."
                                hide melody with dissolve
                                ruby "Awhh... That kinda killed the mood."
                                jump rubyeveningmenu
                        show melody closesad with dissolve
                        melody "N-No way, no way! It's a lie!"
                        melody "I accidentally said so many embarrassing things while under the influence, eep!"
                        ruby "Hah, the secret is out Melody! You're just as much of a degenerate as I am!"
                        mc "Hehe, that's true."
                        melody "Wha?! You're both bullying me, it's no fair!"
                        ruby "Can't you handle us? So much for the indomitable Melody!"
                        melody "Grr! I'll fuck the hell outta both of you! Get on the table ya damn slut."
                        "Hell yes!"
                        play music sex1 fadein 3.0
                        show rubymelody threesome1 with dissolve
                        "On the edge of the kitchen table, the girls stack on top of each other, their legs interlocked as their labia brush against each other slightly."
                        melody "I'm so hot I'm gonna make you both come easily! Fuck her first, [playername]."
                        "Melody’s pussy drools slightly onto Ruby’s, creating a lewd connection between the two."
                        show rubymelody threesome2 with dissolve
                        "After admiring the sight for perhaps a little too long, I position myself adjacent to the table."
                        play sound cum
                        play ambience sex fadein 3.0
                        show rubymelody threesome3 with dissolve
                        "Ruby's pussy throbs as I line the tip of my cock against her vagina and push forward."
                        ruby "Ohhh!"
                        "My cock sinks into Ruby, enjoying the intense tightness of her pussy. Her thighs quiver as I plunge inch and every inch inside."
                        melody "Saving the best for last, hehe. Think you can handle his cock and my grinding?"
                        "The slightly immoral situation excites all three of us."
                        "Melody starts to gradually grind back and forth, her pussy dripping onto the point of connection of her sister and I."
                        "While Ruby’s hot and enticing walls tighten around my throbbing member."
                        "As I fuck Ruby, it’s hard to forget just how experienced Ruby is at using the muscles in her pelvis to squeeze and tease my cock."
                        ruby "Mmmhhh, your dick feels so great darling!"
                        melody "Hmph… How does it feel to be such a nasty whore that you let someone fuck you while your sister watches?"
                        ruby "Ooohh, i-it's so embarrassing and hot!"
                        "Ruby’s entire body quivers with excitement, her pussy clamps down in intervals, squeezing my cock as it buries itself inside of her."
                        "It seems Ruby is getting a lot of additional pleasure being watched. This kind of perverted situation is perfect to get someone like her off."
                        "Her hips wouldn’t stop meekly shaking in an attempt to maximise the pleasure, inadvertently grinding her clit with her sister’s."
                        show rubymelody threesome4 with dissolve
                        melody "Agghh?! Y-You’re fucking like a crazy person sis! Nnnghh…"
                        "Despite what she said, her hips are also erratically moving back and forth; the sisters now grinding together while I pound into Ruby’s sopping wet pussy."
                        "After about a minute fucking and the pleasure constantly rising, Ruby's back curls as a mind shattering orgasm robs her from her body's control."
                        ruby "T-This is t-too much, ahhh, I-I’m cominnggg! I’m cooommminnggg! I’m coommmmiingggg!!  "
                        "Putting some more strength into my limbs, I push myself as fast as possible to orgasm. Aided by Ruby’s rhythmic orgasmic contractions, I was soon pushed to my limit."
                        play sound cum
                        show rubymelody threesome5 with cum
                        play sound cum
                        show rubymelody threesome5 with cum
                        "Finally, unable to bear it, I blew a huge load into the climaxing mare."
                        play sound cum
                        show rubymelody threesome5 with cum
                        play sound cum
                        show rubymelody threesome5 with cum
                        "Like a rushing wave, her pussy was immediately filled with my hot seed."
                        show rubymelody threesome6 with dissolve
                        ruby "Mmmphhhh, ohhh my gosshhhhh! I can’t believe my little sister is watching me being creampied!"
                        melody "Quit it with the hentai dialogue! It's disgustin- mmmgghhh?!"
                        show rubymelody threesome7 with dissolve
                        "Catching Melody off guard, I plunge my cock into her tight snatch."
                        "She’s so immensely wet that I sink in even faster than I expected. Her pussy is usually tighter than this, but she’s so aroused that she accepts my girth far easier."
                        "Ruby was still paralyzed in the glow of her orgasm. Meanwhile Melody’s body twitches, and her toes curl in response to the sudden spike of pleasure."
                        melody "Ahahahhh, haaahhhh, finally, you fucker! Nnghhh, surprised a man like you has the energy to go immediately."
                        "It takes a while for my cock to harden as much as it was before my orgasm, but Melody’s tight throbbing pussy easily brings our rutting back up to speed."
                        melody "You jealous Rubes? I'm getting this amazing cock now, ahaha!"
                        ruby "Haahhh… S-So lewd..."
                        "I pound Melody’s pussy with enough force to keep her from focusing on anything else, pushing any thoughts out of her mind other than pure pleasure."
                        melody "Hahh, haah, haah, gfffhhh, yes, t-that’s it, ya horny bastard!"
                        "She was aching with desire as her body relaxed and melted into Ruby’s."
                        "With each thrust, both of the girls wiggled back and forth. Their clits still brushed against each other, the occasional moan still escaping from Ruby."
                        "I grit my teeth, as pleasurable as this is, it’s still extremely difficult to orgasm twice in a row. I need to maintain my speed to reach orgasm."
                        show rubymelody threesome8 with dissolve
                        ruby "Mmmphh, Melody, milk as much cum from [playername]’s cock as possible, come on!"
                        melody "Gyyaaahhh, ah-ahm trying, I can’t focus!"
                        ruby "Don’t hold back sis, grind your hips into him a little."
                        melody "Y-Yeah, haah, ghh… I-I’m the one that fucks, ahh-ah, I’ll make you cum, ya damn worm!"
                        "Melody’s ass starts bouncing up and down almost immediately with vigour and energy, matching the pure intensity of my own thrusts and rocking the entire table."
                        "Indirectly the amount of clit rubbing from the intense fuck causes Ruby to wriggle with pleasure below us"
                        ruby "Kyaaahh, y-you’re gonna make me come first, mmphh, mmm, s-sis!"
                        melody "S-shut up with that sis shit! Y-you’re putting me off!"
                        melody "Cum for me damnit! [playername]!"
                        "Pounding my dick against her ass, that familiar feeling of climax finally began to rise."
                        play sound cum
                        show rubymelody threesome9 with cum
                        play sound cum
                        show rubymelody threesome9 with cum
                        "My throbbing cock began pumping seed deep into Melody’s pussy and womb. The feeling of my hot cum seeping inside resulted in her own reactionary orgasm."
                        play sound cum
                        show rubymelody threesome9 with cum
                        play sound cum
                        show rubymelody threesome9 with cum
                        stop ambience fadeout 3.0
                        melody "Yess, aaagghhh, that’s it!! Mm! Mmmm!"
                        ruby "Ahh, f-fuck, y-you made me come too- aa-ah and I wasn't even being fucked! Uhahh…"
                        "I piston in and out of Melody’s squeezing insides for my entire orgasm, maximising the pleasure of the experience. No one will blame me for enjoying her pussy for a few extra seconds."
                        show rubymelody threesome10 with dissolve
                        stop music fadeout 3.0
                        melody "Phew... Fuckin' hell."
                        scene bg black with dissolve
                        "The three of us cool down in the kitchen with some water, as if we just finished a tough workout."
                        "We didn't mention the sex a single time, but we were all satisfied."
                        jump evening
                    "Reverse Cowgirl":
                        $ sexwithrubytoday = 1
                        ruby "Oh darling... How about we take this up to my room?"
                        scene bg black with dissolve
                        show bg rubybedroom with dissolve
                        show ruby photoshoot1 with dissolve
                        play music sex1 fadein 3.0
                        ruby "I've been having a lot of naughty thoughts about you today [playername], look how wet you made me."
                        ruby "A gentlemen needs to help a lady relieve some stress, how about it?"
                        "I get down on my knees and between her pillowy marshmellow thighs and start to lick the juices dripping from her delectable pussy."
                        "Her thighs quiver each time my tongue delicately slips around and over her sensitive clit."
                        ruby "Mmphh, you really are an amazing assistant [playername]... How about we take this to the bed?"
                        menu:
                            "Convince her to do a camshow":
                                $ camshow = 1
                                ruby "Mmm, you want to do it live? I love an audience."
                                ruby "Give me a moment to set it up..."
                                scene bg black with dissolve
                            "Camera off":
                                $ camshow = 0
                                ruby "Lay down for me darling, allow me to service that cock."
                        scene bg rubybedroom2 with dissolve
                        if camshow == 1:
                            "Ruby sets up the camera and turns it on, immediately beginning her stream."
                            ruby "It doesn't matter if anyone tips me, I just want someone to watch us make love for the next hour, hehe."
                            "Hour? Oh jeez."
                        show ruby sexlipbite with dissolve
                        play sound cum
                        "As she sinks that tight pussy over my cock, it feels as good as I imagined."
                        ruby "Mmmphhh, you feel so good inside me..."
                        play ambience sex fadein 3.0
                        if camshow == 1:
                            "A few viewers pour into the chat as Ruby starts to ride my cock up and down at a teasing yet pleasureful pace."
                        else:
                            "She bites her lip, and starts to ride my cock up and down at a teasing yet pleasureful pace."
                        ruby "Just sit back and relax dear, and try not to cum before me, hehe."
                        show ruby sexofacedeep with dissolve
                        show ruby sexoface with dissolve
                        "Her hips start to gain speed as she leans forward, and balances herself so she can put more oomph into the riding."
                        show ruby sexofacedeep with dissolve
                        show ruby sexofaceaction with dissolve
                        show ruby sexofacedeep with dissolve
                        show ruby sexofaceaction with dissolve
                        if camshow == 1:
                            ruby "Ohh, look at that, we have our first donation already. I love it when you guys watch me do this, ahhh..."
                        else:
                            ruby "Mmphh, your cock is so thick inside me, I love fucking you darling."
                        "Her experienced hips start to twist and gyrate my cock in magnificent ways, toying and teasing my shaft while squeezing as much pleasure from me as she can."
                        show ruby sexofacedeep with dissolve
                        show ruby sexofaceaction with dissolve
                        "My point of contact with the mare is a deluge of her juices that constantly dribble and drip onto my pelvis, the wet sounds created from our rutting are vulgar to say the least."
                        show ruby sexofacedeep with dissolve
                        show ruby sexofaceaction with dissolve
                        if camshow == 1:
                            "Every so often the wet sounds are overpowered by a vibration and beep from her laptop as a small donation comes in. The reminder that we're being watched causes Ruby to visibly excite each time."
                        show ruby sexofacedeep with dissolve
                        show ruby sexofaceaction with dissolve
                        ruby "Ohoh gosh, this feels too good, I'll lose my mind!"
                        show ruby sexofacedeep with dissolve
                        show ruby sexofaceaction with dissolve
                        "She purrs pure joy as she pounds against my lap, manhandling my cock with the grip of her tight walls which squeeze and constrict in an attempt to milk me."
                        show ruby sexahegaodeep with dissolve
                        show ruby sexahegaoaction with dissolve
                        "Driven by pure pleasure, she begins to rub her pussy too. She's unable to contain her blissful moans in the face of the dual pleasures, which rapidly build her up to a mind-shattering orgasm."
                        show ruby sexahegaodeep with dissolve
                        show ruby sexahegaoaction with dissolve
                        if camshow == 1:
                            "The audience is loving her enthusiasm as more viewers and donations come through."
                        "Her moans of ecstasy make it clear that she's going to orgasm any second, and as she does, she squeals loudly while her vagina clenches around my cock."
                        show ruby sexahegaodeep with dissolve
                        show ruby sexahegaoaction with dissolve
                        "I can’t hold back any longer. The combination of her moans and her contractions push me over the edge..."
                        show ruby sexahegaocumdeep with cum
                        show ruby sexahegaoactioncum with dissolve
                        show ruby sexahegaocumdeep with cum
                        show ruby sexahegaoactioncum with dissolve
                        "I orgasm, ejaculating thick loads of my cum deep inside of her while she continues to ride, causing a sloppy mess of my cum that bubbles and seeps out of her."
                        show ruby sexahegaocumdeep with cum
                        show ruby sexahegaoactioncum with dissolve
                        show ruby sexahegaocumdeep with cum
                        show ruby sexahegaoactioncum with dissolve
                        ruby "Ohh, yes… Mmm…"
                        show ruby sexlipbitecum with dissolve
                        stop ambience fadeout 3.0
                        "She slowly comes to a stop and catches her breath."
                        stop music fadeout 10.0
                        if camshow == 1:
                            ruby "Phew, I hope you're enjoying the show darlings. Feel free to take a fifteen minute break before part two, hehe."
                            scene bg black with dissolve
                            "After a cleanup and break, we fuck again for the audience before finishing up."
                            show bg rubybedroom with dissolve
                            show ruby laughing with dissolve
                            ruby "Sex with you is one thing, sex with an audience is peak happiness."
                            mc "The things you can do with that ass blow my mind."
                            show ruby happy with dissolve
                            ruby "Oh, and one more thing, we earned a lil' bit of cash doing that stream. Not as much as last time, but here's your share."
                            "She hands me an extra ten monies, sweet."
                            $ monies += 10
                            "We hug and say our goodbyes before I return home."
                            jump evening
                        else:
                            ruby "Hehe, look how much you came..."
                            ruby "Darling, you are a wonderful sex partner…"
                            mc "I think you're one of my favourites too, but don't tell the others!"
                            ruby "Hehe, we're so good that people would tune in to watch. Maybe next time we should do a camshow, what do you think?"
                            scene bg black with dissolve
                            "We hug and say our goodbyes before I return home."
                            jump evening
                    "Back":
                        jump rubyeveningmenu
            "Call it a day":
                ruby "Do come back darling."
                mc "See you later Ruby."
                jump evening
    label melodyevening:
        if melodyeveningvisit1 == 0:
            jump melodyeveningvisit1
        else:
            show bg boutiquedoornight with dissolve
            "Using the key from under the plant pot, I enter the boutique and make my way up to see Melody."
            show bg boutiqueinsidenight with dissolve
            pause 0.3
            show bg boutiqueupstairsnight with dissolve
            pause 0.3
            "I lightly knock on Melody's door and I can hear a nonchalant 'come in' from the other side."
            show bg melodybedroomnight with dissolve
            show melody closesurprised with dissolve
            play music melodytheme fadein 2.0
            melody "Oh! I didn't realize it was a burglar, you should have warned me."
            show melody closehappy with dissolve
            mc "It's nice to see you too."
            melody "What's your poison tonight? Wanna chat, wanna bang? I'm game."
            menu melodyeveningmenu:
                "Talk" if melodytalks == 0:
                    menu:
                        "Talk about her future and stuff":
                            show  melody closeneutral with dissolve
                            melody "Heat is so boring! Wake up? Horny. Lunch? Horny. Evening? Horny."
                            mc "Right now?"
                            melody "Hoooornyy!"
                            show melody closehappy with dissolve
                            melody "And I just masturbated. No need to get hard though. I'm not a sex monster, I have some restraint."
                            melody "Sometimes it's nice to just have a normal conversation for once."
                            mc "What do you want to talk about?"
                            show melody closesatisfied with dissolve
                            melody "Humm, with my exams coming up, I've been thinking a lot about what I'm going to do after college."
                            show melody closehappy with dissolve
                            melody "You're a pretty real dude, and some outside perspective could give me a few ideas."
                            mc "As a musician there are only a few career paths I can think of. An actual composer, someone that plays professionally, or a teacher."
                            show  melody closeneutral with dissolve
                            melody "Eugh, that's all so boring... I hate rules, y'know? And I hate the fact that the musical industry is just a shitty excuse to sleep with attractive peeople."
                            mc "What do you mean?"
                            show  melody closeangry with dissolve
                            melody "I mean rich exec mares grooming attractive young stallions and mares, to be the 'next big thing'."
                            melody "Having sex to climb up the career ladder is extremely common, and I won't be a part of that."
                            mc "Eugh... I can see why that'd be very problematic in this society, I guess even I'm guilty of that."
                            show  melody closeneutral with dissolve
                            melody "You may be working and sleeping with a few mares, but you're not grooming anyone with the potential of fame."
                            mc "I guess the system's fucked. Who's a rich asshole with low restraint gonna hire? The secretary that sucks dick, or the one that doesn't."
                            show  melody closeangry with dissolve
                            melody "Eugh, this pisses me off. This is why I'm an angry bitch that wants to step on balls. I'm so sick of people."
                            mc "There, there... What are you going to do in the future to avoid this shit?"
                            show  melody closeneutral with dissolve
                            melody "I'm gonna go independent, maybe start as a DJ and compose my own things. I told Blossom to do the same thing, fuck the system man."
                        "Talk about her bully-mode":
                            mc "Tell me more about your femme fatale personality."
                            show melody closeneutral with dissolve
                            melody "My... What? Female fatal?"
                            "Eugh, are there no french ponies in this world?"
                            mc "Your uhh, deprecating and cruel personality."
                            show melody closefufufu with dissolve
                            melody "Ohh... You want me to tell you more about that? You really do ask some strange questions, lil' wormy."
                            show melody closeneutral with dissolve
                            melody "I just wanna say 'that's how I am', so you're gonna need to be more specific."
                            mc "I mean, do you like, get off on acting like that? Is it a fetish for you?"
                            show melody closehappy with dissolve
                            melody "Oh! I guess? I like dominating men if that's what you mean."
                            show melody closedeath1 with dissolve
                            melody "Society is so used to putting men on pedestals and worshipping them, so I get a kick out of dragging them down."
                            show melody closeneutral with dissolve
                            melody "But you, you're not like the others. There's no ego on you, which is kinda boring, but at the same time it makes you a great match for me."
                            melody "Because as much as I fetishize dominating men, it comes from a place of hate, I can never truly respect a man that just takes it, nor one with ego."
                            mc "That'll be because my society is completely different to yours. I can tell you now, I was never put on a pedestal."
                            show melody closehappy with dissolve
                            melody "I can't comment on your society, but you have a sharpness to you, a wit that I like."
                            melody "The few stallions at my college are soft, or they think they're the goddess's gift to the world."
                            show  melody closeneutral with dissolve
                            melody "That's why I... Uh."
                            mc "Hm? What's wrong?"
                            show melody closesatisfied with dissolve
                            melody "I feel like you understand me, and you actually challenge me too."
                            show melody closehappy with dissolve
                            melody "That's the only reason I had sex with you. Handjob, blowjob, whatever, I wouldn't have let you take my virginity unless I was absolutely sure."
                            mc "And you were sure?"
                            melody "I sure was, champ."
                        "Ask her why she decided to sleep with you":
                            mc "So it's not shocking at this point that we're friends with benefits, right?"
                            show melody closefufufu with dissolve
                            melody "Pfft, you think we're friends? That's adorable!"
                            mc "Alright smarty-pants, what are we then?"
                            show melody closesadistic with dissolve
                            melody "Melody and worm, with benefits! Geheheh."
                            mc "I was just wondering if you had any other 'worms with benefits'?"
                            show melody closeangry with dissolve
                            melody "What, you think I'm fucking around? Do I look like some kinda slut?"
                            "She seemed to take that surprisingly personally."
                            mc "But... I am?"
                            show melody closesatisfied with dissolve
                            melody "I dunno, guess you are a slut."
                            mc "What would happen if you wanted to take things more seriously with me or someone else?"
                            show melody closeneutral with dissolve
                            melody "I'd ask you to stop being a slut and date me, or something."
                            melody "What kind of questions are these?"
                            mc "Just trying to understand our unspoken relationship a little better."
                            show melody closehappy with dissolve
                            melody "Ohhh, you should have said."
                            show melody closefufufu with dissolve
                            melody "I'm Melody, and you're the pathetic worm that sleeps with all the ponies."
                            show melody closesadistic with dissolve
                            melody "Pahaha, you're a disgrace really."
                            mc "Well, when you put it that way, I do seem pretty bad."
                            show melody closesatisfied with dissolve
                            melody "It's not like I blame you...  If I was a man, I'd probably do the same thing."
                            show melody closeneutral with dissolve
                            melody "Remember, it was me that encouraged you to sleep with my sister for my own personal gain. Then I slept with you too, 'cause I liked ya."
                            show melody closehappy with dissolve
                            melody "So it's not like I'm much better."
                            mc "Glad you understand, I guess."
                            show melody closeneutral with dissolve
                            melody "Me sleeping with you was never part of the original plan."
                            mc "Was it not?"
                            show melody closehappy with dissolve
                            melody "Nah, I encouraged Ruby to be open with herself and sleep with you. She told me to do the same, but I declined saying I wasn't interested."
                            melody "Ruby can always see through me though. She probably knew from the start that I was interested in you."
                            melody "I don't know to what extent you realize this, but Ruby's a lot like me, but she keeps her thoughts to herself. She's dangerously sharp sometimes."
                        "Back":
                            jump melodyeveningmenu
                    $ melodytalks = 1
                    show melody closehappy with dissolve
                    jump melodyeveningmenu
                "Sex":
                    if sexwithrubytoday == 1:
                        show melody closefufufu with dissolve
                        melody "Hate to break it to you worm, but I'm not fucking ya after you've just fucked my sister."
                        if fr == 1:
                            mc "You gonna let that stop you, even after everything we've been through?"
                            melody "Hmm... Ahh, you know what? Forget it."
                            melody "What do you wanna do?"
                            jump swrtms
                        mc "Wha? How'd you know?"
                        show melody closeneutral with dissolve
                        melody "She's really noisy, and the walls are thin..."
                        show melody closesatisfied with dissolve
                        melody "Least you could do is shower first, if you put your dick in me now, that's borderline incest!"
                        jump melodyeveningmenu
                    pass
                    melody "So, you want to up your burglary charge to rape?"
                    show melody closesadistic with dissolve
                    melody "Victim, that is, mehehe."
                    label swrtms:
                        pass
                    $ time = 0.8
                    $ timer_range = 0.8
                    $ timer_jump = "mspt1"
                    show screen countdown
                    menu:
                        "Handjob":
                            pass
                        "Blowjob":
                            pass
                        "Cowgirl":
                            pass
                    label mspt1:
                        pass
                    hide screen countdown
                    show melody closefufufu with dissolve
                    melody "Pfft, did you really think I'd give you a choice on how you want to fuck me?"
                    melody "Do you really think I'd give you a little list of options where you could pick if you want a 'handjob', a 'blowjob' or maybe sex?"
                    show melody closesadistic with dissolve
                    melody "Ahahahahahaha! Have you forgotten who I am? I'm the one that fucks you, you're merely a participant."
                    melody "I think for once, I'll choose what to do with you."
                    pass
                    melody "Hmm... What to do, what to do..."
                    $ melodysex += 1
                    if melodysex == 1:
                        melody "I'm spoiling you too much lately, so how about we settle on a simple handjob?"
                        hide melody
                        show melodyb handjob
                        show melody handjob1
                        with dissolve
                        "She wraps her hand around my shaft and starts to masturbate me."
                        "Immediately she strokes quickly, pleasuring my dick as it stiffens into erection."
                        melody "Does my flat chest and small body get you erect this fast? Hehehe, such a pervert!"
                        "Her hands wander between her legs and over her pussy lips as she teases herself too."
                        melody "Mmm, my drippy cunt is aching for something to fill it."
                        show melody handjob3 with dissolve
                        melody "Since there's nothing acceptable around, I guess I'll have to use my fingers, hehe."
                        "Her fingers sink into the folds and she fingers herself like she's mimicking the jerking motions of her other hand."
                        play ambience sex fadein 3.0
                        show melody handjob2 with dissolve
                        melody "Fahh, haaahhh, do you like watching little girls masturbate? Fucking pervert, haahh..."
                        "Her handjob speeds up, mirroring the speed of her hasty fingering. The growing sensations cause my cock to throb and drip with precum."
                        "I can feel the pressure of my orgasm welling up within me, a tightness as I get closer and closer to orgasm."
                        melody "Haahh, ahhh... Come on, cum for me..."
                        "My body quivers as pleasurable spasms overwhelm my muscles and my desire to coat this angsty mare with cum grows. And then..."
                        play sound cum
                        show melody handjob5 with cum
                        play sound cum
                        show melody handjob5 with cum
                        "My hips jerk as I spray an eruption of cum into the air, of which Melody entirely avoids as it pitifully pools on the wooden floor below."
                        play sound cum
                        show melody handjob4 with cum
                        play sound cum
                        show melody handjob4 with cum
                        "The world dissolves little by little as my mind clouds white in the euphoria of orgasm. An orgasm that Melody thoroughly jacks me off throughout, resulting in a sloppy drippy mess, even on her fingers."
                        "She quivers with pleasure enjoying her own orgasm shortly after I finish cumming."
                        stop ambience fadeout 3.0
                        scene bg melodybedroomnight
                        with dissolve
                        pause 0.3
                        show melody happy with dissolve
                        melody "If I was a real bad bitch, I'd make you clean up this cum with your tongue. But instead, I'll let you get some toilet tissue, so go."
                        menu:
                            "Use your tongue.":
                                "Like the obedient toy I am, I graciously lick the cum off my mistress's fingers before cleaning it up off the pristine wooden floors."
                                show melody surprised with dissolve
                                melody "Ooo, good boy..."
                                "While I'm cleaning the floor, Melody pushes her fluffy toes in my way as to really degrade me."
                                show melody sadistic with dissolve
                                melody "Clean these, worm."
                                "I bring one of her clean fluffy toes into my mouth and start to suckle and lick."
                                show melody neutral with dissolve
                                melody "Alright, enough, enough!"
                            "Use toilet tissue.":
                                hide melody with dissolve
                                "I slip into the bathroom and grab some tissue to wipe down Melody and the floor."
                        show melody neutral
                        with dissolve
                        stop music fadeout 7.5
                    elif melodysex == 2:
                        melody "I think your lonely worm could use a blowjob."
                        mc "Yeah, it could use a nice warm place to wriggle into."
                        show melody closeneutral with dissolve
                        melody "... Ew! That's gross man!"
                        mc "It was gonna happen eventually if you kept calling it a worm."
                        show melody closeangry with dissolve
                        melody "Eugh you're right, why would I call something I wanna suck a worm?"
                        show melody closehappy with dissolve
                        melody "Alright, you can shut up and watch."
                        hide melody
                        show melodyb handjob
                        show melody handjob2
                        with dissolve
                        "Melody's fingers coil around my shaft and begin to jerk it back and forth with a hidden enthusiasm that she'd never admit to."
                        "Her cool grip and movements quickly cause my cock to stiffen and throb."
                        "She looks at my cock with surprising admiration."
                        "I can tell deep down that she was looking forward to this."
                        melody "Hehe, I actually relaly like your cock, it's so cute."
                        melody "It's far more attractive than a horsecock."
                        show melody handjob3 with dissolve
                        "Her fingers lock around my cock and start to jack me off even faster."
                        "The rubbing fingers between her own legs also speed up, she even stifles a few moans as she gets more excited."
                        show melody handjob2 with dissolve
                        melody "Ooohh, it's throbbing! I better slow down, hehe."
                        mc "I thought you were going to suck it."
                        melody "Mm, I wanted to get you rock hard first."
                        play ambience blowjob
                        show melodyb blowjob
                        show melody blowjob1
                        with dissolve
                        "She kneels down bringing her face level with my cock and begins idly licking it with her tongue."
                        melody "Mmphh, ehehe, it's so big... *Lick*, *Lick*"
                        show melody blowjob2 with dissolve
                        "Her tongue slides around my shaft, leaving a wet sheen and sparks of pleasure in its deft licks."
                        "She's doesn't hold back at all as she twirls her tongue around the tip of my cock, licking off any precum as it drips."
                        mc "That feels--"
                        show melody blowjob4 with dissolve
                        melody "Shhh, shh… No talking."
                        mc "Mm..."
                        show melody blowjob3 with dissolve
                        melody "Yeahh, you're such a good boy."
                        "Her hand continues rubbing her pussy quickly as her long tongue swipes from my glans to the base with ease."
                        "I wonder if she had already fantasised about this before I arrived."
                        show melody blowjob1 with dissolve
                        melody "Mmmh, you’re just a sex toy for a fine lady like me… That’s right…"
                        "My cock tightens and throbs as I get closer and closer to cumming in her mouth."
                        show melody blowjob4 with dissolve
                        melody "Ohh, it’s throbbing again, does that mean you’re going to cum soon?"
                        mc "Bit faster…"
                        show melody blowjob3 with dissolve
                        melody "Hehe, okay..."
                        show melody blowjob2 with dissolve
                        "Graciously she speeds up, not sparing a second to tease me as her lips pull back and forth along my glans like a fucking motion."
                        "All whilst her tongue dances around the tip, overwhelming me with two distinctly pleasurable stimuli."
                        "With each thrust I can feel myself getting closer to my orgasm, until finally she pushes me over the edge and I release my load into her mouth."
                        play sound cum
                        show melody blowjob2 with cum
                        play sound cum
                        show melody blowjob2 with cum
                        "Until she finally pushes me to the limit, her tongue and hand cause me to start cumming into her mouth."
                        play sound cum
                        show melody blowjob2 with cum
                        play sound cum
                        show melody blowjob2 with cum
                        melody "Aahhh, ahh, aahhh..."
                        melody "Your hot sticky cum, so gross…"
                        "She's really good at blowjobs, her tongue is so long and hot."
                        show melody blowjob3 with dissolve
                        stop ambience
                        melody "You came a lot more than last time... Icky!"
                        show melody blowjob2 with dissolve
                        melody "You need to eat some sweet food, fruit or something. I heard it makes your cum taste better."
                        show melody blowjob3 with dissolve
                        melody "At least we didn't make a mess this time."
                        scene bg melodybedroomnight
                        show melody happy
                        with dissolve
                    else:
                        $ melodysex = 0
                        label melodyeveningsex:
                            pass
                        play music yanderecomplex fadein 3.0
                        melody "Alright, I'm horny, let's fuck!"
                        mc "Ohh, we're finally having sex?"
                        show melody closesadistic with dissolve
                        melody "I'll allow it, hehe. Lay down on the bed, worm!"
                        "I nod and lay down on her on bed, my half-erection limply resting on my belly."
                        melody "Well this is just pathetic, let's fix that."
                        hide melody
                        show melodyb blowjob
                        show melody blowjob2
                        with dissolve
                        "She lowers her muzzle over my cock and starts to suck and lick, within seconds my shaft engorges within her mouth until I'm fully erect and almost too big for her to handle."
                        show melody blowjob3 with dissolve
                        melody "Mmphh, damn, I phorgot how big you were."
                        play ambience blowjob
                        show melody blowjob2 with dissolve
                        "Melody spends a few moments teasing the tip of my cock with her tongue, enjoying the way it feels as it throbs in her mouth."
                        melody "Mmphh, phahh... *Schlurp*. *Lick*."
                        "Every few licks or so, she pushes it deep and fucks it with her lips. My shaft gleams with her saliva."
                        show melody blowjob1 with dissolve
                        melody "My pussy is tight you know, so I need to make sure your cock is dripping wet."
                        scene melodyb sex
                        show melody sex1
                        with dissolve
                        "With a quick movement, she pulls back and climbs on top of me, beginning to grind her cute pussy lips against my wet shaft."
                        melody "You like my tight, little pussy don't you? You're a filthy worm like that, always fantastising about it."
                        melody "Here we go..."
                        play sound cum
                        show melody sex2 with dissolve
                        "With a schlick, she lifts herself up and pushes herself down over my thick cock. Her pussy pushes back and labia indents as her tightness takes me all the way to the hilt in an impressive display."
                        melody "Oohhh... I've picked a good toy, I'm gonna get a few orgasms out of you yet."
                        show melody sex3 with dissolve
                        play ambience sex fadein 4.0
                        "The angry flat-chested mare starts to gently lift her hips up and down with far more control than last time, sensually gyrating and twisting her hips as my cock throbs against the deepest reaches of her pussy."
                        "No doubt filling her with great pleasure as indicated by the quivering in her thighs at the peak of each thrust."
                        "Even though she's moving so slowly and carefully, the incredible tightness of her pussy causes each tiny movement to yield immense pleasure."
                        "My throbbing shaft couldn't be any harder than it is now, and she knows this as she teases me."
                        show melody sex2 with dissolve
                        melody "You're quite the catch, y'know? A stallion would have cum by now."
                        melody "But you and me, we can have a lot of fun..."
                        "She sighs as she once again sinks downwards along the length of my cock, it's a surprise that she can take the entire thing so easily."
                        "I feel her hands squeeze at my legs as she grips onto me for leverage, her hips beginning to speed up their assault."
                        "Her cute breasts bounce up and down with each thrust, I can't help but bring my hands up to them and fondle them."
                        show melody sex4 with dissolve
                        "Despite that I'm a 'toy', Melody allows the action with glee, biting her lip as I toy with her sensitive nipples."
                        melody "Hahh, haahh, c-coming!"
                        "She utters with a few well-kept moans as her insides spasm, clamping down on my cock with a rhythmic tightness."
                        "Unlike last time she's paced herself incredibly well, I'm not even close to cumming yet."
                        show melody sex2 with dissolve
                        "As her orgasm passes, she still doesn't increase her speed, instead choosing to tease me even more."
                        "Unable to simply sit here and wait for her to tease me all night, I bring my hands to her hips and start to rock my hips into her, causing her to bounce up and down even faster."
                        show melody sex3 with dissolve
                        melody "Ohh! Ahhh! You cheeky bastard! Ahh, ahhhh!"
                        show melody sex2 with dissolve
                        "She cries out in girly pleasure as I take control from below, fucking her tight cunt with my rapid thrusts."
                        show melody sex4 with dissolve
                        "Not one for losing, Melody accepts the challenge and pushes back, riding my cock faster than my hips can keep up with."
                        melody "Ahhh, ahh! I am the one that fucks, b-bastaaaahhhh! Haaahh!"
                        "Her ludicrous riding speed pushes us both to an orgasmic mess within ten seconds, as she orgasms again."
                        play sound cum
                        show melody sex5 with cum
                        play sound cum
                        show melody sex5 with cum
                        "My cock erupts within, and the insane riding causes it to go almost everywhere but inside her as it splurts and squirts in all directions."
                        play sound cum
                        show melody sex5 with cum
                        play sound cum
                        show melody sex5 with cum
                        stop ambience
                        stop music fadeout 10.0
                        "After all that teasing, my orgasm is long and powerful, almost rivaling the she-demon as she fatigues and slows down to a crawl."
                        scene bg melodybedroomnight
                        show melody closesatisfied
                        with dissolve
                        "Eventually culminating in her falling on top of me, cuddling while joined at the hips."
                    stop music fadeout 4.0
                    melody "You staying overnight?"
                    menu:
                        "Stay the night":
                            show melody closehappy with dissolve
                            melody "Awesome... Your skin is really soft, so... Yeah."
                            hide melody with dissolve
                            "Melody and I snuggle together in her bed, drifting off to sleep together."
                            stop ambience fadeout 3.0
                            scene bg black with dissolve
                            pause 0.3
                            "..."
                            pause 0.3
                            play ambience ambienceday fadein 3.0
                            scene bg melodybedroom with dissolve
                            "When I wake up it's because Melody is shaking me."
                            show melody neutral with dissolve
                            melody "Come on sleepyworm, you sleep in far too late!"
                            mc "Mehh, you always wake up too early."
                            show melody happy with dissolve
                            melody "I'll make you breakfast, come on."
                            hide melody with dissolve
                            show bg boutiquekitchen with dissolve
                            "I begrudgingly go downstairs and enjoy some breakfast with Melody, Ruby hasn't even woken up yet. Makes sense because it's 7:15am."
                            show melody happy with dissolve
                            melody "I'm gonna leave for college. Feel free to shower, or whatever."
                            melody "I don't think Ruby would be that confused if you were here when she wakes up, heh."
                            mc "No worries, I'll go shower at home I think, I live close enough anyway."
                            melody "See you around champ."
                            hide melody with dissolve
                            "I finish my breakfast and drink before returning home for a shower."
                            jump altmorning
                        "Go home":
                            show melody neutral with dissolve
                            melody "Alright, I don't see why you feel like walking home at this time, but I won't judge."
                            mc "Sorry Mel, I'll see you around."
                            show melody happy with dissolve
                            melody "See ya."
                            jump sleep
                "Leave":
                    if fr == 1:
                        jump finalworldmapnight
                    jump worldmapnight
    label melodyeveningvisit1:
        $ melodyeveningvisit1 = 1
        show bg boutiquedoornight with dissolve
        "I walk up to the boutique and just as I'm about to knock on the door, a familiar she-devil appears."
        show melody neutral with dissolve
        melody "Hello stranger, what are you doing stalking about at this hour? Tryna' spy on my sister again?"
        if boutiqueafteramv == 1:
            mc "I came here to visit you actually, tried in the morning but you'd already left."
            melody "Oh yeah, I have an exam soon so I'm studying overtime."
        else:
            mc "I'm just visiting, maybe with pervy motivations, maybe not."
        mc "What are you up to anyway?"
        show melody death1 with dissolve
        melody "Just going to bury a dead body, wanna join me?"
        mc "What kind of answer is that?"
        show melody sadistic with dissolve
        melody "Ask dumb questions, get dumb answers!"
        mc "Why was my question dumb?"
        show melody neutral with dissolve
        melody "Come on man, what does it look like I'm doing?"
        mc "Going for a walk?"
        show melody happy with dissolve
        melody "Bingo! Didn't have to get up early to study for that one."
        mc "At this time?"
        show melody neutral with dissolve
        melody "It's only 7:00pm, it's not like I'm having a midlife crisis quite yet."
        melody "Come with me, Arcadia is beautiful at night."
        mc "Alright. As long as there's no funny business."
        hide melody with dissolve
        show bg arcadiasuburbsnight with dissolve
        pause 1.0
        show bg arcadiasuburbs2night with dissolve
        pause 1.0
        show bg farm2night with dissolve
        pause 1.0
        show melody neutral with dissolve
        melody "I love just wandering around, and thinking..."
        show melody satisfied with dissolve
        melody "It's very meditative"
        mc "Anything on your mind?"
        show melody neutral with dissolve
        melody "Actually, since you came along, I've been thinking about you."
        mc "I see."
        melody "Look up."
        "She says as she points into the night sky."
        play music PeaceSerenity
        hide melody with dissolve
        show bg farm6night1 with dissolve
        pause 1.0
        mc "It's beautiful."
        "Melody lays down on the grass, arms behind her head, I do the same and join her in star gazing."
        show bg farm6night2 with dissolve
        pause 3.0
        "As the air gets a little cooler, my furless body starts to get a bit of a chill. Melody takes notice and cuddles closer to me, she feels warm."
        show bg farm6night3 with dissolve
        pause 3.0
        melody "Remember when you told me you were from another world?"
        mc "Yeah?"
        melody "I'm sorry I called you crazy, and that I didn't care."
        mc "It's fine, I think that's a fairly normal response to hearing something like that."
        melody "It's true though, right? You're not from around here..."
        mc "Yeah, I'm from a world like this, but at the same time... Everything's different."
        melody "Could you tell me more about your world?"
        mc "Where to even begin..."
        show bg farm6night2 with dissolve
        "Melody and I spend maybe an hour discussing my previous life, my college, friends, and family."
        "Eventually it grows late, and the two of us return to the boutique."
        show bg farm2night with dissolve
        pause 0.3
        show bg arcadiasuburbs2night with dissolve
        pause 0.3
        show bg arcadiasuburbsnight with dissolve
        pause 0.3
        show bg boutiquedoornight with dissolve
        pause 0.3
        show melody happy with dissolve
        melody "Thanks for coming with me tonight, I really enjoyed our walk and talk."
        mc "It was my pleasure, with all the work I've been doing lately it was a nice change of pace."
        melody "Do you wanna come in? Maybe a drink?"
        mc "I'd love to."
        melody "Oh, and if you're ever visiting at night, we won't hear you knocking from upstairs. Key's under this plant pot."
        mc "Gotcha."
        scene bg boutiqueinsidenight with dissolve
        show bg boutiquekitchen with dissolve
        "Melody makes us both drinks and we go upstairs quietly, taking care not to disturb Ruby."
        show bg melodybedroomnight with dissolve
        show melody closehappy with dissolve
        melody "I always get a warm drink after my walks, especially during the colder seasons."
        mc "How cold does it get? I might need Ruby to make me something to wear if it gets any worse."
        melody "It doesn't get too bad here, only snow on the tips of the mountains. Some colder northern settlements do wear clothes to stay warm, I bet you could find something cheap in a city shop."
        show melody closefufufu with dissolve
        melody "Wouldn't want my cute wormy boy to freeze."
        mc "Well, that's very kind of you Melody."
        show melody closehappy with dissolve
        melody "Of course, I'm nice and warm. This fur is thicker than it looks, check it out!"
        "She puffs her chest out, is she encouraging me to caress her breasts? Or just her fur? Is this a test? Am I thinking too much into this?"
        menu:
            "Caress her breast fur.":
                "I bring a hand to her breast and start to ruffle my fingers through the furry texture."
                "It's fuzzy and furry, like a shetland pony."
                show melody closesadistic with dissolve
                melody "Tch, you're such a perv! You'll take any opportunity to get to molest me, clearly!"
            "Go for a modest approach in the middle of her bosom.":
                "I bring a hand to the middle of her chest, and start to ruffle my fingers through the furry texture."
                "It's fuzzy and furry, like a shetland pony."
                show melody closesadistic with dissolve
                melody "Hmph, can't you take a hint? I push my boobs out to you and somehow you miss them both! Useless!"
        stop music fadeout 10.0
        show melody closehappy with dissolve
        melody "Hehe, go on then, play with them."
        "Not one to turn down a lewd prospect, I bring both of my hands to Melody's breasts and start to fondle them."
        mc "They're so soft and squishy."
        show melody closeneutral with dissolve
        melody "You know, I've never let anyone do this to me before."
        mc "That's right, every other time we've done something sexual you've been in complete control."
        show melody closefufufu with dissolve
        melody "Hmph, don't think that'll change for a second, wormy boi!"
        mc "Do you want to do something tonight?"
        show melody closesadistic with dissolve
        melody "Mm yeah, I'm still in heat... So I'm gonna use you as a toy, got it?"
        mc "Whatever you say, 'mistress'."
        melody "Toys don't talk, so be quiet and lay down."
        "I nod and lay down on her bed, my half-erection limply resting on my belly."
        melody "Well this is just pathetic, let's fix that."
        play music yanderecomplex fadein 3.0
        hide melody
        show melodyb blowjob
        show melody blowjob1
        with dissolve
        "She lowers her muzzle over my cock and starts to suck and lick, within seconds my shaft engorges within her mouth until I'm fully erect and almost too big for her to handle."
        show melody blowjob3 with dissolve
        melody "Mmphh, damn, I forgot how big you were."
        play ambience blowjob
        show melody blowjob2 with dissolve
        "Melody spends a few moments teasing the tip of my cock with her tongue, enjoying the way it feels as it throbs in her mouth."
        melody "Mmphh, phahh... *Schlurp*. *Lick*."
        "Every few licks or so, she pushes it deep and fucks it with her lips. My shaft gleams with her saliva."
        show melody blowjob4 with dissolve
        melody "My pussy is tight you know, so I need to make sure your cock is dripping wet."
        show melodyb sex
        show melody sex1
        with dissolve
        "With a quick movement, she pulls back and climbs on top of me, beginning to grind her cute pussy lips against my wet shaft."
        melody "You like my tight, little pussy don't you? You're a filthy worm like that, always fantasising about it."
        melody "Here we go..."
        play sound cum
        show melody sex2 with dissolve
        "With a schlick, she lifts herself up and pushes herself down over my thick cock. Her pussy pushes back and labia indents as her tightness takes me all the way to the hilt in an impressive display."
        melody "Oohhh... I've picked a good toy, I'm gonna get a few orgasms out of you yet."
        show melody sex3 with dissolve
        play ambience sex fadein 4.0
        "The angry flat-chested mare starts to gently lift her hips up and down with far more control than last time, sensually gyrating and twisting her hips as my cock throbs against the deepest reaches of her pussy."
        "No doubt filling her with great pleasure, as indicated by the quivering in her thighs at the peak of each thrust."
        "Even though she's moving so slowly and carefully, the incredible tightness of her pussy causes each tiny movement to yield immense pleasure."
        "My throbbing shaft couldn't be any harder than it is now, and she knows this as she teases me."
        show melody sex2 with dissolve
        melody "You're quite the catch, y'know? A stallion would have cum by now."
        melody "But you and me, we can have a lot of fun..."
        "She sighs as she once again sinks downwards along the length of my cock, it's a surprise that she can take the entire thing so easily."
        "I feel her hands squeeze at my legs as she grips onto me for leverage, her hips beginning to speed up their assault."
        "Her cute breasts bounce up and down with each thrust, I can't help but bring my hands up to them and fondle them."
        show melody sex4 with dissolve
        "Despite the fact that I'm a 'toy', Melody allows the action with glee, biting her lip as I toy with her sensitive nipples."
        melody "Hahh, haahh, c-coming!"
        "She utters with a few well-kept moans as her insides spasm, clamping down on my cock with a rhythmic tightness."
        "Unlike last time she's paced herself incredibly well, I'm not even close to cumming yet."
        show melody sex2 with dissolve
        "As her orgasm passes, she still doesn't increase her speed, instead choosing to tease me even more."
        "Unable to simply sit here and wait for her to tease me all night, I bring my hands to her waist and start to rock my hips into her, causing her to bounce up and down even faster."
        show melody sex3 with dissolve
        melody "Ohh! Ahhh! You cheeky bastard! Ahh, ahhhh!"
        show melody sex2 with dissolve
        "She cries out in girly pleasure as I take control from below, fucking her tight cunt with my rapid thrusts."
        show melody sex4 with dissolve
        "Not one for losing, Melody accepts the challenge and pushes back, riding my cock faster than my hips can keep up with."
        melody "Ahhh, ahh! I am the one that fucks, b-bastaaaahhhh! Haaahh!"
        "Her ludicrous riding speed pushes us both to an orgasmic mess within ten seconds, as she orgasms again."
        play sound cum
        show melody sex5 with cum
        play sound cum
        show melody sex5 with cum
        "My cock erupts within, and the insane riding causes it to go almost everywhere but inside her as it splurts and squirts in all directions."
        play sound cum
        show melody sex5 with cum
        play sound cum
        show melody sex5 with cum
        stop ambience
        stop music fadeout 10.0
        "After all that teasing, my orgasm is long and powerful, almost rivaling the she-demon as she fatigues and slows down to a crawl."
        hide melodyb
        hide melody
        show melody closesatisfied
        with dissolve
        "Eventually culminating in her falling on top of me, cuddling while joined at the hips."
        "I say cuddling, but it's more just like she's died and fallen limp on top of me, and I have a single hand on her back so she doesn't fall."
        "It takes a few seconds, but her soft furry hands wrap around me and she snuggles her cheek into my chest."
        "We snuggle happily while ignoring the hot, wet mess left between us."
        scene bg black with dissolve
        "..."
        play ambience ambienceday
        scene bg melodybedroom with dissolve
        mc "Mmph? Oh."
        melody "Morning sleepyhead."
        show melody neutral with dissolve
        "I turn around to see Melody drying herself with a towel, post-shower."
        show melody happy with dissolve
        melody "Can't say I anticipated you staying the night, but it's no harm. It was nice cuddling with you."
        melody "You gonna join me for breakfast?"
        mc "Sure thing."
        hide melody with dissolve
        show bg boutiquekitchen with dissolve
        "I go downstairs and enjoy some breakfast with Melody, Ruby hasn't even woken up yet. Makes sense because it's 7:15am."
        show melody happy with dissolve
        melody "I'm gonna leave for college. Feel free to shower, or whatever."
        melody "I don't think Ruby would be that confused if you were here when she wakes up, heh."
        mc "No worries, I'll go shower at home I think, I live close enough anyway."
        melody "See you around, champ."
        hide melody with dissolve
        "I finish my breakfast and drink before returning home for a shower."
        jump altmorning
    label rubylingeriesex:
        scene bg black with d
        "You unlocked a secret scene! Requirements met: Work with Ruby after finishing her route. 50%% chance."
        "During work…"
        scene bg boutiqueinside with d
        show ruby happy with d
        ruby "Hey, darling. Could you help me with a particular task? I'll need you to come to my room."
        mc "What about the shop floor?"
        ruby "I’ll put a sign on the door saying that we’re closed for lunch."
        mc "Alright, how can I help?"
        scene bg black with dissolve
        "…"
        stop ambience fadeout 3.0
        play music sex1 fadein 3.0
        scene rubyb doggystyle
        show ruby doggystyle1
        with d
        ruby "You see, darling? Quite the problem indeed, I can’t concentrate at all when I’m this aroused."
        mc "Hmm, yes. I believe I do see the problem."
        ruby "Could you pound this frustration out of me, perhaps?"
        mc "Will I get paid extra for this? Haha."
        ruby "My, my... Do I look like a prostitute to you, [playername]?"
        mc "Oh, no, no. I didn’t mean to imply that."
        ruby "Hehe, I could roleplay that if you’d like, debasing myself is arousing."
        ruby "Perhaps I could throw you another five monies as a tip for an excellent job."
        $ monies += 5
        "You got 5 monies!"
        mc "Wait, that makes {i}me{/i} the prostitute."
        ruby "Ohh, so it does!"
        mc "Well, let’s get on with the plot."
        "Ruby’s exquisite ass is presented to me as she waits on all fours. I have to spend a moment admiring it."
        "I even have to appreciate her hair; it looks exquisite today."
        ruby "No need to window shop, darling, I’m all yours."
        "Taking the hint, I stand at the edge of the bed, and pull her in to me, so her butt is level with my hips."
        "At this point my cock is basically already erect. That’s just the kind of effect Ruby has on me."
        "I’ll just check to see if she’s ready to take my cock first. With a finger I slide it from the tip of her vulva to the clit, collecting a generous amount of lubricants as I do."
        mc "You’re really wet…"
        ruby "Did you not catch me squirming earlier? Haha, a lady has her needs too."
        mc "No need for foreplay, then."
        play sound cum
        show ruby doggystyle2 with d
        "I lift my cock up and jack it off until I’m perfectly solid. Then, gently easing between the plush lips of her labia, I push forward into her delicate folds and sink into my lover."
        "She takes it like a champ, cooing at the sensation of being filled up."
        ruby "Ahhhahhh. Getting filled at the start always feels amazing."
        "And sinking deeply inside of her for the first time in a while also feels amazing."
        play ambience sex fadein 3.0
        "Pulling back, I prepare to thrust back inside. Beginning the session with a pace pleasant to the both of us."
        "Ruby’s contracting insides purposely tease and squeeze my member. She’s almost a little too good at this."
        "The view from up here is amazing, Ruby’s cute bubble butt is always a marvel to witness in action. She doesn’t simply let herself be fucked, she wiggles her hips back and forth to meet mine, making each thrust that much better."
        ruby "Aahhh, ahhh… I love your thick cock, darling… Mmphh, tighten it for me, ahhh…"
        "I tighten my cock slightly at her request, and in turn she tightens her pussy slightly."
        ruby "Mmphhh, so fucking good, haah… hahh…"
        mc "I didn’t realize your wonderful pussy could get any tighter."
        ruby "Nnnh, that sounds like a challenge."
        "Now rhythmically clenching around my cock, Ruby does her best to milk me dry as I pound into her sloppy wet puss."
        "At this rate, it wouldn’t take either of us long to come. But while Ruby does her best to get me off, I still have a trick up my sleeve."
        "With one hand clenching tightly around her hips for leverage, I bring my other between her legs and start to rub her clit."
        "Now she’s really starting to moan. Her eyes close tight and her fingers clench the bedsheets in response to the spike in pleasure."
        ruby "Ahhh, aaahhh… Wh-What a gentleman, ahhaah… Ahhhhh, you’re gonna make me come, so quickly!"
        "Ruby seems easier to get off than most girls, especially by rubbing her clit. Within only thirty seconds orgasmic pleasure seems to completely consume her body."
        "My own orgasm is creeping ever closer. As I continue to pound Ruby, at an accelerating pace, I can feel the urge to cum rising."
        play sound cum
        show ruby doggystyle3 with cum
        play sound cum
        show ruby doggystyle3 with cum
        "And almost before I know it, her tight squeezing cunt robs my orgasm from me and my cum spills freely into her."
        play sound cum
        show ruby doggystyle3 with cum
        play sound cum
        show ruby doggystyle3 with cum
        stop music fadeout 5.0
        stop ambience fadeout 5.0
        "Several loads of ejaculate seep deeply into my lover. Enough to overflow and spill down her white fluffy thighs."
        ruby "Haahh, yeesss… That’s exactly what I needed."
        show ruby doggystyle4 with d
        "Ruby crawls ahead slightly, causing my cock to slip out. She gives me a good view of her cum soaked pussy."
        ruby "Look at all this mess you made… All that cum… Was my pussy really that good? Hehe."
        mc "You sounded a bit like your sister just then."
        ruby "Oh! I suppose I did, hehe. I still have a lot of her in me."
        mc "You also have a lot of me in you, literally."
        ruby "Hah, you’re so bad."
        scene black with d
        "Ruby gets off the bed and stands beside me, giving me a quick kiss on the cheek."
        ruby "Going to clean up. Can you open the shop back up? I’ll be down in a second."
        mc "No problem."
        if crystalballactivated == 1:
            jump cbmenu
        "…"
        $ secretsunlocked += 1
        "After work..."
        jump rubyafternoon
