label library:
    $ libraryvisits += 1
    if libraryvisits == 1:
        $ monies += 25
        $ libraryvisit1 = 1
        jump libraryvisit1
    elif libraryvisits == 2:
        $ monies += 25
        $ libraryvisit2 = 1
        jump libraryvisit2
    elif libraryvisits == 3:
        $ libraryvisit3 = 1
        jump libraryvisit3
    else:
        jump librarymenu
    label libraryvisit1:
        stop music fadeout 10.0
        "The library will be a nice place to work, I already know someone that works there after all."
        "It might even give me the opportunity to learn more about that sciency stuff Penelope was talking about."
        "Maybe I can borrow a good book too, reading will be a good source of information to learn about this new world."
        show bg tree1 with dissolve
        "I walk to the tree library and as I go to let myself in, the door appears to be locked."
        show bg tree2 with dissolve
        "Ah, it's before 9:00am, so the library is closed. I can't even get in to tell Penelope I'm here."
        "I knock on the door, but I get no response."
        "This is somewhat concerning; the library is huge so it’s unlikely anyone would hear me."
        "Just as I’m about to knock on the door again, I hear an unknown voice from a window above."
        show bg tree1 with dissolve
        unknown "Who are you?"
        "I look up and see a purple pony peeking from a window, that must be Lily, right?"
        mc "I’m here to work, Penelope referred me."
        unknown "Alright... I’ll open the door, let yourself in."
        "Rather than come down and actually open the door, she unlocks, and opens it with a spell."
        show bg library with dissolve
        "And when I step in, the door closes and locks itself behind me. Impressive! I don't think Moxie can do that."
        "I walk to the reception and have a look around the massive building in awe, there must be tens of thousands of books in here."
        unknown "Hello, new person..."
        show lilyb
        show lily neutral
        with dissolve
        play music lily
        "Catching me off guard, a quiet unicorn is behind me. The purple mare from the window."
        show lily happy with dissolve
        unknown "You must be [playername], that new 'human' creature Penny mentioned."
        mc "Yes! Hello, it's nice to meet you. You are Lily I believe?"
        lily "Quite right. I've heard about your incident. I'm no stranger to Moxie causing trouble, but this is a strange situation indeed!"
        show lily laughing with dissolve
        lily "I'd love to help you. I'm glad you've finally decided to seek me out."
        "She extends her arm and invites me to shake hands, I do so. It feels unusually formal all things considered."
        show lily neutral with dissolve
        lily "Hmm, your skin feels strange... I wish to learn more about your biology if possible."
        "Ah, so the handshake was just a ploy so she could feel my skin."
        show lily happy with dissolve
        lily "You're here because you want to learn more about this world, and how you got here, right?"
        mc "Actually, I came to work, but I’ll happily kill two birds."
        show lily sad with dissolve
        lily "Kill birds? Unfortunately the library doesn't open to the public until 10:00am."
        mc "Looks like I have time then, where do we begin?"
        show lily laughing with dissolve
        lily "Personally I have a great interest in studying you, I’ve always been fascinated by new creatures, and potential aliens! I want to know everything I can about you."
        "Aliens? I guess I'm technically an alien since I'm from another world."
        show lily happy with dissolve
        lily "I wanna know where you live, how you operate, how you tick."
        mc "Slightly odd phrasing, but I’m more or less open to the idea."
        lily "Perfect. Let's go to my room upstairs, I wasn't expecting any visitors, so don't mind the mess."
        mc "Lead the way."
        scene bg black with dissolve
        pause 0.5
        show bg libraryupstairs with dissolve
        "The two of us head upstairs. First there’s a normal hallway with various typical rooms on the sides, each door has a sign: ‘Penelope', 'bathroom', 'kitchen'."
        "At the end of the hallway there’s something quite remarkable, it’s a strange laboratory-library hybrid simply labelled 'lab'."
        "Peering through the window I can see various pieces of scientific equipment. I can see a fume-cupboard, a rotary evaporator and a HPLC machine."
        show bg dusklightbedroom with dissolve
        "We don’t enter that room yet though, instead she takes a right at the open door and into a messy bedroom labelled 'Lily'."
        show lilyb
        show lily happy
        with dissolve
        lily "Get comfy for a moment [playername], I’ll make you a drink. Would you like tea, or juice?"
        mc "I think I had peppermint tea last time I was here, could I have that please?"
        show lily laughing with dissolve
        lily "Of course you can. I’ll be right back."
        hide lily
        hide lilyb
        with dissolve
        "Now she’s gone; I take a moment to properly analyse just how messy this room is. Even with the lack of clothes, somehow this room is still laden with papers, books."
        "There’s even a dildo just laying upright on her bedside counter. Personally I’d hide something like that before inviting someone to my room, but power to her, I guess."
        "Wait, is it moist or am I imagining it?"
        show lilyb
        show lily laughing
        with dissolve
        "Almost catching me staring at her dildo, Lily returns with drinks."
        show lilyb close
        show lily closehappy
        with dissolve
        "We sit next to each other on the bed, introduce each other and have a relaxing discussion."
        "She seems like a cool person, she does a lot of exceptional things, yet remains remarkably humble."
        "She tells me that she’s an ambassador between the main city and the suburbs, she tries to ensure good relations between the people."
        "Meaning she deals with a few problems around the area, I guess I’m one of those problems now."
        mc "That must be a huge responsibility for you."
        show lily closeshy with dissolve
        lily "It can be somewhat of a burden, I'm quite introverted so it can be especially exhausting for me."
        lily "I used to prefer books over people and I got told off by my teacher, heh..."
        lily "That's why she made me the ambassasdor, now I have no choice but to socialise."
        show lily closesad with dissolve
        lily "I always thought practice makes perfect, and I thought I'd improve, just like studying! But for me, it never gets any easier..."
        mc "I must admit, I wouldn't have assumed you were bad at socialising, you're doing a great job talking to me."
        show lily closehappy with dissolve
        lily "I think you and I managed to click quite well."
        lily "And I’m better at talking once I’ve built some rapport... It's just that I don’t know how to meet new people, or reconnect with old friends."
        show lily closeshy with dissolve
        lily "I just never seem to have the energy for it, I'd always prefer to be alone yet simultaneously feel lonely..."
        mc "I see what you mean, meeting people is really hard if you're not put in a situation where you're encouraged to interact."
        mc "I don't think I would have found all these job opportunities and friends alone."
        show lily closeneutral with dissolve
        lily "You're right, it's easy when you're in a social situation, like when you came in earlier for work. I kinda had no choice but to talk to you and things went okay."
        lily "But I would never have gone out of my way to knock on your door and introduce myself on a whim, I think I'd combust from the social anxiety."
        mc "I can relate to that, talking to strangers can be really difficult."
        lily "I just have this barrier of shyness that prevents me from talking to people I don’t know, even people I do know sometimes."
        show lily closesad with dissolve
        lily "Sometimes if I see someone I know on the street, I’ll avoid them. I don’t know why, it makes me feel pathetic."
        mc "It's strange because you seem fine once you get talking."
        show lily closeshy with dissolve
        lily "Yeah... It’s strange how easy socialising can be once that ice is broken, and it can break in wonderful and unexpected ways."
        mc "I think I know what you mean. It’s easy to talk to a cashier at a store because you have to, but it’s extremely hard to just talk to a stranger on the street, even if they're the same person."
        show lily closesatisfied with dissolve
        lily "That’s a succinct analogy. I'm glad you understand me…"
        "She leans towards me and trails her fluffy fingers down my arm."
        show lily closeneutral with dissolve
        lily "I'm really sorry for that tangent, it was inappropriate of me to vent to a stranger like that."
        lily "I just haven't had the chance to talk to someone like that for a while now..."
        lily "I hope that hasn't made you dislike me in any way."
        mc "No, of course not. I think it's good to speak your mind."
        show lily closehappy with dissolve
        lily "I'm really happy to hear you say that."
        lily "I'm interested in helping you. I want to turn you from a stranger in the community, to a citizen and friend."
        show lily closelaughing with dissolve
        lily "I believe it should be my responsibility to help you."
        mc "I really appreciate that; since you're the ambassador you're probably somewhat of an expert."
        show lily closeneutral with dissolve
        lily "Some may call me that, but I’m just a regular overworked girl that tries her best."
        mc "Overworked? I hope I’m not asking too much of you."
        show lily closehappy with dissolve
        lily "On the contrary. I’ve been woefully bored lately. A personal project like you may be the fresh air to this stale 9-5 I’ve been trapped in for the past few years."
        lily "Could you start by telling me a bit about yourself? Actually, everything you can."
        mc "Everything? Where to begin...."
        mc "I’m [playername], I’m a human. I’m from a planet called earth where the only sentient bipedal creatures are humans."
        mc "However my planet earth is different to this one, so it's potentially in a different universe according to Penny."
        mc "It was Moxie that accidentally cloned and teleported me to her wagon [days] days ago"
        show lily closeangry with dissolve
        lily "Hmph, Moxie… I don’t believe it, she wouldn’t be able to teleport you interuniversally... Only Princess Selene could do such a thing."
        mc "Well uh, maybe not then… That’s just a theory."
        show lily closeneutral with dissolve
        lily "I mean maybe you’re from another universe, but people don’t just magically teleport like that."
        mc "What’s your theory, then?"
        lily "It’s not really my place to say, I rarely speak my mind unless I absolutely know what I’m talking about."
        lily "Perhaps you are from another universe, it’s certainly possible. Although the means of arrival is certainly in question."
        lily "If you really were from another universe, would there be an alternate universe version of you wandering around?"
        mc "That’s not something I’ve really considered; do you think they would match my DNA?"
        show lily closesatisfied with dissolve
        lily "Hmm... My current three ideas are:"
        show lily closehappy with dissolve
        lily "1. You’re either from this world and didn’t realize it, maybe your memories were tampered with and you're actually from a faraway country... Although I think your species would be documented if that were the case."
        lily "2. Our worlds co-exist, but they can’t see each other. You merely crossed a barrier of senses or perception. Like a different plane of existence."
        lily "3. You’re a new creation with implanted memories, but I can’t imagine Moxie doing something so incredible."
        mc "If your third theory is true, wouldn’t that make me a permanent familiar? I thought that was impossible."
        show lily closeneutral with dissolve
        lily "It’s actually possible to create a permanent familiar. It involves dragging a creature from another plane of existence, and if you’re lucky you won’t need to cast an obedience spell on it every 24 hours."
        mc "Alright, that sounds awesome, but it’s slightly over my head... Other planes of existence, huh..."
        "She takes a sip of her drink and leans over, carefully observing my face."
        show lily closehappy with dissolve
        lily "Say, may I be daring and invite you to my laboratory?"
        mc "Lab? Are you going to probe me?"
        show lily closelaughing with dissolve
        lily "I can do that if you’d like, I bet I could get lots of information from probing you."
        mc "You’ve got me there; we can save that until after the lab if you’d like."
        show lily closehappy with dissolve
        lily "Hmm, I was thinking... You mentioned something interesting earlier about DNA. I would like to analyse your DNA."
        mc "Ah, I see where this is going. A swab from my cheek not enough?"
        lily "Afraid not, I have a particular need."
        show lily closesatisfied with dissolve
        menu:
            lily "Answer this next question truthfully, have you slept with anyone since you arrived?"
            "No one!":
                show lily closesurprised with dissolve
                lily "That’s a surprise, I thought you’d…"
                lily "I thought girls would try to sleep with you. I was worried that you might be able to get mares pregnant, and I don’t want a mutant baby crisis."
            "Only Moxie.":
                show lily closeangry with dissolve
                lily "Typical, I guess she summoned you for that exact purpose."
                lily "A mare like her probably can’t control her base desires."
                mc "That seems kinda rude…"
                lily "Think of the bigger picture, what if she gets pregnant? How do you know you’re not compatible?"
            "A couple of people...":
                show lily closeembarrassed with dissolve
                lily "Oh... That could be bad."
                mc "Why? What's wrong?"
                lily "I need to test your DNA in case you got any of them pregnant."
            "Moxie, Honey, Ruby, Butters, Cream, Riku… Pretty much everyone":
                show lily closeembarrassed with dissolve
                lily "Oh, oh dear, that’s worse than I thought."
                lily "Oh sheesh, I guess you’re here for me next..."
                lily "Eh-hem, we have an urgent problem, I need to test your DNA in case you got any of them pregnant."
        if butterspregnant == 1:
            "Didn't I already get Butters pregnant? I thought I needed a potion for that."
            mc "Moxie said I was incompatible with ponies, so I always just assumed..."
        else:
            mc "Pregnant? Shit, you’re right. Moxie said we were incompatible, so I always just assumed…"
        show lily closeangry with dissolve
        lily "Assumed? Moxie said that, so you assumed? Don’t be ridiculous, that girl doesn’t know anything."
        mc "That was mean."
        show lily closesatisfied with dissolve
        lily "That was me being generous, there’s a lot I could say about that girl, she’s trouble."
        show lily closeneutral with dissolve
        lily "She may be trying to improve, but she doesn’t know everything."
        lily "I know you two might have formed a nice little bond since you’re living together, but she isn’t the best guide for you."
        mc "Are you any better?"
        show lily closehappy with dissolve
        lily "Naturally! But actions speak louder than words, ask me anything you want."
        label library12:
            show lily closehappy with dissolve
        menu:
            "Are you a virgin?":
                show lily closeembarrassed with dissolve
                lily "Uwah! What a question!"
                show lily closesatisfied with dissolve
                lily "Ohoh, I see what you're doing here..."
                show lily closehappy with dissolve
                lily "You're asking me a question that Moxie wouldn't know."
                mc "Hmm, I think Moxie could figure it out."
                show lily closeshy with dissolve
                lily "Uuu, meanie..."
                lily "*Sigh* I am a virgin, but not because I want to be."
                lily "I'm just, y'know... Boys never like me, they like other hotter mares instead..."
                lily "An awkward mare like me isn't very popular with the stallions."
                mc "Bless your sweet heart, darling."
                show lily closesad with dissolve
                lily ":'<"
                jump library12
            "Can you give me some money?":
                show lily closeneutral with dissolve
                lily "Oh, uh..."
                lily "I guess you are a new citizen, starting from square one can't be easy."
                show lily closeshy with dissolve
                lily "Living day by day must be a struggle for you..."
                show lily closeneutral with dissolve
                lily "Anything I could give you wouldn't possibly be enough to put you in an appropriate position for an individual of your age."
                show lily closehappy with dissolve
                lily "However, I can contact my superiors that can discuss options with you for potential financial help."
                lily "It would delight me if you were able to find accomodation beyond renting from a friend and truly become a member of this new society."
                lily "I'll do my best to make that transition as smooth for you as possible."
                "That felt dramatic, but maybe she has a point, I should consider my position in this world more seriously from now on."
                "It would be awesome to get a house to myself in the future."
                jump library12
            "Will you let me sleep with you?":
                show lily closeembarrassed with dissolve
                lily "Ah, uh… That was a little forward… Are you hitting on me?"
                mc "Yeah, I think so."
                lily "Oh gosh, I like to take things slow, you know?"
                lily "Maybe uh, take me for dinner first, haha."
                lily "Or we could watch a film."
                show lily closesad with dissolve
                lily "Oh, I’m tearing up a little."
                lily "I’m sorry, that happens when I get nervous."
                lily "I’ve just never been asked that before."
                lily "I don’t get out enough, hah."
                lily "Even if I did, it’s not like any man would be interested in me anyway."
                lily "..."
                mc "I don’t mind taking things slowly."
                show lily closeembarrassed with dissolve
                lily "Wait, you’re really interested in me? That wasn't a joke? Oh my gosh!"
                "I think I broke her."
                mc "Are you okay?"
                lily "*Huff*. Yeah..."
                lily "I’ll let you know when I’m free if you would like, maybe we could do a date or 'chill'."
                lily "... Do you have any other questions?"
                jump library12
            "Do you think I could return to my original world?":
                show lily closeshy with dissolve
                lily "Hmm... Probably not."
                mc "Not at all?"
                lily "I don’t know. It really depends on how you got here."
                lily "If you’re from this planet, maybe, if you’re not, then who knows?"
                mc "That was surprisingly unhelpful."
                show lily closeneutral with dissolve
                lily "Don’t be like that, I don’t want to fill your mind with false promises."
                lily "If you stick around, I could ask Aurora if she knows anything."
                if augustavisit >= 2:
                    "Aurora, eh? I wonder if Lily has met her before, given that she is an ambassador."
                else:
                    "Aurora? I heard that name before from Moxie, isn't that the Queen!?"
                lily "Anything else?"
                jump library12
            "What did Moxie do to cause such ill-feelings?":
                show lily closeangry with dissolve
                lily "Eugh, that girl endangered the entire city by trying to do some stupid circus performance."
                lily "She stole a young animal from its mother for her sick magic show."
                mc "That’s awful…"
                lily "That’s not all, the real problem is, the mother was an angry 10 foot bear that came into the suburbs looking for revenge."
                "Moxie didn't tell me about that part, yikes!"
                lily "If it wasn’t for me and Penelope, it might have been carnage."
                mc "Even so, Moxie has changed now, right? She’s improving."
                show lily closeshy with dissolve
                lily "Meh, when you put hundreds of lives in danger, it’ll take longer than a few months of good intentions to warm me back up."
                mc "I understand…"
                jump library12
            "That’s all":
                pass
        show lily closeneutral with dissolve
        lily "Maybe I’m a little harsh on Moxie. I’ll watch her from a distance and see if she really does change. Maybe this situation with you will help her improve."
        mc "It’s fine, I get it. Not everyone is destined to get along."
        show lily closeshy with dissolve
        lily "It's not like I'm against being friends, but the vibe between us is awkward."
        "It's sad to realize this, but I think Moxie feels the exact same way."
        show lilyb
        show lily happy
        with dissolve
        lily "Enough about that, come, let me show you to my lab."
        scene bg libraryupstairs with dissolve
        "As we head out, we run into a familiar face in the hall."
        show penelope happy:
            xpos 200
            ypos 30
        show lilyb:
            xpos 700
            ypos 10
        show lily surprised:
            xpos 700
            ypos 10
        with dissolve
        penelope "Ahh, hello you two, I wasn't expecting to see you here."
        show lily neutral with dissolve
        lily "Hello Penelope, I think [playername] came to work with you, but I just have a few tests I’d like to run."
        show penelope laughing with dissolve
        penelope "Sure thing! How’s it going [playername]? Settling in alright?"
        mc "I’m doing great, I’m having a lot of fun here."
        if days >= 5:
            mc "Everyone is welcoming and kind; I’m making lots of friends too. I can see myself living a happy life here."
        else:
            mc "I'm still getting used to the new environment, but I'm slowly coming to terms with my new life."
        show penelope happy with dissolve
        penelope "I'm really happy to hear that, pop down whenever you’re done with your lab fun, no rush. I'll pay all the same."
        stop music fadeout 10.0
        hide penelope with dissolve
        "Penny heads off while me and Lily make our way to the lab."
        scene bg librarylab with dissolve
        show lilyb
        show lily happy
        with dissolve
        mc "Does Penny live here? Looked like she came out of a bedroom."
        show lily laughing with dissolve
        lily "Yeah, she does! The rent on this giant tree is cheaper that way."
        hide lily
        hide lilyb
        with dissolve
        "Lily closes the lab door behind us, going so far as to lock it."
        show lilyb lab
        show lily neutral
        with dissolve
        "Then she puts on a lab coat, before ruffling through a cluttered draw of glassware. She takes out a single petri dish."
        show lily shy with dissolve
        lily "Okay, how would you like to do this?"
        mc "Do you want me to spit?"
        show lily happy with dissolve
        lily "Hehe, are you going to make me say something so embarrassing?"
        mc "Huh?"
        show lily horny with dissolve
        label lilytj:
            pass
        lily "I need to test your semen, silly."
        mc "Figured as much... In this petri dish?"
        show lily happy with dissolve
        lily "Yeah, yeah…"
        mc "Alright, where can I go to do this privately?"
        show lily embarrassed with dissolve
        lily "W-Wait, aren’t you going to let me watch?"
        mc "It just feels weird masturbating while a girl watches."
        lily "B-But this is valuable research information on your mating and masturbatory habits!"
        if augustavisit >= 2:
            mc "Sheesh, you're starting to sound like Augusta."
        show lily horny with dissolve
        lily "And... I thought having a girl watching might help..."
        mc "I guess you are nude, that does help a tiny bit."
        lily "Um, what do I need to do?"
        play music sex1 fadein 15.0
        menu:
            "Squish your boobs together.":
                mc "If you’re so determined, how about doing something with your breasts?"
                lily "Ehehe, my boobs?  They're a little small, but I'll try..."
                show lilyb closelab
                show lily closehorny
                with dissolve
                "She squishes her tiny boobs together a little, it’s not much, but it’s the thought that counts."
            "Show me your ass.":
                mc "If you’re so determined, how about doing something with your ass?"
                lily "Ehehe, you're an ass man? I do have a cute butt..."
                hide lilyb
                show lily butt
                with dissolve
                "She turns around, lifts up her labcoat and wiggles her butt; it’s not much, but it’s the thought that counts."
            "Are you serious?":
                lily "Am I being too forward? I'm just trying to flirt..."
                mc "Ooohhh, I see... In that case..."
                menu:
                    "Squish your boobs together.":
                        mc "If you’re so determined, how about doing something with your breasts?"
                        lily "Ehehe, my boobs?  They're a little small, but I'll try..."
                        show lilyb closelab
                        show lily closehorny
                        with dissolve
                        "She squishes her tiny boobs together a little, it’s not much, but it’s the thought that counts."
                    "Show me your ass.":
                        mc "If you’re so determined, how about doing something with your ass?"
                        lily "Ehehe, you're an ass man? I do have a cute butt..."
                        hide lilyb
                        show lily butt
                        with dissolve
                        "She turns around, lifts up her labcoat and wiggles her butt; it’s not much, but it’s the thought that counts."
        "I start to work on my shaft, the blood slowly gets pumping, and I begin to get an erection."
        lily "Woah, I can see it growing..."
        mc "Yeah, they tend to do that. Is this your first time seeing one in person, or something?"
        lily "M-Maybe... It's kinda making me feel hot."
        "Having a girl watch and help me like this is surprisingly erotic. It only takes a few seconds of looking at Lily before I'm erect."
        lily "Mmmhh yeah, rub that cock for me..."
        lily "I mean, for science! Yes..."
        "Lily's stare is transfixed onto my cock as she bites her lip."
        "To my surprise, she closes the distance and gives me an even better view."
        lily "I need to make sure you can't get mares pregnant, you know?"
        mc "To make sure you won't get pregnant?"
        lily "M-Me? I mean, yes technically I'm a mare, b-but..."
        lily "Hnngg, I'm getting so wet..."
        lily "Darn heat..."
        scene bg librarylab
        show lilyb lab
        show lily horny
        with dissolve
        lily "Could I try something?"
        mc "Anything you want."
        lily "I heard it feels better when someone else touches your genitals, I want to test that."
        mc "Is this your first time doing anything like this?"
        show lily shy with dissolve
        lily "Uh, uhm... Is that a bad thing?"
        mc "No, no, I'm just surprised, is all."
        show lilyb closelab:
            xpos 225
            ypos 750
        show lily closehorny:
            xpos 225
            ypos 750
        show lilyhandjob:
            xpos 465
            ypos 0
        with dissolve
        "She brings one hand to my shaft and starts to clumsily move it up and down."
        show lily closelaughing with dissolve
        lily "I'm only nineteen you know, it's normal to be a virgin at my age..."
        "Her movements are hot and arousing, it honestly does feel a little better than when I do it."
        show lily closehorny with dissolve
        lily "I hope I'm not coming onto you too quickly."
        mc "This is good, I hope I won't cum too quickly either."
        show lily closehappy with dissolve
        lily "I really do want to study you, maybe you’re a new species. Kinda makes me feel all fuzzy thinking about it."
        mc "Ah, a real scientist at heart. Maybe you want to study my mating habits next."
        show lily closehorny with dissolve
        lily "Precisely, we can’t give this opportunity up! If I have your DNA, maybe I could find out where you’re from..."
        mc "That being said, if you were trying to come onto me, my semen isn’t any use inside you."
        stop music fadeout 10.0
        show lily closeembarrassed with dissolve
        lily "Uuu… How embarrassing! I was just going to do it with my hand, honest!"
        mc "I don't think you could make me cum with just your hand, your technique is too amateur."
        show lily closeshy with dissolve
        lily "Tsk, reading books about sex only gets you so far I guess."
        play music lily
        hide lilyhandjob
        show lilyb lab
        show lily horny
        with dissolve
        lily "I've got another idea though!"
        scene bg librarylab
        show lilyb
        show lily horny
        with dissolve
        "She takes off her lab coat while intermittently rubbing her pussy. The once shy pony is so aroused that she now openly masturbates in front of me."
        mc "You're getting hornier by the second, I hope you don't do this to every man that walks into your house."
        if boutiquevisit1 == 1:
            "Then again, isn’t that exactly what Melody did?"
        show lily surprised with dissolve
        lily "N-No! It’s just... When you knocked on the door, you interrupted me mid-masturbation…"
        show lily shy with dissolve
        lily "Then we talked a lot, and you were cute… I thought you’d be on board!"
        lily "But, it’s not like I’m trying to trick you [playername]. I do need your DNA!"
        lily "How about I try something else..?"
        menu:
            "Hmm… Should I go along with this mare’s fantasies?"
            "Hell yes, show me what you've got.":
                mc "Show me what you've got cutie."
                show lily laughing with dissolve
                lily "Ah, awesome!"
            "Don't you want to take things slow?":
                show lily embarrassed with dissolve
                lily "I mean a part of me kinda does, but then another part of me wants {i}other{/i} things..."
                lily "So... Why not both? Have some fun, but let's not go too far."
                mc "Hm... Sure thing."
                mc "I guess we've gotten this far, no sense in stopping."
            "This is too much.":
                show lily shy with dissolve
                lily "It's not like we're going to have sex... I like to take things slowly."
                show lily neutral with dissolve
                lily "I just want to do something that might make you cum a bit easier..."
                mc "Like a blowjob?"
                show lily happy with dissolve
                lily "Hehe, you'll see."
                mc "Alright, for science."
        show lily laughing with dissolve
        lily "Ahah, thank you so much! I won't disappoint you!"
        show lilyb close
        show lily closehorny
        with dissolve
        lily "This is going to be a ton of fun; it was so hot when I read about this."
        "At this point I’ve gone flaccid, but I try to get the blood flowing again. Lily closes the gap between us and she starts whispering lustfully into my ear."
        lily "I’m a virgin, so I won’t let you use my pussy…  But..."
        stop music
        stop ambience
        scene bg black with dissolve
        lily "I want you to slide your cock between my legs and fuck my thighs."
        show bg librarylab
        show lilytj
        with dissolve
        play music sex1
        play ambience sex
        "Before I can even comprehend her lecherous words, the cute purple mare straddles my cock between her thighs and starts to rub."
        lily "Mmphh, look how wet my pussy is already, I'm just aching for cock right now..."
        lily "I've never been this horny in my life... I feel like my ovaries could burst."
        "She stands on her tippy toes and positions herself against my chest. My shaft is comfortably nestled between her warm thighs and dripping wet vulva."
        lily "Ooo, being this close to you… I feel like I could melt, [playername]..."
        lily "Such a handsome man... You’re making my loins burn."
        "She pushes me against a wall and leans on me with the sexual aggression of a mare in heat."
        "Her hips gently gyrating against my shaft. It’s such a subtle motion that it seems subconscious."
        lily "Oh my gosh, I can’t believe I’m doing this…"
        lily "This isn't like me at all, honest…"
        menu:
            "(Dirty Talk): You're just a dirty slut like the rest of them.":
                lily "Ohh fuck yeah, I'm just a bad bitch..."
                lily "Oh my gosh, I swore! I don't usually do that..."
            "(Passive Reply): It's fine Lily, I believe you.":
                lily "I can't help myself, I need this dick more than I need anything right now..."
        "Her arms wrap behind my back as she nuzzles my chest and grinds against my erection in a lewd embrace."
        lily "Haahh, this feels so good... Does it feel good for you too?"
        mc "Yeah, much better than just your hand. Tighten your thighs a little more for me."
        "She does so, and while her thrusts are slow and methodical it’s a tight pleasureful sensation."
        "Her thighs are also immensely soft and furry, it’s extremely pleasing."
        lily "Why don’t I feel shy around you? Why do I feel like I can do anything with you? It’s so weird…"
        mc "Is it because of your heat?"
        lily "I dunno… I usually avoid men while I’m in heat..."
        lily "That’s putting it lightly, I avoid everyone even when I’m not in heat…"
        "She starts rocking back and forth quite fast now, seems she’s getting into it."
        lily "Ahhh… [playername], you’re so hard…"
        "The tightness of her thighs combined with her speed feels surprisingly good. Especially as her wetness drips down my cock."
        "Her movements are silky smooth as her hips gyrate up and down my shaft. She’s getting faster too."
        lily "Hahh, hahh… A-Are you close?"
        mc "Keep going, I’ll let you know when I’m ready."
        lily "Mmphh, okay…"
        "She sinks her head back into my chest and continues to grind against my shaft."
        stop ambience
        "But after a few seconds she stops and whispers something into my ear."
        lily "Don’t cum…"
        hide lilytj
        show lilyb sex
        with dissolve
        "She backs away slightly and turns around, bending over slightly and revealing her cute butt."
        show lily sex2 with dissolve
        "Then she guides me inside of her while backing into me."
        "As I slowly slide deeper, her tightness is immediate, squeezing around my shaft."
        lily "Ahhhh, aaaahhhhhhhhh! Yeeessssss..."
        play ambience sex
        "She starts to bounce back and forth on my cock, the thrusts are only shallow, but they tease my glans perfectly."
        lily "Oh gosh, ahh, yes… I-I’m gonna…"
        "She rides me with surprising vigour and her pussy tightens around my cock as she climaxes, I have to hold back to prevent myself cumming inside of her."
        lily "Ahh… Aaaaahhhh, ahhhhhhhh… Haahh… hahh… Gosh… Hah…"
        stop ambience
        "Just as it feels like I won’t be able to hold back my ejaculation much longer, she slows down and pulls away."
        hide lily with dissolve
        lily "Mmphh… Fuck…"
        scene bg librarylab
        show lilyb
        show lily embarrassed
        with dissolve
        lily "Wait, let me get the petri dish."
        scene bg librarylab
        show lily closedish
        with dissolve
        "She grabs the dish and kneels down in front of my cock as I jack myself off, teetering on the edge of orgasm."
        lily "Cum for me [playername], let it all out…"
        show lily closedish2 with dissolve
        "With the dish in hand and her mouth open and waiting, her tongue playfully waggles back and forth, I speed up my hand movements and prepare to let it all out."
        show lily closecumtongueout with cum
        play sound cum
        show lily closecumtongueout with cum
        play sound cum
        stop music fadeout 10.0
        "My orgasm is so powerful that it covers her face and the dish in cum. Several loads dripping down her face, she manages to catch some of it in her mouth which she eagerly gulps down."
        show lily closecumlaughing with dissolve
        lily "Ahhh, yesh, sho much…"
        show lily closecumhorny with dissolve
        lily "Hehe, your aim is pretty bad..."
        show lily closecumhappy with dissolve
        "She licks her lips and laps up some cum dripping off my tip."
        hide lily with dissolve
        "She carefully takes her petri dish and seals it with a plastic wrap, before wiping the cum off her with some tissues."
        play music lily fadein 5.0
        show lilyb
        show lily happy
        with dissolve
        lily "Phew, I feel… I feel alive, I feel so refreshed. I feel all perky and bouncy."
        show lily laughing with dissolve
        lily "Ahahah, this is incredible."
        show lily happy with dissolve
        lily "I haven’t felt this good in… I-I don’t even know!"
        "She's acting wired, glad I could make this otherwise lonely girl feel so good."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        mc "I can't believe we just had sex, you just lost your virginity!"
        show lily embarrassed with dissolve
        lily "Oh... Oh... We DID do that, didn't we?"
        lily "Oh my gosh! [playername]... If you told anyone, I’d die of embarrassment."
        mc "Don’t worry, I promise I won’t tell anyone, not even Moxie."
        show lily laughing with dissolve
        lily "You’re an absolute babe, come here."
        show lilyb close
        show lily closesatisfied
        with dissolve
        "She kisses me on the cheek and giggles."
        show lilyb
        show lily neutral
        with dissolve
        lily "This isn't quite how I imagined losing my..."
        show lily sad with dissolve
        lily "I-I mean you're not even my boyfriend yet!"
        "Yet? I hope I haven't given this girl the wrong idea."
        show lily shy with dissolve
        lily "Was it too much? What would Aurora think?"
        mc "If you enjoyed it, you’re perfectly within your means to do it, as long as it isn’t harming anyone."
        show lily surprised with dissolve
        lily "Of course, you’re right, forget Aurora."
        show lily neutral with dissolve
        lily "It was just… Such a heated in-the-moment decision, I just…"
        show lily shy with dissolve
        lily "I need some time to think, is that okay?"
        mc "Sure, how about we calm down and snuggle for a few minutes?"
        show lily sad with dissolve
        lily "No, no… I need some time alone."
        lily "A-And anyway, I have work to do. Oh, and your semen too."
        mc "When can I expect results for that?"
        show lily neutral with dissolve
        lily "Come back in a few hours? Hopefully my head is cleared up a bit by then."
        mc "Sure thing, I’ll go downstairs and work with Penelope."
        stop music fadeout 3.0
        scene bg black with dissolve
        "..."
        show bg library2 with dissolve
        show penelope happy with dissolve
        play music library fadein 3.0
        "I take my leave and return downstairs where Penelope greets me. She has some work for me to do which is mostly sorting books and then putting them back on the shelves."
        hide penelope with dissolve
        show bg library with dissolve
        "These are otherwise ordinary tasks, but this library is gargantuan. I’ll need to use a ladder for the majority of them."
        "Apparently she usually uses magic to take these books down, I don’t have that liberty. But I’ll get paid the same despite my lessened efficiency."
        "About half-way through my work Penny calls me over for a break."
        show bg library2 with dissolve
        show penelope happy with dissolve:
            xpos 200
            ypos 30
        penelope "Look at you, you’ve almost worked up a sweat."
        mc "Climbing up and down that ladder is dizzying work."
        show penelope laughing with dissolve
        penelope "If you think this is hard work, don’t go working at Honey’s farm."
        if farmvisit1 == 1:
            mc "Oh trust me, I know all about that. Lots of ladders there too, I’m used to it by now."
        else:
            mc "Yeah I can imagine, working at a farm must be exhausting."
        penelope "Anyway, I called you over because, surprise! We have a guest."
        show moxie2 laughing with dissolve:
            xpos 700
            ypos -30
        moxie "Hey hey hey! Surprise new kid! Penelope and I were just scheming behind your back! Hehe."
        mc "Ah! The one and only mad Moxie! Howdy."
        show moxie2 smug with dissolve
        moxie "Haha, I see you’re settling into the soul sucking 9-5."
        show penelope happy with dissolve
        penelope "He’s doing a good job too; I’ve had the chance to sit back and file my nails."
        mc "She says that, but she’s been doing exactly the same thing as me with another pile of books."
        mc "Except she finished in half the time..."
        show moxie2 bashful with dissolve
        moxie "Wowee, working here sounds boring."
        show penelope laughing with dissolve
        penelope "You say that, but as soon as we run out of books, we get to sip tea and have sophisticated conversations. Isn’t that right [playername]?"
        mc "That’s right, I’ll be going home tonight with a few extra points of IQ."
        show moxie2 laughing with dissolve
        moxie "You certainly need all the points you can get, heheh."
        show moxie2 happy with dissolve
        moxie "Anyways, my condolences but I’m here to add another book onto the pile."
        show penelope neutral with dissolve
        penelope "Ah yes, the conjuration book, let me have a look at that for a moment."
        penelope "Did you see anything unusual where [playername] 'teleported' in?"
        show moxie2 sad with dissolve
        moxie "Nope, nothing out of the ordinary at all. It's kinda boring, sorry to disappoint. But I guess it doesn't matter?"
        show penelope happy with dissolve
        penelope "On the contrary, that’s what I hoped. This provides further insight into the method of [playername]’s appearance."
        show moxie2 neutral with dissolve
        moxie "Huh, really? I don’t follow, I'm not very well read on this area of cosmic stuff."
        show penelope shocked with dissolve
        penelope "Okay, let’s say for a moment, that you found a piece of cloth. Perhaps cloth from [playername]’s bed where he was peacefully sleeping before rudely teleporting away."
        penelope "That would imply you teleported a section of space, which undoubtedly included blankets and anything surrounding [playername]."
        mc "Oh, I get it! Because there were no blankets or fabrics that teleported with me, it means I, and only I was specifically teleported."
        show penelope laughing with dissolve
        penelope "Exactly, whatever happened was dead-on specific."
        show moxie2 smug with dissolve
        moxie "Spicy! But how does this further our investigation?"
        show penelope happy with dissolve
        penelope "It narrows down our options significantly."
        penelope "Oh, [playername], you spoke with Lily right? Did she say anything about it?"
        mc "You mean you haven’t asked her yourself?"
        show penelope neutral with dissolve
        penelope "Ah, well… She’s not exactly social, that girl never leaves her room."
        show moxie2 shy with dissolve
        moxie "Eugh... You’ve been hanging around her? Surprised she gave you the time of day, [playername]."
        mc "She wanted to conduct some tests on me."
        show moxie2 angry with dissolve
        moxie "What kind of tests were they? I hope she wasn’t poking you with needles and other weird things."
        mc "No, no, nothing weird, just a swab from the inside of my cheek. She wants to check my DNA."
        show penelope shocked with dissolve
        penelope "DNA? How will that help us?"
        mc "I’ve been thinking that this is another universe. Maybe that means there’s another me in this universe."
        mc "If we have my DNA, maybe we could find a match."
        show moxie2 horny with dissolve
        moxie "Huh? Two versions of you? Oh dear, imagine that? I think it’d overload my head."
        "She's giving me a facial expression that I can only assume means 'threesome please'."
        mc "It would prove that I’m from a different universe, right? Just a tiny bit of evidence will narrow down our options even more."
        show penelope happy with dissolve
        penelope "Trust Lily to have such a fascinating new perspective on the situation... What do you think [playername], is there another version of you walking around?"
        mc "I… I have a strong feeling that there might, just call it a hunch."
        show moxie2 laughing with dissolve
        moxie "There’s no harm in trying to find out, I have faith in you [playername], even if it means we have to work with Lily."
        mc "I’ll see what she has to say, I guess she’s our only avenue for forwarding this."
        penelope "Alright, if you believe it may help, I’m on board."
        show penelope neutral with dissolve
        penelope "If there is another you, that means you were specifically pulled from one universe to another. It's crazy to think about, but at least we’ll have our answer."
        penelope "But I don't want you two to dwell on this issue too much. I still don't think you can go back."
        mc "No worries, I'm pretty comfortable living here now. I guess finding an answer is just something to do, ain't it?"
        show moxie2 happy with dissolve
        moxie "Mhm, you're all mine now, eheh!"
        if livingwithmoxie == 1:
            moxie "Yo, I’m gonna go back to work now, my lunch break has gone on a bit longer than I expected. I’ll see you back in the wagon, cutie!"
        else:
            moxie "Yo, I’m gonna go back to work now, my lunch break has gone on a bit longer than I expected. Be sure to swing 'round my wagon tonight, cutie."
            mc "Sure thing."
        hide moxie2 with dissolve
        "Moxie dashes off leaving both me and Penny alone."
        hide penelope with None
        show penelope happy with dissolve
        mc "She called me cutie."
        penelope "I think she likes you, and I don’t just mean the obvious, I think she really, really likes you."
        mc "I thought as much. But I’m surprised you could tell from casual flirting."
        penelope "I keep my cards close to my chest. I can tell you’ve been sleeping together."
        mc "How’d you figure?"
        show penelope neutral with dissolve
        penelope "Other than the obvious, she’s stopped coming to see me…"
        penelope "We had a… ‘You wash my back, I’ll wash your back’ relationship going on."
        mc "Ah, you were friends with benefits."
        mc "I’m sorry, she’s been too busy looking after me to spend time with her friends."
        show penelope happy with dissolve
        penelope "I’m jealous, but simultaneously I’ve never seen her bursting with so much joy and energy."
        mc "Really? That makes me so happy to hear, wasn’t she like this before?"
        show penelope neutral with dissolve
        penelope "No, she was lonely and while I won’t say miserable, she was definitely sad before you arrived."
        penelope "She’d visit here a lot, sometimes multiple days in a row. We'd cheer each other up."
        show penelope sad with dissolve
        penelope "I guess I feel happy for her, I just feel a little empty inside."
        mc "… I’m sorry, do you like her?"
        show penelope satisfied with dissolve
        penelope "Maybe a little, but I’m kidding myself if I think she’ll be my girlfriend, she always told me she wouldn’t."
        "Damn, that means she asked, doesn't it?"
        show penelope neutral with dissolve
        penelope "I guess I’m just feeling a little lonely."
        penelope "I'm not saying we will, but if we spontaneously find a way to send you back consequence free, what would you do?"
        menu:
            "Stay here.":
                show penelope happy with dissolve
                penelope "Interesting, even if we don't have the clone problem I mentioned last time?"
                mc "Yeah, there's a lot more keeping me here than there was at home."
                show penelope neutral with dissolve
                penelope "I don't mean to be rude, but that's almost sad to hear."
                penelope "I think if I was in your position I'd beg to go back."
                mc "You sure? I have more friends, more to do, more freedom. Things here are just better, and not just for me specifically."
                penelope "Hmm... So this world is better than yours... I... That's interesting."
            "Go back home.":
                show penelope happy with dissolve
                penelope "I suppose that makes sense, so I apologize that it may not happen."
                mc "Yeah, like you said, there's probably another me having a happy life over there."
                mc "Still tapping away at his computer while fapping to pony porn."
                show penelope shocked with dissolve
                penelope "What porn?"
                mc "Sorry, I think I've been here too long."
                penelope "Haha, I see."
            "Hopefully go back and forth.":
                show penelope happy with dissolve
                penelope "That would be ideal for everyone..."
                mc "Perhaps too ideal."
                show penelope satisfied with dissolve
                penelope "You said it..."
        penelope "I'm glad you're so relaxed about this dilemma, someone with less mental fortitude may have genuinely gone crazy at the realisation that they've lost their life."
        mc "It's fortunate that I'm young and didn't have much to lose."
        mc "I miss my family and friend circle, but that's more or less it."
        mc "I have a lot more peace of mind imagining my clone still there with them. I don't like to imagine that not being the case."
        show penelope happy with dissolve
        penelope "Me too, me too..."
        penelope "Say, after we put these books back, do you wanna hang out for a bit?"
        penelope "How about we watch one of my favourite films? I bet you haven’t seen a film from around here yet."
        mc "Yeah, I’ll be down for that. Don’t we need to watch the library though?"
        show penelope laughing with dissolve
        penelope "We close at three, we can do it after that."
        scene bg black with dissolve
        stop music fadeout 3.0
        "…"
        "Penny finishes putting away her pile of books before I do, so she comes and helps me."
        "We get the job done, and she pays me 25 monies. Just before three and as Penny closes up the library I excuse myself to go see Lily."
        show bg libraryupstairs with dissolve
        "I make my way upstairs and knock on the laboratory door."
        show bg librarylab with dissolve
        "The purple pony peeks from the window and opens the door with her magic, I step in and it’s immediately closed behind me."
        play music lily
        show lilyb lab
        show lily happy
        with dissolve
        lily "Good, it’s you. I was thinking about you."
        mc "Can’t get me out of your head?"
        show lily laughing with dissolve
        lily "It would seem that way. I’d say you’ve been positively distracting, yet I find myself unusually productive today."
        show lily happy with dissolve
        lily "Not only have I finished my day’s work, but I also analysed your semen. Come over here a second and check this out, it's fascinating!"
        scene bg librarydna with dissolve
        "I take a look at a computer. It seems to be a set of data mapping out my DNA, but honestly I have no idea what I’m looking at, this technology might not even exist in my world."
        show lilyb closelab
        show lily closesurprised
        with dissolve
        lily "Seems here that you’re incredibly similar to us ponies, but narrowly not sexually compatible. No need to worry about pregnancy."
        mc "I figured as much when I found out there are fewer stallions than mares."
        mc "Where I’m from human births are almost exactly 50/50 male/female, so there’s definitely some subtle differences."
        show lily closehappy with dissolve
        lily "Subtle indeed, although no less subtle than the differences between say a dragoness and a mare. I’ve studied some biology before, so I have a keen eye for it."
        mc "This is good news, but I want to propose something else for you, perhaps a challenge."
        mc "Is there any way to use this DNA to see if there’s another me?"
        show lily closesurprised with dissolve
        lily "Uhh, you mean… A copy of you?"
        mc "Yeah, if we can do that, we’ll know for sure that I’m from a different universe."
        lily "What makes you so sure that you even exist in both universes?"
        mc "There are some subtle similarities between this world and the world I’m from that lead me to believe that there may be another me."
        mc "It was also my cover up story when Penelope asked me why you needed my DNA."
        show lily closehappy with dissolve
        lily "Ahh good thinking, I hope you covered up the semen part too."
        lily "So you have more than a just hunch about this universe thing. I'm not sure myself, but I'll humour you."
        mc "Can you do it?"
        lily "Yeah, I think I could do a test over a short range with my magic, like a radar to see if there’s any nearby creatures that match the DNA. Of course, this'll be able to detect even a 'pony' version of you."
        mc "Hell yeah, I knew you’d pull through, magic is so awesome."
        show lily closeneutral with dissolve
        lily "No promises though, this is me improvising to the best of my ability, it may not work."
        show lily closehorny with dissolve
        lily "But… I’ll do it for you, it’s the least I could do after you put up with my horny ass this morning."
        mc "I would have done that for free."
        show lily closelaughing with dissolve
        stop music fadeout 3.0
        lily "Pfft, don’t embarrass me, it makes it hard to focus on casting, I need complete silence..."
        show bg librarylab with dissolve
        show lilyb closelab
        show lily closesatisfied
        with dissolve
        "She takes a deep breath and takes a few steps backwards before closing her eyes."
        play music epic fadein 5.0
        lily "Here goes…"
        pause 0.5
        scene bg purple with cum
        play sound magic2
        pause 0.5
        "A purple flash emanates through the room, it's bright and all encompassing. But it doesn't hurt my eyes, even if I look right into it."
        pause 0.5
        "As this light passes it's accompanied by a gust of wind which pricks against my skin, sending shivers down my spine and leaving me with goose bumps."
        "The light seems to dissipate, but the magic isn't over yet, merely the radar of the area has begun."
        pause 0.5
        scene bg dusklightmagic with cum
        "Lily glows intently as she diligently examines the surroundings of the Arcadian suburbs for any DNA matches."
        pause 0.5
        "Her eyes glowing with palpable energy as she focuses intensely."
        pause 0.5
        "I remain stood, almost intimidated by the show of power."
        pause 0.5
        "This moment feels like it lasts an eternity, but within mere seconds she finishes and the energy gradually begins to return."
        pause 0.5
        "With one final climatic reverse sweep of energy, it all culminates back into her horn..."
        pause 0.5
        scene bg librarylab with None
        show lilyb lab
        show lily satisfied
        with cum
        "Not with a flash but with a fizzle, she finishes and takes a moment to catch her breath."
        show lily surprised with dissolve
        lily "Phew... Haahh... I got one DNA match!"
        mc "No way! Where?"
        show lily laughing with dissolve
        stop music fadeout 3.0
        lily "Ohh… I just realized that one match was probably you."
        mc "Yeah, that'd make sense…"
        show lily happy with dissolve
        play music day2 fadein 3.0
        lily "Either way, that goes to show that there isn’t another you in the suburbs at least. I’m afraid if you want a more conclusive search, you’d need to ask the Queen."
        if augustavisit >= 2:
            mc "The Queen? I've actually met her. It was a rather random encounter though."
            show lily embarrassed with dissolve
            lily "Really? I suppose it'd only make sense for her to seek you out for questions."
            mc "That's the strange part, she didn't ask me anything, she was just scolding Augusta."
            lily "It sounds like you've been getting tangled up in some strange occurrences if you've already mixed with both the Queen and Augusta."
            mc "You could say that..."
        else:
            mc "The Queen? Seems intimidating."
            lily "Maybe I’ll introduce you two, she may have an interest in a strange alien creature appearing in her domain."
            show lily satisfied with dissolve
            lily "Mostly likely though, she’s already more than aware of you."
        if days >= 3:
            mc "Aurora did send me a care package in the mail, she seems really nice."
            show lily happy with dissolve
            lily "That's very sweet and thoughtful of her. Did it include a cookie?"
            mc "It sure did, how'd you figure?"
            show lily laughing with dissolve
            lily "I always get one too!"
        else:
            mc "She knows I’m here? Spooky."
        show lily happy with dissolve
        lily "Either way, I hope the DNA test helped, although I don’t really know what conclusion you can really draw from it."
        lily "I can tell you’re hiding something, but I’ll let it pass."
        "She can tell? She's extremely sharp."
        mc "I appreciate the help, even if the results aren’t what we hoped, they still help me narrow down the options."
        mc "If there isn’t another copy of me around, that gives more credence to your theories."
        mc "Maybe I’m from a distant planet, or a different plane of reality. I don’t know, it’s all crazy stuff."
        show lily laughing with dissolve
        lily "If that is the case, I’m afraid it’s way out of my pay grade."
        show lily happy with dissolve
        lily "If you genuinely believe that, you should send a letter to Princess Selene, that’s her expertise."
        mc "Princesses and Queens huh? Sounds like it's a little out of my reach as a newbie in these parts, do you think you could help me do that?"
        lily "Yeah, I think I probably could. What do I get in return for that though?"
        mc "Oh, I don’t know, I don’t have a lot to offer."
        show lily horny with dissolve
        lily "Ehehe, I’m just teasing you. Visiting me again will be enough, can you do that for me?"
        mc "I’d love to, Lily."
        show lily laughing with dissolve
        lily "Ehehe, you’re making me all giddy. I can’t believe myself today."
        lily "Next time you see me, I’ll have a permit to let you in the castle and we’ll go together."
        stop music fadeout 60.0
        scene bg libraryupstairs with dissolve
        "We bid our farewells and I head out of the lab."
        show bg peneloperoom with dissolve
        "I take a peek into Penny’s room and spot her lounging around on a quaint sofa setup. It looks comfortable, pretty similar to Moxie’s room."
        show penelope closehappy with dissolve
        penelope "Oh there you are, what do you think of Lily then?"
        mc "She’s nice, and trying to help me in her own ways. She actually wants to give me an audience with Aurora."
        show penelope closeshocked with dissolve
        penelope "You’re kidding…"
        penelope "I guess it makes sense though... Your appearance is within Lily's jurisdiction. She probably feels responsible for you."
        mc "Yeah, she mentioned that she’s kind of a big deal, she helps people here, right?"
        show penelope closeneutral with dissolve
        penelope "Reluctantly perhaps, that girl never leaves the house. Even I barely see her."
        mc "She told me she’s really shy and struggles to talk to people."
        penelope "What’s your take on that, did she say anything weird?"
        mc "Not really, she seemed open and friendly. She specifically asked if I could visit her again."
        show penelope closesad with dissolve
        penelope "I feel like she’s been so cold and aloof lately."
        penelope "But maybe I’m just judging her unfairly… She’s probably just being quiet and shy."
        mc "I’d definitely say the latter, she was friendly with me."
        show penelope closesatisfied with dissolve
        penelope "*Sigh*, yeah… Easy to forget that she’s the Queen’s student, she must have one of the biggest workloads of any mare in the country."
        mc "You’re kidding? She didn’t even mention that to me."
        show penelope closehappy with dissolve
        penelope "She wouldn’t, it’s not a big deal to her."
        mc "Wow, that explains how she can give me an audience."
        show penelope closeneutral with dissolve
        penelope "Could you pay close attention to her the next time you two meet up? I don’t mean to poke my nose where it doesn’t belong, but I am slightly concerned about her sometimes."
        mc "I don’t mind, you’re just worried about a friend."
        show penelope closehappy with dissolve
        penelope "Cheers [playername]. I wasn’t sure about you at first, but you’re pretty cool. I can see why Moxie likes you, you two are a match for sure."
        show penelope closesatisfied with dissolve
        penelope "Pardon me, I’ve been asking you too many questions. I hope I’m not making you uncomfortable, I did invite you here for a movie."
        show penelope closehappy with dissolve
        penelope "I bet you haven’t seen a pony film before, there are so many great ones I could show you."
        mc "I’m excited to see what a film from another world is like."
        mc "Everyone will be naked in the film too, how weird!"
        penelope "Nothing weird about that!"
        hide penelope with dissolve
        play music movie fadein 3.0
        "Me and Penny start watching one of her favourite pony films. It's extremely high quality, it seems the inclusion of magic in this world has given filmmakers tons of freedom in effects and cinematography."
        "Seriously, this film is amazing! I guess Penny did say this was her favourite."
        "Penny seems distracted and fidgety though."
        show penelope closesad with dissolve
        penelope "I think I made a mistake…"
        mc "Are you alright?"
        penelope "Yeah, yeah… I’m fine, let’s keep watching."
        hide penelope with dissolve
        "As we continue to watch, Penny is clearly troubled by something. It gets to the point where she stands up and starts pacing around the room. I can’t help but ask her what’s wrong."
        mc "Really, Penny, is everything okay?"
        show penelope shy with dissolve
        penelope "Uhm, yes and no. Hang on, let me pause the film."
        stop music
        play music suspense
        "Aw damnit, it was just getting exciting."
        show penelope closeneutral with dissolve
        "She sits down beside me again."
        penelope "I was a little naïve, but I didn’t realize my estrus would be this bad."
        penelope "Since you’re a ‘human’, and not a stallion I thought we could just chill out together."
        show penelope closeshy with dissolve
        penelope "But these feelings are overwhelming, I can barely see or think straight."
        mc "I-uh… Should I leave?"
        "She looks at me for a few moments with trepidation."
        "Every mare in heat I’ve met so far has been happy to do something sexual with me, but Penelope doesn’t seem to be like that."
        show penelope closesad with dissolve
        penelope "I don’t want you to leave, I’d feel terrible if I made you do that."
        penelope "This heat is so frustrating. My mind’s saying no, but my body is screaming out ‘YES!’."
        mc "Is it really that bad? It sounds awful."
        show penelope closeneutral with dissolve
        penelope "Yeah, but… I can’t bring myself to do it with a guy."
        penelope "The sexual urges may be annoying, but I can mostly ignore them… However, I start feeling extremely lethargic."
        mc "You’re only into girls, then?"
        penelope "Yeah... If only you were a girl, then maybe..."
        mc "Wait a minute… I’ve seen a gender-changing spell before."
        show penelope closeshocked with dissolve
        penelope "G-Gender… changing…? How have I never ever thought about that?"
        penelope "I’m so used to the idea that gender-changing spells are used to change females into males. I’ve never once considered the opposite."
        mc "I can see why, considering how sparse men are."
        show penelope closehorny with dissolve
        penelope "Oh my, I don’t know why... But the idea of you turning you into a girl right now is turning me on way too much."
        penelope "Haha, I can already imagine a cute girl version of you between my thighs."
        mc "You serious? I didn't think you'd be up for it... I dunno if even I'm up for it, obviously I've never had sex as a girl before..."
        show penelope closelaughing with dissolve
        penelope "Come on! You gotta try it as a girl at least once, I promise I'll make it unforgettable."
        "Is she serious about this?"
        penelope "I’m on such an emotional high, I think I’d genuinely cry if you said no."
        if turnedintogirl == 1:
            mc "I’ve already been turned into a girl once, hit me with your best shot."
            show penelope closehorny with dissolve
            penelope "You have? By Moxie? Gosh, how arousing..."
        else:
            mc "I think I want to see what it’d be like having sex as a girl at least once."
            mc "Well, with another girl anyway, I don’t think I could do that with a man."
            show penelope closehorny with dissolve
        label penelopecunnilingus:
            pass
        penelope "Alright, let's do it!"
        hide penelope with dissolve
        "Penny excitedly checks through her shelves for a specific book, ‘big book of sex spells’, that’s certainly an interesting title..."
        show penelope horny with dissolve
        penelope "Perfect, this is any unicorn's must-buy for any sexy fun they might want to engage in."
        penelope "Sex-change, sex-change… Here we go, thirty minutes enough?"
        mc "Is that as high as it’ll go? You wouldn’t want me to change half-way through."
        show penelope shocked with dissolve
        penelope "Hm… That’s a scary thought. Oddly exciting, but scary."
        show penelope horny with dissolve
        penelope "I can get you off at least thrice in thirty minutes easily, are you ready?"
        mc "I can’t believe we’re doing this, but yeah!"
        play sound magic2
        show penelope horny with cum
        "Almost catching me off guard, Penny’s horn flashes, and I feel a surge of magic surround me. Within a painless instant, I find myself miraculously possessing a female body."
        "It takes my mind a while to adjust to the changes."
        "My senses don’t immediately register the addition of breasts or the loss of my male genitalia, but gradually my senses realign."
        show penelope happy with dissolve
        penelope "Theory is, this is the body you’d have if you were born a girl. Your hair is still short though, that’s fine, I like it short."
        mc "What are we going to do?"
        show penelope laughing with dissolve
        penelope "Oh gosh, your voice has even changed…"
        show penelope horny with dissolve
        penelope "I’ve never used a spell like this before... I can’t believe it’s turning me on this much."
        mc "Is this your fetish, or something?"
        show penelope laughing with dissolve
        penelope "I mean... I guess it is now. You seem to have awoken something in me."
        show penelope horny with dissolve
        penelope "Male feminisation, or something?"
        play music sex1 fadeout 30.0
        penelope "Phew, I just… wanna do things to you."
        show penelope closehorny with dissolve
        show penelope closesatisfied with dissolve
        "Penny sits down next to me and takes a commanding lead, bringing her lips towards mine and passionately making out with me."
        "Her experience is immediately clear as her tongue swirls into my mouth and toys around with my own."
        "Feeling all tension drift away from my body, I sink back into the sofa, completely captivated by her kiss."
        "I can feel myself getting aroused in a new and unusual way. I feel a warmth in my pelvis and a tingling sensation."
        "It’s hard to describe these different feelings, all I know is that I want more."
        show penelope closehappy with dissolve
        penelope "Mmphh, ah… How’s your new body?"
        mc "It’s growing on me; I want to see how everything feels."
        show penelope closehorny with dissolve
        penelope "Don’t worry about that, I’m planning on giving you a full tour…"
        show penelope closesatisfied with dissolve
        "She pushes me down on the sofa and crawls on top of me. Wasting no time she sticks her face in my bosom and begins licking one of my nipples, while teasing the other expertly with her fingers."
        "I can begin to feel a growing, throbbing desire in between my legs."
        "Penny swaps her mouth to the other nipple and continues to tease me. I rub my thighs together slightly resulting in a tiny pleasurable sensation, but it only increases my desire to be touched."
        show penelope cunnilingus with dissolve
        play ambience blowjob
        "She grins as she finally goes between my legs. Thankfully she doesn’t tease me anymore, and I feel her tongue immediately lapping up and down the length of my new vulva."
        "It feels so wet and sloppy, but when she focuses on my clit my body is racked with a powerful sensation that causes my back to arch and my eyes to roll back."
        penelope "Warm, wet, soft, and delicious…"
        penelope "*Lick, lick*, *Lick*."
        "This is fucking awesome. Penny’s tongue skillfully pleasures my clit over and over. I have to hold back a few moans with the worry that Lily might hear me."
        "Occasionally I can feel her lips purse around my clit, sucking. Simultaneously I can feel a pressure from her tongue. The combination of sensations drives me wild, my fingers gripping tightly into the sofa cushions."
        "I can’t help but squirm and moan. It feels amazing, and the pleasure keeps rising."
        "It doesn’t just feel like she’s licking my clit, it feels like she’s making out with my pussy."
        show penelope cunnilingus with cum
        "Finally, her skillful tongue work on my pussy pushes me to the edge and I climax."
        show penelope cunnilingus with cum
        "The initial climax is powerful, similar to a male orgasm, however the peak of euphoria drags on for far longer."
        "The euphoria dissipates but the climax continues with heightened sensitivity, each movement of Penny’s tongue fills my entire body with potent pleasure."
        "Overall, the orgasm lasted far longer than a man's would. And while the peak of pleasure was relatively the same, the length of the female orgasm easily bested the two."
        "My head was in the clouds for a few seconds after the powerful orgasm. It took me a few seconds to notice Penny crawling over me like a cougar hunting her prey."
        stop ambience
        show penelope closehorny with dissolve
        penelope "Hope you enjoyed that tour of your new body."
        penelope "However, it’s time for you to explore a different body now."
        show penelope facesitting with dissolve
        "She giggles and straddles my head, giving me a direct view of her aroused vulva. Her lips glistening with a sheen of wetness."
        play ambience blowjob
        "As she slowly lowers herself, I resign myself to pleasure her as much as possible. I may not be as good at cunnilingus, but I want to wow her."
        "I know for a fact she needs no teasing, so I focus on her clit immediately and draw as much pleasure from her as possible."
        penelope "Ahh, that’s the spot, straight away. You really are a good girl."
        "Only a few licks in, I can already hear her breathing turn ragged, and cute gasps escaping her lips."
        "It’s clear to me that she’s burning with desire."
        penelope "*Pant, pant* Mmphhh gosh, my clit is so sensitive!"
        penelope "Ahh, ah… Don’t hold back though, it feels so amazing! Even better than normal!"
        "I swirl my tongue around in circles on her clitoris as she starts to gradually grind back and forth."
        "As her hips move the fur of her thighs pleasantly brush against my cheek, and the grool from her sex drips onto my lips and tongue."
        penelope "Mmphh, that’s perfect. Keep going like that… Ahh, ahh…"
        "As my tongue persists, continuously keeping up the pleasure on her sweet spot, her grinding gradually becomes more needy and vigorous."
        "She applies more pressure onto my face as she drags herself back and forth. Her gasps from earlier dissolving into complete passionate moans."
        penelope "Ahhh, aaaahhhhh… I-I… Aaaaahhhhhhhhhhhh, I’m gonna…"
        "I have to hold her thighs in place as I tactfully suck and lick her moving clit to the best of my ability, even as she wriggles and writhes above me."
        penelope "C-Coming! Aaaahhhhh, aaaahhhhh!"
        "She actually stops grinding and arches her back as she climaxes, allowing me to pleasure her throughout the entire duration."
        stop ambience
        show penelope closesatisfied with dissolve
        stop music fadeout 3.0
        "As she gradually comes to a halt, she lifts herself from my face and crumples down onto the sofa. Her legs seemingly weak as she catches her breath."
        penelope "*Pant* Damn… That was good."
        show penelope closehappy with dissolve
        "I sit up and she notices my face is covered in her wetness, so she graciously pats me down with a tissue."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        play ambience ambiencenight fadein 25.0
        mc "Thank you, I must say it was extraordinary for me too. That orgasm was like nothing I’d ever experienced before."
        show penelope closelaughing with dissolve
        penelope "You’re telling me. You also gave me an orgasm like nothing I’ve ever experienced too."
        show penelope closehappy with dissolve
        penelope "Some odd combination of my heat, combined with your male pheromones and a newly awakened fetish just exponentially stacked on each other."
        show penelope closehorny with dissolve
        penelope "God damn, I wanna do it again, can we do it again? Right now?"
        "B-But the film… Fine, okay, we can do it again…"
        mc "I’d love to, how about a sixty nine this time?"
        show penelope closehappy with dissolve
        penelope "I like your style [playername]. Lay down, I like to be on top."
        scene bg black with dissolve
        "…"
        show bg peneloperoom with dissolve
        show penelope cunnilingus with dissolve
        "The two of us kept at it for a while, I can’t blame Penny either considering she was in heat."
        show penelope facesitting with dissolve
        "I did have the nagging feeling I’d spontaneously turn male at some point during the sex, but Penny kept a close eye on the time."
        show penelope closehorny with dissolve
        "After we both enjoyed our second orgasms she sat back down on the sofa, shortly after I found myself reacquainted with my penis. I must admit, I was starting to miss it."
        show penelope closeneutral with dissolve
        penelope "Mmphh, the spell finally faded... That felt like a long thirty minutes."
        penelope "I can’t believe I just did something so crazy with a guy."
        mc "Crazy is right. I'm a dude that just had lesbian sex."
        show penelope closehappy with dissolve
        penelope "A wild experience for both of us, I’m sure you won’t soon be forgetting it."
        mc "That’s for damn sure, the knowledge of how much better a female orgasm is compared to a male’s is burned into my mind."
        mc "I feel like all my faps will be so empty and hollow from now on, as I always try to reach the high I had on this sofa."
        show penelope closelaughing with dissolve
        penelope "Heheh, you could always reach that high just by visiting me."
        mc "Are you proposing we do this again sometime?"
        show penelope closehorny with dissolve
        penelope "Mmm, maayybe! How about we finish that film before it gets too late?"
        mc "Sure thing, it was starting to get really good."
        scene bg black with dissolve
        stop music fadeout 3.0
        "…"
        play ambience ambiencenight
        show bg worldmapnight with dissolve
        "What a day..."
        "I finished watching the film and I went back to the wagon."
        "I feel like I can’t tell Moxie about anything I did today. Sleeping with a girl she suggested seemed like fair game, but she didn’t mention anything about Penelope or Lily."
        "Penelope is her best friend and a previous lover, how would she feel if she knew that I of all people managed to seduce her lesbian friend?"
        "What about Lily? She and Moxie seem to resent each other in their stubbornness, and she specifically requested that I kept the sex a secret."
        "Yeah, I think I’ll keep all the sex secret. Both Lily and Penny will likely appreciate that."
        show bg moxiewagonlamp with dissolve
        play music wagon
        show moxie closehappyneutral with dissolve
        "When I return it’s just past 5:00pm so Moxie is already back, relaxing on the sofa."
        show moxie closehappy with dissolve
        moxie "Oh, hey [playername]! How was the booooring library shift?"
        mc "Not bad at all, the tea and sophisticated talks were great."
        show moxie closelaughing with dissolve
        moxie "Ahaha, sure it was! But I bet it can't match our talks."
        show moxie closeneutral with dissolve
        moxie "Speaking of talks, Lily, right? Any news on that DNA stuff?"
        mc "Not really, although Lily did reveal that there are no alternate universe versions of me in the surrounding area."
        show moxie closeshocked with dissolve
        moxie "Jeez, all by herself? I can't even comprehend how she did that, I have to admit that’s immensely impressive."
        show moxie closeneutral with dissolve
        moxie "No other versions of you... Well, now I’m just confused, does this mean you're not from another universe like Penny said?"
        mc "Yeah, I’ll be honest, I’m equally confused."
        mc "Although Lily doesn't think I'm from another universe, she thinks the answer is much more 'simple'."
        mc "Lily suggested that if I wanted to make any real progress in the investigation I’ll have to meet with the Royal Sisters."
        mc "Specifically someone called Selene?"
        show moxie closeshocked with dissolve
        moxie "!!!"
        moxie "You’re kidding? I-I need to come with you if that happens!"
        mc "I’m sure you’d be welcome to come."
        show moxie closehappy with dissolve
        moxie "Meeting Selene would be a dream come true! I've always adored her and her works."
        mc "It’s not just a celebrity visit, Lily genuinely thinks that could provide some insight on the situation."
        show moxie closealthappy with dissolve
        moxie "Meh, I know… Do you think you could convince Lily to let me join you two?"
        mc "I’m not sure, I figured you’d ask her yourself."
        show moxie closesad with dissolve
        moxie "Nah, she’d ignore me outright…"
        show moxie closelaughing with dissolve
        moxie "Come on [playername], I’d appreciate it if you convinced her. Pleeeaase?"
        mc "I'll try... I mean, I perfectly understand why you want to be there. After all, it was your spell that started it all."
        show moxie closehappy with dissolve
        moxie "Certainly was, and they’ll see that! They’ll see I created a fully sentient lifeform, or I teleported you from another universe."
        moxie "Oh boy, this could be my big break as the great and powerful Moxie!"
        mc "Ah sheesh..."
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        if livingwithbutters == 1:
            mc "I'm gonna head over to Butters's place for dinner, I'll see you later Moxie."
            show moxie closelaughing with dissolve
            moxie "See ya!"
        scene bg black with dissolve
        "…"
        jump evening
    label libraryvisit2:
        stop music fadeout 3.0
        "Time for another day of work at the library. It seems like the easiest job out of all of them."
        "I barely did anything last time; I honestly wonder how they’re even paying me."
        show bg tree1 with dissolve
        "As before, I have to knock on the door and wait for a reply."
        show bg tree2 with dissolve
        "I get a reply from a window above."
        lily "Hang on, let me just magic the lock."
        show bg library with dissolve
        "I step in and close the door behind me, re-locking it with the latch."
        show bg libraryupstairs with dissolve
        "Feeling comfortable with the environment, I step through the library and make my way upstairs to where Penny and Lily live."
        "As I do, I catch them both talking in the hall."
        play music library fadein 3.0
        show penelope neutral:
            xpos 200
            ypos 30
        show lilyb:
            xpos 700
            ypos 10
        show lily neutral:
            xpos 700
            ypos 10
        with dissolve
        penelope "[playername]? Yeah, they’re here for- Oh, hello!"
        mc "Good morning, how are you two?"
        show lily happy with dissolve
        lily "It was a good morning, now it’s a great one!"
        show penelope laughing with dissolve
        penelope "It’s great to see you [playername], you must be here to see me, right?"
        show lily neutral with dissolve
        lily "N-No way, he came here to see me! We have important tests to do."
        show penelope neutral with dissolve
        penelope "Tests? I think you’re misunderstanding, he’s here to work at the library."
        show lily happy with dissolve
        lily "If he wanted to work at the library, he wouldn’t have come an hour early. Come on Penelope, figure it out."
        "Hour early? God damnit, I accidentally came early again."
        mc "Don’t worry Penny, I’ll hang out with you after Lily."
        show penelope sad with dissolve
        penelope "Hm, right... Right! I’ll be in my room then..."
        hide penelope with dissolve
        stop music fadeout 3.0
        show lily happy with dissolve
        lily "I do have some important things we need to talk about. Take a seat in the lab, I'll make us some drinks."
        scene bg black with dissolve
        "…"
        play music lily fadein 3.0
        show bg librarylab with dissolve
        show lilyb lab
        show lily happy
        with dissolve
        "I sip on some of Lily’s delicious peppermint tea as she rambles about science-y stuff she’s doing."
        "She's very passionate, but I don't really understand it, and it's definitely not relevant to me."
        mc "So this is what you do as the Queen’s student? It sounds fantastic in theory, but surely she’s too busy running the country to work with you."
        show lily neutral with dissolve
        lily "Yeah, that’s the biggest problem I face. Everyone else doing projects at the college have their own full-time supervisors."
        lily "But me? The Queen's busy, so I’m mostly on my own."
        show lily sad with dissolve
        lily "Isn’t that painfully ironic? The most talented student, gets the most prestigious supervisor, yet the result is the least amount of academic support."
        mc "Sounds frustrating. Have you not complained or told anyone about this?"
        show lily satisfied with dissolve
        lily "Heh, I guess not... Making a fuss like that isn't something I do..."
        mc "It's no fuss... Also, it can't help that you're all the way here in this tree instead of in the city, closer to the Queen."
        show lily neutral with dissolve
        lily "It’s part of my field research, the psychological and magical effects of friendship."
        lily "It would seem that certain hormones in the brain can influence magical output."
        label libraryvisit2choice1:
        menu:
            "So... Having friends makes you better at casting spells?":
                show lily happy with dissolve
                lily "Not directly, it’s a correlation not a causation."
                lily "Certain hormones in your brain can increase your magical abilities."
                mc "Being happy makes your magic stronger?"
                show lily laughing with dissolve
                lily "I guess that’s a clever way of looking at it. The better your mental state the more powerful magic you’ll be able to conjure."
                "That just seems like common sense to me."
                jump libraryvisit2choice1
            "Field research? You don’t seem to leave the library.":
                lily "I’ve kinda collected all the data so I’m mostly just writing up and researching at the moment."
                lily "Just between you and I, this project was really simple, so I’ve been spending a lot of time researching and studying my own things."
                lily "I don't get out much, but that's fine!"
                menu:
                    "Why don't you leave?":
                        show lily neutral with dissolve
                        lily "I work here, I get paid, I leave every so often to do food shopping. I have my entire life comfortably in this tree."
                        lily "Why should I leave?"
                        mc "I dunno, to hang out with friends?"
                    "You didn't seem so fine last time.":
                        show lily neutral with dissolve
                        lily "I was grumpier back then."
                        lily "Thanks to you for being my friend, I've been able to cheer up a bit more."
                        mc "I thought you were friends with Penelope and all the friends she's introducing me to."
        lily "You mean like Riku, Butters, Honeycrisp, Ruby and Cream?"
        show lily sad with dissolve
        lily "I wish. I’ve drifted away from a lot of them and they never invite me to anything."
        mc "Can’t you invite someone to do something, or how about make some new friends?"
        show lily neutral with dissolve
        lily "Look, I don’t tell you how to live your life."
        lily "It’s not easy being as shy as I am."
        mc "I was just curious."
        show lily angry with dissolve
        lily "I know, I know. I’m annoyed because you’re right."
        show lily shy with dissolve
        lily "You’re right, and I just seem to be completely unable to do anything about it."
        show lily sad with dissolve
        lily "Like, how do I make friends, where do I even go? There’s no magical friends-making club."
        lily "But at the same time, I’m happy, I’m fine. I tell myself I don’t need friends."
        mc "What about the other girls we just mentioned?"
        show lily neutral with dissolve
        lily "They’re acquaintances, but when was the last time you hung out with an acquaintance?"
        lily "I can’t fathom the idea of just barging into their place and asking them to be my friend."
        lily "It’s hard for me."
        show lily satisfied with dissolve
        lily "At least I’m lucky, I do have Penelope. And then there's you, you're quite an anomaly in my life."
        show lily happy with dissolve
        lily "I hadn’t anticipated a random interspecies male to become one of my close friends, but life can be weird sometimes."
        "I barely know this girl but she thinks we're close friends, that's incredibly sad in a way."
        mc "Isn’t our sudden friendship proof that you have the social abilities necessary to make more friends?"
        show lily shy with dissolve
        lily "*Sigh*, it was never about my abilities, it’s about the irrational wall of anxiety. It mentally prevents me from putting myself in an environment like that."
        lily "I’m the kind of moron that would go to a social gathering and not say a single word."
        show lily sad with dissolve
        lily "I’m scared of what will happen once Penelope leaves, and then you leave."
        lily "What do I do then? I won’t have any friends; I’ll be truly alone. Just a weird science hermit."
        mc "I don’t know…"
        show lily neutral with dissolve
        lily "Even Aurora doesn’t understand me, it must be pretty damn easy to socialise when you’re 3002."
        mc "How often do you actually visit the Queen?"
        show lily shy with dissolve
        lily "Oh? I’m going to visit her soon actually. We meet up once a month, I was going to mention you."
        lily "You probably want to come with me, don’t you?"
        mc "Yeah, but I don’t have a permit to get into the castle."
        show lily surprised with dissolve
        lily "Oh crap, I totally forgot to get you one... I swear I can get you one of those in a heartbeat."
        mc "Do you think you could get one for Moxie too?"
        lily "M-Moxie?! Why would that broad need to get into the castle?"
        if livingwithmoxie == 1:
            mc "You know I live with her… I’m her responsibility."
            show lily angry with dissolve
            lily "Don’t be ridiculous, you’re not her child. You’re uh… What are you?"
            mc "I guess I’m her housemate."
            lily "You can just tell her about your visit in the evening then."
        else:
            mc "She's asked me, she wants to know just as much as I do."
            show lily neutral with dissolve
            lily "Don't be ridiculous, I'm not going to give everyone a permit and opportunity to meet the Queen."
            mc "If you're giving me the opportunity, why not her? She's part of this too."
            lily "Just tell her about your visit when you see her."
        $ calledbitch = 0
        menu:
            "I need to convince Lily."
            "Stop being a bitch and let me bring Moxie.":
                $ calledbitch = 1
                show lily sad with dissolve
                lily "B-b-b-bitch?! That’s really mean."
                lily "If I was an emotional girl, I’d cry right now, and that’d be on you."
                show lily neutral with dissolve
                lily "But I’m not an emotional girl, I’m a logical one, and god damnit you’re right. I am being a bitch."
                mc "Yeah, so… What are you going to do about it?"
                jump libraryvisit2choice2
            "She’s more involved in this than you are, it’s important she’s there with me.":
                show lily sad with dissolve
                lily "Does she mean that much to you?"
                lily "Meh, if I think about this from your perspective it does make sense."
                show lily neutral with dissolve
                lily "She DID bring you into this world…"
                mc "That she did, and we both want to know the how and why."
                jump libraryvisit2choice2
            "Aren’t you looking for friends? Maybe if you drop the ego there’s a chance for you and Moxie to be friends.":
                show lily sad with dissolve
                lily "Friends? Ahh come on, why do you have to hit me where it stings?"
                lily "She put so many people in danger, I bet she didn’t even tell you what happened."
                mc "She did, actually, she was pretty torn up about it."
                mc "Of course she regrets what she did, and she’s working to improve. Doesn’t she deserve your forgiveness?"
                show lily neutral with dissolve
                lily "I told you this before, forgiveness like that takes time. I need to see change before I can take your word for it."
                mc "Bloody hell, how are you supposed to see change if you avoid her at all costs?"
                jump libraryvisit2choice2
        label libraryvisit2choice2:
            show lily shy with dissolve
            lily "Damnit... I’ll think about it, okay?"
        mc "You’re still not convinced? Come on, isn’t there something I can do to convince you?"
        stop music fadeout 10.0
        show lily horny with dissolve
        lily "Something to convince me?"
        if calledbitch == 1:
            lily "You know, you kinda turned me on when you called me a bitch just then..."
        else:
            lily "I dunno, maybe I’m a jealous girl and need some post-nut clarity to think about this one clearly."
        "So that's it? She'll let me bring Moxie if I have sex with her?"
        "As manipulative as that may be, it's a win/win for me."
        mc "Hmm, alright, I’ll bite. What kind of devious tests do you want to conduct on me today?"
        show lily surprised with dissolve
        lily "Tests? Did I say that?"
        show lily happy with dissolve
        lily "I can’t think of any scientific innuendos, but I don’t want to seem like a slut by asking you straight up."
        mc "Since when were you the kind of person that cared what others think?"
        lily "Nah, it’s not about others, it’ll just be me arguing with myself in my head."
        label lilystandingsex:
            pass
        show lily laughing with dissolve
        lily "If I bent over and begged for it, I can hear my conscious already: ’I can’t believe how much of a slut you are.’"
        show lily happy with dissolve
        lily "But, if you took initiative, my inner lady couldn’t refuse your charming gestures. Then you’d have me bent over and begging for it, but it’d be classy instead of trashy."
        show lily horny with dissolve
        lily "... Are you getting any of this?"
        "She raises a good point; most girls around here are taking the initiative when it comes to sex. It’s time for me to make a move."
        mc "Alright I can’t resist your cute ramblings, come over here."
        show lilyb close
        show lily closesatisfied
        with dissolve
        play music sex1 fadein 3.0
        "She timidly takes a few steps closer. When she's close enough, I grab her by the hips and pull her into an animalistic kiss, she reciprocates with just as much passion and aggression."
        "Lily’s pony tongue is larger than mine and often overwhelms my kiss, slipping into my mouth and lewdly toying with my own tongue."
        "As blood starts to rush to my nether, my cock slowly starts to grow. I make a second move. My hand slips between her soft, fluffy thighs and starts to rub her pussy."
        "Her pussy is already wet; I swear during mating season these mares are perpetually dripping with desire."
        show lilyb close:
            xpos 225
            ypos 750
        show lily closesatisfied:
            xpos 225
            ypos 750
        show lilyhandjob:
            xpos 465
            ypos 0
        with dissolve
        "As I rub, she muffles a few moans into our kiss. Her confidence also grows, and she soon returns the favour by giving me a hand job on my now fully erect cock."
        show lily closehorny with dissolve
        "Her clit is so sensitive that eventually she has to pull away from the kiss, finally letting out her moans and ragged breaths."
        lily "Ahh, aahh… It feels so good, so so good… I need more…"
        lily "I want to do it properly this time, the whole thing... Haahh, hahh..."
        mc "Bend over for me like last time and I’ll give you exactly what you want."
        scene bg librarylab with dissolve
        show lilyb sex with dissolve
        "Without an ounce of reluctance, she hurriedly takes off her coat. She then turns around and presents her curvaceous ass to me."
        lily "Please, fuck me. I’ve never wanted anything more than this! I’ll do anything!"
        "This time since I’m in control, I have the opportunity to really appreciate her pussy and how good it feels."
        play sound cum
        show lily sex5 with dissolve
        "I bring my cock to the tip of her pussy and it easily slides in with a lewd schlick. Lily arches her back and lets out a sigh of relief as she’s finally filled up."
        lily "Yesss, that’s it, ohhhh my gosh…"
        play ambience sex
        "I start to slowly move my hips back and forth, fucking her gently and savouring the tightness of her vagina."
        "My cock was as hard as it could be, as every inch was squeezed and pleasured. With each thrust Lily moaned out with joy from the pleasure."
        lily "Ahaahh, aahhhh... It’s really sensitive, but in a good way."
        "Since we're fucking while standing, her legs are together, making her even tighter around my throbbing shaft."
        "The result is ecstasy, beyond amazing."
        "As I looked up at Lily’s face I could tell by her delirious expression that she is enjoying this even more than me."
        lily "Ah- Ahhh! F-Fuck, I think I’m coming already!"
        lily "Haaa, ahhh! Ohhh, ahhh! *Pant, pant*"
        "Even though I was going slowly, I managed to push her over the edge. Her insides started to constrict in rhythmical waves, tightening around the base of my cock, squeezing and sucking tightly."
        "I couldn’t help but fuck her faster in the moment. Her entire body seemingly reacting to each thrust as I constantly moved my hips back and forth."
        "It was at this moment where I was entranced by the way her cute small breasts bounced with each thrust."
        "With a free hand I reached over to grope one, enjoying how soft it felt against my skin."
        lily "Hahhh, haahh… M-My breasts? T-They’re really sensitive…"
        "I enjoy playing with her cute nipple too, it readily becomes erect under my touch."
        lily "Ooohhh, aah… Aah, aaahh!"
        "My thrusts gradually got harder and faster, it didn’t take long for the slapping sound of our hips colliding to echo throughout the wooden room over and over."
        "That combined with the lewd wet noises from our point of contact, spurred me on even more."
        lily "Aahhh, oohhh… I’m close, again!"
        "I could also feel the pressure building as my cock throbbed and shaft tightened. I wouldn’t be able to hold it much longer."
        mc "I’m going to cum inside, is that okay?"
        lily "Yes, yes! Cum inside me [playername]!"
        lily "Let's come together! Haahh, yes! Aah, aaahhh!"
        play sound cum
        show lily sex6 with cum
        play sound cum
        show lily sex6 with cum
        "Cum exploded out the tip of my cock as I relentlessly pounded her pussy."
        "She came too, as she shivered and moaned in ecstasy, I kept pumping her insides with semen."
        show lily sex3 with dissolve
        stop ambience fadeout 3.0
        stop music fadeout 4.0
        lily "Haaa… Haaahh… *Pant* [playername]…"
        "My orgasm eventually faded, and my hips came to a stop. I didn’t immediately pull out, instead she leans back and we embrace for a few moments."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        hide lily
        show lilyb close
        show lily closesatisfied
        with dissolve
        lily "Mmphh, you came a lot…"
        mc "Hard not to when it feels that good."
        show lily closehappy with dissolve
        lily "Hehe… Let’s cuddle on my bed?"
        play ambience ambienceday fadein 3.0
        play music lily fadein 3.0
        scene bg dusklightbedroom
        show lilyb close
        show lily closesatisfied
        with dissolve
        "I pull out and we go snuggle in her cosy bed while we catch our breath and cool down, beads of sweat gradually evaporating."
        "It’s only about 9:30am so I really ought to be careful, lest I fall asleep and miss work, so I keep my eyes open."
        "Lily looks quite beautiful from where I’m lying."
        "With her eyes still closed, she speaks."
        lily "I’ve decided that I’ll let Moxie come."
        mc "Really? Why the change of heart?"
        lily "Because… Moxie brought you here, and you’ve brought me so much happiness."
        lily "I guess if she’s capable of that… Well, she must be an alright person."
        mc "How uncharacteristically illogical of you."
        show lily closehappy with dissolve
        lily "Mmphh… I’m going to try and be more open with people, less shy…"
        show lily closesatisfied with dissolve
        lily "If being friends with someone can be even half as fun and exciting as being friends with you, that’s worth it in my eyes."
        mc "You’re too sweet."
        "I brush my hands through the long sparkling strands of blue and pink hair, as we quietly relax together."
        scene bg black with dissolve
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        "…"
        show bg library2 with dissolve
        "With regret, we soon have to part ways as she returns to working in her lab and I go downstairs to meet with Penelope."
        "She’s only just opening up the library as I arrive, perfect timing."
        show penelope happy with dissolve
        play music library
        penelope "Ah, there you are, great!"
        penelope "I was worried you and Lily were getting to know each other a little too well."
        mc "Hahah, good one. You encouraged me to get her to open up, and that’s exactly what I managed to do."
        show penelope laughing with dissolve
        penelope "Well aren’t you just a person can opener, I’m fairly sure you’ve helped Moxie, me and Lily with our issues now."
        mc "Helped? Nah, you’re overblowing it, I’m just good at listening to people."
        show penelope happy with dissolve
        menu:
            penelope "That you are. Anything you can tell me about Lily?"
            "She doesn’t leave the house because she doesn’t like anyone.":
                show penelope shocked with dissolve
                penelope "Oh goodness, spending all this time cooped up in here has clearly caused her to build resentment."
                mc "I’ve heard of that happening before. The mind can be woefully irrational."
                show penelope neutral with dissolve
                penelope "That it can… Gosh, she isn’t beyond help though, is she?"
            "She’s too shy to talk to anyone.":
                show penelope shocked with dissolve
                penelope "Too shy… That’s quite a surprise, she always holds a conversation quite well."
                mc "She doesn’t seem to have an issue with small talk, but she struggles going out to meet people."
                mc "She feels like she’s drifted too far away from her friends, and any attempt to reconnect would be awkward."
                show penelope neutral with dissolve
                penelope "Those insecurities will eat her away, most people are more than happy to be her friend."
                penelope "Hmm… How can we help her?"
            "She has too much work to have a social life.":
                show penelope shocked with dissolve
                penelope "With her course work? Did she say that?"
                penelope "I dunno, I’m doing a similar course to her and I have plenty of free time. Hence why I’m working in the library."
                mc "She said she doesn’t get much supervisor support, maybe that’s why?"
                show penelope neutral with dissolve
                penelope "Heh, yeah I guess when your supervisor is the Queen there’s not a lot of leeway."
                penelope "Honestly though, it just sounds like an excuse to avoid talking to people. One that she really ought to get over."
        "Come to think of it, the conversation with Lily about her shyness went nowhere. It feels like she’s trapped and can’t find a way out."
        "The only progress I made with Lily is to let Moxie come to the castle, I couldn’t think of anything else."
        $ lilysexuallyrepressed = 0
        label libraryday2choice2:
            pass
        menu:
            "Maybe I can convince Penelope to help."
            "You live in the same building as her, why aren’t you her friend?":
                show penelope shy with dissolve
                penelope "I’d like to think we are, but I can go days at a time without seeing her. It’s crazy to think about."
                penelope "I’m no beacon of confidence myself, I’d feel awkward knocking on her door just to talk. I wouldn’t know what to say."
                mc "Can’t you invite her out somewhere and just talk as friends?"
                show penelope neutral with dissolve
                penelope "I mean I guess, but I just feel like I’d get a resounding ‘no’ if I asked that."
                mc "Hmm… I think you’d be surprised."
                jump libraryday2choice2
            "Lily is sexually repressed and lonely, this is your chance to get a girlfriend!":
                $ lilysexuallyrepressed = 1
                show penelope shocked with dissolve
                penelope "Eehhh…? Giiiiirlfriend?"
                show penelope satisfied with dissolve
                "She quickly regains her composure and her blush disappears as if it was never on her cheeks to begin with."
                penelope "She’s really not my type."
                mc "Pffft, and I am?"
                show penelope laughing with dissolve
                penelope "I mean… As a girl, I guess you were."
                show penelope happy with dissolve
                penelope "It’s different, can we talk about that later?"
                penelope "Anyway! How the hell do you know she’s sexually repressed?"
                "Uh oh, cover story time."
                mc "Aren’t almost all mares sexually repressed?"
                show penelope neutral with dissolve
                penelope "Well that’s kinda what mating season leads to, yes."
                mc "We’re getting distracted, let’s keep on topic here."
                jump libraryday2choice2
            "Could you help her? She needs someone to reach out to her to re-establish friendships.":
                show penelope happy with dissolve
                penelope "Yeah, I think I will."
                penelope "I’ll get the girls together again and invite her out for a few drinks. Do you think she’d like that? She never seems enthusiastic."
                mc "What I think Lily really needs is easy-going, low energy opportunities to hang out and socialise every week or two."
                mc "She’s clearly an introvert, she won’t seek it out, and too much will overwhelm her. But she still needs to socialise."
                mc "A few drinks with friends in a bar sounds perfect for her."
                show penelope laughing with dissolve
                penelope "Perfect! Maybe I can build up her confidence. Once she starts making a few friends, hopefully she can snowball into her own social life."
                mc "I feel like she’s in a position where she’ll definitely make an effort."
        show penelope neutral with dissolve
        penelope "Hey, one more question before we get down to brass tacks."
        mc "Yeah, what’s up?"
        show penelope shy with dissolve
        penelope "You don’t have to answer this if you don’t want, but did you sleep with Lily?"
        if lilysexuallyrepressed == 1:
            penelope "You did say she was sexually repressed; I wouldn’t blame you…"
            "I probably shouldn't have said that, there's realistically no way I should know that unless I slept with her."
        "I'm finding myself lying a lot lately, I can't say I like it."
        mc "Nah, nothing happened between me and Lily."
        mc "She just did a few tests, and we were just talking about getting me into the castle, so we can discuss the whole ‘me being here’ thing with the Queen."
        show penelope happy with dissolve
        penelope "Ahah, sorry for being presumptuous. I know you weren’t in there for long, it was wrong of me to assume you guys would fuck so quickly."
        "Ow, that stung, was it my pride? Am I being a slut? Lavishly sleeping around may get me in trouble one of these days."
        show penelope laughing with dissolve
        penelope "Anyway, let’s get to work, if we finish up today maybe you could come up to my room again? Hehe, for another movie?"
        "Thankfully today is not one of those days."
        scene bg black with dissolve
        stop music fadeout 3.0
        stop ambience
        "…"
        show bg library with dissolve
        "Today I spend most of the day cleaning up the library. Penelope may be planning to do lewd things with me later, but told me she’s going to keep her distance while we work, lest she gets too horny from the pheromones."
        "From the top of the library, I clean up alone. First, I dust the shelves, it’s a pain in the ass having to move the ladder around each time."
        "Despite the monotonous nature, it eventually becomes simple and calming. The hum of soft classic music playing from Penelope’s radio drives me on."
        "It takes hours to dust everything. Once that’s done, I get to have a lunch break before I sweep the entire floor, and mop it."
        "All while Penelope comfortably sits at reception giving me a nonchalant thumbs up for my excellent work."
        "I’m really earning my pay here. So much for the easiest job."
        play music day2
        show penelope happy with dissolve
        penelope "All done? Nice one, here’s your pay."
        penelope "How much does Moxie actually take from you? I mean… You’re not from around here, so you probably don't have much."
        if livingwithmoxie == 1:
            mc "She doesn't actually charge me rent, I guess living in the wagon lowers her overheads."
            mc "I guess I’ll just spend monies on luxury until I have a bigger plan."
            penelope "Got anything in mind?"
        elif livingwithbutters ==1:
            mc "Actually I'm living with Butters, she isn't charging my rent."
            penelope "Is that so? You've gotten yourself a great deal there. Her cottage is one of the oldest houses in the suburbs you know."
            penelope "With all that spare money, what's your plan?"
        $ askedpenelopeformonies = 0
        label libraryvisit2choice5:
        menu:
            "Ask her for more monies." if askedpenelopeformonies == 0:
                "I don’t feel so bad asking Penelope for money, she’s always been helpful and concerned about my plight."
                mc "Hey, do you think I could get some monies?"
                show penelope laughing with dissolve
                penelope "Looking to buy something special? I won’t ask, here."
                "She hands me another 5 monies to go along with my pay."
                $ monies += 5
                $ askedpenelopeformonies = 1
                mc "Appreciate it."
                jump libraryvisit2choice5
            "I mainly have my eyes on gifts.":
                show penelope happy with dissolve
                penelope "That’s really sweet. I bet Moxie is doing a lot for you."
                mc "She certainly is, if it wasn’t for her I’d have nothing in this world."
                mc "You and Moxie have given me everything I could ask for, and more."
                mc "A roof over my head, food, work, and 'stuff' that we don’t need to go into detail on."
                show penelope laughing with dissolve
                penelope "Heh, we care about our own in Arcadia… You're one of us now."
                jump libraryvisit2choice5
            "I have my eye on the spa":
                show penelope happy with dissolve
                penelope "Ohoh, I can see why. You’re really trying to get as much action as you can, I don’t blame you."
                mc "I've never been to a spa like this, it'll be nice and relaxing after all the work I do."
                penelope "Hah, too right. I’ve been to that spa once. Those spa mares know their way around a lady’s body, that’s for sure."
                mc "What service did you get?"
                show penelope laughing with dissolve
                penelope "I went for the oral service, there’s really nothing else there for me."
                show penelope happy with dissolve
                penelope "I heard that they do have a stallion you can pay for, but you know me."
                mc "What kind of services could I get?"
                penelope "You have a few more options; you could probably fuck ‘em for starters."
                show penelope laughing with dissolve
                penelope "If you get a choice of girls, go for the greyish brown one, she’s really giggly and fun."
                mc "I’ll keep that in mind."
                jump libraryvisit2choice5
            "(Conclude)":
                jump libraryvisit2choice6
        label libraryvisit2choice6:
            show penelope happy with dissolve
            penelope "Since you’re around Moxie a lot, I wanted to ask how her studies are going."
        mc "She studies for an hour every evening after dinner. If you were worried that I'm interfering with her studies, it's no worry at all! She's on top of it."
        show penelope neutral with dissolve
        penelope "Only an hour? I was hoping she’d study slightly more than that."
        mc "I think she’s making timely progress; she’s reading this book with an invisibility spell at the moment."
        show penelope angry with dissolve
        "Penny scoffs and shakes her head, taking me by surprise."
        penelope "I keep telling her that field of magic is too advanced for her, she needs to build up her basics first."
        mc "What do you mean?"
        show penelope neutral with dissolve
        penelope "It’s like she’s reading a book on how to run before she can walk. She’ll never be able to do that invisibility spell."
        show penelope shy with dissolve
        penelope "She still struggles to pick up books with her telekinesis, she completely lacks the magical power to turn herself invisible... Right?"
        mc "But she showed me, it was awesome!"
        show penelope neutral with dissolve
        penelope "Showed you? You realize she’s a performer, she’s full of tricks. Are you sure she didn’t just use a cloud of smoke and then reappear in a doorway?"
        show penelope angry with dissolve
        penelope "I mean come on... Invisibility... There's no way Moxie has made that much progress already."
        penelope "I only know a handful of unicorns that come close. It’d take me a year to learn how to do it, it’s not worth it."
        mc "I’m serious. Moxie didn’t turn invisible, she can’t quite do that yet, but she managed to turn partially transparent."
        show penelope shy with dissolve
        penelope "Transparent... I-I... Hmm... Coming from you, someone that doesn't know a lot about magic, that's a surprisingly accurate interpretation."
        penelope "I know I have no reason to doubt you, but..."
        mc "I could see objects through her, it was fantastic."
        show penelope sad with dissolve
        penelope "That’s… so illogical! It’s hurting my head trying to understand."
        penelope "She’s a great friend, but I have to admit she’s a complete amateur at magic, there’s no logical reason she should be able to accomplish such a phenomenal magic feat."
        mc "Maybe she has a greater affinity for that type of magic? She does seem to enjoy studying it."
        show penelope neutral with dissolve
        penelope "Affinity? I don’t know...?"
        penelope "Could Moxie have realized? There's no way..."
        penelope "Sorry, I’m still trying to wrap my head around this. Give me a moment to close up, meet me in my room?"
        mc "Sure thing, see you in a second."
        hide penelope with dissolve
        "She seemed surprisingly irate, I wonder if there's history I'm missing here."
        scene bg black with dissolve
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        "…"
        show bg peneloperoom with dissolve
        "I head upstairs and into Penny’s room, I take a seat on the sofa and look around the room."
        "Damn, she invited me in here so nonchalantly. I know I’m here for sex, but it's so normal to me I don't even think about it anymore."
        "Sex in the morning, sex in the afternoon, sex in the evening."
        "Then there’s me, just going along with everything without question."
        menu:
            "Am I having doubts? Do I feel weird about this?"
            "I’m being too slutty.":
                "Maybe I am."
                "The thing bothering me most about having sex with Moxie, Lily and Penelope is that I’m keeping it all secret."
                "I guess Penelope figured out that me and Moxie are sleeping together, but I doubt Moxie caught on."
                "I don’t like keeping secrets, but there’s more than my ego on the line."
                jump libraryvisit2choice7
            "Everyone’s having fun, it doesn’t harm anyone.":
                "Peace and love! These girls are enjoying themselves just as much as I am."
                "Moxie wasn’t wrong, sex comes far easier in this world than mine."
                "When was the last time I went to a girl’s bedroom and she didn’t fuck me?"
                "Haha, I might act like some kind of player that gets all the girls, but these girls all have me wrapped around their fingers and I don’t even realize it."
                jump libraryvisit2choice7
            "I think these girls are using me.":
                "They’re using me to satisfy their heat…"
                "Moxie said they’re biologically wired, right?"
                "If I think about how animals in heat behaved in my world, a female in heat would seek a male mate."
                "If you throw sentience into this mix, this gives the male the power to choose, the complete role reversal when compared to my world."
                "So here I am in this world, there are girls in heat wanting to mate, and I’m inadvertently never refusing them."
                "It’s like they can’t help but use me. I’m like the fix to a bad addiction."
                "Or… I’m like the cake in the kitchen closet, if I’m there long enough I’ll get eaten."
                "I can’t blame the ladies if I’m putting myself in these situations, that’s for sure."
                "I’m forgetting one thing though; heat only lasts about a month. I wonder how big the difference will be."
                jump libraryvisit2choice7
            "Sex for breakfast, lunch and dinner sounds like the perfect diet to me":
                "All three girls offer something slightly different too. I could get used to this."
                "The lesbian sex is weird, but I think my dick appreciates the break."
                "I’m actually looking forward to doing it again."
                "Hypothetically, if I do end up in a permanent relationship with Moxie, I’ll definitely have to convince her to do this every so often."
                jump libraryvisit2choice7
        label libraryvisit2choice7:
        show penelope closehappy with dissolve
        "At that moment as I’m lost in thought, Penelope arrives with two glasses of juice. I hadn’t realized how thirsty I was until my sips turned into gulps."
        mc "Ahh, thank you Penny."
        show penelope closehorny with dissolve
        penelope "My pleasure... And it'll be our pleasure soon... Hehe."
        mc "I know I touched on this the last time, but I really have to ask why you enjoy what we’re about to do."
        show penelope closehappy with dissolve
        penelope "You mean, lesbian sex, but with a dude? Ahah, I wouldn't want to try describing this to one of our friends."
        mc "You know I’m not a girl, isn't that offputting?"
        show penelope closelaughing with dissolve
        penelope "Maybe you’re not a girl, but you can be, and that’s the best part!"
        mc "Doesn’t that put you off? I could not for the life of me imagine casting a spell on a guy and having sex with them while they’re a girl."
        show penelope closehappy with dissolve
        penelope "Hehe, okay, I totally get what you're saying. But... I actually like it!"
        penelope "How do I describe it… I was thinking about this earlier… It’s like a power fantasy."
        penelope "I love being in control with another girl, but there’s something about reducing a man into a girl, and maintaining that power that just sends my brain into overdrive."
        show penelope closehorny with dissolve
        penelope "Hehehe, the thought makes me feel all gooey and hot."
        mc "And you feel absolutely nothing towards me as a male, right now?"
        show penelope closelaughing with dissolve
        penelope "Not at all, I just want to turn you into a cute girl and eat you up."
        show penelope closehorny with dissolve
        penelope "I didn’t get much of an opportunity to play with you before because it was new to me, and I was getting used to the idea of it."
        penelope "But later that night I was so horny, I started masturbating while thinking about it"
        mc "And what specifically did you think about?"
        penelope "Oh goodness, everything. I want to dominate you, not in a kinky BDSM way, but I want your entire body to submit to me in pleasure."
        penelope "I really want to rub you down there and hear your cute girly moans."
        "This is getting erotic, that combined with the pheromones is causing blood to get flowing down there, although I doubt Penny has any interest in my erection."
        show penelope closeshocked with dissolve
        penelope "Oh jeez, you’re getting an erection."
        show penelope closeshy with dissolve
        penelope "I don't wanna see that, so I’m going to cast the spell now, okay?"
        "I haven’t even agreed to have sex yet and she’s about to cast the gender-changing spell on me."
        "I guess I indirectly agreed when I sat down on this sofa."
        menu:
            "You’re really crazy about this gender-changing thing, aren’t you?":
                show penelope closehappy with dissolve
                penelope "Bahaha, maybe too much, it’s making me a little twitchy."
                penelope "I’m sorry, I hope I’m not being too overbearing."
                mc "Don’t worry about it, you’re just being outspoken, confident and dominant."
                mc "I’ll be honest, I like it, it’s hot."
                penelope "Mmphh, I hear you say that, but it's just not the same when you say it as a guy. You're way cuter as a girl, so I’m going to change you now."
                "Wow, I feel simultaneously shot down and flattered."
            "If I must, I’ll be your cute submissive girl.":
                show penelope closehorny with dissolve
                "Why do I feel strange saying that? It’s not like my masculinity is at risk."
                "I think I get it now; a part of her fantasy is reducing me from a masculine figure to a dainty submissive feminine one."
                "I can’t completely relate to that, but I think I understand why she’s enjoying it so much."
                "What about me, do I enjoy being turned into a submissive little girl to be played with?"
                penelope "Mmm... The things I’m gonna do to you…"
                "Yeah, I think I do."
            "Alright, hit me with your best shot.":
                show penelope closehappy with dissolve
                "I’d be lying if I said I wasn’t excited to have lesbian sex again; this genuinely is an experience of a lifetime."
                "And I’ll take as many female orgasms as I can get, they are terrific."
                penelope "Here we go [playername]!"
        play sound magic2
        show penelope closelaughing with cum
        "Penny’s horn quickly glows as she recants the spell without even needing the book this time."
        "I find myself immediately returning to my dainty female body."
        "It takes a few seconds for my nervous system to readjust, but it’s much faster than last time."
        "There’s something I didn’t notice last time, I’m actually shorter and smaller as a girl. I guess it makes sense, but it’s just one of those things that you don’t think about."
        "At this size, Penelope is actually the same height as me, that’s quite a remarkable difference."
        "As she sits beside me her hands caressing my soft thighs, she continues what she was saying before."
        show penelope closehorny with dissolve
        penelope "So cutie, where were we before? Hehe."
        mc "You were- "
        "Ah, my voice. Right, it’s different."
        label peneloperubbing:
            pass
        mc "You were talking about how you want to hear my cute moans."
        penelope "Ohhh yeah, I have this favourite fantasy in my head right now where both me and my girlfriend are sat on a sofa together."
        mc "Oh, right? Just like us."
        penelope "Mhm, and my girlfriend is laying into the couch feeling submissive and timid, while I lewdly rub her pussy."
        mc "O-Oh my. That’s all?"
        penelope "It sounds simple, right? But in that moment, you are wholly giving your body to me."
        penelope "The simple things really get me going, the slow build-up of tension, the kisses, the rising arousal."
        penelope "Especially that rising arousal."
        "She whispers into my ear with a lustfully sweet tone, as her hands continue to glide over my thighs causing me to coo, and wiggle as I gradually feel my new female body get turned on."
        penelope "Kiss me."
        mc "K-Kiss?"
        penelope "That’s it, that’s the feeling I wanted to capture."
        mc "Huh? What feeling?"
        penelope "That delicate shyness, I’ve turned you from a gruff man into a delicate flower."
        "Hey, I’m not that gruff…"
        menu:
            "Am I?"
            "I am a bit gruff.":
                "I’ve noticed that the gender-change spell subtly changes my personality."
                "However, that could easily be psychological, because I look like a girl, I act how I perceive a girl should act."
                "I don’t see why I would, given the circumstances, but Penelope can see right through me regardless."
                "There’s no point in fighting it, her tongue feels amazing."
            "I can be a delicate flower if I want to be.":
                "Yeah, that’s right… Give into Penelope, just relax. Spread your legs slightly."
        play music sex1 fadein 5.0
        show penelope closesatisfied with dissolve
        "She pushes me down and I can feel her tongue trace the outline of my lips."
        show penelope closehorny with dissolve
        mc "A lick? Is that all?"
        show penelope closesatisfied with dissolve
        "Penny doesn’t wait another second, she surprises me with a sudden forceful kiss of the lips. She soon backs away and observes my reaction."
        show penelope closehorny with dissolve
        penelope "Mmm… I like that."
        mc "Me too… Let’s do it again?"
        show penelope closesatisfied with dissolve
        "Holding both my hands back, she lowers her head and begins to kiss me again."
        "Penelope’s tongue slipped its way into my mouth past my pursed lips."
        penelope "Ahn… hnn… mmm…. ha…"
        "I responded with an equal amount of passion, my tongue twisting around hers."
        "In our overeagerness the wet noises from our kiss were borderline obscene, and our lips began to glisten with a layer of moisture."
        "The intensity of the kiss reminds me of the passion I showed Lily this morning."
        "That primal, animalistic energy as our tongues twirl and toy with each other."
        "This is an exact role reversal of this morning. I had all the control as I dominated Lily, this time Penelope has the control over me."
        "Every few seconds I could feel Penny’s hand gently brush against my thighs,  inching ever closer to my sweet spot."
        show penelope closehorny with dissolve
        penelope "Haah… Hah… Your girly skin is so soft."
        show penelope closesatisfied with dissolve
        "She says before returning to kissing me. The teasing arouses me and the aching feeling between my thighs re-emerges."
        play ambience sex fadein 10.0
        show penelope rubbing with dissolve
        "Finally, Penny’s fingers start to brush against the wet folds of my pussy. Penny pulls away from the kiss as she watches eagerly for my reactions."
        penelope "You’re so warm down there… Already so wet too hehe…"
        "She teases me by lifting her fingers and showing a string of my wetness between them, with a lewd expression she licks off the juices before bringing her finger back to my pussy."
        "Her fingers find and focus my clit. As a woman she certainly knows how to please one."
        "My entire body shivers with that unique pleasure, causing me to squirm under her movements."
        "She speeds up, and before I know it my breath is becoming ragged and I’m struggling to hold back moans."
        "Penny admiring my cute expressions and takes joy in giving me as much pleasure as she can in this situation."
        penelope "If I keep going like this, I’ll make you come…"
        "She’s right, she continues to rub my clit, she doesn’t get faster or harder, yet the pleasure keeps rising."
        "She keeps going, my toes curl and my muscles tense up slightly."
        penelope "I love your cute faces..."
        mc "I-I’m close."
        penelope "You’re lucky that I’m not one for orgasm denial."
        "Her fingers start to speed up slightly, building up intensity and pressure inside me."
        penelope "I’m more of a ‘how many times can I make you come in one session’ gal."
        "I can’t feel anything else, except the electrifying pleasure of Penny’s finger rubbing my clitoris. It radiates all over my body."
        "Before I can even conceptualise what’s happening, the building pressure releases all at once in a powerful orgasm."
        show penelope rubbing with cum
        "Pleasure runs through my entire body in the form of heat and tingling sensations. The orgasm is intense and is coupled with the contraction of my vaginal muscles."
        "My female body squirms with delight as a feeling of euphoria washes over me."
        "The euphoria melts away, leaving a calming feeling of peace and relief that gently washes over me, until I'm back to reality."
        stop ambience
        mc "Mmphh… That was even better than last time."
        show penelope closehorny with dissolve
        "I open my eyes and see Penelope looking smug with bedroom eyes."
        penelope "I think it’s my turn for an orgasm now, isn’t it?"
        mc "Are you going to sit on my face again?"
        show penelope closelaughing with dissolve
        penelope "Actually, I wanted to try something new with you."
        show penelope closehorny with dissolve
        penelope "You may be my cute little plaything, but I want to show you as much as I can."
        mc "Your kindness betrays your inner femme dom."
        penelope "Hmph, I’ll show you. Lay down for me and spread your legs."
        mc "Like this?"
        penelope "Perfect..."
        show penelope tribbing with dissolve
        "She raises herself and straddles my hips in an unusual way that interlocks our bodies. Before I could register what was happening, I could feel a wetness as our girl parts touched."
        play ambience sex fadein 5.0
        "Before I knew it, with my legs spread and at her mercy, she began to grind against me."
        penelope "I’m so horny right now, aahh, aah… I won’t hold back."
        mc "It feels amazing, give it all to me…"
        "Our pussy lips were connected, and with each grind an amazing pleasure swelled through my body making my hairs stand on end."
        "I had heard tribadism was overhyped, but as Penelope and I rubbed our genitals against each other, we were both overwhelmed by pleasure."
        penelope "Haaahh, haah… This is so hot…"
        "Penelope grinded me in an experienced and dominant fashion. Each gyration of her hips rubbed against my clit, and created a building wave of pleasure, just as her rubbing had before."
        penelope "Ahaah, ahhh, I love your body, it’s so cute."
        "I looked up and down Penelope’s feminine body, admiring hers just as she admired my own."
        "I loved the way her perky breasts wiggled around as her hips turned, and her long hair bounced and flowed with the force of her movements."
        penelope "Haah, haah… I-I’m so wet, I don’t think I’ve ever been this wet before…"
        "Her mare pussy is dripping with juice, far wetter than a human pussy. It lubricates our movements, creating lewd noises at our point of contact."
        "Her movements were frantic and frenetic. It was clear she was immeasurably horny and aroused; she couldn’t even contain her moans."
        penelope "Aahhh, aahhh… Your pussy feels way too good!"
        mc "Me too, it’s amazing!"
        "She pushed harder and deeper, determinedly shaking her hips so she could reach her orgasm."
        penelope "Ahhh… I’m getting close, I won’t be able to hold back much longer."
        mc "I’m close too, ahh!"
        "She sped up, the speed and stamina of a mare is unrivalled for a human. Thus I struggled to match the pace of her hips, as they overpowered and overwhelmed me in speed and pleasure."
        "Eventually I slowed down and submitted to her as she continued to ride me. I could feel the pleasure and pressure building in me, about to boil over any second."
        penelope "Aahhh, haahh… I-I’m going to come! Haah, ha, ha… Hnngg…"
        show penelope tribbing with cum
        "It didn’t take long for my climax to release as well, the two of us coming at almost the same time."
        "We kept grinding throughout the length of our orgasms, but as they faded Penny buckled down on top of me"
        stop ambience
        penelope "Haahh… Haah… Haahh…"
        show penelope closesatisfied with dissolve
        "I wrapped my arms around the pinkish mare and cuddled her closely. Her fur was nestled against me, she felt extremely soft."
        show penelope closeneutral with dissolve
        penelope "Haah… Haaah…. Haah- K-Kinda  Haah-overdid it, and tired myself out…"
        mc "How about you let me take over and service you this time?"
        show penelope closesatisfied with dissolve
        penelope "Mmm… Go on then, I’m all yours, love…"
        play ambience blowjob
        "She rolled to her side, and I got between her thighs and kept licking."
        "We loved each other back and forth for half an hour, a long, long half hour."
        "We cuddled, we laughed, we loved, just like a couple."
        stop ambience fadeout 5.0
        "A part of me is sad that this intimate experience is fleeting. Penelope will never be able to see me as she sees me right now, in this moment."
        "But now, I just want to rest in her soft arms and enjoy her presence."
        stop music fadeout 3.0
        scene bg black with dissolve
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        "…"
        show bg peneloperoomnight with dissolve
        play ambience ambiencenight fadein 5.0
        "I must have fallen asleep, when I opened my eyes my body was spontaneously male again and the night sky loomed from out the window."
        "I sighed and rubbed my eyes, thankfully I didn’t feel groggy, I actually feel incredibly relaxed."
        "It was at that moment I realized I wasn’t alone on the sofa. Penelope was napping behind me using me as a little spoon, unfortunately I had outgrown the vacancy."
        show penelope closesatisfied with dissolve
        "I turn as gently as I can and see her cute snoozing face. All the orgasms and grinding must have really tired her out."
        "I could feel myself getting slightly attached to Penny, both as a friend but also as a lover. We shared some sensual experiences together."
        "But what did she really think about me? Am I nothing more than a fantasy for her, a fetish?"
        "I fear that I don’t even want that question answered."
        menu:
            "Should I wake her, or leave quietly?"
            "I need to ask her…":
                pass
            "Leave quietly":
                hide penelope with dissolve
                "As quietly as I can, I lift myself up off the sofa. A wave of melancholy, of emptiness passes over me as I take the final steps out of her room."
                "… Should I really leave?"
                "No… I can’t do it; I can just imagine her waking up alone, confused."
                "In my imagination, she seems really sad for some reason."
            "Wake her up":
                pass
        show penelope closehappy with dissolve
        "I shake her slightly; it takes a few moments and a few shakes, but she soon opens her eyes and smiles softly at me."
        penelope "Mmm… That time already?"
        mc "Afraid so, I’m back to being regular ol’ me."
        penelope "Not as cool as girl you, but equally as sweet."
        "She stretches and groans on the sofa before looking up to me, still with the soft heart-warming smile."
        mc "What are we?"
        penelope "Mm… That’s a subjective question, I haven’t put much thought into it."
        show penelope closeneutral with dissolve
        penelope "Why the sudden question? Is there something on your mind?"
        mc "Yeah… I’m wondering if you like me, or am I just a fantasy?"
        penelope "… I see."
        show penelope closehappy with dissolve
        penelope "I like you, a lot actually."
        penelope "You’re charming, most endearing, and you’re fun to be around too. You also send my pheromones into a doozy."
        penelope "But… I just can’t bring myself to love you."
        penelope "I guess, I turn you into a female, and suddenly there she is. Someone I can love."
        mc "But… That’s only temporary."
        show penelope closesatisfied with dissolve
        penelope "Yeah… I can temporarily turn you into something I can love… But I realize how selfish that seems."
        mc "It’s okay, I understand."
        show penelope closehappy with dissolve
        penelope "No… It’s not okay. If I can’t bring myself to love you for who you are, I shouldn’t be subjecting you to ridiculous magics just to fulfil my own selfish fantasies…"
        mc "You’re acting like I didn’t enjoy every single moment. I came here out of my own volition."
        show penelope closeshy with dissolve
        penelope "Yeah, but you came here for me. I didn’t come here for you."
        penelope "I’m here for the non-existent magical version of you, the version that plays the girlfriend in my fantasies… *Sigh*."
        "Oh jeez, I was the girlfriend in that fantasy?"
        mc "Why me?"
        show penelope closesad with dissolve
        penelope "I… don’t know. You remind me of Moxie, I like her a lot too."
        "I notice her eyes begin to water up slightly as she says that, her voice trails off sorrowfully."
        "This is growing more tragic by the second, I feel a tinge of sadness as she admits to liking Moxie."
        "A few tears roll down her face."
        penelope "I-I’m sorry, I don’t know what came over me."
        hide penelope with dissolve
        "I offer out my arms and we hug. She rests her head on my shoulder. Quietly, we share the moment."
        "I’ve practically stolen her girlfriend, and then in her confusion she rebounded onto me."
        "Shit, what do I do? What do I say?"
        show penelope closeneutral with dissolve
        "While I was lost in thought, Penny had moved back and was now looking deeply into my eyes"
        show penelope closesatisfied with dissolve
        "Before I could say a word, she moved in for a surprising kiss."
        "We had kissed so many times today and this was no different, yet it felt weird, it felt like I shouldn’t be doing it."
        show penelope closeneutral with dissolve
        "After a few drawn out seconds, our lips parted, and she was once again staring deeply into my eyes."
        mc "Why did you kiss me?"
        penelope "I wanted to see what it was like. You know... with a guy…"
        mc "With a guy?"
        show penelope closehappy with dissolve
        penelope "Yeah, hehe… Sorry, it's just not the same..."
        penelope "I think I’m going to leave all this stupid sex and love stuff behind me for a while."
        penelope "I’m going to give myself some time to clear my thoughts and re-explore myself."
        penelope "My heat is nearly over anyway, it started early this half."
        "What a strong girl, I had no idea what to do, yet she’s already figured it all out."
        label libraryvisit2choice11:
        menu:
            "What do you mean by ‘this half?’":
                penelope "I meant this half of the year. Mares go into heat twice a year, I’m assuming that’s just like your species?"
                "Oh, she doesn’t know. I guess I don’t have the time to tell everyone every single detail about me and humans."
                jump libraryvisit2choice11
            "Does this mean we’ll never try the spell again?":
                penelope "The gender-changing? I had a lot of fun; if you’re still around and available, I’d be open to trying it again, but purely for fun."
                penelope "For now though, I need some time for self-reflection."
                penelope "I never was one to get caught up in love and sex, sometimes your emotions can get the best of you."
                mc "You’re certainly right about that, there’s no need to rush into anything."
                penelope "Or rush into nothing for that matter."
                mc "I see what you mean."
                "So she's concerned that she’s growing attached to people like myself and Moxie that she can’t realistically have a relationship with."
            "We all need a break from time to time.":
                show penelope closesatisfied with dissolve
                penelope "Yeah… I need to focus on myself, I’ve got work, studies and friends."
                show penelope closehappy with dissolve
                penelope "Sometimes the brain is a bit weird and irrational when it comes to relationships and love."
                penelope "I’m crushing on people far too easily; I just need to take a deep breath and learn to love myself first."
                mc "You don’t love yourself?"
                penelope "I do, but I still have some growing to do."
                mc "Always trying to improve yourself, you’ve definitely rubbed off on Moxie."
                penelope "Rubbed off on Moxie? She told you that we scissored too?"
                mc "W-What? No!"
                show  penelope closelaughing with dissolve
                penelope "Hahaha, I’m just joking… Or am I? Hahaha."
        show penelope closehappy with dissolve
        penelope "What time is it?"
        "I look around the room but there’s a notable absence of a clock, Penny checks her laptop to see that it’s 4:50pm"
        penelope "Looks like you should get back to Moxie, and I should get some studying done."
        mc "Yeah, I’ve really enjoyed our time together, Penny."
        penelope "Me too [playername], don’t be a stranger."
        scene bg black with dissolve
        "…"
        show bg worldmapnight with dissolve
        if livingwithmoxie == 1:
            "I head back to the wagon, on the way there I think back to the events of today."
        else:
            "I decide to visit Moxie before going home, I need to let her know that she'll be coming to the castle with me."
            "On the way there I think back to the events of today."
        "Lily is going to get Moxie and I a permit so we can meet with the Queen... I feel like I haven't fully appreciated the weight of that action."
        "A regular dude like me, going to meet the Queen... I wonder what'll happen."
        "Does she go into heat too? That'd be the ultimate... Oh jeez, what am I thinking?"
        "Spending time with Moxie has made me a perv, with her 'gotta fuck 'em all' challenge."
        "Although having sex with Lily wasn't one of Moxie's ideas... That shy gal sure is coming out of her shell."
        "Then there's the stuff with Penny. Penny's strong though, there isn’t a doubt in my mind that she’ll be able to bounce back from any low."
        "With my recollection of events complete, I’m also finally at the wagon, stepping inside and greeting Moxie."
        play music wagon
        show bg moxiewagonlamp with dissolve
        show  moxie2 happy with dissolve
        moxie "Good evening [playername]! I just got back."
        "She's always so happy when she sees me, her face goes from resting to a wide smile."
        mc "Hey Moxie, how has your day been?"
        show  moxie2 laughing with dissolve
        moxie "Awesome! My performances went great today."
        show  moxie2 happyneutral with dissolve
        moxie "I’m trying to think of a new trick though."
        moxie "I need to think of a new trick roughly once a week to keep the performance fresh, because I often perform in the same places."
        mc "Oh! How’s your invisibility spell progressing?"
        show moxie2 smug with dissolve
        moxie "I’m glad you asked, check this out!"
        play sound magic2
        hide moxie2 with cum
        "Well fuck me, she vanished before my eyes."
        mc "You are still there, right?"
        moxie "Try me!"
        "I take a step forward and timidly reach out to where Moxie was before, and---"
        "Yep, I can definitely feel her invisible fluffy breast."
        moxie "Hey, it’s too early to start caressing my boobs!"
        show moxie2 shy with dissolve
        "When she reappears, she’s notably a little worn out, as if she’d just sprinted around the wagon."
        mc "Wow, Penelope told me that’s extraordinarily difficult."
        show moxie2 happyneutral with dissolve
        moxie "Mm, you spoke to her about that? I bet she told you I was wasting my time, I can’t wait to prove her wrong."
        mc "She seemed bewildered when I told her you could turn transparent, and now look at you, you’ve mastered the spell."
        moxie "Heheheh, hehe!"
        show moxie2 closelaughing with dissolve
        "She practically hugs me and tackles me at the same time, causing me to fall down onto the sofa and the two of us cuddle."
        show moxie2 closealthappy with dissolve
        moxie "Mmm, thank you for motivating me lately."
        mc "Why are you thanking me? I'm the one in your debt, I couldn’t do anything without you."
        moxie "Even so, you’re one of the best things that has happened to me…"
        "She says as she nuzzles my chest and I stroke her hair."
        show moxie2 closehappy with dissolve
        moxie "You told Penny I could turn slightly invisible, right? What did she think?"
        mc "I don’t know if she entirely believed me. She thought it was too advanced for you."
        show moxie2 closehappyneutral with dissolve
        moxie "She always says that, but I’ve been messing around with these kinds of spells all my life. I’m good with that magic, my mom was too!"
        show moxie2 closealthappy with dissolve
        moxie "But if you find something you’re good at, you’re more likely to stick to it, right?"
        mc "Makes sense to me."
        mc "I also spoke to Lily, she’ll let you come to the castle with me."
        show moxie2 closeshocked with dissolve
        moxie "Ohh, so you went to the library today?"
        mc "Yeah, the conversation I had with Penelope was earlier today."
        show moxie2 closelaughing with dissolve
        moxie "That makes sense, that’s also great news! Thank you, just let me know when you’re going to visit."
        show moxie2 closesmug with dissolve
        "With Moxie on top of me on the sofa, we both realise we're in a somewhat compromising position."
        "Biting her lip, Moxie begins to grind her pussy against my thigh."
        "That along with her 'fuck me' eyes, it's obvious she wants my dick."
        "She always seems to get hornier when she's in a good mood."
        mc "Are you hinting something to me, darling?"
        show moxie2 closehorny with dissolve
        moxie "No hints, I'm seconds away from sliding your cock inside me."
        mc "I’ve been cleaning dust, dirt and grime all day, so I’m going to go shower first."
        show moxie2 closelaughing with dissolve
        moxie "I wondered why you didn’t smell as nice as usual, heheh, joking!"
        show moxie2 closehappy with dissolve
        moxie "Can I come shower too? Hehe, no, no, I showered this morning."
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        if livingwithbutters == 1:
            mc "I'm gonna go to Butters's place and get a shower, I'll see you soon?"
            show moxie2 closealthappy with dissolve
            moxie "You could always have one here, but... I bet her cooking is delicious heh."
            moxie "Come finish me off later, hehehe..."
            scene bg black with dissolve
            "..."
            jump evening
        show moxie2 closealthappy with dissolve
        moxie "You go shower, and I’ll start cooking, it’ll nearly be done by the time you get back."
        mc "Sounds like a plan."
        scene bg black with dissolve
        "…"
        jump evening
    label libraryvisit3:
        "Today’s the big day, I’m going to visit the castle with Moxie and Lily. I hope they don’t bicker too much amongst themselves."
        "Although it’s more likely to be quiet and awkward between us."
        "Moxie has already gone to work, but that’s fine, she's performing near the market today so we can collect her on the way to the castle."
        stop music fadeout 3.0
        show bg tree1 with dissolve
        "I knock on the door and get let in as usual, and make my way up to Lily’s room. I don’t see Penelope on the way."
        show bg library
        show bg libraryupstairs
        show bg dusklightbedroom
        with dissolve
        play music lily fadein 3.0
        show lilyb
        show lily happy
        with dissolve
        mc "Today’s the big day."
        lily "Yeah, I can see why it’d be big for you, but don’t worry about it."
        mc "What time are we leaving?"
        lily "I’d say we should head out in two hours; we’ll be able to catch the Queen before lunch."
        mc "Alright, guess I have nothing to do until then."
        label lilylegsupmissionary:
            pass
        show lily horny with dissolve
        lily "Actually uhh, there's one thing I want to do with you..."
        show lilyb close
        show lily closehorny
        with dissolve
        stop ambience fadeout 10.0
        "She closes the distance and places a hand on my chest, which slowly falls to my pelvis and then my cock."
        lily "I wanna fuck you..."
        mc "Eh? W-What? Already?"
        lily "Yeah, I've been thinking about you all the time!"
        lily "A-and m-my pussy is so wet already!"
        hide lily
        show lilyhandjob
        with dissolve
        "Her lewd words are already causing me to become erect as she jacks me off."
        mc "No build up, no flirting, just sex?"
        hide lilyhandjob
        show lilyb close
        show lily closehappy
        with dissolve
        lily "All I have to do is spread my legs and you can put it in, it's easy!"
        "Awh sheesh, she was an innocent virgin only a few days ago."
        hide lily
        show lilytj
        with dissolve
        "She presses my now erect cock between her thighs and starts to grind against me, I can't help but fondle her cute ass."
        "She used to be so innocent, but now she's a dirty girl that wants to take any opportunity she can to ride my dick."
        mc "Are you always horny in the morning?"
        hide lilytj
        show lilyb close
        show lily closelaughing
        with dissolve
        lily "Yeah, I always wake up with morning dew when in heat."
        lily "And uh..."
        "She lifts up her bedsheets revealing a hidden wet dildo under them."
        show lily closehappy with dissolve
        lily "Somehow you always manage to interrupt me mid-masturbation."
        mc "Alright, lay down."
        play music sex1
        show lily closehorny with dissolve
        lily "Okay, you can do whatever you want to me..."

        show lily missionary1 with dissolve
        "Lily bounces backward on top of her bed with her legs eagerly spread, her drippy pussy shamelessly ready and in view."
        "Lily lays there and waits for me to make my move, while her tail gently sways back and forth."
        lily "I'm ready for you babe, make me your little slut."
        show lily missionary0 with dissolve
        "I lay on top of her and start making out with the cute purple mare as she submissively melts into my kiss."
        "Her hands caressing up and down my chest, and her legs wrap around my waist pulling me in closer."
        lily "Mmm... mmphh… Hnn…"
        "She pulls away from the kiss, and buries her face into my chest."
        lily "I’m ready for you, fuck me hard!"
        play sound cum
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
        play sound spank
        "In addition to my thrusting, I occasionally spank her ass, each time she lets out an adorable squeak."
        lily "Aahh! Yes! I like that babe, mmmm...!"
        play sound spank
        "I knew she’d love the spanking; the quiet ones are always the kinkiest."
        "My thrusts start to come faster, and Lily in her enthusiasm tries to match my thrusts by bouncing her hips up against my body."
        "The effort of both our bodies result in hard, deep thrusts that pleasure every inch of my shaft, and every inch of her insides."
        play sound spank
        show lily missionary4 with dissolve
        "I spank her again and the mare's eyes practically roll back, overwhelmed with pleasure as her hips buck and her pussy dribbles with a few droplets of squirt."
        lily "Aaahhh, ahhh, aaaaahhhhh! I-I'm gonna, I'm gonna cum! Yessss..."
        lily "Aahh… F-Fuck… I-I'm coming! Hnngg…"
        play sound spank
        "The next spank seems to really push her over the edge, her muscles tense up and her pussy tightens. She squirts a bit more onto my cock as she has an extremely powerful orgasm."
        "Now that she's coming, I no longer have to hold my orgasm down, immediately I let down my guard and my hips start to speed up. I couldn't hold back even if I wanted to."
        "I fuck Lily’s wet pussy as fast as I can and my cock starts to throb as my orgasm quickly builds."
        lily "Mmmmm, I want you to cum inside me! Make me your lil' cum dump! Aaahhh, aaaahh…"
        "Eager to fill up this dirty mare's pussy, my cock stiffens and prepares to unload itself as I reach my climax."
        play sound cum
        show lily missionary5 with cum
        play sound cum
        show lily missionary5 with cum
        "I release my load deep into her pussy; my thick, hot cum seeps inside her as I continue to fuck her throughout my orgasm, maximising the brief heightened pleasure."
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
        lily "Mmm, but it could… Heheh…"
        scene bg dusklightbedroom with dissolve
        play music lily fadein 3.0
        "The mare kneels down and cleans up the sexual fluids off my cock using her long, moist tongue. She does it tenderly and passionately."
        "She really has become an obedient little slut in three visits."
        show lilyb close
        show lily closesatisfied
        with dissolve
        lily "Mmphh, mm... *Schlurp*..."
        show lily closehappy with dissolve
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        lily "You know, you could always visit... Maybe, live with me once Penelope moves out?"
        mc "Live with you? What do you mean?"
        show lily closelaughing with dissolve
        lily "Come on, you're not planning on subletting in that wagon forever, are you? You can do better than that, a man like you needs his own space."
        if livingwithbutters == 1:
            mc "Actually, I'm living with Butters right now."
            lily "Yeah, but maybe you'll want your own place sometime in the future."
        else:
            mc "Yeah, maybe you've got a point..."
        show lily closehappy with dissolve
        lily "Get back to me after graduation, we'll figure something out, trust me."
        "She's got a point, I don't even have my own room and possessions yet."
        "Even if I move out of Moxie's wagon, it's not like I can never visit her again."
        show lily closelaughing with dissolve
        lily "Oh, and morning sex! If that's something you'd be interested in."
        mc "More sex? You're crazy."
        "With all this sex lately, it’s taking longer to orgasm and I’m cumming slightly less than before."
        "I might be having too much sex, but that’s not a problem in my book."
        show lily closehappy with dissolve
        lily "We still have about an hour left until we need to leave, could use a spell and do it again, but… I think I’ll check over some work I'll be giving Aurora later, if that’s okay."
        mc "Yeah of course, anything I can do?"
        show lily closeneutral with dissolve
        lily "Um, help yourself to any food or drinks- oh and I have lots of books if you’re looking to pass the time."
        mc "Only books? Don’t you have a laptop?"
        show lily closeembarrassed with dissolve
        lily "M-My laptop? Mm… I guess you can use that if you want…"
        "She seemed to doubt herself for a second, I can only assume that means she has copious amounts of porn on her laptop."
        hide lily
        hide lilyb
        with dissolve
        "Regardless, I spend the rest of the hour on her laptop while she works."
        menu:
            "Snoop around on her laptop.":
                "There is indeed porn on her laptop. Porn shows up in her search bar, in her most visited page, in her favourites and of course saved to her files."
                "I had a little snoop through the stuff, it was mostly vanilla with light bondage themes, quite a lot of distinct species here too, but I’m guessing that’s normal."
                "Unfortunately, it’s mostly male models so I can’t enjoy this much at all. I would have loved to see what a female naga looks like, but all I really learnt is that the male ones have weird looking dicks."
            "Be a good boy and don't snoop.":
                "I don't snoop, but even that can't hide the porn results in her most visited tabs and the search bar."
                "I respect her privacy and don't click any of it, but it explains a lot."
        "With all this porn she views, it's no wonder she's so eager and open about sex."
        "I bet she masturbates more than any other mare I've visited so far. Which is saying a lot, because they’re all horny as heck."
        stop music fadeout 3.0
        scene bg black with dissolve
        show bg arcadiasuburbs with dissolve
        play music day
        "About an hour later, Lily and I collect Moxie from the market and the three of us make our way to the castle."
        show moxie2 neutral:
            xpos 100
            ypos -30
        show lilyb:
            xpos 750
            ypos 30
        show lily neutral:
            xpos 750
            ypos 30
        with dissolve
        "Lily hands me a custom permit to enter the castle, and also gives one to Moxie."
        lily "You better thank me for this one Moxie, you owe me even more than before."
        show moxie2 shy with dissolve
        moxie "I know, I know, of course I thank you."
        "She says as she rolls her eyes, I can tell Moxie is holding her tongue. She probably wants to say something snarky, but she’s trying hard to be above that."
        "The lack of sass even seems to catch Lily off guard."
        show lily surprised with dissolve:
        lily "Hm… Well, you’re welcome… I guess it wasn’t that big of a deal."
        mc "I was going to say, do I owe you too? You’re doing a lot for me."
        show lily shy with dissolve:
        lily "Ehh? Of course you don't... Come on, let’s just go see the Queen, she’s waiting for us."
        hide lily
        hide lilyb
        with dissolve
        "Lily wanders off ahead on her own, Moxie has been by my side almost this entire time, it’s been heart warming to say the least but Lily seems really agitated."
        "I can see why, but her pride means she wouldn’t dare admit that she’s jealous."
        "Moxie takes the chance to whisper in my ear."
        show moxie2 althappy with dissolve
        moxie "Ya nervous?"
        mc "I think so, these castles are so tall they make me feel dizzy."
        show moxie2 shy with dissolve
        stop music fadeout 3.0
        moxie "Mm, me too- about both things."
        scene bg arcadiastreets with dissolve
        pause 0.5
        show bg castlehall with dissolve
        "The three of us pass through a small city street into a large castle courtyard. When we enter the castle, we’re led to a great hall."
        show bg castlethrone with dissolve
        "Sat on a throne at the end of that great hall was none other than the Queen herself, she stands and the three of us bow."
        play music castle
        show aurorab dress
        show aurora happy
        with dissolve
        "Damn, she’s thick."
        lily "Here’s the strange new creature I mentioned in the letter Aurora, what do you think?"
        "Strange new creature? Bloody hell, I wouldn’t call someone I’ve fucked that."
        show aurora laughing with dissolve
        if augustavisit > 0:
            aurora "We've already met, actually."
            mc "You certainly helped me deal with Augusta earlier, thanks your majesty."
            show aurora neutral with dissolve
            aurora "It was not a problem, she was out of line."
            show aurora happy with dissolve
            aurora "Thank you for the letter, Lily... I think your letter evaluated [playername] to be harmless and horny, I have to thank you for such an expert level analysis."
        else:
            aurora "So I’ve heard. I think your letter evaluated [playername] to be harmless and horny, I have to thank you for such an expert level analysis."
        show moxie2 shocked:
            xpos 0
            ypos -20
        show lilyb:
            xpos 900
            ypos 40
        show lily surprised:
            xpos 900
            ypos 40
        with dissolve
        "I can feel both Moxie and Lily’s tails stand on end when she said I’m horny. My tail would be standing on end too, does she know I’ve been sleeping around?"
        show aurora happy with dissolve
        aurora "Hohoh, just one of my juvenile jokes! Don’t mind me, you need a sense of humour at my age."
        show moxie2 shy with dissolve
        show lily happy with dissolve
        "And the vibe in the room returns to normal."
        aurora "Lily, give me the short and simple."
        show lily neutral with dissolve
        lily "Okay, so I've thought about it, and I have a few potential leads... I have them written down here, let me see..."
        show lily happy with dissolve
        lily "Firstly, he arrived when Moxie cast an alleged 'Summon Familiar' spell."
        lily "We had to rethink what the spell actually was, and thus shortlisted it to teleportation."
        lily "Penelope also told me that the teleportation was specific to [playername] and didn’t capture any area around him."
        lily "His DNA was analysed and there were no matches, so my best theory is that he’s from a faraway planet."
        show moxie2 shocked with dissolve
        moxie "Wow… She investigated this better than me…"
        show moxie2 neutral with dissolve
        show aurora satisfied with dissolve
        aurora "Oh Lily, you and your fascination with aliens."
        show aurora happy with dissolve
        "She has a fascination with aliens?"
        "Wait... Does she like to sleep with me because she has an alien fetish?"
        show lily surprised with dissolve
        lily "Am I wrong…?"
        aurora "Moxie, do you have anything to add?"
        show moxie2 shy with dissolve
        moxie "No... Well... Actually, maybe [playername] is from an alternate universe?"
        show lily neutral with dissolve
        lily "Pfft, ridiculous!"
        show aurora satisfied with dissolve
        aurora "Now now, Lily. That theory is no more or less ridiculous than yours of a faraway planet."
        show aurora happy with dissolve
        aurora "Come with me [playername], I have my own theory and some private information pertinent to you."
        show lily surprised with dissolve
        lily "W-What about us?"
        show moxie2 neutral with dissolve
        aurora "This is a private conversation I can have with only [playername], I hope you understand young one."
        aurora "Perhaps later [playername] can fill you in on the details."
        show lily shy with dissolve
        lily "Yes your majesty…"
        show moxie2 shy with dissolve
        "Moxie seems confused and concerned, so I give her a reassuring nod and she returns it with a steadfast expression."
        scene bg castlemirrors1
        with dissolve
        "To my surprise, the Queen takes my hand and leads me up a flight of spiral stairs to a comfortable living quarters, and then further into a strange room with a few blank mirrors."
        "On closer inspection though, these are not mirroring at all, they’re more like monitors showing an image."
        show aurorab dress
        show aurora happy
        with dissolve
        aurora "I believe I have your answer, but I do not think the young ones are ready for such a revelation."
        show aurora laughing with dissolve
        aurora "And I have a good sense that you have not fully disclosed everything you know to them."
        show aurora happy with dissolve
        aurora "If my theory is correct, I honestly do not blame you."
        mc "That is correct, your majesty."
        show aurora satisfied with dissolve
        aurora "No need to be formal, you can call me Aurora."
        show aurora happy with dissolve
        mc "Okay, Aurora."
        aurora "There are two halves to fully solving your situation."
        aurora "The first is the 'Where'. And I believe I have the answer to that."
        aurora "The second is the 'How'. For that, I'll refer you to my sister Selene, she’s far more knowledgeable on bizarre magics."
        mc "What’s the ‘where’, then?"
        show aurora neutral with dissolve
        aurora "Where did you come from?"
        aurora "In truth, your species is not new to me, I have seen it before, but not in this universe."
        mc "Ah- you’ve seen a human before?"
        show aurora happy with dissolve
        aurora "Do you see these mirrors?"
        "She points to the mirror-like objects that are projecting images."
        scene bg castlemirrors2
        with dissolve
        aurora "These are portals to parallel universes."
        show aurorab dress
        show aurora happy
        with dissolve
        aurora "You're not from a distant planet, or another universe."
        aurora "Perhaps you're simply from one of these three parallel universes, and you mistakenly stumbled through."
        mc "That’s crazy, how is that possible?"
        show aurora satisfied with dissolve
        aurora "There are infinite universes, and each of them exists simultaneously."
        show aurora happy with dissolve
        aurora "However, some universes are more similar than others."
        aurora "And the more similar two universes are, the greater the overlap between them, and the smaller the boundary between them."
        aurora "The smaller the boundary, the easier it is for Selene to create a wormhole to that alternative universe."
        aurora "Here we have three very similar universes with wormholes between them."
        aurora "The first portal leads to a near identical world to this one. Every single individual is the same; they’re also ponies too."
        "The portal scans over the world, and I can see a Lily and some other ponies. But to my bewilderment these are actual ponies walking on all fours."
        mc "They’re actual ponies?"
        show aurora laughing with dissolve
        aurora "Indeed, however, they walk on four legs instead of two, similar to the ponies in your world, right?"
        mc "Yeah- yes! How did you know?"
        show aurora happy with dissolve
        aurora "Here, look at this third portal."
        "I look at the third portal and it slowly scans over a different world. It seems more urban and alike my own, but something is off about it."
        mc "Is that Moxie?"
        aurora "Indeed it is. Unlike this universe, and the other pony universe, this third mirror has 'human' creatures like you."
        "I take a closer look at the portal, and there are humans, but they’re many unusual colours."
        mc "Ah… This is a parallel universe with slightly different humans, not my universe."
        aurora "Indeed, there are blue humans, purple humans, every colour you could imagine. These colours resemble that of the mares of this world, such as Lily who is purple in both."
        mc "It looks like a combination of my universe and this colourful pony one."
        aurora "There's more... Look at the mirror in the middle."
        hide aurora
        hide aurorab
        with dissolve
        "The mirror monitors over a city, showing various sights and sounds. It seems like it can locate any point in the world for observation."
        mc "Is that... New York?"
        aurora "I couldn't possibly say. All I know is that it may be your universe, it's full of similar looking humans."
        mc "Yeah, this one looks pretty similar..."
        aurora "There’s more... This universe has another [playername] living there."
        "As Aurora said my name out  loud, the middle mirror swapped to a third person view of another me."
        "Wow... That's definitely me, wearing clothes and living out my old life."
        "Looks like I'm on a date with a girl. I know that girl too, she's called Moxie."
        "I met this 'human Moxie' the day I arrived in Arcadia. Imagine my confusion when I teleport here and there's also a unicorn called Moxie."
        mc "Alive and well I see, hope you kill it out there [playername]."
        mc "Love you man."
        mc "Well... Now I really gotta know, what's going on here? Why am I here?"
        mc "And what does this all have to do with Moxie? This can't be a coincidence."
        show aurorab dress
        show aurora laughing
        with dissolve
        "Aurora can't help but burst out into some light giggles."
        show aurora happy with dissolve
        aurora "Moxie has been quite the nuisance, but I believe my sister is better to explain this."
        aurora "She sleeps during the day, but I’ll give her a lil’ telepathic buzz and wake her up."
        aurora "Come, I shall escort you back to the hall, we have kept the girls waiting long enough."
        play sound magic2
        show aurora happy with cum
        aurora "Oh, and I placed a spell on you so you will be unable to tell them about the mirrors. Those are top secret! But feel free to mention the parallel universe."
        stop music fadeout 3.0
        scene bg black with dissolve
        play music uhoh
        "Aurora escorts me back to the hall and stays with Lily, as Moxie and I are led by a guard to Selene's living chambers."
        show bg castlehall with dissolve
        show moxie2 shocked with dissolve
        "On the way I briefly explain why we’re visiting Selene. Moxie seems absolutely ecstatic to meet her hero."
        show moxie2 neutral with dissolve
        show bg castlehallway with dissolve
        "When we arrive at the living chambers the guards let us in and close the door behind us."
        moxie "Where do we go now?"
        mc "I dunno... I guess even the guards aren't allowed in the living quarters."
        moxie "The Queen must trust us a lot..."
        unknown "You two, come to this room."
        "The two of us hear a friendly voice cordially invite us into a softly lit bedroom."
        hide moxie2 with dissolve
        show bg selenebedroom with dissolve
        "Selene lazily slips out of her massive bed, rubbing some sleep from her eye."
        show moxie2 shocked:
            xpos 125
            ypos -20
        show selene neutral:
            xpos 550
            ypos -40
        with dissolve
        moxie "Oh my gosh, Princess Selene, I am so honored."
        show selene laughing with dissolve
        selene "Hello, are you two the troublemakers that are keeping me up?"
        mc "Afraid so, but we won’t keep you long."
        mc "Oh, by the way, why are we in your bedroom?"
        show selene neutral with dissolve
        selene "That’s because I’m planning on sleeping as soon as you leave. Just trimming the fat of the situation, don’t worry about it."
        show moxie2 althappy with dissolve
        moxie "Okay, we'll trim the fat too, so you can get back to sleep, your majesty."
        show selene happy with dissolve
        selene "I appreciate that."
        show selene neutral with dissolve
        "She stares at us with a patient yet confused expression. Then I realize she's staring at me."
        show selene shy with dissolve
        selene "So... You're the human..."
        selene "This is a first for me, I've never seen a human in this universe before."
        mc "Yeah, Aurora told me that I’m from a parallel universe, meaning Moxie accidentally transferred me from one universe to another."
        show selene surprised with dissolve
        "Immediately upon hearing the universal transfer Selene’s weary eyes snap wide open and she takes a more serious stance."
        show selene angry with dissolve
        selene "Yeah, that definitely sounds like my expertise."
        selene "Shit, pardon the bed hair and grogginess."
        "I’m surprised to hear a princess swear. It’s clear that she’s a lot less regal and a lot more casual than Aurora."
        show selene neutral with dissolve
        selene "Moxie, could you tell me what spell you were trying to cast?"
        show moxie2 neutral with dissolve
        moxie "Of course your majesty, uh, uhm, it was 'Summon Familiar'."
        show selene happy with dissolve
        selene "I haven’t had a situation like this in hundreds of years, I can see why Aurora sent you."
        mc "Is it bad?"
        show selene shy with dissolve
        selene "Bad? I guess not, it's not even urgent. But it’s just my job to deal with these problems."
        moxie "May I ask how you deal with them?"
        show selene neutral with dissolve
        selene "Usually by securing and containing anomalies, in the case that they may be dangerous. Parallel universes can be oddly terrifying."
        mc "Uhh… Am I an anomaly?"
        show selene laughing with dissolve
        selene "Nah, I'm talking real dangerous unexplainable shit."
        show selene happy with dissolve
        selene "If you were dangerous I don’t think Aurora would have waited this long to send you to me. She’s been keeping an eye on you longer than she cares to admit."
        if augustavisit >= 2:
            mc "That explains what happened with Augusta, and also the letter she sent me."
        else:
            mc "That explains the letter she gave me."
        show selene laughing with dissolve
        selene "My sister will only tell you what you need to know. She undoubtedly deemed you safe and moved on, but that doesn’t mean we’re rude enough to refuse to help you."
        label libraryvisit3choice5:
            menu:
                "Could you give me examples of that 'real dangerous unexplainable shit' you talked about?":
                    show selene neutral with dissolve
                    selene "Hmm, well they're all supposed to be classified..."
                    show moxie2 bashful with dissolve
                    "Moxie awkwardly looks at me and then away. Maybe I shouldn't have asked that."
                    show selene laughing with dissolve
                    selene "Haha, no need to look so glum Moxie. I never get to tell people about these things, so I'll tell you about one I dealt with a few centuries back."
                    show moxie2 embarrassed with dissolve
                    moxie "W-What was it?"
                    show moxie2 althappy with dissolve
                    show selene happy with dissolve
                    selene "It was a special vine from an unknown universe, it would initially attach itself to a host like a plant/parasite hybrid."
                    selene "It would eventually replace hair and more with vines, leaves, et cetera."
                    selene "Until eventually the host completely transforms into a plant."
                    selene "Given its extremely high infection rate and nearly infinite lifespan as a plant, it'd eventually consume entire planets."
                    mc "Woah, that's terrifying."
                    show selene neutral with dissolve
                    selene "Don't you think it's kinda cool?"
                    selene "Heh, either way, I think this world has enough dangerous flora without a plant that could potentially infect the entire planet."
                    jump libraryvisit3choice5
                "Why does Aurora know about me, but you don’t?":
                    show selene neutral with dissolve
                    selene "Me and my sister have exceptionally distinct roles to play in this universe."
                    selene "She deals with the people, alteration, and whatever you can see."
                    show selene happy with dissolve
                    selene "I focus on mysticism, the cosmic, and phenomena."
                    show moxie2 happy with dissolve
                    "I can feel Moxie’s eyes light up; she’s hanging on Selene’s every word."
                    jump libraryvisit3choice5
                "Does Aurora know everything?":
                    show selene laughing with dissolve
                    selene "Everything? No, not even close. Her magic is powerful, but all magic has limitations."
                    mc "How would she know about me before meeting me then?"
                    show selene happy with dissolve
                    selene "She keeps track of anything new around Arcadia, she almost certainly noticed a strange creature pop up in her kingdom."
                    selene "I think she always analyses Arcadian newcomers to see if they’re troublemakers or not."
                    "'Harmless and horny'… Right, she must have been the one that analysed me, not Lily."
                    mc "So, she’s always watching?"
                    show selene neutral with dissolve
                    selene "It’s not like she has her eyes trained on everyone at once, she can only watch individuals one at a time."
                    "Come to think of it, the mirrors in the portal room would show certain individuals if they were mentioned, was that a part of Aurora’s magic?"
                    mc "It’s kinda scary how powerful she is…"
                    moxie "It’s not scary at all, it’s a relief that both her and Selene are always protecting us."
                    show selene happy with dissolve
                    selene "We’ve got your back, [playername]."
                    show moxie2 happyneutral with dissolve
                    "She smiles warmly, there’s no insincerity behind that smile. It quells any fears I have about evil rampaging goddesses."
                    jump libraryvisit3choice5
                "So, can you help us? (Proceed)":
                    pass
        show selene happy with dissolve
        selene "Of course. Moxie, you mentioned a 'Summon Familiar' spell, could you tell me which book that’s in? Seems like it may well be the late Midnight’s work."
        show moxie2 althappy with dissolve
        moxie "Yeah, it was Midnight’s third edition."
        selene "Ohh, that’s a valuable one, I didn’t realize the suburbs library had a copy available to the public."
        "With great ease, Selene uses telekinesis to promptly whoosh a book between us."
        "Not only was her telekinesis so quick it caused a slight gust, she had it opened precisely to the correct page."
        show selene satisfied with dissolve
        selene "’Bring forth that which I desire, summon familiar’"
        show selene happy with dissolve
        selene "Bring forth that which I desire, hah, I got it. That ol’ girl and her indolently stuck together spells."
        selene "Unfortunately old dusty spell tomes aren’t entirely accurate. New ones aren’t either for that matter."
        selene "The notes on this spell are more a suggestion than anything, the spell is a melange of a summoning spell and a desire satisfaction spell."
        selene "These two mixed together would ideally result in the summoning of a something that meets your desires"
        mc "That explains why Penelope’s familiar was female..."
        show moxie2 shy with dissolve
        moxie "Wait, so… I wanted [playername], and summoned him as my familiar? That doesn’t explain how he can talk and think."
        show selene neutral with dissolve
        selene "Spells like this are rarely as simple as those spell books make them seem, they’re often multi-layered. I’m certain you know that even slight changes of dialect and magical intensity can change the outcome of the spell."
        selene "As a result, spells are both magical and psychological."
        selene "This ‘summon familiar’ spell is more accurately a ‘bring an object of which I desire to me spell’."
        show moxie2 shocked with dissolve
        moxie "Oh, so it works on other things too?"
        show selene happy with dissolve
        selene "Yes Moxie, if you were to just cast this nonchalantly while you were hungry, maybe it’d give you some food."
        show moxie2 neutral with dissolve
        selene "However if you were to read the book, you’re told that this spell specifically creates a familiar, your psychological state will affect the result of your magic."
        "This is the same stuff Lily is researching! Finally, something I know a little about."
        mc "So just because you think it happens, it does?"
        show moxie2 happy with dissolve
        moxie "That's how all magic works, you need to think about something specific to get the desired result."
        show moxie2 neutral with dissolve
        moxie "But that’s only the psychological aspect, what about the magical aspect? Ponies can only do so much with magic."
        show selene laughing with dissolve
        selene "I’m glad you’re following; with these psychological parameters most unicorns will cast the 'summon familiar' spell, and the limits of their magic will conjure up a blank, brainless familiar."
        show selene happy with dissolve
        selene "This isn’t necessarily what they desire most. But it’s a product of their imagination as much as their magical power will allow."
        selene "But… What if you took away that magical limit and cast the ‘bring an object of which I desire to me’ spell."
        moxie "Without a limit, would the spell aggressively pull any object you desired?"
        selene "Yup."
        show moxie2 shocked with dissolve
        moxie "Then… [playername] was my object?"
        show selene neutral with dissolve
        selene "Mhm, I remember the evening you cast your spell, I could feel that energy."
        show moxie2 shy with dissolve
        moxie "I didn't know I had that kind of magic input within me... That explains why I was so tired that evening..."
        mc "We did end up going to sleep around 10:30pm."
        show moxie2 laughing with dissolve
        moxie "Heh yeah, then we slept for about 14 hours. Even though I was the only one that was tired, I don’t know why you were in there so long."
        mc "What can I say? Your bed was comfy."
        show moxie2 neutral with dissolve
        moxie "Still… I don’t understand why [playername] is from a different universe?"
        show selene happy with dissolve
        selene "That's because this is a specific universe where [playername] doesn't exist, therefore your spell couldn't find a [playername] in this universe."
        selene "So your spell tore a boundary into the closest universe it could, and pulled [playername]."
        show moxie2 sad with dissolve
        moxie "But… That’s absurd, I’m just a regular unicorn."
        selene "It seems that there’s more to you than meets the eye, Moxie."
        show moxie2 shy with dissolve
        moxie "How did I do that… A-And why [playername]? I adore him, but I didn’t even know he existed."
        show selene satisfied with dissolve
        selene "Spells are ignorant to the whims of ponies and humans, they’re objective."
        show selene happy with dissolve
        selene "It doesn’t matter if you know he exists or not, what matters is that you asked for what you desired most, and the spell brought the thing you desired most at that time."
        selene "You two had such a strong bond at that time in other universes that the spell persisted."
        show moxie2 embarrassed with dissolve
        moxie "Well... That makes sense, when I was casting the spell I was thinking a lot about a boyfriend..."
        show selene neutral with dissolve
        "Selene looks at me expectantly. She’s smart, she knows I would have some extra information that could add to the discussion."
        "If there’s anything I’ve learnt from this, it’s that Moxie probably loves me. Although in retrospect she was bad at hiding it."
        "Was she was only letting me sleep with others to keep herself detached and distant?"
        mc "Uhm, I met a human Moxie the day you cast that spell."
        show moxie2 angry with dissolve
        moxie "And you never said?"
        mc "Well, you don't share many similarities other than your name. She doesn't have a mane, blue hair, or purple eyes. She was just a regular human with brown hair."
        mc "It was only a first date, it was such an insignificant moment that I wrote it off as a coincidence that you shared a name, but..."
        show moxie2 neutral with dissolve
        show selene laughing with dissolve
        selene "If I were a betting mare, I'd say if [playername] existed within this universe, you would have met him on that day."
        show moxie2 shocked with dissolve
        moxie "Oohh... So me and him met in all these different universes."
        show moxie2 shy with dissolve
        moxie "And the spell I cast probably realized that?"
        show selene happy with dissolve
        selene "Yeah, in a sense your spell recognized that the Moxies in all the other universes desired [playername], and as a result it attempted to correct the difference between this universe and those by bringing you your own [playername]."
        show moxie2 laughing with dissolve
        moxie "Oho, I get it!"
        show moxie2 althappy with dissolve
        moxie "I'm really sorry [playername], I guess I just really aggressively liked you."
        mc "No kidding..."
        mc "Imagine loving someone so much you pull your perfect match from another universe."
        show moxie2 sad with dissolve
        moxie "Heheh, I still can't believe I did that... Gosh... Am I dangerous? What if I accidentally pull another [playername], or worse?"
        selene "Naturally I'd like to offer my hand to you Moxie, I am extremely interested in your unique magical abilities."
        selene "You seem to have a rare affinity for space time magic, I’d like to find out more."
        selene "Usually only my family members can cast interuniversal magic. You will have to come and see me again, so I can teach you how to control your powers."
        show moxie2 happy with dissolve
        moxie "Really? I’d love to, your majesty!"
        show moxie2 happytears with dissolve
        "Moxie cries tears of joy as the two plan to meet once again."
        "Selene even teases the idea of Moxie becoming her student if she works hard enough, Moxie remains unflinchingly courageous and excited."
        "Moxie’s enthusiasm greatly pleases Selene. It's such a wholesome display, I can't help but smile."
        stop music fadeout 3.0
        scene bg black with dissolve
        "…"
        show bg castlehall with dissolve
        "The two of us leave Selene to her daytime beauty sleep and it’s clear Moxie’s mind is racing."
        play music day2 fadein 3.0
        show moxie2 happy with dissolve
        moxie "Ohhh, this is why I’m so good at the invisibility spell!"
        mc "I’m still wondering just how powerful you have to be to be a universal level kidnapper."
        show moxie2 laughing with dissolve
        moxie "It’s okay, from now on, I’ll use these powers for good, hehe."
        show moxie2 happyneutral with dissolve
        moxie "I want nothing more than to understand what’s so special about me, I’m so excited."
        scene bg black with dissolve
        "..."
        show bg arcadiasuburbs with dissolve
        play ambience ambienceday
        show moxie2 happyneutral:
            xpos 125
            ypos -25
        show lilyb:
            xpos 650
            ypos 30
        show lily happy:
            xpos 650
            ypos 30
        with dissolve
        "The two of us soon meet up with Lily again and we return to the Arcadian suburbs, the three of us slightly livelier than we were on the way here."
        mc "Yeah, so it really was another universe."
        show lily surprised with dissolve
        lily "That’s… Uh, what do I even say to that? The logical part of my brain is screaming."
        mc "That's what the sisters said."
        show lily neutral with dissolve
        lily "I’m intrigued now, I want to see what these other universes are like."
        show moxie2 laughing with dissolve
        moxie "Selene said she wants to see me again, she thinks I have a ton of potential, maybe I’ll even become her student."
        play music prismaserenade fadein 3.0
        show lily angry with dissolve
        lily "Pfft, unbelievable, I’ve worked so hard to be the Queen’s student!"
        show bg mdfight1 with dissolve
        lily "Don't think dumb deus ex magical powers can just skip all that challenging work."
        show bg mdfight2 with dissolve
        lily "I don’t believe it, must be a fluke, some kind of cosmic anomaly."
        mc "Lily you went from trying to be as rational and logical as possible, and now you’re deducing it to a fluke?"
        show moxie2 angry with dissolve
        show bg mdfight3 with dissolve
        moxie "Hmph, I don’t appreciate being undermined. I’ve been an avid fan and reader of Selene’s work since I was a filly."
        moxie "Anyway, the only reason you got the opportunity to be the Queen’s student is because your brother is head of the royal guard, and you have connections."
        mc "Really? Damn I didn’t know that."
        show lily surprised with dissolve
        show bg mdfight4 with dissolve
        lily "Tch, how did you- ah, Penelope told you..."
        lily "Y-You b-b-b..."
        "I take the opportunity to poke Lily and she gets the hint."
        show lily satisfied with dissolve
        stop music fadeout 3.0
        show bg arcadiasuburbs with dissolve
        lily "Fine… I’m being unfair; I’ll give you that."
        show lily happy with dissolve
        lily "Honestly? You’ve done well."
        show moxie2 neutral with dissolve
        lily "You've come a long way since the ursa incident."
        lily "And being recognized by Selene is no light achievement."
        show moxie2 shocked with dissolve
        moxie "You mean it?"
        show moxie2 neutral with dissolve
        show lily laughing with dissolve
        lily "Yeah, clearly you’re doing something right. I don’t really care if it’s just some born talent or arduous work, I’ll support a fellow student."
        show lily happy with dissolve
        lily "Because I’m a superior with more experience, so you’ll need my guidance."
        show moxie2 happy with dissolve
        moxie "That sounds great Lily but… If it’s okay, maybe we could just be friends?"
        show lily neutral with dissolve
        lily "Friends..?"
        show lily happy with dissolve
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        lily "Yeah, a friend sounds great."
        "I'm sure they'll figure out their differences, in time..."
        scene bg black with dissolve
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        "…"
        play music wagon
        play ambience ambiencenight
        show bg moxiewagonlamp with dissolve
        "Moxie and I return to the wagon, rather exhausted we collapse onto the sofa."
        "There isn’t much more than needs to be said after a day like today."
        show moxie closesatisfied with dissolve
        moxie "I'm so tired! We barely did anything but I'm so low on energy."
        mc "Wanna order some food?"
        show moxie closehappy with dissolve
        moxie "Let's get the same pizza from the second night you spent here."
        mc "How romantic, a callback to our first proper meal together."
        show moxie closealthappy with dissolve
        mc "If you do become Selene's student, you're gonna earn bajillions of monies anyway."
        moxie "Awhh yes! Did you see how beautiful Selene's living quarters were? She had a balcony overlooking the entire city!"
        show moxie closelaughing with dissolve
        moxie "That'll be us in ten years!"
        mc "Us?"
        show moxie closeshy with dissolve
        moxie "U-Uhm..."
        show moxie closealthappy with dissolve
        moxie "I guess there's a chance we won't be lovers, and that's okay."
        show moxie closelaughing with dissolve
        moxie "But you'll always be welcome as my roommate, and snuggle buddy, hehe."
        mc "Are you sure? I know how you feel about me now."
        show moxie closeshy with dissolve
        moxie "I mean sure, I like you a lot, but..."
        moxie "Ever since we met I made our relationship pretty clear, we're friends with benefits."
        moxie "I even encouraged you to sleep around with other mares."
        mc "You don't get jealous?"
        show moxie closehorny with dissolve
        moxie "Jealous? Nah... When you get back from work and tell me about all the naughty things you've done... It's kinda hot actually.."
        moxie "Even if we get serious, I'd probably still let you do that."
        show moxie closelaughing with dissolve
        if livingwithbutters == 1:
            moxie "Why do you think I'm so happy letting you live with Butters?"
            moxie "But... Do you wanna stay here tonight?"
        else:
            moxie "You're the alpha after all."
        show moxie closealthappy with dissolve
        "Moxie and I order pizza for dinner, then cuddle on the sofa."
        jump eveningmoxie2
