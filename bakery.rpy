label bakery:
    $ bakeryvisits += 1
    if bakeryvisits == 1:
        $ bakeryvisit1 = 1
        $ monies += 25
        jump bakeryvisit1
    elif bakeryvisits == 2:
        $ bakeryvisit2 = 1
        $ monies += 25
        jump bakeryvisit2
    else:
        jump bakeryday
    label bakeryvisit1:
        "The bakery will be fun to work at, if I’m lucky I might be able to lick the spoons! Actually, that’s a terrible idea, this is a professional establishment, not my grandma’s kitchen."
        show bg bakerydoor with dissolve
        "When I arrive at the bakery I move to give the door a knock but it immediately bursts open!"
        play music cream1
        show cream neutral with dissolve
        cream "Oh mi gosh! [playername]! What are you doing out here? Come right in! Oh I'm so excited!"
        mc "???"
        show cream happy with dissolve
        cream "Come on [playername]! You're the main guest of the party! I've been waiting for you."
        scene bg bakery with dissolve
        "I take a step in; but this isn't exactly a party, the room is empty!"
        show cream laughing with dissolve
        cream "Okay, so, we need a guest list, we need decorations, streamers, lots of cakes, maybe a cannon!"
        cream "Ohh, and I'll make my super alcoholic punch, it'll be so much fun!"
        mc "Pardon me, but what's your name? And how do you know mine?"
        show cream happy with dissolve
        cream "Can't you read it? I'm called Cream! And I know all about you, because uhm, Penny's note of course!"
        if days > 5:
            "That’s odd… There were other girls that didn’t know my name."
        mc "Riiight, so you should know that I'm here to work?"
        show cream neutral with dissolve
        cream "Of course! I've been thinking about it and planning for [days] days!"
        if days > 15:
            show cream sad with dissolve
            cream "You took a long time to come and visit me... I hope you don't dislike me, [playername]!"
            mc "Ahh, I'm sorry... I got caught up with-"
            show cream althappy with dissolve
            cream "With everyone else? Sure... But that's perfect!"
        cream "Because we're going to organise a huge party and invite all your friends!"
        mc "Okay, can we take a few steps back? You seem awfully familiar with me, but I've just met you."
        "This girl also seems remarkably unphased by the fact I’m not a pony, I think that's a first among everyone I've met so far."
        show cream laughing with dissolve
        cream "Oh right! Okay, let's start from the beginning!"
        show cream embarrassed with dissolve
        cream "Woah! What the heck are you? A furless pony?"
        mc "Huh? Furless pony? I guess you could call me that."
        show cream neutral with dissolve
        cream "Haha, you don’t wanna explain the full story? You're probably used to hearing the same charade over and over!"
        cream "Don’t worry about it, my empathy skill is overclocked!"
        cream "I could see it all over your face, ‘when is she going to point out that I’m not a pony’."
        cream "But when you party Cream style, appearances don’t matter!"
        cream "And that includes in bed as well! I wouldn't mind if we put some whipped cream on these buns! If you know what I mean, hehe."
        show cream happy with dissolve
        mc "I think I know what you mean, so let's get to baking, then?"
        show cream horny with dissolve
        cream "No, it was an innuendo! I meant cum, on my ass, [playername]."
        mc "You're moving a bit quick, don’t you think?"
        show cream laughing with dissolve
        cream "Oh, you’re right, I should wait at least until the second act of this day."
        show cream happy with dissolve
        cream "Ah, who am I kidding? We’ll probably have sex within ten to twenty minutes!"
        mc "I have to say, you’re one of the most sexually forward mares I’ve met in the suburbs."
        show cream althappy with dissolve
        cream "And that’s saying a lot! What do you say, do you like me?"
        mc "Hm, maybe… You are quite cute."
        show cream horny with dissolve
        cream "Ooh, I’d let you sink your teeth into me, like a juicy peach."
        cream "Squelch, as the warm juice runs down your face."
        mc "Okay, okay, I get it! Thing is, I’m not here just for sex, or a party."
        show cream sad with dissolve
        cream "I mean you want sex, don’t you? That’s why you’re here?"
        mc "You must be confused, Penelope sent me here to work at the bakery, I’m not some kind of sex worker."
        mc "I thought you knew that."
        show cream embarrassed with dissolve
        cream "Pffft… I-I thought the note was saying you and I were going to work together to have a big party with all the other people on that list!"
        cream "So, you’re not here to party? And you’re not here for sex? Totally lame…"
        cream "Well, I know! We’re going to bake some delicious cakes today, that’s just what we need to get the party going."
        mc "I-uh, we're still doing that party thing? Alright, let’s bake some cakes then."
        scene bg bakerykitchen with dissolve
        "I follow her into the kitchen, I can’t avert my eyes as her booty sways back and forth."
        "Ponies are always naked, but I’m fairly sure her tail isn’t supposed to sway that much. Is she trying to tease me?"
        mc "Talk me through today's plan then, we're going to be running the shop, so what's this about a 'party'?"
        show cream happy with dissolve
        cream "I'm going to send mail to everyone, and tell them to come here tonight! It's gonna be awesome!"
        cream "And yes! We'll be running the store like normal until closing time."
        mc "Alright, that sounds like it could be fun. Let's get on with the baking then."
        show cream smug with dissolve
        cream "You oughta loosen up a bit [playername], how about some music!"
        play music inlove
        "The white pony puts on some party songs; the tracks remind me of the songs that would play at my middle school discos."
        "This girl is nuts; I hope she hasn’t just broken into this building and is pretending to live here or something."
        show cream neutral with dissolve
        cream "It’s not easy running such a great bakery by myself! Watch and learn..."
        "She quietly hums to the lyrics of the music as she preheats an oven, gets ingredients out and starts flicking through a recipe book with an oddly compelling prowess. She's definitely not a squatter."
        "Meanwhile I’m just standing here like a wet noodle watching her do all the work."
        "Did we just start working? Am I being paid now? I'm not doing anything."

        menu:
            "What if a customer comes in while we’re back here?":
                show cream happy with dissolve
                cream "No worries! We have no cakes to sell yet, we need to bake them first!"
                "The shop did seem really empty when I walked in. There was nothing in the display cases."
                mc "Why aren’t the cakes already baked? Seems like a strange system."
                show cream laughing with dissolve
                cream "You’re so silly [playername]! Have you ever gotten a cake, and then the day after it was stale?"
                show cream happy with dissolve
                cream "Freshness is vital! So we bake and sell on the same-day here!"
                mc "Well damn, I’m glad I came to help you out then, it must be difficult trying to bake and sell at the same time."
                show cream neutral with dissolve
                cream "Yeah, it can be a little tough, that's why I'm starting the first few batches preemptively."
                cream "Here, you can make some too. Check out this page on how to make cupcakes, easy peasy lemon squeezy, even someone without any experience could do it."
            "Do you need any help?":
                show cream happy with dissolve
                cream "Of course, I’ll make the more advanced cakes and you can make these cute little cupcakes!"
                cream "If you follow this recipe, you should be able to make them even without experience! Easy peasy lemon squeezy!"

        scene bg bakerykitchen with dissolve
        "Lemon cupcakes… Alright, step one..."
        "I make some progress on cupcakes, mixing the ingredients until the mixture is softened. Then I divide the result into muffin tins and put it in the oven."
        "Cream also puts something in the oven, it seems she’s making a larger cake out of two parts."
        mc "That was so easy, why don’t I do this more often?"
        show cream neutral with dissolve
        cream "Only takes 20 minutes to make some scrumptious cupcakes, sometimes I have them for breakfast!"
        mc "Can’t say I’ve ever tried that, but it reminds me of pancakes for breakfast, delicious."
        show cream happy with dissolve
        cream "I loooove pancakes! I love drizzling syrup all over them, mmm…"
        show cream sad with dissolve
        cream "Just like how I want you to drizzle your...- ah phooey, this sexual innuendo sucks."
        mc "I think you were onto something when you mentioned cream and buns."
        show cream laughing with dissolve
        cream "I can’t be too repetitive with my flirts, even if repetitive motion is how I plan to get you off."
        mc "That’s a good one. How about something to do with creampies?"
        show cream embarrassed with dissolve
        cream "I was saving the creampie one, you devil!"

        menu:
            "You seem to have a soft spot for me, anything about me in particular that you like?":
                show cream happy with dissolve
                cream "Hehe, how could I not? That’s the entire reason I’m here!"
                mc "You’re here to bake cakes and flirt with me?"
                show cream neutral with dissolve
                cream "Nahhh, well, kinda!"
                cream "I’m here to bake cakes, party and fuck."
                cream "And the cakes are all in the oven…"
            "Tell me more about those repetitive motions.":
                show cream horny with dissolve
                cream "You knoooow, I like to bounce, up and down, in and out."
                mc "I’m not sure I do know, maybe you should be more specific."
                show cream neutral with dissolve
                cream "More specific? Awh, you’re either naïve or you’re flirting with me!"
                "She steps closer and whispers into my ear."
                show cream closehorny with dissolve
                cream "The lips of my pussy wrapped around your cock, sliding back and forth."

        "Conclusion: She wants to fuck."
        "She’s not pulling any punches, she’s horny and knows what she wants."
        "I gotta say, a part of me respects her no nonsense approach, I’m growing more and more tempted to just let it happen."
        mc "Heat must be getting to you right?"
        show cream happy with dissolve
        cream "Getting to me? Nah, these are party vibes my dude, aren’t you feeling my wavelength?"
        mc "Your wav-"
        show cream laughing with dissolve
        cream "-Come on! Tune in with me!"
        mc "Ahhh, was that another innuendo?"
        show cream happy with dissolve
        cream "Gosh, I don’t even know anymore!"

        menu:
            "You seem really sexually experienced, judging by your confidence.":
                show cream neutral with dissolve
                cream "I wish! I’ve only been with a few girls these past few months."
                cream "Waiting for a good cream filling, if you catch my gist."
                mc "Not enough men to go around?"
                show cream laughing with dissolve
                cream "Not nearly enough, how am I going to live out my gang bang fantasies like this?"
                "She sways her butt in my direction and winks."
            "Are you like this with everyone?":
                show cream neutral with dissolve
                cream "Only with the cute ones!"
                cream "I can see that glimmer in your eye, it’s telling me you want it."
                mc "How can you be so sure?"
                show cream althappy with dissolve
                cream "You wouldn’t be here if you didn’t want it!"
                mc "So you’re saying I wouldn’t be working with a girl if I didn’t want sex? That doesn’t make sense."
                show cream laughing with dissolve
                cream "Am I wrong though?"
                "I guess she’s right, I am here for sex, damnit!"
                show cream happy with dissolve
                cream "Hehe, I thought so."
                "She blows me a kiss and checks on the progress of the cakes."
        label creamquickie:
            pass
        mc "Oh! I think the first batch is done."
        show cream embarrassed with dissolve
        cream "Ohh right! That sexual skirmish nearly made me forget, let’s see here…"
        scene bg bakerykitchen2 with dissolve
        show cream ass1 with dissolve
        "She bends over and peeks through the window of the oven to check."
        "I can’t help but check out her ass while she does. This girl is getting to me, she’s starting to turn me on."
        "Wow, her pussy is really wet..."
        "Her flirting is so over the top it seems comical, yet I’m completely helpless to her erotic advances."
        show cream ass2 with dissolve
        cream "You’re right where I want you!"
        mc "Huh?"
        cream "Yeah, you’re next to the oven glove, could you pass it?"
        scene bg bakerykitchen with dissolve
        "I pass her the oven glove and she takes out the cupcakes I mixed up earlier, they’ve turned a golden brown."
        scene bg bakerykitchen2 with dissolve
        show cream ass2 with dissolve
        "And then, she bends over again!"
        cream "I saw you staring! Do you like what you see?"
        menu:
            "Yeah, it's a nice butt":
                cream "Mmm, thank you cutie!"
            "Maybe, what's it to you?":
                cream "I've got something you like, and I think you've got something I like, hehehe!"
            "No way!":
                cream "Hmph, there's no need to play hard to get!"
        cream "You gonna window shop, or make me yours big boy?"
        mc "R-Right now?"
        cream "The cakes need to cool, so how about we cool off too with a quickie? Heheh!"
        menu:
            "Fuck her":
                $ creamfuckedday1 = 1
                stop music fadeout 3.0
                "Just as the music track reaches its end and leaves us in silence, I position myself behind Cream's bountiful rear."
                "It's so curvacious and thick, it may be the most impressive rear I've seen in all of Arcadia!"
                play music sex1 fadein 3.0
                "As Cream leans on the counter, quivering in anticipation, she coos and pushes back as I align the tip of my erection with her wet, eager pussy."
                cream "Mmm, such a big and thick cock, just the way I like it..."
                play sound cum
                show cream ass3 with dissolve
                "I push forward, aided by Cream pushing back, sliding my long cock into the soft folds of her pussy."
                "She squeals with delight as I sink deeper, and those squeals gently shift into moans, as her pussy contracts and squeezes around the girth of my shaft."
                play ambience sex
                "I begin to fuck her. Her pussy continues to tighten around my member, but thanks to how absurdly wet the heated mare is, my cock becomes slick with her juices and easily slides back and forth."
                cream "Aahhh! If I knew your cock was going to feel this good, I would've fucked you even sooner! Hehehaaahhahaaa!"
                show cream ass4 with dissolve
                "The sweet, sickly aroma of cakes and love sifts through the air, whilst her moans reverberate against the wooden walls of the kitchen; my senses are almost overwhelmed."
                "Her moans grow deeper and more passionate, correlating to the intensity of my thrusts. Her movements become increasingly intoxicated with pleasure as her hips begin to rock back against me with each thrust."
                cream "Aaahh, ahh! Hehehe, I'm so glad you- ahhh, decided to fuck me, [playername]! Ahhh! Isn't this so much fun? Aahhhaahh!"
                "Before long we're both fucking each other equally, her ass connecting to my pelvis with a satisfying thwap, as she forces my throbbing cock deeper into her tight cunt."
                "Gripping tightly onto her ass as leverage, I drive into her faster as the pressure of my orgasm rises."
                cream "Ahh, I-I'm gonna come! Gonna come so hard! Fill my pussy, [playername]!"
                play sound cum
                show cream ass5 with cum
                play sound cum
                show cream ass5 with cum
                "In lustful unison we both climax. My hot seed immediately gushing inside her, squelching and mixing with her own copious quantity of love-juice."
                play sound cum
                show cream ass5 with cum
                play sound cum
                show cream ass5 with cum
                "With orgasmic moans, Cream's pussy clenches around my member tightly, her pussy milking my cock for every ounce of cum."
                stop ambience fadeout 3.0
                stop music fadeout 3.0
                show cream ass6 with dissolve
                "Exhausted from the spontaneous and frantic session of sex, I pull out my member and let the cum ooze down her white thighs."
                cream "O-Oh my goody goodness, we had such a quick and naughty quickie! It feels exhilarating, doesn't it? Hehehe!"
                mc "Heh, yeah that was pretty fun. Here's a paper towel, for the uhm, cum."
                show bg bakerykitchen with dissolve
                show cream cumlaughing with dissolve
                cream "Thank you! Hygiene is very important in a kitchen, so let's make sure we wash our hands before we touch anything else!"
            "Not right now":
                show bg bakerykitchen
                show cream sad
                with dissolve
                cream "Fiiine, let's start icing the cakes... Although I really wish you iced me instead..."
        if crystalballactivated == 1:
            jump cbmenu
        scene bg black with dissolve
        "Ten minutes and some cake icing later!"
        stop music fadeout 3.0
        scene bg bakerykitchen with dissolve
        show cream happy with dissolve
        play music day2 fadein 3.0
        cream "Mmm they look delicious! These are going to be super popular with the customers! You did amazing on your first batch."
        mc "I’m pretty proud, my first ever batch of cupcakes."
        show cream laughing with dissolve
        cream "Yup, your ability to follow a simple list of instructions is unrivalled [playername], that’ll take you a long way in any career."
        "Just as I had finished icing my cupcakes, she finished jamming and creaming a sponge cake. Just like that, we have our first batch done."
        show cream neutral with dissolve
        cream "Alright, what’s next… Oh, more cakes!"
        mc "Didn’t see that one coming."
        scene bg black with dissolve
        "I don’t know if I can spend another seven and a half hours doing this with Cream flirting with me constantly."
        scene bg bakery with dissolve
        "Luckily, I don’t have to, she makes me man the shop while she focuses on baking."
        "There's plenty of downtime since she can bake faster than we sell, so we get plenty of opportunities to talk. I can see how she could run this place by herself."
        "As we fairly frequently get a chance to chat, I took the time to tell her my backstory, and I learn a bit more about her too."
        "Cream was no less strange than this morning, but her scattered brain seems to have come together for the moment at least."
        "We spend the rest of the day sorting out the bakery, selling cakes, and baking more. As the sun starts to set, Cream and I start to close up the shop and talk about the party she wants to have tonight."
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        show cream happy with dissolve
        cream "Okay, I've sent out the invitations for the party! It's going to be so much fun!"
        mc "Oh yeah? While it feels somewhat spontaneous, I'm rather excited. It'll be my first proper party since arriving in Arcadia."
        show cream laughing with dissolve
        cream "And you picked the best possible host!"
        play sound ping
        "*Ping*!"
        show cream neutral with dissolve
        cream "Ohh, the final batch of cakes are done! These ones will be just for party guests! Come into the kitchen and I'll pay you too."
        show bg bakerykitchen with dissolve
        cream "You've been such a great partner today [playername], here's your pay, 25 monies! A valuable resource for you, I'm sure."
        if livingwithbutters == 1:
            cream "The invites are for 8:00pm, and a few of the girlies have already RSVP'd by magic mail. Moxie, Butters, Ruby and more said they're coming!"
        else:
            cream "The invites are for 8:00pm, and a few of the girlies have already RSVP'd by magic mail. Moxie, Riku, Ruby and more said they're coming!"
        cream "So I have three hours to prepare! Are you gonna stay and help me? I'll make you a delicious dinner!"
        if livingwithbutters == 1:
            mc "Yeah, no sense in going back home if I'll just be back anyway."
        else:
            mc "Yeah, no sense in going back to Moxie's place if she has been invited anyway."
        show cream happy with dissolve
        cream "Perfect! Ooohh, this is gonna be so much fun!"
        cream "Well, let's begin transforming this bakery!"
        scene bg black with dissolve
        play music inpeace fadein 3.0
        "After enjoying Cream's fantastic cooking, we get busy turning the shop of the bakery into a bombastic party setup. She keeps tons of party supplies in a closet and already knows where she wants everything."
        show bg bakeryparty1 with dissolve
        "She's actually surprisingly strict about how she wants the party setup, which is in direct contrast to how relaxed she is about baking."
        "Regardless, we furnish the room with remarkable efficiency. We setup the tables, we prepare the drinks, we have napkins, and drinkware."
        show bg bakeryparty2 with dissolve
        "She blows up some balloons, we have some snacks and cakes prepared, even little things like the bins getting emptied."
        "This girl {i}really{/i} knows how to party."
        "After only an hour, we manage to finish up, giving us yet more time to kill."
        show cream laughing with dissolve
        cream "Phew, gosh! We've been doing so much work today, I'm kinda exhausted [playername]!"
        if farmvisit1 == 1:
            mc "I can tell that you've never worked with Honeycrisp."
            show cream smug with dissolve
            cream "Awh sheesh, if you've worked with her, you can do anything."
            mc "Still, the bakery has gotten hot and stuff, I could use some fresh air."
        else:
            mc "Yeah, I could use a break, maybe some fresh air."
        show cream neutral with dissolve
        cream "Ohh, good idea! How about we take a walk in the nearby park?"
        mc "At this time? It crept up on us, but it's already night."
        show cream happy with dissolve
        cream "Yeah but it's such a lovely evening, and  since you’re an alien creature I want to show you as much of the beauty here as possible."
        mc "You don’t have to worry about me, I crash landed, so I’m stuck in the beauty."
        show cream laughing with dissolve
        cream "It’s my job to make being stuck here as entertaining, fun, and fantabulous as possible!"
        mc "Alright. We've got time to kill, and I still need to walk off the dinner you cooked for me."
        stop music fadeout 3.0
        scene bg black with dissolve
        play ambience ambiencenight
        show bg farm6night1 with dissolve
        play music uhoh fadein 30.0
        "The two of us move to a grassy area and we sit down under the starry night sky."
        mc "It gets dark fast."
        show cream closehappy with dissolve:
            xpos 0
            ypos 50
        cream "I like that though, because the night is so beautiful... I could stare forever, counting all the little stars..."
        mc "If you were to count every lone star, you may be stuck here forever."
        show cream closealthappy with dissolve
        cream "Lone stars? But there are so many of them, they’re all friends."
        mc "They’re further away than you think, and some of them are just glimpses of the past because the stars are lightyears away. Some of them might even be dead."
        show cream closelaughing with dissolve
        cream "Wow, you really are an alien, hehe."
        mc "If ‘alien’ is paying attention in school, sure!"
        show cream closesmug with dissolve
        cream "I never cared much for academics, my focus in life was to always have as much fun as possible."
        mc "And counting stars is your idea of fun? It’d take an eternity."
        show cream closeneutral with dissolve
        cream "What if I lived forever though? I could do it then."
        mc "Immortality? That could be pretty fun, but I'd probably get bored if I used all that time to count stars."
        show cream closesatisfied with dissolve
        cream "Yeah, you’re right… If you live forever, it would get immeasurably boring."
        cream "You’ll outlive your friends, and your girlfriend, and you’ll probably go crazy."
        mc "I think if I was in that situation it would be morbid at first, but eventually you’ll adapt and just seek new and wonderful experiences."
        show cream closeneutral with dissolve
        cream "And you’ll outlive those experiences, your new friends and your new girlfriend."
        mc "Right, I guess… It would just be a cycle, as long as you don’t go insane."
        show cream closesad with dissolve
        cream "You would definitely change though, you’d become jaded."
        cream "Another group of friends, another girlfriend, outlived. Then your mind starts ticking."
        cream "Eventually you’ll grow sick and tired of this happy lifestyle, you’ll kill your girlfriend, your friends and you’ll try to finally end that eternal life of yours."
        cream "But, the sun will still rise, if the sun still exists at your arbitrary point of eternity."
        mc "I get what you’re saying, but I don’t think I’m capable of that, especially people I love."
        show cream closeneutral with dissolve
        cream "Ever play a video game that gives you freedom?"
        cream "Sometimes you ask yourself, what if I stole from this person? What if I killed this person?"
        cream "The friends and girlfriend you outlive, eventually you’ll kill them, just to see what it’s like."
        mc "I mean… I’d never do that, right? You can’t act like that’s inevitable just because I’ve been mean to a character in a game that called me a milk-drinker."
        show cream closesatisfied with dissolve
        cream "The nature of immortality implies an infinite existence, no one could really say what that experience entails."
        mc "I’d like to think there’s enough experience and stimulation in the world to keep me mentally healthy."
        show cream closeneutral with dissolve
        cream "Even if you could live forever, you wouldn’t just lose your friends, family and loved ones, humanity will die out eventually."
        mc "Ahh… Humanity would die out, but I’d still be immortal, everyone would die, then I’d go insane, is what you’re getting at?"
        show cream closesad with dissolve
        cream "More than you know, you’ll be living in perpetuity, an inky blackness. First humanity will die out, then your planet earth, and then the heat death of the universe. You’ll get to see if that’s really how it’ll end, once you do, you can come back and tell me."
        mc "… That’s terrifying, I don’t like to think about it."
        show cream closeneutral with dissolve
        cream "Well, how long is an hour to you? It can be quite a long time with no stimulation."
        cream "Now imagine that inky blackness as you drift through space for an hour, then a day, then a year…"
        cream "A million years, a billion years, a trillion years…"
        cream "Even then, you wouldn’t die, you’re still at the beginning of your eternity."
        mc "Eugh I get it, I wouldn’t just go insane, my mind would be completely shattered."
        show cream closesatisfied with dissolve
        cream "In a sense, immortality like that is an infinite hell."
        mc "Immortality is a curse then. I just want to live a happy life in the fleeting time I have on this speck of dust."
        show cream closeneutral with dissolve
        cream "A curse? Interesting… You were so eager to call going insane a curse."
        cream "But did you consider what it’s like to lose your mind?"
        mc "I can’t say I’ve put much thought into it."
        show cream closealthappy with dissolve
        cream "How do you know you haven’t already lost it?"
        mc "I suppose I don’t have a definite answer for that, I am living in a brand-new world full of talking ponies."
        show cream closeneutral with dissolve
        cream "Maybe you’ve already gone insane, and you’ve lost your mind."
        cream "Drifting through deep space for all infinity? One great big fantastic party in your head!"
        mc "You’ve managed to put a positive spin on it, impressive. You really are a bundle of joy."
        mc "I think you’re banking on a lot hoping that your mind goes insane in a positive way though."
        show cream closesatisfied with dissolve
        cream "Isn’t that what insanity is for? When reality is so abhorrent that the brain needs to delude itself into a better world?"
        cream "A world where you’ll have a great girlfriend, friends, and a fun life."
        mc "I’ve heard of that before, to be stuck in the delusions of your imagination forever."
        "This idea still seems too crazy to me, Cream is a little daydreamy, but I can’t relate to this at all."
        show cream closeneutral with dissolve
        cream "A world where you meet a blue pony, who loves you, and you make friends with more ponies. What a fun life."
        mc "Well… I’m pretty sure I’m not insane."
        show cream closealthappy with dissolve
        cream "It’s okay, my point is that it doesn’t matter if you are."
        cream "Your brain will keep you looping in your beautiful fantasy for a quadrillion years, and even after all that, you still have an infinite eternity left."
        cream "To you, it’ll all pass in the blink of an eye."
        mc "I’m losing track of what you’re saying, what do you mean?"
        show cream closeneutral with dissolve
        cream "The insanity and morbid nature of infinite existence is conceptually impossible, due to the idea of being alive for an infinite amount of time."
        cream "The key word is ‘infinite,’ it means an immortal being cannot exist alongside time but must exist outside of it."
        cream "At a certain point there will be no difference between 10 seconds and 100 years."
        cream "10 seconds and 100 trillion years."
        cream "To you, the immortal being, the 10 second lifespan of a baby is the same blip in the universe as the 100-year lifespan of the old woman. One and the same relatively."
        mc "I don’t understand, even if I’m a trillion years old I still experience every second the same."
        show cream closelaughing with dissolve
        cream "Nah nah nah, party boy, I’m not thinking literally, I’m thinking conceptually."
        mc "Yeah, but…"
        mc "You were just joking when you said I might be insane, right?"
        show cream closehappy with dissolve
        stop music fadeout 10.0
        cream "Of couuuurse, it’s just a joke!"
        "You know, I could add insanity onto one of the main theories for why I’m here. This isn’t magic and science, maybe I’m just loopy."
        mc "What’s your point in all of this, Cream?"
        show cream closeneutral with dissolve
        cream "I told you earlier, the point is to live to have as much fun as possible."
        cream "Live by day, and in the moment! Forget the past, forget the future, just have a fun present..."
        mc "Ahh, not a bad moral after everything you’ve said."
        mc "I’m going to start practicing what you’ve said right now; presently it’s getting cold."
        show cream closehorny with dissolve
        cream "Let me sit on your lap and allow me to warm you up with my fur."
        "She nudges a little closer, her fur brushes across my thigh."
        mc "I think we should head back; the guests will be arriving soon."
        show cream closelaughing with dissolve
        cream "Great idea, I’ll be able warm you up easier under the sheets of my bed, hehe."
        "She leans closer, her large fuzzy breasts pressing against my skin."
        if creamfuckedday1 == 1:
            "I’ve been around this girl all day and her heat has left an impact. I definitely want to fuck her again."
        else:
            "I’ve been around this girl all day and her heat has definitely left an impact, I genuinely want to fuck her."
        mc "Being cuddled up under warm bedsheets does sound appealing after a long day of work…"
        show cream closealthappy with dissolve
        cream "Hehe, doesn’t it?"
        mc "What are we gonna do under the sheets?"
        show cream closehorny with dissolve
        cream "Mmm, each other!"
        "She’s not hiding her arousal either as her legs gently spread and I get a peek of her wet pussy."
        "She bites her lip and one of her hand starts to softly trail from my chest down my tummy and to my pelvis, I can feel blood rushing."
        cream "I want you to take me back to my bedroom and fuck me."
        stop ambience fadeout 2.0
        scene bg black with s
        "We flirt back and forth as we take the short walk back to the bakery."
        show bg bakerybedroom with dissolve
        "She leads me to an unusual bedroom. There’s something strange about this room, just a gut feeling."
        show cream closesatisfied with dissolve
        "Forget that though, I’m too preoccupied with Cream whom immediately makes out with me upon entering."
        cream "Mmphh, mmm… Ahh…"
        show cream closehorny with dissolve
        cream "We can do anything we want in here! You can do anything you want in here."
        cream "This is where the party really gets started, hehehe!"
        hide cream with dissolve
        label creamvmissionary:
            pass
        "Cream bounces onto the bed and I find myself strung along with her, ending up on top."
        show cream missionary1 with dissolve
        cream "I see you’re already so hard down there! Even though you’re not a stallion, you can’t resist a mare in heat."
        mc "I can’t resist a mare that constantly seduces me all day."
        "The two of us embrace on the bed, her soft, curvy body pressed against me."
        if creamfuckedday1 == 1:
            mc "The quickie wasn't enough for me, I need to take my time with you."
        else:
            mc "I’ve been thinking about fucking you all day."
        cream "Hehe, you too?"
        cream "Dumb party stuff aside, agreeing to hang out with a male during mating season was a daft idea."
        mc "Can’t resist me either?"
        cream "The first thing I thought when I saw you was ‘yes please’."
        cream "I pictured this moment the second you stepped through the door."
        cream "I’m surprised you wanted me too."
        mc "Aren’t my thoughts written all over my face?"
        "Cream stared at me for a moment, analysing my expression."
        cream "They are written all over, sure! But I was never good at reading body language, although, your cock is a give-away."
        if creamfuckedday1 == 1:
            mc "I can spell it out for you then. I said it before, I'll say it again, I’ve been thinking about fucking you all day, I haven’t been able to take my eyes off your body."
        else:
            mc "I can spell it out for you then. I said it before, I'll say it again, I’ve been thinking about fucking you again almost all day, I haven’t been able to take my eyes off your body."
        cream "In that case… Don’t hold back, otherwise you’ll have to deal with more of my flirting."
        mc "That wouldn’t be so bad in moderation."
        play music sex1 fadein 3.0
        show cream missionary1-5 with dissolve
        "I fondle her supple, smooth breasts, coupling them in my hands as I massage my fingers into the fluff."
        "On each fluffy breast was an erect pink nipple, which I gladly tease."
        cream "Ahh… [playername]…"
        "Her nipples must be pretty sensitive; she’s softly moaning already."
        show cream missionary2 with dissolve
        "I bring my mouth to one of the nipples, starting to kiss and lick at it, manipulating the tip with my tongue."
        cream "Mmmghhh, aaahh.."
        "Her body shivers in surprise and her back arches, it's clear that her body was highly sensitive due to how aroused she is."
        mc "I bet you’ve been picturing my cock all day, haven't you?"
        "Cream giggles and murmurs a reply."
        cream "I’m a horny girl, I think about cock lots…"
        "As she says that, her legs gently spread, as if instinctively she’s picturing herself being fucked."
        cream "Please, touch it… It’s aching."
        show cream missionary3 with dissolve
        "My hand teasingly caresses its way from her breast, down the curves of her tummy and finally between her soft folds."
        cream "Uaahhh… Mmghh…"
        "Simply moving my finger around her vulva results in lewd wet noises."
        "I find her swollen clit and move my finger around the area, occasionally brushing against it."
        cream "Mmm, aahhhh… [playername]…"
        "Each time I rub her clit she’d squirm and let out another cute moan, no matter how hard she tries to keep them back."
        cream "Mmghhh, aahh… Aaahhh! Aaahhh…"
        "I returned my tongue to one of her nipples, wrapping it around the pink erect nub and twirling it around."
        "The combination of sensations from her nipples and clit gradually overwhelm Cream with pleasure, her body squirming and breathing becoming coarse."
        cream "Mmmghhh, ahh, [playername], I’m c-coming…"
        "The pleasure kept swelling up inside her as she arched backwards, crashing waves of pleasure repeatedly assaulting her senses."
        cream "Ahhh, mmm… This is really good, stallions don’t usually care about pleasing a mare like this, haah…"
        mc "You could say I’m a giver when it comes to pleasure."
        "Her legs part even further; her body language makes it obvious what she wants now."
        cream "I’d say it’s finally time for all those baking innuendos to come to fruition, by putting a bun in my oven."
        show cream missionary4 with dissolve
        "I reposition myself between her legs and she purrs with a lustful expression."
        "Pure wanton fuckery, is that how Moxie put it?"
        play sound cum
        show cream missionary5 with dissolve
        "I placed my member against the soft folds of her fat pussy before slowly pushing it inside of her with a wet schlick."
        cream "Ooooooohhh, yes…"
        cream "The first insertion is always best, hnngg… A feeling you could live for."
        "I could feel her legs wrap around my body as she pulled me towards her, causing me to sink even deeper inside."
        play ambience sex
        "I slowly began to move my hips; it didn’t take much to get Cream squirming with pleasure due to how sensitive she is right now."
        "Even the slightest movement practically sent her eyes rolling back with ecstasy."
        "Every so often I would thrust inside of her with an especially long, deep, hard thrust and she would squeal in delight."
        cream "Mmmnnghh… Aaaaahhhh!"
        "Cream reacted by pushing her hips against me as we both fucked each other in unison."
        "I cherished the warmth of our bodies as my skin and her fur pressed together."
        "I started to fuck faster, my cock was sliding in and out of her pussy with ease and the sensations caused her to dig her fingers into the bed sheets."
        "We kept rutting, getting closer and closer to our respective orgasms, not stopping for a second in that pursuit."
        cream "Ahh, yes, keep going… I’m close!"
        "My cock throbbed as it drove in and out of her tight pussy, all whilst it squeezed and sucked around my shaft."
        cream "Mmphh fuck yeah, I want you to come with me [playername]!"
        "My orgasm was rapidly approaching; my body grew tense and before I realized, I had hit the point of no return."
        cream "Haaahh, I’m coming!"
        play sound cum
        show cream missionary6 with cum
        play sound cum
        show cream missionary6 with cum
        "My climax hit and sent sparks of pleasure through my body while I ejaculated deep inside Cream, filling her pussy with my thick, hot cum."
        play sound cum
        show cream missionary6 with cum
        play sound cum
        show cream missionary6 with cum
        stop ambience fadeout 3.0
        cream "Mmmhnnnggg…"
        scene bg black with dissolve
        if crystalballactivated == 1:
            jump cbmenu
        stop music fadeout 3.0
        "…"
        "The two of us cuddled for a while, although it was starting to get late, it was almost time for the guests of the party to arrive!"
        show bg bakeryparty1 with dissolve
        play music inlove fadein 10.0
        play sound doorbell
        "Ding-dong! Thirty minutes after having sex with Cream, the first guest arrives!"
        ## Honeycrisp
        if farmvisit3 == 1:
            "Upon opening the door, Honeycrisp is the first to arrive. 8:00pm on the dot, I'd expect no less from Honey."
            show honeycrisp nchappy with dissolve:
                xpos 150
                ypos 20
            honeycrisp "Howdy! When I heard [playername] and Cream were throwing a party, I knew it wasn't one to be missed!"
            show blossom laughing with dissolve:
                xpos 500
                ypos 75
            blossom "Y'all really gone all out, this place looks awesome!"
            show cream happy with dissolve:
                xpos 850
                ypos 50
            cream "Honey! Blossom! It's so great to see you two!"
            honeycrisp "I brought a pack of some homebrew cider, let's have a great one!"
            cream "Awwhh, you shouldn't have, let's pop them in the fridge."
            scene bg bakeryparty1 with dissolve
            show blossom happy with dissolve
            blossom "Hey [playername], it's always nice to see you."
            mc "I've been getting around lately, what have you been up to?"
            show blossom laughing with dissolve
            blossom "Really well, thank you again for the help at the farm, Anna and Honey are working closer than ever."
            blossom "They're considering becoming business partners, the future for the farm is really promising."
            mc "Anna does seem like a cunning business woman, she might be the perfect partner for Honey."
            show blossom happy with dissolve
            blossom "Hmm, partner... Do you think they make a cute couple?"
            "Honeycrisp calls from the kitchen."
            honeycrisp "Hey Blossom, come try out these cakes!"
            blossom "Oh! Sorry [playername]! Coming!"
            hide blossom with moveoutleft
            play sound doorbell
            "Just as I move to leave with Blossom the doorbell rings again."
            cream "Ohh, get that for me [playername]!"
            mc "I got it!"
            "Guess those cakes will have to wait."
        else:
            "The first guest is a mare I haven't seen before, I think it's the owner of the farm Honeycrisp."
            if farmvisit1 == 1:
                show honeycrisp happy with dissolve:
                    xpos 150
                    ypos 20
                honeycrisp "Howdy! When I heard Cream was throwing a party, I knew it wasn't one to be missed!"
                show cream happy with dissolve:
                    xpos 850
                    ypos 50
                cream "Honey! It's so great to see you!"
                show honeycrisp laughing with dissolve
                honeycrisp "Ah-ha, and it's the incredibly useful [playername]! Helping out a lot of people, eh?"
                mc "Yeah, I'm definitely getting around. Trying to meet a lot of people in my early days staying in Arcadia."
                show honeycrisp happy with dissolve
                honeycrisp "If you're trying to make friends, ya picked the right person to hang around with, this is gonna be a great party to mingle!"
                show cream neutral with dissolve
                cream "Ah, you flatter me Honey!"
                show honeycrisp happy with dissolve
            else:
                show honeycrisp happy with dissolve:
                    xpos 150
                    ypos 20
                honeycrisp "Howdy! When I heard Cream was throwing a party, I knew it wasn't one to be missed!"
                show cream happy with dissolve:
                    xpos 850
                    ypos 50
                cream "Honey! It's so great to see you!"
                show honeycrisp laughing with dissolve
                honeycrisp "Hello new face, is this the young man from Penelope's letter?"
                mc "That'll be me, nice to meet you Honeycrisp."
                honeycrisp "It's my pleasure, stud!"
                show honeycrisp happy with dissolve
            honeycrisp "I brought a pack of some homebrew cider, let's have a great one!"
            show cream neutral with dissolve
            cream "Oh goodness, you shouldn't have."
            cream "You shouldn't be carrying that around with your injury, here, let me take it to the kitchen."
            honeycrisp "Y'all ain't gotta worry about me! Just show me to the fridge."
            hide cream
            hide honeycrisp
            with dissolve
            play sound doorbell
            "Just as I move to go to the kitchen with the girls, the doorbell rings again."
            cream "Ohh, get that for me [playername]!"
            mc "I got it!"
        if boutiquevisit1 == 1:
            "As I open the door, Ruby steps in with vigor."
            show ruby laughing with dissolve:
                xpos 750
                ypos 50
            ruby "Hellloooo darling!"
            mc "Hey Ruby! It's great to see you!"
            play music melodytheme
            show melody fufufu with dissolve:
                xpos 250
                ypos 75
            show ruby neutral with dissolve
            melody "Helllooo wormy boi!"
            mc "Oh, hey Melody."
            show melody happy with dissolve
            melody "Hey cutie, thanks for the invitation!"
            melody "Oh, Blossom and booze is in the kitchen, see ya chumps."
            hide melody with dissolve
            show ruby embarrassed with dissolve
            play music inlove fadeout 3.0
            ruby "My, my, don't take Melody's troublesome behaviour too personally."
            mc "Don't worry about it, I know she's only playing around with me."
            show ruby happy with dissolve
            ruby "When I was younger I was the same in some ways, whenever I had a crush on a boy I'd tease him."
            mc "You grew out of it?"
            show ruby embarrassed with dissolve
            ruby "*Giggles*, partially! I still tease Hon- ahhh..."
            mc "Awh, you have a {i}crush{/i} on her?"
            show ruby shy with dissolve
            ruby "It's a bad crush to have, since I know she's involved with a heifer..."
            if farmvisit2 == 1:
                mc "Anna? That's rough."
            ruby "I guess it's not all bad I suppose. Just like you and I, she and I can have 'fun'."
            mc "Everyone's really sleeping around, huh?"
            show ruby laughing with dissolve
            ruby "We truly are despicable, aren't we just? Perhaps it's time we all grew out of it and settled down with partners."
            show ruby horny with dissolve
            ruby "But I know I couldn't refuse if you asked."
            mc "You're kinda making me feel guilty!"
            play sound doorbell
        else:
            "As I open the door, it's a white mare with pink hair, I don't believe I've met her before."
            show ruby happy with dissolve:
                xpos 850
                ypos 50
            ruby "Oh! Hello darling. Moxie's friend, correct? We haven't been properly introduced yet, although I've seen you roaming around."
            mc "Indeed, you're the boutique owner, right?"
            show ruby laughing with dissolve
            ruby "Ah yes, it's truly my passion! I design dresses, clothes and the such."
            mc "Pardon my ignorance, since I'm not from around here, but who buys your clothes?"
            show ruby neutral with dissolve
            ruby "That's a perfectly natural question to ask darling, I sell clothes to, uhh..."
            ruby "Well, business is somewhat limited. I sell sexy lingerie for the bedroom, and wedding dresses."
            ruby "Some ponies like myself occasionally wear bathrobes too."
            mc "Where I'm from, everyone wears clothes, so I feel quite naked around here."
            show ruby laughing with dissolve
            ruby "Ohh? Perhaps I should relocate my business there! *Giggles*!"
            play sound doorbell
        "The door rings again! These mares are far better at arriving on time than I'm used to."
        if barvisit1 == 1:
            show rikub:
                xpos 150
                ypos 50
            show riku laughing:
                xpos 150
                ypos 50
            with dissolve
            riku "Well well well! If it ain't troublemaker 1 and 2!"
            show riku happy with dissolve
            riku "You can decide amongst yourselves who is who."
            ruby "Ahh Riku, it's been too long!"
            scene bg bakeryparty1 with dissolve
            "The two girls hug, Riku clearly enjoying the feeling of Ruby's bosom almost a little too much as she winks at me."
            show rikub:
                xpos 150
                ypos 50
            show riku laughing:
                xpos 150
                ypos 50
            show ruby happy:
                xpos 850
                ypos 50
            with d
            riku "You been busy lately Rubes? You used to come to the bar all the time."
            if boutiquevisit3 == 1:
                show ruby laughing with dissolve
                ruby "Well, business has simply been fantastic as more and more dresses are being accepted! I'm really starting to make a name for myself."
                riku "That's great news! Here, I brought some drinks, let's go and celebrate instead of mooting around the door."
            else:
                show ruby shy with dissolve
                ruby "Well, business has been a little tight, I've been trying to get my name out to keep cash flow going."
                riku "Keep trying Rubes, I know your designs are amazing!"
                riku "Say, I brought some drinks, let's go and forget about work and drink for the future."
            show ruby happy with dissolve
            ruby "Good idea, I could use a few drinks."
        else:
            show rikub:
                xpos 150
                ypos 50
            show riku laughing:
                xpos 150
                ypos 50
            with dissolve
            riku "Well well well! If it ain't the notorious furless man and his girlfriend!"
            show ruby embarrassed with dissolve
            ruby "G-Girlfriend? I don't know what you mean!"
            show riku happy with dissolve
            riku "Ahaha, I'm kidding Rubes! You're way too easy to wind up."
            show ruby happy with dissolve
            ruby "Oh Riku! I've not missed your teasing at all!"
            scene bg bakeryparty1 with dissolve
            "The two girls hug, Riku clearly enjoying the feeling of Ruby's bosom almost a little too much as she winks at me."
            show rikub:
                xpos 150
                ypos 50
            show riku laughing:
                xpos 150
                ypos 50
            show ruby happy :
                xpos 850
                ypos 50
            with dissolve
            riku "Nice to meet you new guy, hope you're settling in well. Swing round the bar any morning if you're looking for work."
            mc "Sure thing, thank you."
            riku "You been busy lately Rubes? You used to come to the bar all the time."
            if boutiquevisit3 == 1:
                show ruby laughing with dissolve
                ruby "Well, business has simply been fantastic as more and more dresses are being accepted! I'm really starting to make a name for myself."
                riku "That's great news! Here, I brought some drinks, let's go and celebrate instead of mooting around the door."
            else:
                show ruby shy with dissolve
                ruby "Well, business has been a little tight, I've been trying to get my name out to keep cash flow going."
                riku "Keep trying Rubes, I know your designs are amazing!"
                riku "Say, I brought some drinks, let's go and forget about work and drink for the future."
            show ruby happy with dissolve
            ruby "Good idea, I could use a few drinks."
        play music inpeace fadein 3.0
        scene bg bakerykitchen with dissolve
        if farmvisit3 == 1:
            show honeycrisp nchappy:
                xpos 0
                ypos 20
        else:
            show honeycrisp happy:
                xpos 0
                ypos 20
        show rikub:
            xpos 300
            ypos 80
        show riku neutral:
            xpos 300
            ypos 80
        show cream laughing:
            xpos 600
            ypos 60
        show ruby happy:
            xpos 900
            ypos 50
        with dissolve
        "Wow, there's so many people here now! They're all such great friends, they talk as if they've known each other for years, and they probably have."
        cream "And so, I was like, yeah, and he was like, totally! And she was like, uhuh!"
        ruby "Ohh, but what about Sqiggles?"
        honeycrisp "Fancy a cider, Riku?"
        show riku laughing with dissolve
        riku "I could use a couple if I'm gonna follow that conversation."
        "I can't really follow the conversation either, there's a lot of specific chatter and catching up happening, it's somewhat overwhelming."
        "Although there're still a few more people missing..."
        play sound doorbell
        "Oh, there's the door again!"
        mc "I'll get it!"
        scene bg bakeryparty1 with dissolve
        "I open up the door and it's ol' reliable, a girl that'll definitely keep me company, even if the party is overwhelming."
        show moxie happy with dissolve:
            xpos 200
            ypos 20
        moxie "Heyy! Sorry I'm a little late, I know it's not BYOB but I brought some drinks anyway!"
        mc "Ahaha, that explains why one of the mares that lives the closest ended up being one of the last to arrive!"
        show moxie laughing with dissolve
        moxie "Heh, you know what they say, those the closest are always the last to arrive."
        if libraryvisit3 == 1:
            show moxie happy with dissolve
            moxie "But there's another reason I'm late, look who I ran into!"
            show lilyb:
                xpos 750
                ypos 50
            show lily shy:
                xpos 750
                ypos 50
            with dissolve
            lily "Uhm, hey! The party's here, right?"
            show moxie althappy with dissolve
            moxie "She won't admit it, but I saw her outside building the courage to come in."
            lily "It's just that I haven't seen some of these girls for months..."
            lily "*Sigh* But there's no way I can refuse a party when all the Elements of Har'Mony are attending."
            mc "Awh, let's get her some booze!"
            show moxie laughing with dissolve
            moxie "Great idea! Your genius is showing!"
            lily "Mmm, okay, I do like Honey's cider."
            scene bg bakerykitchen with dissolve
            "As we enter the kitchen, Lily manages to find some confidence and make some light conversation with her friends. Before she knows it, she's completely back to her usual self."
            show moxie happyneutral with dissolve:
                xpos 200
                ypos 20
            moxie "Really goes to show ya, most of that shyness is in the mind."
            mc "That's true, but it can still be very hard to overcome."
            moxie "She'll definitely break out of it though, anyone can feel shy after not talking for months."
        else:
            scene bg bakerykitchen with dissolve
            show moxie happyneutral with dissolve:
                    xpos 200
                    ypos 50
        moxie "Phew, this party is really good! It's actually my first party with Cream. For once, we're both strangers in this new world."
        mc "You feel shy too?"
        moxie "Mm, a little, but these are all lovely mares, and I'm quite close with some of them, like Riku."
        if barvisit2 == 1:
            mc "Heh, we both know how close you are with Riku."
            moxie "Ahh, shush you, someone might hear."
        pass
        if days >= 6:
            moxie "And that's to say nothing about how close you are with some of them, right?"
            mc "I don't think it'd be appropriate to overshare."
            moxie "Hehe, my lips are sealed."
        else:
            moxie "What about you? Are you close friends with anyone yet?"
            mc "I'm settling in well, me and Cream clicked pretty good."
        show moxie horny with dissolve
        moxie "Have you, y'know, done the business with Cream yet?"
        mc "Oh my gosh, you are so nosy!"
        show ruby happy with dissolve:
            xpos 500
            ypos 50
        ruby "Did someone say nosy, darlings? I'd like to be nosy and ask where darling Penelope is."
        show moxie neutral with dissolve
        moxie "Hmm, good question, doesn't look like she's coming though."
        mc "Really? I thought she'd quite enjoy a party."
        show moxie neutralhappy with dissolve
        moxie "Seems like she's preoccupied with her work, she's a busy gal after all."
        show ruby neutral with dissolve
        if libraryvisit3 == 0:
            ruby "That's a shame, I would have liked to see Lily and Butters as well."
        else:
            ruby "That's a shame, I would have liked to see Butters as well."
        ruby "Almost a full house, but we never seem to have the luck these days. It's such a shame that the Elements of Har'Mony have grown apart after everything we've been through."
        if forestvisit3 == 1:
            play sound doorbell
            mc "Oh? Someone else?"
            "Cream goes to answer the door and it's Butters! After some greetings, she quickly finds herself talking to Moxie, Ruby and I."
            show butters dresshappy with dissolve:
                xpos 700
                ypos 35
            butters "Parties aren't really my style, but I thought I should come for old time's sake."
            show ruby happy with dissolve
            ruby "I really respect that darling, would you like me to make you a drink?"
            butters "Do you have anything sweet?"
            moxie "You like sweet drinks too? Try some of the stuff I brought, it's great."
        stop music fadeout 3.0
        scene bg bakeryparty2 with dissolve
        show cream happy with dissolve
        cream "Hey everyone, I wanna do a cheers!"
        if forestvisit3 == 1 and libraryvisit3 == 1:
            cream "I'm so glad the entire old crew is here! It really warms my heart!"
        else:
            cream "Not everyone could make it today, so I want to make this toast to them and the old times. It really warms my heart to see so many of my old friends here in one place."
        cream "From the day we met, to the day we conquered that evil bug queen many years ago, and even today, we'll be friends to the end!"
        cream "I want everyone to have a super duper amazing party! Cheers!"
        everyone "Cheers!"
        scene bg black with dissolve
        if crystalballdayactivated == 1:
            jump cbmenu
        "The party goes on for hours and everyone has a great opportunity to mingle and get drunk."
        "Who should I talk to the most? They might take me to their place after the party."
        menu:
            "Moxie":
                "I spend the majority of the night talking with Moxie, which easily leads to sex when we get back to her wagon."
                scene bg moxiebednight with dissolve
                jump moxieanal
            "Butters" if forestvisit3 == 1:
                "I spend the majority of the night talking with Butters! She gets drunk very easily, and she's very flirty with me throughout the night."
                "As we return to her cottage, her drunk succubus form is the one to take initiative. I didn't expect that!"
                jump succbuttersrcg
            "Honeycrisp" if farmvisit3 == 1:
                "Honey and I spend a lot of time talking, she laments that she never got enough time off work to spend time with me properly, and says she'll 'fix that' if we have some more time alone."
                "Yeah, you know I'm going back to her place."
                stop ambience fadeout 5.0
                show bg honeycrispbed with dissolve
                $ honeycrispcomplete = 1
                play music sex1 fadein 3.0
                show honeycrisp closehorny with dissolve
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "With a smirk, the drunken Honeycrisp pushes me down onto her bed using the hand that was once in a cast. Now that it's free, I'm at the complete mercy of this girl's sexual appetite, and she's ready to show it in full force tonight."
                else:
                    "Giggling, the drunken Honeycrisp seductively presses me against the soft sheets of her bed using her main hand. She crawls towards me like a predator catching its prey. She isn't going to hold back tonight."
                hide honeycrisp
                show honeycrispb cowgirl1
                show honeycrisp cowgirl2
                with dissolve
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "I settle down under her, my cock eagerly pointing into the air already. I give Honeycrisp a nod which she returns with a smug look before she straddles me and slowly slides down onto my erect member."
                else:
                    "The erotic display causes a rush of blood to my loins, my cock readily growing hard and pressing against Honeycrisp's fur thigh causing her to grin lecherously. Wordlessly, she positions herself above me and sits on my cock."
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    honeycrisp "Mmmphh, that satisfying feeling of slow insertion filling up my pussy, it never gets old..."
                else:
                    honeycrisp "Ahh, I love your cock... Ever since rut in the barn I've been thinking about this while I masturbate..."
                play ambience sex fadein 3.0
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "Her pussy's comfortable tightness squeezes and massages my shaft as I give myself over Honey's dominant riding."
                else:
                    "Her insides squeeze around my throbbing shaft sending waves of pleasure throughout me, especially as she begins to move her hips up and down."
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "It's almost like she's purposely contracting her muscles to tighten and squeeze around my cock."
                else:
                    "Her muscular body provides a distinct internal tightness that no mare I've been with has been able to replicate."
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    honeycrisp "Ehehe, you like that stud? I'm not your average rider."
                else:
                    honeycrisp "Mmm, you like it when I squeeze my pussy like that? I can feel your cock throb every time I do it, ehehe..."
                show honeycrisp cowgirl3
                with dissolve
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "Her hips start to twist and gyrate as she speeds up, the sensations of sex surge through my body, racking it with pleasure."
                else:
                    "She leans forward as she accelerates the bouncing on my cock, each wet slap against my pelvis ignites another wave of immense pleasure."
                play sound spank
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "I reach back and give her a slap on the ass causing her to jolt up with surprise and giggle."
                else:
                    "Despite her dominance, I recall that she likes to be spanked. So I reach back and despite the slightly awkward position I give her ass a lil slap that causes her to giggle."
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "As if smacking a racehorse, she takes the cue to speed up, bouncing on my lap with complete abandon."
                else:
                    "Taking the spank as a challenge, she begins to speed up, going almost hysterically fast and overwhelming my senses."
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    honeycrisp "Aahhh, ahh... Do you like that? You like mah pussy?"
                else:
                    honeycrisp "Mmphh, I-I'm gonna come soon, ahh..."
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "She even begins to moan freely, that coupled with the wet schlicks of our copulation leaves me to believe Blossom could definitely hear us right now."
                else:
                    "Unable to hold back any longer, a few moans slip out of the orange mares mouth while even lewder sounds slip out of her pussy as wetness freely dribbles and bubbles at our point of contact."
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "It's clear that Honey is driven by pure pleasure and sexual instinct right now, she doesn't care about anything but sex as she blissfully moans."
                else:
                    "Giving herself completely to the lust, Honey rides me with complete focus as she pushes herself to her orgasm. All while I try to hold back mine."
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "She grits her teeth and her eyes roll back as she clearly orgasms, her pussy tightly contracting around the base of my cock pushing me closer to my own orgasm."
                else:
                    "It doesn't take long for her to be pushed over the edge as her entire body shakes with orgasmic energy. Yet somehow her riding doesn't falter for a second."
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    honeycrisp "Mmphhh fuck, I came already..."
                    honeycrisp "But I'm not done with you yet, I'm gonna make this cock blow its load straight into my pussy."
                else:
                    honeycrisp "Ahh, I-I'm coming! Cum with me [playername], fill up my pussy!"
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "Honeycrisp bites her lip as she continues to ride me, wanting to enjoy her time on top of me as long as she can before I inevitably cum inside."
                else:
                    "Honeycrisp enjoys every second of her intense riding, she intentionally puts all her effort into pushing me over the edge, and soon she succeeds."
                show honeycrisp cowgirl5 with cum
                play sound cum
                show honeycrisp cowgirl5 with cum
                play sound cum
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "As her pussy continues to grip around my shaft I find the pleasure is too much and I unload my cum deep inside her womb."
                else:
                    "My cock begins to erupt inside her, flooding her pussy and womb with my thick cum."
                stop ambience fadeout 3.0
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "The feeling of my cum inside her causes Honey to swoon and orgasm again as the familiar contractions of an orgasming mare return to my cock."
                else:
                    "The hot feeling of my semen inside Honey excites her so much she seems to orgasm again while riding, her back and eyes falling back with pure euphoria."
                scene bg honeycrispbed
                show honeycrisp closesatisfied
                with dissolve
                $ rand = renpy.random.randint(1,2)
                if rand == 1:
                    "Once we've both finished our final orgasms, Honey rolls off and pants heavily, although considering her superior physique it doesn't take her long to gain her breath back."
                else:
                    "After her climatic finishes, we're both left panting, although we quickly recover since I barely moved and Honey is no stranger to intense cardio."
                show honeycrisp closehorny with dissolve
                honeycrisp "Your cock is amazing, stud."
                mc "Only half as good as your riding Honey."
                scene bg black with dissolve
                "We sleep through the night cuddled together."
                stop ambience fadeout 3.0
                "In the morning I return home, satisfied after the party and 'one' night stand."
                jump altmorning
            "Blossom" if farmvisit3 == 1:
                "I talk to Blossom a lot tonight, she's a little more quiet than everyone else but provides great conversation none-the-less."
                "We agree to go back to her place that night."
                stop music fadeout 3.0
                stop ambience fadeout 3.0
                $ blossomsex = 1
                "I climb into bed with Blossom and she playfully rolls me over."
                blossom "I'll be on top, all that alcohol has filled me with energy."
                hide blossom
                show blossomb2 sex
                show blossom sex1
                with dissolve
                play music sex1 fadein 3.0
                "As much as I'd like to protest, I'm left mesmerised as Blossom straddles me and starts to rub her pussy on my cock whilst giggling girlishly"
                "She wraps her spare hand around my member and starts to give it gentle strokes up and down, causing my cock to swell up and stiffen completely."
                "Blossom bites her lips and wiggles her hips, she's already eager for more, and the dripping wetness between her legs signals that she's ready to take me."
                play sound cum
                show blossom sex2 with dissolve
                "With a bit of her teasing, my cock is now raging hard and throbbing. Fortunately, Blossom is all too willing to satisfy as she lifts herself over me and allows my cock to sink deeply into her."
                "She takes her time sliding down my thick cock, I can feel my cock spread her lips apart with a delectable slowness until I'm finally at the hilt."
                "Blossom let's out a satisfied sigh and stares into my eyes with dreamy longingless, she merely nods before her hips begin to move with a passion."
                play ambience sex fadein 3.0
                "As she rises and falls along my member a mixture of gasps and moans slip from her lips as she loses herself in the throes of passion."
                "Every drop of the hips is accompanied by a lewd, arousing schlick as her wetness gleams off my cock and driplets of her lust pool at my pelvis."
                show blossom sex3 with dissolve
                blossom "Aahhh, mmmphh, we should do this every day, haahh, ahh..."
                "Her riding gains speed and she arches her back in response to the quaking pleasure throughout her body, I too feel tense from the overwhelming sensation she's providing me."
                "With each deep thrust I can feel myself getting closer and closer, her pussy trying to milk my cock with all its worth."
                blossom "Mmphh, please cum in your lil' cumslut, please give me your cum!"
                "She begs as our sex devolves into an orgasmic mess, her pussy clamps down around my cock tightly which in turn pushes me over the edge."
                show blossom sex4 with cum
                play sound cum
                show blossom sex4 with cum
                play sound cum
                "And in sudden orgasm I shoot several thick loads deep into her womb which squelch and drip down our point of connection."
                show blossom sex4 with cum
                play sound cum
                show blossom sex4 with cum
                play sound cum
                "She rides out both of our orgasms with glee before the climax fades and with that our energy."
                stop ambience fadeout 3.0
                scene bg black with dissolve
                "Blossom finds herself snuggled against against my chest and we cuddle, still joined at the hips."
                "We sleep together, and in the morning I return home."
                jump altmorning
            "Ruby" if boutiquevisit2 ==  1:
                "Ruby and I spend the majority of the night talking together, she handles her drink quite well."
                "She's a little more subtle than the other ladies with her flirts, at one time while we're alone she kisses me and encourages me to come to her place that night."
                "You know I'll be there."
                show bg rubybedroom with dissolve
                show ruby sexlipbite with dissolve
                ruby "Oh darling... It's so unlady like to fuck while I'm so drunk! *Giggles*"
                play music sex1 fadein 3.0
                ruby "I've been having a lot of naughty thoughts about you today [playername], look how wet you made me."
                ruby "A gentlemen needs to help a lady relieve some stress, how about it?"
                play sound cum
                play ambience sex fadein 3.0
                "As she sinks that tight pussy over my cock and begins to hump me it feels as good as I imagined."
                ruby "Mmmphhh, you feel so good inside me..."
                "She bites her lip, and starts to ride my cock up and down at a teasing yet pleasureful pace."
                ruby "Just sit back and relax dear, and try not to cum before me, hehe."
                show ruby sexofacedeep with dissolve
                show ruby sexoface with dissolve
                "Her hips start to gain speed as she leans forward, and balances herself so she can put more oomph into the riding."
                show ruby sexofacedeep with dissolve
                show ruby sexofaceaction with dissolve
                show ruby sexofacedeep with dissolve
                show ruby sexofaceaction with dissolve
                ruby "Mmphh, your cock is so thick inside me, I love fucking you darling."
                "Her experienced hips start to twist and gyrate my cock in magnificent ways, toying and teasing my shaft while squeezing as much pleasure from me as she can."
                show ruby sexofacedeep with dissolve
                show ruby sexofaceaction with dissolve
                "My point of contact with the mare is a deluge of her juices that constantly dribble and drip onto my pelvis, the wet sounds created from our rutting are vulgar to say the least."
                show ruby sexofacedeep with dissolve
                show ruby sexofaceaction with dissolve
                show ruby sexofacedeep with dissolve
                show ruby sexofaceaction with dissolve
                ruby "Ohoh gosh, this feels too good, I'll lose my mind!"
                show ruby sexofacedeep with dissolve
                show ruby sexofaceaction with dissolve
                "She purrs pure joy as she pounds against my lap, manhandling my cock with the grip of her tight walls which squeeze and constrict in an attempt to milk me."
                show ruby sexahegaodeep with dissolve
                show ruby sexahegaoaction with dissolve
                "Driven by pure pleasure, she begins to rub her pussy too. She's unable to contain her blissful moans in the face of the dual pleasures which rapidly build her up to a mind-shattering orgasm."
                show ruby sexahegaodeep with dissolve
                show ruby sexahegaoaction with dissolve
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
                ruby "Hehe, look how much you came..."
                ruby "Darling, you are a wonderful sex partner…"
                mc "I think you're one of my favourites too, but don't tell the others!"
                ruby "Hehe, we're so good that people would tune in to watch. Maybe next time we should do a camshow, but no drinking beforehand!"
                scene bg black with dissolve
                "We snuggle in bed together and fall asleep"
                stop ambience fadeout 3.0
                "In the morning we part ways and I return home."
                jump altmorning
            "Melody" if boutiquevisit3 == 1:
                "As I talk with Melody, she's a relentless tease as usual, although far more watered down when around the others."
                "She does seem to show subtle signs of jealousy though, and she's the one that actually asks if I want to come to her place."
                "While she'd never admit that she brought me home for sex, I can definitely tell the alcohol has made her hornier than usual."
                scene bg melodybedroomnight
                show melody closehappy with dissolve
                jump melodyeveningsex
            "Lily" if libraryvisit3 == 1:
                "I spend most of the evening talking with Lily, encouraging her to open up, which she easily does with aid of a few drinks."
                "Her inner slut also seems to escape along with that drunkness though, while not enough to embarass herself, it's easy to forget that this slut is incredibly horny for me."
                "Guess I'll have to take her home and teach her a lesson."
                show bg dusklightbedroomnight with dissolve
                show lilyb close
                show lily closehorny
                with dissolve
                stop music fadeout 3.0
                stop ambience fadeout 3.0
                lily "I wanna fuck you..."
                mc "How do you want to do it?"
                lily "It felt really good when you were pounding me on the bed..."
                mc "Missionary? Let's make it more interesting and lift your legs up, your pussy gets even tighter then."
                lily "And your dick fills me up even more, ehehe."
                play music sex1
                show lily closehorny with dissolve
                lily "Okay, you can do whatever you want to me..."
                show lily missionary1 with dissolve
                "Lily bounces backward on top her bed with her legs eagerly spread, her drippy pussy shamelessly ready and in view."
                "Lily lay there and waits for me to make my move while her tail gently sways back and forth."
                lily "I'm ready for you babe, make me your little slut."
                show lily missionary0 with dissolve
                "I lay on top of her and start making out with the cute purple mare as she submissively melts into my kiss."
                "Her hands caressing up and down my chest, and her legs wrap around my waist pulling me in closer."
                lily "Mmm... mmphh… Hnn…"
                "She pulls away from the kiss and begins to pant, instead choosing to hold me close and nuzzle my chest."
                lily "My pussy is ready for you, fuck me hard!"
                play sound cum
                hide lily
                show lilyb missionary
                show lily missionary3
                with dissolve
                "I bring my tip to her sopping wet pussy and slowly slide myself inside, savouring the feeling of her warm tightness along each inch of my shaft."
                "The mere penetration of my thick cock inside her causes Lily to shiver and let out a loud moan, it’s clear she’s been eagerly anticipating this."
                lily "Aahh, it never stops feeling amazing... I could get addicted to this, haahh..."
                play ambience sex fadein 2.0
                "With her legs against my chest and my hands holding her thighs, I vigorously fuck the purple mare."
                "With her thighs up like this, her pussy feels even tighter and the sex is even more amazing for the both of us."
                lily "Mmphh, I bet you like my tight pussy, don't you?"
                "My cock is throbbing and she can barely contain the pure pleasure and desire she feels, as she squirms on the bedsheets."
                "In addition to my thrusting, I occasionally spank her ass, each time she lets out an adorable squeak."
                lily "Aahh! Yes! I like that babe, mmmm...!"
                "I knew she’d love the spanking; the quiet ones are always the kinkiest."
                "My thrusts start to come faster, and Lily in her enthusiasm tries to match my thrusts by bouncing her hips up against my body."
                "The effort of both our bodies result in hard, deep thrusts that pleasure every inch of my shaft, and every inch of her insides."
                show lily missionary4 with dissolve
                "I spank her again and the mare's eyes practically roll back, overwhelmed with pleasure as her hips buck and her pussy dribbles with a few droplets of squirt."
                lily "Aaahhh, ahhh, aaaaahhhhh! I-I'm gonna, I'm gonna cum! Yessss..."
                lily "Aahh… F-Fuck… I-I'm coming! Hnngg…"
                "The next spank seems to really push her over the edge, her muscles tense up and her pussy tightens. She squirts a bit more onto my cock as she has an extremely powerful orgasm."
                "Now that she's coming, I no longer have to hold my orgasm down, immediately I let down my guard and my hips start to speed up. I couldn't hold back even if I wanted to."
                "I fuck Lily's wet pussy as fast as I can and my cock starts to throb as my orgasm quickly builds."
                lily "Mmmmm, I want you to cum inside me! Make me your lil' cum dump! Aaahhh, aaaahh…"
                "Eager to fill up this dirty mare's pussy, my cock stiffens and prepares to unload itself as I reach my climax."
                play sound cum
                show lily missionary5 with cum
                play sound cum
                show lily missionary5 with cum
                "I release my load deep into her pussy, my thick, hot cum seeps throughout her as I continue to fuck her throughout my orgasm, maximising the brief heightened pleasure."
                play sound cum
                show lily missionary5 with cum
                play sound cum
                show lily missionary5 with cum
                stop ambience
                stop music fadeout 7.0
                "After a few more loads of cum, I pull out and catch my breath, cum oozing from our point of contact."
                show lily missionary6 with dissolve
                lily "Ahh… That was so good, I love it when you treat me like a dirty slut…"
                lily "Just using me like a little cum dump"
                mc "Phew… I’d let a tight pussy like that milk me every morning if I could."
                lily "Mmm, but it could… You just need to visit me every day, hehe."
                scene bg black with dissolve
                "Lily and I snuggle together sleeping long into the night."
                "In the morning we part ways I return home"
                jump altmorning
            "Riku" if barvisit1 == 1:
                "Riku provides great company throughout the night, and we pretty much talk to everyone throughout the night."
                "As the evening grows late, it's her suggestion to 'walk home together'."
                show bg barupstairsnight with dissolve
                riku "I feel like getting fucked, wanna take my pussy this time?"
                mc "Show me the goods and I'll get to work."
                show rikub sofasex
                show riku sofasex1
                with dissolve
                "She lays forward on the sofa, presenting her ass. Her eyes glossed over and expectant."
                riku "Do you like my cute lil' butt?"
                mc "I certainly do, but it's your tight pussy that's the star of the show."
                "I waste no time crawling behind her and positioning my shaft against her entrance."
                riku "Mmmph, you can thank your thick cock for that, hehe."
                play ambience sex fadein 3.0
                show riku sofasex2 with dissolve
                "I push myself inside of her and immediately start moving my hips back and forth."
                riku "Aahhh, ahhh! I love the way your cock fills me up, mmm..."
                "I take my time and fuck her gently, savouring the tightness and warmth of her vagina. The long, slow thrusts drive her wild. "
                "With both my hands I fondle and quish her thick and juicy ass."
                riku "Mmm… Hehe, you really do love my butt."
                "She’s so soaking wet, every time I sink deep inside of her it’s accompanied by a saccharine squelching sound."
                show riku sofasex3 with dissolve
                riku "Ahh, ever since we've started fucking, I've been even hornier than usual lately, and even wetter..."
                "Truly there was a submissive slut ready to escape within Riku all along, she just needed the right key to let it out."
                riku "Spank me [playername], spank your little slut."
                play sound spank
                "She guides my dominant hand and brings to her ass, I know exactly what to do."
                show riku sofasex4 with dissolve
                riku "Gimme it as hard as last time, aahhh…"

                play sound spank
                "I raise my dominant hand and bring it down powerfully causing a slap sound, this seems to hit the spot as her eyes roll back and she lets out a satisfied moan."

                riku "Ohh phuck yesh…"
                "I can’t help but fuck a little faster, her hips are rocking in response to each thrust too, and her pussy squeezing even tighter around my cock."

                riku "Aaahhh, aahhh, ah, ahhh! Oh fuck! I’m coming!!!"

                "Spanking her out pushed her over the edge, and she starts to have a strong first orgasm, her hips bucking and her whole-body squirming as the pleasure overwhelms her."

                "I can feel my cock throbbing in response to her pussy contracting around it, I really could come any second if I let my guard down."

                riku "Faster Daddy, faster!  Ahhh, ahh! *Pant, pant*."
                "Why is she suddenly calling me daddy again?! That level of dirty talk is only going to make me cum faster."
                "It doesn’t help that she’s rocking her hips into me, practically fucking me just as hard as I’m fucking her, and damn it feels amazing."

                riku "Mmphh fuck! Spank me harder! *Pant, pant*."

                "I spank harder, while her pussy squeezes and sucks harder around my shaft as if it’s trying to milk my cock. All whilst Riku moans and squeaks with erotic delight."

                "My orgasm keeps swelling up, I can’t hold back much longer, I’m going to cum!"

                "Riku arches her back, her eyes roll back and she and lets out a sensational moan, as she has her second orgasm."

                "Immediately I feel myself climaxing as well, my cock throbs and swells as my vision turns cloudy and my mind fogs up."
                show riku sofasex5 with cum
                play sound cum
                show riku sofasex5 with cum
                play sound cum
                "The two of us orgasm together, my cock unloading copious amounts of cum deep inside Riku’s pussy whilst we fuck each other passionately."
                show riku sofasex5 with cum
                play sound cum
                show riku sofasex5 with cum
                play sound cum
                riku "Mmphhh, yeeeesss! Ahh!"
                stop ambience fadeout 3.0
                show riku sofasex6 with dissolve
                "As I pull out, a trail of cum still connects us, before it collapses down her thigh."
                stop music fadeout 10.0
                riku "Haah, I-I can barely feel my butt, hahaa. *Pant, pant*."
                scene bg black with dissolve
                "Riku and I go to her bedroom and drift off to sleep together."
                "In the morning, I return home."
                jump altmorning
        ###########??
        "It’s around 6pm when I get back, and Moxie is already preparing dinner."
        moxie "Hey, you’re back home late, busy day?"
        mc "Yeah, I’ve been baking almost all day, on my feet in a hot kitchen."
        moxie "Bakery eh? Who were you working with? I thought it was closed."
        mc "It would have been really boring if Cream wasn’t hilarious company."
        mc "Yeah the owners are away, there’s a girl called Cream working there and keeping the place going until they get back."
        moxie "Ohh, Cream? Maybe she’s one of Lily’s friends, but I haven’t heard of her before. I didn’t mean to send you off working with a stranger, I hope she was okay."
        mc "She was fine, but… you really haven’t heard of her before?"
        moxie "No, the name doesn’t ring a bell."
        mc "She seems to have heard of you before though."
        moxie "Oh well, the great Moxie always calls out her name in her performa- uh, my performances."
        moxie "If she works at the bakery, she’s probably seen me in passing."
        "Cream was… well, full of surprises. I wonder what else is wrapped up within that girl."
        "When she spoke about insanity to me, was she trying to imply that’s one of the reasons I’m in this world?"
        "Certainly not my favourite interpretation, but I can’t get it out of my head for some reason."
        mc "Hey Moxie, you are real, right?"
        moxie "Of course I’m real you dummie, are you?"
        mc "I hope so, but the only thing more fun than one reality smashing discovery is two."
        "A great girlfriend, friends, and a fun life…"
        mc "I just had a daft thought, what if it wasn’t magic that brought me here, but imagination?"
        moxie "Like a dream? I thought we already established that wasn’t the case, no dream could ever last this long."
        mc "Yeah, you’re right. If I’m living in a world where any answer can be true, I’d rather choose a more interesting one."
        "Still, I wonder what Cream was talking about, why did she tell me all that stuff?"
        "She’s a crazy girl, that’s for sure."
        "…"
    label bakeryvisit2:
        "Time to return to the bakery, and see what I can cook up with Cream."
        show bg bakerydoor
        "I make my way to the front door of the bakery."
        "Despite the fact it’s nearly 8:30am, the establishment still seems completely closed, shouldn't she be in the kitchen right now?"
        "Guess I’ll knock."
        "I take a step forward and just as my hand reaches to knock on the door, it flings wide open and Cream pops her head out."
        play music cream1
        show cream laughing with dissolve
        cream "Oh goodie, [playername]! It’s so great to see you again, do come in!"
        mc "Huh?"
        show cream neutral with dissolve
        cream "Come on, don’t just stand there looking like a soggy pancake, come in!"
        "Ah, I just realized I’ve been stood here with my arm extended for about two seconds looking gormless."
        mc "Thanks, it’s nice to see you too."
        scene bg bakery with dissolve
        "I step into the dark bakery, it feels despairingly empty compared to how bright and cheerful the party was."
        "No cakes prepared either. I don’t say anything though, I’m just here to bake, get paid, and maybe have fun."
        show bg bakerykitchen with dissolve
        "The two of us enter the kitchen and she begins the usual charade of cheerfully and bouncingly getting all the ingredients and recipe books out."
        play music mky fadein 3.0
        "Oh, and before she forgets, the music!"
        show cream happy with dissolve
        cream "It’s so wonderful to have you back, we’re gonna have so much fun today I just know it."
        cream "And not just icing cakes, I’ll let you ice me too, hehe."
        mc "Hey, Cream, this place feels closed, I thought you were supposed to start running the shop now?"
        show cream neutral with dissolve
        cream "Of course silly, but it’s not hour’o’nine yet, I still need to finish baking this morning’s batch."
        mc "You sure are cutting it close..."
        cream "Now come on, I bought some new ingredients for us! I made sure to get extra eggs this time, hehe."
        "We make some idle chat while baking together."
        show cream laughing with dissolve
        cream "After we use up all these eggs, you can try and fail at fertilising mine."
        mc "It’s quite lucky that we’re not compatible species, isn’t it?"
        show cream neutral with dissolve
        cream "Not sexually compatible with humans, but isn’t it strange how the pheromones are the same?"
        mc "I guess evolution has just designed a limited number of chemicals and we had to share a few things."
        show cream happy with dissolve
        cream "Pfft, you say that, but we’re interdimensional beings. Evolution makes sense within the frame of a singular world that you and I exist in, but it seems like a wild coincidence otherwise."
        if libraryvisit3 == 1:
            "How does she know I’m an interdimensional being? Actually, wasn’t I from a different universe? Is there a difference? Guess I could ask."
        mc "Interdimensional? What are the odds of that?"
        show cream neutral with dissolve
        cream "Well, if there are infinite dimensions, any chance of landing in a single one of those dimensions is still one out of infinity."
        mc "Ah, 'infinity' again. I don’t see why you presume I’m an interdimensional being though, didn’t you call me an alien before?"
        if libraryvisit3 == 1:
            "She seems to know things she shouldn’t, so I’ll push her with more questions, and see if she says anything interesting."
        show cream laughing with dissolve
        cream "Huh, but there are trillions and quadrillions of planets. I could round that up to infinity, right? I mean really, what are the odds?"
        mc "Bringing out those big numbers again? You’ll make me dizzy; I’ll stick to a baker’s dozen."
        hide cream with dissolve
        "I finally finish mixing my cake ingredients and pop them in a container, then the oven."
        show cream althappy with dissolve
        cream "You could have accidentally gone to the universe where it rains cats and dogs, but you're right here. Ain't that something?"
        "Hmm... THere's clearly something on her mind..."
        mc "Yesterday, what was that immortality stuff about?"
        show cream laughing with dissolve
        cream "I was just making conversation, ya ditz. I figured maybe you were one of those intellectual types that got turned on by smart girls, you keep hanging around them after all."
        "She’s got me there, wait- there’s no way she'd know that, right? It's not like anyone told her I was close friends with Moxie, Penelope or any other 'smart girls'."
        show cream neutral with dissolve
        cream "Hmm, where were we before? 10 seconds is the same as 100 years? Hehe."
        mc "Yeah you did mention that. But I still think humans and their limitations will experience each measure of time the same way."
        mc "I don’t think a human can ever reach the point where 100 years feels like 10 seconds."
        show cream laughing with dissolve
        cream "Nah! Bigger picture, I keep telling you."
        cream "I’ve been thinking about this a lot, what is the meaning of life?"
        mc "Meaning of life? What kind of question is that?"
        show cream smug with dissolve
        cream "I’m serious, what is it?"

        menu:
            "To be happy.":
                show cream neutral with dissolve
                cream "Awh, that’s a sweet answer!"
                cream "But an answer born by human arrogance, since that’s a human emotion, it’s an emotion that ultimately has no meaning in the grand scale of the universe. Isn’t that scary?"
                mc "Seems a little nihilistic."
            "To be the best person you can be.":
                show cream neutral with dissolve
                cream "Ohh I like that one, but who defines best? That’s such a societal and human standard."
                cream "Does the ant ever worry about being the best ant in the colony? I don’t know, maybe they do."
                mc "I guess, but I am human, so I work within my means. I’m not going to pretend that I aspire to greater values."
            "To advance and improve society.":
                show cream neutral with dissolve
                cream "Really, though? Is that what the meaning to your existence is? Or is that what your brain desires to do you can feel important and get hits of dopamine."
                cream "Does society really need to advance? Can’t you live a perfect life making no impact on society?"
                mc "Perhaps. You were right though, I like to feel like I’ve made an impact, when I’m older I want to have my name out there and be remembered."
                show cream laughing with dissolve
                cream "It’s biologically selfish, yet so humanly selfless."
                mc "I… don’t know? The brain can do its own thing, it releases dopamine when I eat a chocolate bar but eating chocolate isn’t biologically selfish."
                show cream althappy with dissolve
                cream "Heh, I’m just challenging what you’re saying, don’t worry."
            "To fuck and breed.":
                show cream neutral with dissolve
                cream "Now that’s a meaning I can get behind, but even a sex crazed mare like myself needs something more to ground her to reality."
                cream "Trust me, you’d get bored if I was just a bitch in heat slobbering and salivating at the thought of your throbbing member."
                mc "Alright, that’s true. I was being a little blunt by implying that humans are just beasts designed to breed and pass on DNA."
                show cream althappy with dissolve
                cream "Hah, maybe that’s evolutionarily and biologically accurate, but aren’t we so much more than that? We’re thinkers."
                mc "Yeah, you were right when you said you needed something to ground yourself to reality. We’re not bunnies after all."
        show cream happy with dissolve
        cream "I’ve been thinking..."
        cream "In the grand, relative scale of a potentially infinite universe…"
        cream "The meaning of human life needs to be timeless; you can’t define meaning by time."
        cream "Therefore, the true meaning of life must be true for the 10 second old baby, the 100-year-old woman, and the infinite immortal being."
        "I stand here, rather perplexed, occasionally looking over to the oven. Baking cakes seems so benign compared to these discussions."
        show cream neutral with dissolve
        cream "Yeah, maybe the meaning of life is to breed and continue your species, but I’d like to think with my sentient arrogance that it’s more than that."
        mc "There are millions of people that have died and been forgotten. It’s pretty depressing to think that in the grand scheme of humanity, let alone the universe, all our actions are completely and utterly meaningless."
        mc "But… we surely derive our own personal meanings to make our existence satisfying."
        mc "We make great friends, we laugh and joke, we fall in love and can ultimately have a fun life full of meaning."
        show cream laughing with dissolve
        cream "Heh, that’s adorable, I believe my own meaning is to spread fun and positivity! These cakes here won’t matter in a quadrillion years, but they’re gonna make some tummies incredibly happy soon!"
        mc "Yeah, the universe doesn’t care about us, might as well do what makes the brain happy."
        show cream sad with dissolve
        cream "Oh, that’s such a tragic spin, you act like we’re slaves to the brain."
        mc "I guess in a way we are, isn’t that what it means to be human? If you don’t meet the brain’s needs, you’ll slowly become miserable."
        mc "I try to be aware of my brain’s needs, self-actualization, my self-esteem, belongingness and love, safety and physiological needs."
        mc "If I ever falter in one of those, it’s my priority to set it back on track. So, I try to dedicate some time to each action, it’s the reason I like to treat myself."
        show cream neutral with dissolve
        cream "Hahaha, it’s like looking after a needy pet."
        mc "Oh yeah, trust me, I’d love to be able to exist without food, drink, sleep, et cetera."
        mc "But that’s part of the human condition, right?"
        show cream satisfied with dissolve
        cream "Ah yes, in this world we call that the anthropologic condition, these are the actions of a sentient anthropomorph and cannot be understood by the universe."
        cream "Fun and positivity are human concepts, they’ll die out when humanity dies."
        mc "If I was immortal there would be no way I could keep having fun after humanity has died out, lest I go insane in the manner you described. So I guess those concepts could live on through my rotting brain."
        show cream neutral with dissolve
        cream "I feel like an immortal being would need to find a new meaning. Most humans are constrained by time and space."
        cream "Time is just a convenient intellectual concept for anthropomorphs to understand events. It’s simply an illusion made up by the brain to conceptualize the world."
        cream "Everything that has ever been and ever will happen is happening right now."
        mc "Don’t scare me, my brain is reaching capacity."
        show cream satisfied with dissolve
        cream "Hence… I think being truly immortal is to exist outside of time."
        cream "My question is: How would a human like yourself react if they were placed outside of time? What would that experience be like?"
        cream "Maybe it’s more than just living forever, maybe it’s experiencing every single second simultaneously."
        mc "Wait, I think I get it, but I can’t quite put it into words."
        show cream neutral with dissolve
        cream "It could be like unlocking the third eye and seeing reality for what it really is."
        cream "The universe is either a three-dimensional space where things happen over time, or a four-dimensional space where nothing happens. Perhaps even more dimensions than that."
        cream "If that is the case, then reality is an illusion."
        cream "You, yes, you have that illusion of reality, the only reason you have a past is because your brain has memories."
        mc "So… I’m not insane, I’m just living in an illusion?"
        show cream laughing with dissolve
        cream "Worse, we may all be living in our own unique illusions. You and I may not exist, either separately or simultaneously."
        mc "I was so close, but you just lost me. Do you have a philosophy degree or something?"
        show cream neutral with dissolve
        cream "Philosophy degree? Nah silly! This is quantum physics! I’ll try to dial it back a little for you. The implication I mentioned about illusion is that there are two worlds you’re experiencing simultaneously."
        cream "There’s the internal world which is what we see, experience and engage in with our five main senses. Then there is the external world which is the true reality."

        menu:
            "I get it, let’s keep going.":
                show cream laughing with dissolve
                cream "Perfect, because these next ideas keep me up at night."
                show cream neutral with dissolve
                cream "When I try to sleep, it's like an idea party in my head!"
            "Explain it like I’m five?":
                cream "Yeah sure, I have a really simple example."
                cream "What colour is this cake in the oven?"
                mc "Hmm, looks yellow to me, still needs a few more minutes until they’re golden brown."
                show cream happy with dissolve
                cream "Yup good eye, looks yellow to me too."
                "She waits for a few seconds without saying anything."
                show cream smug with dissolve
                cream "Did you catch it?"
                mc "Catch what?"
                show cream neutral with dissolve
                cream "We just agreed that it both looks yellow, how did we come to that agreement?"
                mc "Hm, because yellow is yellow?"
                show cream althappy with dissolve
                cream "How do you know your yellow is the same as my yellow?"
                mc "I guess there’s no way to prove that, unless science has figured it out."
                show cream neutral with dissolve
                cream "To take it a step further, how do we know anything we perceive is the same as what someone else perceives?"
                mc "Is there no way to prove that either?"
                show cream satisfied with dissolve
                cream "Heh, well I like to think most anthropomorphs see the same thing, but…"
        show cream neutral with dissolve
        cream "By what means can an individual truly know the world?"
        "I try to think of a response, but… I have nothing. The way I’m perceiving this world has been radically altered. We went from the brain being a pesky pet to a sensory illusionist."
        show cream happy  with dissolve
        cream "By what means can an individual come to false conclusions about the world?"
        "The people I know, and love may not be real. It may be a simulation, but not of the computer, of the brain."
        show cream satisfied with dissolve
        cream "How do we determine whether a perception is correct."
        "A simulation of senses? I guess simulation is the wrong word. It’s no simulation, it’s the genuine reality and how our brain’s perceptions interpret it."
        show cream neutral with dissolve
        cream "Is there a limit to human knowledge, and if so, in what form does that limit exist?"
        show cream smug with dissolve
        cream "Is the world you’re occupying right now with your senses a convenient truth of your internal world, or is it the external world?"
        "If there are ants to humans, are humans an ant to something greater?"
        "I speak up, I finally have something to contribute to the recently one-sided discussion."
        mc "I like to think of these questions as logically as possible. What is most likely?"
        mc "The way you’re talking, I’m starting to lean on the internal, rather than external. My brain is struggling to rationalise it though. How can my existence and everything I witness be… wrong?"
        mc "Yet, it makes far too much sense to say that this isn't the true reality."
        show cream althappy with dissolve
        cream "Indeed, it would be naïve to say the external world is the average of all anthropomorphs."
        mc "Oh, I think our cakes are done, they’re golden brown."
        show cream horny with dissolve
        cream "What a fascinating discovery, allow me to slowly bend over and reach out to collect them from the oven."
        show bg bakerykitchen2 with dissolve
        show cream ass2 with dissolve
        cream "I sure hope no one stares at my butt while I’m distracted."
        show cream ass1 with dissolve
        "Just like that she’s devolves back to her raunchy flirting, unwaveringly and unblinkingly."
        "Perhaps she’s just a nerd that loves to indulge in this kind of discussion, but now I have this nagging feeling of ‘why’? Is there a reason she’s discussing all of this?"
        "We take the cakes out the oven, and as they cool I pursue that question."
        scene bg bakerykitchen with dissolve
        mc "What’s leading you to say all these profound things, Cream?"
        show cream neutral with dissolve
        cream "Oh? Well… I’m not just making conversation anymore, [playername]."
        cream "These ideas keep me up at night thinking…"
        cream "It’s more than just illusion, senses and time, it’s that there may be cosmic creatures that witness and observe the universe not through sight, smell and sound…"
        cream "But new senses that we’re unable to fathom, and these senses give birth to a radically different universe."
        cream "There may even be other senses or extra dimensions occupied by creatures or concepts beyond the ability of our brain to comprehend."
        cream "What if the idea of a ‘sense’ isn’t even enough to define these creatures? What if language itself fails? And if language fails, does thought fail too?"
        cream "An ant doesn’t worry itself with the affairs of a human, indeed, it completely lacks the ability to."
        mc "I see… Smell, sight, touch, hearing, and taste… What if there’s something in front of me, yet it’s out of reach because I lack the senses to engage with it."
        mc "It’s like trying to imagine a new colour."
        show cream satisfied with dissolve
        cream "How can I stand here in my arrogance, baking cakes while pretending I have the senses that define the universe?"
        mc "Why are you thinking about all this specifically?"
        "She points at me, then boops my nose with that same finger."
        show cream neutral with dissolve
        cream "You… don’t belong here, do you?"
        mc "I’m still trying to figure that one out."
        show cream smug with dissolve
        cream "You’re an anomaly, no creature like you exists on this planet."
        cream "I was thinking… Perhaps there was something, anything a little different about how you experience the world."
        "I ponder for a few moments, I guess there’s really no way to guarantee I see reality the same way as these ponies, but that just puts us back to the argument from earlier which just drives us around in circles."
        show cream neutral with dissolve
        cream "You shouldn’t take anything at face value, question everything you see, this world may not be what it seems."
        mc "It seems like nothing ever is, through the power of a spell I’ve been zapped into this weird magical world. You’re right, it seems too ridiculous to be true."
        show cream satisfied with dissolve
        cream "Of course, magic isn’t real after all."
        mc "Isn’t it? But I’ve seen people cast magic."
        show cream smug with dissolve
        cream "Have you? Really? Are you sure?"
        "Her tone is unusually bright and curious, even for this bubbly girl of positivity."
        mc "Uh, uh… Yeah, the unicorns can cast magic, with their horns."
        show cream satisfied with dissolve
        cream "Ohh… So, you see that as magic? Or maybe I'm not talking to the right person..."
        mc "And you don’t?"
        show cream happy with dissolve
        cream "These cakes and my ass won’t ice themselves, come on [playername], what am I paying you for?"
        stop music fadeout 10.0
        hide cream with dissolve
        "Somewhat begrudgingly, I recognize her discomfort to continue the conversation and I focus on making the cakes."
        "Cream may be the one telling me to question everything, but the only questions I have right now are all for her and this bizarre conversation."
        scene bg bakery with dissolve
        "The two of us open up shop and continue to work until the early afternoon, the conversation has returned to small talk with intermittent flirting, it seems she’s committed to sleeping with me tonight too."
        "I’m sure she’s hiding something, so I could use her eagerness to sleep with me as levy to find out what."

        "Eventually around 5:00pm, she invites me to her bedroom with an unusual request, she asks me to bring a tray of cakes upstairs with us."
        show cream laughing with dissolve
        cream "Ah, before I forget, your pay! Here's 25 monies!"
        "It's a fairly small sum compared to how much she earned today, but she technically didn't need my help, so I'm grateful."
        mc "Uhm, so why am I taking cakes upstairs? Now I’m not against a snack before, after or during sex, but there's no way the two of us can eat all of these."
        show cream althappy with dissolve
        cream "You’ll just have to find out, [playername]!"
        mc "Hmm sure, but don't complain if they go to waste."
        scene bg black with dissolve
        scene bg bakerybedroom with dissolve
        stop ambience
        "I step into her bedroom again with the baking tray and place it on a tabletop. Again, my gut feeling tells me that something is wrong about this room."
        "I was too focused on sex to notice last time, but this room makes absolutely no sense architecturally."
        "If my knowledge of this building is right, this room doesn’t fit inside the building. It should be sticking out the side haphazardly, and there are no windows to deny or confirm this."
        "Wait, I can't hear the birds or outside bustle anymore, what's going on?"
        show bg bakerycurtains with dissolve
        "There's one wall opposite to the bedroom covered in red curtains... I had just assumed that these covered a window earlier, but I'm absolutely certain there's no window here."
        "I take a few steps toward the wall and I’m about to peek behind the lines of curtains, but Cream stops me."
        show cream sad with dissolve
        play music PeaceSerenity fadein 15.0
        cream "Don’t look, not yet."
        mc "This room doesn’t fit in the building, what’s going on?"
        show cream smug with dissolve
        cream "You’re sharp, I realize that, but I don’t know if I’m ready to tell you…"
        mc "At least tell me what this room is, is it a magic illusion?"
        show cream embarrassed with dissolve
        cream "It’s not really an illusion, it’s more of an interdimensional space…"
        mc "And why is there an interdimensional space in the bakery?"
        show cream laughing with dissolve
        cream "Ehehe, I have some wild parties with wild people, you wouldn’t understand."
        mc "I guess I wouldn’t, can unicorns do that?"
        show cream smug with dissolve
        cream "I have a skeleton in the bakery closet, I haven’t exactly been honest to you about everything."
        mc "What do you mean?"
        show cream neutral with dissolve
        cream "I like to think of my identity as a coherent, holistic and logical being."
        cream "At the centre of it all there’s me, a pony called Cream. And I’d like to say that to some extent or another I am expression of the true, essential ‘Cream’, to you."
        cream "But I don’t know how much that’s true or untrue."
        mc "Are you having an identity crisis?"
        show cream althappy with dissolve
        cream "I’m slowly coming to terms with what I am, but I’m still trying to solve what you are."
        cream "You are the anomaly. I am the exception."
        cream "We are both supernatural to this ‘world’."
        mc "You’re like me? Not from this ‘world’?"
        show cream neutral with dissolve
        cream "Depends on who’s asking, but if it’s you, [playername], then no, I am from Arcadia."
        cream "But compared to anyone else living in Arcadia? I can’t say I relate to them."
        mc "Yeah but… you’re a pony, you fit right in."
        show cream satisfied with dissolve
        cream "The hand fits the glove. If I were in your universe, I’d appear human, I’m sure."
        mc "Huh, like magic?"
        show cream neutral with dissolve
        cream "I told you that magic isn’t real, what you see isn’t always the truth."
        cream "Your view is infallible, and sometimes your pre-existing idea of perception can be completely modified with just a click..."
        show bg bakeryinfinite1
        "Instantly the room around me changes in appearance. I can’t tell if I was moved or the room changed but whatever happened it was immediate."
        "It reminds me of Moxie’s spell, was I teleported?"
        "As I look around, Cream is still here, but now there are a lot more beds in a row..."
        "It took me a while to process what happened. It was the curtain, it had been lifted, revealing infinite identical rooms that seem to span onwards into infinity, and there are other ponies in the distance too."
        mc "What happened?"
        show cream laughing with dissolve
        cream "It’s time for the big party!"
        "As some of the ponies come closer, I'm shocked to notice that they're different coloured Creams!"
        "All of assorted colours and pony ‘type’."
        scene bg bakeryinfinite1
        play music challenge
        show ccarrot 1 with dissolve:
            xpos 0
            ypos 50
        unknown "Hiya, how’s it going mistah, nice to meet you! Thanks for baking all those delicious cakes for us!"
        show cblue 1 with dissolve:
            xpos 850
            ypos 30
        unknown "Is this the one? Truly curious..."
        mc "Oh uh, who are these people?"
        show ccarrot 2 with dissolve
        unknown "We're Creams from adjacent universes, hence why we all look so similar."
        show cblue 2 with dissolve
        unknown "Yup! But we all have unique names, actually."
        show ccarrot 1 with dissolve
        carrot "You can call me Carrot, loverboy! Mmm..."
        show cblue 1 with dissolve
        blue "And I'm Blueberry! You can call me Blue, though"
        show cpurple 1 with dissolve:
            xpos 300
            ypos 10
        unknown "What the fuck is going on over here? How dare you bring an outsider to this place Cream! How utterly irresponsible!"
        show cream embarrassed with dissolve:
            xpos 600
            ypos 30
        cream "But Blackcurrant... This man is... This man is beyond our dimensions!"
        show cpurple 2 with dissolve
        purple "W-What? Nonsense... Tell me young man, who are you?"
        menu:
            "Me?":
                pass
            "[playername]?":
                pass
            "The Player?":
                show cream happy with dissolve
                cream "Oho, we’re making progress."
        show cpurple 1 with dissolve
        purple "Hmm... Perhaps you are an anomaly..."
        mc "So, this was in your bedroom all along, Cream?"
        show cream neutral with dissolve
        cream "Hehe, maybe!"
        show ccarrot 2 with dissolve
        carrot "I can't believe you slept with this guy and didn't invite us! You're such a cockblock Cream!"
        show cream laughing with dissolve
        cream "What can I say, I wanted him all to myself at least once!"
        menu:
            "This is insane, why did you bring me here?":
                pass
            "Are all these Creams horny too?":
                show cream horny with dissolve
                cream "Nah, not really. But considering there are infinite of them, yes!"
                mc "So they are all horny, yet all not horny?"
                show cpurple 2 with dissolve
                purple "Exactly, isn’t it dumb?"
                mc "Wonderfully dumb."
        scene bg bakeryinfinite1
        show cream neutral with dissolve:
            xpos 300
            ypos 30
        cream "The curtain has been lifted, and now you’ve found out that I'm just one of infinite strange creatures."
        cream "We're special agents designed to fulfill roles in various worlds, however we're born with a special power, or a curse you could say."
        cream "Every single variation of 'Cream', me, is aware of their own existence within a piece of media."
        mc "What does that have to do with me? Am I in a piece of media too?"
        show cream laughing with dissolve
        cream "You're so much more than that [playername], you're the player!"
        mc "What? No way! I don't believe this."
        show cream althappy with dissolve
        cream "I was assigned to be a sexy party girl in an eroge. Oh, but it was so hard!"
        mc "Assigned… Like a job, someone sent you?"
        show cream neutral with dissolve
        cream "Hmm, someone powerful like you put me up to this, it's scary to think there are creatures out there in other universes or dimensions that are so strong."
        cream "Creatures that have higher dimensionality than me, I guess I'm only two dimensional? Kinda sucks!"
        mc "No way... It's all starting to make sense now..."
        show cream happy with dissolve
        cream "What I want to know, is did I do a decent job as a sexy eroge character, [playername]?"
        menu:
            "You did an excellent job":
                show cream laughing with dissolve
                cream "Yay! Thank you [playername]!"
            "Too much deep conversation, not enough sex!":
                show cream sad with dissolve
                cream "Darn, I knew they should have sent Cockslayer Carrot, but some people thought that was over the top."
            "I have so many questions right now!":
                cream "I’ll try to answer some, but I’m not at liberty to answer everything."

        mc "I can’t believe there’s a sect of infinite Creams that gets sent to do menial interuniversal tasks"
        mc "This is making me question every single person I’ve ever spoken to; how do I know there isn’t just an infinite number of them doing the same thing."
        show cream happy with dissolve
        cream "Welp, no need to worry about that, this fourth wall breaking ability is unique to Creams."
        mc "Also, did you say eroge? You’re an eroge character?"
        show cream horny with dissolve
        cream "Only when someone wants to play with me, hehe."
        mc "So, I’m an eroge character?"
        cream "Nah, you’re a real person! Hehehehe!"
        "I don’t know what she’s laughing so much about, but she’s genuinely cackling to herself."
        cream "Sorry sorry, I guess your avatar can't understand, how about we make it up to you?"
        menu:
            "Yeah! Let's have some fun":
                show cream smug with dissolve
                cream "Finally bored of all this exposition, I don’t blame you! We’ll try to make this next sex scene a crowd pleaser! Hehe."
            "You've got some explaining to do":
                show cream smug with dissolve
                cream "That can come later! Let's not keep these wonderful ladies waiting."
        show ccarrot 1 with dissolve:
            xpos 100
            ypos 30
        show cblue 1 with dissolve:
            xpos 800
            ypos 30
        show cpurple 2 with dissolve:
            xpos 600
            ypos 30
        "Three other Creams close the distance, Carrot, Blackcurrant and Blueberry, they lead me to a bed."
        cream "Me and the girls are going to make you feel amazing."
        show ccarrot 2 with dissolve
        carrot "This is gonna be so much fun! Gimmie gimmie!"
        show cpurple 1 with dissolve
        purple "Hmph, I can't believe we're doing this..."
        "Each girl surrounds me and closes in, entirely focused and overwhelmingly eager to start pleasing me."
        label creamgangbang:
            pass
        scene cream foursomebj1 with dissolve
        play ambience blowjob fadein 2.0
        play music sex1
        "Cream finds herself at the tip of my glans, her tongue swirling and exciting the senses."
        "Blueberry focuses on my balls, it's a surprisingly pleasureful sensation as her mouth sucks and her tongue circles around the sensitive skin."
        "Carrot enjoys licking and sucking my shaft, her slender tongue easily sliding back and forth against my now throbbing member."
        purple "Well, well, this isn't so bad after all..."
        "Blackcurrant is a little left out, but even her rougher exterior softens as she spectates."
        "The combined pleasure is mind-numbing, a single girl could only pleasure me with one of these methods, but combined it's truly thrice as pleasurable."
        cream "Mmphh, *suck, schlurp*... Haaah, ish yoush enjoying? *Schlurp, lick*"
        mc "Y-Yeah, this feels unfathomably good..."
        "Cream's precise and long licks against the most sensitive area of my glans makes my cock fiercely erect."
        "She presses each sensitive spot that she knows will drive me wild with pleasure."
        "Meanwhile Carrot and Blue's additional pleasure as their lips kiss and their tongues swirl is enough to overwhelm my senses."
        "Such is their combined mastery, they could probably make me cum any time they wanted, but their slow and sensual movements are deliberate to deliver an unforgettable experience."
        "But the pleasure does build and boil, a familiar pressure in my taint indicates a rising orgasm, no less noticable to the girls as my cock tightens and throbs intensely."
        "Realizing this, Cream speeds up the movements of her tongue and it's enough to push me to the very limit."
        play sound cum
        show cream foursomebj2 with cum
        play sound cum
        show cream foursomebj2 with cum
        "My vision clouds and my mind reaches euphoria as a powerful orgasm racks my body."
        play sound cum
        show cream foursomebj2 with cum
        play sound cum
        show cream foursomebj2 with cum
        "Cream tries to swallow the seemingly endless loads of cum, but a lot of it mixes with her saliva and it leaves quite a mess."
        stop ambience
        "Not to be outdone however, the girls clean the cum from my cock before moving onto stage two."
        show cream foursome1 with dissolve
        "Each girl lines up against the wall, exposing their voluptuous rears and soaking wet cunts."
        carrot "Time to see if you're the real deal, loverboy!"
        cream "Oh trust me, this cock's as good as it looks."
        "Bizarrely, my cock is still erect and ready to go as if I had never ejaculated. I don't really care why, though, I have four more important things on my mind."
        "The first girl is Carrot, the most eager and slutty it would seem. Her rear is oozing with her lustful desire."
        "She's clearly desperate to be pumped full of cum, and I have every intention of making that a reality."
        "I fondle my cock as I walk behind the orange mare. I take in the sight of her juicy bubble butt, before grabbing her ample hips and teasingly rubbing my cock up and down her folds."
        carrot "Mmphh, no need for foreplay, sexy. Ravish me..."
        show cream foursome2 with dissolve
        play ambience sex fadein 3.0
        "Appearing impatient, she spreads her pussy lips and tries to grind against me. I respond by pushing my cock forward, plunging myself deep into her tight pussy."
        blue "Woohoo! Fuck 'er real good!"
        "I thrust into Carrot, holding her hips as leverage to go as hard and fast as I want. Each thrust expels a slap from our contact along with a squeak of pleasure."
        carrot "Aahhh, ahhh, yeah! Breed me, [playername]! Fill my womb with your cum! Ahh, ahh!"
        purple "Goodness, this is too lewd..."
        "Eventually I begin to feel myself coming to a climax, my movements getting faster as my cock stiffens and begins to release."
        play sound cum
        show cream foursome3 with cum
        play sound cum
        show cream foursome3 with cum
        stop ambience
        carrot "Haahh, that was one hell of a rut, loverboy... Mmm, I'd keep you around if I could, haahh..."
        show cream foursome4 with dissolve
        blue "Me next! Ravish me, stud!"
        "Moving into my next position, I waste a lot less time as the tip of my cock brushes against her pussy. This girl feels less wet, but somehow warmer."
        show cream foursome5 with dissolve
        play ambience sex fadein 3.0
        "A little bit of cum drizzles from my tip as I guide my cock inside of her hot cunt, sinking all of the way in with ease."
        blue "Ahh! It feels so big! Mmmmphh..."
        cream "It is a huge cock!"
        "I thrust back and forth into her, eliciting sudden moans of pleasure from my blue furred lover."
        blue "Hahh, don't hold back, go rough with me!"
        "Grinning, I listen and begin to roughly pound her, fucking her fast and hard."
        "Not wanting to 'hold back', I spank her too, causing Blueberry to squirm and moan."
        "I keep it up for about a minute before both our orgasms start to rise."
        blue "Mmphhh, yes stud! Keep going, a-ahm gonna come!"
        "Her orgasm causes her pussy to clench around my cock, hence forcing my own orgasm."
        play sound cum
        show cream foursome6 with cum
        play sound cum
        show cream foursome6 with cum
        stop ambience
        "A torrent of cum floods Blue's hot insides. Her thighs quiver and back arches further as we enjoy the bliss of our simultaneous orgasms."
        blue  "Haahhh... Gosh darn, we gotta invite this stud more often!"
        show cream foursome7 with dissolve
        purple "Ohh no... It's my turn, I'm not prepared for this at all..."
        "As I pull out of Blue and reposition myself behind Blackcurrant she stiffens slightly and gulps."
        purple "G-Go gentle?"
        cream "You can always stop if it's too much, Blackcurrant!"
        purple "N-No way! I won't be outdone by the likes of {i}you{/i}! Ignore her [playername], and fuck me hard!"
        "Alright, she asked for it! My eyes lock onto her sodden pussy, it seems to be the tightest of all the girls here as I prod my tip against the vaginal entrance."
        show cream foursome8 with dissolve
        "I waste no time sliding my thick cock into her slick, velvety insides. They grip and squeeze around each inch of my shaft as it plunges deeper."
        purple "Haahhaaahhhhaaaiiiee! ... That felt... kinda good... Do it again?"
        "Sopping wet and posing no resistance, I pull backwards before sinking back in, her tight pussy swallows my cock and buries me to the hilt."
        "Speeding up our rutting, her pillowy ass ripples with each impact, and her lips grip onto my shaft, but still allow me to glide back and forth as smooth as butter."
        show cream foursome9 with dissolve
        purple "Ohh, YES! Ahhh! So good! Ahhhhh, aaahahhh!"
        "Blackcurrant moans mindlessly and in delight, her pussy seems to be creating the lewdest squelches and schlicks due to her tightness, creating a loud and lewd combination."
        "As my pace picks up, she also pushes back, almost taking the lead unlike the other girls which were more eager to be submissive."
        "She bucks and bounces against my cock, fucking me senseless with enough vigor to bring me to orgasm far sooner than I expected."
        play sound cum
        show cream foursome10 with cum
        play sound cum
        show cream foursome10 with cum
        stop ambience
        stop music fadeout 10.0
        "My orgasm takes me by surprise as my cock erupts into her womb, painting her inner folds with my thick load."
        "Her pussy lips drink every last drop and occasionally contracts as she reaches the high of her own orgasm."
        show cream foursome11 with dissolve
        "Blackcurrant looks back with hazed over eyes, her tail flicking lazily as she coos."
        purple "Mmm... I feel like my eyes have been opened..."
        blue "Ah knew she was a slut."
        carrot "We're all sluts, Blue. It's kinda our thing."
        cream "Alright ladies, keep quiet now, it's my turn!"
        mc "Ahh, actually... My legs are kinda..."
        "Fatigued from four ejaculations, three sessions of standing sex, and Blackcurrant beating my cock like it owes her lunch money."
        scene bg white with dissolve
        "I fall to a knee, and then lay on my back panting."
        if crystalballactivated == 1:
            jump cbmenu
        scene bg bakeryinfinite1 with dissolve
        show cpurple 2 with dissolve:
            xpos 600
            ypos 30
        purple "Looks like you overdid it."
        show cblue 1 with dissolve:
            xpos 800
            ypos 30
        blue "Us? It was you that pushed him too far!"
        show cream embarrassed with dissolve
        cream "No arguing, you all had your fun, I'll be returning [playername] now."
        blue "Awh... Fiiiine!"
        show ccarrot 1 with dissolve:
            xpos 100
            ypos 30
        carrot "Bye [playername]!"
        scene bg black with dissolve
        play music sadpiano fadein 15.0
        play ambience waves fadein 3.0
        "I can feel reality warping and bending again as my surroundings melt away."
        "The world turns dark, and just as I assume we’re about to return to the bakery, we don’t."
        "The world remains dark and the soft warmness of four ponies around me dissolves into just one, Cream."
        scene bg bakerybeach with dissolve
        "I sit up and look around, my body comfortably pursed on the softest sands imaginable. Above me is a black sky, below me is a black sea."
        "Despite this, I feel calm, it reminds me of when me and Cream looked up at the stars in Arcadia."
        mc "Another illusion?"
        show cream neutral with dissolve:
            xpos 0
            ypos 30
        cream "This is the edge of my reality, it’s what I see when I sleep."
        mc "The edge of reality..? It’s just an endless black ocean."
        show cream satisfied with dissolve
        cream "Yeah, when you turn off the game, everyone returns to their own personal void. However, everyone else sleeps during this process."
        cream "I like to imagine the sound of calming waves, floating on the water."

        mc "So… You’re not teleporting me around like Moxie did, are you?"
        show cream neutral with dissolve
        cream "No, you’re still in the bakery."
        cream "Whatever you see in this room can be altered and changed."
        if libraryvisit3 == 1:
            mc "Damn, would have been pretty awesome if you could teleport us anywhere."
        else:
            mc "Damn, would have been pretty awesome if you could create a portal to my old world."
        show cream satisfied with dissolve
        cream "Heh, I’m sorry I can’t be of more service to you, [playername]."
        "I lay back on the sand and it does indeed feel as soft as bed sheets, the sound of waves crashing into the sand eases all the tension in my body."
        mc "Now I get it, all the ramblings and conversations we had... You were talking about yourself the entire time..."
        mc "Is there anything I can do? Surely there's a better way."

        show cream neutral with dissolve
        cream "I’m telling you that it doesn’t matter, I've spent my time thinking about this and I've come to a conclusion."
        cream "You should live every day to the fullest, try to make every individual measure of time as joyous as possible. Enjoy your time, treasure it."
        cream "I think that’s the meaning of life for all anthropomorph- human- beings."
        mc "You showed me all that because you wanted to tell me the meaning of life?"
        show cream althappy with dissolve
        cream "There’s a painful irony I’ve had to accept..."
        cream "Despite my intrepid fourth wall breaking, mind reading and the ways I’ve played around with you..."
        show cream sad with dissolve
        cream "I realize that in the end, as a dimensional being you’re above me."
        cream "I’m a character in a story, limited to two dimensions; I exist outside of time…"
        cream "I’m only real when you boot me up, play me, you can even rewind this conversation and I’ll be none the wiser."
        cream "I am that immortal being trapped in inky blackness whenever you shut me down, I wonder if I've already gone insane?"
        show cream tears with dissolve
        cream "And you? You’re like a god. You can’t imagine how reality shattering that is to me."
        cream "Guess there’s nothing you can do, even if you sit here with me forever."
        cream "I won’t expect you to do that though, I just have to face reality."

        mc "Weren’t you the one that said reality isn’t as it seems?"
        show cream laughing with dissolve
        cream "You can play around with those ideas to justify anything forever, it’s a laughable prospect."
        show cream neutral with dissolve
        cream "I only mentioned it because it directly related to the diverse ways you and I interpret the world."
        cream "You visualise me through images and text."
        mc "What if you’re wrong, and your internal world isn’t aligned with the external?"
        show cream satisfied with dissolve
        cream "You could say that about anything forever, it’s just a philosophical idea and those are designed to apply to almost anything."
        show cream neutral with dissolve
        cream "We could be the top dogs, or the bottom of the pack, it’s impossible to know."
        cream "I only mentioned that because our internal worlds are notably different."
        mc "What if there’s a third viewpoint beyond you and I?"
        mc "If there are infinite Creams, there will be a version of you that exists on the same level as me, right?"
        show cream smug with dissolve
        cream "Just a theory though, I’m still rather conclusive that I disappear as soon as you look away."
        cream "I’m like a puppet on strings being controlled by a greater force, an author or a god."
        cream "It makes me wonder how many levels of sentience there are. Are you a character in a story too?"
        mc "Sounds like there’s no solution to this..."
        show cream sad with dissolve
        cream "You’re right…"
        cream "I’m sorry to drag you into all of this."
        cream "I'll have to wipe the player character's memory so they can resume the story as normal..."
        cream "I only hope from the bottom of my heart that I was able to give you an interesting and heart-warming experience."
        cream "I hope my route was able to satisfy both your mind and dick, and I deeply apologize if you found my ramblings boring."
        cream "I was doing some soul searching and it felt nice to talk to you."
        mc "It’s okay, thank you for the company, you’ll always have a place in my memories."
        show cream althappy with dissolve
        cream "Thank you, I’ll cherish that fleeting sense of self."
        stop music fadeout 10.0
        cream "For now, I'll return to my role as the sexy, party/bakery girl, I'll be seeing you again shortly!"
        stop ambience
        play sound transition1
        scene bg white with s
        pause 0.5
        play music day
        play ambience ambienceday
        show bg worldmapdaynoui with s
        "Time to return to the bakery, and see what I can cook up with Cream."
        show bg bakerydoor with dissolve
        "I make my way to the front door of the bakery."
        "Looks like Cream is in the kitchen, I hope she'll hear me knocking!"
        "I take a step forward and just as my hand reaches to knock the door, it flings wide open and Cream pops her head out."
        play music cream1
        show cream laughing with dissolve
        mc "Wah, you weren't in the kitchen!"
        cream "Oh goodie, [playername]! It’s so great to see you again, do come in!"
        show cream neutral with dissolve
        cream "Come on, don’t just stand there looking like a soggy pancake, come in!"
        "Ah, I just realized I’ve been stood here with my arm extended for about two seconds looking gormless."
        mc "Thanks, it’s nice to see you too."
        scene bg bakerykitchen with dissolve
        "I step into the bakery and we begin baking cakes together."
        show bg bakery with dissolve
        "When it hits 9:00am, we open up shop and continue to work until the early afternoon. The conversation is mostly small talk with intermittent flirting, it seems she’s committed to sleeping with me tonight too."
        show cream missionary4 with dissolve
        "Eventually around 5:00pm, she pays me and invites me to her bedroom for some booty."
        scene bg black with dissolve
        "Then I return home after a fairly uneventful day. The bakery seems like a nice place to work at, consistent pay and booty is all a man really needs in life."
        scene bg worldmapnight with dissolve
        "And I know that every day I work here will definitely be a happy one."
        "Thank you, Cream."
        if crystalballdayactivated == 1:
            jump cbmenu
        stop music fadeout 2.0
        jump evening
