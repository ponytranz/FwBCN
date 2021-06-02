label farm:
    $ farmvisits += 1
    if farmvisits == 1:
        $ monies += 25
        $ farmvisit1 = 1
        jump farmvisit1
    elif farmvisits == 2:
        $ monies += 25
        $ farmvisit2 = 1
        jump farmvisit2
    elif farmvisits == 3:
        $ monies += 25
        $ farmvisit3 = 1
        jump farmvisit3
    elif farmvisits == 4:
        stop music fadeout 3.0
        show bg farm with dissolve
        show honeycrisp nchappy with dissolve
        play music farm
        honeycrisp "Hey stud! It's great to see you again."
        mc "Hey Honey, I'm always happy to visit."
        show honeycrisp nclaughing with dissolve
        honeycrisp "I have great news too, mah wrist is finally okay! And, I have a new cow employee."
        mc "That's wonderful, you'll barely need my help anymore I guess."
        show honeycrisp nchappy with dissolve
        honeycrisp "Well stud, I could always use an extra set of hands around the farm."
        honeycrisp "With three able bodied workers, this place is gonna glow!"
        show honeycrisp nchorny with dissolve
        honeycrisp "And of course, y'all welcome to join me in bed, ehehe..."
        $ blossomvisit = 0
        jump farmmenu
    else:
        stop music fadeout 3.0
        play music farm
        label prefarmmenu:
            scene bg farm with dissolve
            if annamilking == 7:
                jump annamilkingevent
            else:
                pass
            show honeycrisp nchappy with dissolve
            if blossomvisit == 1:
                honeycrisp "Howdy again, I hope you and Blossom are behaving up there."
                if confessedsexwithblossom == 1:
                    honeycrisp "I'd tell y'all to use protection, but I guess I don't need to worry about that."
                honeycrisp "Ready to get some work done? Or are you heading out?"
            else:
                honeycrisp "Howdy stud, here for work?"
            jump farmmenu
    label farmmenu:
        menu:
            "Work with Honeycrisp":
                scene bg farm2 with dissolve
                $ monies += 25
                "I work all day and earn 25 monies."
                $ rand = renpy.random.randint(1,2)
                if rand == 1 and honeycrispoutsidesex == 0:
                    $ honeycrispoutsidesex = 1
                    jump farmsexduringwork
                else:
                    pass
                show bg farmkitchen with dissolve
                show honeycrisp closehappy with dissolve
                "As the afternoon lulls on, I spend my time with Honey which eventually leads us into the kitchen."
                play ambience ambiencenight
                stop music fadeout 3.0
                menu honeycrispmenu:
                    "Talk" if honeycrisptalks == 0:
                        "I decide to strike up a conversation with Honeycrisp, I'm sure she's full of interesting stories."
                        jump honeycrisptalk
                    "Sex" if honeycrispsex == 0:
                        menu:
                            "Threesome" if fr == 1:
                                $ honeycrispsex = 1
                                show honeycrisp closeshocked with dissolve:
                                    xpos 200
                                    ypos 720
                                honeycrisp "Wha wha?!?!"
                                "Blossom who overheard us while pouring herself a drink also reacts."
                                show blossom closeshocked with dissolve:
                                    xpos 600
                                    ypos 75
                                blossom "Wha wha?!?!"
                                mc "Well, we don't need to play games where we take turns doing it behind everyone else's back anymore."
                                mc "So why not kick back and have some fun?"
                                show honeycrisp closeangry with dissolve
                                honeycrisp "Jeeeeeeeeeeezzzzzzz... Ya got some nerve [playername]..."
                                show blossom closeawkward with dissolve
                                blossom "I'll do it! If that's what you want..."
                                honeycrisp "Uhhhuhh..."
                                "Looks like I'll have to convince Honeycrisp, like a boss battle?"
                                "If I pick the wrong choices, she'll refuse and I'll have to try again another day."
                                menu:
                                    "Come on Honeycrisp, you're not gonna let Blossom have all the fun are you?":
                                        show honeycrisp closeneutral with dissolve
                                        blossom "That's right! You're not embarrassed to play around are you?"
                                        honeycrisp "Ehh... My lil Blossom is getting tough lately."
                                    "It's not like it's your first time doing it.":
                                        honeycrisp "Tch, that's your convincing argument? I did it when I was brainwashed so I'll do it now?"
                                        honeycrisp "The answer's no."
                                        blossom "Awhh man..."
                                        hide blossom with dissolve
                                        jump honeycrispmenu
                                show honeycrisp closeangry with dissolve
                                honeycrisp "But doing something with my sister? That's inexcusable... I can't..."
                                menu:
                                    "Doing something with your sister? You don't have to do anything with her at all.":
                                        show honeycrisp closeneutral with dissolve
                                        honeycrisp "Mmm... That's true enough..."
                                        honeycrisp "And you didn't make us do anything with each other when we were brainwashed..."
                                    "You're sharing me anyway, what's wrong with cutting the middleman?":
                                        honeycrisp "This isn't some game where you can play around with everyone..."
                                        honeycrisp "Stop taking my opinions so lightly..."
                                        blossom "Awhh man..."
                                        hide blossom with dissolve
                                        jump honeycrispmenu
                                blossom "Yeah, yeah! We're only gonna be next to each other! It's easier for all three of us!"
                                honeycrisp "Siiighhh, fine!"
                                jump honeyblossomthreesome
                            "Cowgirl position":
                                $ honeycrispsex = 1
                                "She grins at my proposition and leads me up to her bedroom."
                                jump honeycrispsex
                            "Back":
                                jump honeycrispmenu
                    "Leave":
                        "I bid Honeycrisp farewell and return home."
                        jump evening
            "Talk" if honeycrisptalks == 0:
                    menu:
                        "Talk about recent events":
                            honeycrisp "Ever since you came along things have been going so well lately."
                            mc "Don't forget the work your sister and Anna did, I was only a small part of that."
                            honeycrisp "Ay, but sometimes the smallest cog is required to make the machine run."
                            honeycrisp "I think you were the exact knock back to reality I required."
                            honeycrisp "Sometimes you're so alone, and you work so hard you forget what the outside world is like."
                            mc "It's good to reach out and reconnect with friends and family every so often."
                            mc "You need to remember that you're not alone, and you can get the support you need."
                            honeycrisp "You're right stud, but you forget that one of the hardest steps sometimes is reaching out and accepting that support."
                            honeycrisp "For that, the solution is a little more cloudy. I'm just fortunate that you decided to show up when ya did."
                        "Plans for the future?":
                            mc "Now you're working closely with Anna and have an employee, what are your plans for the future?"
                            honeycrisp "Hmm, good question stud."
                            honeycrisp "Ya see, I was never the planner in the farm, that was always paps. He always had a plan and ambition."
                            show honeycrisp ncsad with dissolve
                            honeycrisp "Which is why it felt so icky for him to pass in his prime, he had so much spirit in him."
                            honeycrisp "Never got to see the fruit of his work, or even the opportunity to have grandkids."
                            "See sighs and tears up slightly, it's clear that the memories are still painful."
                            mc "I've never actually asked because it felt like a sensitive topic, but how did he pass?"
                            honeycrisp "He didn't even get to die in an interesting way, it was a disease that caused him to deteriorate so fast."
                            honeycrisp "Paps was healthy one moment, and in the next week he was immobilised in hospital, and then in a month..."
                            mc "It's shocking how fast it can happen sometimes."
                            mc "What about your mother, is she not around?"
                            honeycrisp "Nah, we're estranged from her. I have no idea where she is, or what she's doing."
                            honeycrisp "My paps was a single father for years, quite a rare case in Arcadia. After mother left, he didn't care much for dating, Blossom and I were always his priority."
                            show honeycrisp ncneutral with dissolve
                            honeycrisp "Gosh, anyway... Sorry to bore you with that tangent, you asked me if I had any plans for the future."
                            show honeycrisp nchappy with dissolve
                            honeycrisp "Guess I'll have to think about it more now, thanks stud."
                        "How did you become a farmer?":
                            mc "How did you become a farmer?"
                            honeycrisp "It has always been in my blood, stud. Hey, that rhymed!"
                            honeycrisp "I helped out paps ever since I was a tiny girl."
                            honeycrisp "Back then he'd give me small 'made up' jobs for fun, like uh, raking the leaves!"
                            mc "You've never considered any other work?"
                            honeycrisp "I mean it's a farce ain't it. I'd probably have to sell the farm, and that's been in our family for longer than I know."
                            honeycrisp "But I don't mind being a farmer for the rest of mah days, it's incredibly satisfying work, and every evening is free time so I never burn out."
                            mc "You reckon your children will run the farm then?"
                            honeycrisp "Hah, I don't tend to think that far forward in mah life, I just meander mah way through each day."
                            honeycrisp "What about you? Are you ever going to settle down with a permanent job?"
                            mc "That's a great question, it would probably pay more if I specialised into one career."
                            show honeycrisp nclaughing with dissolve
                            honeycrisp "Y'all always welcome to make working here your career, although if you do we won't be able to have children to run the place after us, ahaha!"
                            mc "That's very cheeky of you to presume, haha."
                        "Ask what Honey does in her free time":
                            honeycrisp "Now that I've actually got free time, I've been getting out more and visiting friends."
                            mc "Anyone in particular?"
                            honeycrisp "I like to pop down to the Riding Mare for a pint of cider and Ruby often visits."
                            honeycrisp "It may be the cider I make, but it's even more satisfying drinking with friends."
                            honeycrisp "Sometimes me and Ruby go to a nearby nightclub too, that's always a great night out."
                            mc "I should join you sometime."
                            honeycrisp "Absolutely! Three's a crowd!"
                            honeycrisp "I'd give you a specific time and date, but the fun of visiting the nightclub and bar is just seeing who's there!"
                        "Back":
                            jump farmmenu
                    $ honeycrisptalks = 1
                    jump farmmenu
            "Sex" if ashoney == 0:
                $ ashoney = 1
                honeycrisp "Hmm, not right now, stud. I need to make the most of today's sun."
                honeycrisp "If you stick around tho', I'll give you one heck of a ride."
                "Looks like Honeycrisp will only have sex with me after work."
                jump farmmenu
            "Visit Blossom" if blossomvisit == 0:
                scene bg farmkitchen with dissolve
                scene bg blossombed with dissolve
                $ blossomvisit = 1
                "I go into the farmhouse and visit Blossom, she seems to be lazing around in her bedroom and hasn't left for college yet. I should have an hour to talk or play with her."
                jump blossomvisit
            "Visit and work with Anna (This will take all day)":
                jump annavisit
            #"Replay a Scene":
                #menu:
                    #"Milking into Paizuri with Anna":
                        #hide honeycrisp ncwith dissolve
                        #jump annamilking
                    #"Threesome with Honey and Anna":
                        #hide honeycrisp ncwith dissolve
                        #jump honeyannathreesome
                    #"Cowgirl with Blossom":
                        #hide honeycrisp ncwith dissolve
                        #jump blossomcowgirl
                    #"Back":
                        #jump farmmenu
            "Back to World Map":
                if fr == 1:
                    jump prefinalworldmap
                jump preworldmap
    label farmvisit1:
        stop music fadeout 30.0
        "I’ll go work at the farm; if I recall the mare running the place has an injury, helping her is fair incentive."
        "It’s a ten-minute walk away past the river, I best head out quickly. "
        scene bg farm with dissolve
        show bg farm with dissolve
        "Upon arriving I see a massive plantation, apple trees stretching far as the eye can see, although on closer inspection the trees are blending into the forest behind the farm’s perimeter."
        "There are various crops scattered around, however, I can’t identify any because they’re far from flowering."
        "Roughly in the centre there is a house with a barn at the side, I step past a fence and make my way to the farmhouse."
        "I walk up to the farmhouse and I’m just about to knock before I hear someone call out to me."
        "An orange mare that was hidden away behind a wagon appears, waving and gesturing for me to come over."
        show honeycrisp happy with dissolve
        "As I get closer, her figure comes into sight, and I notice she has her right hand in a cast."
        "Wow, I could grind cheese on those abs."
        "And her breasts are huge"
        mc "Good morning, you must be Honeycrisp?"
        show honeycrisp laughing with dissolve
        if bakeryvisit1 == 1:
            honeycrisp "Howdy stranger! I believe you were the 'hairless stallion' at Cream's party right? But ain't you something, you ain't much of a stallion at all."
        else:
            honeycrisp "Howdy stranger, I was told to expect someone that looks like a hairless stallion, but ain’t you something, ain’t much of a stallion at all."
        mc "I guess not, but I’m good to work like the rest."
        show honeycrisp happy with dissolve
        honeycrisp "That’s fantastic news sugar, really appreciate ya coming here"
        show honeycrisp neutral with dissolve
        honeycrisp "You came just in time, I’ve been struggling to keep up the farm alone with mah dang cast and I'm running behind on apple deliveries."
        mc "You’re working here on your own? But this farm is massive!"
        show honeycrisp laughing with dissolve
        honeycrisp "Yup, it’s more of a recent thing unfortunately, things around ‘ere have halted and the injury certainly hasn’t helped."
        show honeycrisp sad with dissolve
        honeycrisp "Big issue is, I have some early varieties of apples that need picking and I just can’t do it... No matter how hard I try... I can’t use a ladder and pluck apples with this darn cast slowing me down."
        mc "Don’t worry about it, you shouldn’t push yourself, just show me where the trouble is."
        show honeycrisp laughing with dissolve
        honeycrisp "’ppreciate it friend. Let’s get right to it, there’s a ladder in the barn, lemme show ya."
        hide honeycrisp with dissolve
        show bg farm2 with dissolve
        play music farm fadein 5.0
        "She’s not wasting any time as she marches ahead, doesn’t look like she’ll let her injury slow her down even a little, I follow briskly from behind."
        "We start with a few nearby trees as she demonstrates how to safely secure the ladder in place."
        show honeycrisp happy with dissolve
        honeycrisp "When you pick ‘em, come down the ladder and place them in gently. If you drop ‘em they’ll smash, and I need to make sure mah goods are of pristine quality for the customers."
        mc "Okay, so I’ll pick a few, carry them down, place them in the basket, no problem."
        hide honeycrisp happy with dissolve
        show bg farm3 with dissolve
        play sound move
        "I head up the ladder, it’s surprisingly high but I’m not one to be particularly afraid of heights, but I felt particularly uneasy at the fact I had to outstretch myself to reach some apples."
        "With Honey at the bottom of the ladder, I hope my butt and nutsack look good from this angle."
        show bg farm2 with dissolve
        "Thankfully, there wasn’t much foliage in the way. I collect a couple of apples and descend the ladder."
        show honeycrisp closehorny with dissolve
        "Honeycrisp was at the bottom rung keeping the ladder in place. I don’t think she needed to do that, but I felt appreciative nonetheless, albeit slightly vulnerable at the fact she could see my butt."
        honeycrisp "Alright stud, we’re going to move the ladder ninety degrees and pick the next quart of the tree dry. If you ever fill one of these baskets, I’ll head back to the barn, empty it, then come back."
        "Stud? Isn't that what you call the stallion that fucks all the mares in the farm?"
        "I could feel my cheeks get a little hot when she said that."
        show honeycrisp happy with dissolve
        mc "You got it boss! I’ll have this tree done in no time."
        show honeycrisp horny with dissolve
        honeycrisp "Y’all not bad to be honest, Penelope done good finding a physically fit man like you to help a gal out."
        mc "Aha, you’re flattering me. I’m simply happy to help, I need to earn my pay to stay."
        honeycrisp "You’ll earn more than just pay at this rate!"
        "More than money? I’m guessing she’s not just talking about respect and admiration."
        "I’m finding Honeycrisp’s up and at ‘em, get what you want attitude endearing."
        "She laughs to herself as she scoops up a full apple basket in one arm and takes it away. Her arm strength must be insane to do that, these baskets would be heavy for me with both arms."
        show honeycrisp laughing with dissolve
        honeycrisp "Well, I'll be right back, keep at it stud."
        hide  honeycrisp laughing with dissolve
        "Okay, with her returning the basket to the barn, I have half this tree left."
        show bg farm3 with dissolve
        play sound move
        "I must admit, I’m building a sweat even though it has only been ten minutes…"
        "How many trees do I have to do?"
        "I take a peek to my right and see a row of similar looking trees stretching out until it becomes an amorphous blur of foliage."
        "Oh no, I’m going to be here forever and I’m already sweating after ten minutes."
        show bg farm2 with dissolve
        show honeycrisp laughing with dissolve
        "Honeycrisp returns and pops the basket down, it took her a surprisingly long time to get the basket all the way there and back, I’ve nearly filled up the next basket."
        honeycrisp "With the two of us working through this together, it’ll take no time at all! Usually I carry the baskets back and forth myself, so it takes twice as long."
        show honeycrisp happy with dissolve
        mc "This is perfect then, let no injury slow us down, we’ll harvest these apples twice as fast!"
        "Honeycrisp bounces and pumps her fist in the air proudly. I could feel her infectious pride and energy fill me up."
        show honeycrisp laughing with dissolve
        honeycrisp "Heck yeah, that’s the spirit!"
        show honeycrisp horny with dissolve
        honeycrisp "I’ve missed having support like this, keep it up sugar!"
        hide honeycrisp horny with dissolve
        "She takes the next basket and heads off grinning to herself.  After seeing her earnest smile, I feel more motivated now than when I had started."
        "It’s hard to believe she has been running this entire farm all by herself with that injury."
        show bg farm3 with dissolve
        "I move the ladder to the next tree and keep filling basket after basket, I can feel myself getting faster as my movements become muscle memory."
        show bg farm4 with dissolve
        stop music fadeout 10.0
        "Even under the sweltering sun the shade from the apple trees prevent overheating."
        show bg farm3 with fade
        play sound move
        pause 0.5
        show bg farm3 with fade
        play sound move
        pause 0.5
        show bg farm3 with fade
        play sound move
        pause 0.5
        "Onto the next tree, and the next, and the next. It’s menial work, but with each filled basket I look forward to Honey returning and delivering another motivational quip."
        show bg farm2 with dissolve
        honeycrisp "Heyyy, stud! Time for a break!"
        "My ears perk, ‘stud’ again."
        "I look back towards the farmhouse and I can see Honeycrisp shouting and waving from beyond the fence."
        "I had lost track of time; I was more or less automatically plucking apples while lost in thought."
        "I step down the ladder and enjoy a cathartic stretch. I bring the final basket back on my way, which is thankfully only half full and thus not heavy."
        show bg farm with dissolve
        show honeycrisp laughing with dissolve
        honeycrisp "Well, I’ll be, amazing work! Everything’s all coming together, thought I’d treat ya with something special."
        mc "Special?"
        show honeycrisp happy with dissolve
        show bg farm5 with dissolve
        play music castle fadein 10.0
        honeycrisp "Over here, got some homebrew for you to try out."
        "She leads me to a picnic bench cosy in the shade generated by the farmhouse, where I spot two empty glasses and an ice-cold pitcher of cider."
        "Pouring us both a glass, a few ice cubes drop into mine. This is perfect, just what I needed after working up a sweat."
        honeycrisp "This is mah first month making some of my own for proper, and you are my first proper customer, though this one’s on the house! What do you think?"
        "I take a sip at first, but as soon as it hits my lips, I realize how parched I am and take a longer gulp."
        "Savouring the taste, it’s sweet and pleasantly dry. I’m no stranger to the taste of cider but this far exceeds the taste of anything I’ve bought at a bar."
        if barvisit1 == 1:
            "This is the same stuff Riku had in her refridgerator, but it tastes even fresher and richer."
        show honeycrisp laughing with dissolve
        mc "Mmmm, this is delectable, genuinely the best cider I’ve ever had."
        show honeycrisp happy with dissolve
        honeycrisp "Ay, I agree, no one quite makes cider like my ol’ paps."
        show honeycrisp neutral with dissolve
        honeycrisp "This is his secret recipe, maybe it isn’t as good as he used to make it, but judging from your reaction, looks like I lived up to his name."
        show honeycrisp happy with dissolve
        mc "You certainly did."
        "I take another sip, feeling refreshed."
        show honeycrisp neutral with dissolve
        honeycrisp "Paps passed a few months back, it was a surprise. Means I have to look after this entire place by myself, rather than the two of us."
        mc "That’s really recent… I’m sorry to hear that."
        show honeycrisp shy with dissolve
        honeycrisp "Figured you should know the backstory of the farm if you’re going to work here."
        mc "You don’t have to say anything if you don’t want to."
        honeycrisp "Yeah, I know sugar… But it must be a ridiculous sight, seeing a damaged mare trying desperately to keep this place going."
        mc "I don’t think it’s ridiculous at all, I’ve seen how hard you’re working, and I think it’s admirable."
        show honeycrisp sad with dissolve
        honeycrisp "I would be working harder if it wasn’t for my wrist. They said it’ll take seven or eight weeks to heal, but I don’t have a second to spare on the farm."
        honeycrisp "It’s just me and mah sister now, and I need to do everything I can just to ensure we have a profitable harvest."
        mc "I’ve been wondering, what’s wrong with your wrist?"
        show honeycrisp neutral with dissolve
        honeycrisp "Mmphh… Well sugar…"
        honeycrisp "I told people I fell from a ladder but I kinda haven’t told anyone else the truth, it’s too humiliating to say."
        show honeycrisp happy with dissolve
        honeycrisp "I feel like I should tell you though, maybe it’s because you’re a new face, but I reckon I can trust ya."
        honeycrisp "Promise to keep it between us?"
        mc "Of course, I promise."
        show honeycrisp shy with dissolve
        honeycrisp "Well, aha… I fractured the bone because I got into a fight with a tree and lost."
        mc "You punched a tree?"
        show honeycrisp neutral with dissolve
        honeycrisp "*Sigh*, yeah… I was really frustrated, ya’know?"
        honeycrisp "It was just after the funeral, and I didn’t have time to grieve."
        show honeycrisp sad with dissolve
        honeycrisp "I was already working twice as hard, no other family around here to speak of and I couldn’t tarnish my sister’s education by asking her to quit college."
        honeycrisp "I was about to carry some apples back on my own, but the basket broke, some apples fell, smashed and got covered in mud."
        show honeycrisp neutral with dissolve
        honeycrisp "It may have been a small thing, but to me that was mah breaking point."
        show honeycrisp angry with dissolve
        honeycrisp "I was so pissed, I full force punched the tree, didn’t think for a second."
        mc "Ouch… That must have really hurt."
        show honeycrisp satisfied with dissolve
        honeycrisp "It really hurts my pride admitting it. Whatever pride I have left."
        show honeycrisp sad with dissolve
        honeycrisp "I feel pathetic, it’s not like me to do something so darn stupid. But sometimes in these moments ya just don’t think."
        mc "Your emotions must have been stirring, I can understand that you’d be frustrated and lash out."
        mc "Everyone has their weak moments, and they don’t necessarily reflect you as a person, your personality."
        show honeycrisp shy with dissolve
        honeycrisp "Heh, lash out, it is like me to lash out on a tree of all things. Don’t think I have the heart to be that mean to a person."
        show honeycrisp satisfied with dissolve
        honeycrisp "Phew… It feels good to finally tell someone that."
        show honeycrisp closesatisfied with dissolve
        "Honeycrisp surprises me by closing in for a hug, her overly large breasts nonchalantly pressing against my chest and catching me off guard as I awkwardly hug back."
        show honeycrisp closehorny with dissolve
        honeycrisp "Heck, sorry about these large jugs getting in the way, I hope my nipples didn’t poke ya."
        mc "It’s fine, they were nice and soft."
        honeycrisp "I can hug you again if you’d like stud, heh."
        menu:
            "(Hug her again.)":
                show honeycrisp closesatisfied with dissolve
                "We reembrace and this time I do indeed feel her nipples poking against my chest, maybe it’s because I’m paying close attention, or perhaps they weren’t erect before."
                show honeycrisp closehorny with dissolve
                "I feel a flitter of butterflies in my stomach before we part, and she gleefully takes a sip of cider to break up the post-hug awkwardness."
                honeycrisp "Heh, didn't think you'd actually go for it."
                honeycrisp "Thanks, I needed that."
            "How about something more than a hug?":
                "She takes a sip of cider before replying with a bemused expression."
                honeycrisp "I’d love to show a guest like yourself how a cowgirl like me performs at a rodeo."
                honeycrisp "But with mah injury, well, maybe you’ll have to do the showing off."
                honeycrisp "Later, though, we got some demanding work to do first."
            "I’ll pass for now; I don’t want to get distracted before going back to work.":
                honeycrisp "Mm, good thinking stud, too much physical contact might…"
                show honeycrisp closelaughing with dissolve
                "She takes a sip of her cider and sticks her tongue out at me."
                honeycrisp "Heh… You know."
        show honeycrisp satisfied with dissolve
        honeycrisp "You know, you’re the first person I’ve spoken to other than my sister this week."
        honeycrisp "I’ve been too exhausted to visit my friends in the evening. It’s back breaking work all daylight, until it gets too dark to see anything, then I pass out on my bed."
        mc "I’m not one to judge, but it sounds like you’re putting too much burden on yourself."
        mc "I can tell you’re tough, but even you can’t keep that up, you’ll burnout and crack sooner or later."
        show honeycrisp shy with dissolve
        honeycrisp "Ugh, I already cracked when my wrist went, I’m running on fumes sugarcube…"
        hide honeycrisp shy with dissolve
        show bg farm4 with dissolve
        honeycrisp "Actually… The only thing still keeping me going is my little sister, there’s no way I could let her down, she’s an angel."
        mc "That’s sweet, what’s she like?"
        honeycrisp "She’s called Blossom, and she’s not like me and paps. She’s intelligent and bright, she got into a college and is pursuing music now."
        "Blossom must be at least eighteen then, roughly the same age as me."
        show bg farm5 with dissolve
        show honeycrisp closehappy with dissolve
        honeycrisp "She helps me out during the weekend, I always tell her she doesn’t need to, but she’ll just do it anyway."
        mc "Is there no one else that can help you? Another relative, or just an employee?"
        show honeycrisp closeneutral with dissolve
        honeycrisp "Hmm..."
        honeycrisp "Maybe… I’m so busy though, and I can’t even legibly write a letter with my wrist like this."
        mc "Pardon my naivety if I’m wrong, is there no way to fix your wrist with magic?"
        show honeycrisp closehappy with dissolve
        honeycrisp "Aha, unfortunately not stud, any attempt to forcibly repair my fractures will cause the bone to reform incorrectly. It's gotta heal naturally."
        mc "Ahh, I guess this is one problem you can’t just wave away with magic."
        show honeycrisp closelaughing with dissolve
        honeycrisp "Heh, sometimes I imagine how much easier everything would be if I could just pluck the apples one by one with magic like one of those unicorns."
        show honeycrisp closehappy with dissolve
        honeycrisp "But their magic ain’t all that. Ain’t one of those unicorns ever beating me in a race or an arm wrestle. Well, as soon as my wrist is fixed anyway."
        honeycrisp "Us wingless and hornless ponies are the strongest, without us the heavy work wouldn’t get done."
        menu:
            "Why don’t you hire a unicorn to help?":
                show honeycrisp closelaughing with dissolve
                honeycrisp "I can’t imagine a unicorn being any more helpful than a regular ol’ hornless pony."
                show honeycrisp closehappy with dissolve
                honeycrisp "If it was a powerful unicorn, I couldn’t let them waste that potential on a farm."
                honeycrisp "But if they were too weak, their magics wouldn’t be any faster than plucking apples or crops by hand."
                "I recall back to Moxie using telekinesis on a plushie, I don’t know much about magic but Honeycrisp is probably right."
            "I think a pegasus would be a lot of help.":
                show honeycrisp closelaughing with dissolve
                honeycrisp "Hmm, imagine a winged pony getting all those apples in seconds."
                show honeycrisp closehappy with dissolve
                honeycrisp "Not many pegasi in these parts though, other than dear Riku of course."
                honeycrisp "Me and a pegasus would make a good team though."
                "She’s right, I don’t think I’ve seen many pegasi around here at all, I wonder if they predominantly live elsewhere?"
        show honeycrisp closelaughing with dissolve
        honeycrisp "I need one of them flying horned goddesses."
        stop music fadeout 5.0
        show honeycrisp closehappy with dissolve
        honeycrisp "Although, I think you'll do just fine."
        show honeycrisp happy with dissolve
        honeycrisp "We should get back to work, let’s say we clear a bunch more trees, that’ll give me plenty of apples to sort out for the morning, I’ll pay ya and you can head home then if you want."
        mc "Sounds good."
        hide honeycrisp happy with dissolve
        play music farm fadein 5.0
        show bg farm with dissolve
        pause 1.0
        show bg farm2 with dissolve
        "We head back to the trees, with the sun shining overhead, I continue to harvest apples well into the day."
        show bg farm3 with dissolve
        pause 1.0
        show bg farm2 with dissolve
        show honeycrisp neutral with dissolve
        "Honeycrisp once again takes a heavy basket in one arm, leveraging it against her hips, she’s struggling slightly more than she was before, yet she pushes onwards regardless."
        hide honeycrisp neutral with dissolve
        show bg farm3 with dissolve
        "I spend a few moments watching her struggle towards the barn. Before I came along, how did she manage to do everything by herself?"
        "I can’t work here forever, and she can’t do all this on her own. Is there anything I can do to help?"
        "She’s such a strong and sweet person despite the burden and recent tragedy."
        "I can’t even fathom the emotional turmoil of what she’s going through, yet she still wears a strong smile for me and her sister."
        "It seems she has enough money to employ someone if she’s employing me, so I’ll just need to find someone to replace me when I’m not here."
        "I just got an idea though, I’ll pick all the apples Honeycrisp asks of me, then I’ll stick around and talk to her sister, maybe she can help me."
        "A girl like Honey, she deserves so much more."
        show bg farm6 with dissolve
        "I use my forearm to wipe the sweat off my brow. The sun is no longer overhead, it’s passed the centre of the sky and halfway to meeting the mountainous surroundings, so the trees no longer give me shade."
        "Fortunately, the air has grown cool and there’s occasionally a soft breeze that calms the skin."
        show bg farm2 with dissolve
        show honeycrisp laughing with dissolve
        honeycrisp "Fantastic work, partner! Part of me always wanted a strong capable man to work with."
        menu:
            "Like a husband?":
                show honeycrisp laughing with dissolve
                honeycrisp "Haha, you’re funny stud."
                show honeycrisp closehorny with dissolve
                honeycrisp "You’re not entirely wrong either, but let’s not rush anything."
                show honeycrisp laughing with dissolve
                honeycrisp "Joking, of course! Haha."
            "I’m strong and capable in other areas too.":
                show honeycrisp closehorny with dissolve
                honeycrisp "Oh I bet you are stud; your physical performance has more than met my standards today."
            "Thanks Honeycrisp, we worked well as a team today.":
                show honeycrisp laughing with dissolve
                honeycrisp "We sure did stud, if you ever come back here, I’ll make sure there’s plenty of fun work we can do together."
                "I wouldn’t call picking apples fun, unless she’s hinting at something else."
        show honeycrisp happy with dissolve
        "I pick up the last basket and carry it back instead of letting her do it."
        show bg farm with dissolve
        mc "Just so you know Honeycrisp, I won't be able to work here everyday, and I’m concerned about your wrist."
        stop music fadeout 30.0
        show honeycrisp horny with dissolve
        honeycrisp "If you’re leaving soon, then maybe I should savour the moment."
        "She looks at me flirtatiously as I’m reminded of her heat, working hot and sweaty with her all day seems to have left us both a little horny."
        "I don’t even have time to dwell on the fact she ignored my concern."
        show honeycrisp happy with dissolve
        honeycrisp "Oh and call me Honey, all my friends call me that. "
        show bg barn with dissolve
        mc "You got it, Honey."
        "I pour the final apples into a large pile in the barn, seeing the literal fruit of my day’s labour sprawled out here like this is immensely satisfying."
        mc "What’s the plan now?"
        show honeycrisp laughing with dissolve
        honeycrisp "Heh, well, I don’t think I could ask for you to stick around while I sort and process these apples, I’ll pay you now and you can leave before it gets late."
        hide honeycrisp lauging with dissolve
        show bg farm with dissolve
        show bg farmkitchen with dissolve
        "We head back to the kitchen in her farmhouse where she hands me the pay and I put it in my satchel."
        show honeycrisp happy with dissolve
        honeycrisp "Good pay for hard work, partner."
        mc "Thanks Honey, I’ve definitely enjoyed working here."
        show honeycrisp horny with dissolve
        honeycrisp "Next time, let’s put an emphasis on the hard part of the work."
        mc "Oh-"
        hide honeycrisp horny with dissolve
        show honeycrisp ass with dissolve
        "Her tail briefly brushes itself against my crotch as she walks past me to leave, I peek at her ass and she keeps her tail tucked out the way almost purposely."
        "It’s well-lit in here, so I catch a glimpse of a glisten between her thighs."
        "Unfortunately, I can’t enjoy the view for long as she steps outside and returns to the barn, leaving me with a slight erection. What a tease."
        hide honeycrisp ass with dissolve
        "She's definitely hungry for some action, but even now with an opportunity she's too busy."
        "More than ever, I want to solve her plight."
        "..."
        "Ah, great, I have a erection. There's no way I'm walking home with this."
        "I could jack off right now, or maybe I could let Moxie deal with it later. There’s one thing for sure though, I will absolutely not walk back in public until my erection is gone, it would be far too embarrassing."
        show blossom shocked with dissolve
        play music challenge
        blossom "Eep! A strange creature with a boner!"
        "Regrettably, embarrassment didn’t wait and came to me instead as a new figure walked in the door and stared at me, shocked, mouth agape."
        mc "N-no, you misunderstand, I've been with your sister!"
        show blossom embarrassed with dissolve
        "This new mare was a little shorter than Honeycrisp, she had a orange coat with cute fluffy blonde hair."
        "She was staring at my cock, neither of us have said anything for a few seconds, and there was definitely awkward air."
        show blossom awkward with dissolve
        blossom "I- uhm, hello... My name’s Blossom. You uh, you were just with my sister?"
        mc "Hey Blossom, I’m [playername], I’ve been helping your sister all day."
        show blossom bashful with dissolve
        blossom "You did… ‘that’ with my sister?"
        show blossom shocked with dissolve
        mc "No, no, I’ve been helping with the apples and the ladder and stuff."
        "Her eyes light up, looks like I said the right thing. She bounces over in a similar gait to her sister and begins making herself a cup of tea."
        stop music fadeout 5.0
        show blossom happy with dissolve
        blossom "This is so wonderful, yes! I’ve been worried sick about my sister! I’m so glad to hear we have an employee."
        mc "Actually, I wanted to talk to you, I think, I’m not sure."
        blossom "Ohh, I see, just one second and I’ll be with you."
        hide blossom happy with dissolve
        play music castle fadein 5.0
        "I take a seat by the kitchen table and wait a few moments."
        show blossom happy with dissolve
        "To my surprise she hands me a cup of tea."
        blossom "Here’s your tea sir, I hope you enjoy it."
        mc "Thank you, that’s very generous."
        show blossom closelaughing with dissolve
        "She sits opposite me with her legs slightly agape."
        show blossom lewd with dissolve
        "It’s not particularly lady-like, I can see her cute innie vulva neatly tucked between her thighs…"
        "My mind keeps drifting to perverted thoughts, all that flirting from Honey has gotten to me."
        blossom "U-uh, are you... staring..."
        show blossom closebashful with dissolve
        mc "Oh sorry, I was lost in thought..."
        show blossom closeneutral with dissolve
        "No more perverted thoughts, time to think seriously. I look up to Blossom and make a mental note to keep eye contact with her, not staring at her breasts or in-between her legs..."
        "Alright, one more peek."
        show blossom lewd with dissolve
        show blossom closeawkward with dissolve
        blossom "Uhm, is your tea okay?"
        menu:
            "Do you have any milk for the tea?":
                mc "Thank you for the tea, that’s generous of you. I don’t mean to seem ungrateful, but do you have any milk?"
                show blossom closebashful with dissolve
                "She looks down and blushes for a moment."
                blossom "M-Milk? N-Now? With me? Oh my…"
                mc "Uh, what with you?"
                show blossom closeawkward with dissolve
                blossom "Uhm… We don’t have any milk right now, I’m sorry… We have a delivery soon though."
                blossom "Anyway, this tea is fruity, apple flavoured, you don’t have milk with those…"
                show blossom closehappy with dissolve
                blossom "M-Maybe I can get you milk next time though…"
            "I like my tea black, thank you.":
                show blossom closehappy with dissolve
                blossom "You mean without milk? That’s normal for fruit tea."
                mc "Oohhh, right, I haven’t had a fruity tea in years, the aroma is tantalising."
                "As predicted the tea emanates an apple fragrance."
                show blossom closelaughing with dissolve
                blossom "Ooo, thank you, I made it myself!"
        show blossom closehappy with dissolve
        "She’s just as kind and generous as her sister in creating and giving me apple-based drinks."
        "The warmth of the cup around my hands is relaxing, for the first time I can feel a wave of tension being released that was pent up by the day’s physical activity."
        show blossom closeawkward with dissolve
        "I take a sip of the tea, it’s already at drinking temperature, and the taste is so alluring I find myself sipping more."
        show blossom closeneutral with dissolve
        "I notice that she’s staring at me inquisitively, neither one of us are really speaking. I probably would have said something by now if I wasn’t so tired."
        show blossom closeawkward with dissolve
        "… Hm…"
        show blossom closeneutral with dissolve
        "She just seems to be waiting for me to say something... Oh, right! I was going to ask about trying to find employees for her sister."
        show blossom closehappy with dissolve
        mc "So, about your sister."
        blossom "Uhm, yes! About my sister?"
        mc "I’ve been working here all day, but I’m not an employee. I actually won’t be able to help much, so I was hoping to find another way to help her run the farm while she’s injured."
        show blossom closeawkward with dissolve
        "Her hands tremble slightly as she clings onto her teacup. "
        show blossom closesad with dissolve
        blossom "Y-yes…"
        "I take a sip of my tea to give her some time to speak, despite this, she doesn’t say anything else."
        show blossom closeawkward with dissolve
        "She seems incredibly shy, and somewhat anxious about this subject."
        mc "Do you have any ideas?"
        show blossom closeneutral with dissolve
        blossom "How long will you be working here, Sir?"
        mc "Who knows, I have a few places I want to work at, but I don't want to make any permanant decisions yet."
        show blossom closeshocked with dissolve
        blossom "Then you'll work here long enough for me to get help?"
        mc "Yeah, sure."
        show blossom closehappy with dissolve
        blossom "I want to send a letter to some nearby cow farmers and try to form a business relationship with them."
        mc "Ohh, that’s perfect."
        show blossom closeawkward with dissolve
        blossom "Honey says she doesn’t have the time, but I know it’s because she’s too scared to reach out to people right now, she acts really tough, but she feels vulnerable and alone."
        show blossom closehappy with dissolve
        blossom "S-So, I thought it’s my turn to be strong for her!"
        show blossom closeawkward with dissolve
        blossom "If we got just one or two extra people down here this farm can really flourish."
        show blossom closelaughing with dissolve
        blossom "I know they’ll agree to it, I just know it!"
        mc "That’s a great plan."
        mc "It sounds like you have everything sorted, all you need me to do is fill the gap between now and then, right?"
        show blossom closebashful with dissolve
        blossom "Ehehe… Could you help me write the letter too? I’m not good with these things."
        mc "Really?"
        "After that speech about being strong, she wants me to write the letter."
        show blossom closeawkward with dissolve
        "There’s a strange insincerity behind her voice though, she’s been peeking lewdly at my body, despite my effort to keep eye contact with her."
        show blossom closeneutral with dissolve
        "Her eyes hazily scan my body, I noticed she looks in-between my legs every so often."
        show blossom closebashful with dissolve
        blossom "Y-you s-should come to my room, I have paper and a pen there."
        show blossom closeawkward with dissolve
        "Oh! She doesn’t want me to write the letter at all, she’s trying to make a move on me. Like a switch in my brain I can feel blood rush down below."
        show blossom lewd with dissolve
        "Struggling to maintain eye contact, I impulsively look down and I spot something unusual."
        "She is shivering, particularly her thighs are trembling, she’s incredibly nervous right now."
        show blossom closebashful with dissolve
        mc "Are you okay?"
        blossom "I-I, uh… May… Uh…"
        "Just like with Honeycrisp, I find myself in an intriguing situation where a girl is hitting on me. This is different though, the atmosphere isn’t one of confidence, she's really nervous."
        "I’m not sure what’s running through Blossom’s mind right now. She seems to be struggling to assert herself. I think she tried to be bold for a moment but accidentally wound up in the deep end and regrets it. "
        "Looks like it’s up to me to be calm and confident here. I’ll take the pressure off."
        show blossom closeawkward with dissolve
        mc "Are you sure you want to do this right now?"
        show blossom closeneutral with dissolve
        blossom "S-sure? What do you mean?"
        show blossom closeawkward with dissolve
        mc "We can always do that another day, there’s no rush."
        show blossom closebashful with dissolve
        blossom "Ahh, right… Another day…"
        show blossom closeneutral with dissolve
        blossom "You know actually, I don’t know the address for the letter, s-so we’ll have to do it another day…"
        show blossom closeawkward with dissolve
        "She takes a sip of her tea; she seems somewhat relieved, yet also seems demoralized."
        "Maybe I’m just overthinking it. At moments like this I wish I could read minds"
        show blossom closeneutral with dissolve
        mc "We will help your sister, I’m sure of it, things will get better around here."
        show blossom closesad with dissolve
        blossom "Th-thank you sir… We both really appreciate it…"
        "She seems saddened; her eyes are teary. I’ve overlooked it until now, but Blossom has been through the same struggles as Honey, it can’t be easy for either of these girls."
        "Even if I’m just doing simple things like picking apples, or writing a letter, it helps. What these girls really need, is just someone there for them, someone that understands and will listen to them."
        hide blossom closesad with dissolve
        show bg farm4 with dissolve
        "We both look through the window as the setting sun sinks below the distant mountains, it’s almost time for me to leave."
        show bg farmkitchen with dissolve
        show blossom closeneutral with dissolve
        "I look back to Blossom and she seems more composed. I think she wanted to proposition me for sex, but she’s simply too nervous to do something like that, she choked on her words merely on the suggestion that we go to her room. Her legs are even crossed now."
        "Should I mention it? Maybe she wants sex, but she’s just too nervous to ask."
        show blossom closeawkward with dissolve
        menu:
            "Should I mention sex?"
            "Hint at it.":
                mc "I’m surprised you would invite a boy up to your room."
                show blossom closebashful with dissolve
                blossom "Ahh, eheh, as long as my sister doesn’t find out."
                "And there it is, the ulterior motive behind her words."
            "Explicitly mention sex.":
                mc "You want to go upstairs because of this uh, ‘season’, right?"
                show blossom closebashful with dissolve
                blossom "Uhm, maybe I wasn’t thinking straight."
                blossom "Sometimes the ‘season’ makes it hard for me to think straight."
                show blossom closesad with dissolve
                "So, it indeed was a moment of courage driven by her heat."
                "I wish I had some way to relate to the feelings and emotions that the mating season brings, it could help me better understand these mares."
            "Say nothing, we’ll see each other again anyway.":
                "Finishing my tea, I decide to excuse myself."
        mc "It’s been great meeting you Blossom, thank you for your tea, it was delicious."
        stop music fadeout 10.0
        show blossom closehappy with dissolve
        blossom "Thank you for coming mister, please come back another time, I’ll make you more tea!"
        mc "I’ll be back, and hopefully I’ll see you then."
        hide blossom closehappy with dissolve
        show bg farm with dissolve
        stop ambience fadeout 5.0
        "On my way back, I wave goodbye to Honey who spots me from the barn as I leave."
        show bg worldmapnight with dissolve
        play ambience ambiencenight
        "..."
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        if livingwithmoxie == 1:
            "By the time I get back to the wagon the sun has fully set, the sky is a stunning sea of stars."
            pause 0.5
            show bg moxiewagonlamp with dissolve
            show moxie laughing with dissolve
            "I let myself into the wagon and find myself pleasantly greeted by Moxie who naturally smiles upon seeing me."
            moxie "Evening [playername], how’s it going?"
            mc "I'm great thanks, definitely need a rest though."
            "I lay on her sofa, feeling exhausted, my muscles are heavy and aching. Moxie comes over and joins me."
            show moxie closehappyneutral with dissolve
            moxie "Where’d you end up working today?"
            mc "I went to the farm, Honey really put me to work there, I don’t think I’ve worked that hard all my life."
            if forestvisit1 == 1:
                mc "Except maybe the spelunking Butters made me do."
            show moxie closesmug with dissolve
            moxie "Ooohh, Honey eh? Check you out, you’re already calling her a nickname, sounds like you two got along fine."
            mc "Aha, you got me, she’s quite an assertive lady, definitely gets what she wants."
            show moxie closehappy with dissolve
            moxie "I can attest to that. Question on my mind is, did she get what she wanted?"
            mc "You mean sex? Nah, we didn’t do anything like that, but she was quite flirty, is that normal for her?"
            show moxie closeshocked with dissolve
            moxie "Hmm, I’m surprised to hear that she’s flirtatious, but all mares in heat can act slightly different around men."
            show moxie closehappyneutral with dissolve
            mc "Interesting… I met Blossom too, she seemed really shy, not at all assertive like her sister."
            moxie "She’s a lovely girl, I think they had slightly different upbringings, you’d assume two sisters would be alike, but I find that’s not always the case."
            mc "Well there’s one thing they have in common, they both seem flirty. Honeycrisp was quite confidently flirting with me, calling me a stud. Blossom was flirty too but so shy that she was stumbling over her own words."
            show moxie closelaughing with dissolve
            moxie "Chatting up two girls in one day I see, sounds like you are a stud!"
            mc "It felt like they were the ones chatting me ‘up’."
            show moxie closehappyneutral with dissolve
            mc "I need some quick Moxie expertise on something that happened. Only about thirty minutes ago Blossom asked me to go up to her room, she seemed to be propositioning me for sex, but then she was suddenly exceedingly shy about it."
            mc "Her body language almost seemed to indicate that she immediately regrets asking, any thoughts?"
            show moxie closelaughing with dissolve
            moxie "Hmm… She’s probably a virgin, and in heat. She saw you and in a momentary horny lapse of judgement she wanted to bone."
            show moxie closehappyneutral with dissolve
            mc "Wanted to bone? Expertly put Mox."
            mc "Are those moments of weakness normal for heat?"
            show moxie closeneutral with dissolve
            moxie "I guess so, heat can be insidious to the mind just like an addiction, sometimes willpower is required to restrain yourself."
            mc "Ahh, that helps me relate to it a little."
            mc "It’s like when I can’t stop myself from eating the last pizza slice."
            show moxie closelaughing with dissolve
            moxie "That’s an awful metaphor [playername], although I can definitely relate to Blossom."
            show moxie closehappyneutral with dissolve
            moxie "Remember the night you appeared? Even though I was confidently planning on sleeping with a ‘familiar’ I had an overwhelming surge of shyness and doubt when you arrived."
            show moxie closehappy with dissolve
            moxie "Sure, we ended up doing something anyway, but not immediately, we took a day to warm up to each other first."
            show moxie closehappyneutral with dissolve
            moxie "So even though she might want to have sex with you, it might take her a little while to get comfortable with you."
            mc "You’re right, me and Blossom only spoke for around ten minutes."
            mc "I think what she experienced was a knee jerk reaction to her heat rather than genuine desire to have sex with me. I don’t want to abuse that."
            show moxie closehappy with dissolve
            moxie "While I respect that, you don’t need to worry too much, these girls are capable of making their own decisions."
            show moxie closehappyneutral with dissolve
            moxie "Honestly, just go with the flow, next time she invites you up to her room, she might surprise you."
            "…"
            jump evening
        elif livingwithbutters == 1:
            "By the time I get back to the cottage the sun has fully set, the sky is a stunning sea of stars."
            pause 2.5
            show bg buttershousedark with dissolve
            show butters dresslaughing with dissolve
            "I let myself into the cottage and find myself pleasantly greeted by Butters who naturally smiles upon seeing me."
            butters "Evening [playername], how are you?"
            mc "I'm great thanks, definitely need a rest though."
            "I lay on her sofa, feeling exhausted, my muscles are heavy and aching. Butters comes over and joins me."
            show butters closedresshappy with dissolve
            butters "Where’d you work today? You look even more tired than after a good cave dive."
            mc "I went to the farm, Honey really put me to work under the sun, I don’t think I’ve worked that hard all my life."
            mc "The spelunking comes close though..."
            butters "Ooohh, Honey! You should get nice and strong so you can help me spelunk in even more dangerous areas."
            mc "Aha, she’s quite an assertive lady, definitely gets what she wants."
            show butters closedresshappy with dissolve
            butters "I can attest to that. Question on my mind is, did she get what she wanted?"
            mc "You mean sex? Nah, we didn’t do anything like that, but she was quite flirty, is that normal for her?"
            show butters closedresssurprised with dissolve
            butters "Hmm, she is quite flirtatious, she's at that age where she's looking for a man, I think."
            show butters closedresshappy with dissolve
            mc "Interesting… I met Blossom too, she seemed really shy, not at all assertive like her sister."
            butters "She’s a lovely girl, I think they had slightly different upbringings, but they're more similar than you may realize at first glance."
            mc "Well there’s one thing they definitely have in common, they both seem flirty. Honeycrisp was quite confidently flirting with me, calling me a stud. Blossom was flirty too but so shy that she was stumbling over her own words."
            show butters closedresslaughing with dissolve
            butters "Chatting up two girls in one day I see, you're terrible [playername]!"
            mc "It felt like they were the ones chatting me ‘up’."
            show butters closedresshappy with dissolve
            mc "I need some quick Butters expertise on something that happened. Only about thirty minutes ago Blossom asked me to go up to her room, she seemed to be propositioning me for sex, but then she was suddenly exceedingly shy about it."
            mc "Her body language almost seemed to indicate that she immediately regrets asking, any thoughts?"
            show butters closedresslaughing with dissolve
            butters "Hmm… She’s probably a virgin, and in heat. There can be a lot of conflicting emotions going through the head of a girl at her age."
            show butters closedresshappy with dissolve
            mc "Are those moments of weakness normal for heat?"
            show butters closedressneutral with dissolve
            butters "I guess so, I haven't had a lot of recent experiences with heat until just now, but I can definitely say it's easy to make bad decisions when you're young and dumb."
            mc "Ahh, that helps me relate to it a little."
            mc "It’s like when I can’t stop myself from eating the last pizza slice."
            show butters closedresslaughing with dissolve
            butters "Hehe, the last pizza slice needs to be savoured, [playername]."
            show butters closedressneutral with dissolve
            "…"
            jump evening
        else:
            pass
    label farmvisit2:
        "Time to go back to Honey’s farm and help her. Hopefully it won’t be eight hours of plucking apples again."
        "I’ll get a chance to meet with Blossom too, who knows what’ll happen today, especially with both girls flirting with me."
        stop music fadeout 5.0
        "Honey said ‘Let’s make an emphasis on hard next time’, those words have been stirring around in my head. With her main hand in a cast, she must have a lot of pent up sexual frustration."
        "Whether it’s Blossom or Honey, one of them is probably going to make their move onto my dick today, I’m excited."
        scene bg farm with dissolve
        "While I’m daydreaming about these two mares, I soon arrive at the farm, and low and behold Honey is already outside working. "
        show honeycrisp neutral with dissolve
        mc "From the first light of day to the last, isn’t that right Honey?"
        show honeycrisp closehappy with dissolve
        honeycrisp "Ahah, correct partner!"
        "She’s currently carrying about some small metal buckets."
        play music farm
        show honeycrisp closehorny with dissolve
        honeycrisp "I’m so glad you decided to come today, I have the perfect job for a stud like you."
        mc "A perfect job? You’ve piqued my interest."
        show honeycrisp closehappy with dissolve
        honeycrisp "Yep, I have a very special lady visiting today, and only a good-looking man like you will be able to give her what she wants."
        show honeycrisp closelaughing with dissolve
        honeycrisp "And I ain’t just talking about that thick-rod of yours. Since you ain’t got a cast on you’ll be able to massage breasts much better than me."
        mc "Massage her breasts?"
        "Is she trying to give me an erection? Her flirting is even more oppressive than last time."
        "Also, I have absolutely no idea what she’s talking about, special lady, thick-rod, massage breasts?"
        show honeycrisp closehorny with dissolve
        honeycrisp "Ahh, I see your little fella is getting excited."
        mc "You can tell?"
        show honeycrisp closelaughing with dissolve
        honeycrisp "With more than my eyes, stud."
        show honeycrisp horny with dissolve
        "She turns around and pops the metal buckets on the ground just outside the barn and scans me from bottom to top rather earnestly."
        honeycrisp "We’re going to work nice and hard today, getting an erection is only natural."
        honeycrisp "It’s making me more tingly than I expected, but we can’t let ourselves get distracted by lust, we have work to do."
        mc "What’s going to happen anyway?"
        show honeycrisp happy with dissolve
        honeycrisp "I have a cow girl visit once a week to be milked. But I'm too slow with my cast, so I need you to milk her breasts."
        mc "Oh, yeah I can see why getting an erection would be natural now, albeit embarrassing."
        honeycrisp "There’s nothing I can do for ya unfortunate erections."
        show honeycrisp horny with dissolve
        honeycrisp "However, there are more things that can be milked than just udders if you do a good enough job."
        "This girl has a surprisingly dominant streak of flirts going, I can’t say I didn’t expect it, but I’m still amazed."
        menu:
            "She stares at me with a salacious expression."
            "You’re really horny this morning.":
                honeycrisp "it’s hard for a girl like me out here."
                honeycrisp "No men to speak of, I haven’t had any action since heat began."
            "Is today the day we’re going to have sex?":
                honeycrisp "I’m resisting the urge to take you into the barn right now, stud."
        show honeycrisp laughing with dissolve
        honeycrisp "Hah, sorry stud, my appetite for sex has been out of control recently. I can dial down the  flirting if you'd like."
        mc  "I don't mind, that's how heat goes, right?"
        show honeycrisp happy with dissolve
        honeycrisp "You know, cow go into heat this time of year too, can you imagine just how worked up she’d get if a male was milking her nipples?"
        honeycrisp "I bet you're getting excited too."
        mc  "A little."
        show honeycrisp ass with dissolve
        honeycrisp "How about now, hm?"
        mc "Damn Honey..."
        honeycrisp "I've been thinking about you stud."
        show honeycrisp horny with dissolve
        honeycrisp "I can't wait to see how excited you'll get milking Anna's breasts."
        mc "It’s just like playing with their breasts isn’t it? There’s no way I won’t get excited."
        show honeycrisp satisfied with dissolve
        honeycrisp "Ohoh, no, no, y’all may be a stud but y’all naïve."
        show honeycrisp happy with dissolve
        honeycrisp "Milking a cow lady is so much more than that, you have to be an expert with your fingers, ease her into it with a massage, comfort her and excite her."
        mc "Are you implying what I think?"
        show honeycrisp laughing with dissolve
        honeycrisp "Maybe I am, maybe I’m not, Anna is a close friend of mine, I always milk her, but she told me she lactates so much more if it’s a guy."
        honeycrisp "How about we test that theory?"
        show honeycrisp happy with dissolve
        honeycrisp "We’re killing three birds with one stone, I treat Anna to a charming boy, you get the opportunity to play with a delightful girl and I get to watch a great show. Yeehaw!"
        "Have I been led into some bizarre threesome by a horny mare? If this is real, I think I’m in love with Arcadia."
        menu:
            "You’ve set me up to have sex with a cow girl?":
                show honeycrisp laughing with dissolve
                honeycrisp "Hmm, ‘setup to have sex’ is pushy wording."
                honeycrisp "Setup for the opportunity, now that’s more like it."
            "I’d much rather you join in.":
                show honeycrisp laughing with dissolve
                honeycrisp "Aye, I might, I wasn’t planning on it, but my heat is kicking in fiercely."
            "I’d prefer to do it with just you Honey.":
                show honeycrisp laughing with dissolve
                honeycrisp "Sugarcube, just you wait, and we’ll see if you think that in thirty minutes."
                honeycrisp "You can have me any time you want, but this girl? She's a rare catch."
        show honeycrisp shocked with dissolve
        honeycrisp "I think I see her!"
        "Honey points down the path as a busty figure appears on the horizon."
        show honeycrisp happy with dissolve
        honeycrisp "There’s mah girl, you stay here stud, I’m going over to say hi!"
        honeycrisp "Oh, I nearly forgot, could you put these buckets into the barn and wait there?"
        hide honeycrisp happy with dissolve
        stop music fadeout 5.0
        show bg barn with dissolve
        "I pick up the buckets and make my way into the barn. I’ll have to use this short amount of time to compose myself."
        "What exactly have I gotten myself into? Are two horny and dominant girls about to have their way with me?"
        "It isn’t long until I see Anna the cowgirl peep into the barn and step in."
        show anna happy with dissolve:
            xpos 700
            ypos 10
        show honeycrisp horny with dissolve:
            xpos 200
            ypos 30
        anna "Hey there cutie, I heard you’re taking shift on milking. The name’s Anna, splendid to meet you!"
        "Woah-ho! She's thicc!"
        hide anna happy with None
        hide honeycrisp horny with None
        show anna boobs with dissolve
        "Look at the size of those-"
        hide anna boobs with dissolve
        show anna happy with None:
            xpos 700
            ypos 10
        show honeycrisp horny with dissolve:
            xpos 200
            ypos 30
        mc "Hey Anna, name’s [playername]. The pleasure is mine."
        show honeycrisp laughing with dissolve
        honeycrisp "Three’s a crowd, but how about I go make us some drinks while y’all get acquainted."
        hide honeycrisp laughing with dissolve
        play music day2
        "Honey winks at me as she leaves. Just what is she up to?"
        hide anna happy with dissolve
        show anna closelaughing with dissolve
        "Anna meanders over and sits on one of two wooden stools that are conspicuously placed next to each other."
        anna "Hehehe, that girl... Setting us up like this."
        mc "I know right?"
        show anna closehappy with dissolve
        anna "You have no idea how much I’m looking forward to getting these boobies drained though, I was so worried Hun wouldn’t be able to do it."
        mc "No worries, I’m helping out Honey any way I can."
        show anna closelaughing with dissolve
        anna "You’re doing a wonderful thing. I think Hun needed some help considering everything that happened, low and behold she managed to employ a dashing young man."
        anna "I guess she doesn’t need my help when she has a treat like you by her side."
        mc "A treat, am I?"
        show anna closesurprised with dissolve
        anna "Ohh yes, you’re visually interesting, I can see all your skin and muscles."
        show anna closehappy with dissolve
        anna "If I may be so rude, may I touch your body?"
        mc "Sure thing, no harm in curiosity if you’ve never seen a creature like me."
        show anna closelaughing with dissolve
        anna "I hope we'll get better acquainted with each other’s bodies soon, hehe."
        show anna closesatisfied with dissolve
        "Anna runs her hands up and down my thighs, her hands are covered in a soft fur that is pleasant to the touch, it’s notably thicker, and more rugged than a pony's."
        show anna closehappy with dissolve
        anna "Mmm, how soft and exquisite. What creature are you? Wingless dragon? Furless pony?"
        mc "Nahh, nothing that surprising, I’m just a human."
        show anna closesurprised with dissolve
        anna "Oooo, hoo-man, I’ve never met one before. I’m thrilled to though! You don’t seem to be like those brutish minotaurs or stallions."
        mc "Brutish? I’ve never heard anyone call stallions that before, and minotaurs sound a little scary."
        show anna closehappy with dissolve
        anna "Hmm, you’re not from around here, are you?"
        mc "Heh, you've figured me out."
        label farm2annameet:
            menu:
                "Can you tell me about minotaurs?":
                    show anna closeneutral with dissolve
                    anna "Hehe, well, minotaurs are the male variant of cow girls. They're our natural breeding partner, but we have an unusual culture where the men and women live separated until mating season."
                    anna "Unfortunately minotaurs tend to be overbearing, selfish and monogamy is rarely practiced. Most cow girls are okay with this, but my standards are a little higher!"
                    jump farm2annameet
                "What's wrong with stallions?":
                    show anna closeangry with dissolve
                    anna "Stallions are different, they’re narcissistic, they think they’re Queen Aurora’s gift to the world just because there’s a shortage of them, so sometimes they won’t even pay heed to us 'lower' breeds."
                    mc "That sounds horrible, why would they act like that?"
                    show anna closeneutral with dissolve
                    anna "Due to the shortage of stallions, they have a larger dating pool, and as such they only take the best pickings from the tree. Usually rich and successful mares will marry them."
                    anna "Sounds pretty boring to me."
                    jump farm2annameet
                "Can you tell me a bit about yourself?":
                    show anna closelaughing with dissolve
                    anna "Why, I’m a farmer just like Hun over here! I work at a similar place about half an hour away in a village occupied by heifers!"
                    mc "Uh, what’s a heifer?"
                    show anna closehappy with dissolve
                    anna "A heifer is just a name for a cow that hasn’t had a calf yet. You could call it a cow village if you'd like."
                    mc "Wait a second, are you the cow farmers Blossom talked about? "
                    anna "That’ll be us! No other cow farmers out here for miles over yonder."
                    anna "I’m a real ambitious type though, maybe you’ll see more farms pop up in nearby villages. With Arcadia situated nearby, there is always a market for crops and milk."
                    "Interesting… I should talk to Blossom about this."
                    jump farm2annameet
                "(Proceed)":
                    anna "Hehe, you can see why I want to remain single and childless for a while. I'm a career lady first and foremost."
        mc "Wait, if you’ve never had a calf, how are you producing milk?"
        show anna closesurprised with dissolve
        anna "Sexually mature cows always produce milk."
        show anna closelaughing with dissolve
        anna "Does your species only make milk when pregnant?"
        mc "Yeah, that’s how it works for a lot of mammals where I’m from."
        show anna closehappy with dissolve
        anna "Us cow girls always produce milk, we’ve evolved that way, maybe you'll figure out why a bit later."
        anna "Where are you from anyway? What brings such a fine hoo-man here?"
        if days >= 10:
            mc "I haven't been here long, I've been living a fairly new life."
        else:
            mc "I just moved into town, looking to start a new life."
        show anna closelaughing with dissolve
        anna "Awh that's so sweet, if there's anything you need, I'd love to help you."
        mc "That's very generous of you. I’m grateful to meet so many amazing people here, and in particular gorgeous girls."
        show anna closehappy with dissolve
        anna "Ooohh, are you saying I'm gorgeous too? Hehe, I'm glad you're the one milking me today, I'm already excited."
        mc "That’s just going to be milking right? Doesn’t Honey do that to you?"
        anna "Mhm, but even when Honey does it, I get a teeny bit excited, hehe… I’ve always wanted to try it with a man, not a minotaur though!"
        show anna closesatisfied with dissolve
        anna "Oh gosh, it’s that season too, I have no idea what’s going to happen."
        mc "This is a first for me too."
        show anna closehappy with dissolve
        anna "Let’s just have some fun, [playername]."
        "I notice her tail swishes when she’s happy, ponies don’t do that, but it’s adorable seeing Anna giving away how she feels so easily."
        "The atmosphere she radiates is incredibly positive and upbeat, I could see the two of us becoming great friends."
        "I hear some steps on the grass outside the barn as Honeycrisp returns."
        hide anna closehappy with None
        show anna closehappy with None:
            xpos 600
            ypos 50
        show honeycrisp laughing with dissolve:
            xpos 200
            ypos 30
        honeycrisp "Howdy y’all, I have some fresh, cold cider prepared, perfect for a long arduous milking session."
        show anna closelaughing with dissolve
        anna "Perfect Hun! Your cider always cools me down on a sweltering day like this."
        show honeycrisp horny with dissolve
        honeycrisp "Only for me to warm you right back up, ain’t that right?"
        show anna closesatisfied with dissolve
        anna "Oh Hun, you shouldn’t say such lewd things with our friend here."
        mc "Don’t worry about me, after all, I’ll be the one warming you up today."
        show anna closelaughing with dissolve
        anna "Ahah, you can’t both be perverts! I can’t handle that."
        show honeycrisp laughing with dissolve
        honeycrisp "Our stud here will have his work set out if he plans on out-perving me!"
        hide honeycrisp with None
        show honeycrisp closehappy with dissolve:
            xpos 0
            ypos 30
        "The three of us enjoy some refreshing cider as we banter back and forth."
        show honeycrisp closelaughing with dissolve
        show anna closehappy with dissolve
        "After thirty minutes I feel slightly drunk and the two girls are undoubtedly going to be tipsy too."
        "From what I’m gathering the milking takes hours, so the girls usually make the most of their time together, talking, having drinks and having lunch."
        "It's clear that they’re great friends, the chemistry they have together is infectiously potent, even if it is platonic."
        "As Anna pours the last drop of cider from the pitcher into her mug, Honeycrisp speaks up."
        show honeycrisp closehappy with dissolve
        show anna closesatisfied with dissolve
        honeycrisp "Alright stud, time for you to work your magic on the lucky lady."
        "Anna blushes as she takes another sip of cider. She then leans towards me and wiggles her bosom at my face."
        hide honeycrisp closehappy with None
        hide anna closesatisfied with None
        $ annamilking = 0
        label annamilking:
            stop music fadeout 10.0
        stop music fadeout 10.0
        show anna boobs with dissolve
        show bg barnblur with dissolve
        anna "All yours sugar."
        "The alcohol did its work, the atmosphere feels great, there isn’t a hint of shyness in anyone now that we’re all sufficiently warmed up and tipsy."
        show anna boobs2 with dissolve
        "I inch my stool a little closer, so Anna’s breasts are right in front of my face."
        "Upon closer inspection, I can see faint white drops already on her nipples."
        anna "Oh my, I’ve already dripped a little…"
        "I think that means she’s aroused, although I think all three of us are, the pheromones in the air are certainly getting to me."
        honeycrisp "Don’t let any escape sugarcube, get as much as you can in this here bucket."
        "Honey takes one of the buckets and places it below us."
        mc "Okay, so what do I do now? Just squeeze?"
        honeycrisp "First, you’ll have to stimulate her. Those are fancy words for massage her until she’s wet."
        anna "B-but Hun, I’m already…"
        honeycrisp "Shh sugar, I need to train him properly.  [playername], y’all have to stimulate a cow girl first before she’ll lactate."
        play music sex1 fadein 10.0
        show anna milking1 with dissolve
        "I start by massaging her breasts with my hands, kneading them with my fingers, they feel overwhelmingly soft."
        "I think I'm doing something right, because she reacts extremely favourably to each and every touch."
        anna "Mmmphh…"
        "She’s enjoying herself so much that her eyes are practically rolled back and some milk starts dripping down, it’s a slow natural drip though, and fortunately every drop lands in the well placed bucket below us."
        anna "Oh gosh… I-I’m leaking…"
        "I’m fully erect at this point, I can’t help myself. The pheromones and flirting were stimulating enough, but now I’m massaging these stunning breasts, so I can’t help but get aroused."
        honeycrisp "You can massage other areas too y’know, actually the breasts are usually the last area I massage, but feel free to explore her body any way you want stud."
        "I peek over to Honey, she’s watching with glee, sat on a stool perpendicular to us smugly sipping cider."
        "As I turn back to look at Anna, her eyes are closed as she completely submits to the sensations, she even stifles a slight moan."
        hide anna milking1 with None
        show anna milking1 with dissolve:
            xpos 425
            ypos 0
        show annapussycloseup with dissolve:
            xpos 0
            ypos -75
        "As she submits, she leans back a little and parts her legs, subsequently her thighs, revealing her glistening pussy to me. "
        anna "Haahh… It has never felt this good before…"
        "Her puffy labia is enticing, I follow her invitation and begin to deftly tease her inner thighs, narrowly avoiding her sensitive areas."
        "As my fingers brush against the fur of her thighs, she adorably wiggles every time I get close to her pussy."
        "My other hand continues to knead into her breasts, every so often I can hear a metal clang as another drop of milk lands in the bucket."
        "I was too distracted by teasing her pussy that I hadn’t even noticed how much she was beginning to lactate. Drip, drip, drip, into the bucket below. "
        honeycrisp "Well I’ll be, you’re a natural. All you’ll need to do now is work the nipples, they’ll release lots of milk."
        "I wanted to continue teasing Anna, I really wanted to sink my fingers deep into her wet pussy, but I do have a job to prioritise, the lewd acts can wait."
        "I bring both of my hands to Anna’s nipples and vaguely point them down in the bucket before pinching them slightly."
        "*Squirt*! A stream of milk immediately trickles out the moment I put any pressure on, all seeping down into the bucket, some of it getting sodden in the fur surrounding Anna’s breasts."
        anna "Mmphh, so sensitive…"
        "I pinch harder, then soften my grip, then I squeeze again, pulling the nipples towards the bucket. *Squirt*!"
        "Applying pressure to the nipples in a regular pattern, pulling and squeezing one then the other, the milk squirts out in intervals while Anna squirms in delight."
        "Lots of milk flows out of her breasts and directly into the bucket."
        anna "Ahh, I-I want to make you feel good too…"
        "Rather suddenly, I feel Anna lean over, her face nearing mine as I continue to milk her."
        show annahandjob with dissolve:
            xpos -69
            ypos 325
        "I assume she’s about to kiss me, but to my surprise I feel her fluffy hand wrapping around my erection, looks like my erection hadn’t gone unnoticed."
        honeycrisp "Ohh, now we’re talking! Work that shaft girl, milk him just like he’s milking you!"
        "Spurred on by Honeycrisp’s words, Anna’s hand tightens around my shaft and begins to jerk me off."
        "She’s doing it with her eyes closed, making it sloppy, but it still feels great."
        "She freely moans and enthusiastically works my shaft while I pinch her nipples. Now we’re both feeling good."
        "I do my best to concentrate on the milking, Anna’s lactation had already peaked and the amount of milk trickling from her nipples was starting to decrease."
        "The squirts of lactating milk from each squeeze of her nipples eventually turn into a trickle which inefficiently runs down her breasts rather than dripping into the bucket."
        hide annahandjob with dissolve
        "As I’m realizing this, Anna stops jerking me off and wearily looks down at her bosom. "
        anna "Ohh… Hun, I think I’m done filling the bucket, but… There’s a little more…"
        honeycrisp "You know what to do then, sugarcube."
        anna "Right!"
        hide anna milking1 with None
        hide annapussycloseup with dissolve
        show anna boobs2 with dissolve
        "I stop working her nipples and Anna leans in really, really close"
        "Her breasts are right in front of my face. Up close her moist fur sheens with the milk."
        anna "You’ll have to… suck to get the last bit out…"
        mc "What about the bucket? "
        honeycrisp "Don’t worry about the bucket stud, you got us plenty, a few more drops won’t change much."
        "Honey dips between us and takes the bucket out of our way, it sloshes about half full of milk."
        honeycrisp "Anna still has a tiny bit of milk left; you’ll only be able to get the rest out by sucking."
        mc "Sucking? Are you sure?"
        anna "Mhm, my breasts feel heavy and swollen if they have too much milk, I like to try and get rid of as much as possible."
        "I’m so aroused I can’t decline the opportunity to suck her nipples, even though she’ll be lactating."
        "It’s only milk though, I’ve had that plenty of times, so I shrug it off and use my hands to bring one of her drippy nipples to my mouth."
        show anna milking2 with dissolve
        "I take a moment to lick around the pinkish areola, my tongue moves around in a few circles before focusing on her erect nipple, even as I’m licking a few drops of her milk trickle down my tongue."
        play sound cum
        "My lips wrap around the nub and begin sucking, Anna is quick to let out a cute whimper in response."
        "It takes a moment, but my mouth is suddenly intruded by a stream of surprisingly warm liquid, it is pleasantly refreshing, enough to prompt me to suckle harder."
        play sound cum
        anna "Oh Aurora, this is the hottest thing I’ve ever done…"
        hide anna milking2 with None
        show anna milking2 with dissolve:
            xpos 500
            ypos 0
        show annahandjob with dissolve:
            xpos -69
            ypos 325
        "I feel her furry hand once again wrap itself around my stiff shaft and she wastes no time in jacking back and forth."
        show anna milking3 with dissolve
        "As the milk from this first nipple seems to dry out, I pull back and move to the next nipple, eagerly wrapping my lips around it and starting to suck."
        play sound cum
        show annapussycloseup with dissolve:
            xpos 0
            ypos -75
        hide annahandjob with None
        show annahandjob with dissolve:
            xpos -69
            ypos 325
        "Anna squirms in delight causing her hand movements to get erratic, she leans into me, all of her body language is begging for more."
        "She’s incredibly aroused and her legs spread once again giving me a glimpse of her pussy whenever I want."
        "More of the milk trickles into my mouth, warm and enticing. As it coats my mouth and drips down my throat it refreshes and invigorates me, drinking this strange milk just feels wonderful. "
        "I close my eyes and give in to all the sensations, my cock throbs as Anna starts to speed up, I can feel myself potentially getting close to climax."
        "I suck harder but the milk stops coming, and Anna’s hand job slows down quite considerably."
        show anna closehappy with dissolve:
            xpos 500
            ypos 50
        "I drop her tiddy from my mouth and wipe my lip dry with the back of my forearm."
        show anna closehorny with dissolve
        anna "Looks like you milked me all dry! But look at your cock… It’s still so swollen and hard…"
        "She is still jacking me off, unable to keep her eyes away from my dick."
        hide annahandjob with dissolve
        show anna closesmug with dissolve
        "She stops for a moment, her expression is that of hazy bedroom eyes and a blush, she seems completely infatuated at this moment. "
        anna "How about I milk you with my mouth, just like you did to me?"
        mc "Please do."
        anna "Mmm…"
        play ambience blowjob
        show anna blowjob with dissolve:
            xpos 500
            ypos 0
        "Wordlessly she kneels down in front of my cock and enthusiastically brings the tip to her lips and begins to suck it."
        "She playfully suckles the tip, as if she was milking a nipple, her lips tightly gripping around my glans and smoothly moving back and forth. Holy shit this feels good."
        "With a quick peek to my side, I remember that Honey has been watching us this entire time, albeit quietly."
        hide annapussycloseup
        hide anna blowjob
        show honeycrisp masturbating
        with dissolve
        "I don’t know when Honey started, but she let her hair down and now she's leaning back comfortably rubbing her pussy as if she were watching porn."
        honeycrisp "Enjoying yourself, stud? I know I am."
        "Teasingly she spreads her pussy for me, however as if competing for my attention Anna starts to sloppily swirl her tongue around my tip causing a shiver of pleasure to jolt my body upright."
        hide honeycrisp masturbating with None
        show annapussycloseup with None:
            xpos 0
            ypos -75
        show anna blowjob with dissolve:
            xpos 500
            ypos 0
        "Okay, this is really hot, even hotter than five minutes ago, and that was already fucking hot."
        anna "I think ish too big… It won’t fit in my mouth."
        honeycrisp "Anna, your head is so cloudy with erotic thoughts, that you forgot your best assets."
        mc "What do you mean?"
        "Anna turns to Honey, to get quite a surprise."
        anna "Wha? You perv! You’re touching yourself!"
        honeycrisp "Oh, please sugarcube, y’all have your mouth wrapped around his cock."
        honeycrisp "If you’re struggling to take it, just use your breasts, they’re definitely big enough."
        hide annapussycloseup with None
        hide anna blowjob with None
        stop ambience
        show anna closesurprised with dissolve
        "Anna squishes her breasts together next to my cock for a few seconds confused before she suddenly glows with enthusiasm."
        show anna closelaughing with dissolve
        anna "Ahh, I get it!"
        "Moxie wasn’t kidding when she said I’d get a lot of crazy experiences, I’m about to get a genuine breast job from a cowgirl."
        hide anna closelaughing with None
        play ambience sex
        show anna paizuri with dissolve:
            xpos -60
            ypos 0
        "Anna lifts herself up slightly and clamps her breasts around my cock, completely squishing my shaft with a surprising tightness."
        show honeycrisp masturbating with dissolve:
            xpos 600
            ypos 0
        "And to my side, Honey is rubbing herself fervently, this is like a sex fantasy."
        "Anna uses her arms to squish her breasts together against my cock while she leans forward."
        "Her breasts feel so soft around my cock and they’re slightly damp too, it’s a snug fit."
        "She starts raising her torso up and down, so her breasts stimulate my shaft."
        anna "Mmphh, so good…"
        "Lewd sloppy wet sounds keep coming from her breasts as she drools down onto my cock, providing some lubrication. That combined with the surprising tightness, the pleasure is overwhelming."
        "It won’t take me long to cum at all, I can even hear Honey moaning as she onlooks!"
        "Anna holds her breasts even tighter as she glides up and down my shaft. It feels so skin-tight, wet with drool, and sweat that it’s genuinely like fucking someone."
        "I can’t hold back much longer, this is too good... I can feel my orgasm building up quickly."
        anna "Cum for me, cum for me!"
        "Using both her hands she slides her breasts back and forth against my dick, far faster than she could by moving her entire body, it completely overstimulates my senses and pushes me over the edge."
        "I can’t take another second of her paizuri and start to ejaculate, shooting several thick loads all over her."
        play sound cum
        play sound cum
        show anna paizuricum with cum
        anna "Ahh, ahh… ahh! So-So much!"
        play sound cum
        play sound cum
        show anna paizuricum with cum
        "She keeps her breasts moving back and forth the entire time overall resulting in an explosive and satisfying orgasm."
        stop ambience
        stop music fadeout 10.0
        play ambience ambienceday
        anna "Mmm, I milked you dry too, hehe!"
        scene bg barn with dissolve
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        "For a few moments, the barn returns to relative normalcy. Everyone is panting, and feeling a little bit of fatigue from what had just occured."
        mc "That felt so good, you two teased me for so long."
        "Honeycrisp ties her hair back up, having given up masturbating, seemingly unable to get herself off."
        show anna closesatisfied:
            xpos 600
            ypos 50
        show honeycrisp closelaughing:
            xpos 0
            ypos 30
        with dissolve
        honeycrisp "Phew, how do you think we feel? We got teased exactly the same amount of time and neither of us got to cum ourselves!"
        show anna closesurprised with dissolve
        anna "Ohh… I guess not. I'm still horny!"
        show honeycrisp closehappy with dissolve
        mc "Ah, I was hoping you’d come from your nipples being stimulated, Anna."
        show anna closehappy with dissolve
        anna "I-I nearly came, but it’s hard from just my nipples, it made me really wet though."
        mc "What about you Honey, you were basically just masturbating back there."
        show honeycrisp closesad with dissolve
        honeycrisp "I’m right-handed boo, I don't come easily through masturbating, and I just can’t seem to do it with my left, drives me mad."
        "She waves her casted right hand around. "
        "These two girls aren’t finished with me yet; I need a break first though."
        "(If you’re playing along at home, you might want to take a break here too.)"
        show honeycrisp closehorny with dissolve
        show anna closehorny with dissolve
        "They huddle up together and whisper among each other, I wonder what they’re scheming?"
        "I’m still recovering from my orgasm, but if they give me some time, I’d be more than willing to go again."
        show honeycrisp closehappy with dissolve
        show anna closelaughing with dissolve
        honeycrisp "Alright, I’m starting to sober up, so I’m going to get another pitcher of cider. Should give you enough time to recover, right?"
        mc "Should be, but uh, what are we going to do?"
        show honeycrisp closelaughing with dissolve
        honeycrisp "Oh, come on, what do you think we’re going to do? Each other."
        hide honeycrisp with dissolve
        show bg barn with dissolve
        show anna horny with dissolve
        play music day2
        "Honey hops out of the barn with the bucket of milk and empty pitchers."
        anna "She’s such a perv, isn’t she?"
        mc "She sure is, I bet she was whispering something naughty to you."
        hide anna horny with None
        show anna laughing with dissolve
        anna "Aha, she told me I have to wait for your refactory period or something, but as soon as it’s over you’ll be able to go again!"
        mc "It's refractory, and it’ll take about fifteen minutes, otherwise it’s too sensitive and uncomfortable."
        anna "Then hopefully Honey was right about my milk! It should make you ready and rearing to go in no time!"
        mc "Your milk? What does it have to do with my boner?"
        show anna surprised with dissolve
        anna "Ohh, you don’t know? A cow girl’s milk is a soft aphrodisiac."
        mc "Wait a minute, what the heck?"
        show anna neutral with dissolve
        anna "Y-You didn’t know?"
        mc "Why would I know? I’ve never met an anthropomorphic cow before, I thought the milk was just for drinking and feeding young."
        show anna surprised with dissolve
        anna "Awh… I feel bad now… Our milk is double use as food and aphrodisiac."
        show anna laughing with dissolve
        anna "Minotaur cum is the same and even more potent, but no one wants to collect that…"
        mc "I feel like everything in this world is encouraging me to have sex, except the minotaur thing of course."
        show anna happy with dissolve
        anna "Ahah, really? What do you mean?"
        mc "Where do I start? Two girls in heat, getting me slightly drunk, flirting with me, and now giving me aphrodisiacs."
        mc "I’m having the time of my life, but I’m half expecting to just wake up back in my bed with it all a dream."
        anna "Sounds like you’re hanging around with the right crowd! We’re cool!"
        mc "Yeah, Honey is quite the character, I think being unable to get herself off is making her get a little loopy."
        show anna laughing with dissolve
        anna "I think Hun totally set us up."
        show anna horny with dissolve
        anna "Not that I’m complaining, you’re a charming young man, I’m grateful to share such a fun day with you."
        mc "So, we’re probably going to have sex. What do you think?"
        show anna surprised with dissolve
        anna "Ohh boy, hah… No need to be so upfront about it, you’ll make me swoon."
        show anna happy with dissolve
        anna "I have a dildo at home, but it never quite satisfies during heat."
        anna "I want to have sex, but I live in a female only village and I don’t want to have sex with a minotaur, I’d get pregnant for sure."
        show anna neutral with dissolve
        anna "If I get pregnant, I can kiss my career goodbye, you know? Haha."
        mc "I can definitely see the appeal in an interspecies relationship then."
        show anna happy with dissolve
        anna "Yup, you’re risk free and perfect for me… Honey knew what she was doing when she set up this erotic atmosphere, she’s hoping she’ll sate all three of our appetites in one explosive threesome."
        hide anna with dissolve
        show anna pussycloserup with dissolve:
            xpos 0
            ypos -300
        "She sits back down and spreads her legs again, she’s soaking wet."
        "I can't wait to put my dick in that."
        anna "When she whispered in my ear, she said we’re both going to fuck you…"
        anna "Ahh… I’ll be honest, I’m so horny thinking about it right now I’m struggling to see straight, I’ve just been peeking at your cock this entire time hoping it grows. "
        "I can feel blood half-heartedly rushing back to my cock as her words and the erotic sight of her stir arousal within me. "
        mc "I should be ready to go in a few more minutes."
        hide anna pussycloserup with None
        show anna closehorny with dissolve
        "To my surprise, I’m starting to get erect again, there’s a notable lack of sensitivity too."
        mc "Actually… This feels unusually okay, it feels like I didn’t even cum earlier."
        show anna closelaughing with dissolve
        anna "Mmm, that’ll be my milk, it’s designed to keep two lovers going for a long time."
        mc "Oh, this stuff removes the refractory period?"
        show anna closehappy with dissolve
        anna "I think so! A cowgirl and a minotaur will go for hours, cumming up to ten times. Pregnancy is almost guaranteed, that’s why we have a separate village for heifer that don’t want to get pregnant yet."
        mc "I see… I can certainly see why that’s evolutionarily beneficial."
        mc "So you’re telling me I should be able to keep going?"
        show anna closehorny with dissolve
        anna "Haha… I don’t know, but sometimes when I’m feeling naughty, I’ll suck my own nipple and it turns me on a lot."
        "To my bewilderment, I’m already erect, the aphrodisiac must have finally worked its magic."
        hide anna closehorny with None
        show anna pussycloserup with dissolve:
            xpos 0
            ypos -300
        "I feel energetic and ready as if it was the first time all over again. I’m aroused and Anna is presenting herself to me"
        anna "Mmph fuck, I don’t know if I can wait for Hun, maybe just the tip?"
        honeycrisp "Easy there sugarcube, I won’t let you have all the fun!"
        hide anna with None
        stop music
        play music challenge
        show anna lsurprised with dissolve:
            xpos 100
            ypos 30
        show honeycrisp happy with dissolve:
            xpos 750
            ypos 30
        "Eep! Anna thumps her thighs shut as Honey surprises the two of us, carrying a jug of her icy cider."
        honeycrisp "Figured you two worked up a sweat doing all that milking, so how about we cool down before we heat back up?"
        show anna lsatisfied with dissolve
        show honeycrisp shocked with dissolve
        honeycrisp "B-Blimey, are you erect already, stud?"
        mc "You know me, hardworking and reliable. "
        show honeycrisp horny with dissolve
        honeycrisp "Well I’ll be... I picked the right man for the job."
        "Honey fills our mugs before pouring herself half a mug of her cider which she necks in one go."
        show anna lhappy with dissolve
        "Anna thirstily gulps hers down."
        "I’m not that thirsty, considering the milk, I just have a sip of mine."
        show anna lsurprised with dissolve
        honeycrisp "[playername], I should let you know that I invited Anna here to have sex with me, and you happened to show up at the right time."
        show anna lhorny with dissolve
        anna "H-Hun! Eh... I guess there's no hiding it."
        show anna satisfied with dissolve
        show honeycrisp laughing with dissolve
        mc "Really? You two do that often?"
        "I look at Anna and expect her to be embarrassed, but she’s far too horny to care."
        show honeycrisp happy with dissolve
        honeycrisp "It’s not that unusual for girls to do those kinds of things during heat, but imagine my surprise when I get a man willing to join us on that same day."
        mc "What can I say? I came to help anyway I can. I expected a lot of physical exercise, but I didn’t think it’d be this fun!"
        show honeycrisp closelaughing with dissolve:
            xpos 550
            ypos 50
        honeycrisp "Mmm, that’s what I like about you stud, always willing to try your hardest."
        show honeycrisp closehorny with dissolve
        show anna lsurprised with dissolve
        "Honey kneels closely beside me and reaches out for my penis, exploring it clumsily with her left hand. Anna gasps as she watches in awe."
        show honeycrisp closeshy with dissolve
        honeycrisp "It’s difficult with my left hand."
        "She begins jerking me off lightly."
        show honeycrisp closehorny with dissolve
        honeycrisp "You have no idea how much I want to ride your cock right now. But that wouldn’t be fair for Anna…"
        show anna llaughing with dissolve
        honeycrisp "We’ve seen how you deal with one girl. Think y’all be able to please two girls begging for your cock?"
        "She stands up and moves over to some hay bales."
        hide honeycrisp with dissolve
        honeycrisp "Over here Anna, copy me."
        show anna lsurprised with dissolve
        anna "Oh?"
        $ honeyannathreesome = 0
        label honeyannathreesome:
            stop music fadeout 5.0
        stop music fadeout 5.0
        stop ambience fadeout 5.0
        "Honey gets on her knees and presents her ass, using the hay bales to hold her up."
        anna "Oh my… Such a lewd pose…"
        scene bg barnblur with dissolve
        anna "Okay, okay! I can’t hold on anymore."
        show honeycrispannab threesome
        show honeycrispanna threesome1
        with dissolve
        play music sex1 fadein 60
        "Anna scurries over and mirrors Honey’s pose, leaving me with two amazing asses presenting themselves to me. Their pussies both dripping wet, needy and in heat."
        "Honey is looking back expectantly, while Anna is wiggling her butt desperately."
        "With my cock ready to go, I choose to start with Anna, she’s undoubtedly in a horny stupor right now and needs some sense fucked into her."
        play ambience sex
        show honeycrispanna threesome2 with dissolve
        "I position my cock at her pussy and slowly push forward, easily sinking inside, her warmth is inviting and squeezes against my shaft."
        anna "Aaahhhh, ahh!"
        "Anna’s whole body reacts with a shiver of pleasure, culminating in a loud moan that escapes her mouth and echoes off the barn walls."
        honeycrisp "Mmphh… you took it all in so quickly, you’re a perverted girl after all this time, Anna."
        anna "Eheh, I’ve had some practice with my dildo, but ahhh, this cock feels far better…"
        "I can see Honey biting her lip as she looks on, her left hand is between her legs, prepared to rub herself as she watches and waits for her turn."
        "I start to move my hips; my cock comfortably slides back and forth inside Anna. She’s so wet that as I pull out, I can see the entirety of my cock coated in a sheen of that wetness."

        "Every time I slide in, I can feel her insides tighten around my cock, enhancing the pleasure for both of us at the peak of each thrust."
        anna "F-Finally, ahh! This is incredible! T-Thank you, thank you!"
        "She starts rocking her hips, making her butt rhythmically bounce into me, enthusiastically intensifying each thrust."
        "Every time our bodies meet there’s a satisfying thwap sound along with the girls’ moans."
        show honeycrispanna threesome3 with dissolve
        anna "This is the best thing ever! Ahhhh! Ahhh!"
        "Her pussy feels astounding around my cock right now, it’s overwhelming my senses."
        "It wouldn’t take me long to cum deep inside this girl’s tight pussy, but I’m hoping I can get her to come once or twice before I finish inside."
        "I decide to help her out by using my hand to rub her clit."
        "This drives Anna absolutely wild, her back arches and her entire body trembles, some of her hairs stand on end!"
        anna "F-F… F-F-Fuck!"
        "She can barely contain herself, she’s in complete ecstasy."
        anna "Ahh, k-keep going, I’m… Aaaiiiieeeee!"
        "Her moans are reduced to adorable squeaks as her hips buckle and a strong orgasm consumes her. "
        "Anna even squirts onto my rubbing finger and thighs as she climaxes."
        anna "Gosh, so good… D-don’t stop! I want more!"
        "I wasn’t planning on stopping. If anything, I’m going even quicker and harder so I can fill her pussy up with my cum before moving on to Honey."
        "I have to stop rubbing her clit and hold her ass tightly in order to speed up, but Anna is soon to replace my hand with hers as she starts to rub herself."
        "Perfect, now I can go as hard as I want. After a long morning of teasing and flirting, I’m finally going to get what I want by deeply filling this cow girl."
        anna "Ahh! C-Cum inside me, I want it all!"
        "Her words enthuse me as my orgasm begins to swell up, her pussy feels euphoric right now. "
        anna "It feels so good, I-I’m going to... Again!"
        "Her insides contract around my cock and she squirts even more this time, but all I can concentrate on is fucking. The pleasure is indescribable, I can’t hold on much longer, I’ll cum any second."
        play sound cum
        show honeycrispanna threesome4 with cum
        play sound cum
        show honeycrispanna threesome4 with cum
        "My vision turns white and my muscles tense up as I ejaculate inside her, cumming just as much as the last time, countless loads deep inside her."
        play sound cum
        show honeycrispanna threesome4 with cum
        play sound cum
        show honeycrispanna threesome4 with cum
        anna "Aiiieeee, you’re cumming! Ahhhh…"
        play sound cum
        show honeycrispanna threesome4 with cum
        play sound cum
        show honeycrispanna threesome4 with cum
        "*Splurt, splurt, squirt*."
        honeycrisp "Mmm, damn, stud, leave some for me…"
        anna "So much inside me… I have so much of your cum in my belly and womb…"
        show honeycrispanna threesome5 with dissolve
        "I pull out and copious amounts of cum oozes out of her pussy, even I’m surprised by just how much there is."
        stop ambience
        "Anna is left exhausted and panting, hopefully her heat is satisfied for now, because…"

        honeycrisp "Hope you sugarcubes didn’t forget about me, I want you to stick that semen coated cock straight inside me, get to work stud!"
        "I shuffle over to Honey with my erection in hand, it’s slightly softened but thanks to the aphrodisiac’s effects getting stronger I think I’m ready to go immediately."
        "Honey presents her pussy to me by spreading her outer lips out with her fingers. She’s utterly soaked, it has even dripped down her thighs."
        play sound cum
        show honeycrispanna threesome6 with dissolve
        "As it drips with cum, I bring the tip of my cock to the entrance of her pussy. As usual, the pussies of these incredibly aroused girls invites me in with a delightful warmth and tightness."
        "While sinking deeper, my shaft becomes fully erect again, that aphrodisiac is amazing!"
        honeycrisp "Aaahh! Don’t hold back stud, I haven’t been able to get off in a week!"
        play ambience sex
        "My cock slides in all the way, the cum mixing in with her juices creating a messy lubricant the enables me to skip the gentle sex and get straight to the rough fucking."
        "With each thrust, I pull out the entirety of my shaft and sink it back in as deep as it’ll go."
        honeycrisp "Ahhh, darn… That’s really good…"
        "Honey’s body and muscles are tighter than the soft, squishy Anna. Even her pussy feels different as it squeezes around my shaft."
        "It’s a more rough and rugged fuck, even if the cum around my cock makes her insides soaked and sloppy."
        honeycrisp "Mmmm, keep going like that, just like that."
        "Yes ma'am! I kept fucking at this current pace which allowed me to feel all the best parts of her pussy on every nerve ending of my penis."
        "The pleasure wasn't so overwhelming that I would ejaculate too soon. She on the other hand could easily climax at this speed."
        "I could see Anna also masturbating whilst she eagerly watched us, cum dripping down her thighs."
        anna "Spank her butt, [playername]! Spankies!"
        show honeycrispanna threesome7 with dissolve
        play sound spank
        "Good idea, I lift up my dominant hand and markedly bring it down square onto Honey’s tight ass cheek."
        honeycrisp "Eep! Don’t gang up on me you two!"
        "As my hand connected, I could feel her insides briefly squeeze around my cock."
        anna "Ohh that was hot, again, again!"
        play sound spank
        "This time I use my other hand, with a raise and a return, I smack Honey’s other ass cheek creating a satisfying slapping sound, even against her soft fur."
        honeycrisp "Oh, ohh! That… Again! I’m close!"
        play sound spank
        anna "Ahah! She loves it! I always pictured Hun being the dominant one, not the sub! This is great!"
        play sound spank
        "As requested by Honey herself, I spank her ass again with my dominant hand, this sets her off and she begins to orgasm, her pussy contracting and squeezing my shaft more and more."
        honeycrisp "Aahhhh, ahhhhh, coming! Mmmm…!"
        "Anna seems to get herself off too, or at the least I can see her squirting more. The barn at this point is dense with the thick aroma of sex."
        honeycrisp "Mmph, *Pant*. I can’t believe I came by getting spanked, I’ll get you back for that one stud…"
        honeycrisp "Y’all don’t stop thrustin’ though! I wanna be sore in the morning."
        "I never stopped fucking her, but I take that as a challenge to speed up."
        "Even though I had two orgasms, I am still incredibly horny. Ever since I met Honey and she started to tease me, I knew I wanted to bend her over and ravish her."
        "It’s amusing to think she was so provocative and dominant when she was flirting with me, but now she’s the one kneeling over submitting to me. "
        honeycrisp "You darn stud… I knew you’d be a good lay…"
        play sound spank
        "I spank her again with my other hand, I love the way she twitches and gasps in response to it. "
        honeycrisp "Ahh… C-Cum inside!"
        "I stop holding back and begin to fuck at the same pace that allowed me to cum in Anna, I could already feel my orgasm brimming."
        "As I’m pumping, I can feel her insides start to tighten and squeeze, she’s coming again! So soon after her first one. I'm going to come too!"
        play sound cum
        show honeycrispanna threesome8 with cum
        play sound cum
        show honeycrispanna threesome8 with cum
        "The sudden tightness of her pussy, combined with the speed we’re rutting, easily pushes me over the edge, and I start to unload inside of her."
        play sound cum
        show honeycrispanna threesome8 with cum
        play sound cum
        show honeycrispanna threesome8 with cum
        honeycrisp "Ahhh! Inside, inside! Mmpphh…"
        play sound cum
        show honeycrispanna threesome8 with cum
        play sound cum
        show honeycrispanna threesome8 with cum
        "As I climax, I continue to thrust into her as I fill up her pussy with my hot cum, enjoying what is perhaps my most satisfying orgasm of the day."
        stop ambience fadeout 3.0
        stop music fadeout 5.0
        scene bg black with dissolve
        "Most satisfying, however, most tiring. After my third orgasm I close my eyes and fall back onto some hay feeling exhausted."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        honeycrisp "Wew, I didn’t know you had it in ya, stud."
        show bg barnblur with dissolve
        show honeycrisp closelaughing with dissolve
        "From my uncomfortable position on the floor, I can see Honeycrisp standing over me, brushing off some hay that was stuck to my sweaty skin."
        hide honeycrisp
        show anna closesatisfied
        with dissolve
        "Peeking to the side I can see Anna sat down with her eyes closed, enjoying the moment I assume."
        hide anna
        show honeycrisp closesatisfied
        with dissolve
        "To my surprise, Honeycrisp straddles me and… Suddenly kisses me!"
        show honeycrisp closehorny with dissolve
        honeycrisp "Mmm stud, thank you for this special opportunity."
        mc "I didn’t think you were the affectionate type."
        show honeycrisp closehappy with dissolve
        honeycrisp "Nah, I’m not, but who doesn’t like cuddles after sex?"
        show anna closesurprised with dissolve:
         xpos 900
         ypos 40
        anna "Cuddles? Oh, don’t cuddle without me!"
        "Anna had opened her eyes and realized she was missing out, Honey may not be affectionate, but Anna definitely is."
        hide honeycrisp with dissolve
        hide anna with dissolve
        show bg black with dissolve
        play ambience ambienceday
        play music castle fadein 5.0
        "The three of us cuddle on the hay for a few minutes as we slowly reattune with reality."
        "Deep breaths, birds singing, ponies, farm… Right, I’m back."
        show bg barn with dissolve
        show anna closeneutral with dissolve:
            xpos 600
            ypos 40
        anna "Uh… Actually… This hay isn’t actually comfy, I’m getting tired of leaning on hay. Can we do this on a bed next time?"
        mc "Next time?"
        show honeycrisp closehappy with dissolve:
            xpos 0
            ypos 40
        honeycrisp "Heh, it’ll be a week before you need milking again and [playername] might not be here to work that day."
        show anna closesurprised with dissolve
        anna "Then he should visit me at my farm, we can do the thing again!"
        honeycrisp "Don't forget about me, stud."
        mc "I can just visit you both, right?"
        show honeycrisp closelaughing with dissolve:
        honeycrisp "Naturally!"
        show anna closehappy with dissolve
        mc "Ladies, you spoil me, or maybe I’m spoiling you, I think it’s both."
        show honeycrisp closehappy with dissolve
        show anna closelaughing with dissolve
        anna "It’s both!"
        show honeycrisp closeshy with dissolve
        mc "By the way… Those aphrodisiacs were great, but… When is my erection going to go away?"
        "I point to my still-erect cock, the flesh is willing, but the mind is weak."
        show anna closesurprised with dissolve
        anna "Aha… Uhm… Soon?"
        hide anna with None
        hide honeycrisp with None
        show bg black with dissolve
        stop music fadeout 5.0
        "…"
        show bg farmkitchen with dissolve
        "Thankfully my erection disappeared after about twenty minutes. Then the three of us enjoyed some conversation and lunch before Anna returned to her farm."
        "Anna’s bubbly and fun-loving personality really grew on me during the short time I got to know her, I hope I get to see her again."
        show honeycrisp closelaughing with dissolve
        "Honey on the other hand, is still here sat opposite to me, she’s positively glowing, she’s been unable to stop smiling ever since we left the barn."
        play music day
        show honeycrisp closehappy with dissolve
        honeycrisp "Ahh… What a wearisome morning, you not only managed to rut all the pent-up horniness out of me, but also some frustrations I’ve been having lately."
        mc "Oh yeah? Other frustrations?"
        show honeycrisp closesatisfied with dissolve
        honeycrisp "Let’s just say, that was intensely liberating. I feel like I can breathe and think clearer now."
        mc "That’s good, I'm still catching my breath, you’re a lot tougher than me, Honey."
        mc "Even so, I can keep going, what jobs do we have to do next?"
        show honeycrisp closehappy with dissolve
        honeycrisp "Don’t sweat it sugarcube, I could tell y’all sore after all that, you could barely walk straight on the way back from the barn."
        honeycrisp "I’ll pay you the full amount right now, least I can do for ya."
        mc "Thanks, I feel a bit useless only working half a day though, are you sure?"
        show honeycrisp closehorny with dissolve
        honeycrisp "Stud, you didn’t work half a day, I was so sexually frustrated; I reckon you worked me for at least a week."
        "Only a week huh? It must suck being in heat."
        "As Honey is handing me my pay, Blossom modestly walks in the door, and closes it gently behind her."
        hide honeycrisp
        show honeycrisp closeshocked:
            xpos 600
            ypos 40
        show blossom happy:
            xpos 120
            ypos 75
        with dissolve
        blossom "Hello sis, and hello sir!"
        "She’s back early today, if her college is anything like mine the timetables tend to be random."
        show honeycrisp closehappy with dissolve
        honeycrisp "Howdy Blossom, how was college?"
        blossom "Mhm, it was good."
        show honeycrisp happy with dissolve
        honeycrisp "Welp, I best get back to work. I’ve been slackin’ and I’ve got a to-do list before sundown, I’ll see you two later."
        mc "Later and thank you!"
        show blossom awkward with dissolve
        blossom "See you soon, Sis."
        hide honeycrisp with dissolve
        hide blossom with None
        show blossom embarrassed with dissolve
        stop music fadeout 3.0
        "Honey nonchalantly makes her way out, starting to hum to herself once she’s outside."
        "I turn to Blossom who is staring at me intently and as soon as I do, she inelegantly looks away."
        show blossom shocked with dissolve
        play music challenge fadein 10.0
        blossom "What in tarnation did I just overhear?"
        "Oh no, did she overhear me and Honey talking about the threesome?"
        menu:
            "What should I say?"
            "She was talking about the apple supply.":
                show blossom bashful with dissolve
                blossom "Nuh uh, you totally had sex with my sister, I can tell…"
                mc "You can tell?"
            "We totally fucked.":
                show blossom bashful with dissolve
                blossom "Hmm… I already know."
                mc "You do?"
            "Nothing you need to know about.":
                show blossom bashful with dissolve
                blossom  "Well too late, I already know."
                mc "You saw us?"
                blossom "Nuh uh..."
        show blossom awkward with dissolve
        blossom "You two smell of sex."
        "Is she bluffing? Or do ponies have much sharper senses of smell than humans?"
        show blossom closeneutral with dissolve
        "Blossom sits on the same chair as last time. She leans over and takes a cover off a peculiar box in the corner of the room."
        blossom "Ohh, Anna was here, she brought the week’s milk."
        "I look down at the box and I see that it’s full of bottles. Bottles of… milk?"
        mc "Wait a second, is that really a box full of milk?"
        show blossom closehappy with dissolve
        blossom "Oh uh, yes, Anna milks this and delivers it to us every week, and we distribute it around here."
        mc "You’re kidding, I spent all that time milking her only for there to be this much?"
        show blossom closebashful with dissolve
        stop music fadeout 10.0
        blossom "You milked her? Oh, my goodness that’s kinda lewd…"
        mc "Oh, is it?"
        show blossom closeneutral with dissolve
        blossom "It’s probably a good thing you came today then, sis probably would have struggled with one hand. "
        mc "So, she delivers milk and gets milked herself?"
        show blossom closehappy with dissolve
        blossom "Mhm, I’m not sure why Anna doesn’t just get another cow to milk her, maybe it’s a personal thing."
        "Now I have even more questions about Anna and Honey’s relationship."
        show blossom closeawkward with dissolve
        blossom "So… If you were supposed to be milking Anna this morning… When did you…?"
        mc "Uhm… When did I...?"
        show blossom closebashful with dissolve
        blossom "When did you have sex with my sister…"
        mc "Ah… Well… We did it in the barn, with Anna."
        show blossom closeawkward with dissolve
        "She blushes and looks down at the floor."
        blossom "L-Lewd."
        show blossom closeembarrassed with dissolve
        blossom "It sounds like her and Anna are closer than I thought, we should write that letter as soon as we can to see if Anna can help."
        mc "Yeah, I had suspected that Anna was the same cow farmer you mentioned. Let's get on that."
        show blossom closehappy with dissolve
        blossom "Come upstairs with me?"
        show blossom happy with dissolve
        "This time she displays less doubt and more confidence, without even waiting for my reply she starts to walk her way upstairs."
        hide blossom with dissolve
        blossom "Come on, my room is this way."
        "She isn’t giving me a choice this time, how exciting, I’m invested in how this situation plays out."
        show bg blossombed
        "Blossom leads me to her bedroom, it’s a small yet adorable room, adorned with several girly decorations, there’s a keyboard in one corner, a dressing table, and a double bed."
        show blossom closehappy with dissolve
        "Blossom sits at her dressing table and takes out a paper and a pen, I casually sit on the bed adjacent to her and watch what she’s doing."
        mc "Alright, what are we writing then? "
        show blossom closeneutral with dissolve
        blossom "Uhmm… Hmm… "
        "She writes 'Dear Anna', and leaves it at that, perhaps a little too formal but I can work with it."
        show blossom closehappy with dissolve
        blossom "Could you please help? You’re a grown up so you should be good with these things."
        mc "I think we’re the same age."
        show blossom closeshocked with dissolve
        blossom "Ohh, really? But you're so mature..."
        mc "How about something along the lines of, ‘Honeycrisp has been struggling to maintain the north Arcadia farm on her own, especially with her injury.’"
        show blossom closehappy with dissolve
        blossom "Okay, I’ll just write that down."
        mc "As a result, we would like to form a deal that involves the employment of an additional person to help around the farm, payment to the person will be naturally provided."
        show blossom closelaughing with dissolve
        blossom "That’s good!"
        mc "It’s alright, but that’s not really forming a partnership, that’s just stealing an employee, we need to sweeten the deal."
        mc "How about this at the end; ‘What else can we offer you to sweeten this relationship and make it official?’"
        show blossom closehappy with dissolve
        blossom "I like that, we’ll probably trade crops since there are a few things we grow here that they don’t grow."
        mc "You already have the milk trade, so it sounds like this is just a logical step in that direction. Honestly, I wonder why it hasn’t already happened, this seems perfect."
        show blossom closeneutral with dissolve
        blossom "It hasn’t happened yet because we haven’t been alone long, we’re still grieving."
        show blossom closesad with dissolve
        blossom "Perhaps this partnership was inevitable in the future, but I want it now, because I can’t just sit here and wait while my sister suffers."
        "She folds up the letter and turns to me, placing her hands on my thighs."
        show blossom closeshocked with dissolve
        blossom "Earlier downstairs, Honey looked happier than she has in a long time, I want to thank you for that."
        show blossom closehappy with dissolve
        blossom "Thank you so much, having you here has brightened up both of our days."
        mc "I admit, I don’t feel like I’ve done much, but I’ve enjoyed every second of it, and no doubt every second further."
        show blossom closelaughing with dissolve
        blossom "You’re so sweet, I can see why Honey likes you."
        show blossom closehappy with dissolve
        blossom "I kinda like you too... You know…"
        "She moves from the stool of her dressing table and straddles me. Her body language is pretty similar to Honey when she's acting confident."
        show blossom closelaughing with dissolve
        blossom "I want to do unspeakable things to you, I can't let my sister have all the fun with the cute boys..."
        mc "R-Right now, are you sure?"
        "She leans in and kisses me on the cheek."
        show blossom closeembarrassed with dissolve
        blossom "Not today, you’ve already had my sister today."
        show blossom closebashful with dissolve
        blossom "I’ll have you to myself another day, I just wanted to whet your appetite for the next time we meet."
        "She then climbs off me and lazily lays around on the rest of her bed. I’m honestly shocked by that sudden bout of confidence she had, it was like she became her sister for a fleeting moment."
        "My first impression of her being completely shy and the opposite of Honeycrisp may be wrong. She’s definitely shy, but she’s absolutely got the same fire."
        if livingwithbutters == 1:
            "Butters was undeniably right about what she said, ‘The next time she invites you up to her room, she might surprise you.’"
        else:
            "Moxie was undeniably right about what she said, ‘The next time she invites you up to her room, she might surprise you.’"
        show blossom closehappy with dissolve
        blossom "I can tell you’re tired anyway. I don’t know what you three did, but it looks like you need a rest."
        mc "Honestly, I do, and your bed is super soft. Is it okay if I just lay here for a while?"
        show blossom closelaughing with dissolve
        blossom "Of course, mister."
        show blossom closehappy with dissolve
        "I let out a sigh and allow myself to fall backwards onto the bed, sinking into the cosy sheets."
        "Blossom is more or less doing the same, but at a ninety-degree angle to me, her head and twin tails pressed against my side."
        "Now that I’m finally laying down, I become physically hyper-aware about how heavy and numb my body feels."
        "As I lay here, my mind starts to wander, it occurs to me that I don’t actually know a lot about Blossom other than what Honey has told me, we’ve only ever talked business."
        "And yet she still wants to have sex with me, I mean sheesh, I barely know this girl."
        "She's this shy and yet she's moving onto me faster than Moxie did."
        "I should get to know her a little better first."
        play music day2 fadein 5.0
        mc "Hey Blossom."
        blossom "Hm?"
        mc "I notice you call me mister or sir a lot, call me [playername]."
        show blossom closelaughing with dissolve
        blossom "Okay, [playername]"
        label farmvisit2choice1:
        menu:
            "Let’s learn more about her."
            "What do you spend most of your time doing?":
                show blossom closeneutral with dissolve
                blossom "You mean at college?"
                mc "Anything, studies, hobbies, spare time."
                show blossom closehappy with dissolve
                blossom "I study music, me and my friend Melody like to make music."
                if boutiquevisit1 == 1:
                       "Melody? I can’t imagine that she-devil and Blossom being friends."
                if boutiquevisit3 == 1:
                       "Well, even Melody has a softer side. The more I get to know Melody the softer she gets, the more I get to know Blossom the rougher she gets."
                blossom "Some people choose music because they love it, but I think music chose me. I would always listen to music; I remember going to the store when I was three to buy the latest CDs with paps."
                show blossom closelaughing with dissolve
                blossom "I always loved learning how to play instruments, yet most of all, I wanted to compose music that could move the hearts of people."
                mc "That’s inspirational, I’d say you can achieve anything if you try hard enough, but it seems you already know what you’re doing."
                show blossom closehappy with dissolve
                blossom "Yeah, learning instruments is challenging, I used to get frustrated that I couldn’t do things right first."
                blossom "My sister told me something though, she said that the river doesn’t erode the rocks through strength, but through perseverance."
                mc "That’s a beautiful philosophy, I wish I knew that before I started college."
                blossom "Oooo… You’re at college too?"
                mc "Well... I was."
                "I best not talk too much about my old life, especially to Blossom."
                mc "What else do you do?"
                blossom "Oh, hmm… In my spare time I entertain myself by reading or touching myself. Usually reading then getting distracted and masturbating, you can probably relate."
                "Yeah, I can relate, but I didn’t expect her to be so upfront about masturbating."
                jump farmvisit2choice1
            "You seem less shy than you were yesterday.":
                show blossom closeneutral with dissolve
                blossom "I tried to be open before. I was too nervous though, I’m always like that with new people."
                blossom "Managed to keep my cool this time though. "
                show blossom closehappy with dissolve
                blossom "I think it’s because I saw how happy my sister was, it allowed me to relax; I’ve been highly strung lately, so I apologize if I made you uncomfortable."
                mc "Don’t worry about me, I get it."
                mc "I wasn’t uncomfortable either, you made me tea, and helped me figure how to help Honey."
                show blossom closelaughing with dissolve
                blossom "You’re so sweet, but in my eyes, I see it the other way."
                show blossom closehappy with dissolve
                blossom "You enjoyed my homemade tea and helped me figure out how to help my sister. Well, I already had the idea, and you gave me the confidence to go through with it."
                jump farmvisit2choice1
            "Why do you want to have sex with me?":
                show blossom closeneutral with dissolve
                blossom "Uhm, that’s a personal question…"
                mc "No more personal than having sex though."
                blossom "Hm, yeah…"
                show blossom closebashful with dissolve
                blossom "I want to have sex with you, because I’m horny."
                mc "Is that it?"
                blossom "Yeah, I think a lot about sex while I’m in heat."
                "Well... That's pretty simple, maybe {i}too{/i} simple."
                jump farmvisit2choice1
            "That’s enough questions. (Proceed)":
                "She stretches out a little beside me. Seems like things will get better. The two of us chill out for a while, Blossom at some point starts playing some music from a stereo, it seems more upbeat and poppy compared to what Moxie listens to."
        show blossom closeneutral with dissolve
        blossom "I’ll send the letter off later today, hopefully things will be okay soon."
        mc "Guess you won’t need my help anymore."
        show blossom closehappy with dissolve
        blossom "Having you around will make me feel better. You need to come back anyway, you know why."
        mc "You already know I’m coming back to see you."
        show blossom closelaughing with dissolve
        "I playfully fondle her breast causing her to gasp, although she’s soon to giggle and nod."
        show blossom closehappy with dissolve
        blossom "Hehe, I like that..."
        blossom "You should come early in the morning just before I go to college."
        show blossom closelaughing with dissolve
        blossom "I'd say it’s important enough to miss a few classes, wouldn't you? Hehe."
        mc "Sure thing, I’m still here to work though, don’t forget that."
        show blossom closehappy with dissolve
        blossom "Obviously, that’s why you need to get here early, hehe…"
        "I sit up on the side of her bed, and Blossom follows my movements so she's sat up next to me."
        show blossom closesatisfied with dissolve
        "She hugs me, and we cuddle for a while. I can feel her small breasts pressing against my chest, her nipples are hard."
        "She smells great too, I’ve noticed a lot of mares smell nice, I think I’ve figured out that those are the pheromones."
        show blossom closehappy with dissolve
        blossom "Alright, I’ll see you soon [playername]."
        mc "Did you want me to leave? "
        show blossom closeneutral with dissolve
        blossom "Oh, I thought you were about to leave."
        mc "Yeah I was, just teasing you. Still, it feels weird leaving work when it’s so early in the afternoon. I don’t want to keep you. though "
        show blossom closehappy with dissolve
        blossom "Yeah you should probably leave before I start grinding on you, hehe"
        mc "Wow, you went from being so shy you couldn’t speak to having no filter at all."
        show blossom closelaughing with dissolve
        blossom "Hehe, I don’t get it either, you just have a strange way of making me open up to you."
        show blossom closehappy with dissolve
        blossom "Strange way of making me open my legs, heh… Was that one too much?"
        mc "I don’t know what to say, I’m too surprised."
        show blossom closebashful with dissolve
        blossom "Sorry, I’m so horny I’m not exactly thinking straight."
        "That’s my fault for lying in bed with a mare in heat."
        show blossom closeawkward with dissolve
        blossom "I was planning on masturbating though; I always do it when I get home."
        mc "I won’t keep you from it then; I’ll see you very soon."
        "I stand up and make my way to her door."
        show blossom closehappy with dissolve
        blossom "I’m going to think about you while I do it."
        mc "Slowly leaving!"
        show blossom closelaughing with dissolve
        blossom "I’m going to have sex with you when you come back."
        mc "I’m leaving!"
        hide blossom closelaughing with dissolve
        show bg farmupstairs with dissolve
        "I step out of her room and close the door behind me."
        "I stay there for a few seconds and listen, I can’t resist."
        play ambience sex
        blossom "Mm… Mmmm…"
        "She’s certainly didn’t waste any time; I can hear wet sounds and her moans."
        "She has reached a point where she's freely expressing her sexuality and desires with me, and indulging in that freeing feeling."
        "I’ll be back for you Blossom, just you wait."
        stop ambience
        show bg black with dissolve
        stop music fadeout 5.0
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        "…"
        if livingwithmoxie == 1:
            show bg moxiewagonday with dissolve
            play ambience ambienceday fadein 5.0
            "I return to the wagon, it’s still quite early in the day. Despite that, I’m more exhausted than the first time I went to the farm and had to actually work."
            "I’ve noticed that there’s something about sex that tires muscles I didn’t even know I had."
            show bg black with dissolve
            stop ambience fadeout 3.0
            "I lay on Moxie’s bed and nap. I’m extremely grateful for all the great people I’m meeting here in Arcadia."
            "It doesn’t take too long for Moxie to return and wake me up."
            play ambience ambiencenight fadein 5.0
            show bg moxiebednight with dissolve
            moxie "Hey lazy, time to wake up! I hope you weren’t napping all day! Lazy, lazy!"
            mc "*Grumble* Today was exhausting, I was at the farm working really hard."
            show bg moxiewagonlamp with dissolve
            "I stretch and crawl out of bed and make my way to the sofa to laze around even more."
            show moxie laughing with dissolve
            moxie "Yeah no wonder, farm work is tough, too tough for me."
            mc "Actually I didn’t end up doing that much farm work, I just ended up… Well, you know."
            show moxie smug with dissolve
            moxie "Ohh, chatting up all those ladies lead to something?"
            mc "You know it, Honey needed it badly, turns out she was struggling to masturbate because of her cast."
            show moxie happyneutral with dissolve
            moxie "So you helped her out? Smooth."
            moxie "You’re so smooth talking I bet you could get any mare in Arcadia."
            mc "Actually, there was someone that wasn’t a mare, there was a cow as well."
            show moxie shocked with dissolve
            moxie "A cow? I’ve seen a few of those, not as many as ponies though."
            mc "Yeah, my job was to milk her, but it escalated quickly into a threesome of all things."
            if barvisit2 == 1:
                show moxie bashful with dissolve
                moxie "You had a threesome without me? Awh darn, we should invite Riku over again sometime."
            show moxie happyneutral with dissolve
            moxie "Did you drink the milk? It’s a sex drug, right? Haven’t tried it myself, but I’ve seen it in the market."
            mc "It was crazy, the milk let me just keep going even after ejaculating."
            show moxie happy with dissolve
            moxie "Multiple orgasms? I hope you didn’t tire yourself out, maybe I should buy milk for you to have with your dinner."
            mc "I think I’ll stay away from that milk for a while, it’s nothing like the harmless milk from my world."
            show moxie smug with dissolve
            mc "The cow girl was called Anna, I’m assuming she was in heat too. Turns out she was there for more than just milking and before I knew it, I had the two girls bending over and begging."
            show moxie althappy with dissolve
            moxie "No progress on the little sister then? I was curious about her; I want to know if she has the same sex drive you say Honeycrisp has."
            mc "Wow, you’re actually enjoying my sexual adventures, aren’t you?"
            show moxie laughing with dissolve
            moxie "Ahah yes, they’re hilarious! I wish I could spy on you; I love seeing the psychology behind sex and love."
            mc "I made more progress with Blossom than I had anticipated. She made quite a few advances, in her bedroom, no questions asked, straddled me and told me that she wants to do unspeakable things with me."
            show moxie happy with dissolve
            moxie "I knew it! Those girls have a rage in their heart that runs through the family."
            mc "I’m sure she’s still shy, but she seems to have managed to build rapport with me. We laid together in bed listening to music for a long time, that definitely helped."
            show moxie smug with dissolve
            moxie "With a mare in heat no less. She’s probably thinking about you right now."
            mc "Yeah I think she might be, while masturbating, right?"
            show moxie laughing with dissolve
            moxie "Pretty much, you gonna tap that?"
            mc "You know it."
            "Me and Moxie high-fived."
            jump evening
        elif livingwithbutters == 1:
            show bg buttershouse with dissolve
            play ambience ambienceday fadein 5.0
            "I return to the cottage, it’s still quite early in the day. Despite that, I’m more exhausted than the first time I went to the farm and had to actually work."
            "I’ve noticed that there’s something about sex that tires muscles I didn’t even know I had."
            show bg black with dissolve
            stop ambience fadeout 3.0
            "I lay on Butters's bed and nap. I’m extremely grateful for all the great people I’m meeting here in Arcadia."
            "It doesn’t take too long for Butters to return and wake me up."
            play ambience ambiencenight fadein 5.0
            show bg buttersbednight with dissolve
            butters "Hey dear, time for dinner! I hope you weren’t napping all day! You'll get even more tired."
            mc "*Grumble* Today was exhausting, I was at the farm working really hard."
            show bg buttershousenight with dissolve
            "I stretch and crawl out of bed and make my way to the table to eat dinner."
            show butters dresslaughing with dissolve
            butters "Farm work is tough, as you can guess from my tummy, cave work isn't actually very intensive."
            mc "Actually I didn’t end up doing that much farm work, I just ended up… Well, you know."
            show butters dressfufufu with dissolve
            butters "Ohh, flirting with the lovely ladies lead to something?"
            mc "You know it, Honey needed it badly, turns out she was struggling to masturbate because of her cast."
            show butters dresshappy with dissolve
            butters "Bless her, I know that frustration well."
            butters "You’re so smooth talking I bet you could get any mare in Arcadia."
            mc "Actually, there was someone that wasn’t a mare, there was a cow as well."
            show butters dresssurprised with dissolve
            butters "A cow? Were you milking her?"
            mc "Yeah, but it escalated quickly into a threesome of all things."
            butters "You had a threesome? We should have one of those..."
            show butters dresshappy with dissolve
            butters "Take care of that milk, it's a potent aphrodisiac you know!"
            mc "It was crazy, the milk let me just keep going even after ejaculating."
            butters "Aha, you actually had some? I hope you didn’t tire yourself out, maybe I should buy milk for you to have with your dinner."
            mc "I think I’ll stay away from that milk for a while, it’s nothing like the harmless milk from my world."
            show butters dresshorny with dissolve
            mc "The cow girl was called Anna, I’m assuming she was in heat too. Turns out she was there for more than just milking and before I knew it, I had the two girls bending over and begging."
            show butters dresshappy with dissolve
            butters "No progress on the little sister then? I thought you and her were gonna..."
            mc "Wow, you’re actually enjoying my sexual adventures, aren’t you?"
            show butters dresslaughing with dissolve
            butters "Mmm, it's a little embarrassing but yeah, I like hearing about sex and stuff."
            mc "I made more progress with Blossom than I had anticipated. She made quite a few advances, in her bedroom, no questions asked, straddled me and told me that she wants to do unspeakable things with me."
            show butters dresshappy with dissolve
            butters "You can't keep a mare in heat down, they get what they want."
            mc "I’m sure she’s still shy, but she seems to have managed to build rapport with me. We laid together in bed listening to music for a long time, that definitely helped."
            show butters dresshorny with dissolve
            butters "She’s probably thinking about you right now, I would be."
            mc "Yeah I think she might be, while masturbating, right?"
            show butters dresslaughing with dissolve
            butters "Yeah, I'd say you have that cat in the bag, have fun with her!"
            jump evening
        else:
            pass
    label farmvisit3:
        "If I’m quick, I should be able to get to the farm just before Blossom leaves for college."
        "I wonder what’s going to happen. Does she genuinely just want to meet me in the morning for quick, cheeky sex?"
        "Either way, I’m finding myself being seduced by both Honey and Blossom, it’s enjoyable to see what situations they’ll throw me in."
        stop music fadeout 10.0
        scene bg farm with dissolve
        "I arrive at the farm a little earlier than last time. Although I don't doubt that Honey has been outside working since sunrise. I don't envy how much hard work it must be running this place."
        show bg farmkitchen with dissolve
        show blossom closeneutral with dissolve
        "I walk up to the farmhouse without seeing Honey, I enter through the front door and step into the kitchen to find Blossom munching some breakfast cereal."
        blossom "*Munch* Oh, hey. *Munch, munch*"
        show blossom closeawkward with dissolve
        blossom "Do you want some?"
        mc "I’ve already eaten, appreciate the offer though."
        show blossom closehappy with dissolve
        "I take a seat, as per usual in the exact same spots as the last two times I was in the kitchen with Blossom."
        play music farm
        blossom "Heh, you actually came. *Munch*."
        show blossom closebashful with dissolve
        blossom "You’re making me blush internally."
        mc "I think you’re blushing externally too."
        show blossom closeembarrassed with dissolve
        blossom "Mm… Maybe. *Munch, crunch*"
        "Seems like she’s back to being shy, although maybe she just woke up and feels lethargic."
        blossom "I sent that letter off."
        mc "Any good news?"
        show blossom closeawkward with dissolve
        blossom "Nah, not yet. I’m still building up the courage to tell sis what I did."
        show blossom closeneutral with dissolve
        blossom "Does my sister know you’re here?"
        mc "Haven’t seen her yet."
        show blossom closehappy with dissolve
        blossom "Perfect, that means we have as much time as we want."
        "She finishes eating her cereal and puts down her spoon, before putting the kettle on and getting two mugs out."
        show blossom bashful with dissolve
        blossom "Would you like to have some tea with me, perhaps with milk?"
        "I can’t forget that there are some side effects to this milk. It's quite a potent aphrodisiac that let me cum three times in a row with Honey and Anna."
        "Should I have some? Ah, fuck it, it’ll just let me ravage that cute butt of hers for way longer."
        mc "Sure thing, and a teaspoon of sugar please?"
        show blossom laughing with dissolve
        blossom "Good choice, I’ll definitely give you some sugar."
        show blossom closehappy with dissolve
        "She finishes the tea, hands a cup to me and sits back down."
        blossom "You picked a wonderful day to visit, I don’t have college at all."
        show blossom closebashful with dissolve
        blossom "So, we could just, you know, chill out all day… Like a couple, hehe."
        mc "I guess… What about my work though? I’m here to work and get paid."
        show blossom closeshocked with dissolve
        blossom "Oh crap, yeah, you’re right."
        mc "’Crap’? You’ve developed a rude mouth, Blossom"
        blossom "Shh! That isn't even a real swear! M-Maybe it is where you come from…"
        mc "Nah, you’re fine, I’m just teasing you."
        show blossom closebashful with dissolve
        blossom "Bully, drink your tea!"
        "My tea is at the perfect drinking temperature. I take a sip, and it is indeed typical black tea, unlike the apple tea Blossom served me before."
        "Even the milk tastes the same, it is pleasantly familiar."
        "I sit back and enjoy the feeling of the drink's hotness spreading throughout my body on this cool morning."
        "This tea is one of the few connections between this world and my own. Wistfully I close my eyes and allow my mind to wander back home for a few moments."
        show blossom closehappy with dissolve
        blossom "Did my tea put you to sleep, [playername]?"
        mc "Not quite, this tea reminds me of home."
        blossom "I see… Where abouts are you from? Is there a town with lots of furless people?"
        mc "It’s complicated, I’m not from around here. You could say I’m from some far-off distant land."
        show blossom closelaughing with dissolve
        blossom "How mysterious, I like mysterious boys."
        mc "Even if they’re furless?"
        show blossom closeembarrassed with dissolve
        blossom "I can see all your tone and muscles, it’s a- it’s… Oh, I’m too embarrassed to say it."
        "I take another sip of my tea. The taste is so normal I almost forgot about the aphrodisiac. It’s making me tingle at the loins as its effects start to kick in."
        mc "Have you gone shy again?"
        show blossom closebashful with dissolve
        blossom "I think so… I do sometimes, sorry…"
        "She takes a sip of her tea, and it only just occurred to me… She added milk to hers as well!"
        mc "Uhm, so, you’re having milk too?"
        show blossom closehappy with dissolve
        blossom "Mhm, it’s my first time trying it, I’m pretty excited."
        blossom "I only added a little, it gives you a slight buzz and results in sex feeling better. "
        mc "Is that common among mares?"
        blossom "Apparently common enough for us to make decent monies selling it."
        "Do the people of this world really need more reasons to have a strong sex drive? It seems between the disparity of sexes and the estrus they have that covered."
        mc "Out of curiosity, how horny does heat make you?"
        show blossom closebashful with dissolve
        blossom "Uuu, we’re starting the lewd questions."
        show blossom closeembarrassed with dissolve
        stop music fadeout 5
        blossom "Let’s go to my room? I’d feel more comfortable answering there…"
        hide blossom with dissolve
        show bg black with dissolve
        pause 0.5
        show bg blossombed with dissolve
        play music castle fadein 5.0
        "We make our way upstairs with our cups in hand. Her bedroom is tidier than last time, her bed is even made."
        show blossom closeembarrassed with dissolve
        "Blossom places her tea on the dressing table and turns towards me."
        show blossom closebashful with dissolve
        "I always thought I’d get used to seeing these mares publicly nude, but the sight of Blossom still greatly excites me, with her delicious petite breasts, and her cute butt."
        show blossom closeembarrassed with dissolve
        "She sits on her dressing table chair and I sit opposite to her on the bed, we can’t help but blush and laugh as we look at each other."
        blossom "Hehe, so… My heat, right?"
        mc "Ah yeah, I’m curious to know how it affects you."
        show blossom closehappy with dissolve
        blossom "Right now, I really want to get a cute boyfriend I can go on dates with and experiment with in bed."
        show blossom closeawkward with dissolve
        blossom "Buuuut… You have no idea how few males there are at music college, let alone stallions, and none of them are single!"
        blossom "So lame… Poor me’s going to be single forever. "
        "Blossom has quite a unique take on this situation, she seems to crave for a bond as well as intimacy and affection."
        show blossom closeembarrassed with dissolve
        blossom "I uh… Really hope you don’t mind if I live out my fantasies vicariously through you."
        mc "As long as I get to live out my fantasies inside you."
        show blossom closebashful with dissolve
        blossom "G-Gosh… You may…"
        show blossom closeembarrassed with dissolve
        blossom "M-My turn to ask a question then."
        blossom "How does it feel to be horny as a male? I like being a girl, but I’ve watched porn and wondered what it’d be like to be a guy in those situations."
        "She watches porn? I swiftly scan the room and spot a laptop bag in the corner. Ah, there's the dark portal to the internet and its porn."
        mc "It’s hard to explain to someone that doesn’t know."
        show blossom closeshocked with dissolve
        blossom "Well… Your thingy isn’t hard yet, does that mean you aren’t horny?"
        mc "Not quite… I can be horny without being erect, and I can be erect without being horny, the two aren’t mutually inclusive."
        show blossom closeembarrassed with dissolve
        blossom "Whaaa? Hm… Actually, that makes sense, when I’m horny it’s not like I necessarily walk around wet and ready…"
        mc "When I’m horny, I’m flirtier, I have a stronger desire to sleep with a girl, and I get erections easier."
        mc "Everything feels better too."
        show blossom closelaughing with dissolve
        blossom "For me it’s like an overwhelming desire to caress a sexy man’s firm body, I wanna drive a man crazy and make them think about me."
        "I think the effects of the aphrodisiacs are making themselves known."
        "I can feel myself unwittingly becoming erect, although that may be partially due to the sexual nature of our conversation."
        "And Blossom has taken notice of my growing erection."
        show blossom closeshocked with dissolve
        blossom "Ooo, it’s growing…"
        show blossom closeawkward with dissolve
        "She leans in and stares innocently at my growing penis, in turn only causing more blood to surge into it."
        "Now half erect, it’s twitching slightly, Blossom is practically staring in awe."
        show blossom closeshocked with dissolve
        blossom "It moved by itself! That’s so cool…"
        "Blossom and I seem to have built up our relationship to the point where I don’t even feel embarrassed about her watching this. Her excitement is actually rubbing off on me. "
        show blossom closeawkward with dissolve
        "Blossom’s right hand slyly slips between her thighs and starts tentatively rubbing at her clitoris. It seems like the aphrodisiac has taken effect on her too."
        show blossom closeembarrassed with dissolve
        blossom "Mmphh... For some reason, I can't help myself..."
        "Watching her masturbate, my eyes take in every detail of her pristine nude body. I’m now fully erect, maybe even more than usual, my cock feels tight and it’s throbbing."
        show blossom closebashful with dissolve
        blossom "Can you show me what you do with it?"
        mc "What I do with it? I put it in stuff."
        show blossom closeembarrassed with dissolve
        $ blossomcowgirl = 0
        label blossomcowgirl:
            stop music fadeout 15.0
            show bg blossombed
        blossom "No, I mean... L-Like this..."
        show blossom masturbating with dissolve
        "She leans back on her chair with one hand and spreads her legs out, beginning to ardently rub her pussy in full view for me, it’s an incredibly sexy and sensual display."
        "I see, so she wants to watch me masturbate."
        "I wrap my hand around my cock and slowly with just a few fingers massage the shaft up and down, as if demonstrating to her how it works."
        blossom "Ohh… Oh gosh… That is so hot, [playername]…"
        blossom "I feel so horny, I’ve never felt this aroused before…"
        "That milk has definitely worked its saccharine spell, Blossom’s fingers have sped up even more, she doesn’t appear able to hold back."
        blossom "Ahh… Ahhh… Oh my gosh, yes…"
        "Faster, she just keeps rubbing. In turn I speed up and jerk off faster, albeit not to match her pace, lest I prematurely cum."
        blossom "Ahhh… C-Coming! Oh, I’m coming, ahaha… Yes…"
        "Coming already? She certainly isn’t holding back, I guess it doesn’t matter if she climaxes prematurely, but that was impressively fast. "
        "Her eyes roll back and her thighs spasm slightly as her entire body seems to be taken over by the powerful sensations from her orgasm."
        "As her climax fades, she slows down, her face beams with joy, she looks adorable with that goofy smile."
        stop music fadeout 15.0
        show blossom closesatisfied with dissolve
        mc "You didn’t waste any time getting off!"
        show blossom closelaughing with dissolve
        blossom "That was exhilarating…"
        mc "Well, it’s not over yet."
        show blossom closehappy with dissolve
        play music sex1
        blossom "Of course, I’m not finished with you."
        hide blossom
        show blossomb1 sex
        show blossom sex1
        with dissolve
        "She lifts up from her seat and swiftly straddles me like before, this time however, I can feel my erection twitching against her tummy."
        blossom "Hehe, it’s kinda big, is it going to fit? I don’t finger myself often."
        mc "Take it nice and slow. You should be more than wet enough for it to fit."
        blossom "Okay, I’m gonna!"
        play sound cum
        show blossom sex2 with dissolve
        "She takes my cock in her hand and positions it between her thighs and slowly begins to lower herself onto it."
        blossom "Ooo… It’s… tight!"
        "Blossom is surprisingly tight for a mare in heat, my cock doesn’t slide in immediately, she has to slowly guide herself down and with persistence she manages to take the full length of my shaft."
        mc "That feels so good."
        "Her pussy constricts around my cock, squeezing all the sensitive points."
        "I’m definitely more sensitive than usual due to the milk, the result is a staggeringly pleasureful sensation."
        blossom "Ahh… T-The entire thing, it’s inside me…"
        blossom "I’m going to start moving now."
        play ambience sex
        show blossom sex3 with dissolve
        "She slowly lifts herself up and then allows herself to drop back down, this feeling is unreal, Blossom seems to be feeling it too, as she’s gasping under her breath."
        "She eventually begins to loosen around my shaft, and she finds it easier to ride my cock, her pace ever so slightly increasing and her face flushing as it becomes more pleasureful for her."
        "Blossom soon finds herself in a rhythm, bouncing up and down against me."
        blossom "Ahh, s-so this is what it feels like…"
        blossom "I can feel it move inside me, it’s even better than I imagined… Mmmphh…"
        "My eyes are drawn to her breasts which wiggle each time she bounces. They’re usually hidden behind her thick bushy twintails so it’s especially nice to see them."

        "I caress her breasts and tease her nipples, she responds by biting her lip and arching her back."

        show blossom sex2 with dissolve
        blossom "Mmm yesss… Enjoying the view?"

        mc "Oh yeah, you have such a sexy body."

        mc "I’m getting close, you should speed up."
        blossom "Ahh, I really want you to fill me…"
        show blossom sex3 with dissolve
        "She begins to speedily piston up and down, excitedly focusing on getting me off."
        "It’s working too, her tightness combined with that speed is blowing my cock and mind."
        blossom "I-I can feel you throbbing inside me, ahh, fill me up!"
        play sound cum
        show blossom sex4 with cum
        play sound cum
        show blossom sex4 with cum
        "Not holding myself back, I let myself freely ejaculate deep inside of her, she continues fucking me the entire time and the resulting orgasm is ecstasy."
        play sound cum
        show blossom sex4 with cum
        play sound cum
        show blossom sex4 with cum
        blossom "Ahh- Y-You! I can feel it! I-I’m gonna come too!"
        show blossom sex4 with dissolve
        show blossom sex4 with dissolve
        "She winces almost as if her own orgasm caught her off guard, and we climax passionately together. My cock continuing to pump her with more cum throughout the entire experience."
        stop ambience
        show blossom sex5 with dissolve
        "As we peak and fall, her hips gradually stop, globs of cum trickling down the length of my cock, out of her pussy and dripping down onto my pelvis."
        "Usually around this time, I’d be feeling sensitive and getting soft, but thanks to the cheeky milk tea I had earlier, I’m lustful for more."
        blossom "*Pant* There’s so much, hehe, it’s dripping out…"
        mc "Ready to go again?"
        blossom "Mmm, absolutely, just give me one second…"
        "She brings a finger and prods at some cum on my pelvis, seemingly surprised by its viscosity, that same finger soon brings itself to her mouth as she curiously tastes it."
        blossom "Hmm, not as tasty as they act like it is in porn."
        play ambience sex
        show blossom sex4 with dissolve
        "Tasting aside, she wastes no time in beginning to raise herself up and down, her insides now soaking in both cum and her natural lubricant."
        "Every time she slips back down onto my cock, it displaces more cum and it oozes, creating a lewd squelching sound."
        blossom "This is so naughty, it’s making my head spin…"
        blossom "Ahhh, I didn’t think anything could feel this good, ahhh!"
        blossom "I just wanna be your cum dump, filled over and over by you."
        "The aphrodisiac has given Blossom an insatiable sexual appetite, just like Anna forewarned when she mentioned cow and minotaur mating habits."
        "Blossom and I will keep going until we collapse, I can already feel my cock stiffen up fully, bulging inside her drippy pussy as my second orgasm rises."
        blossom "Faster.. Ahh… Mmm!"
        "This crazy mare is already riding me just as fast as when I came earlier, I won’t be able to hold back much longer."
        "She seems to be losing her mind to pleasure, various squeaks and moans escaping her mouth, I desperately hope Honey doesn’t come inside because she’d unquestionably hear us."

        "This is intense, I can feel my breath growing shorter, and my vision clouding over."
        play sound cum
        show blossom sex6 with cum
        play sound cum
        show blossom sex6 with cum
        "Fuck! Her pussy is just too good, I can feel myself cumming again!"
        play sound cum
        show blossom sex6 with cum
        play sound cum
        show blossom sex6 with cum
        blossom "Oh my gosh, oh my gosh, more cum!"
        blossom "Fill me up, I’m such a naughty girl, haah, ahh!"
        "Several loads of my cum discharge deep within her, but she doesn’t slow down her riding for a second, causing a lot of it to gush out spectacularly."

        blossom "More, more…! Ahh, gaa- !!!"
        "Her breathing becomes more erratic as she seems to climax again, her pussy contracting tightly, particularly around my glans, keeping me erect."

        "As she comes, she throws her head into the air and arches her back. Her thrusts become disjointed as she’s visibly dazed with pleasure."
        "However, it doesn’t take her long to regain her composure and resume her previous pace, with a lustful wanton abandon perpetuated within her eyes which lock mine while she continues to bounce on my cock."

        blossom "This is… *Pant* The best… *Pant* Thi.. Ah… *Pant*"
        "She mumbles almost unintelligibly between her ragged breaths, it was starting to become clear that her fatigue was overtaking her uncontrollable lust."
        blossom "One… more…"
        "Even after so many orgasms, Blossom’s pussy is unrelentingly squeezing and stimulating my cock while she’s fucking me so fast. I try to keep rubbing her clit, but she’s moving too fast to keep up."

        "Her endurance to ride me this fast for so long almost seems impossible by human standards."

        "The pleasure continues to send my senses into overdrive as her rapid riding is unyielding. I can barely think straight. "
        blossom "Woahh… *Pant* Ahh, oh gosh!"
        "She closes her eyes and arches her back slightly, is she coming again so soon?"
        "Blossom is practically drooling as she speeds up again."
        "Her insides begin to contract, exciting my cock even further. It’s so sudden and impossibly pleasureful that it feels like she’s stealing my third orgasm."
        play sound cum
        show blossom sex8 with cum
        play sound cum
        show blossom sex8 with cum
        show blossom sex8 with dissolve
        "I couldn’t hold myself back even if I wanted to, her riding forces my cock to erupt yet another load of cum in perhaps the most powerful orgasm yet."
        play sound cum
        show blossom sex8 with cum
        play sound cum
        show blossom sex8 with cum
        blossom "Cum, cum, yes! Mooooreee!"
        show blossom sex8 with dissolve
        "Hysterically, Blossom keeps up this immense pace throughout my entire orgasm, sending me straight to the heights of euphoria."
        show blossom sex8 with dissolve
        "Yet again, more cum straight to the deepest reaches of her vagina, the area connecting our sexes is an absolute cum laden mess."
        show blossom sex8 with dissolve
        "After this orgasm, I start to feel somewhat sensitive, and my cock softens, yet Blossom in her drunk lust just keeps going, that is, until..."
        stop ambience
        stop music
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        scene bg blossombed with dissolve
        "She immediately stops."
        play music challenge fadein 5.0
        blossom "Aaiiiieeeeeeeeeeee, shit!"
        "In the middle of her breakneck riding, she suddenly rolls off me, and clings to her thigh whilst yelping. "
        blossom "Aiiieeahhhhhh, mmmphh…"
        "She bites onto a nearby pillow, her eyes welling up with tears. "
        "Uh oh, looks like she overdid it and received an awful cramp."
        "I try to massage her cramped thigh muscle, but she half-heartedly shimmies away from me."
        "I awkwardly lay here feeling guilty while she cradles herself in the fetal position for about half a minute."
        show blossom closesad with dissolve
        blossom "Awh… gosh darn it, why did I have to go and push it, we were having such a good time…"
        mc "Are you okay?"
        blossom "No, no, no… I think I pulled something, or a cramp? A cramp, definitely a cramp."
        "Blossom wiggles around on the bed, slowly recovering, she looks defeated and embarrassed."
        show blossom closesatisfied with dissolve
        mc "Come cuddle me, stupid."
        "She timidly crawls into my arms and we cuddle quietly, even with both of our pelvic areas glazed with cum."
        stop music fadeout 5.0
        hide blossom with None
        show bg black with dissolve
        pause 0.5
        "After having a minute or two of recovery, Blossom lays me down and begins to clean up all the cum with her tongue."
        pause 0.5
        show bg blossombed with dissolve
        show blossom closehappy with dissolve
        play ambience ambienceday
        play music castle fadein 5.0
        blossom "I told ya, I’m in a cum bucket mood today…"
        "She caringly trails her tongue over every cum covered inch of my cock and pelvis, there’s a lot and it takes her a long time, yet she still perseveres."
        show blossom closeembarrassed with dissolve
        blossom "Mmphh... I wish it tasted better… *Lick* Whatever… Licking you feels good…"
        mc "Oh right, cum tastes gross, I think you still have some tea left over if you want to wash it down."
        show blossom closebashful with dissolve
        blossom "More tea? I think I had enough milk for a lifetime, it kinda turned me into a lustful demon."
        show blossom closehappy with dissolve
        blossom "Either way, gotta lick it up, wouldn’t want to stain the bed!"
        "With the cum cleaned, we cuddle again, this time for much longer. My erection is gone now, so the aphrodisiac must have worn off."
        mc "I’m probably an hour late for work, I know Honey isn’t necessarily expecting me, but I should go see her before it gets any later."
        show blossom closesatisfied with dissolve
        blossom "Mm, yeah, sorry for keeping you."
        mc "It's okay. What are you going to do?"
        show blossom closeneutral with dissolve
        blossom "Muhh, I’m going stay here awhile, I’m feeling dizzy."
        mc "You did push yourself a lot, and you did all of the work too."
        show blossom closehappy with dissolve
        blossom "Of course I did… You’ve got farm work after this; I couldn’t tire you out."
        "Even at times like this, Blossom is so thoughtful and caring, even down to the little details. She’d make a good wife."
        show blossom closelaughing with dissolve
        blossom "Come visit me when you’re done, okay?"
        mc "I will, hope you recover fast!"
        hide blossom with dissolve
        show bg farmkitchen with dissolve
        stop music fadeout 5.0
        pause 0.5
        "I leave her room and head down the stairs. My balls may be drained but I feel quite perky and ready to face the day."
        "A passing clock says it’s 10:00am, fortunately I’m only an hour late, Honey probably wouldn’t mind and there are plenty of excuses that could work."
        "Oh, shit..."
        "As I enter the kitchen, Honey is right there."
        play music farm
        show honeycrisp shocked with dissolve
        honeycrisp "Uhm, howdy partner, what are you doing here?"
        "She caught me, no less going down the stairs of her house, so I can’t just lie and say I was looking for her."
        $ confessedsexwithblossom = 0
        menu:
            "Admit you were sleeping with Blossom":
                $ confessedsexwithblossom = 1
                mc "You caught me."
                mc "Blossom and I were just sleeping together."
                show honeycrisp satisfied with dissolve
                honeycrisp "Haha, napping so early? I hope I don’t work you that hard, stud."
                mc "No, I mean we had sex."
                show honeycrisp angry with dissolve
                honeycrisp "Haha, good one stud…"
                honeycrisp "Y’all need to work on your sense of humour."
                mc "I’m serious."
                honeycrisp "Look son, I gave you an out, I’d say you take it."
                "She has a mildly terrifying aura right now."
                mc "I think it’s important that Blossom and I can be honest to you, although I assume she would have preferred to keep it quiet."
                mc "But you caught me and I think you deserve to know."
                "She thinks for a moment and then nods."
                show honeycrisp neutral with dissolve
                honeycrisp "Ay, she’s old enough to make her own decisions now, I shouldn’t be too over-protective."
                honeycrisp "Let’s keep this one to ourselves for her sake, she’s a teenage mare so she’s bound to have secrets that she doesn’t want me to know."
                mc "Agreed, thanks for seeing eye to eye."
                show honeycrisp angry with dissolve
                honeycrisp "Gawsh darn I oughta bend ya dick in half!"
                honeycrisp "Jeeez... Y'all really are a stud... I'm still angry with you!"
            "Tell her you were helping Blossom with something and don’t mention the sex.":
                "I believe that being honest is usually the best way, so I’ll tell her the truth, just not the complete truth..."
                mc "Hey Honey, I came to work, I just had to help Blossom with something beforehand."
                show honeycrisp happy with dissolve
                honeycrisp "Oh really? Well I’ll be, looks like you and Blossom became good friends behind my back, what is it that you two were doing?"
                "I feel a sudden chill in my body as I remember what Blossom told me once before, ‘You two smell of sex’."
                "When me, Honey and Anna had sex, Blossom said she could smell it on me, pony noses are sharp."
                "Can she tell? I certainly hope not."
                mc "I’m afraid it’s a secret, did Blossom mention anything to you?"
                show honeycrisp laughing with dissolve
                honeycrisp "Hm... A secret? Not that I recall. Y’all got some kind of surprise waiting for me?"
                "That’s right, Blossom never told Honey about the letter, that’s fine, it’ll take a few days to resolve."
                show honeycrisp happy with dissolve
                honeycrisp "I won’t pry; I’ll patiently await a pleasant surprise!"
            "Completely lie and say you were using the bathroom.":
                mc "I was just using the bathroom, I would have asked but I was desperate, and couldn’t see you outside, sorry Honey!"
                "Wow, that was a perfect excuse."
                show honeycrisp neutral with dissolve
                honeycrisp "You couldn’t see me? But I was outside at the trees, y’all can’t miss me."
                "Ah, I’m a moron."
                "I feel a sudden chill in my body as I remember what Blossom told me once before, ‘You two smell of sex’."
                "When me, Honey and Anna had sex, Blossom said she could smell it on me, pony noses are sharp."
                "Can she tell? I certainly hope not."
                mc "I’m sorry, I don’t know how I missed you."
                show honeycrisp laughing with dissolve
                honeycrisp "Oh well, y’all welcome to use the bathroom here anytime you want, partner."
        honeycrisp "For now, let’s just get to work. I need your help with a big job."
        show honeycrisp neutral with dissolve
        honeycrisp "I was just about to ask Blossom for help anyway, hopefully you can do it instead."
        "Phew, that cramp may have been a blessing in disguise."
        mc "Okay, let’s go get started."
        "Perfect, everything settled amicably, and Honey isn’t even remotely bothered, she’s just grateful that I’m helping out."
        "I hope I’m not taking advantage of her good nature."
        scene bg barn with dissolve
        pause 0.5
        "The two of us head to the barn and there are a lot of heavy barrels that need lifting onto a wagon. This is definitely a two-person job."
        show honeycrisp happy with dissolve
        honeycrisp "Alright stud, these barrels need to go on a wagon so they can be sent to Arcadia and distributed among our customers. Pain in the ass with only one hand though!"
        mc "These uh… They’re really heavy."
        "We attempt to lift the first barrel with our three able hands."
        "However, I’m too weak, and as a result the two of us combined can’t lift them, only awkwardly shimmy it across the ground."
        "Ponies are definitely stronger than humans so I’m probably useless here."
        show honeycrisp shy with dissolve
        honeycrisp "Ehehe… It’s still too heavy, sorry I couldn’t be more help, stud."
        mc "No need to apologise, my species is a lot weaker than yours so I’m not as good at lifting."
        show honeycrisp sad with dissolve
        honeycrisp "Even a stud like you has their weaknesses huh?"
        mc "This seems like a two-person job, well uh, you know, a two-pony job?"
        show honeycrisp neutral with dissolve
        honeycrisp "Yeah, I agree, I’m just getting in the way with my clumsy left hand. Maybe I should go get Blossom as well? The three of us could definitely do this."
        if confessedsexwithblossom == 0:
            "Blossom? The suggestion makes me slightly nervous; I came inside her a lot earlier…"
            "As ridiculous as this sounds in my head, I’m worried that Honey will spot cum dripping out of her."
            "I don’t know how Honey will react if she finds out I’ve been sleeping with the little sister she’s so protective of."
            "I’m probably overthinking it. There’s no way she would notice something like that, right?"
        mc "Uhm, Honey, I have to ask, how would you do this if you were on your own?"
        show honeycrisp shy with dissolve
        honeycrisp "I’ll be honest, this is tough for me, even with both my hands, I have to roll it and use anything I can as leverage to get the job done."
        mc "You really need to hire someone; you can’t keep going on like this."
        show honeycrisp sad with dissolve
        honeycrisp "I… Uh…"
        "She looks at the barrels, sighs before sitting atop of one."
        honeycrisp "I know… I know…"
        show honeycrisp shy with dissolve
        honeycrisp "I feel like I can just be open with you, so I’ll be honest."
        honeycrisp "Whenever I think about hiring someone else... I feel awful for some reason."
        mc "You hired me, right?"
        show honeycrisp neutral with dissolve
        honeycrisp "You just showed up partner, this might sound strange but I feel scared to ask anyone for help..."
        show honeycrisp sad with dissolve
        honeycrisp "*Sigh*. I’m supposed to be inheriting this place from paps, a well-known and respected farmer, I don’t want to seem weak."
        mc "You’re not weak, you’re one of the strongest people I’ve ever met."
        show honeycrisp tears with dissolve
        honeycrisp "*Sniff* You’re gonna make me cry, stud."
        "Has she been struggling with these barrels all morning? Tracks on the ground seem to suggest as much."
        show honeycrisp closesatisfied with dissolve
        "She beckons me in for a hug and we embrace in the barn."
        mc "You definitely need to build up the courage to talk to Anna about this."
        show honeycrisp closeshy with dissolve
        "Honeycrisp takes a deep breath before responding, she seems so stressed from the overwork."
        honeycrisp "Yeah, you’re right [playername]."
        show honeycrisp neutral with dissolve
        "I pull away from the hug and lean back on the wagon."
        mc "You can’t run this farm on your own."
        honeycrisp "You mentioned Anna? I know Anna can help; she has always been there for me…"
        show honeycrisp sad with dissolve
        honeycrisp "I was just too anxious to say anything when she was here before…"
        "Ah, these sisters… They really are alike; they're both exceedingly shy, however, Honey is much better at hiding it. "
        mc "To be honest Honey, the reason I was in the house earlier with Blossom is because we were trying to help you."
        if confessedsexwithblossom == 1:
            show honeycrisp angry with dissolve
            honeycrisp "So y’all didn’t have sex and that was a cover up?"
            mc "Oh, we did that as well, sorry."
        show honeycrisp shy with dissolve
        honeycrisp "Help me? What do you mean---"
        show honeycrisp shocked with dissolve
        stop music fadeout 5.0
        unknown "Hooooooooooooooooooooooiiiiiiiiiiii"
        "A loud cheer can be heard outside, a familiar female voice yelling out."
        honeycrisp "Oh? That’s…"
        hide honeycrisp with dissolve
        show bg farm with dissolve
        "We pop our heads out the barn, and we’re greeted with a friendly face."
        show anna laughing with dissolve:
            xpos 700
            ypos 30
        show honeycrisp shocked with dissolve:
            xpos 200
            ypos 10
        anna "Oh my gosh, Honey! It’s so great to see you!"
        play music sad2
        show anna happy with dissolve
        anna "[playername]! Wow, both of you, I picked a wonderful day to visit!"
        show honeycrisp sad with dissolve
        "I expect Honey to give her usual positive greeting, but to my surprise she seems nervous."
        "Anna quickly reads the mood and adapts to a softer tone."
        show anna neutral with dissolve
        anna "Uhmm… Not a good time?"
        mc "Actually, this is the perfect time, we were just talking about you."
        "Taking my lead, Honey perks up, her vigour restored."
        show honeycrisp happy with dissolve
        honeycrisp "That’s right! Pardon my surprise."
        honeycrisp "I think uhm, we should talk about the farm…"
        show anna happy with dissolve
        anna "That’s why I’m here. I got your letter!"
        show honeycrisp shy with dissolve
        honeycrisp "Letter? I… I didn’t…"
        anna "Quite a surprise to see how neat the handwriting was considering your injury, I guess [playername] must have written it."
        mc "That was Blossom’s neat handwriting."
        show anna laughing with dissolve
        anna "Ohh, she wrote the letter? I didn’t even realize."
        mc "Yeah, Blossom really wanted to help Honey, so we wrote the letter together asking if you’d help."
        show anna happy with dissolve
        anna "Aww, that’s so sweet."
        show honeycrisp sad with dissolve
        honeycrisp "You two did that for me? Y'all are too nice to me…"
        "To our surprise, the steadfast Honeycrisp starts tearing up."
        show anna surprised with dissolve
        anna "Don’t cry! Hun!"
        show anna satisfied with dissolve:
            xpos 600
            ypos 30
        show honeycrisp tears with dissolve:
            xpos 325
            ypos 10
        "Anna cuddles Honey, holding her close in a soft fluffy embrace."
        honeycrisp "E-Everyone is too kind to me…"
        show anna happy with dissolve
        anna "Of course we are Hun, everyone here wants the best for you, and you absolutely deserve it."
        anna "I received the letter, and I’m incredibly happy to help, I think expanding our relationship would be perfect for our farms."
        show honeycrisp shy with dissolve
        honeycrisp "Y-Yeah… I finally admit it, I need help. I’m so tired of trying to do everything by myself."
        honeycrisp "I’m sorry it took me so long to admit it."
        mc "Even people as tough as you need a helping hand sometimes, there’s no shame in that."
        anna "We’re all here for you, we always have been."
        anna "Gosh, I just wish you said something earlier Hun, when I saw you had a new man around the farm, I thought you had it all figured out."
        show honeycrisp happy with dissolve
        honeycrisp "[playername] has been so much help, I can’t thank him enough."
        mc "Heh, I do my best."
        honeycrisp "Anna too, thank you so much for coming here today…"
        anna "I came as soon as I could, I can’t leave a friend in need."
        show anna laughing with dissolve
        anna "Today, I’ll work for you, just tell me and [playername] what to do, after that, we’ll talk business."
        show honeycrisp shy with dissolve
        honeycrisp "B-But…"
        mc "Even if you want to keep working today, you should take a small break Honey. Don’t worry about us, we’ll have all these barrels delivered before you know it."
        show anna happy with dissolve
        anna "Yeah, you should go see Blossom, sounds like you have some catching up to do regarding this secret letter she sent out!"
        show honeycrisp satisfied with dissolve
        honeycrisp "Alright…"
        honeycrisp "Once y’all are done, come back to the house, me and Blossom are going to make the most delicious lunch you’ve ever had."
        hide honeycrisp with dissolve
        "Honey heads back to the farmhouse leaving us to sort out the barrels again."
        stop music fadeout 5.0
        hide anna with dissolve
        show bg barn with dissolve
        pause 0.4
        "…"
        pause 0.4
        show anna satisfied with dissolve
        anna "Bless her… She’s still struggling over the loss of her father, I can’t even imagine how much that hurt her."
        show anna neutral with dissolve
        anna "I hadn’t realized how much the loss was affecting Hun."
        show anna surprised with dissolve
        anna "I haven’t seen her cry before, even if it was just a few tears."
        show anna satisfied with dissolve
        anna "I always looked up to Honey as a beacon of strength."
        show anna neutral with dissolve
        anna "I guess it was naive of me to not see through her smiles and realize how deeply she's hurting."
        anna "I'm supposed to be one of her best friends but I didn't even notice, I have this pit of guilt in my tummy right now..."
        mc "Don't feel guilty, you can make those tears her last, you can make things better for her, right?"
        show anna happy with dissolve
        anna "That’s right, I’m going to strike a business deal with her similar to the milking deal. I’ll send someone to work here, and in the evening, she’ll come back with some produce that covers the cost."
        show anna laughing with dissolve
        anna "It’s a pretty nice deal for both of us since Hun’s farm grows produce that we don’t, I want to try those yummy parsnips."
        mc "That’s great news! Ever since I arrived I knew this farm was far too big for just a single person to run it."
        show anna happy with dissolve
        anna "Exactly! It should be profitable for both of us too, we’re just far enough away from each other to have different customers"
        mc "Well, perfect, especially for an eager businesswoman like yourself."
        show anna laughing with dissolve
        anna "Mhm! I’ve been looking to start a new farm, however it’s hard to fund a venture like that. But if me and Honey start a partnership, we could become big players in the industry. Why stop at two farms, why not three, or four?"
        play music farm fadein 15.0
        "Anna’s eyes are practically glowing with passion. I hope she can use that same passion to lift these barrels though."
        mc "Honey wanted us to deliver these barrels, we couldn’t lift them on our own, do you think you and I can do it?"
        show anna happy with dissolve
        anna "Oohh, barrels? Easy peasy, cutie!"
        "The two of us get into position around a barrel, bending at the knees, we position our hands underneath the barrel and to my surprise it raises. Not easily mind you, I still have to exert myself."
        "We manage to hoist the barrel onto the wagon! It’s much easier with the strength of a cow girl on my side."
        show anna surprised with dissolve
        anna "I’m surprised Honey managed to fill this many barrels all by herself, that girl must'a been working fifteen hour days."
        "We lift the next barrel and plonk it onto the wagon."
        mc "We’ll need to push this into town, right? How many barrels do you think we could take at once?"
        show anna neutral with dissolve
        anna "I’m thinking… two trips of four?"
        show anna happy with dissolve
        "We get four barrels onto the wagon, and pulling together it moves rather easily, it’s downhill on the way to the market as far as I’m aware too, so this is no problem."
        show bg arcadiasuburbs with dissolve
        pause 1.0
        "Together we push the wagon and make some conversation as we go"
        pause 1.0
        show anna laughing with dissolve
        anna "Phew, getting all sweaty in the barn with you reminds me of last time. I guess we can’t spend every working day having sex, right sugar?"
        mc "Every working day? Sure, you could, we just need to get the work done first."
        show anna horny with dissolve
        anna "Haha, are you flirting with me? I’m still in heat, so go easy on me, [playername]."
        mc "Ahah sorry, I shouldn’t tease you too much, right?"
        show anna happy with dissolve
        anna "Mmm, probably not today since I’m visiting. If you tease me all day, I’ll be too horny to focus."
        mc "You should tell that to Honey, she often flirts with me while I work, so by the time we finish I’m really horny."
        show anna laughing with dissolve
        anna "She’s so naughty, she does that to me too you know."
        label farmvisit3honeydialogue:
            menu:
                "Just how deep does your sexual relationship go with Honey?":
                    show anna happy with dissolve
                    anna "Aye, we typically have sex when she milks me."
                    show anna laughing with dissolve
                    anna "We actually have a strap-on hidden in the barn, but we didn't need it when you arrived, ehehe."
                    mc "Who uses the strap-on?"
                    show anna happy with dissolve
                    anna "We take turns."
                    show anna laughing with dissolve
                    anna "And yes, when I asked you to spank Honey, I knew she liked that from experience, hehe!"
                    jump  farmvisit3honeydialogue
                "We should get together again sometime. A time like before is too good to only experience once.":
                    show anna happy with dissolve
                    anna "If you manage to visit me on a milking day, I'm sure Hun would love to."
                    mc "What if I wanted a one on one experience?"
                    show anna laughing with dissolve
                    anna "Oohh babe, you should come visit me sometime and I'll show you what this cow can do."
                    "I can still picture what it was like having sex with Anna, along with how good it felt. It was exciting to do it with another species of girl, I definitely want to have sex with her again."
                    jump farmvisit3honeydialogue
                "(Proceed)":
                    mc "I may visit your village one day in the future, it'll be fun."
        show anna happy with dissolve
        anna "Ooo, you spoil me. I’ve been thinking about the things we did in the barn in my head over and over."
        mc "You’re in luck then, I’d quite like to try it again."
        show anna closesatisfied with dissolve
        "Anna leans over and kisses me on the cheek."
        show anna happy with dissolve
        anna "I’m glad I got to meet you [playername], you’re such a gentleman."
        show anna laughing with dissolve
        anna "And you’ve got a deal, if you ever come visit my farm, I’ll pay you for any work you do, and I’ll be sure to give you the full sexy service."
        stop music fadeout 5.0
        hide anna with dissolve
        show bg black with dissolve
        pause 0.5
        "…"
        pause 0.5
        "It ends up taking around two and a half hours to finish the barrel runs, leaving the timing appropriately around lunch."
        show bg farmkitchen with dissolve
        "Anna and I return to the farmhouse where Blossom and Honeycrisp are joyously cooking up a treat."
        play music day
        show honeycrisp happy at center with dissolve
        show blossom happy with dissolve:
            xpos 850
            ypos 75
        show anna surprised at left with dissolve
        honeycrisp "Howdy y’all, I’ve baked us all some delicious apple fritters"
        show blossom laughing with dissolve
        blossom "And some of our homemade ice-cold cider to go with!"
        mc "Apple fritters? Delicious!"
        show anna laughing with dissolve
        anna "What a treat, thank you so much!"
        show blossom happy with dissolve
        show honeycrisp laughing with dissolve
        honeycrisp "Least me and Blossom could do for all the help, y’all have been absolute blessings."
        blossom "We couldn’t have done it without ya!"
        "Blossom smooches me on the cheek and personally hands me a fritter, it's ludicrously delicious, I can’t stuff it into my mouth fast enough."
        mc "It was my pleasure, I’ve loved getting to know you three, I’m looking forward to working here again."
        show anna happy with dissolve
        anna "Same to you [playername], I think you’ve managed to find a spot in each of our hearts!"
        show honeycrisp happy with dissolve
        honeycrisp "…and our beds!"
        show anna surprised with dissolve
        anna "Shh, lewd!"
        "Blossom hands each of us a glass of cider, playfully winking as she hands me mine."
        blossom "Here’s to a brighter future!"
        show anna laughing with dissolve
        show honeycrisp laughing with dissolve
        show blossom laughing with dissolve
        everyone "Cheers!"
        stop ambience fadeout 3.0
        stop music fadeout 5.0
        scene bg black with s
        "…"
        play ambience ambienceday
        "After a delicious lunch, and a long afternoon of work, I return to the kitchen to collect my pay and rest. Anna has already returned home, and Honey is as ever tirelessly doing extra work before sun sets."
        "Once again, it’s just me and Blossom in her bedroom enjoying a cup of tea as we relax, this time without milk."
        show bg blossombed with dissolve
        pause 0.3
        show blossom closehappy with dissolve
        pause 0.3
        blossom "What do you think of the farm then? This must be your third day here now."
        mc "I love working here. Sure, there’s plenty of strenuous physical activity but there’s catharsis in that."
        show blossom closelaughing with dissolve
        blossom "I always say you never get to the end of a day of hard work and regret it."
        mc "Especially when Honey cooks lunch, the food is delectable, and I love being able to rest here at the end of the day and enjoy a cup of special apple tea."
        show blossom closehappy with dissolve
        blossom "Aww, well, you can take some home with you, if you want."
        mc "That’s generous of you, I may just do that."
        show blossom closelaughing with dissolve
        blossom "Of course, you can always visit, you’re always welcome to come see me, or Honey, or even Anna again."
        show blossom closehappy with dissolve
        blossom "That being said, I gotta know, who’s your fave?"
        menu:
            "You, of course!":
                show blossom closelaughing with dissolve
                blossom "Ahah yes! Maybe you can be my boyfriend after all."
                mc "Are you asking me out?"
                show blossom closebashful with dissolve
                blossom "Mmm, maybe, are you saying yes?"
                mc "I’ll have to give you an answer a bit later."
                mc "Maybe in the future, you never know."
                show blossom closeawkward with dissolve
                blossom "Ohh, I think my heart just swooned."
            "Anna":
                show blossom closelaughing with dissolve
                blossom "Awhh, I can see that. Anna is such a great character, I think many a man would admire her."
                show blossom closeshocked with dissolve
                blossom "But I thought she wasn't interested in relationships and stuff."
                mc "You’re right, she did mention that, however I'm a bit of a special case."
                show blossom closesatisfied with dissolve
                blossom "Y’all have that interspecies charm that some mares love, cow girls must like it too."
                mc "It has been quite a clutch for me."
            "Honeycrisp":
                show blossom closeshocked with dissolve
                blossom "Ahaha, darnit!"
                show blossom closehappy with dissolve
                blossom "If you ever decide to date mah sister, you’ll have to deal with my flirting, so be careful."
                mc "Now that’s just rude."
                mc "I wouldn’t be able to resist."
                show blossom closelaughing with dissolve
                blossom "Hehe, shoulda picked me, then!"
        show blossom closehappy with dissolve
        blossom "You know… I really enjoyed our time together."
        show blossom closelaughing with dissolve
        blossom "I always wanted a cute boyfriend like you."
        mc "You probably don’t want to date me; I’ve slept with both Anna and your sister."
        show blossom closeawkward with dissolve
        blossom "Bleh, true, I want a boy all to myself, and it seems you’re in hot demand."
        mc "I bet you’d still welcome me to your bedroom though."
        show blossom closebashful with dissolve
        blossom "Hmm… I guess you’ve got me there, that means I’m part of the problem!"
        mc "Problem? It doesn’t have to be a problem, let’s just sit back, relax and have some fun while we can. You can worry about settling down when you’re older."
        show blossom closehappy with dissolve
        blossom "Ooohh, that’s what Melody is always telling me, but I’m too shy to actually approach anyone."
        mc "Hmm, that’s quite the predicament, but you approached me more or less, remember? I think you’re more confident than you realize, you have the same fiery soul as your sister."
        show blossom closelaughing with dissolve
        blossom "R-Really? Me? Uuu, I guess you’re right, I need to stop overthinking."
        mc "Some say that your brain is your own worst enemy."
        show blossom closehappy with dissolve
        blossom "Yeah… Yeah! That’s it, that’s exactly my problem, my dummy brain is holding me back."
        blossom "I want to be more like my sister, strong and confident."
        blossom "I know she used to be shy like me when she was young, however that just means I have the potential to outgrow my worries and become self-assured."
        mc "Honestly, in my eyes, you already have that confidence deep inside. You had the strength to do something even your sister couldn’t do."
        show blossom closelaughing with dissolve
        blossom "The letter… Yeah! That was all me, I kicked butt!"
        mc "You sure did."
        "As the sun starts to slowly sink beneath the distant mountains, I take one last sip of my tea."
        mc "Thank you for the tea, I think I’ll set off now."
        show blossom closehappy with dissolve
        blossom "Visit me lots, ‘kay? I really wanna cuddle more."
        blossom "Maybe if you get attached to me you can become my cool boyfriend."
        mc "I assure you, I’m not that cool. Although, I may be so inclined to come visit for some fun."
        show blossom closeawkward with dissolve
        blossom "Oh, and my sister doesn’t know that we had sex, let’s just keep that one between us, okay?"
        if confessedsexwithblossom == 1:
            "I’ve already accidentally told her, but she doesn’t need to know that, a secret within a secret."
        mc "Yeah I’ll keep quiet about that. You don’t mind me sleeping with her though?"
        show blossom closehappy with dissolve
        blossom "Nah, not at all, if anything that just makes me want to sleep with you more. I don’t know, something competitive within me spurring me on."
        blossom "Anyway, I’m keeping you from leaving, you should head off before it gets dark."
        mc "No worries, it has been my pleasure."
        show blossom closelaughing with dissolve
        blossom "Have a nice evening [playername], hope to see you again sometime soon!"
        mc "Same to you!"
        mc "Oh, and one more thing."
        mc "Next time, no milk, okay?"
        show blossom closehappy with dissolve
        blossom "Hehe, you have a deal, no milk!"
        hide blossom with dissolve
        stop ambience fadeout 50.0
        pause 0.4
        show bg farmkitchen with dissolve
        "I leave her room, head downstairs and step out the house having said my goodbyes."
        show bg farmnight with dissolve
        "As I walk down the path leading out of the farm, I spot Honeycrisp on the way."
        show honeycrisp happy with dissolve
        honeycrisp "You weren’t jus’ about to leave without saying goodbye to me?"
        mc "Uhh, technically I think I’ve done that twice already."
        show honeycrisp embarrassed with dissolve
        honeycrisp "Shh… I want to give you something before you leave."
        show honeycrisp closesatisfied with dissolve
        "She kisses me on the lips, it’s soft, yet short, leaving me wanting more."
        show honeycrisp neutral with dissolve
        honeycrisp "I realize we’ve never uh, had a chance to have sex one on one yet… But hopefully, if I have some help around here, I’ll be more available for you sugarcube…"
        mc "Let me guess, you want me to come back and see you?"
        show honeycrisp embarrassed with dissolve
        honeycrisp "I’m still in heat stud, I could use another pounding from you. Let’s call it a benefit in addition to your usual pay?"
        show honeycrisp happy with dissolve
        honeycrisp "Or a part of your job, whatever you prefer, stud."
        show honeycrisp closesatisfied with dissolve
        "I grab her by her butt and pull her in closer for another prolonged kiss."
        show honeycrisp horny with dissolve
        honeycrisp "Mmphh… *Kiss*… Have a good night, stud…"
        mc "You too, sexy."
        hide honeycrisp with dissolve
        "Finally, with that, I head back home."
        show bg worldmapnight with dissolve
        play ambience ambiencenight
        "..."
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        if livingwithmoxie == 1:
            play music wagon
            show bg moxiewagonlamp with dissolve
            "As I arrive at the wagon I slump down onto Moxie’s sofa, somewhat fatigued from all of the strenuous exercise required at the farm."
            "Moxie isn't around, but she soon manages to sneak up on me."
            show moxie closesmug with dissolve
            moxie "You’re a bit late today. Lemme guess, balls deep?"
            mc "Hey Mox, not quite, I was just enjoying some tea with Blossom."
            show moxie shocked with dissolve
            moxie "Oh, no sex today then?"
            mc "You’re fairly one-track minded tonight. Yeah, I had plenty in the morning, Blossom rode me so hard she ended up getting a cramp."
            show moxie laughing with dissolve
            moxie "One-track because I wanted to know if you slept with her, and you have, niiiice."
            mc "Sex notwithstanding, I helped Honeycrisp, I made a positive change and I feel great because of it."
            show moxie neutral with dissolve
            moxie "Help her? What do you mean? Didn't you tell me you just slept with her sister?"
            mc "Honey was trying to run that entire farm on her own with her dominant hand in a cast."
            mc "Me and Blossom concocted a plan to lighten the load she has to burden and get her some employees."
            show moxie laughing with dissolve
            moxie "Where does the sex fall into that plan?"
            mc "Hey, quiet you! I helped out and things are definitely looking better for the farm now."
            show moxie happy with dissolve
            moxie "Check you out! Being a good soul and helping out the residents of Arcadia."
            show moxie althappy with dissolve
            moxie "In a small community like this, word gets out, good things may come your way."
            mc "Speaking of small community, I was delivering some produce to the market today with Anna, and I could see you performing your magic show from a distance."
            show moxie embarrassed with dissolve
            moxie "W-Wah?! You saw me?"
            mc "Something wrong?"
            show moxie sad with dissolve
            moxie "Noooo, you’re not allowed to see, it’s too embarrassing!"
            mc "But it’s public, everyone can see you."
            show moxie angry with dissolve
            moxie "You know what I mean airhead, too embarrassing to let you see me do it."
            mc "I don’t think I understand what you mean at all, haha."
            moxie "Then how about I watch you next time you go have sex with someone, huh?"
            mc "What? No! What kind of comparison is that anyway? Those two concepts aren’t even in the same universe, you’re crazy!"
            show moxie laughing with dissolve
            moxie "It's cause you were totally stalking me, so I should stalk you, muhaha."
            hide moxie  with dissolve
            "Moxie sticks her tongue out at me and goes to make dinner."
            jump evening
        elif livingwithbutters == 1:
            play music butters
            show bg buttershousenight with dissolve
            "As I arrive at the cottage I slump down onto Butter's sofa, somewhat fatigued from all of the strenuous exercise required at the farm."
            "Butters isn't around, but she soon appears from her work.."
            show butters closedresshappy with dissolve
            butters "Sorry I'm late today. How've you been?"
            mc "Hey Butters, it's been great at the farm today. I was just enjoying some tea with Blossom."
            show butters dresssurprised with dissolve
            butters "Blossom is such a delightful girl, how did it go?"
            mc "Blossom rode me so hard she ended up getting a cramp."
            show butters dresslaughing with dissolve
            butters "Bless her, the first time can be quite an experience, hehe."
            mc "Sex notwithstanding, I helped Honeycrisp, I made a positive change and I feel great because of it."
            show butters dressneutral with dissolve
            butters "What did you do?"
            mc "Honey was trying to run that entire farm on her own, with her dominant hand in a cast."
            mc "So Blossom and I concocted a plan to lighten the load she had to burden, by getting her some employees."
            show butters dresslaughing with dissolve
            butters "Which part of that plan involves sleeping with three people?"
            mc "That was a side operation I had running concurrently. Other than that, I helped out, and things are definitely looking better for the farm now."
            show butters dresshappy with dissolve
            butters "You're a good friend and a good fuck, no mare could ask for anything better."
            butters "In a small community like this, good things may come your way."
            jump evening
        else:
            pass
    label honeycrisptalk:
        menu:
            "Talk about recent events":
                honeycrisp "Ever since you came along things have been going so well lately."
                mc "Don't forget the work your sister and Anna did, I was only a small part of that."
                honeycrisp "Ay, but sometimes the smallest cog is required to make the machine run."
                honeycrisp "I think you were the exact knock back to reality I required."
                honeycrisp "Sometimes you're so alone, and you work so hard you forget what the outside world is like."
                mc "It's good to reach out and reconnect with friends and family every so often."
                mc "You need to remember that you're not alone, and you can get the support you need."
                honeycrisp "You're right stud, but you forget that one of the hardest steps sometimes is reaching out and accepting that support."
                honeycrisp "For that, the solution is a little more cloudy. I'm just fortunate that you decided to show up when ya did."
            "Plans for the future?":
                mc "Now you're working closely with Anna and have an employee, what are your plans for the future?"
                honeycrisp "Hmm, good question stud."
                honeycrisp "Ya see, I was never the planner in the farm, that was always paps. He always had a plan and ambition."
                show honeycrisp closesad with dissolve
                honeycrisp "Which is why it felt so icky for him to pass in his prime, he had so much spirit in him."
                honeycrisp "Never got to see the fruit of his work, or even the opportunity to have grandkids."
                "See sighs and tears up slightly, it's clear that the memories are still painful."
                mc "I've never actually asked because it felt like a sensitive topic, but how did he pass?"
                honeycrisp "He didn't even get to die in an interesting way, it was a disease that caused him to deteriorate so fast."
                honeycrisp "Paps was healthy one moment, and in the next week he was immobilised in hospital, and then in a month..."
                mc "It's shocking how fast it can happen sometimes."
                mc "What about your mother, is she not around?"
                honeycrisp "Nah, we're estranged from her. I have no idea where she is, or what she's doing."
                honeycrisp "My paps was a single father for years, quite a rare case in Arcadia. After mother left, he didn't care much for dating, Blossom and I were always his priority."
                show honeycrisp closeneutral with dissolve
                honeycrisp "Gosh, anyway... Sorry to bore you with that tangent, you asked me if I had any plans for the future."
                show honeycrisp closehappy with dissolve
                honeycrisp "Guess I'll have to think about it more now, thanks stud."
            "How did you become a farmer?":
                mc "How did you become a farmer?"
                honeycrisp "It has always been in my blood, stud. Hey, that rhymed!"
                honeycrisp "I helped out paps ever since I was a tiny girl."
                honeycrisp "Back then he'd give me small 'made up' jobs for fun, like uh, raking the leaves!"
                mc "You've never considered any other work?"
                honeycrisp "I mean it's a farce ain't it. I'd probably have to sell the farm, and that's been in our family for longer than I know."
                honeycrisp "But I don't mind being a farmer for the rest of mah days, it's incredibly satisfying work, and every evening is free time so I never burn out."
                mc "You reckon your children will run the farm then?"
                honeycrisp "Hah, I don't tend to think that far forward in mah life, I just meander mah way through each day."
                honeycrisp "What about you? Are you ever going to settle down with a permanent job?"
                mc "That's a great question, it would probably pay more if I specialised into one career."
                show honeycrisp closelaughing with dissolve
                honeycrisp "Y'all always welcome to make working here your career, although if you do we won't be able to have children to run the place after us, ahaha!"
                mc "That's very cheeky of you to presume, haha."
            "Ask what Honey does in her free time":
                honeycrisp "Now that I've actually got free time, I've been getting out more and visiting friends."
                mc "Anyone in particular?"
                honeycrisp "I like to pop down to the Riding Mare for a pint of cider and Ruby often visits."
                honeycrisp "It may be the cider I make, but it's even more satisfying drinking with friends."
                mc "I should join you sometime."
                honeycrisp "Absolutely, just visit the bar in the evenings."
                honeycrisp "I'd give you a specific time and date, but the fun of visiting the bar is just seeing who's there!"
            "Back":
                jump honeycrispmenu
        $ honeycrisptalks = 1
        jump honeycrispmenu
    label honeycrispallsex:
        label honeyblossomthreesome:
            scene bg black with dissolve
            play music sex1 fadein 3.0
            show honeyblossomb threesome
            show honeyblossom threesome1
            with dissolve
            "The sisters present themselves eagerly on the bed, their pussies soaked with lust and their expression glazed with need and obedience."
            "My cock is throbbingly erect, I'm going to take my time loving these girls."
            honeycrisp "Ahh, this is a little weird, you're lucky I like you."
            blossom "You'll warm up to it when you see how much fun it is!"
            "Blossom lowers her eyes slightly as I lean in. Her expression is shy, but she still licks her lips as my cock nears her aching pussy."
            "She blushes as I take hold of her fuzzy thighs and move closer. I rub the head of my member against her dripping snatch, coating my tip with her wetness."
            play sound cum
            show honeyblossom threesome2 with dissolve
            play ambience sex fadein 3.0
            "With enough of her juices gleaming on my glans to act as lubricant, I align her slippery pussy with my cock and push forward."
            "Parting her lips, she moans with relief as I slowly enter her. However, I don’t give her time to savour the feeling, as I immediately begin humping her slick pussy."
            blossom "Haahh, yesshh… This is so good, I’m so glad the three of us can enjoy this together…"
            honeycrisp "Ooohh, why is this turning me on so much?"
            show honeyblossom threesome3 with dissolve
            blossom "Y-Yes, I love your cock, [playername]!"
            "As usual, the girls never touch each other, but that doesn't stop them from touching themselves as Honeycrisp masturbates while she watches."
            "Not to mention how much Blossom is enjoying this, her pussy twitches as I go harder; fucking her with such force that even her tiny tits bounce up and down."
            blossom "Ohhh, oooohhh! [playername]! Y-You’re going so fast today! Oohh… You’re gonna make me come!"
            "Within a few moments I could feel her vagina clamp around my girth, wringing it as she easily reached her climax."
            "Her encouraging moans combined with the fastest pumping I’m able, I can’t stand the tightness of her pussy for long."
            play sound cum
            show honeyblossom threesome4 with cum
            play sound cum
            show honeyblossom threesome4 with cum
            "Pressure builds in my loins as my climax surges throughout my entire body, releasing a generous amount of thick cum which her pussy greedily accepts."
            play sound cum
            show honeyblossom threesome4 with cum
            play sound cum
            show honeyblossom threesome4 with cum
            stop ambience fadeout 2.0
            blossom "Ooohh, mmmphhh, s-so good!"
            show honeyblossom threesome5 with dissolve
            "Recklessly, I pull out as a last few spurts of cum splatter over Blossom’s tummy and I move over to Honeycrisp."
            honeycrisp "Dang stud, y’all crazy today!"
            play sound cum
            play ambience sex fadein 3.0
            show honeyblossom threesome6 with dissolve
            "Honey’s pussy was already drenched with her lubricative fluids allowing me to sink to the hilt in a single motion."
            "Resuming sex at the same intensity as before, Honeycrisp’s back arches and toes curl in response to the immediate spike in pleasure."
            blossom "Mm… Cum inside her too [playername]!"
            honeycrisp "Yeah stud! Ahhh, ahh, gimmie your cum too, mmphh!"
            "Honey fucks a lot more proactively than Blossom did, her hips bucking towards me and clashing with each thrust, making my job a lot easier."
            "Together we rut, the disgusting lewd squelching sounds are more than enough to make Blossom blush."
            show honeyblossom threesome7 with dissolve
            honeycrisp "Haahh, ahhh, don’t hold out on me stud! Th-this isn't so bad after all!"
            "It takes a frustratingly long time to achieve a second orgasm in a row, even with Honeycrisp's rocking hips."
            "But Honeycrisp’s moans and movements eventually close the distance, as my cock returns to its close to climax throbbing state."
            "With a few final deep thrusts, an intense orgasmic sensation ascends my loins and fills my body."
            play sound cum
            show honeyblossom threesome8 with cum
            play sound cum
            show honeyblossom threesome8 with cum
            "Finally, my cock uploads a jet of cum causing Honey to gasp as she feels it enter her. Her pussy convulses into an orgasm, causing her entire body to rack, her breasts jiggling wildly."
            play sound cum
            show honeyblossom threesome8 with cum
            play sound cum
            show honeyblossom threesome8 with cum
            stop ambience fadeout 3.0
            stop music fadeout 3.0
            "Together we both pull away, cum now oozing from both mares."
            scene bg black with dissolve
            "The three of us spend a few minutes cuddling before we go our separate ways."
            "I feel like a total alpha right now."
            jump evening
        label honeycrispsex:
            stop ambience fadeout 5.0
            show bg honeycrispbed with dissolve
            $ honeycrispcomplete = 1
            play music sex1 fadein 3.0
            show honeycrisp closehorny with dissolve
            $ rand = renpy.random.randint(1,2)
            if rand == 1:
                "With a smirk, Honeycrisp pushes me down onto her bed using the hand that was once in a cast. Now that it's free, I'm at the complete mercy of this girl's sexual appetite, and she's ready to show it in full force tonight."
            else:
                "Giggling, Honeycrisp seductively presses me against the soft sheets of her bed using her main hand. She crawls towards me like a predator catching its prey. She isn't going to hold back tonight."
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
                honeycrisp "Ahh, I love your cock... Ever since our rut in the barn I've been thinking about this while I masturbate..."
            play ambience sex fadein 3.0
            $ rand = renpy.random.randint(1,2)
            if rand == 1:
                "Her pussy's comfortable tightness squeezes and massages my shaft as I give myself over to Honey's dominant riding."
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

            show honeycrisp cowgirl3 with dissolve
            if rand == 1:
                honeycrisp "Aahhh, ahh... Do you like that? You like mah pussy?"
            else:
                honeycrisp "Mmphh, I-I'm gonna come soon, ahh..."
            $ rand = renpy.random.randint(1,2)
            if rand == 1:
                "She even begins to moan freely, that coupled with the wet schlicks of our copulation leaves me to believe Blossom could definitely hear us right now."
            else:
                "Unable to hold back any longer, a few moans slip out of the orange mare's mouth while even lewder sounds slip out of her pussy as wetness freely dribbles and bubbles at our point of contact."
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
            show honeycrisp cowgirl4 with cum
            play sound cum
            show honeycrisp cowgirl4 with cum
            play sound cum
            $ rand = renpy.random.randint(1,2)
            if rand == 1:
                "As her pussy continues to grip around my shaft I find the pleasure is too much and I unload my cum deep inside her womb."
            else:
                "My cock begins to erupt inside her, flooding her pussy and womb with my thick cum."
            stop ambience fadeout 3.0
            show honeycrisp cowgirl4 with cum
            play sound cum
            show honeycrisp cowgirl4 with cum
            play sound cum
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
                "After her climax finishes, we're both left panting, although we quickly recover since I barely moved and Honey is no stranger to intense cardio."
            show honeycrisp closehorny with dissolve
            honeycrisp "Your cock is amazing, stud."
            play ambience ambiencenight fadein 10.0
            mc "Only half as good as your riding, Honey."
            "I say my goodbyes and give her a quick kiss on the cheek. To my surprise, the usually unaffectionate Honey blushes at the gesture."
            "The two of us spend a few minutes cuddling before we go our separate ways."
            jump evening
    label blossomvisit:
        show blossom closehappy with dissolve
        blossom "Oh, hello [playername]! It's always a good start to the day when you visit."
        if boutiquevisit3 == 1 and blossommelodytalk == 0:
            hide blossom with dissolve
            play music melodytheme
            show melody closefufufu with dissolve:
                xpos 600
                ypos 70
            show blossom closeshocked with dissolve:
                xpos 50
                ypos 75
            melody "Ohoh, you're coming to perv on my friends now, are you?"
            mc "Oh no, the demon is back!"
            $ blossommelodytalk = 1
            melody "You can't escape me [playername], I watch you fap!"
            blossom "Uhm, wha?"
            mc "Whatcha doing here Melody?"
            show melody closehappy with dissolve
            melody "Just visiting my bestie, we've got some work to do later on."
            show blossom closehappy with dissolve
            blossom "We're working on an album together, it's going to be awesome."
            melody "Care to tell me why you're snooping around in little girl's bedrooms, [playername]?"
            mc "I'm just here to visit Blossom, I didn't think I'd get a double dose of loli."
            show melody closedeath1 with dissolve
            melody "Ohoh, did you just call me a loli?"
            blossom "Don't encourage her [playername]."
            show melody closehappy with dissolve
            mc "My bad."
            melody "Anyway, we better get off, sorry 'stud', no time to have sex with Blossom this morning."
            show blossom closebashful with dissolve
            blossom "A-Ah don't know whatcha talking about!"
            melody "Haha, I love how southern she gets when she's lying."
            mc "I'll see you two later."
            stop music fadeout 3.0
            melody "Sure thing champ, I'll see you in the boutique."
            jump prefarmmenu
        menu blossomvisitmenu:
            "Talk" if blossomtalks == 0:
                jump blossomtalk
            "Sex" if blossomsex == 0:
                blossom "Hehe, I thought you'd never ask."
                jump blossomsex
            "Leave":
                blossom "Yeah, I better get to the music studio. See you later [playername]!"
                if annamilking == 7:
                    jump annamilkingevent
                else:
                    jump prefarmmenu
    label blossomtalk:
        menu:
            "What have you been up to lately?":
                blossom "I'm feeling much better now my sister's happy. I was getting residual stress if you know what I mean."
                mc "Yeah, I bet you're feeling relieved."
                blossom "Definitely. I've had the opportunity to focus on college more lately, I have some deadlines on music theory and I want to make some of my own music to put online too."
                stop music fadeout 3.0
                mc "Think I could listen to a few?"
                blossom "I'd love it if you could listen and tell me what you think."
                play music inpeace
                "I spend a few minutes listening to a selection of songs by Blossom, the genre of it surprises me."
                mc "There's a lot more drum and bass than I expected, I thought you liked pop and classical music."
                blossom "Oh I do, I like all sorts of music, but this is the kind of music I like to make the most."
                blossom "You see, a lot of people in the music industry just try to do the same thing."
                blossom "Me and Melody both make music like this, and we'd rather make something new and unique that people can enjoy, rather than doing the same thing everyone else is doing."
                blossom "It takes a certain bravery to make music that some people may genuinely dislike I guess."
                mc "There's nothing wrong with appealing to a niche crowd."
                mc "This music sounds like it would suit a nightclub, it just needs some meaty equalisation so you can really feel the bass."
                blossom "Oh my gosh, exactly! I love dancing. Me, you and Melody should go out clubbing sometime!"
                stop music fadeout 3.0
            "Any plans for the future?":
                mc "Any plans after college?"
                blossom "Hum... The idealist in me wants to become a full-time musician."
                blossom "But not just someone that plays music, but a composer... That's not easy though, not everyone gets noticed."
                blossom "Especially since I'm not trying to pander to the people with my music."
                mc "Haha, that certainly isn't the profitable route."
                blossom "I could always teach or tutor in the mean time, that pays well."
                blossom "It's quite fortunate that you're never short of job opportunities in Arcadia."
                blossom "It's just a question of whether you get the job you want I guess."
                mc "I wish you luck, it seems hard work pays off around here."
                show blossom closelaughing with dissolve
                blossom "Thanks [playername], I'll do my best."
                show blossom closehappy with dissolve
                blossom "Have you thought about what you want to do yet?"
                mc "Hmm... Not really..."
                mc "I'm your age though, so I'm not in a rush."
                blossom "I guess not, but I heard you're working job to job. Maybe you should get a career."
                mc "You've got a point, any recommendations?"
                blossom "Have you looked into college? If you're not from around here, maybe there's a course there that'll suit your needs."
                mc "Is it free?"
                blossom "Of course, dummy!"
                mc "Interesting..."
            "Talk about her cooking":
                blossom "You just missed breakfast, I could have made you some pancakes [playername]!"
                mc "Are they as tasty as your fritters?"
                blossom "Hehe, not quite, they don't have our special apples."
                mc "I feel like everything here has apples in it, at this rate you'll probably taste like apples if I kissed you."
                blossom "The pancakes didn't have any apples!"
                mc "Now I'm sad I didn't come sooner."
                blossom "Look, if you marry me, you can have those every morning!"
                mc "Hmm, tempting, tempting..."
                blossom "Come on, consider it! Can the other mares cook tasty treats as well as I do?"
                mc "Well, there's always Cream at the bakery."
                blossom "Hmph, I bet I have a tighter pussy though."
                mc "Does that taste of apples too?"
                blossom "Why don't you find out?"
            "Back":
                jump blossomvisitmenu
        $ blossomtalks = 1
        jump blossomvisitmenu
    label blossomsex:
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        $ blossomsex = 1
        "I climb into bed with Blossom and she playfully rolls me over."
        blossom "I'll be on top, I wouldn't want you to get too tired before work."
        hide blossom
        show blossomb1 sex
        show blossom sex1
        with dissolve
        play music sex1 fadein 3.0
        "As much as I'd like to protest, I'm left mesmerised as Blossom straddles me and starts to rub her pussy on my cock whilst giggling girlishly"
        "She wraps her spare hand around my member and starts to give it gentle strokes up and down, causing my cock to swell up and stiffen completely."
        "Blossom bites her lips and wiggles her hips, she's already eager for more, and the dripping wetness between her legs signals that she's ready to take me."
        play sound cum
        show blossom sex2 with dissolve
        "With a bit of her teasing, my cock is now raging hard and throbbing. Fortunately, Blossom is all too willing to satisfy as she lifts herself over me and allows my cock to sink deeply into her."
        "She takes her time sliding down my thick cock, I can feel my cock spread her lips apart with a delectable slowness until she's finally at the hilt."
        "Blossom lets out a satisfied sigh, stares into my eyes with dreamy longingness, and merely nods before her hips begin to move with a passion."
        play ambience sex fadein 3.0
        show blossom sex3 with dissolve
        "As she rises and falls along my member a mixture of gasps and moans slip from her lips as she loses herself in the throes of passion."
        show blossom sex3 with dissolve
        "Every drop of the hips is accompanied by a lewd, arousing schlick as her wetness gleams off my cock and driplets of her lust pool at my pelvis."
        show blossom sex4 with dissolve
        blossom "Aahhh, mmmphh, we should do this every morning, haahh, ahh..."
        show blossom sex4 with dissolve
        "Her riding gains speed and she arches her back in response to the quaking pleasure throughout her body, I too feel tense from the overwhelming sensation she's providing me."
        show blossom sex4 with dissolve
        "With each deep thrust I can feel myself getting closer and closer, her pussy trying to milk my cock with all its worth."
        show blossom sex4 with dissolve
        blossom "Mmphh, please cum in your lil' cumslut, please give me your cum!"
        "She begs as our sex devolves into an orgasmic mess, her pussy clamps down around my cock tightly which in turn pushes me over the edge."
        show blossom sex5 with cum
        play sound cum
        show blossom sex5 with cum
        play sound cum
        "And in sudden orgasm I shoot several thick loads deep into her womb which squelch and drip down our point of connection."
        show blossom sex5 with cum
        play sound cum
        show blossom sex5 with cum
        play sound cum
        "She rides out both of our orgasms with glee before the climax fades and with that our energy."
        stop ambience fadeout 3.0
        hide blossomb1
        show blossom closesatisfied
        with dissolve
        "Blossom snuggles against my chest and we cuddle, still joined at the hips."
        "For now, we ignore the thick wet mess left between our nude bodies and instead indulge in a long passionate kiss."
        show blossom closehappy with dissolve
        "She lets me go and pulls out, cum still dripping out of her pussy."
        stop music fadeout 3.0
        blossom "Haahh... Lovemaking is so messy, I need to get some tissues in my room if you're going to be a regular guest."
        show blossom closelaughing with dissolve
        jump blossomvisitmenu
    label annamilkingevent:
        if blossomvisit == 1:
            scene bg barn with dissolve
            show anna happy with dissolve:
                xpos 700
                ypos 20
            show honeycrisp nchappy with dissolve:
                xpos 200
                ypos 10
            "I return to the barn to find the girls cheerfully gossiping over cider."
        else:
            "As I arrive on the farmstead, it's completely quiet."
            "But I know exactly where to find the girls."
            show bg barn with dissolve
            play music castle fadein 3.0
            show anna happy with dissolve:
                xpos 700
                ypos 20
            show honeycrisp nchappy with dissolve:
                xpos 200
                ypos 10
            honeycrisp "Well, well... The stud appears."
            anna "Ohmigosh! You remembered?"
            mc "How could I forget the opportunity to work with my favourite girls?"
            honeycrisp "Hehe, let's make it as fun as it was last time."
        menu:
            "Work with the girls":
                stop music fadeout 10.0
                scene bg barnblur with dissolve
                show anna boobs with dissolve
                anna "All yours sugar."
                show anna boobs2 with dissolve
                "I inch my stool a little closer, so Anna’s breasts are right in front of my face."
                "I can already see the faint white drops on her nipples."
                anna "Oh my, you're making me drip [playername]."
                honeycrisp "Already? Here's the bucket!"
                "Honey takes one of the buckets and places it below us."
                play music sex1 fadein 10.0
                show anna milking1 with dissolve
                "I start by massaging her breasts with my hands, kneading them with my fingers, they're overwhelmingly soft."
                "She reacts extremely favourably to each and every touch on her sensitive breasts."
                anna "Mmmphh…"
                "With many metallic pitter-patters, the milk freely seeps from her nipples. She's enjoying the feeling so much, her eyes are practically rolled back."
                hide anna milking1 with None
                "The more she enjoys herself, the more her thighs subconsciously part as her body's desire to mate grows."
                show anna milking1 with dissolve:
                    xpos 425
                    ypos 0
                show annapussycloseup with dissolve:
                    xpos 0
                    ypos -75
                "It doesn't take much milking for her glistening pussy to be readily viewable, I can't help but occasionally glance down."
                anna "Haahh… It always feels so good when you do it."
                "Her pussy is enticing, as before one of my hands finds its way between her legs, teasing her pussy."
                "My other hand works on the breasts. The stimulation of her pussy causes the lactation to noticeably increase."
                honeycrisp "As always, you're the right man for the job [playername], drain those jugs dry."
                "With Anna sufficiently aroused, I use both my hands to really milk her nipples."
                "*Squirt*! A stream of milk immediately trickles out the moment I put any pressure on, all seeping down into the bucket, some of it getting sodden in the fur surrounding Anna’s breasts."
                "Applying pressure, the nipples in a regular pattern, pulling and squeezing one then the other, the milk squirts out in intervals while Anna squirms in delight."
                anna "Ahh, your cock is so... Hehehe."
                "Rather suddenly, I feel Anna lean over and wrap her furry hand around my shaft."
                show annahandjob with dissolve:
                    xpos -69
                    ypos 325
                honeycrisp "Here we go again, making me jealous!"
                "As Anna jerks me off, I concentrate on the milking. Finally past the midway point, the amount of milk slows down to a trickle."
                hide annahandjob with dissolve
                anna "Okay sugar, want to finish me off with your mouth?"
                mc "If you two want to have your fun with me, I'll need the aphrodisiac."
                hide anna milking1 with None
                hide annapussycloseup with dissolve
                show anna boobs2 with dissolve
                "I stop working her nipples and Anna leans in really, really close. Up close her moist fur sheens with the milk."
                show anna milking2 with dissolve
                "I bring one of her drippy nipples to my mouth and begin to suckle at the nipple."
                play sound cum
                anna "Mmphhh, yeshh!"
                "It takes a moment, but my mouth is suddenly intruded by a stream of warm and refreshing liquid."
                play sound cum
                hide anna milking2 with None
                show anna milking2 with dissolve:
                    xpos 500
                    ypos 0
                show annahandjob with dissolve:
                    xpos -69
                    ypos 325
                "I feel her furry hand once again wrap itself around my stiff shaft and she wastes no time in jacking back and forth."
                show anna milking3 with dissolve
                "As the milk from this first nipple seems to dry out, I pull back and focus on the next nipple."
                play sound cum
                show annapussycloseup with dissolve:
                    xpos 0
                    ypos -75
                hide annahandjob with None
                show annahandjob with dissolve:
                    xpos -69
                    ypos 325
                "All of her body language is begging for more, she’s incredibly aroused and her legs spread once again giving me a glimpse of her pussy whenever I want."
                "More of the delectable milk trickles into my mouth, warm and enticing. As it coats my mouth and drips down my throat it refreshes and invigorates me, drinking this strange milk feels wonderful. "
                "I close my eyes and give in to all the sensations, my cock throbs as Anna starts to speed up, I can feel myself potentially getting close to climax."
                "I suck harder but the milk stops coming, and Anna’s hand job slows down quite considerably."
                hide annahandjob with dissolve
                hide annapussycloseup with dissolve
                show anna closehappy with dissolve:
                    xpos 500
                    ypos 50
                "I drop her tiddy from my mouth and wipe my lip dry with the back of my forearm."
                show anna closehorny with dissolve
                anna "Looks like you milked me all dry! Time for me to return the favour."
                show anna paizuri with dissolve:
                    xpos -60
                    ypos 0
                "Anna lifts herself up slightly and clamps her breasts around my cock, completely squishing my shaft with a soft tightness."
                show honeycrisp ncmasturbating with dissolve:
                    xpos 600
                    ypos 0
                "Honey is masturbating as she enjoys the show, no need to hold back now she's out of her cast."
                "Her breasts feel so soft around my cock and they’re slightly damp too, it’s a snug fit."
                "She starts raising her torso up and down, so her breasts stimulate my shaft."
                anna "Mmphh, do you like this? Are you gonna cum for me?"
                "Lewd sloppy wet sounds keep coming from her breasts as she drools down onto my cock, providing some lubrication, that combined with the surprising tightness of her breasts around my cock is extremely stimulating.."
                "It won’t take me long to cum at all, I can even hear Honey moaning while she watches."
                "Anna uses her hands to squeeze her breasts together tighter as she glides up and down my shaft. It’s feels so skin-tight and wet with drool and sweat that it’s genuinely like fucking someone."
                "I can’t hold back much longer, this is too good. I'm gonna cum"
                anna "Cum for me, cum for me!"
                "Using both her hands she slides her breasts back and forth against my dick, far faster than she could by moving her entire body, it completely overwhelms my senses and pushes me over the edge."
                "I can’t take another second of her paizuri and start to ejaculate, shooting several thick loads all over her."
                play sound cum
                play sound cum
                show anna paizuricum with cum
                anna "Ahh, ahh… ahh! So-So much!"
                play sound cum
                play sound cum
                show anna paizuricum with cum
                "She keeps her breasts moving back and forth the entire time overall resulting in an explosive and satisfying orgasm."
                stop ambience
                stop music fadeout 10.0
                play ambience ambienceday
                anna "Mmm, I milked you dry, hehe!"
                mc "Your boobs are heavenly, Anna... Alright ladies, gimme a fifteen minute break for my cock to recover, and I'll be all yours again."
                hide anna
                hide honeycrisp
                show anna closesatisfied with dissolve:
                    xpos 600
                    ypos 50
                show honeycrisp closelaughing with dissolve:
                    xpos 0
                    ypos 30
                honeycrisp "Alrighty stud, fifteen minutes. But that's coming outta your pay!"
                honeycrisp "Ehehe, joking!"
                stop music fadeout 5.0
                scene bg black with dissolve
                "..."
                stop ambience fadeout 5.0
                show bg barnblur with dissolve
                "Honey gets on her knees and presents her ass, using the hay bales to hold her up."
                anna "Wait for me!"
                show honeycrispannab threesome
                show honeycrispanna threesome1
                with dissolve
                play music sex1 fadein 60
                "Anna scurries over and mirrors Honey’s pose, leaving me with two amazing asses presenting themselves to me. Their pussies both dripping wet, needy and in heat."
                "With my cock ready to go, I choose to start with Anna since she's the special guest."
                play ambience sex
                show honeycrispanna threesome2
                "I position my cock at her pussy and push forward, easily sinking inside her warm cow pussy."
                "Anna’s whole body reacts with a shiver of pleasure, culminating in a loud moan that escapes her mouth and echoes off the barn walls."
                anna "Aaahhhh, ahh! Finally, mmm..."
                "I can see Honey biting her lip as she watches my cock slide in, her left hand is between her legs, rubbing herself while she watches."
                show honeycrispanna threesome3
                "I fuck Anna, her warm insides tightly squeezing and sucking around my cock with each movement in her wet pussy."
                show honeycrispanna threesome3
                "At the peak of each thrust her pussy contracts around my cock, enhancing the pleasure for both of us."
                "She can't help but fuck me back by rocking her hips up and down, making her thick ass bounce into me."

                "Every time our bodies meet there’s a satisfying thwap that echoes throughout the barn, mixed in with the girls’ moans."
                show honeycrispanna threesome2
                anna "Ahhh, haaahh, your cock is so good [playername]."
                show honeycrispanna threesome3
                "This tight pussy feels amazing right now, at this speed it won't take me long to reach orgasm."

                "Judging by her moans, she's close too, her back is arching and her entire body trembles as her explosive orgasm boils within."

                anna "F-F… F-F-Fuck! C-Coming!"

                "She can barely contain herself, she’s in complete ecstasy as her entire body experiences a powerful orgasm."

                anna "Ahh, k-keep going, I’m… Aahhhhh!"

                "Her moans are reduced to adorable squeaks as her hips buckle and her tongue lulls out lewdly."

                "As before, Anna squirts a little with her orgasm, splattering her lewd juices onto my cock."

                anna "Gosh, so good… D-don’t stop! I want more!"

                "I wasn’t planning on stopping. If anything, I’m going even quicker and harder so I can fill her pussy up with my cum."

                "Tightly grabbing her ass as leverage, I speed up, prepping myself to cum inside."
                anna "Ahh! C-Cum inside me, I want it all!"
                "Her words enthuse me as my orgasm begins to swell up, her pussy feels euphoric right now. "
                anna "It feels so good, I-I’m going to... Again!"
                "Her insides contract around my cock and she squirts again, but all I can concentrate on is fucking. The pleasure is indescribable, I can’t hold on much longer, I’ll cum any second."
                play sound cum
                show honeycrispanna threesome4 with cum
                play sound cum
                show honeycrispanna threesome4 with cum
                "My vision turns white, and my muscles tense up as I ejaculate thick ropes of semen deep into her womb."
                play sound cum
                show honeycrispanna threesome4 with cum
                play sound cum
                show honeycrispanna threesome4 with cum
                anna "Aiiieeee, you’re cumming! Ahhhh…"
                play sound cum
                show honeycrispanna threesome4 with cum
                play sound cum
                show honeycrispanna threesome4 with cum
                "*Splurt, splurt, squirt*."
                honeycrisp "Mmm, damn stud, leave some for me…"
                anna "So much inside me… I have so much of your cum in my belly and womb…"
                show honeycrispanna threesome5 with dissolve
                "I pull out and copious amounts of cum oozes out of her pussy."
                stop ambience
                honeycrisp "Hope y'all didn’t forget about me, I'm paying ya to stick that semen coated cock straight inside me!"
                "I shuffle over to Honey with my erection in hand. Thanks to the aphrodisiac’s effects getting stronger, I’m ready to go immediately."
                "Honey presents her pussy to me by spreading her outer lips out with her fingers. She’s utterly soaked."
                show honeycrispanna threesome6 with dissolve
                "I bring the tip of my cock as it drips with cum to the entrance of her pussy, and as per usual with these intensely aroused girls in heat, it comfortably invites me in with a delightful warmth and tightness."
                "As I penetrate her my shaft becomes fully erect again, this aphrodisiac never fails to impress!"
                honeycrisp "Aaahh! Don’t hold back stud, I want my ancestors to feel this one!"
                play ambience sex
                "My cock slides in all the way, the cum mixing in with her juices creating a messy lubricant the enables me to skip the gentle sex and get straight to the rough fucking that she loves."

                "With each thrust, I pull out the entirety of my shaft and sink it back in as deep as it’ll go."

                honeycrisp "Ahhh… You're pretty good..."

                "The warm insides of Honey's pussy are just as inviting as Anna's, yet as a more toned individual and as a mare instead of a cow, it also feels very different as it squeezes around my shaft."

                honeycrisp "Mmmm, keep going like that, just like that."

                "I kept fucking at this current pace which allowed me to feel all the best parts of her pussy on every nerve of my penis, while not overwhelming and causing me to ejaculate too soon. She on the other hand could easily climax at this speed."

                "Anna was also masturbating whilst she eagerly watched us, cum dripping down her thighs. Not one to miss a single chance of pleasure in our erotic threesomes."

                anna "Don't forget to spank her!"
                show honeycrispanna threesome7 with dissolve
                play sound spank
                "I lift up my dominant hand and markedly bring it down square onto Honey’s tight ass cheek."
                honeycrisp "Oh you two, always ganging up on me, heh."
                play sound spank
                "As I spank again, I could feel her insides briefly squeeze around my cock."
                honeycrisp "Mmphh fuck, it feels good..."
                play sound spank
                "This time I use my other hand, with a raise and a return, I smack Honey’s other ass cheek creating a satisfying slapping sound, even against her soft fur."
                honeycrisp "Oh, ohh! Keep going, I-I'm close!"
                play sound spank
                "As requested by Honey herself, I spank her ass again and she begins to orgasm. Her pussy contracting and squeezing my shaft more and more."
                honeycrisp "Aahhhh, ahhhhh, coming! Mmmm…!"
                "Anna seems to get herself off too, or at least I can see her squirting more. The barn at this point is dense with the thick aroma of sex."

                honeycrisp "Mmph, *Pant*. I swear, I'll get you both back for these spanking shenanigans."

                anna "Don't stop thrustin' [playername]! If you give her a good enough fuck, she'll forget all about getting revenge!"
                "I never stopped fucking her, but I take that as a challenge to speed up."
                "Even though I had two orgasms, I am still incredibly horny. I love fucking these two, so much energy and love."
                honeycrisp "Ahhh, are you close stud? I wanna feel your hot cum inside me."
                play sound spank
                "I spank her again with my other hand, I love the way she gasps and her pussy twitches around my cock, also serving to push me closer to my climax."
                honeycrisp "Ahh… C-Cum inside!"
                "I stop holding back and begin to fuck at the same pace that allowed me to cum in Anna, I can already feel my orgasm brimming."
                "As I’m pumping, I can feel her insides start to tighten and squeeze, she’s coming again! So soon after her first one. I'm going to come too!"
                play sound cum
                show honeycrispanna threesome8 with cum
                play sound cum
                show honeycrispanna threesome8 with cum
                "The sudden tightness of her pussy combined with the speed we’re rutting easily pushes me over the edge and I start to unload inside of her."
                play sound cum
                show honeycrispanna threesome8 with cum
                play sound cum
                show honeycrispanna threesome8 with cum
                honeycrisp "Ahhh! Inside, inside! Mmpphh…"
                play sound cum
                show honeycrispanna threesome8 with cum
                play sound cum
                show honeycrispanna threesome8 with cum
                "As I climax, I continue to thrust into her as I fill up her pussy with my hot cum, enjoying what is perhaps my most satisfying orgasm of the day."
                scene bg black with dissolve
                stop ambience
                stop music fadeout 5.0
                "Most satisfying, however, most tiring, after my third orgasm I close my eyes and fall back onto some hay feeling exhausted."
                show bg farmkitchen with dissolve
                "The three of us clean up and have a jovial lunch."
                "Anna eventually has to return home."
                show bg farm2 with dissolve
                "Honeycrisp and I continue to work around the farm throughout the early afternoon."
                $ monies += 30
                "I work all day and earn 30 monies, a little extra than usual!"
                show bg farmkitchen with dissolve
                show honeycrisp closehappy with dissolve
                "As the evening breaks, I spend some time with Honey in the kitchen."
                play ambience ambiencenight
                stop music fadeout 3.0
                jump honeycrispmenu
            "Visit Blossom" if blossomvisit == 0:
                scene bg farmkitchen with dissolve
                show bg blossombed with dissolve
                $ blossomvisit = 1
                "I go into the farmhouse and visit Blossom, she seems to be lazing around in her bedroom and hasn't left for college yet. I should have an hour to talk or play with her."
                jump blossomvisit
            "Back to the Worldmap":
                if fr == 1:
                    jump prefinalworldmap
                jump preworldmap
    label annavisit:
        "I nod and bid farewell to Honey as I walk past the farm and into the mountains to visit Anna."
        if cowvillagevisit == 0:
            $ cowvillagevisit = 1
            scene bg farm2 with dissolve
            "This gives me an opportunity to take in the beautiful Arcadian countryside, the rolling grasslands, the bright colourful flowers, everything is so saturated and pretty in comparison to my world."
            "In the distance in most directions are towering mountains clinging to the horizon, no matter how far I walk they never seem to get any closer."
            "As I walk down the path, I cross paths with a familiar cow girl. This is the girl that has recently started to work at Honeycrisp’s farm. We exchange greetings and she assures me that I’m heading the right way."
            "The plains of grass at some point are drowned out by a forest of trees, within the trees, I start to see some structures."
            scene bg cowfarm with dissolve
            "I’m already an oddity in Arcadia as mares would stare at me, it’s no different here as the cows peek at me, confused."
            "Anna’s farm is at the other end of the village, thankfully it’s a small settlement so I don’t have to bear the awkward glare of the locals for too long."
            "I enter through the gate of the only farm like location, and an instantly recognizable face jogs my way."
            show anna laughing with dissolve
            anna "Heyyy, [playername], you actually came to work? Oh my gosh, this is so cool!"
            show anna happy with dissolve
            anna "I can’t believe you came to see me, I’m not even a pony or anything, I’m so honored ahah."
            mc "How could I refuse an invitation? I'm here to work and spend some time with you."
            anna "Heh, perfect, I have some jobs we can work on together and then we can have some fun later."
            anna "We don’t really need to work hard, crops only grow so fast! Hehe."
            anna "Oh! I know what you can do, you can do something very special for me."
            mc "What's that?"
            anna "If you recall, this is the heifer village, it’s twinned with another village, the cow village. Those aren’t the actual names, but that doesn’t really matter right now."
            anna "During mating season minotaurs come down from the mountains, visit the cow village and mate with the cows in heat."
            anna "If you don’t want to breed you stay in the heifer village, however, this creates a difficult situation for when we want to trade supplies during mating season."
            "Images of a perpetual cow orgy fill my mind; didn’t Anna say a minotaur and a cow could go for hours?"
            mc "So, what’s stopping you going? Surely you can just avoid sex and trade supplies quickly?"
            anna "A girl from here tried that, she came back hours later than she was supposed to, ended up having sex the entire time. She wasn’t forced, just couldn’t help herself."
            anna "If I were to go to the cow village while minotaurs are visiting I doubt I could help myself, some of the ladies here say the smell of their sex is enough to make you swoon and lose your mind."
            anna "You see sparks in your eyes, before you know it, you’re on your knees, or spreading your legs, getting pounded."
            mc "Sparks? Like hypnosis or magic?"
            anna "You know how when a mare or a cow is in heat, they release pheromones?"
            mc "I sure have, they even work on me, they’re probably working on me right now. It’s like a sweet smell, it makes me feel warm inside, and it gets the blood going."
            anna "Yeah, minotaurs have pheromones like that too, but far more powerful."
            anna "If you were a minotaur right now, we’d probably be having sex, I don’t know, I’ve never actually done it with a minotaur. But to be honest, I kinda want sex with you right now anyway."
            show anna neutral with dissolve
            anna "It kinda makes my skin crawl, the fact my natural instincts and primal reaction to those pheromones will cause me to do something I otherwise wouldn’t want to."
            anna "Makes me feel like I'm not in control of my own body. What a nightmare."
            mc "Okay, so you need me to do a few deliveries?"
            show anna happy with dissolve
            anna "Yeah, usually we have a cow from the other village come and collect some things. But they're late."
            anna "So I'll need you to do a delivery in a lightweight wagon, just like we did with the barrels back at Honey's place."
            anna "Oh, also I want you to bring some things back. I have a list here for you just in case, but the girls on the other end already know what to do."
            mc "I’m kinda nervous, what if I meet a minotaur? Are they territorial?"
            anna "They’ll almost certainly ignore you. They’re not particularly social, and they’re only aggressive when it comes to mating with cows."
            "It’s extraordinary how each species in this world has their own culture surrounding their biology."
            anna "If one does talk to you, they'll just treat you like a normal person, an equal. Don't worry about it."
            mc "Alright then, I’ll do it. Where am I being sent off to?"
            anna "Ah yeah, there was a map with the list, the location of this village is somewhat secret to prevent nosy minotaurs, but it should be pretty clear where to go."
            "This map is extremely clear. There’s no way this was drawn, it must be the result of satellite imaging, although it's not too surprising that this kind of technology exists in this world."
            mc "Sweet, you got a deal Anna. This kind of job is perfect for me and I’m more than happy to help you out."
            anna "The wagon is already setup outside, come back soon darling, and I’ll show you just how much I appreciate your hard work."
            "She flirtatiously bends at the waist, accentuating her deliciously round bubble butt, along with the fact she’s completely nude, I can even see her pussy which she seems all too aware of."
            anna "I’ll let you play with it, hehe."
            scene bg farm2 with dissolve
            stop music fadeout 3.0
            "I take the wagon and wheel it off before my half-chub turns into a full erection. Following the map, it takes about thirty minutes to haul the wagon all the way to the twinned cow village."
            "This is honestly quite exhausting, and for awhile there have been no trees to shade my nude figure from the heat, I’m just glad I don’t get sunburn for whatever reason in this world."
            "As tiring as this is, this is paid work so it’s a lot easier to suck it up and get on with it."
            scene bg cowfarm2 with dissolve
            "Eventually, after an agonising hour of pulling this cart, I arrive at the cow village on the map."
            "The map has a certain building circled, so I pull the wagon along to that specific building, skirting around the town rather than going through it to avoid embarrassment."
            "While it is unusually quiet, I do spot a few residents milling around, running shops. I can't even see any minotaurs."
            "I pull up to a storage area that has a few parked wagons and boxes of various goods. There’s no one around though, I just noticed that this particular area of the village is really quiet."
            "I listen really closely, and… It’s actually not as quiet as I initially thought."
            "Along with the chirpings of resident birds, I can only just hear giddy feminine moans and giggling."
            scene cow threesome with dissolve
            play music sex1 fadein 3.0
            "I peak into the window of the storage shack and… I’m not surprised actually; I’d fully prepared myself to see something like this."
            "There’s not one, but two cow girls having sex with a minotaur."
            "Honestly I expected the minotaur to be bigger, but he’s around the same size as me. Sure, taller than the cow girls, but thankfully not the 8ft big dick towers I imagined."
            "The minotaur plows into one of the cowgirls doggy style, while the other waits next to her. Similar to the way I had a threesome with Honey and Anna actually."
            "Are those the girls I'm supposed to be working with?"
            "They must be having a lunch break, heh."
            "Power to ya Mr. Minotaur, I won’t interrupt."
            stop music fadeout 3.0
            scene bg cowfarm2 with dissolve
            "Guess I'll do this myself, I return to the wagon and take a look at my list; glad I have this. I unpack the relevant resources and repack the ones on the list."
            "I’m sure no one would mind if I just did the job and vanished, it’s not like there’s anyone around watching me."
            scene cow threesome with dissolve
            "With the wagon restocked I take one last peek through the window, I can’t resist."
            "They just keep going, in a erotic sex-filled delirium."
            "It looks fun, if I’m still here the next time Anna needs milking, I’ll have to try that one with Honey. For now, I really want to sleep with Anna."
            scene bg farm2 with dissolve
            "With map in hand, I wheel the wagon all the way back to the heifer village."
            scene bg cowfarm with dissolve
            "When I return I find Anna is sat on a wall reading a book while she waits for me."
            show anna happy with dissolve
            anna "Ahh, there you are, thought I’d catch up with some reading while I wait."
            "She waves around a business novel, '7 Habits of Highly Effective Mares', honestly I think I’ve read my world’s version of that book."
            mc "You were waiting?"
            show anna laughing with dissolve
            anna "It was more my impatience, I couldn’t stop thinking about you, hehe."
            show anna happy with dissolve
            anna "Here, let me take that wagon."
            "She takes the wagon and wheels it with finesse over to an employee of hers who takes it to a barn."
            show bg annahouse with dissolve
            "We go back to Anna’s farmhouse where she pays me 30 monies!"
            mc "Wow, that's even more than Honey pays me."
            anna "Well [playername], you did a very high paying job just now. A job no one else in this village could have done as quickly and cleanly."
            anna "If you came here every day, that'd be lucrative to me, so I have no choice but to pay you more than the competition, right? Hehehe."
            anna "I also offer other benefits with my employment... Come with me."
            $ monies += 30
            scene bg annabedroom with dissolve
            show anna closehappy with dissolve
            "She leads me to a cute bedroom with a double bed."
            "Anna sits on the edge of her bed and invites me to sit beside her with a pat."
            anna "What was it like at the other village, everything go smoothly?"
            mc "Yeah, I did actually spy a glimpse of a minotaur fucking the two girls that were supposed to meet me there. Other than that, in and out without a fuss."
            anna "I can’t believe you were peeking!"
            anna "Wanna show me exactly how they did it? Ehehe!"
            jump annamenu
        scene bg cowvillage with dissolve
        show anna happy with dissolve
        anna "Nice to see ya [playername], let's get to work so the play tonight's even better!"
        "I work at Anna's farm and earn 30 monies!"
        scene bg annahouse with dissolve
        show anna closehappy with dissolve
        "Eventually Anna brings me to her house."
        $ monies += 30
        menu annamenu:
            "Talk" if annatalks == 0:
                jump annatalk
            "Sex":
                jump annasex
            "Leave":
                "I thank Anna for the day and return home before it gets too late."
                jump evening
        label annatalk:
            stop ambience fadeout 10.0
            menu:
                "You quite like interspecies men, don't you?":
                    anna "I'm so glad I got to meet you!"
                    anna "I adore interspecies men, they're so exotic and interesting compared to those rough 'taurs."
                    mc "Trust me when I say I feel exactly the same way."
                    mc "Being able to meet all these cows, mares, and maybe more has been some of the most fun I've ever had."
                    anna "Hah, well of course all the lovely ladies are exceptional."
                    mc "Speaking of loving ladies, you and Honeycrisp have an erotic relationship right?"
                    anna "Ohh yeah, I think I told you that once. It's only some fun between friends."
                    show anna closelaughing with dissolve
                    anna "She is really good with a strap-on, ehehe."
                    mc "I'd say that's a little more than just friends."
                    show anna closehappy with dissolve
                    anna "Heh, maybe! I'd do this with any close friends though, it's fun sharing in pleasure."
                    anna "You may have noticed this is a female only village, and the ladies know how to have a good time, ahaha."
                    anna "Speaking of a good time, a lady like me needs a man too..."
                "Ask her about her business mindset":
                    mc "So you're a real ambitious type I take it?"
                    show anna closelaughing with dissolve
                    anna "Mmm definitely! I'm working hard, I built and now own this entire farm myself."
                    show anna closehappy with dissolve
                    anna "Before me, the heifer village only had imports, now both villages have farms."
                    mc "That's certainly remarkable for someone your age, what's the plan?"
                    anna "Ohh, well... I just paid off my debts for building supplies, funds are low right now but the future looks bright."
                    anna "I want to expand my house, my business and invest into the heifer village."
                    anna "I haven't told anyone yet, but I'm planning on living here forever, no kids for me!"
                    mc "I got that impression, and I respect it. Looks like I'm doing the same."
                    anna "Ohh, of course you are Mr. Hooman."
                    anna "You know, I thought I never wanted a partner too, but after meeting you I changed my mind."
                    anna "I want a cute interspecies boyfriend, not picky as long as they're ambitious and fun."
                    mc "That sounds healthy, I think I'd go a bit crazy if I was alone for a few decades."
                    anna "And I can't keep this pillowy ass to myself, I need to share it."
                    anna "How about it 'stud', want some tail?"
                "What are your parents like?":
                    mc "What are your parents like?"
                    anna "Hard to say friend, as a cow you're never quite sure who your father is."
                    mc "Isn't that an incest problem?"
                    anna "Nah, nah... Uhm, I hope not."
                    anna "Anyway, my mother used to live here in the heifer village with me."
                    anna "When a girl is born, she's brought here where she's raised and educated."
                    anna "When a male is born, they're taken to the mountains where he's raised and educated."
                    anna "And when everyone comes of age and they're ready, they'll return to the cow village."
                    anna "Momma went back to the cow village, I wonder if she'll get pregnant again."
                    mc "Ohh, I should have asked you if you have any siblings."
                    anna "I dooo, I have a brother. Couldn't tell you much more than that. Not even his name."
                    mc "Feels pretty lonely having the men and women separated in such a way."
                    anna "Yeah perhaps, but from our perspective it's always been like that."
                    mc "What if hypothetically you went back to the cow village, ready to breed, and you met your brother?"
                    show anna closeneutral with dissolve
                    anna "Ohh, uh..."
                    mc "What about if you met your father?"
                    anna "Uuuhhhhhmmmm..."
                    mc "Awkward..."
                    "She's blushing so much at the strange and conflicting thoughts that I feel bad for even bringing it up."
                    show anna closehappy with dissolve
                    anna "See? This is why I stick to cute interspecies men like you."
                "Back":
                    jump annamenu
            $ annatalks = 1
            jump annamenu
        label annasex:
            menu:
                "Paizuri":
                    hide anna with dissolve
                    stop music fadeout 3.0
                    show bg annabedroom with dissolve
                    show annahandjob with dissolve:
                        xalign 0.5
                        yalign 0
                    "She immediately begins by wrapping her hand around my cock and building me up to an erection."
                    "It's rather apparent that she's eager to begin, Anna's always horny after all."
                    "It doesn't take long for watery precum to start dribbling from my cock causing Anna's eyes to light up."
                    play music sex1
                    anna "I think you're ready, big boy."
                    hide annahandjob with dissolve
                    show anna boobs with dissolve
                    "The cow girl lifts herself up slightly and coos as she squeezes her tits together in-front of me."
                    show anna paizuri with dissolve
                    "Anna lifts herself up slightly and clamps her breasts around my cock."
                    "She giggles and pushes her breasts together even more, completely squishing my shaft with a soft tightness."
                    play ambience sex fadein 2.0
                    "As soon as my cock has disappeared under her pillowy cleavage, she begins to lift her chest up and down, and at quite the pace."
                    "At the speed she's going each thrust of her underboob hits my body with a slap causing her breasts to quake at the impact."
                    "She's really not holding back, she's completely absorbed in her work as she thrusts herself backwards and forwards, putting her whole body into the titjob."
                    anna "It's good, yeah? Your face is telling me that much, hehe..."
                    "She giggles as she drools a little onto the tip of my cock, her saliva dripping down and serving as lubrication."
                    "With a little more drool, her breasts start to feel moist and wet like the insides of a pussy. It's incredibly arousing and stimulating."
                    "She's enjoying herself too, she's moaning not from pleasure, but from the pure erotic joy she's elicting from the lewd act."
                    "No doubt her breasts are somewhat sensitive too. I bring my fingers to her nipples to tease and squeeze, causing her to bite her lips and give me sensual bedroom eyes."
                    "She's moaning quite a lot actually, could she really get off from this? And before even I get off?"
                    "I play with both her nipples with that question in mind, fondling and teasing them causing her back to arch with pleasure and her eyes to almost roll back."
                    anna "Mmmphh, mmm, hahh... Don't stop, ahhh..."
                    "She speeds up, and her hips start to gyrate as her body quivers with erratic sparks of energy."
                    "If she keeps going this fast, I'm gonna cum any second!"
                    anna "Aahhh, ahhh- I-I'm gonna..."
                    "She's coming, she's really coming from this! And as she persists in sliding my cock back and forth between her breasts, it won't take long for me to join her too."
                    play sound cum
                    play sound cum
                    show anna paizuricum with cum
                    "I feel a tension as my shaft throbs  and a large load of cum spills from the depths of Anna's cleavage and over the tops of her breasts, her hair, her face, everything."
                    anna "Ahh, ahh… ahh! So-So much!"
                    play sound cum
                    play sound cum
                    show anna paizuricum with cum
                    "She keeps her breasts moving back and forth the entire time we both orgasm, until she's finally emptied my balls and she's left plastered in cum."
                    stop ambience
                    "She laughs as she licks up some of the cum from her fingers but ultimately realizes she can't lick all of this up herself."
                    stop music fadeout 5.0
                    anna "Mmm, I like it messy, but this might require a shower! Hehe"
                    hide anna with dissolve
                    "As much as we'd love to cuddle before we go our separate ways, Anna and I agree that it's best if she goes and showers now."
                    "I say goodbye as I give her a quick kiss on the cheek that doesn't have cum on it, and she returns the gesture by kissing me straight on the lips."
                    scene bg black with dissolve
                    "..."
                    jump evening
                "Doggystyle":
                    show bg annabedroom with dissolve
                    show anna horny with dissolve
                    anna "My heat is bad this year, I keep having wet dreams where I get ravished and fucked over and over… I want it so bad…"
                    "She leans against me meekly, one of her hands brings itself to my flaccid penis and starts to jerk it, getting the blood flowing as it rapidly stiffens."
                    anna "I know it’s a little selfish… But can you?"
                    "Her hand speeds up, I’m almost fully erect now, and her seductive whispers only excite me more."
                    mc "I’ll do it, I’ll fuck that heat of yours into the next decade if I have to."
                    anna "Oohh… This is it, I finally have you all to myself. Last time in the barn was good, but it left me wanting more of you, babe."
                    anna "Here, this position should make use of my best asset."
                    play music sex1 fadein 2.0
                    show anna doggystyle1 with dissolve
                    "She gets on all fours, face to pillow, and ass presented towards me. I get a good look at her inviting pussy again, it’s even wetter and messier than a mare’s."
                    "As I look at her vulva and get into position, there’s something primal within me that prevents me from holding back, something subconscious telling me that I need to fuck her right now."
                    anna "Don’t worry about me sugar, just go crazy… I know I will!"
                    play sound cum
                    show anna doggystyle2 with dissolve
                    "With my hand, I guide my tip to her wet entrance, and I waste no time sinking deep inside her."
                    "She gasps and shudders with pleasure in response, I can’t help but grind my teeth as pleasure surges through me."
                    anna "Yeaahh… That’s it, I can’t get over how good this feels… Hahh…"
                    play ambience sex fadein 2.0
                    "I bring my hands to her hips and start to fuck her slowly with long, deep thrusts that hit every nerve ending inside her."
                    "At the peak of each thrust Anna reacts favourably as she muffles a moan into her pillow, it seems like she has some especially sensitive areas deep inside her."
                    "I go balls deep and gyrate my hips with shallow pumps instead, focusing on these deep pleasure points, this clearly excites her, causing her breathing to become more ragged."
                    anna "Mmmphh… You’re so deep… Hahh… I love that, keep going…"
                    "I cling onto her hips tightly and pull her close. While I grind my cock against her insides, she arches her back and moans out."
                    anna "Mmmm, I-I can’t even think… Mmmmpphh…"
                    "She looks back with a hot, hazy, seductive expression, pure wanton lust. I can tell that she’s loving every moment."
                    "While gyrating my hips, her pussy does feel incredibly pleasant, it’s so tight it almost feels like I’m being sucked by her insides, there’s also an alluring warmth that sends tingles throughout my body."
                    "But I won’t be able to cum without thrusting, so I accompany the deep sensual movements with just that."
                    "I start slow at first with deep thrusts like before, and gradually speed up my pace."
                    "She has such a fat ass causing a naughty slapping sound with each thrust, accompanied by the wet sound of my cock sliding in and out of her."
                    anna "Yess… Faster [playername], mmmm… *Pant, pant*"
                    "My cock throbs and my muscles tense a little. I speed up even more, causing the entire mattress to rock beneath us. The sheets becoming dishevelled as Anna grasps tightly onto them."
                    "This speed combined with the intense dripping wetness of a cow girl makes for an incredible squelching sound."
                    "Not to mention her constant moans, all the stimulation to my senses excites and arouses me."
                    anna "Ohmygoshh… *Pant* Mmmm, really close!"
                    "As a cow girl she seems to have far more strength and endurance than I do, and she doesn’t shy away from showing that, as she gets closer to orgasm, she starts to bounce her ass and hips back against me."
                    anna "Mmmphh… Mmmmm *Pant* Yess…"
                    "At first she moved back in rhythm with my thrusts moving forward, however she started speeding up, quickly outpacing me and soon completely overpowering my thrusts, leaving me to just kneel and witness her pound against my cock."
                    anna "Faahhh… I’m cominggg, ahhh…!"
                    "I’d actually forgotten that Anna squirts as haphazard gushes of juice flow out of her urethra at random bursts, dousing both me and the bed."
                    "The pleasure is overwhelming, I can feel her starting to climax, her pussy tightening around my shaft, taking me from just being close to… I-I can’t hold back, I can feel my orgasm rapidly welling up, it feels too good."
                    play sound cum
                    show anna doggystyle3 with dissolve
                    play sound cum
                    show anna doggystyle3 with dissolve
                    "She keeps pumping up and down against my cock as I ejaculate inside of her, unloading thick hot globs of cum inside of needy pussy."
                    play sound cum
                    show anna doggystyle3 with dissolve
                    play sound cum
                    show anna doggystyle3 with dissolve
                    anna "Ahhhhh, aaaahhhh… *Pant* yess, mmm… all your sperm… deep inside me… just like my heat wanted…"
                    "Blowing my load inside her only serves to excite her even more, my vision and thoughts are cloudy due to the powerful climax but I’m sure she speeds up and squirts again."
                    stop ambience fadeout 3.0
                    "Thankfully as I soften and grow more sensitive, Anna does slow down, although judging by the lustful glow in her eyes, she’s not quite satisfied yet…"
                    show anna satisfied with dissolve
                    anna "Mm… That was really great for the first one, I can’t believe how good that felt."
                    mc "First… Right… How many times are you planning on going?"
                    show anna horny with dissolve
                    anna "Hehe, we won’t fuck my heat into next week with just one go."
                    "She spreads her pussy, some of my cum drizzles out and slides down her thigh."
                    mc "It’ll take my cock a while to get erect and ready again. Although I’d be happy to do it a second time or maybe even a third time."
                    show anna boobs2 with dissolve
                    anna "Come here babe… Suckle my nipple, maybe that’ll help you."
                    "Milk? I’ve messed with it before… Guess it couldn’t hurt."
                    mc "Sure…"
                    show anna milking2 with dissolve
                    "She turns around and sits down, perking up a breast and playfully bouncing it up and down expectantly."
                    anna "It hasn’t been long enough to produce a lot, but it’ll be enough for you."
                    show annahandjob with dissolve:
                        xpos 776
                        ypos 0
                    "With a somewhat fatigued mind I lean in and start suckling, I can feel Anna’s hand move itself between my legs and start to gently jack off my half-erection."
                    scene bg annabedroom
                    show anna doggystyle3 with dissolve
                    stop music fadeout 3.0
                    "With a hit of perhaps too much milk, more than I think I’ve had before, me and Anna fuck, then we fuck again, then we fucked again."
                    play sound transition1
                    scene bg white with s
                    "It’s fortunate that Anna had so much strength and stamina, she took a lot of the burden I’d otherwise experience with what amounted to a six hour session of sex."
                    scene anna doggystyle4 with s
                    "Honestly, it’s a blur, I think I had too much milk."
                    show bg annabedroom
                    hide anna
                    show anna satisfied
                    with dissolve
                    "About six hours later, it’s evening and the sun has nearly set. Even Anna seems a little tired, she put all the work in for that last ejaculation."
                    "She was covered in so much cum it was nearly comical. My balls genuinely ache a little after the aphrodisiac finally wears off."
                    "This is like the Blossom situation all over again..."
                    anna "*Pant, pant* You know… I think…"
                    mc "Hmm?"
                    show anna smug with dissolve
                    anna "I’m not horny anymore… Hah… ahaha… My heat, I can’t feel it at all."
                    "My ears perk up, thankfully I’m not so exhausted I can’t move, I still have to walk home after all."
                    mc "Really? That’s great news."
                    anna "Yeah… Usually there’s this tingling inbetween my legs all the time during heat, but it’s gone!"
                    anna "I think we really did fuck it until next week."
                    anna "Anyway, I guess I gotta clean you up a bit before you head off, and I feel like showing my gratitude by doing it the good ol’ way."
                    show anna closesatisfied with dissolve
                    "She lazily shuffles towards my pelvis and uses her large wet cow tongue to lick off all the semen, rather efficiently too."
                    "I’d tell her that’s not necessary, but honestly at this point she can do whatever she wants."
                    anna "Mmm… *Lick*… *Slurp*, it’s a good thing you don’t have sex fuelling cum like those minotaurs… Else we’d probably be going for another six hours."
                    anna "You remember those two cow girls you saw from earlier right? I bet they’re still going."
                    mc "Gosh, that’s crazy… I wish I had that kind of stamina."
                    anna "*Liiiiick*… Mmm… It’s a good thing we can take turns to give each other a break."
                    mc "Ah yeah, true, honestly I’m surprised I’m not sorer."
                    show anna closehappy with dissolve
                    anna "Hehe, you might be sore in the morning, milk is supposed to boost your physical attributes too."
                    mc "Is that so? In that case I best walk back as soon as I can before I collapse or something."
                    show anna closeneutral with dissolve
                    anna "Don’t say something like that stupid, you’ll worry me."
                    anna "You should head back before it gets dark though."
                    mc "Yeah, I'd probably only just make it before the crickets chirp. I should probably leave now."
                    anna "Ohh, yeah. That would be for the best."
                    "She bounces towards me, hugs and kisses me."
                    anna "Oohh, my legs are like jello. That tired me out a lot too."
                    mc "Go have a nice bath, you deserve it, chill out this evening, no more heat to bother you."
                    anna "Mmm, I’m looking forward to it! I’ll be able to read a book tonight without getting distracted."
                    mc "Haha, alright, thanks for today Anna, hope to see you again."
                    anna "See you, oh, and your pay is on the counter in the kitchen."
                    mc "Got it!"
                    "I collect my pay, then I head out, racing my way back to Arcadia, racing the sun before it sets."
                    jump evening
                "Back":
                    jump annamenu
    label farmsexduringwork:
        "During work…"
        "You found a secret scene! Requirements met: Work with Honeycrisp after her arm is out of a cast. 50%% chance."

        show honeycrisp nchappy with d
        honeycrisp "Phew, another tree down. Fancy a quick apple break?"
        mc "Yeah, it’s pretty hot today."
        scene honeycrispb outside
        show honeycrisp outside1
        with d
        "I stretch out and sit down on the grass beside the fence. Looking up I realize I accidentally gave myself a good view of Honey’s rear."
        honeycrisp "Psshh, you sat there on purpose. I know your game, sugar."
        "Honey laughs to herself and teasingly flicks her tail upwards."
        mc "I could have sat anywhere and gotten a great view of you, Honeycrisp."
        mc "Your back is especially nice though, very well-defined muscles."
        honeycrisp "Heh, just my back? Betcha oogling more than just that."
        mc "You certainly have other assets I can appreciate from down here. But do you just want idle compliments, or something more?"
        honeycrisp "You certainly are being a naughty stud today. I tell ya what, how about a quickie? Don’t even need ta worry about my own orgasm, just fill ‘er up with cum."
        mc "Now that is an offer I don’t think I can refuse."
        play music sex1 fadeout 25.0
        "Standing up behind Honeycrisp, I bring one hand to her hips to hold her steady on the fence. My other hand slips under her ass and starts to rub between her plump labia."
        mc "You’re already a little wet…"
        honeycrisp "Tell ya the truth, I always get a bit horny around you, stud."
        honeycrisp "Somethin’ about seeing that delicious cock in the corner of my eye all day."
        "I rub her clit gently to prepare her pussy. She soon gets wetter and wetter, her pussy blooming as the blood starts flowing."
        "Slipping a single finger inside, it easily sinks up to my knuckle. She readily accepts a second finger too, albeit with slightly more resistance."
        "Honeycrisp turns her body slightly. Taking advantage I bring our lips together and we kiss. The hand I had on her hip moves upwards to her breast, and I begin kneading my fingers into the soft fur."
        "Our tongues lovingly twirl around each other’s mouths while my fingers grind back and forth."
        "She’s getting really wet now, and I’m fully erect, my cock pressing against her butt slightly and twitching."
        honeycrisp "Mmmpphh, go on stud, fill ‘er up."
        "She flashes a thumbs up while giving her ass a little wiggle."
        mc "You got it, boss."
        "Making my move, I start by grabbing her ass while guiding my cock towards her wet and awaiting pussy."
        play sound cum
        show honeycrisp outside2 with d
        "I push inside and slide deep into her inviting warmth, each inch of my member pleasantly squeezed."
        "The mare moans pleasantly as she’s taken to the hilt, holding on carefully to the fence with her feet and left hand."
        play ambience sex fadein 3.0
        "I grit my teeth in response to the sharp pleasures, beginning to fuck at an appropriate pace for a ‘quickie’. Fast and deep."
        "Honeycrisp handles the unusual position like a pro, remaining steadfast on the fence while taking a hell of a ploughing. She even takes a bite out of her apple between moans."
        "She isn’t entirely ignorant to the pleasure though, as her body soon heats up. First her back arches slightly, and secondly the moans grow in intensity and volume."
        honeycrisp "Ahhh, ohhh… I wish we could do this all day, stud.  *Pant*"
        "Essentially, we’re rutting at a pace that’d usually bring either one of us over the edge, but it’s so early in our rutting that those orgasmic feelings haven’t had the chance to culminate yet."
        "Needless to say, it’s still just as pleasurable. Honeycrisp’s face contorts with lust, her hands gripping so tightly into the wood that it may leave a mark."
        "My member pounds her over and over, going from the base to completely filling her. Splattering her juices with a squelch, and that noise is joined by a slapping sound at the peak of each thrust."
        "From this position she can’t exert any effort into the rutting, so it’s up to me to finish what I started."
        "Determined, I fuck her just fast enough to feel a slow rise of orgasmic pleasure stir deep within me. Perhaps overexerting myself as I try to force that feeling out."
        honeycrisp "Oohh, gosh… Cum in me, stud! Make me yours!"
        play sound cum
        show honeycrisp outside3 with cum
        play sound cum
        show honeycrisp outside3 with cum
        "Pushing as hard as I can to the edge. I manage to finally achieve climax, spraying several loads deep inside."
        play sound cum
        show honeycrisp outside3 with cum
        play sound cum
        show honeycrisp outside3 with cum
        "I continue humping throughout my orgasm with the same passion. It feels blissful."
        stop ambience
        stop music
        play sound movement
        scene bg farm2 with hpunch
        "Oh-?!"
        "Honeycrisp almost falls forward flat onto her face, but actually manages to catch herself with her hands."
        play ambience ambienceday fadein 5.0
        honeycrisp "Oohh, ahhh… Ahahahah."
        "It takes me a while to realize she had orgasmed, causing her to lose grip and fall off."
        "Swinging myself over the fence, half-flaccid dick in tow, I move to make sure she’s okay."
        show honeycrisp nclaughing with d:
            xalign 0 ypos 700
            linear 3.0 ypos 400
        honeycrisp "I-I’m good, just couldn’t handle my orgasm, hah."
        "Hmm... This reminds me of that one time Blossom got a cramp. I hope this doesn't awaken anything within me."
        mc "I’m surprised you had one so quickly!"
        show honeycrisp nchappy with d:
            linear 3.0 ypos 30
        honeycrisp "I’ll put that up to your expert treatment of my pussy. The way you warmed me up at the start really set me up to get the most out of that rutting."
        mc "Always the best from me. I think we overdid it. Well… I overdid it."
        honeycrisp "Y'all can never overdo it with me, sugar. Us farm girls are tough. Now, how about we go inside and have a proper break? I could use a drink."
        scene bg black with dissolve
        if crystalballactivated == 1:
            jump cbmenu
        $ secretsunlocked += 1
        "Much later on..."
        show bg farmkitchen
        show honeycrisp closehappy
        with dissolve
        "As the afternoon lulls on, I spend some time with Honey which eventually leads us into the kitchen."
        play ambience ambiencenight
        stop music fadeout 3.0
        jump honeycrispmenu