label librarymenu:
        scene bg library2 with dissolve
        stop music fadeout 3.0
        "As usual, Lily lets me into the library using her magic. I'm an hour early so I have an opportunity to spend some time with her."
        show bg libraryupstairs with dissolve
        show bg dusklightbedroom with dissolve
        play music lily fadein 3.0
        if fr == 1:
            show lilyb w
        else:
            show lilyb
        show lily happy
        with dissolve
        lily "Good morning, it's nice to see you again. Want to talk about something?"
        menu lilymenu:
            "Talk" if lilytalks == 0:
                jump lilytalk
            "Sex" if lilysex == 0:
                if fr == 1:
                    show lily horny with dissolve
                else:
                    show lily horny with dissolve
                lily "Oh? You wanna fuck? I'll be your slut any time, babe."
                jump lilysex
            "Work at the Library":
                $ monies += 25
                if lilysplitsex == 0 and fr == 1:
                    $ lilysplitsex = 1
                    "You found a secret scene! Requirements met: Beat Morrigan and work at the library."
                    lily "[playername], do you think you can work with me today? I’ll pay you the same rate as Penelope."
                    lily "I could really use a second pair of hands to help me with some things today. A bit like a personal assistant. I’ll make it easy for you."
                    mc "Sure thing, what do you need?"
                    show lily laughing with d
                    lily "Yeah, let’s begin right away! First thing is…"
                    scene bg black with d
                    jump lilysplitsex
                jump penelopework
            "Leave":
                if fr == 1:
                    show lily neutral with dissolve
                else:
                    show lily neutral with dissolve
                lily "Leaving so soon? Have a good day [playername]!"
                if fr == 1:
                    jump prefinalworldmap
                jump preworldmap