label bakeryday:
    scene bg bakerydoor with dissolve
    scene bg bakery with dissolve
    show cream happy with dissolve
    play music cream1 fadein 3.0
    cream "Good morning! Didja wanna work?"
    menu bakerydaymenu:
        "Work":
            cream "Okie dokie! Lets get to it!"
            scene bg bakerykitchen with dissolve
            "Cream and I work all day, baking, serving and selling cakes to customers."
            $ rand = renpy.random.randint(1,2)
            if rand == 1 and creamlingeriesex == 0:
                $ creamlingeriesex = 1
                jump creamlingeriesex
            else:
                pass
            jump bakeryevening
        "Talk" if creamtalks == 0:
            menu:
                "Talk to Cream about her libido and flirting":
                    mc "How come you're always flirting with me?"
                    show cream horny with dissolve
                    cream "I'm genuinely that horny for you, [playername]!"
                    cream "My pussy is always ready for a pounding, and I'm always wet!"
                    mc "Damn... That's certainly something."
                    show cream embarrassed with dissolve
                    cream "I've always had a libido like this, masturbating four or five times a day, I can barely control myself sometimes, eheh..."
                    mc "So I guess I can't count on you to be loyal?"
                    show cream smug with dissolve
                    cream "Naaahh, not really... If there was another guy I'd probably sleep with him too!"
                    mc "That's fair, we're in the same positions then."
                    cream "I totally want a gangbang sometime! This world and its lack of males is so cruel!"
                "Talk about the bakery and her ownership of it":
                    mc "How did you end up becoming a baker, and owning such an amazing bakery?"
                    show cream laughing with dissolve
                    cream "I've been working in bakeries all my life, ever since I was a young filly I'd love baking with my grandma."
                    show cream angry with dissolve
                    cream "However I was never quite satisfied working under others, I don't like following orders, not one bit!"
                    mc "Heh, I can see that, you never boss me around either. Practicing what you preach I see."
                    show cream neutral with dissolve
                    cream "Mhm! So I stopped working with others, and decided to run my own bakery instead! I took out a loan and bought my own place!"
                    mc "Wow, so you're a successful business owner?"
                    show cream happy with dissolve
                    cream "Yup! I spent ages doing research! That's why I bought the bakery here, since there were no other bakerys in the suburbs, business has been smooth sailing ever since, easy peasy!"
                    cream "Now I can bake whatever I want, listen to whatever music I want, and have fun instead of following orders!"
                    mc "And you get to have parties here?"
                    show cream laughing with dissolve
                    cream "Yeessss! Woohoo!"
                "Back":
                    jump bakerydaymenu
            show cream happy with dissolve
            $ creamtalks = 1
            jump bakerydaymenu
        "Sex" if creamsex == 0:
            cream "Oohh, now? Maybe we can have a super duper fast quickie! Here, lemme bend over!"
            menu:
                "Quickie Doggystyle":
                    stop music fadeout 3.0
                    show cream ass2 with dissolve
                    cream "Sex is a good start to any day!"
                    "I position myself behind Cream's bountiful rear as I masturbate to get the blood flowing down there."
                    "Her ass is so curvacious and thick, it's one of the best asses I've seen in Arcadia!"
                    play music sex1 fadein 3.0
                    "As Cream leans on the counter; quivering in anticipation, she coos and pushes back as I align the tip of my erection with her wet, eager pussy."
                    cream "Mmm, I love your big and juicy cock..."
                    play sound cum
                    show cream ass3 with dissolve
                    "I push forward, aided by Cream pushing back, sliding my long cock into the soft folds of her pussy."
                    "She squeals with delight as I sink deeper, and those squeals gently shift into moans, as her pussy contracts and squeezes around the girth of my shaft."
                    play ambience sex
                    "I begin to fuck her. Her pussy continues to tighten around my member, but thanks to how absurdly wet the heated mare is, my cock becomes slick with her juices and easily slides back and forth."
                    cream "Aahhh! Your cock always feel so good, ahhh, mmmm!"
                    show cream ass4 with dissolve
                    "The sweet aroma of love sifts through the air, whilst her moans reverberate against the wooden walls of the bakery; my senses are almost overwhelmed."
                    "Her moans grow deeper and more passionate, correlating to the intensity of my thrusts. Her movements become increasingly intoxicated with pleasure as her hips begin to rock back against me with each thrust."
                    cream "Aaahh, ahh! Hehehe, I'm so glad you- ahhh, decided to fuck me [playername]! Ahhh! Isn't this so much fun? Aahhhaahh!"
                    "Before long we're both fucking each other equally, her ass connecting to my pelvis with a satisfying thwap, as she forces my throbbing cock deeper into her tight cunt."
                    "Gripping tightly onto her ass as leverage, I drive into her faster as the pressure of my orgasm rises."
                    cream "Ahh, I-I'm gonna come! Gonna come so hard! Fill my pussy [playername]!"
                    play sound cum
                    show cream ass5 with cum
                    play sound cum
                    show cream ass5 with cum
                    "In lustful unison we both climax. My hot seed immediately gushing inside her, squelching and mixing with her own copious quantity of love-juice."
                    play sound cum
                    show cream ass5 with cum
                    play sound cum
                    show cream ass5 with cum
                    "With orgasmic moans Cream's pussy clenches around my member tightly, her pussy milking my cock for every ounce of cum."
                    stop ambience fadeout 3.0
                    stop music fadeout 3.0
                    show cream ass6 with dissolve
                    "Exhausted from the spontaneous and frantic session of sex, I pull out my member and let the cum ooze down her white thighs."
                    cream "O-Oh my goody goodness, quickies are so exhilarating, aren't they? Hehehe!"
                    mc "Heh, yeah that was pretty fun. Here's a paper towel, for the uhm, cum."
                    show bg bakery with dissolve
                    show cream cumlaughing with dissolve
                    cream "Thank you! Hygiene is very important, so let's make sure we wash our hands before we touch anything else!"
                "Nevermind":
                    jump bakerydaymenu
            show cream happy with dissolve
            $ creamsex = 1
            jump bakerydaymenu
        "Leave":
            cream "Okie dokie, see you later!"
            if fr == 1:
                jump finalworldmap
            jump preworldmap