label lilytalk:
    menu:
        "Ask her why she's gotten so sexual lately":
            mc "Hey Lily, can I ask you a personal question?"
            show lily surprised with dissolve
            lily "Oh, of course, I'm happy to answer anything."
            mc "I don't think it'd be vulgar to say you've gotten a lot more sexually confident around me, right?"
            show lily laughing with dissolve
            lily "Uhhmm, I think so! I enjoy being your little slut."
            mc "You remember how shy you were the first time, right?"
            show lily neutral with dissolve
            lily "Vaguely... It's normal to be shy on your first time!"
            mc "And you got that confident because you really enjoyed sleeping with me?"
            show lily horny with dissolve
            lily "Ohoh yes!"
            mc "Does your enjoyment have anything to do with the fact I'm interspecies, and perhaps, 'alien'?"
            show lily embarrassed with dissolve
            lily "Y-yeah... A lot to do with that..."
            show lily happy with dissolve
            lily "I've been schlicking to interspecies porn for as long as I can remember, female pony on anything."
            show lily laughing with dissolve
            lily "But then I found a world of art, where it was female pony with aliens, and monsters! It was so hot!"
            show lily happy with dissolve
            lily "Now that stuff is my go-to for masturbating."
            mc "Art, you say?"
            show lily sad with dissolve
            lily "Y-You don't think that's weird, do you?"
            mc "Not at all, I think it's perfectly normal. I do it too sometimes."
            show lily happy with dissolve
            lily "Awhh, this is why you're so cool [playername], you're like a living, breathing fantasy."
            show lily horny with dissolve
            lily "We're such a good match."
        "Ask her what kind of porn she likes":
            show lily horny with dissolve
            lily "You wanna see? Maybe we can look at some porn and have sex after."
            mc "If we have time, sure."
            if fr == 1:
                show lily happy with dissolve
            else:
                show lilyb close
                show lily closehappy
                with dissolve
            lily "Okie well, come over here to my desktop."
            "She sits down at her computer chair and opens up a folder in her documents named 'important work', it's full of finely curated, high quality porn."
            lily "These are my favourites, anything I could get myself off to goes in here."
            mc "Well I'll be, you're a big fan of... dicks."
            if fr == 1:
                show lily horny with dissolve
            else:
                show lily closehorny with dissolve
            lily "Hehe of course I am..."
            mc "What kind of fetishes do you have saved on here?"
            lily "Ohh, all sorts... We have interspecies of course, but there's also alien stuff."
            lily "Egg laying/oviposition, some hyponosis... Facehuggers, but not guro!"
            mc "Is that one there incest?"
            if fr == 1:
                show lily embarrassed with dissolve
            else:
                show lily closeembarrassed with dissolve
            lily "N-NO! Those two aren't related!"
            "She scrolls down to hide a certain picture where the word 'sis' was mentioned."
            lily "Eh-hem, anyway..."
            mc "Are those... Insects? That's pretty hardcore..."
            if fr == 1:
                show lily sad with dissolve
            else:
                show lily closesad with dissolve
            lily "Uuu, maybe showing you this was a bad idea... I forgot how fucked up some of these pics are to normal people..."
            mc "You can enjoy whatever you want to enjoy, I won't judge."
            if fr == 1:
                show lily embarrassed with dissolve
            else:
                show lily closeembarrassed with dissolve
            lily "It-It's only a fantasy! W-Wait no, not even that! I just appreciate the art!"
            mc "Right, right. I get it, it's just art."
            lily "Mhm, mhm!"
        "Talk to her about the other girls":
            mc "As far as I'm aware, you're friends with the other girls I'm working with, right?"
            mc "That's how Penelope met them in the first place."
            mc "So why aren't you closer friends with a lot of them anymore?"

            show lily neutral with dissolve
            lily "You mean Honeycrisp, Ruby and a few others?"
            show lily happy with dissolve
            lily "The six of us used to be close friends back when we were all younger, we'd do things almost every day."
            lily "But we got older, burdened by responsibilities, and slowly drifted away."
            lily "Some of them still hang out, but it's a weekly affair..."
            show lily neutral with dissolve
            lily "For a while I isolated myself a lot, you know about that."
            show lily happy with dissolve
            lily "But thanks to your encouragement I'm reaching out to them again."
            show lily neutral with dissolve
            lily "It's not easy for me, everyone else has an important job, like running a bar or shop."
            lily "But for me, I'm often cooped up in the lab and on my computer for eight hours a day."
            show lily laughing with dissolve
            lily "Penelope is helping me by organising evening meet-ups at the bar, it'll be like all those years back..."
            show lily neutral with dissolve
            lily "Sorry to bore you with that long rant, I got lost reminiscing."
            mc "That's okay, I'm really happy to hear you're challenging yourself again."
            show lily happy with dissolve
            lily "Mhm, I got so stuck in my own comfort zone, it ended up shrinking into a tiny bubble."
            show lily laughing with dissolve
            mc "And then I came in and popped it, right?"
            lily "Exactly!"
        "Ask her about being the Queen's student." if fr == 0:
            mc "So... There's an elephant in the room that I've wanted to discuss, but I've never really found a good way to ask about it."
            show lily surprised with dissolve
            lily "What's that?"
            mc "Why exactly are you the Queen's student?"
            show lily neutral with dissolve
            lily "Well uh, apparently it's potential..."
            mc "Potential?"
            show lily shy with dissolve
            lily "I'm supposed to become an alicorn, but... It's so hard!"
            mc "Wait, you're going to become one of those immortal goddesses?"
            show lily neutral with dissolve
            lily "Yeah, that's what I'm studying for, in legends there was a spell that could turn a regular unicorn into an alicorn."
            lily "The Queen put me in charge of discovering that spell, she believes I'm the only unicorn that could do it."
            show lily sad with dissolve
            lily "But I'm at a standstill, and it feels like I'm missing something, I've been running around in circles with that mystery for almost a year now."
            lily "Aurora keeps telling me to take a break and see my friends instead, maybe she's right, maybe I'm overworking myself."
            show lily neutral with dissolve
            lily "But that's just the kind of mare I am."
            mc "I don't know much about magic, but I know overworking yourself deteriorates the quality of work."
            mc "Work from nine to five, sure, but after five? That's you time."
            mc "And yeah, you should spend some of that time with friends, even if you're an introvert."
            mc "It's extremely healthy just to spend a little bit of time with good friends every week."
            show lily happy with dissolve
            lily "So... I need to increase my quality of life to improve my quality of work."
            mc "Absolutely, high achievers often have a balanced work and social life."
            lily "Any personal advice?"
            mc "Well, you like books right? Read a book on it."
            lily "Ohh, good idea!"
        "Back":
            jump lilymenu
    $ lilytalks = 1
    if fr == 1:
        show lilyb w
    else:
        show lilyb
    show lily happy
    with dissolve
    jump lilymenu
label lilysex:
    menu:
        "Thigh-Fuck":
            stop music fadeout 3.0
            stop ambience fadeout 3.0
            lily "I want you to slide your cock between my legs and fuck my thighs."
            hide lily
            hide lilyb
            show lilytj
            with dissolve
            play music sex1
            play ambience sex
            "Before I can even comprehend her lecherous words, the cute purple mare takes charge by straddling my cock between her thighs."
            lily "Mmphh, look how wet my pussy is already, I'm just aching for your cock..."
            lily "Hehe, you always make me horny [playername], you're my ideal lover."
            "She stands on her tippy toes and positions herself against my chest. My shaft is comfortably nestled between her warm thighs and dripping wet vulva."
            lily "Ooo, I feel like I could melt when I'm this close to you."
            "She pushes me against a wall and leans on me with the sexual aggression of a mare in heat."
            "Her hips gently gyrate against my shaft. It’s such a subtle motion that it seems subconscious."
            lily "Ohh fuck yeah, make me your little slut."
            "Her arms wrap behind my back as she nuzzles my chest and grinds against my erection in a lewd embrace."
            lily "Haahh, this feels so good... I love squishing your dick between my thighs."
            mc "You're such a dirty girl."
            "Her slow and methodic thrusts are tight and pleasureful as she smoothly glides her wet folds up and down against my erection."
            "Her thighs are also immensely soft and furry, it’s like a soft, erotic hug around my cock."
            lily "You've really brought out the slut in me [playername], I feel like I can do, and say anything to you."
            "She starts rocking back and forth quite fast now, she’s really getting into it."
            "The tightness of her thighs combined with her speed feels surprisingly good. Especially as her wetness drips down my cock."
            lily "Ahhh… [playername], I can feel you throbbing, I want you to cum for your naughty little slut."
            "Her movements are silky smooth as her hips gyrate up and down my shaft. Even faster now."
            "She sinks her head back into my chest and continues to grind against my shaft."
            lily "Mmphh, my pussy feels so good."
            "She starts to rub her clit as she bounces against my pelvis, with more recklessness by the moment."
            "Passion rises and so does my orgasm, as I get closer and closer to cumming."
            lily "Ahh, ahhh, I'm gonna come baby, cum with me! Ahhh, ah!"
            play sound cum
            show lilytj with cum
            play sound cum
            show lilytj with cum
            "A pressure builds in my loins as a surge of pleasure overwhelms my senses and thick loads of jism splurt between Lily's thighs."
            lily "Ahh… Aaaaahhhh, ahhhhhhhh… Haahh… hahh… Gosh… Hah…"
            stop ambience fadeout 2.0
            stop music fadeout 3.0
            scene bg dusklightbedroom with dissolve
            if fr == 1:
                show lilyb w
            else:
                show lilyb
            show lily happy
            with dissolve
            lily "Mmphh... Fuck..."
            lily "Ehehe, hehehe, it's going to be a productive day today."
        "Standing Sex view from Behind":
            stop music fadeout 3.0
            stop ambience fadeout 3.0
            lily "You know what I really enjoyed? When you took me from behind while we were standing."
            lily "There's something so primal and aggressive about it, makes me swoon."
            play music sex1
            mc "Primal? Alright, let's do it."
            if fr == 1:
                show lily satisfied with dissolve
            else:
                show lilyb close
                show lily closesatisfied
                with dissolve
            "She timidly takes a few steps closer and just as she gets close, I grab her by the hips and pull her into an animalistic kiss which she reciprocates with just as much passion and aggression."
            "Lily’s pony tongue is larger than mine and often overwhelms my kiss, slipping into my mouth and lewdly toying with my own tongue."
            "She's definitely gained a lot of confidence in our sexual skirmishes."
            "As I make a second move, my hand slips between her soft, fluffy thighs and starts to rub her pussy. She responds by slipping a hand to my erection."
            hide lily with None
            if fr == 1:
                hide lilyb
                show lilyb w:
                    xpos 0
                    ypos 30
                show lily satisfied:
                    xpos 0
                    ypos 30
                with dissolve
            else:
                hide lilyb
                show lilyb close:
                    xpos -150
                    ypos 65
                show lily closesatisfied:
                    xpos -150
                    ypos 65
                with dissolve
            show lilyhandjob with dissolve:
                xpos 465
                ypos 0
            "As I rub, her pussy is already wet; I swear these mares are perpetually dripping with desire."
            "Her clit is so sensitive that eventually she has to pull away from the kiss, finally letting out her moans and ragged breaths."
            if fr == 1:
                show lily horny with dissolve
            else:
                show lily closehorny with dissolve
            lily "Ahh, aahh… It feels so good, so, so good… I want you to take me now."
            mc "Bend over for me like last time and I’ll give you exactly what you want."
            scene bg dusklightbedroom with dissolve
            if fr == 1:
                show lilyb wsex
            else:
                show lilyb sex
            with dissolve
            "Without an ounce of reluctance, she turns around, presenting her curvaceous ass to me."
            lily "Please, f-fuck me. I'm addicted to your thick human cock."
            play sound cum
            show lily sex5
            with dissolve
            "I bring my cock to the tip of her pussy and it easily slides in with a lewd schlick. Lily arches her back and lets out a sigh of relief as she’s finally filled up."
            lily "Yesss, that’s it, ohhhh my gosh…"
            play ambience sex
            "I start to slowly move my hips back and forth, fucking her gently and savouring the tightness of her vagina."
            "My cock was as hard as it could be, as every inch was squeezed and pleasured. With each thrust Lily moaned out with joy from the pleasure."
            lily "Ahaahh, aahhhh... It’s really sensitive, but in a good way."
            "Since we were fucking while standing, her legs weren’t far apart making her even tighter around my throbbing shaft."
            "The resulting pleasure is ecstasy, beyond amazing."
            "As I looked up at Lily’s face I could tell by her delirious expression that she is enjoying this even more than me."
            lily "Ah- Ahhh! F-Fuck, I think I’m coming already!"
            lily "Haaa, ahhh! Ohhh, ahhh! *Pant, pant*"
            "Even though I was going slowly, I managed to push her over the edge. Her insides started to constrict in rhythmical waves, tightening around the base of my cock, squeezing and sucking tightly."
            "I couldn’t help but fuck her faster in the moment. Her entire body seemingly reacting to each thrust as I constantly move my hips back and forth."
            "I'm entranced by the way her cute small breasts bounce with each thrust."
            "With a free hand I started to massage them, lifting them and rubbing them."
            lily "Hahhh, haahh… M-My breasts? T-They’re really sensitive…"
            "Even though they're small, they're incredibly soft, I enjoy playing with her cute nipples too, both of which are erect."
            lily "Ooohhh, aah… Aah, aaahh!"
            "My thrusts gradually get harder and faster, and it doesn't take long for the slapping sound of our hips colliding to echo throughout the wooden room over and over."
            "That combined with the lewd wet noises from our point of contact spurred me on even more."
            lily "Aahhh, oohhh… I’m close, again!"
            "I could also feel the pressure building as my cock throbbed and shaft tightened. I wouldn’t be able to hold it much longer."
            mc "I’m going to cum inside, is that okay?"
            lily "Yes, yes! Cum inside me, [playername]!"
            lily "Let's come together! Haahh, yes! Aah, aaahhh!"
            play sound cum
            show lily sex6 with cum
            play sound cum
            show lily sex6 with cum
            "Cum exploded out the tip of my cock as I relentlessly pounded her pussy."
            play sound cum
            show lily sex6 with cum
            play sound cum
            show lily sex6 with cum
            "She came too, as she shivered and moaned in ecstasy, I kept pumping her insides with semen."
            stop ambience fadeout 3.0
            stop music fadeout 4.0
            lily "Haaa… Haaahh… *Pant* [playername]…"
            "My orgasm eventually faded, and my hips came to a stop. I didn’t immediately pull out, instead she leans back and we embrace for a few moments."
            scene bg dusklightbedroom with dissolve
            if fr == 1:
                show lilyb w
            else:
                show lilyb
            show lily happy
            with dissolve
            lily "Mmphh... That was really good..."
        "Legs-Up Missionary":
            stop music fadeout 3.0
            stop ambience fadeout 3.0
            lily "I wanna fuck you..."
            mc "How do you want to do it?"
            lily "It felt really good when you were pounding me on the bed..."
            mc "Missionary? Let's make it more interesting and lift your legs up, your pussy gets even tighter then."
            lily "And your dick fills me up even more, ehehe."
            play music sex1
            if fr == 1:
                show lily horny with dissolve
            else:
                show lilyb close
                show lily closehorny
                with dissolve
            lily "Okay, you can do whatever you want to me..."
            show lily missionary1 with dissolve
            "Lily bounces backward on top her bed with her legs eagerly spread, her drippy pussy shamelessly ready and in view."
            "Lily lays there, waiting for me to make my move, while her tail gently sways back and forth."
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
            "And since her thighs are up like this, her pussy feels even tighter, making the sex feel even more amazing for the both of us."
            lily "Mmphh, I bet you like my tight pussy, don't you?"
            "My cock is throbbing and she can barely contain the pure pleasure and desire she feels, as she squirms on the bedsheets."
            play sound spank
            "In addition to my thrusting, I occasionally spank her ass, each time she lets out an adorable squeak."
            lily "Aahh! Yes! I love that babe, mmmm...!"
            "The quiet ones are always the kinkiest."
            "My thrusts start to come faster, and Lily in her enthusiasm tries to match my thrusts by bouncing her hips up against my body."
            "The effort of both our bodies result in hard, deep thrusts that pleasure every inch of my shaft, and every inch of her insides."
            play sound spank
            show lily missionary4 with dissolve
            "I spank her again and the mare's eyes practically roll back, overwhelmed with pleasure as her hips buck and her pussy dribbles with a few droplets of squirt."
            lily "Aaahhh, ahhh, aaaaahhhhh! I-I'm gonna, I'm gonna come! Yessss..."
            lily "Aahh… F-Fuck… I-I'm coming! Hnngg…"
            play sound spank
            "The next spank seems to really push her over the edge, her muscles tense up and her pussy tightens. She squirts a bit more onto my cock as she has an extremely powerful orgasm."
            "Now that she's coming, I no longer have to hold my orgasm down, immediately I let down my guard and my hips start to speed up. I couldn't hold back even if I wanted to."
            "I fuck Lily’s wet pussy as fast as I can and my cock starts to throb as my orgasm quickly builds."
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
            lily "Mmm, but it could… You just need to visit me every morning, hehe."
            hide lilyb
            hide lily
            with dissolve
            play music lily fadein 3.0
            "The mare kneels down and cleans up the sexual fluids off my cock using her long, moist tongue. She does it tenderly and passionately."
        "Standing Sex view from in front" if fr == 1:
            lily "Yes, yes! I love the sound of that!"
            show lily ssex1 with dissolve
            play music sex1
            "Without a second thought, the horny mare jumps up from the bed and leans over a counter, wiggling her dripping crotch in my direction, her tail fluttering back and forth excitedly."
            lily "I want you to bend me over and fuck me silly!"
            "Watching such a lustful display causes me to easily get an erection. I only uttered the word and she just assumed the position..."
            "I could get used to this, Lily would be great girlfriend material, and a future princess too!"
            mc "Hmm... You make a good argument."
            lily "Hey, hey! No teasing!"
            mc "Heh, I'm only teasing myself if I wait."
            "I close the distance and prod the tip of my cock against her wet labia, not willing to waste any more time than I need to."
            lily "Mmphh, I hope my pussy is still nice and tight for your thick cock!"
            mc "Just as tight as the first time, cutie."
            play sound cum
            show lily ssex2 with dissolve
            "I thrust my hips forward, plunging my cock into the depths of her tightness in an instant."
            "Lily coos and starts to rhythmically grind her butt back and forth playfully, as her pussy eases to the girth of my cock."
            play ambience sex fadeout 2.0
            "Knowing she has a growing kinky side, I give her a playful spank on the ass, she yelps and I start to pound her pussy."
            lily "Hahh! S-So eager! I hope my t-taaaaahhh, ahhh!"
            "The pleasure overrides her ability to talk, any attempt at words is replaced with a lustful moan."
            lily "Gaahh, I love it when you're roughhhhhh!"
            "Lily's pussy feels almost too good, and her technique has even been improving slightly."
            "She's contracting and squeezing her insides around my cock similarly to how Ruby does; I wonder which book she must have learnt this from?"
            "With this added technique Lily’s tight pussy easily brings me close."
            "My cock grows tighter and harder as it throbs in her clenching pussy."
            "She’s been indulging in light orgasmic pleasure repeatedly during the entire session. Her squelching pussy is dripping with an overabundance of juices and lust."
            show lily ssex3 with dissolve
            lily "Hahhh, you’re getting even harder! Y-You’re gonna make me come!"
            "Lily’s pussy tightly clenches around my member, rhythmically increasing the pleasure with each passing second."
            "I grit my teeth and pull on her tail as a familiar feeling in my taint signals an impending orgasm."
            play sound cum
            show lily ssex4 with cum
            play sound cum
            show lily ssex4 with cum
            "With a few last deep thrusts my cock finally releases its load deep into her vagina and womb."
            play sound cum
            show lily ssex4 with cum
            play sound cum
            show lily ssex4 with cum
            stop music fadeout 5.0
            stop ambience fadeout 5.0
            lily "Kyaaaahhhh, I want you to breed me like the slut I am! Fill my belly with your cum!"
            "Satisfied, I pull out and leave Lily panting on the counter as she continues to enjoy her longer orgasm."
            show lily ssex5 with dissolve
            lily "Ohhh, sheesh, I just said something really embarassing right now..."
            lily "And... It was totally hot, I'd definitely say it again, hehe..."
            "Damn, what a character arc Lily has had."
        "Back":
            if fr == 1:
                show lily happy with dissolve
            else:
                show lily happy with dissolve
            jump lilymenu
    $ lilysex = 1
    if fr == 1:
        show lilyb w
    else:
        show lilyb
    show lily happy
    with dissolve
    jump lilymenu