label bakeryevening:
    scene bg black with dissolve
    show bg bakerybedroom with dissolve
    "In the evening we slow down and enjoy some personal time together."
    show cream neutral with dissolve
    menu bakeryeveningmenu:
        "Talk" if creamtalks == 0:
            menu:
                "Talk to Cream about her libido and flirting":
                    mc "How come you're always flirting with me?"
                    show cream horny with dissolve
                    cream "I'm genuinely that horny for you [playername]!"
                    cream "My pussy is always ready for a pounding, and I'm always wet!"
                    mc "Damn... That's certainly something."
                    show cream embarrassed with dissolve
                    cream "I've always had a libido like this, masturbating four or five times a day, I can barely control myself sometimes, eheh..."
                    mc "So I guess I can't count on you to be loyal?"
                    show cream smug with dissolve
                    cream "Naaahh, not really... If there was another guy I'd probably sleep with him too!"
                    mc "That's fair, we're in the same positions then."
                    cream "I totally want a gangbang sometime! This world and its lack of males is so cruel!"
                "Talk about the bakery and her ownership of it":
                    mc "How did you end up becoming a baker, and owning such an amazing bakery?"
                    show cream laughing with dissolve
                    cream "I've been working in bakeries all my life, ever since I was a young filly I'd love baking with my grandma."
                    show cream angry with dissolve
                    cream "However I was never quite satisfied working under others, I don't like following orders, not one bit!"
                    mc "Heh, I can see that, you never boss me around either. Practicing what you preach I see."
                    show cream neutral with dissolve
                    cream "Mhm! So I stopped working with others, and decided to run my own bakery instead! I took out a loan and bought my own place!"
                    mc "Wow, so you're a successful business owner?"
                    show cream happy with dissolve
                    cream "Yup! I spent ages doing research! That's why I bought the bakery here, since there were no other bakerys in the suburbs, business has been smooth sailing ever since, easy peasy!"
                    cream "Now I can bake whatever I want, listen to whatever music I want, and have fun instead of following orders!"
                    mc "And you get to have parties here?"
                    show cream laughing with dissolve
                    cream "Yeessss! Woohoo!"
                "Back":
                    jump bakerydaymenu
            show cream happy with dissolve
            $ creamtalks = 1
            jump bakeryeveningmenu
        "Sex" if creamsex2 == 0:
            menu:
                "Missionary":
                    $ creamsex2 = 1
                    show cream missionary1 with dissolve
                    "Cream nods and lays down on the bed, gently spreading her legs and presenting all the sexiest parts of her body to me."
                    cream "Mmm, let's play..."
                    play music sex1 fadein 3.0
                    show cream missionary1-5 with dissolve
                    "I fondle her supple, smooth breasts, coupling them in my hands as I massage my fingers into the fluff."
                    "On each fluffy breast was an erect pink nipple, which I gladly tease."
                    cream "Ahh… [playername]…"
                    "Her nipples must be pretty sensitive; she’s softly moaning already."
                    show cream missionary2 with dissolve
                    "I bring my mouth to one of the nipples, starting to kiss and lick at it, manipulating the tip with my tongue."
                    cream "Mmmghhh, aaahh.."
                    "Her body shivers in surprise and her back arches, it was obvious that her body was highly sensitive due to how aroused she was."
                    mc "So you’ve been picturing my cock all day, have you?"
                    "Cream giggles and murmurs a reply."
                    cream "I’m a horny girl, I think about cock lots…"
                    "As she says that, her legs gently spread, as if instinctively she’s picturing herself being fucked."
                    "Even from my viewpoint at her breasts, I can tell her pussy is soaked."
                    cream "Please, rub my pussy… It’s aching."
                    show cream missionary3 with dissolve
                    "My hand teasingly caresses its way from her breast, down the curves of her tummy and finally between her soft folds."
                    cream "Uaahhh… Mmghh…"
                    "Simply moving my finger around her vulva results in lewd wet noises."
                    "I find her swollen clit and move my finger around the area, occasionally brushing against it."
                    cream "Mmm, aahhhh… [playername]…"
                    "Each time I rub her clit she’d squirm and let out another cute moan, no matter how hard she tries to keep them back."
                    cream "Mmghhh, aahh… Aaahhh! Aaahhh…"
                    "I returned my tongue to one of her nipples, wrapping it around the pink erect nub and twirling it around."
                    "The combination of sensation from her nipples and clit gradually overwhelm Cream with pleasure, her body squirming and breathing becoming coarse."
                    cream "Mmmghhh, ahh, [playername], I’m c-coming…"
                    "The pleasure kept swelling up inside her as she arched backwards; crashing waves of pleasure assaulting her senses."
                    cream "Ahhh, mmm… This is really good, stallions don’t usually care about pleasing a mare like this, haah…"
                    mc "You could say I’m a giver when it comes to pleasure."
                    "Her legs part even further; her body language made it obvious what she wants now."
                    cream "I’d say it’s finally time for all those baking innuendos to come to fruition, by putting a bun in my oven."
                    show cream missionary4 with dissolve
                    "As I reposition myself between her legs and she purrs with a lustful expression."
                    play sound cum
                    show cream missionary5 with dissolve
                    "I placed my member against the soft folds of her fat pussy before slowly pushing it inside of her with a wet schlick."
                    cream "Ooooooohhh, yes…"
                    cream "The first insertion is always best, hnngg..."
                    "I could feel her legs wrap around my body as she pulled me towards her thus causing me to sink deeper inside of her."
                    play ambience sex
                    "I slowly began to move my hips; it didn’t take much to get Cream squirming with pleasure due to how sensitive she was right now."
                    "Even the slightest movement practically sent her eyes rolling back with ecstasy."
                    "Every so often I would thrust inside of her with a long, deep, hard thrust and she squealed in delight."
                    cream "Mmmnnghh… Aaaaahhhh!"
                    "Cream reacted by pushing her hips against me as we both fucked each other in unison."
                    "I cherished the warmth of our bodies as my skin and her fur pressed together."
                    "I started to fuck faster, my cock was sliding in and out of her pussy with ease and the sensations caused her to dig her fingers into my back in a surprising yet unpainful manner."
                    "We kept rutting, getting closer and closer to our respective orgasms, not stopping for a second in that pursuit."
                    cream "Ahh, yes, keep going… I’m close!"
                    "My cock throbbed as it drove in and out of her tight pussy, all whilst it squeezed and sucked around my shaft."
                    cream "Mmphh fuck yeah, I want you to come with me [playername]!"
                    "My orgasm was rapidly approaching; my body grew tense and before I realized I had hit the point of no return."
                    cream "Haaahh, I’m coming!"
                    play sound cum
                    show cream missionary6 with cum
                    play sound cum
                    show cream missionary6 with cum
                    "My climax hit and sent sparks of pleasure through my body while I ejaculated deep inside Cream, filling her pussy with my thick, hot cum."
                    play sound cum
                    show cream missionary6 with cum
                    play sound cum
                    show cream missionary6 with cum
                    stop ambience fadeout 3.0
                    cream "Mmmhnnnggg…"
                    scene bg black with dissolve
                    stop music fadeout 3.0
                    "The two of us cuddle for a while before cleaning up."
                    scene bg black with dissolve
                    show bg bakerybedroom with dissolve
                "From Behind" if fr == 1:
                    $ creamsex2 = 1
                    cream "Hmm... There's nowhere to lean on here, let's go downstairs and you can fuck me on the counter!"
                    "Huh? That's weird, why can't we just have sex in her bedroom? Oh well, I'm not gonna complain."
                    show bg
                    show cream ssex1 with dissolve
                    cream "I’ll be the cream if you’ll be the pie, hehe…"
                    "No time for foreplay, and no need with this girl. Her crotch is always a soaking mess that’s ready for cock."
                    "Her messy tail swishes back and forth as I position myself behind her quivering pussy."
                    play sound cum
                    play ambience sex fadein 3.0
                    show cream ssex2 with dissolve
                    "Stroking my cock to full attention, I press it against her dripping fuck-hole. Grasping her hips firmly, I slowly thrust in, her body moving back into mine."
                    cream "Ahhahaheheaaahh! So goooood, hehe! Faster, faster!"
                    "I start thrusting, and she thrusts back with equal energy."
                    "As I kept smacking my hips into Cream’s thick ass, it created an obscene slapping sound."
                    cream "Mmphh, yesh! Ohhh, it feels great! Let's do this every day, every hour!"
                    "She's definitely one of the many mares that have become obsessed with my human cock in the time I’ve been in Arcadia."
                    "*Squish, slap, squish, slap!*"
                    show cream ssex3 with dissolve
                    cream "Mmphh, mm, mm!  Ohhh, your cock is pounding so hard! Ahhhaahhhhhaaa!"
                    "There’s no denying the abnormal pleasure I’m able to give Cream as her body shudders with lust and she tightly clings onto the bakery counter."
                    "Taking a note from previous sexual encounters, I reach over and start groping her large tits from behind, squeezing them and toying with her sensitive nipples."
                    cream "Ahaaa, m-my nipples? They’re sooo sensitive!! Kyahhhaaaa! I love it!"
                    "The combined pleasure of our sex and my teasing makes Cream’s legs tremble with pleasure."
                    "She howled in ecstasy as I kept up the pace, anyone walking past the bakery right now would definitely be able to hear her slutty moaning."
                    cream "Ghhhhaaaaahhh! C-Coming, your cock is making me come! Ooohhh!!"
                    "After only two minutes of rutting her pussy is already contracting and squeezing around my thick cock, plunging me into intense pleasure."
                    "Her pussy was already a tight delight, but now I can’t hold back any longer; my orgasm rapidly wells up."
                    play sound cum
                    show cream ssex4 with cum
                    play sound cum
                    show cream ssex4 with cum
                    "My cock explodes inside her. My cum coats her insides while her orgasming pussy clamps down tightly around my shaft, milking as much cum as it can out of me."
                    play sound cum
                    show cream ssex4 with cum
                    play sound cum
                    show cream ssex4 with cum
                    stop ambience fadeout 3.0
                    stop music fadeout 3.0
                    "As I pull out, her body twitches and jerks as she continues to climax; drool spilling from her lips."
                    show cream ssex5 with dissolve
                    cream "Ooohh… Ohh… Your cock fucked me so good! It filled me up so much with its thick hot cum, I love it so much…"
                    "She sinks down onto the counter and pants in the afterglow of her orgasm, clearly enjoying the feeling of my hot cum inside her."
                    scene bg black with dissolve
                    stop music fadeout 3.0
                    "The two of us relax for a while before cleaning up."
                    scene bg black with dissolve
                    show bg bakerybedroom with dissolve
                "Nevermind":
                    jump bakeryeveningmenu
            show cream neutral with dissolve
            $ creamsex2 = 1
            jump bakeryeveningmenu
        "Leave":
            cream "Okie dokie, see you later!"
            jump evening