label lilysplitsex:
    "…"
    scene bg librarylab with d
    "After many hours of genuine work, it’s clear that Lily is getting slightly sexually aroused. That’s pretty normal for her, but she still managed to surprise me with what happened next."
    show lilyb w
    show lily horny
    with d
    lily "Did you know that I used to be a ballet dancer? It had me thinking, I could use some of my flexibility for more interesting sex positions."
    "We’d been talking about sex intermittently for a while now. Lily seemed to like the idea of discussing how we could make our sex more fun and interesting."
    mc "Ballet, right? Show me what you can do."
    show lily happy with d
    lily "Mmh, let’s see… Can I still do this?"
    "With one hand on a wooden surface, and the other on her hips, she slowly raises her left leg upwards."
    show lilyb splits
    show lily splits1
    with d
    "Higher, higher, higher… A complete split!"
    lily "I did it!"
    mc "I had no idea you could do that. Although I should have noticed your flexibility whenever we fucked legs up missionary. I can’t even get my legs that high."
    lily "I bet you could fuck me like this, hehe!"
    mc "Well, uh.."
    "Lily is probably only somewhat aware of how wet her pussy is right now. But judging by her nodding, she might be more aware than I realize."
    lily "Go on, do whatever you want… I’m your little slut."
    mc "Where do I even begin? Hmm…"
    play music sex1 fadeout 5.0
    "Kneeling down, I bring my face level to her delicious spread pussy. I decide to slide my tongue across her clit, starting an assault of pleasure."
    "I figured this would be a good test to see if Lily can keep her leg held upright under the pleasure, and I’m mighty impressed when she does."
    "Meanwhile I also gently stroke my cock to full erection. Doesn’t take long at all while munching Lily’s carpet."
    lily "Ahh, ohhh… You’re really good at that, haaahh… I bet you could get me off really easily, but… I’d much rather…"
    mc "My cock? Don’t worry, I got you."
    "I stand up beside Lily, looks like her pussy is the perfect height for my erection to slide right inside."
    "With one hand wrapped around her left thigh, I hold her steady as I guide my cock into her pussy."
    play sound cum
    show lily splits2 with d
    "A lewd schlick can be heard as I part her dripping wet lips. Lily moans and shivers with pleasure as I push as far as her tight pussy would allow."
    lily "Oohh, that feels good! This is fun, hehe."
    play ambience sex fadein 3.0
    "Wrapping my other hand around to the right side of her hips, I support both thighs and body as I start to gently make love to her."
    "At the peak of each thrust, almost on cue, Lily lets slip a cute moan. Her tail lazily swishes back and forth, signalling her enjoyment."
    mc "You’re pretty good at holding this position. Think I can speed up?"
    lily "Easy! Give it to me hard."
    mc "You asked for it."
    "Squeezing my fingers into her fur, I grip onto her thigh and hip tightly as I begin to pummel away with my hips."
    "*Slap, slap, slap.* Each successful connect of our bodies manages to create a palpable slap sound even against her sheer fur."
    lily "Ohh, ohhh gosh! Harder, fill up your slut!"
    "Even though we’ve only just started, it’s hard to resist the temptation to go all out and cum inside her now. Although she could use magic to get me going again, it’s still very tiring to orgasm twice."
    "Begrudgingly, I make an effort to hold my orgasm back, but still keep my speed up. Not only do I get to savour this divine pleasure a little longer, but I pamper Lily with excess amounts of pleasure."
    "Her thighs tremble as sparks of bliss course through her nerves. Yes, she seems to be getting closer."
    "I wonder if I could… Yeah, I’ll rub her clit too, and really push her over the edge."
    "My fingers find her swollen little nub and begin to rub. The simultaneous pleasures shock her briefly, her poor body spasming as it’s overloaded with stimulation."
    lily "Ack! Ahhha, ahhh! O-Ohhhhh! Y-You’re… Ahhhh…"
    "She can barely get a sentence out, and within ten seconds of squirming she’s easily brought to an orgasm. I’m really impressed that she manages to hold her leg up, although she is resting it on my chest right now."
    "I could probably keep going and get her off 2-3 times until she gets sensitive. But if I did that her legs might get stuck like this forever."
    "Alright, my turn… I stop rubbing her clit and start pounding at a pace that’ll get me off soon."
    "It doesn’t take long for Lily’s tight pussy to bring me close, and as her orgasm tapers off mine begins to surface."
    lily "Ahh, yesss… Cum in my slutty pussy! Haahh, haaahh…"
    play sound cum
    show lily splits3 with cum
    play sound cum
    show lily splits3 with cum
    "*Spurt, squirt* My mind is briefly lost in bliss as my cock explodes deep inside Lily."
    play sound cum
    show lily splits3 with cum
    play sound cum
    show lily splits3 with cum
    stop ambience fadeout 5.0
    stop music fadeout 5.0
    "*Thrust, thrust, thrust* I squeeze as much as I can out of my seven seconds of heaven, before I gradually come back down to earth and my cock begins to tap out."
    show lily splits4 with d
    "I pull myself out and allow a drip of cum to ooze down her thighs. She actually keeps her leg up a little longer just to let me marvel at my work."
    lily "Mm, look at what you did… I’m your cum dumpster. *Pant, pant*"
    scene bg librarylab
    show lilyb w
    show lily neutral
    with d
    "She drops her leg almost immediately after that. Her thighs trembling slightly as she tries to hold herself upright."
    lily "Ooww, my legs are aching. Maybe I overdid it?"
    mc "I think so. Can you stand?"
    show lily embarrassed with d
    lily "Mhm. It hurts a bit though. Maybe we’ll do it lying down next instead."
    mc "Haha, if you say so."
    scene bg black with d
    if crystalballactivated == 1:
        jump cbmenu

    "We spend the rest of the day finishing off her tasks before I return home."
    "…"
    $ secretsunlocked += 1
    jump evening

label penelopework:
    if fr == 1 and frs == 0:
        scene bg black with dissolve
        show bg library2 with dissolve
        play music library fadein 3.0
        $ frs = 1
        "I work at the library alone while Lily occasionally comes down to help or give me orders."
        "Eventually as it nears closing time a familiar face catches the corner of my eye."
        show penelope chappy with dissolve
        penelope "Oh, it's you!"
        show penelope csad with dissolve
        penelope "I just wanted to apologize again."
        mc "Well... I don't really know what to say."
        show penelope cshy with dissolve
        penelope "Y-Yeah... You were one of the people that got burnt most by my actions, so I'd understand your apprehension..."
        penelope "I won't ask you to understand why I did what I did, but I will ask if you'd find it in your heart to forgive me."
        mc "To be honest, I don't know enough to not forgive you."
        mc "I can kinda work out your reasonings, but... Could you tell me your motive?"
        show penelope cshocked with dissolve
        penelope "M-My motive? Well... My motive sucks!"
        show penelope csad with dissolve
        penelope "It was a mixture of unreciprocated love, jealousy, greed and a desire to fulfill a debt owed."
        penelope "I had been under Morrigan's care for years after she saved my life, took me in, and taught me everything I knew."
        penelope "I was kinda... manipulated, I guess..."
        penelope "But Morrigan made one big mistake, she taught me too well so I eventually outgrew her aggressive and toxic philosophies."
        penelope "Like an idiot I stuck around hoping I could 'change', or 'improve' her."
        penelope "Ahh, ahh, and I was kinda infatuated with her... I'll be honest, I still am..."
        penelope "But even I have my limits."
        mc "Well, she almost killed you..."
        show penelope cshy with dissolve
        penelope "Y-Yeah... I am so full of shame right now, euughh..."
        penelope "Hey, think you can cheer me up?"
        mc "Huh? How can do I do that?"
        show penelope chorny with dissolve
        penelope "Meeehhh, I want a good dicking."
        mc "Wha?!"
        show penelope claughing with dissolve
        penelope "Like, an aggressively good fucking to just melt my brain."
        mc "I thought you were gay!"
        show penelope chorny with dissolve
        penelope "Oh? The only reason I made that excuse is because I didn't want to fall under the spells Morrigan placed on you."
        penelope "Truth is I'm bisexual. Sorry if that feels cheap to you, but I feel like I need to stop lying to people now."
        penelope "No more disguises, just you and I having raw sex."
        penelope "Oh, and maybe you'd be able to get me pregnant too!"
        mc "Pregnant? Aren't we moving a little fast?"
        penelope "I was the second in command to Morrigan, so I'm actually the new Morphling Queen... As the matriach I have a duty to breed."
        mc "Isn't that a little suffocating as a responsiblity?"
        penelope "It's just our culture, once I give birth, the eggs will be sent to the hive to be raised anyway."
        mc "Eggs? Wow, you really are a morphling Queen now, aren't you?"
        show penelope claughing with dissolve
        penelope "Slowly adjusting to it, but yeah, I guess!"
        "Well... Maybe I could try knocking her up?"
        stop music fadeout 3.0
        play ambience ambiencenight fadein 3.0
        scene bg peneloperoom with dissolve
        show penelope chappy with dissolve
        jump penelopemenu
    scene bg black with dissolve
    show bg library2 with dissolve
    if fr == 1:
        show penelope chappy with dissolve
    else:
        show penelope happy with dissolve
    play music library fadein 3.0
    penelope "Heyy, I didn't know you were here! To work, I assume?"
    mc "You know it, what've you got for me?"
    penelope "Oh, a little bit of this, a little bit of that. You can start with today's book returns and I'll work the reception."
    stop ambience fadeout 3.0
    scene bg library with dissolve
    "I spend all day working at the library with Penelope."
    "As the evening draws closer, we close the library and take a break in her room."
    stop music fadeout 3.0
    play ambience ambiencenight fadein 3.0
    scene bg peneloperoom with dissolve
    if fr == 1:
        show penelope chappy with dissolve
    else:
        show penelope happy with dissolve
    penelope "We've got about an hour to kill before five, wanna watch a film or something?"
    menu penelopemenu:
        "Talk" if penelopetalks == 0:
            jump penelopetalk
        "Sex":
            jump penelopesex
        "Leave":
            if fr == 1:
                show penelope claughing with dissolve
            else:
                show penelope laughing with dissolve
            penelope "Got something to do? I won't hold it against ya."
            if fr == 1:
                show penelope chappy with dissolve
            else:
                show penelope happy with dissolve
            penelope "See you around."
            jump evening