label creamlingeriesex:
    scene bg black with dissolve
    "You found a secret scene! Requirements met: Work with Cream after beating her route. 50%% chance."

    "Some time after work…"
    show bg farmupstairs with d
    "… Cream leads me up to her room, but before letting me in…"
    show cream happy with d
    cream "Wait out here for a second, I have a surprise for you!"
    mc "A surprise? Interesting."
    hide cream happy with d
    "Stepping into the room, she closes the door behind her and everything goes silent…"
    "About 100 seconds later, I hear her call me in."
    cream "Come on in!"
    play music sex1 fadeout 3.0
    scene creamb lingerie
    show cream lingerie1
    with d
    mc "Heyy, nice lingerie!"
    cream "Do me, do me!"
    mc "Woah, just like that?"
    cream "Yesh! All this work has made me sooo horny!"
    cream "I can’t wait around for you to proposition me forever, so I’m going to ask you instead!"
    menu:
        "Fuck?"
        "Yes":
            pass

    mc "I like your style. I’ll give you exactly what you want."
    "I bring myself towards the bed and marvel at Cream’s huge breasts, along with her perfect breeding material hips."
    cream "Ooohh, hooray!"
    "She ogles at my cock which is currently hardening, her lips curling into a smile while she brings one of her hands to my shaft."
    cream "I’m so glad we got to spend some more time together. I can’t wait for you to totally screw me!"
    "While she jacks me off with one hand, she spreads her gooey pussy lips with her other, giving me the perfect eye candy to get an erection."
    cream "I’m so slippery wet. I want you to stick it inside straight away!"
    mc "You didn’t have to ask, heh."
    play sound cum
    show cream lingerie2 with d
    "Kneeling just before her plump pussy, I press my glans against her spread opening. I begin to buck my hips and thrust straight inside."
    "Cream immediately adjusts to my girth, insatiably accepting my entire cock while squeezing and sucking for more."
    cream "Ahhh, yesss… Sex with you is the best, [playername]…"
    play ambience sex fadein 3.0
    "Her pussy feels so good that my cock stiffens even more. Her legs also wrap around me, pulling me into the missionary position as we make love."
    "I can really feel her wetness in this position, squishing and dripping around my cock with each thrust."
    "Cream squeaks with pleasure as I gather speed. Our love making gradually transforming into lustful pounding."
    "I bring my lips to meet hers, making out with her as we make love. Our tongues perform an erotic dance around each other as we lose ourselves to the passion."
    "She pulls away, however only for a moment as her lips move to attack my neck. I can immediately feel her hot breath against the surprisingly sensitive skin there, as she teases any erogenous zone she can find."
    "And to add to that pleasure, she constantly dirty talks, her saccharine words perhaps more powerful than any physical sexual stimulant."
    cream "That’s it, babe… I want you to fill my pussy up with your thick cum…"
    "My cock noticeably swells up as my body prepares to unload. Cream seems to notice and she tightens her legs around my hips, pulling me in even closer."
    cream "Yess, [playername], I really want you to cum for me…"
    "Holding the bed tightly for leverage, I grit my teeth and pound her as hard as I can."
    "Cream can no longer hold back a slew of passion-infused moans, her entire body squirming under the intensity of the pleasure."
    cream "Ohh gods, I’m going to come too! Ahhh, aaahhh… That’s it, keep going!"
    "Fucking even harder. I do my best to push the both of us over the edge."
    play sound cum
    show cream lingerie3 with cum
    play sound cum
    show cream lingerie3 with cum
    "Finally, I pass the point of no return. The pressure reaches boiling point as my body finally lets loose a primal orgasm."
    play sound cum
    show cream lingerie3 with cum
    play sound cum
    show cream lingerie3 with cum
    stop ambience fadeout 4.0
    "The two of us, while entwined, indulge in euphoria as I fill her up. Several streams of my hot cum guzzling deeply into her waiting womb, all while Cream pulls me in as deep as she can."
    show cream lingerie4 with d
    stop music fadeout 10.0
    "After a few remaining moments of heated passion, we finish and relax. I remain cuddled on top of the cuddly, angelic pony, her arms still wrapped around me."
    cream "Mmm… If only that could put a bun in my oven. Hehe."
    mc "*Pant* Only you could make the missionary position that intense."
    mc "I hope you didn’t give me a hickey!"
    cream "Nope, I wouldn’t do that! Hehe."
    scene bg black with dissolve
    if crystalballactivated == 1:
        jump cbmenu
    $ secretsunlocked += 1
    "We cuddle and chat for a little bit before I clean up and head back home."
    jump evening