label penelopetalk:
        menu:
            "Any plans for the future?":
                mc "Any plans for the future?"
                if fr == 1:
                    show penelope cneutral with dissolve
                    penelope "Well, I want to help the rest of my species in these strange times."
                    penelope "News of our Queen's death may cause even more resentment to boil within our numbers, which isn't ideal for peace."
                    penelope "Bravely, the Royal Sisters will help me figure things out..."
                    penelope "As the new morphling Queen, I need to do my best to ensure there isn't an uprising."
                    mc "Sounds like you've got your hands full."
                    show penelope claughing with dissolve
                    penelope "No kidding... Hmm... I'm hopeful though. I remember from a young age that there were many people that wondered why we didn't form a peace agreement with Arcadia."
                    show penelope chappy with dissolve
                    penelope "Whisperings like 'I heard the cow girls have a great trading agreement, why don't we do that?'."
                    penelope "In truth, the toxicity may have simply been a seed planted by Morrigan, who has ruled for sixty years."
                    mc "Oh really? What were the morphlings like before that?"
                    show penelope cneutral with dissolve
                    penelope "The previous leader wasn't much better. This recent incident marks the third time the morphlings tried to take over Arcadia in one hundred years."
                    penelope "But before that, as far as I'm aware we were a normal species stained with arrogant leaders that attempted to make non-unicorn creatures slaves."
                    mc "Ah... I can see why had problems with the Royal Sisters, then."
                    show penelope chappy with dissolve
                    penelope "Heh, yep... The sisters were very against keeping slaves, which caused plenty of conflict."
                    penelope "You could make the argument that the Royal Sisters don't have any juristiction over the morphlings, so they shouldn't poke their muzzles where they don't belong..."
                    penelope "But... Let's face it, you do something about that if you can."
                    mc "I absolutely agree."
                    show penelope cshy with dissolve
                    penelope "Feels pretty pathetic knowing that lead to several wars and resentment over one hundred years."
                    penelope "The morphlings don't even try to keep slaves anymore. I think we just want all this to be over and done with."
                    penelope "And it will be over, soon... I'll put things right."
                    mc "You're an amazing person Penelope. You're going to be a great Queen"
                    show penelope claughing with dissolve
                    penelope "Awh you..."
                else:
                    if fr == 1:
                        show penelope claughing with dissolve
                    else:
                        show penelope laughing with dissolve
                    penelope "Just the usual, get an adorable girlfriend and/or harem of girls."
                    penelope "Get my dream job that pays millions."
                    penelope "Buy a mansion, of course. Maybe the entire castle."
                    penelope "Then uhm, maybe become a princess!"
                    mc "I see you like to keep your goals small and manageable."
                    if fr == 1:
                        show penelope chappy with dissolve
                    else:
                        show penelope happy with dissolve
                    penelope "Absolutely!"
                    penelope "Really though, I'm hoping to use my Mysticism qualifications to get a job becoming an enchanter."
                    penelope "If I can make a new enchantment that people want to buy, I can patent it and become a bazillionaire."
                    mc "Enchantments?"
                    penelope "Like... Objects imbued with magic, like a ring that helps you sleep at night."
                    mc "Ohh, that sounds awesome! I need to get me some of those."
                    penelope "They're expensive though, it can take weeks to make just a single one."
                    mc "Do you have any enchanted objects?"
                    if fr == 1:
                        show penelope cneutral with dissolve
                    else:
                        show penelope neutral with dissolve
                    penelope "I'm studying one right now, a really fucking unusual one too."
                    mc "Fuckin' unusual? I'm not used to hearing you swear."
                    penelope "Seriously check out this circlet."
                    "Penny takes a golden circlet from a desk, puts it on and shows me it."
                    mc "Looks like an ordinary circlet."
                    if fr == 1:
                        show penelope cshocked with dissolve
                    else:
                        show penelope shocked with dissolve
                    penelope "Indeed, but this is a 'lucky' circlet, it makes you luckier."
                    mc "Luckier? How the hell do you measure that?"
                    penelope "I have no idea! I'm studying this intensively, I want to crack it."
                    mc "Have you tried asking the original creator?"
                    if fr == 1:
                        show penelope cneutral with dissolve
                    else:
                        show penelope neutral with dissolve
                    penelope "This is a relic that was found by archeologists, so unless I have a time machine, no can do."
                    penelope "At first, all I knew is that it emnates magic, and the engraving tells you it gives luck."
                    penelope "So of course I tested it, I wanted to figure out if it's true. Does it really make me lucky?"
                    penelope "I decided to field test it with permission, I wore it and paid very close attention to myself and my surroundings."
                    mc "What happened?"
                    if fr == 1:
                        show penelope csad with dissolve
                    else:
                        show penelope sad with dissolve
                    penelope "Almost nothing remarkable, I was so disappointed."
                    if fr == 1:
                        show penelope cshocked with dissolve
                    else:
                        show penelope shocked with dissolve
                    penelope "But then something occured to me..."
                    if fr == 1:
                        show penelope chappy with dissolve
                    else:
                        show penelope happy with dissolve
                    penelope "My body felt great while wearing the bracelet, I never once got ill, or got a cold. Even though it was the winter."
                    penelope "All my social interactions were smooth, I'd never slip up, or embarass myself."
                    penelope "When I tried playing board games and card games with friends, I'd win slightly more often than usual."
                    penelope "I never tripped over while working, I never burnt the roof of my mouth while eating, and I always slept soundly while wearing it."
                    penelope "That's when I realized, it worked! There was a small element of luck sprinkled into all the aspects of my life."
                    mc "That's... incredible."
                    mc "I want one!"
                    if fr == 1:
                        show penelope claughing with dissolve
                    else:
                        show penelope laughing with dissolve
                    penelope "Haha, that's it! Everyone will want one!"
                    penelope "So I need to figure this enchantment out and become a bazillionaire."
                    mc "Damn, that's so cool Penny. Keep me updated on how that goes."
                    if fr == 1:
                        show penelope chappy with dissolve
                    else:
                        show penelope happy with dissolve
                    penelope "Will do [playername], you can test my first batch."
                    mc "Oh hell yeah."
            "How did you find out you were a lesbian, and what was that like?" if fr == 0:
                if fr == 1:
                    show penelope claughing with dissolve
                else:
                    show penelope laughing with dissolve
                penelope "Seems crazy, doesn't it? You'd think it should be biologically impossible. When was the last time you met a gay horse?"
                if fr == 1:
                    show penelope chappy with dissolve
                else:
                    show penelope happy with dissolve
                penelope "But short answer is, I'm just not sexually attracted to men. I have nothing against them, it's not their personalities or behaviour, they're just not hot."
                penelope "The female body on the other hand is extremely attractive to me; the curves, the breasts, the pussy... It all arouses me greatly."
                penelope "So you could probably see why I have no issue engaging with a male turned female, for me it is purely physical attraction."
                penelope "Wish I could tell you more of the underlying psychology behind it, but I couldn't explain it even if I tried."
                mc "Is this sexual orientation common among the female aligned pony population?"
                penelope "I'd say a preference to both genders is the norm, and while there are some mares that only like men, I'm in a minority of mares that only like females."
                mc "Are there any stallions that only like men?"
                penelope "You bet, I think by percent there are more gay stallions than there are gay mares."
                mc "I wonder why that is."
                penelope "I reckon it's evolutionary, perhaps because mares have a deep maternal instinct and a mating season to go along with that."
                mc "You could be on to something there."
            "What made you reach out to Moxie?":
                mc "What made you reach out to Moxie when she was down?"
                if fr == 1:
                    show penelope chappy with dissolve
                else:
                    show penelope happy with dissolve
                penelope "Good question, not many would in my position."
                penelope "But I saw myself in her, I was young and naive once too."
                if fr == 1:
                    show penelope claughing with dissolve
                else:
                    show penelope laughing with dissolve
                penelope "A good role model can make the difference between a good person and a bad person, so I wanted to inspire her."
                mc "You saw yourself in her?"
                if fr == 1:
                    show penelope cneutral with dissolve
                else:
                    show penelope neutral with dissolve
                penelope "Yeah... I wasn't always a good person, maybe I was worse."
                penelope "I lost a close friend and spiralled into isolation, I became quite toxic for many years."
                penelope "I hated everyone else, I thought they were the problem. I never once considered that I was being an asshole and behaving problematically."
                if fr == 1:
                    show penelope cshy with dissolve
                else:
                    show penelope shy with dissolve
                penelope "It's quite easy to become resentful when you're isolated, whilst also justifying yourself."
                penelope "Moxie was following that same path."
                if fr == 1:
                    show penelope cneutral with dissolve
                else:
                    show penelope neutral with dissolve
                penelope "She isn't a bad person, she's just very lonely, she doesn't have the friends nor role models to teach her how to be a better person."
                mc "How did you pull yourself out of that isolation?"
                if fr == 1:
                    show penelope chappy with dissolve
                else:
                    show penelope happy with dissolve
                penelope "It was Lily and her friends that reached out to me, so it felt natural to reach out to Moxie when I saw her following the same path I did."
                penelope "Especially at such a crucial age, you need to grow up fast before the world overwhelms you."
                mc "I definitely agree with you there, some people never grow up and it's such a sorry sight."
                penelope "Indeed..."
                mc "What about Lily? Isn't she quite isolated?"
                if fr == 1:
                    show penelope cneutral with dissolve
                else:
                    show penelope neutral with dissolve
                penelope "Lily? Surprisingly no. She isn't isolated, she's does talk and meet with people on occasion."
                penelope "She's just extremely introverted, but I believe that she's already learnt the important lessons."
                penelope "My worry for her is that once I graduate, she won't be able to carry on her social life alone."
                if fr == 1:
                    show penelope chappy with dissolve
                else:
                    show penelope happy with dissolve
                penelope "I'm trying my best to build up her confidence step by step."
                mc "Me too, she's really started to come out of her shell {i}again{/i} lately."
                penelope "Yeah, it's easy to fall into old habits when you're alone for a while."
                penelope "But don't worry, we mares are tough."
            "Could you tell me what it's like being a Morphling, and perhaps some more detail about your involvement before we met?" if fr == 1:
                show penelope cshy with dissolve
                penelope "Ah, it's rough sometimes... Our history has left our species stigmatised and stereotyped."
                penelope "It's not like I blame anyone, I'd even agree with that sentiment... Especially considering how evil and corrupt our leader was..."
                mc "So you think she was evil and corrupt too?"
                show penelope csad with dissolve
                penelope "Perhaps, but no one is beyond help... At least, that's what I used to think..."
                penelope "Turns out, you can only help someone if they want to help themself."
                show penelope cneutral with dissolve
                penelope "You can't change someone, or even ever really understand them, you can only try to push them in the right direction with guidance. But you can never predict what they'll be like when the time comes."
                penelope "I thought Morrigan was changing for the better, but I was entirely mistaken..."
                penelope "While I was trying to better Moxie-Morrigan, I did notice some improvement, but it seems like that improvement was entirely levied by Moxie."
                penelope "All you need to do is look at how the two handled supreme power."
                show penelope cangry with dissolve
                penelope "The moment any droplet of power was offered to Morrigan, she suddenly became selfish, bitter, hateful. Even I was irrelevant in her eyes now, a used tool."
                show penelope chappy with dissolve
                penelope "But Moxie? She has really come a long way, she immediately wanted to use that power to help, and even to this day she's trying to pursue that path through Selene's lessons."
                mc "You were close with Morrigan though, why did she turn on you so quickly?"
                show penelope cshy with dissolve
                penelope "'Close'... is a questionable term with Morrigan, I think she sees everyone as expendeable. Even while we were lovers, I think she was just using me to get energy via sex."
                mc "I see... So she was likely taking advantage of your feelings towards her."
                mc "Why help her take over at all? Did you have something against the Royal Sisters?"
                show penelope csad with dissolve
                penelope "*Sigh* She also took advantage of me by making me her spymaster..."
                penelope "While I was helping Morrigan to take over Arcadia, I always wanted her to be a benevolent Queen... Not an evil tyrant."
                show penelope cneutral with dissolve
                penelope "I, like many other morphlings, was subject to a lot of propaganda from a young age, so I did initially detest the royal sisters for the majority of my life."
                penelope "But as I began to live my life here as a spy, it became apparently obvious just how many lies I was fed."
                penelope "I just hope the other morphlings can follow in my footsteps. I'm going to try to instate peace and trade agreements between Arcadia and the hive of remaining morphlings."
                show penelope chappy with dissolve
                penelope "One day, perhaps our species will no longer be seen as evil, but merely another 'type' of pony, like unicorns or pegasus."
                mc "I wish you the best of luck, Penelope, and thank you for defying your upbringing."
            "Back":
                jump penelopemenu
        $ penelopetalks = 1
        if fr == 1:
            show penelope chappy with dissolve
        else:
            show penelope happy with dissolve
        jump penelopemenu
label penelopesex:
    menu:
        "Cunnilingus and Facesitting":
            penelope "Ahh, up for practicing some girl lovin'?"
            mc "Sure thing, no holding back."
            penelope "You could tell I was holding back before? Hehe."
            play sound magic2
            if fr == 1:
                show penelope chorny with cum
            else:
                show penelope horny with cum
            "Almost catching me off guard, Penny’s horn flashes, and I feel a surge of magic surround me. Within a painless instant, I find myself miraculously possessing a female body."
            "As before, my senses don’t immediately register the addition of breasts or the loss of my male genitalia. This bizarre phantom feeling eventually fades."
            if fr == 1:
                show penelope chappy with dissolve
            else:
                show penelope happy with dissolve
            penelope "You make a cute girl [playername], I'd tap that."
            mc "You are 'tapping' that."
            if fr == 1:
                show penelope claughing with dissolve
            else:
                show penelope laughing with dissolve
            penelope "How could I not? Hehe."
            if fr == 1:
                show penelope chorny with dissolve
            else:
                show penelope horny with dissolve
            penelope "This spell always turns me on."
            play music sex1 fadein 30.0
            if fr == 1:
                show penelope csatisfied with dissolve
            else:
                show penelope closesatisfied with dissolve
            "Penny sits down next to me and takes a commanding lead, bringing her lips towards mine and passionately making out with me."
            "Her experience is immediately clear as her tongue swirls into my mouth and toys around with my own."
            "Feeling all tension drift away from my body, I sink back into the sofa, completely captivated by her kiss."
            "I can feel my new body getting aroused. I feel a warmth in my pelvis and a tingling sensation between my thighs."
            if fr == 1:
                show penelope chappy with dissolve
            else:
                show penelope closehappy with dissolve
            penelope "Mmphh, ah... Does it feel better as a girl?"
            mc "It actually does, the orgasms are much better."
            if fr == 1:
                show penelope chorny with dissolve
            else:
                show penelope closehorny with dissolve
            penelope "I wonder if I should try turning into a guy, hahah"
            if fr == 1:
                show penelope csatisfied with dissolve
            else:
                show penelope closesatisfied with dissolve
            "She pushes me down on the sofa and crawls on top of me, wasting no time sticking her face in my breasts and licking one of my nipples while she teases the other expertly with her fingers."
            "I can begin to feel a growing, throbbing desire in between my legs."
            "Penny swaps her mouth to the other nipple and continues to tease me, I rub my thighs together slightly resulting in a tiny pleasurable sensation, but it only increases my desire to be touched."
            if fr == 1:
                show penelope mcunnilingus with dissolve
            else:
                show penelope cunnilingus with dissolve
            play ambience blowjob
            "She grins as she finally goes between my legs. She doesn’t tease me anymore, and I feel her tongue immediately lapping up and down the length of my new vulva."
            "It feels so wet and sloppy, but when she focuses on my clit my body is racked with a powerful sensation that causes my back to arch and my eyes to roll back."
            penelope "Warm, wet, soft, and delicious…"
            penelope "*Lick, lick*, *Lick*."
            "This is fucking awesome, Penny’s tongue skillfully pleasures my clit over and over. I have to hold back a few moans with the worry that Lily might hear me."
            "Occasionally I can feel her lips purse around the nub as they suck, simultaneously I can feel a pressure from her tongue, it drives me wild as my fingers grip tightly on the sofa cushions."
            "I can’t help but squirm and moan, it feels amazing, and the pleasure keeps rising."
            "I think I’m going to orgasm soon."
            "It doesn’t just feel like she’s licking my clit, it feels like she’s making out with my pussy."
            "Finally, her skillful tongue pushs my pussy over the edge and I climax."
            "The initial climax was powerful, similar to a male orgasm, however the peak of euphoria dragged on for far longer."
            "The euphoria dissipated but the climax continued with a heightened sense of sensitivity, each movement of Penny’s tongue filled my entire body with potent pleasure."
            "My climax lasted far longer than a man’s. And while the peak of pleasure was relatively the same, the length of the female orgasm easily bested the two."
            "My head was in the clouds for a few seconds after that powerful orgasm. It took me a few seconds to notice Penny crawling over me like a cougar hunting her prey."
            stop ambience
            if fr == 1:
                show penelope chorny with dissolve
            else:
                show penelope closehorny with dissolve
            penelope "Hope you enjoyed the first act, but this next part is my favourite..."
            if fr == 1:
                show penelope mfacesitting with dissolve
            else:
                show penelope facesitting with dissolve
            "She giggles and straddles my head, giving me a direct view of her aroused vulva. Her lips glisten with a sheen of wetness."
            play ambience blowjob
            "As she slowly lowers herself, I resign myself to pleasure her as much as possible. I may not be as good at cunnilingus, but I want to wow her."
            "I know for a fact she needs no teasing, so I focus on her clit immediately and draw as much pleasure from her as possible."
            penelope "Ahh, that’s perfect, ahhh... You really are a good girl."
            "Only a few licks in and I can already hear her breathing turn ragged and cute gasps escaping her lips."
            "It’s clear to me that she’s burning with desire."
            penelope "*Pant, pant* Mmphhh gosh, my clit is so sensitive!"
            penelope "Ahh, ah… Don’t hold back though, it feels so amazing!"
            "I swirl my tongue around in circles on her clitoris as she starts to gradually grind back and forth."
            "As her hips move the fur of her thighs pleasantly brush against my cheek and the grool from her sex drips onto my lips and tongue."
            penelope "Mmphh, that’s perfect, keep going like that… Ahh, ahh…"
            "As my tongue persists, continuously keeping up the pleasure on her sweet spot, her grinding gradually becomes more needy and vigorous."
            "She applies more pressure onto my face as she drags herself back and forth. Her gasps from earlier dissolving into complete passionate moans."
            penelope "Ahhh, aaaahhhhh… I-I… Aaaaahhhhhhhhhhhh, I’m gonna…"
            "I have to hold her thighs in place as I tactfully suck and lick her moving clit to the best of my ability, even as she wriggles and writhes above me."
            penelope "C-Coming! Aaaahhhhh, aaaahhhhh!"
            "She actually stops grinding and arches her back as she climaxes, allowing me to pleasure her throughout the entire duration."
            stop ambience
            if fr == 1:
                show penelope csatisfied with dissolve
            else:
                show penelope closesatisfied with dissolve
            stop music fadeout 3.0
            "As she gradually comes to a halt, she lifts herself from my face and crumples down onto the sofa, her legs seemingly weak as she catches her breath."
            penelope "*Pant* Damn… That was good."
            if fr == 1:
                show penelope chappy with dissolve
            else:
                show penelope closehappy with dissolve
            "I sit up and she notices my face is covered in her wetness, so she graciously pats me down with a tissue."
            mc "Thanks Penny, those female orgasms are mind-shattering."
            if fr == 1:
                show penelope claughing with dissolve
            else:
                show penelope closelaughing with dissolve
            penelope "You’re telling me. You also gave me an even better orgasm than last time."
            if fr == 1:
                show penelope chappy with dissolve
            else:
                show penelope closehappy with dissolve
        "Rubbing and Tribbing":
            penelope "I'm going to take my time playing with you..."
            play sound magic2
            if fr == 1:
                show penelope claughing with cum
            else:
                show penelope closelaughing with cum
            "I find myself immediately returning to my dainty female body."
            "It takes a few seconds for my nervous system to readjust."
            "Penny, whom is sat beside me starts caressing my soft thighs, each movement gets closer and closer to my new vulva."
            if fr == 1:
                show penelope chorny with dissolve
            else:
                show penelope closehorny with dissolve

            penelope "Yeah, that’s right… Give in to me..."
            penelope "Just relax... Spread your legs slightly."
            play music sex1 fadein 5.0
            if fr == 1:
                show penelope csatisfied with dissolve
            else:
                show penelope closesatisfied with dissolve
            "She pushes me down and I can feel her tongue trace the outline of my lips."
            if fr == 1:
                show penelope chorny with dissolve
            else:
                show penelope closehorny with dissolve
            mc "A lick? Is that all?"
            if fr == 1:
                show penelope csatisfied with dissolve
            else:
                show penelope closesatisfied with dissolve
            "Penny doesn’t wait another second, she surprises me with a sudden forceful kiss of the lips. She soon backs away and observes my reaction."
            if fr == 1:
                show penelope chorny with dissolve
            else:
                show penelope closehorny with dissolve
            penelope "Mmm… I like that."
            mc "Me too… Let’s do it again?"
            if fr == 1:
                show penelope csatisfied with dissolve
            else:
                show penelope closesatisfied with dissolve
            "Holding both my hands back, she lowers her head and begins to kiss me again."
            "Penelope’s tongue slipped its way into my mouth past my pursed lips."
            penelope "Ahn… hnn… mmm…. ha…"
            "I responded with an equal amount of passion, my tongue twisting around hers."
            "In our overeagerness the wet noises from our kiss were borderline obscene and our lips began to glisten with a layer of moisture."
            "That primal, animalistic energy as our tongues twirl and toy with each other."
            "Every few seconds I could feel Penny’s hand gently brush against my thighs, ever inching closer to my sweet spot."
            if fr == 1:
                show penelope chorny with dissolve
            else:
                show penelope closehorny with dissolve
            penelope "Haah… Hah… Your girly skin is so soft."
            if fr == 1:
                show penelope csatisfied with dissolve
            else:
                show penelope closesatisfied with dissolve
            "She says before she returns to kissing me. The teasing aroused me and the aching feeling between my thighs re-emerged."
            play ambience sex fadein 10.0
            if fr == 1:
                show penelope mrubbing with dissolve
            else:
                show penelope rubbing with dissolve
            "Finally, Penny’s fingers start to brush against the wet folds of my pussy. Penny pulls away from the kiss as she watches eagerly for my reactions."
            penelope "You’re so warm down there… Already so wet too hehe…"
            "She teases me by lifting her fingers and showing a string of my wetness between them, with a lewd expression she licks off the juices before bringing her finger back to my pussy."
            "Her fingers waste no time finding and rubbing my clit, as a woman and she certainly knows how to please one."
            "My entire body shivers with that unique pleasure, causing me to squirm under her movements."
            "She speeds up, and before I know it my breath is becoming ragged and I’m struggling to hold back moans."
            "With each passing second I can feel Penny admiring my expression and pleasure in the situation."
            penelope "If I keep going like this, I’ll make you come…"
            "She’s right, she continues to rub my clit, she doesn’t get faster or harder, yet the pleasure keeps rising."
            "She keeps going, my toes curl and my muscles tense up slightly."
            penelope "I love your cute faces..."
            mc "I-I’m close."
            penelope "You’re lucky that I’m not one for orgasm denial."
            "Her finger starts to speed up slightly, building up intensity and pressure inside me."
            penelope "I’m more of a ‘how many times can I make you come in one session’ gal."
            "I can’t feel anything else, except the electrifying pleasure of Penny’s finger rubbing my clitoris. It radiates all over my body."
            "Before I can even conceptualise what’s happening, the building pressure release all at once in a powerful orgasm."
            if fr == 1:
                show penelope mrubbing with cum
            else:
                show penelope rubbing with cum
            "Pleasure runs through my entire body in the form of heat and tingling sensations. The orgasm is intense and is coupled with the contraction of my vaginal muscles."
            "My female body squirms with delight as the feeling of euphoria washes over my body."
            "The euphoria soon melts away, replaces with a calming feeling of peace and relief that gently passes over me, bringing me back to reality."
            stop ambience
            mc "Mmphh… That was even better than last time."
            if fr == 1:
                show penelope chorny with dissolve
            else:
                show penelope closehorny with dissolve
            "I open my eyes and see Penelope looking smug with her bedroom eyes."
            penelope "I think it’s my turn for an orgasm now, isn’t it?"
            mc "Are you going to sit on my face again?"
            if fr == 1:
                show penelope claughing with dissolve
            else:
                show penelope closelaughing with dissolve
            penelope "Actually, I wanted to try something new with you."
            if fr == 1:
                show penelope chorny with dissolve
            else:
                show penelope closehorny with dissolve
            penelope "You may be my cute little plaything, but I want to show you as much as I can."
            mc "Your kindness betrays your inner femme dom."
            penelope "Hmph, I’ll show you. Lay down for me and spread your legs."
            mc "Like this?"
            penelope "Perfect..."
            if fr == 1:
                show penelope mtribbing with dissolve
            else:
                show penelope tribbing with dissolve
            "She raises herself and straddles my hips in an unusual way that interlocks our bodies. Before I could register what was happening, I could feel a wetness as our girl parts touched."
            play ambience sex fadein 5.0
            "Before I knew it, with my legs spread and at her mercy she began to grind against me."
            penelope "I’m so horny right now, aahh, aah… I won’t hold back."
            mc "It feels amazing, give it all to me…"
            "Our pussy lips were connected, and with each grind an amazing pleasure swelled through my body making my hairs stand on end."
            "I had heard tribadism was overhyped, but as Penelope and I rubbed our genitals against each other, we were both overwhelmed by pleasure."
            penelope "Haaahh, haah… This is so hot…"
            "Penelope grinded me in an experienced and dominant fashion, each gyration of her hips rubbed against my clit and created a sensational building wave of pleasure just as her rubbing had before."
            penelope "Ahaah, ahhh, I love your body, it’s so cute."
            "I looked up and down Penelope’s body feminine body, admiring hers just as she admired my own."
            "I loved the way her perky breasts wiggled around as her hips turned and her long hair bounced and flowed with the force of her movements."
            penelope "Haah, haah… I-I’m so wet, I don’t think I’ve ever been this wet before…"
            "Her mare pussy is dripping wet, far wetter than a human pussy. It lubricates our movements, and creating lewd wet noises at our point of contact."
            "Her movements were frantic and frenetic. It was clear she was immeasurably horny and aroused; she couldn’t even contain her moans."
            penelope "Aahhh, aahhh… Your pussy feels way too good!"
            mc "Me too, it’s amazing!"
            "She pushed harder and deeper, determinedly shaking her hips so she could reach her orgasm."
            penelope "Ahhh… I’m getting close, I won’t be able to hold back much longer."
            mc "I’m close too, ahh!"
            "She sped up, the speed and stamina of a mare is unrivalled for a human and thus I struggled to match the pace of her hips as they overpowered and overwhelmed me in speed and pleasure."
            "Eventually I slowed down and submitted to her as she continued to ride me, I could feel the pleasure and pressure building in me, about to boil over any second."
            penelope "Aahhh, haahh… I-I’m going to come! Haah, ha, ha… Hnngg…"
            if fr == 1:
                show penelope mtribbing with cum
            else:
                show penelope tribbing with cum
            "It didn’t take long for my climax to release as well, the two of us coming at almost the same time."
            "We kept grinding throughout the length of our orgasms, but as they faded Penny buckled down on top of me"
            stop ambience
            penelope "Haahh… Haah… Haahh…"
            if fr == 1:
                show penelope csatisfied with dissolve
            else:
                show penelope closesatisfied with dissolve
            "I wrapped my arms around the pinkish mare and cuddled her closely, her fur nestled against my skin; she feels extremely soft."
        "Penetrative Sex" if fr == 1:
            $ sdps = 1
            penelope "I’m looking forward to this, after all, I’ve heard so many great things."
            play music sex1 fadein 2.0
            scene bg black with dissolve
            "She escorts me to her bedroom and takes initiative by laying down and spreading her legs."
            show penelopeb sex
            show penelope sex1
            with dissolve
            penelope "Maybe this can help me atone a little? Hehe, kidding of course."
            "Her legs had spread into the letter ‘M’, revealing her tight slit. The sight got my blood flowing as my shaft grew to a full erection."
            "Her slow, heavy breathing accentuates her breasts as they tremble slightly with each exhale. It would seem she’s slightly nervous about this; she’s probably used to being in control."
            penelope "I see you’re admiring my body. How about I make it even more enticing for you?"
            play sound cum
            show penelope sex2 with dissolve
            "Penelope brings her right hand to her pussy, spreading her lips apart to reveal her warm gooey insides. I gasp and my cock throbs at the sight."
            penelope "She’s all ready for your cock, no need to go easy on me."
            "She coos as I close the distance and position myself between her legs, her tail flicking back and forth with anticipation as I align my cock against her twitching pussy."
            play sound cum
            show penelope sex3 with dissolve
            "I shift my hips, letting my shaft slide between her wet, plump lips."
            play ambience sex fadein 2.0
            "She throws her head back and gasps sharply as she’s penetrated. I grasp her by her soft, fluffy hips and begin to rock back and forth."
            "My movements are deep and sensual, my body pressing against her clit at the apex of each thrust and causing Penny to stir from the pleasure."
            penelope "Oooohh, yesss… I usually only do this with girls that have dicks, but this is amazing too…"
            "Passion increases as I continue to thrust into her sensitive pussy, her copious wetness slathering over my shaft and allowing me to gradually increase the pace."
            "Tightening my grip on her hips, I relish the feeling of her twitching pussy on every inch of my cock sinking into her."
            "Her initially reserved moans slowly grow as the rutting intensifies."
            penelope "Aahh, ahhh! D-Damn, s-so this is what everyone else has been feeling this entire time? I-It’s so good, aahhh…  H-How have I resisted for so long?"
            "The morphling mare’s hips try to thrust against me in the hopes of maximising the pleasure of our sex. She’s very slowly losing her mind to the pleasure like so many mares have before her."
            "She tries to wrap her legs around my hips, pulling me in closer and spreading her pussy slightly wider."
            "My grip on her hips gets tighter and my legs grow tense with effort, while her pussy quivers around my shaft and her legs begin to tremble."
            penelope "Oh gods! I’m coming really hard! Ahhh, s-so hard… Ahhhhah!"
            "She moans loudly each time our bodies connect, groaning and writhing as lust and pleasure overwhelm her body."
            "Her back arches as the explosive orgasm finally shatters her mind, her pussy tightly squeezing around my cock in overwhelming contractions."
            play sound cum
            show penelope sex4 with cum
            play sound cum
            show penelope sex4 with cum
            "I can’t help but blow my load as I hammer my hips into my lover’s pelvis."
            play sound cum
            show penelope sex4 with cum
            play sound cum
            show penelope sex4 with cum
            stop ambience fadeout 3.0
            stop music fadeout 3.0
            "Thick, hot loads of cum surge through Penny’s pussy as I enjoy the warmth of a powerful orgasm."
            "The load is so copious that each complete thrust creates a lewd squelch sound and oozing cum from our connection bubbles with air."
            show penelope sex5 with dissolve
            "Thrusting harshly against her for the duration of both orgasms, I eventually pull away from her trembling form."
            "As if released from a bind, Penelope’s body slumps down lazily on the bed, panting as she stares at the wooden ceiling."
            penelope "Woah… *Pant, pant* Is it supposed to feel that good? Or are you still under Morrigan's spells? Haahh…"
            scene bg black with dissolve
            "Penny and I clean up and spend some time kissing and cuddling before I return home."
            "..."
            jump evening
        "Back":
            jump penelopemenu
    stop music fadeout 3.0
    play ambience ambiencenight fadein 3.0
    if fr == 1:
        show penelope chappy with dissolve
    else:
        show penelope closehappy with dissolve
    penelope "Phew, you're getting really good at this. You'd make a pretty damn good lesbian."
    mc "Hahaha, maybe so. It is teaching me how to really please a lady."
    penelope "Tricks of the trade, but you didn't hear them from me! Hehe."
    "Penny and I clean up and spend some time kissing and cuddling before the spell expires and I return home."
    scene bg black with dissolve
    "..."
    jump evening
