label bar:
    $ barvisits += 1
    if barvisits == 1:
        $ barvisit1 = 1
        $ monies += 25
        jump barvisit1
    elif barvisits == 2:
        $ barvisit2 = 1
        jump barvisit2
    else:
        jump barvisitday
    label barvisit1:
            "I think the bar will be a wonderful place to work. It’ll give me an opportunity to meet people and learn more about Arcadian culture."
            show bg baroutside
            with dissolve
            "I head to the bar and knock on the door. It takes a moment, but a small red Pegasus girl opens the door for me."
            show riku closehappy with dissolve
            "Initially she squints at me, a look I’m getting used to. Her heterochromia leaves a striking first impression. However, she seems to be quick on the uptake as she nods her head and smiles"
            if bakeryvisit1 == 1:
                riku "Oh hey! It's Ruby's boyfriend, from the party!"
                mc "I am definitely not Ruby's boyfriend."
                riku "Aha, it's great to see you. Come right on in."
            else:
                riku "Ah, furless! Yep, you’re definitely the one Penelope mentioned in the letter! Come right on in."
            play music day2 fadein 3.0
            scene bg bar with dissolve
            show rikub
            show riku happy
            with dissolve
            mc "Thank you, the name’s [playername]."
            show riku laughing with dissolve
            if bakeryvisit1 == 1:
                riku "Just in case you forgot, I'm Riku."
            else:
                riku "I’m Riku. It’s always great to see a new face around these parts."
            show riku happy with dissolve
            riku "Glad you decided to come work here. It's on a reduced wage but sometimes when you’re new you need a little something to get you off your feet, I get that."
            "I look around the bar, it’s marvellously antiquated. It’s exactly how I’d imagine a fantasy tavern or mead hall. Bright and cheerful."
            mc "Great place you’ve got here."
            riku "This entire building is my house, and I’m using the bottom floor as the bar, it’s quaint."
            riku "We’re closed at the moment, so let me show you upstairs and we can chill."
            scene bg bar with dissolve
            "Riku and I walk up a set of wooden stairs into a more traditional room."
            show bg barupstairs with dissolve
            "Seeing this ordinary looking room really shows how well renovated the bottom floor is, it really does look like a fancy bar."
            mc "So you're closed, what time do you open?"
            show rikub
            show riku laughing
            with dissolve
            riku "Only in the afternoon, don’t tend to get many morning drinkers in Arcadia, so there’s no point in being open."
            mc "I’m sorry to bother you by coming so early, I can come back later if you’d like."
            show riku happy with dissolve
            riku "You’re no bother at all, in fact I gave my grace to Penelope under the pretense that you’d arrive at this time."
            mc "You have some kind of plan for me?"
            riku "Yup, I deal a lot with people around here, perhaps more than most others."
            show riku laughing with dissolve
            riku "So before we get to work, I felt like I’d take it upon myself to introduce you to the suburbs, while also making a new friend. How about it?"
            mc "That sounds great."
            show riku happy with dissolve
            riku "But first... Take a seat, don't stand around awkwardly hehe."
            "I take a seat on her sofa while she tidies around us. Seems like she wasn’t prepared for visitors. Regardless it’s quite tidy, it seems Riku is very orderly."
            riku "Awesome, as a barmaid I know the word around town. If you’ve got a question, I may have an answer."
            menu barvisit1choice1:
                "I should ask Riku some questions."
                "Heard any rumours?":
                    show riku laughing with dissolve
                    riku "Ohh that’s a good one, I’ve heard the strangest thing lately."
                    show riku shy with dissolve
                    riku "People have been talking about having vivid nightmares lately."
                    riku "As much as I’d like to call it all a buncha crap, I must admit I’ve been stirring in my sleep a little myself."
                    riku "Rumour is, there’s a witch that has put a curse over Arcadia."
                    mc "That sounds scary, do you think it’s true?"
                    show riku neutral with dissolve
                    riku "I just think hysteria is getting to us, if you think about some stupid curse enough it may eventually come true."
                    riku "And now all of a sudden people have one nightmare and they attribute it to some ‘curse’ to feed the myth."
                    mc "That’d be easy to say if magic didn’t exist in Arcadia though."
                    show riku shy with dissolve
                    riku "Yeah true, but I spoke about this with Penny a few days back and she said there’s no ‘normal’ magic like that, who am I to argue with the magic nerd?"
                    mc "Fair enough."
                    jump barvisit1choice1
                "Give me the latest gossip.":
                    show riku happy with dissolve
                    riku "You’ve also been referred to work with some of my friends, right?"
                    riku "I gotta say, we’re living in strange times. There was once a time where all six of us would meet up and have a good drink and chat at this bar, but nowadays there has been a notable distance."
                    riku "I can’t quite put my finger on it, but Butters, Lily and even Honeycrisp barely seem to leave their homes."
                    riku "It feels like that inner circle has morphed into Penny, Moxie and Ruby, but everyone is so busy lately."
                    mc "Yeah sorry about that, me and Moxie have been a little preoccupied."
                    riku "So unfortunately, I don’t have much gossip."
                    riku "Absolutely feel free to come visit the bar during the evenings, we can make our own gossip! First rounds on me, alright?"
                    mc "I’ll put you up to that."
                    riku "Hmm, maybe I should convince Melody and Blossom too, those two would be great fun."
                    jump barvisit1choice1
                "What kind of work can I do here?":
                    show riku neutral with dissolve
                    riku "Specifically in the bar, you’ll be serving drinks and talking to patrons. You’ll be a riot, girls will love ya."
                    mc "I’ve been getting that vibe."
                    show riku happy with dissolve
                    riku "If it’s new to you, you’re going to have to get used to it. After a few drinks these mares are even easier than before."
                    mc "Easier?"
                    show riku laughing with dissolve
                    riku "Hornier!"
                    show riku happy with dissolve
                    mc "Ooohh, isn’t it a bad idea to have me work here then?"
                    show riku laughing with dissolve
                    riku "Are you kidding? You’ll bring in all my customers! Hahaha."
                    show riku happy with dissolve
                    riku "But don’t worry, before it gets too late your shift will end, just before the mares get too tipsy and touchy."
                    mc "Touchy? Are they worse at night?"
                    riku "Oh for sure, girls get hornier and hornier as the day goes on. Peaks at midnight, that’s about when I start feeling it anyway, dumb heat."
                    show riku neutral with dissolve
                    riku "There’s other work outside of the bar, I’m sure Penny has been great, and given you a bunch of other leads."
                    riku "In Arcadia hard work gets rewarded, if you offer something to the community you get paid, same goes for here."
                    jump barvisit1choice1
                "Could you tell me about yourself?":
                    show riku happy with dissolve
                    riku "Not much to say, I just turned 19 so I guess I’ve peaked in life."
                    riku "Used to be an athlete, really serious from age 16 on. I wanted to compete in majors, but I ended up getting injured a year back, and I’ve never been the same since."
                    mc "Did you damage something permanently?"
                    show riku shy with dissolve
                    riku "Physically? Nah, I’m fine."
                    show riku neutral with dissolve
                    riku "I like drinking, playing games, going to the gym, chatting with my girlies."
                    show riku horny with dissolve
                    riku "Between you and me, I’m an enthusiastic fan of dick. But that’s just my inner heat demon speaking, so pretend you never heard that."
                    mc "You’ll fluster me with that abrupt attitude."
                    show riku neutral with dissolve
                    riku "Hey, I’m reading the list of most common thoughts from my brain."
                    riku "Booze, games, gym, socialising, dick."
                    riku "Not always in that order."
                    riku "If you want the order, it’s gym, socialising, booze, games, then dick."
                    mc "Is that your plan for today?"
                    show riku laughing with dissolve
                    riku "Hehehe… Hehehehe… Sure."
                    jump barvisit1choice1
                "(Conclude)":
                    pass
            mc "What are we going to do this morning then?"
            show riku neutral with dissolve
            riku "Ahh well, I thought maybe I could show you the gym."
            mc "The gym? How does that show me around the suburbs?"
            riku "We can totally do that too, we can go the scenic route."
            if libraryvisit3 == 1:
                mc "Lily gave me a permit for the city, so we can go there."
            riku "Not the city though, the entire city would take way too long to show you around, that place is bonkers humongous."
            mc "And then… the gym?"
            riku "Yeah, I was gonna go anyway, wouldn’t mind having a gym buddy."
            mc "Sure why not, I probably won’t be able to keep up with you though."
            "I mean heck, she can fly."
            riku "Not that special? You have a nice physique though, I thought you’d be a regular at the gym."
            mc "I have a nice physique? Are you sure you’re not just used to seeing this covered in fur?"
            riku "Nah man, don’t sell yourself short, you’re kinda hot."
            "I feel all fuzzy and warm inside now that she’s said that. I should go to the gym more often and become even hotter, hmm…"
            "Wait, was that her plan?"
            stop music
            scene bg arcadiasuburbs with dissolve
            "We head out and she begins a small tour of the village. She’s mainly pointing out the basics, there’s a market, a spa/brothel, a farm, a bakery, the library, the boutique…"
            if days >= 7:
                "Of course, this isn’t new to me at this point, but she adds a funny anecdote to each observation, it’s interesting to hear."
            show bg market
            show rikub
            show riku happy
            with dissolve
            play music castle fadein 3.0
            riku "Right away we can see the market here, and just next to it is the spa/brothel. Not unusual for them and the bar to have a close working relationship if you know what I mean."
            mc "That I do. Is the brothel, I mean uh, spa any good?"
            show riku neutral with dissolve
            riku "I used to get a few massages to relieve muscle tension, great for that. Can’t say what the other services are like though."
            riku "There’s also the bakery, they make cakes you could die for. I wouldn’t eat more than one a week though unless you were going to put on the pounds."
            mc "If I’m going to be become a regular customer, I’ll definitely need to visit the gym more."
            show riku happy with dissolve
            riku "I’m glad I’m not on a strict athlete diet anymore, I can balance the calories burnt at the gym with delicious cake."
            mc "Always a great reason to go to the gym, guilt free luxuries."
            show bg worldmapdialogue with dissolve
            show riku neutral with dissolve
            riku "If you peek just to the left of the bakery, you can see Honey’s farmhouse in the distance."
            show riku horny with dissolve
            riku "Honey, now that’s one hot piece of ass. If the two of us were ever alone and drunk enough, I reckon I’d go for it."
            show riku shy with dissolve
            riku "Unfortunately I don’t think she’s into mares, oh well."
            if farmvisit2 == 1:
                mc "Actually, you’re in luck, she is into mares."
                show riku embarrassed with dissolve
                riku "You’re kidding?"
                riku "Wait, how do you even know that?"
                show riku shy with dissolve
                riku "Ah, you know what, I’m not even gonna ask."
            riku "Haven’t seen her since… well… moving on."
            show riku neutral with dissolve
            riku "You probably already know about the library, right? We can skip that nerdy stuff."
            mc "Nerdy? I saw some books in your house."
            show riku laughing with dissolve
            riku "Pfft, ya got me! I love myself a good book as much as those unicorns do."
            show riku happy with dissolve
            riku "They read boring sciency books though, I like reading actiony things."
            mc "Any good suggestions?"
            show riku neutral with dissolve
            riku "Brave Boo and the Orange Chicken is fantastic, I’m nearly at the third act and it’s riveting."
            mc "I’m sorry, what?"
            show riku laughing with dissolve
            riku "Brave Boo? How have you not heard of her? She’s a treasure hunter that goes to different historical locations and looks for ancient artifacts, in this latest epic she’s looking for a legendary orange chicken, however it turns out to be…"
            "She’s even nerdier than the unicorns!"
            show riku shy with dissolve
            riku "Ahh… I’m boring you, aren’t I?"
            mc "Oh no, not at all, something about a chicken, right?"
            show riku laughing with dissolve
            riku "Whatever man! Look, we’re nearly at the gym, there are two places to point out here."
            show riku neutral with dissolve
            riku "There’s Moxie’s wagon, extremely charismatic and entertaining. I wish she’d perform in the market more often, I’d get to see her out of my window."
            mc "I'm glad you pointed out the wagon, that's one place I have no idea about."
            show riku laughing with dissolve
            riku "Pfft, your sarcasm is duly noted."
            show riku happy with dissolve
            riku "Here's something you probably don't know about the wagon area though, that's actually a clearing for a travelling circus that comes once a year. You just missed it though."
            mc "Awh damn."
            riku "Just past the wagon you have that big looming boutique, scary place! They make clothes!"
            riku "Who for? I don’t know, Ruby is a whimsical character indeed."
            show riku laughing with dissolve
            riku "I know I certainly wouldn’t be caught dead wearing one of those frilly dresses, heh."
            if boutiquevisit1 == 1:
                "I could tell her they make lingerie, but I’ll keep quiet."
            show bg arcadiasuburbs with dissolve
            show riku neutral with dissolve
            riku "Alright, let’s head to the gym. Figured I’ll pay for your membership, my treat."
            mc "Actually, I’m sharing Moxie’s membership, so you don’t need to worry about that."
            show riku happy with dissolve
            riku "Oh, you’re not supposed to do that! I’ll stay hush though."
            mc "Appreciate it, say, aren’t you worried about hanging around a male all day?"
            show riku embarrassed with dissolve
            riku "What, just because I’m in heat?"
            mc "Well, yeah…"
            mc "That and working out together, hot, sweat, exercise and all that."
            show riku neutral with dissolve
            riku "You’re making me feel nostalgic. I used to work out with my last gym buddy, then we’d go home and cap it off with sex."
            show riku angry with dissolve
            riku "Mmm... Hmph..."
            "She soon snaps from daydreaming to anger."
            riku "Then the shithead ditches me for some slut."
            mc "Oh? What happened?"
            show riku shy with dissolve
            riku "I don’t know… She was some bimbo with big tits, it won’t last, guarantee it."
            "I wonder if she has a complex about her breasts."
            stop music fadeout 3.0
            menu:
                "Are you jealous?":
                    show riku angry with dissolve
                    riku "Eugh, kinda? It’s not like he was special, he was just a guy."
                    riku "If anything he should have been grateful to be with me."
                    riku "Thin, attractive, good money, stable job, good in bed."
                    riku "But you know sometimes that’s just not good enough for some people."
                "You’re not using me to replace him, are you?":
                    show riku embarrassed with dissolve
                    riku "Whaaat? No!"
                    show riku shy with dissolve
                    riku "I’m not like that bimbo that sleeps around with anything! You have to earn me."
                    riku "I mean plenty of stallions come into my bar, you won't see me sleeping around with them."
                    riku "I need to get to know someone first. I’m not about that sleezy life, I’ve been at a bar and seen the worst of it."
                    riku "And my old gym buddy and that bimbo was the worst of it."
            show riku angry with dissolve
            mc "You sure there isn’t something you’re not telling me? I’m not sure why you would be this mad over a single friend with benefits."
            show riku shy with dissolve
            riku "Hmph… You’re not just nodding and yes-manning me. I respect that."
            riku "A lot of guys, especially this time of year will do whatever a mare says to please and placate them."
            riku "But yeah, you’re right... There is something else that I find a little harder to talk about."
            riku "Tch, you see… He wanted to start a relationship, but I was too reluctant to commit to anything."
            riku "We were friends, and the sex was good, but I just couldn’t see it going anywhere."
            mc "If that’s the case, why are you so hurt? You two were only friends."
            riku "Yeah, yeah, I know… Let’s sit on this bench before we go into the gym, I can’t run while ranting."
            play music triads
            scene bg arcadiasuburbs2 with dissolve
            show riku closeangry
            with dissolve
            riku "So this dude is frustrated that I won’t date him, right?"
            riku "He sleeps with me one night. Then the next evening there’s a drunk mare flirting with him, and he goes off with her."
            riku "Flirting and lovey-dovey, right in front of my face, while I serve them both alcohols. I was enraged."
            riku "He goes off and fucks her, then acts like he did nothing wrong because we’re just ‘friends with benefits’."
            "Heck, isn’t that what I’m doing? Time to enquire."
            mc "Was he wrong to sleep with someone else, especially considering he has no obligation to stay loyal to you?"
            show riku closeshy with dissolve
            riku "Tch, no, I guess not. But he acted like he wouldn’t, we had this unspoken rule of not sleeping with others."
            riku "Also, the bastard did it right in front of me! If you’re going to sleep with someone else, at least have the dignity to do it behind their back."
            "I can empathise, I imagine Moxie would get extremely jealous if I flirted with someone else while she was around, I would too."
            riku "If he had done it behind my back and one day earnestly mention he had slept with someone else; I probably would have reluctantly shrugged it off."
            riku "The two ended up dating, he ditched me real fast."
            mc "Why can’t you shrug it off regardless? If he’s out of your life now, you don’t have to worry about it."
            show riku closeangry with dissolve
            riku "Well the thing that pissed me off the most was his smug attitude the next time we met up. He told me about how it was ‘great sex’, and he might see her a few more times."
            riku "He bragged about the things she did in bed, that I don't."
            riku "I was honest to him, if he was gonna act like a dick, he can go fuck off back to her."
            riku "He played the victim, acted like he was justified and stormed out."
            mc "I see, so it was an attitude problem."
            show riku closeshy with dissolve
            riku "Yeah, the way I see it, he was trying to emotionally blackmail me into being his girlfriend, I ain’t having that shit."
            riku "You’re right though, he is a loser. I should just shrug it off because I can find someone better."
            mc "A better friend with benefits?"
            show riku closeneutral with dissolve
            riku "Hehe, crap. I did make it sound like that a bit, didn’t I?"
            show riku closelaughing with dissolve
            riku "Well, this time of year, I’ll make do with anything. As long as it’s a good man, know what I mean?"
            show riku closeneutral with dissolve

            stop music fadeout 7.0
            riku "Life’s too short to stick around toxic people that only bring you down."
            mc "You’re right, there’re plenty of amazing people around here that just want the best for everyone."
            riku "Ain’t that the truth, surround yourself with good people."
            riku "Phew, that was a long tangent."
            show riku closehorny with dissolve
            riku "Long story short, yeah I will get horny hanging around a male all day. But I can control myself, don’t worry your furry feet, [playername]."
            riku "Oh right, that saying doesn’t work for you and your furless feet."
            show riku closehappy with dissolve
            mc "No, I guess it doesn’t. Let’s see how these feet compare in the gym?"
            riku "Let’s do it!"
            scene bg gym with dissolve
            play music challenge
            "The two of us head to the gym and she absolutely obliterates me at everything we do."
            "She runs faster than me, she lifts bigger weights than me, she can do every higher intensity option."
            "All whilst being smaller than me, and appearing relatively innocuous."
            "We build up quite a sweat, but a combination of air conditioning, cold bottled water, and towels stave off the sweat to keep me going."
            "After being shown up by the athletic Pegasus we grab lunch before heading back to the bar and opening up."
            play music day2 fadeout 3.0
            scene bg bar
            show rikub
            show riku neutral
            with dissolve
            riku "Serving drinks is really simple, just grab a glass pop it under this tap and turn the knob. Take the money, into the register, return the change, and job’s a good’un."
            riku "Daisy is in the back washing up and clearing tables, she’ll probably help us serve drinks if it gets a bit busier too."
            mc "Not bad, this seems like a relaxing job."
            show riku happy with dissolve
            riku "It can get busier lately, we’re the only bar this side of Arcadia. So, there’s another worker for the evening shift. You’re just here extra as a favour, so don’t worry too much, we’ll look after you."
            mc "Am I really helping? I won’t just get in the way?"
            show riku neutral with dissolve
            riku "Honestly yeah, if you’re down here that means I can be in the office doing some boring shit, rather than having to stay up late into the evening to do it."
            riku "I guess in a literal sense you’re taking a large workload off my back; I definitely appreciate that."
            mc "Alright, I think I can handle things around here, thanks for showing me."
            show riku laughing with dissolve
            riku "Sweet, I’ll be in the back, gimme a buzz if you need me for anything at all."
            scene bg bar with dissolve
            "She heads off and I get ready to do the best job possible."
            "Of all times but now I feel oddly naked standing behind this counter. I think I know why too."
            "I feel like I should be in a uniform, you definitely can’t have a nametag without a uniform."
            "Speaking of that though, I’ve noticed a lot of subtle differences in my time here. The lack of clothing has radically altered the demands of ponies."
            "Riku often carries around a satchel to carry objects in because she doesn’t have pockets. Handbags and satchels are quite common, including the one I own."
            "That’s probably the reason why mobile phones don’t seem to exist in this world, but laptops and computers do. There simply was no demand for a small computer that can fit in a pocket."
            show barcustomer1 with dissolve:
                xpos 25
                ypos 50
            "Lost in thought and here comes my first customer, a cute mare! Heck yeah, although 85 percent of the population in Arcadia are cute mares."
            show barcustomer2 with dissolve:
                xpos 800
                ypos 50
            "The next one seems a little older, almost MILF-y. I’ve noticed that the fur causes ponies to age immensely well, wrinkles are far less noticeable."
            "Given that everyone is nude, people in this world also seem to take better care of their bodies, although there are perhaps multiple factors going into that."
            "It feels strange to say, but I’ve yet to see an unattractive individual in this society. Beauty is definitely high value when you’re nude, and hence so open and vulnerable."
            if boutiquevisit2 == 1:
                "That reminds me of Ruby, gosh her body was utterly stunning."
            hide barcustomer2 with dissolve
            show barcustomer3 with dissolve:
                xpos 350
                ypos 50
            "The younger customer is eventually joined by another mare, and the two come up to order drinks and we make some small talk."
            "They’re not completely unphased that I’m not a pony, but their reaction is positive and small talk between them is full of niceties."
            hide barcustomer1 with dissolve
            hide barcustomer3 with dissolve
            "The two mares head off to chat amongst themselves at a table. It’s not long before another customer heads in, an even older mare, perhaps retired that chooses to drink alone."
            "She even called me a ‘young man’ when she thanked me."
            "Daisy the other girl that works here is pleasant to talk to, however she seems notably disinterested in me. Our conversations never escaped small talk as she’d soon find something else to distract herself with."
            "Hours pass and customers come and go."
            "In my world when you buy something from a shop or a bar it tends to be transactional, at least for me anyway."
            "You’d say what you want, get it, pay and say thank you."
            "But almost every single customer, even the occasional stallion has made an effort to talk to me and ask me various questions."
            "The pure, happy vibe of this bar, and the people here leave a smile on my face every time."
            show barcustomer1 with dissolve:
                xpos 280
                ypos 70
            show barcustomer4 with dissolve:
                xpos 500
                ypos 0
            "There was one couple that were particularly interested in me, it was a mare clinging to the arm of a tall stallion."
            "They actually dared to ask me what I was."
            "I imagine a lot of people want to ask that, but feel like it’s too rude. I don’t mind though, I just haven’t figured out a satisfactory answer."
            mc "I’m a species from far away."
            "They usually ask where ‘far away’ is, and suddenly I don’t have an answer."
            "Sometimes honesty is the best policy though, just tell ‘em I was wrapped up in a magic related incident. It’s a great talking point."
            "’Magic? What kind of magic incident?’, ‘Are you like a dragon, can you breathe fire?’, ‘Do you get much action?’, ‘What do you think about Riku?’, ‘You think she’s hot?’."
            "Actually… These are a lot of questions, and they’re getting strangely personal."
            "And then something strange happens when I’m chatting with this couple, Riku is in the corner of my eye prompting me to come with her."
            stop music fadeout 3.0
            scene bg bar with dissolve
            "As I leave, I can hear the couple laugh as they realize what happened. And then it all clicks together."
            scene bg barupstairs
            show rikub
            show riku angry
            with dissolve
            "Me and Riku head upstairs and she rolls her eyes."
            riku "They finally decided to show their faces in here, they were basically interviewing you with all those inane questions. Daisy told me."
            mc "I wouldn’t call it an interview, but I suppose they were asking a lot of questions."
            mc "Are they who I think they are?"
            riku "Yep, the ol’ gym buddy wanker, and his new sleeve."
            "Oohh, that’s brutal."
            show riku neutral with dissolve
            play music day2 fadein 3.0
            riku "It’s whatever, your shift is practically over. Velour is here now; she’ll cover for you."
            riku "Here’s your pay, 25 smackaroos. It’s not exactly much, but it’s just what you need right?"
            mc "Yeah, I don’t have much use for money except for feeding myself."
            show riku happy with dissolve
            riku "Alright, but I can do a bit better than 25 monies. How about we have a few drinks to celebrate your first shift? I could use the distraction; I don’t want to go down there while those two are sneering."
            mc "Sure, I’ve got time. No point going to a bar without having a few, right?"
            riku "That’s the attitude, let me grab a few cold ones."
            "Pony brew beer?"
            "Ohh, I was wrong, Riku comes back with cold bottles of cider from the fridge."
            if farmvisit1 == 1:
                "I should have figured that out, it’s the same stuff Honeycrisp makes."
                mc "Ahh, I love this stuff."
                riku "It’s the best, ain’t it?"
            else:
                mc "Thanks for the cider."
                riku "It’s Honeycrisp’s special, thank her when you get the chance."
            hide rikub
            show riku closeneutral
            with dissolve
            "I take a swig and its sweetness combined with its coolness hits the spot, especially after being stood serving drinks for hours."
            mc "Those two were quite nosy."
            riku "Yeah, they probably saw that there was a new man in the house, so they wanted to get as much juicy info as possible."
            mc "Nothing to tell really, we just met. No juice!"
            show riku closehorny with dissolve
            riku "I think there’s a little bit of juice. Darn, hanging around a guy all day does make you horny. Is it just me, or do you feel it as well?"
            mc "I kinda noticed it, but I’ve mostly been preoccupied with work."
            show riku closeneutral with dissolve
            riku "Hmm, right, I’ve been sat in my office doing spreadsheets."
            mc "Hah, were you distracted?"
            show riku closelaughing with dissolve
            riku "Pfft, like I’d tell you."
            mc "You kinda already told me, you said you were horny."
            show riku closeembarrassed with dissolve
            riku "Ah shit, I did imply that. I didn’t think before I said it."
            show riku closesatisfied with dissolve
            "She takes a long swig of her alcoholic cider."
            show riku closeneutral with dissolve
            riku "How about you tell me something about you to make it even?"
            mc "You accidentally slipped up; I’m not obligated to return the favour!"
            show riku closelaughing with dissolve
            riku "Awh come on, it’s just a laugh ain’t it."
            mc "I don’t even know what I’d say though."
            "I take another sip of my cider. Mmm, this stuff is really moreish."
            show riku closeneutral with dissolve
            riku "Hmm, how about this, truth or dare?"
            riku "First to refuse loses!"
            "Her stubborn competitive nature is going to make this really interesting."
            menu:
                "Ohoho, you’re challenging me???":
                    show riku closelaughing with dissolve
                    riku "Hell yes I am! You’ve got spirit, [playername]. I feel like you and me see eye to eye."
                    show riku closeneutral with dissolve
                    riku "I think we could get to know each other more with a game like this."
                "This is going to end up bad and you know it.":
                    show riku closelaughing with dissolve
                    riku "Hmph, even if it does, it’s just in the spirit of the game, right?"
                    mc "I guess, are you sure you want to commit to what you may be committing to?"
                    show riku closeneutral with dissolve
                    riku "Hey, like I said, first to refuse loses, I ain’t going down without a fight."
                    "I wonder if she's truly considering the implications of this game."
            mc "What do I get if I win?"
            show riku closelaughing with dissolve
            riku "If you win? Haha, that won’t happen!"
            mc "Sure, what does the winner get then?"
            show riku closeneutral with dissolve
            riku "I dunno, how about the other person has to be a slave to the other?"
            mc "Seems paradoxical for the punishment of not following an order to be made to follow orders."
            show riku closehappy with dissolve
            riku "Don’t get tricky with me, I think it’s a clever idea!"
            riku "Fine, how about the slave orders are only allowed to be as bad as the truth/dare refused?"
            mc "Yeah, I like that idea. It escalates the stakes the further the game goes on."
            riku "Next time you come to my bar, one of us will be the other’s slave for the day."
            mc "Deal."
            label cbrikutod:
                pass
            stop music
            stop ambience
            play sound thunder
            show bg barupstairsgame
            show riku closeangry with hpunch
            riku "It’s on! Truth or dare?"
            show bg barupstairs with dissolve
            play music challenge
            menu:
                "Truth":
                    show riku closeneutral with dissolve
                    riku "I’m glad you picked truth, now I can make it even."
                    mc "I think all ideas of even-ness went out the window as soon as we started playing truth or dare."
                    show riku closehappy with dissolve
                    riku "Here’s your question. Have you been sleeping with any other mares in Arcadia?"
                    mc "Yeah, I have."
                    riku "Ohhh, what? Anyone I know?"
                    mc "You only have one question, Riku."
                    show riku closeshy with dissolve
                    riku "Awh damnit, I should have been more careful with my wording."
                    "She crosses her arms and pouts, thinking of a way to get me back no doubt."
                "Dare":
                    show riku closehappy with dissolve
                    riku "A first turn dare? Well aren’t you brave."
                    mc "Figured I’d throw you for a loop, since it sounded like you had a question prepared."
                    show riku closeneutral with dissolve
                    riku "You got me there, I don’t have a dare prepared, but I’m good at improvising."
                    "She points at my cider and winks."
                    riku "I dare you to finish that off in one go."
                    mc "Awh… Such a waste if I can’t savour it."
                    show riku closelaughing with dissolve
                    riku "If you do it, I’ll get you another one from the fridge. Go on!"
                    show riku closeneutral with dissolve
                    "It’s still just over half-full, but a dare is a dare."
                    "I bring the cusp of the bottle to my lips and start to chug it."
                    "After a few patient gulps and some nose breathing, it goes down quite well."
                    "Riku seems content and fetches another two bottles of cider, one for me and another for her, seems like she’s a faster drinker than I am."
            show riku closehappy with dissolve
            riku "Alright, my turn, I pick dare to start with."
            "I should build up the intensity of my dares slowly. Maybe try and target some of her weaknesses."
            "I could try to embarrass her, maybe use her heat to my advantage."
            menu:
                "What should I dare Riku?"
                "I dare you to sit on my lap.":
                    show riku closeembarrassed with dissolve
                    riku "W-wha? What a cruel first dare! You’re really going there, huh?"
                    riku "Using my femininity to your advantage, what a punk."
                    show riku closeshy with dissolve
                    riku "I’ll show you; I can use my femininity to my own advantage."
                    mc "You can think of ways to do that while you sit on my lap."
                    "She begrudgingly shuffles over to me, before hoisting herself onto my lap. Her thighs unflinchingly locked together, and she avoids any body contact other than where she’s seated on my lap."
                    show riku closeembarrassed with dissolve
                    riku "Hey, your skin is really soft, what the hell? I thought it’d be leathery and rough."
                    mc "I’m full of surprises you know."
                    show riku closeshy with dissolve
                    riku "You better not get a boner, damn perv."
                    mc "As long as you don’t drip on me, we should be good."
                    "I’m bluffing, it’s surprisingly hard to avoid getting erect while she’s sat on me, even though she’s explicitly making sure she puts no pressure on my genitals."
                    show riku closeembarrassed with dissolve
                    riku "Wait, how long am I doing this? We never agreed to a time!"
                    "I accidentally brush my hand past her thigh as I bring it to scratch my nose, causing her to jump."
                    show riku closeembarrassed with vpunch
                    riku "Uwah! I can feel something brushing against me! Don’t tell me that’s what I think it is?"
                    hide riku with dissolve
                    play sound cartoonimpact
                    "She scurries off and looks in-between my thighs. I’m a teeny, tiny bit erect, but no way near enough to brush against Riku."
                    show riku closeshy with dissolve
                    riku "Oh… Must have been my imagination…"
                    show riku closeangry with dissolve
                    riku "I’m gonna get you back for this! Truth or dare!"
                "I dare you to serenade me.":
                    show riku closeembarrassed with dissolve
                    riku "S-Serenade? Are you kidding?"
                    show riku closeshy with dissolve
                    riku "I’m not a tenth drunk enough to do something that embarrassing."
                    mc "What’s that? You want to be my slave for a day? I’m going to make you do more embarrassing things if that happens."
                    show riku closeangry with dissolve
                    riku "Pfft, I’ll do it, but you’re a loser."
                    show riku closeshy with dissolve
                    riku "…"
                    mc "…"
                    "…"
                    riku "Uh, I don’t know what to do, I don’t know any serenades…"
                    mc "Nothing at all?"
                    riku "Well, I listen to metal and shit, so… I'm going to put on some music."
                    riku "Eh-hem…"
                    stop music
                    pause 1.0
                    play sound thunder
                    play sound prismaserenade
                    show bg barupstairsgame
                    show riku closeangry with hpunch
                    pause 5.0
                    "She tries to serenade me, is this a serenade? I don't know, the song doesn't seem to have anything to do with love at all."
                    "I give her points for the effort though."
                    stop sound fadeout 2.5
                    show bg barupstairs
                    show riku closesatisfied with dissolve
                    mc "Wow..."
                    show riku closeembarrassed with dissolve
                    play music challenge fadein 3.0
                    riku "Was it not supposed to be like that? You said serenade! Like, singing!"
                    mc "Haha, that wasn’t a love song, that was uh... heavy metal."
                    show riku closeshy with dissolve
                    riku "Eugh, did I do it wrong? Whatever, I did your dare! It’s your turn now."
            "I imagine the truths and dares are going to get pretty brutal from here on."
            "She’s going to ask some tough and embarrassing questions that might change the way she looks at me, especially since she seems to be against sleeping around."
            "Her truths will be bad, but what will her dares be like? Painful, sexual?"
            "Dares are her real opportunity to give me something in the hopes I’ll fail."
            show riku closeneutral with dissolve
            riku "Come on, truth or dare?"
            menu:
                "Truth":
                    riku "Perfect, I can get you back for the dare you gave me."
                    riku "I was too nice to you on the first turn."
                    show riku closesatisfied with dissolve
                    "She takes a break in the middle of her sentence to gulp down some cider."
                    show riku closeneutral with dissolve
                    riku "I’m gonna start being mean now."
                    play music farm fadeout 3.0
                    "The room is heating up; the intensity is increasing!"
                    riku "Now that I know you’ve slept with a mare before, I gotta ask, who was it?"
                    if days > 6:
                        "Hmm, she assumes it was only one person, when in reality it’s a few now."
                    mc "I’ve slept with Moxie."
                    show riku closeembarrassed with dissolve
                    riku "Ohoh, my gosh! Really?"
                    show riku closehappy with dissolve
                    riku "She’s a performer in sheets as well as the streets."
                    mc "I have to say, she gives a great vocal performance."
                    show riku closelaughing with dissolve
                    riku "Haha, good one! Gimme five."
                    "We high-five each other, then she has a quick realisation that we’re not on the same side in this game."
                    show riku closeembarrassed with dissolve
                    riku "Wait, shit! That question was too easy, maybe I need to get my head out the gutter and ask something actually embarrassing."
                    show riku closeneutral with dissolve
                "Dare":
                    show riku closelaughing with dissolve
                    riku "Perfect, I can get you back for the dare you gave me."
                    show riku closeneutral with dissolve
                    riku "I was too nice to you on the first turn."
                    show riku closesatisfied with dissolve
                    "She takes a break in the middle of her sentence to gulp down some cider."
                    show riku closeneutral with dissolve
                    riku "I’m gonna start being mean now."
                    play music farm fadeout 3.0
                    "The room is heating up; the intensity is increasing!"
                    riku "I’ve had a bit more time to think of a good dare, so you’ll have to ready yourself."
                    riku "You know that gym work was really hard, how about a nice wing massage?"
                    "That’s her dare? I really don’t mind doing that, I hope she’s not missing the point of the game. Or am I missing the point of it?"
                    show riku wing with dissolve
                    "Oh well, her wings spread outwards, splayed out for the first time, it’s a gorgeous sight."
                    mc "I have no idea what I’m doing, but I’ll rub your… I don’t know."
                    mc "I’ll fondle you and see what you enjoy, I guess."
                    riku "Take your time, it feels fantastic anywhere, and I haven’t had one in months because the damn spa doesn’t do them."
                    "She turns her back to me and I start working at her wings. I figure working the feathers isn’t much use, so I focus on the appendages that sprout out from the top of her back, and slowly work my way out to the tips of her wings."
                    "Riku lets out a few sighs and ‘oooh’s, but it really doesn’t seem sexual, relaxing if anything."
                    riku "Mmm I knew it, your hands feel far better than a stallion’s."
                    riku "They have a firmness and yet softness."
                    riku "Fur on fur is rough, and awkward in comparison."
                    mc "You say that, but the touch of a mare feels incredibly soft to me."
                    riku "Maybe it’s just our contrasting textures that feel nice."
                    "This dare takes about five minutes, the two of us just enjoy the moment in silence. It’s not a hard dare, but we both enjoyed it, I guess that’s what matters."
                    show riku closeneutral with dissolve
                    riku "Phew, alright, that’s enough, all that tension is gone."
            mc "Your turn now, truth or dare?"
            riku "Alright, hit me with one of those spicy truths."
            menu:
                "What do I want to ask Riku?"
                "How many people have you slept with?":
                    show riku closehappy with dissolve
                    riku "Ooo, hitting me with a personal question like that."
                    riku "I like it though, keep them coming."
                    show riku closeneutral with dissolve
                    riku "Fortunately for me, I’ve only slept with two people because I’m not sleezy."
                    riku "I never understood those mares that have a different guy every week. Hah, where do they keep finding these losers anyway?"
                    mc "Looks like that question was too easy for you."
                    show riku closelaughing with dissolve
                    riku "Guess so, better luck next time [playername]. If you’ll even have a next time, hehe…"
                "What’s your dirtiest kink?":
                    show riku closeembarrassed with dissolve
                    riku "Woah, like… A naughty thing I like??"
                    mc "Yeah, a fetish."
                    show riku closeneutral with dissolve
                    riku "Gosh, I dunno, maybe dragons? They’re kinda cute, I reckon I could date one."
                    mc "That’s… Huh…"
                    "How do I interpret that? Interspecies sex is obviously extremely taboo where I'm from, but wouldn't it be normal here? I have literally no idea."
                    riku "Did I say something wrong?"
                    menu:
                        "Push her for a dirtier answer.":
                            mc "You misunderstood the question, I meant something naughty you like to do in bed, not in a partner."
                            show riku closelaughing with dissolve
                            riku "Ohh, you were being a pervert, I get it now."
                            show riku closeneutral with dissolve
                            riku "I like anal, how about that? Oh, and being choked."
                            "Nice. I’ll make a note."
                            mc "Yup, that’s a perfect answer. That was supposed to be a hard one, but you got it pretty easily."
                            riku "Like I said, I ain’t losing. You’ll have to try harder than that to phase me."
                        "Nevermind, she answered perfectly.":
                            mc "Dragons, right? Interesting."
                            mc "Sounds like one for the bucket list."
                            show riku closelaughing with dissolve
                            riku "Pfft, hahah, right… It’s already on my bucket list."
            show riku closeneutral with dissolve
            riku "Truth or dare? Oh, hang on, I’ll get us another drink."
            "The atmosphere is nice, and we’re a few drinks in."
            "She goes and gets another two out and passes me one, mmm, this stuff is delicious."
            "Her last truths and dares have been so easy. But mine haven’t exactly been difficult either. I wonder what she’ll give me this time."
            menu:
                "Here we go again"
                "Truth":
                    show riku closeneutral with dissolve
                    riku "Okay, time for a tough question…"
                    show riku closeshy with dissolve
                    riku "Damn, you’re new here so there aren’t many good questions I could ask you."
                    riku "I really want to ask you a question like ‘What mare do you want to sleep with most’, but maybe that’s too easy, and maybe there aren’t many mares you know."
                    mc "True, I only know a few."
                    show riku closehorny with dissolve
                    riku "But… You know me, don’t you? What do you think about me, would you fuck me?"
                    "I struggle to hide my surprise as she asks that. I wonder if what she was saying earlier was just a phony build up to that sudden question."
                    "There’s more than meets the eye to Riku though. She knows how this game works, she doesn’t care what I say. She’s just trying to pressure me with the most awkward question she can think of."
                    riku "What’s the matter, neko got your tongue?"
                    mc "Nah, I can answer this, it’s not embarrassing at all."
                    show riku closeembarrassed with dissolve
                    riku "Oh?"
                    mc "I mean yeah, of course I’d fuck you- in the right circumstances."
                    mc "You’re an attractive mare, and a catch on top of that, I’d be lucky."
                    riku "In the… Hmph."
                    "She’s blushing, somehow despite the fact she was trying to embarrass me, the opposite ended up happening and now she’s flustered."
                "Dare":
                    show riku closelaughing with dissolve
                    riku "Alright, here’s a dare that you’re going to hate."
                    show riku closeneutral with dissolve
                    riku "I dare you to get on your knees, then suck and lick my toes."
                    mc "Your toes?"
                    show riku feet1 with dissolve
                    "She brings her knees together and lifts her feet, her toes wiggling as she does so."
                    riku "What’s the matter, too gross for you? Just give up then!"
                    mc "Yeah, that’s pretty gross, you’ve been walking around bare foot all day."
                    riku "I had a post-gym shower only an hour ago. So, I’m all clean for your mouth [playername], now get sucking or get slaving!"
                    mc "Alright… Fine. It’s truth or dare, whether I like it or not."
                    "I shuffle around to orientate myself with her toes on the sofa."
                    mc "I am so getting you back for this one."
                    "Her toes are bright red and fluffy, no odour at all thankfully, you can tell she’s washed recently."
                    "I take a deep breath before placing her big toe in my mouth and starting to suckle on it."
                    riku "Ewwiee, you were supposed to refuse this one! You’re actually doing it!"
                    "I can’t help but giggle internally as Riku squirms."
                    "I pop her toe out of my mouth and do the licking part of the dare, across all five of her fluffy bean toes."
                    show riku feet2 with dissolve
                    riku "Uwaahh, it’s like a wet slug sliding up and down!"
                    "Fortunately, no hair gets in my mouth, but I’m still looking forward to washing this down with a lot of cider."
                    riku "Ahhh, okay, okay, that’s enough!"
                    show riku closeembarrassed with dissolve
                    "With only five of ten toes serviced, she’s too embarrassed to go on and pushes me back."
                    "The dare that was supposed to torment me ended up having the opposite effect."
                    "Although I admit that one hurt my ego, a little cider can wash away the hurt."
            show riku closeshy with dissolve
            "It’s becoming apparent that either Riku is bad at giving me difficult truths or dares, or I’m just a psychopath that’ll do anything to torment the poor girl."
            riku "Mmm shit, it’s my turn again? It feels like I just had a turn."
            mc "Certainly is, truth or dare?"
            riku "Ahh damnit, uh, dare?"
            menu:
                "I dare you to tongue kiss me anywhere you choose for 30 seconds.":
                    "She gulps and her eyes scan all around my body as she tries to think of the least harmless place to do it."
                    show riku closeembarrassed with dissolve
                    riku "I guess this is my just desserts for that previous round."
                    mc "You bet it is, where are you going to do it?"
                    show riku closeshy with dissolve
                    riku "Mm, maybe I should keep it above the chest, that way it’s not too lewd, hehe…"
                    "Silently I shuffle closer and look away in an expectant manner."
                    show riku closesatisfied with dissolve
                    "In my peripheral vision I can see her lean in and then suddenly against my neck I can feel her soft lips pursed."
                    "And then, the hot tongue swirls outwards followed by her lips sucking against my neck."
                    mc "Don’t leave a mark."
                    riku "Mmphh… Yeah…"
                    "She stops sucking and just licks my neck from now on. She does in fact stray away from the original position, starting to lick up and down the length of my neck. Over eagerness, or perhaps misinterpreting the dare."
                    show riku closeneutral with dissolve
                    riku "Mmm, hash it bween thwirty sethonds?"
                    "She mutters with her tongue awkwardly shimmying up and down my neck."
                    "She then gives my neck one last kiss before leaning back and winking at me."
                    show riku closelaughing with dissolve
                    riku "Too easy!"
                "I dare you to suck on my finger and pretend you’re performing oral sex for 30 seconds.":
                    "She gulps and her eyes look down at my hand which I then raise before pointing my index finger at her."
                    show riku closeembarrassed with dissolve
                    riku "I guess this is my just desserts for that previous round."
                    mc "You bet it is. Don’t half ass it, my finger is tough to please."
                    show riku closelaughing with dissolve
                    riku "Hmph, yeah right, let me at him. He won’t last 30 seconds with my technique."
                    show riku closesatisfied with dissolve
                    "She leans forward and takes the full length of my index finger in her mouth. I can immediately feel her tongue at the tip playing around as her lips move back and forth."
                    "Obviously it doesn’t feel pleasureful at all, but it’s so erotic."
                    "Her eyes are closed, and she’s completely in the zone. I can’t help but imagine how good it would feel if she were doing this to my actual cock right now."
                    "For the last few seconds she pulls out, and pretends to jerk my finger off while she sticks her tongue out. As if pretending she’s getting a facial."
                    "This would be the part where I’d laugh, but I’m too turned on to see the funny side."
                    show riku closehappy with dissolve
                    riku "All done, way too easy."
                    mc "Good job, I could definitely feel that you were an expert with your tongue."
                    show riku closeneutral with dissolve
                    riku "I don’t like to brag; but my tongue does that for me."
            show riku closehappy with dissolve
            riku "Truth or dare?"
            "I’m pretty turned on right now, I can’t think of anything I want to do other than a dare. If I’m lucky, it’ll be erotic, I have almost no doubt it will be at this point."
            mc "Dare, gimme your best."
            show riku closeneutral with dissolve
            riku "There’s nothing to give other than my best, especially after your last dare."
            mc "You can talk, I was going easy on you after what you just put me through."
            show riku closelaughing with dissolve
            riku "Is that so? Then you’re going to love this next one."
            show riku closehappy with dissolve
            riku "I dare you to lick my nipples, both of them until they’re erect"
            mc "That’s easy, gimme the tiddy."
            show riku closeneutral with dissolve
            riku "Not so fast, there’s a catch, you are absolutely not allowed to get erect."
            mc "Pfft, a failure state?"
            mc "So I have to get you erect, but I’m not allowed to get erect myself?"
            show riku closelaughing with dissolve
            riku "Exactly! Muhahaha!"
            show riku boobs with dissolve
            "She does a cute, fake evil laugh before pushing forward her tiny chest along with her tiny nipples."
            mc "Alright, should be easy, right?"
            "Since mares don’t wear clothes and their breasts are always on display. I should be desensitised enough by now."
            "That knowledge doesn’t make this dare any easier though, I feel like I genuinely would start getting erect if I didn’t mentally prepare myself."
            "Slightly drunk, definitely feeling some pheromones, slightly horny."
            "Licking the nipples of a cute nude girl."
            "But I am absolutely not allowed to get a boner."
            "Riku is giggling to herself as she notices me mentally preparing, her breasts still pushed out towards me."
            "I bring my mouth to one of her nipples and start to lick, just licking it."
            "It takes approximately seven seconds to get a nipple erect, and I’m sure boners can take longer than that."
            "As I lick the first nipple something terrifying and unexpected happens though, she moans."
            "Hot, erotic, moaning."
            "I can feel a heat in my loins, blood responding immediately, and precum dribbling."
            "If I’m going to win this round, I’ll need some strategy."
            "Fuck it, I’m going to move to the second nipple early, the first should get erect in a few seconds even without my tongue touching it, that way I can turn this dare from 14 seconds to only about 8."
            "Every second counts."
            "After licking her second nipple for a few seconds I pull away, and Riku giggles."
            show riku closelaughing with dissolve
            riku "That didn’t take you long at all, there’s no way they can be erect already!"
            "She says that and goes to check, to her surprise they’re both erect."
            show riku closeembarrassed with dissolve
            riku "Oh shit, you actually did it? I had no idea nipples could get erect that fast!"
            "She then averts her gaze from her pink erect nubs to my pink unerect nub."
            show riku closeneutral with dissolve
            riku "It… grew a tiny bit…"
            mc "Yeah, but it’s not an erection."
            show riku closelaughing with dissolve
            riku "Damn, I guess you showed me on that lil’ erection race."
            show riku closeneutral with dissolve
            riku "Guess that makes it my turn, I pick dare- hey wait a minute, your dick, it’s still growing!"
            mc "Hey, it’s rude to stare!"
            riku "Hmph, if you were a stallion, you’d be rock hard by now. Maybe mare pheromones aren’t as strong on your species."
            mc "It’s too late now, I’m thinking of a dare for you."
            riku "Ohh, a male with an erection is thinking of a dare for me? I can already predict the perverted result, hahaha."
            mc "Hey, I’m still not erect, only semi. Don’t get too eager now."
            show riku closelaughing with dissolve
            riku "Pfft, me, eager? Yeah, right!"
            stop music fadeout 30.0
            show riku closehorny with dissolve
            riku "Gonna need another cider for this one."
            "She heads off to the kitchen to prep us another drink."
            show riku closeshy with dissolve
            riku "Yo, we’re out of cider, want me to mix up a spirit with soda?"
            mc "That sounds very alcoholic, but hit me up."
            "She comes back with two glasses of some kind of pony derivative of cola, it’s so sweet I can barely taste the alcohol."
            "But! I can still taste the alcohol, and I can tell that this is some strong stuff."
            "Riku has a really small frame, I wonder how drunk exactly she is? She has been getting notably gigglier as the night as gone on."
            show riku closelaughing with dissolve
            riku "Alright nipple-licker, what’s my dare?"
            mc "Nipple-licker? This is coming from the self-proclaimed licking expert."
            show riku closeneutral with dissolve
            riku "Oh yeah? You wanna test me again on my licking skills?"
            riku "I can lick your nipples too, hehe."
            mc "Actually I have something else you can help erect."
            show riku closeembarrassed with dissolve
            riku "Ooooooooohhhhhhh…"
            "She’s surprised and wide eyed, but notably not embarrassed. She remains composed and takes a sip of her soda."
            mc "I don’t even need to say it, do I?"
            "She looks down in between my legs and nods"
            show riku closehorny with dissolve
            riku "That thing? Erect? Sure, easy peasy."
            riku "I could probably get it erect just by staring at it."
            mc "You probably cou- ooh…"
            play music sex1 fadein 3.0
            scene rikub blowjob
            show riku blowjob1
            with dissolve
            play ambience blowjob fadein 3.0
            "She cuts me off by laying down on the couch and positioning her head just above my thighs. She uses one of her hands to redirect my currently half-limp shaft towards her mouth and hence tongue where she begins to lick."
            "Her tongue wriggles up, down and around the tip of my cock. Her pleasureful assault on the most sensitive area causes me to get fully erect in almost seven seconds."
            show riku blowjob3 with dissolve
            "She closes her eyes and licks all around the growing shaft."
            "She doesn’t move her head back as it grows, causing it to grow into her mouth in an erotic display."
            "Her lips wrap around my shaft, and she slowly pulls herself back, leaving the area that was in her mouth glisteningly wet."
            stop ambience
            stop music fadeout 3.0
            scene bg barupstairs
            hide rikub blowjob
            show riku closehorny
            with dissolve
            "She lays there for a few seconds admiring her work, watching as my erection throbs."
            "I can see her tail swishing in the corner of my eye. I’ve noticed mares do that when they’re really horny. Their tails swish off to the side, as they subconsciously flash their ass and present themselves."
            riku "Could you imagine me sitting on your lap now? Hehe, you shouldn’t, you shouldn’t…"
            "She sits back up, and then sinks down lazily into the sofa with a smug expression, and then takes another sip of her soda."
            "I follow it up with another sip too. As I put my glass down, she leans forward and lays against me shoulder to shoulder."
            "She’s officially in the horny mare stage, her eyes are slightly glossed over and she’s trying to touch me every chance she gets."
            riku "Uuhmm, truth or dare?"
            mc "Got another dare for me?"
            show riku closeneutral with dissolve
            riku "Yesh *Nod, nod*, I want you to…"
            "She looks at my shaft, it’s starting to soften, albeit slightly."
            show riku closehappy with dissolve
            riku "Hahaha, it looks so sad sagging over."
            menu:
                "Want to cheer it up?":
                    show riku closeneutral with dissolve
                    riku "It’s kinda cute when it’s sad, I like watching it move around and throb."
                    show riku closehorny with dissolve
                    riku "Maybe I can cheer it up indirectly, hehe."
                "It just wants to find a nice, warm place to cum in.":
                    show riku closeneutral with dissolve
                    riku "Hehe, it’s sad because it knows it won’t have a chance."
                    show riku closehappy with dissolve
                    riku "If I’m going to make you lose this game of truth or dare, I can’t give you a dare you’re gonna enjoy, stupid penis!"
            show riku closehorny with dissolve
            riku "I dare you to... Uhm, be my pillow for this and the next dare!"
            mc "What are you implying Riku? You can sit on my lap if you want."
            riku "Nooo, no!"
            show riku closehappy with dissolve
            riku "I’m gonna sit on your face dummie, I wanna watch to see if your thingy gets bigger or not."
            play music sex1 fadein 3.0
            "She takes a sip of her soda before pushing me down, I haven’t even accepted the dare yet, she isn’t even giving me a chance to fail and she’s already halfway through straddling me."
            show riku facesitting2 with dissolve
            "Before I know it, the small red mare’s pussy is pushed right in my face, without a care in the world."
            "She’s absolutely drunk."
            "Her hips kinda swag back and forth playfully in a half-hearted grind on my face."
            riku "Oh my gosh, your penis is getting harder again! It’s so cool how it does that."
            riku "I think it’d be cool to have one of those for a day, just a day! Hahah."
            riku "Oi, why aren’t you licking?"
            mc "You never asked me to lick!"
            "My reply is muffled from between her thighs."
            riku "Oh what, how did I mess that up? I meant to... Oh man, I really screwed that up."
            riku "Stupid heat, it’s so hot…"
            "Looks like her heat was worse than she initially expected, hanging around a guy all day, and playing dumb games has gotten her really riled up."
            "Her pussy is wet with a sheen of her lubricant; she is more than ready to fuck, and her arousal is only going to increase from here on."
            riku "Waaait a minute, how did this happen?"
            riku "How did I end up sitting on your face while you have an erection, this is so lewd!"
            mc "This was your dare!"
            riku "Ohh, right…"
            riku "I’m not a slut you know, I’m not usually this forward, it’s just… it’s just, you’re really nice…"
            mc "It’s just a game, right? You don’t want to lose."
            riku "Haha, but I also really want that cock inside me right now."
            riku "No Riku, no, these are the tactics of the enemy."
            riku "Gotta focus! I’m not a slut."
            "While she’s having her internal struggle with logic and heat, her hips are gyrating back and forth, thankfully not mushing against my face, but it’s a fun sight from down here."
            "I decide to break the silence in the best way."
            mc "Truth or dare, Riku?"
            riku "Dare, duh! You gotta stay down there for this one."
            riku "Unless you dare me to move… Or something… That’d be lame though."
            "What should I dare her now? It’s hard to think straight when she’s sitting on my face."
            "Am I just trying to have sex with her, or am I trying to get her to be my slave? Surely there’s a dare or two that can give me the best of both worlds."
            riku "It’s throbbing, are you having lewd thoughts?"
            mc "I’m thinking of all the dares I could give you."
            mc "How am I supposed to escalate from here, if feels like if I asked you for sex, you’d do it."
            riku "Pfft, no!"
            riku "Okay, actually I would, but only for the game."
            mc "Exactly, so I need to make you feel weird."
            riku "I’d like to see you try!"
            mc "Alright. I dare you to call me daddy, and roleplay that your heat is so bad you’re trying to seduce your dad."
            riku "Aw for fucks sake, that’s weird."
            show riku closeshy with dissolve
            "She gets up off my face and sits back down on the sofa pouting, I sit back up also."
            riku "Hmm… Daddy, right?"
            mc "Yup."
            "She takes a final sip of her soda; it’s all gone now. I’m only halfway through mine."
            show riku closeangry with dissolve
            riku "I’m gonna make you one hell of a slave when I get my chance, ‘daddy’."
            mc "Don’t forget the roleplay!"
            show riku closeembarrassed with dissolve
            riku "Eugh, you’re making me choke up."
            riku "Eh-hem… Ahhh, ehhh…"
            show riku closeshy with dissolve
            riku "EH-HEM, daddy, I’m so hot and horny. I need daddy’s big cock…"
            mc "You can always dare me for it."
            show riku closeembarrassed with dissolve
            riku "No way daddy, I’m going to make you suffer!"
            riku "You’re going to pick dare, right?"
            mc "Yeah, a truth would be too boring to pick right now."
            show riku closeneutral with dissolve
            riku "As usual, I like your style- eh, daddy."
            "Her legs spread slightly; her pussy is nearly running."
            "I think this girl has a daddy fetish, actually, most modern girls do. In retrospect that dare wasn’t as effective as I thought."
            show riku closeshy with dissolve
            riku "Euuuuugghhhhh…"
            riku "I can’t stand this any longer daddy, I don’t even care about winning right now, I just wanna get fucked."
            mc "What’s my dare going to be then?"
            riku "I dare yooouuu, to get over here, between my legs and fuck me! --- daddy!"
            riku "BUT! You’re not allowed to cum until I’ve had two orgasms. I’ll play fair and tell you when I’ve had them."
            riku "Daddy needs to take loving care of his daughter in heat after all."
            scene rikub sofasex
            show riku sofasex1
            with dissolve
            "She lays forward on the sofa, presenting her ass. Her eyes glossed over and expectant."
            "I’m still partially erect, horny as fuck too. I waste no time crawling behind her and positioning my shaft against her entrance."
            riku "Mmm, fucking finally, haven’t had a good dicking all heat."
            mc "One more slip up like that, and you’ll fail your dare!"
            riku "I mean… Oh gosh, daddy, your cock is so big, I want it inside me!"
            "Her actual personality contrasts pretty heavily with her cheesy daddy roleplay, both lines are hot though."
            play ambience sex fadein 3.0
            show riku sofasex2 with dissolve
            "I push myself inside of her and immediately start moving my hips back and forth."
            show riku sofasex2 with dissolve
            riku "Aahhh, ahhh, don’t you dare cum!"
            show riku sofasex2 with dissolve
            "She’s right, I need to restrain myself slightly, I slow down a little and fuck her gently."
            "The long hard thrusts drive her wild, despite her small tits, her rump is thick and juicy."
            show riku sofasex2 with dissolve
            riku "Mmm daddy- Aahhh, that’s good…"
            "She’s so soaking wet, every time I sink deep inside of her it’s accompanied by a saccharine squelching sound."

            show riku sofasex3 with dissolve
            riku "I’m such a horny bitch for you, Daddy!"
            riku "Ahh, I’ve been wet and wanting to spread my legs for you ever since we left the gym, I really am such a nasty slut."
            "I can’t tell what’s roleplay and not anymore, she’s probably just rambling through the pleasure."
            riku "Spank me daddy, spank your little slut."
            "She guides my dominant hand and brings it to her ass, I know exactly what to do."
            show riku sofasex4 with dissolve
            play sound spank
            riku "I like it hard daddy, aahhh…"
            "I raise my dominant hand and bring it down powerfully causing a slap sound, this seems to hit the spot as her eyes roll back and she lets out a satisfied moan."
            show riku sofasex4 with dissolve
            riku "Ohh phuck yesh…"
            "I can’t help but fuck a little faster, her hips are rocking in response to each thrust too, and her pussy squeezing even tighter around my cock."
            show riku sofasex4 with dissolve
            riku "Aaahhh, aahhh, ah, ahhh! Daaahhhdddyy, I’m coming!!!"
            show riku sofasex4 with dissolve
            "Spanking her out pushed her over the edge, and she starts to have a strong first orgasm, her hips bucking and her whole body squirming as the pleasure overwhelms her."
            show riku sofasex4 with dissolve
            "I can feel my cock throbbing in response to her pussy contracting around it, I really could come any second if I let my guard down."
            show riku sofasex4 with dissolve
            riku "Faster Daddy, faster!  Ahhh, ahh! *Pant, pant*."
            show riku sofasex4 with dissolve
            "It doesn’t help that she’s rocking her hips into me, practically fucking me just as hard as I’m fucking her, and damn it feels amazing."
            show riku sofasex4 with dissolve
            riku "Mmphh fuck! Spank me harder! *Pant, pant*."
            show riku sofasex4 with dissolve
            play sound spank
            pause 0.4
            play sound spank
            "I spank harder, while her pussy squeezes and sucks tighter around my shaft as if it’s trying to milk my cock. All whilst Riku moans and squeaks with erotic delight."
            show riku sofasex4 with dissolve
            "My orgasm keeps swelling up, I can’t hold back much longer, I’m going to lose…"
            show riku sofasex4 with dissolve
            "Just when I think all hope is lost, Riku arches her back, her eyes roll back and she lets out a sensational moan, is she having an orgasm?"
            show riku sofasex4 with dissolve
            show riku sofasex4 with dissolve
            riku "Mmm, coming daddy!"
            show riku sofasex4 with dissolve
            show riku sofasex4 with dissolve
            "Yes! Immediately I feel myself climaxing as well, my cock throbs and swells as my vision turns cloudy and my mind fogs up."
            show riku sofasex5 with cum
            play sound cum
            show riku sofasex5 with cum
            play sound cum
            "The two of us orgasm together, my cock unloading copious amounts of cum deep inside Riku’s pussy all whilst we fuck each other passionately."
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
            if crystalballactivated == 1:
                $ crystalballactivated = 0
                jump cbmenu
            show riku sofasex6 with dissolve
            mc "Oh shit, did I overdo the spanking?"
            "I say as I pull away, although before I can escape she pulls me in close for a cuddle."
            scene bg barupstairs
            show riku closesatisfied
            with hpunch
            riku "Haahh, that was awesome, you came around the same time as me, so I don’t know who won, but… I think we’re both winners tonight."
            mc "It’s a draw?"
            show riku closeshy with dissolve
            riku "Naahh, nahh... I’m going to forfeit and let you win, you deserve it."
            mc "You’re giving up after everything you said? Are you sure?"
            show riku closesatisfied with dissolve
            riku "Mhhmm, I don’t wanna play anymore, I need a nap."
            "I think the combination of alcohol and sex has exhausted the poor girl; she’s practically falling asleep as we’re cuddling."
            mc "I need to head home, I’ll see you again another day, okay?"
            show riku closeshy with dissolve
            riku "Mehhh meh, you could stay… but… buh-bye."
            "I give her a quick kiss on the cheek, leaving her with a blush, and a smile. I clean up and then slip out the back door of the bar, making my way back home."
            play ambience ambiencenight fadein 3.0
            scene bg black with dissolve
            "…"
            if crystalballdayactivated == 1:
                $ crystalballdayactivated = 0
                jump cbmenu
            if livingwithmoxie == 1:
                show bg moxiewagonlamp with dissolve
                play music wagon fadein 3.0
                "It’s a little later than usual at 6:00pm, but I should still be in time for dinner."
                mc "Good evening Mox."
                show moxie laughing with dissolve
                moxie "Hello, you’re a little late [playername]!"
                mc "Yeah, I was working in the bar. It gets a little hectic around this time."
                show moxie althappy with dissolve
                moxie "Ooohh, I can imagine. Did Riku keep you for a little longer in exchange for more pay?"
                mc "Something like that."
                show moxie smug with dissolve
                "Moxie’s smug all-knowing look is all the confirmation I need to realize she knows exactly what might have happened."
                "I’m gonna take the opportunity to ask Moxie a question, another dose of her wisdom never hurt."
                mc "Will any mares get mad at me for sleeping around?"
                show moxie neutral with dissolve
                moxie "Hm? Of course. Ponies can get mad at you for anything."
                mc "I mean more specifically."
                show moxie happy with dissolve
                moxie "Heh, of course. There are indeed some mares that get a little pissed off at stallions that throw their weight around."
                show moxie happyneutral with dissolve
                moxie "It is easy for a stallion to get sex, or a girlfriend, and that does annoy some mares."
                mc "Yeah, I can empathise with that."
                moxie "Even though that’s the case, if you’re just respectful and as you say, empathetic about it, you shouldn’t have any problems."
                show moxie althappy with dissolve
                moxie "Also, sometimes the best scenario is simply to seal your lips."
                mc "Keep it to myself?"
                moxie "Yeah, what people don’t know won’t hurt them. As long as you’re not maliciously withholding something important."
                mc "Riku was pissed at an old friend she used to sleep with, because he slept around, but not pissed at all on the implication that I might be doing the same thing."
                show moxie neutral with dissolve
                moxie "I guess sleeping around wasn’t the thing that pissed her off, it was something else."
                moxie "But I guess it's easy for me to say that, since I don't mind our loose relationship. Would you get annoyed if I slept with another?"
                mc "I couldn’t justifiably be annoyed, but…"
                show moxie bashful with dissolve
                moxie "There’s always a tinge of jealousy, isn’t there?"
                mc "If someone like Riku did that, I wouldn’t mind at all."
                mc "But, then I think about you."
                show moxie althappy with dissolve
                moxie "Heh, I’m not sleeping around."
                mc "I am though, doesn’t that hurt?"
                moxie "It’s okay, you know I don’t mind."
                "She says that steadfast, it’s just like her to stay strong when faced with a question like that."
            elif livingwithbutters == 1:
                scene bg buttershousenight with dissolve
                play music butters fadein 3.0
                "It’s a little later than usual at 6:00pm, but I should still be in time for dinner."
                mc "Hey Butters."
                show butters dresslaughing with dissolve
                butters "Good evening Master!"
                mc "Master? That’s a new one. Between that and daddy I seem to be building a harem of submissive girls."
                show butters dresssurprised with dissolve
                butters "What do you mean?"
                mc "Oh well, I was just at the bar and Riku seems to like calling me daddy."
                show butters dressneutral with dissolve
                butters "Ooohh my, how lewd…"
                mc "What do you think about me sleeping around?"
                show butters dresshappy with dissolve
                butters "Hm? I don’t mind, I think sharing partners is partially biological for mares. Although not that common."
                mc "What if we were to take things more seriously?"
                show butters dresslaughing with dissolve
                butters "Heh, of course if we got married, I wouldn’t want you to sleep around."
                show butters dresshappy with dissolve
                butters "Sure, there are some mares that would be okay with that. But most? Probably not."
                mc "Riku was pissed with an ex-friend with benefits, because he slept around, but not pissed at all on the implication that I was doing the same thing."
                show butters dressneutral with dissolve
                butters "Hmm… Is there anything else that may have annoyed her?"
                mc "I guess sleeping around wasn’t the thing that pissed her off, it was the approach and events surrounding the sleeping around."
                butters "Would you be particularly annoyed if any of the mares you’ve been with slept with a stallion?"
                mc "I couldn’t justifiably be annoyed, but I can see how it’s be a touchy subject."
                butters "Ohh yeah…"
                show butters dresslaughing with dissolve
                butters "You’re kinda naughty, you know? Sleeping around with lots of mares, you’re putting us in a difficult situation!"
                mc "Sorry about that. You’re welcome to sleep around too."
                show butters dresshappy with dissolve
                butters "Me? I couldn’t risk the succubus emerging, don’t worry about it [playername], you’re doing me a great favour."
                mc "I’m glad you see it that way."
            scene bg black with dissolve
            "…"
            stop music fadeout 3.0
            jump evening
    label barvisit2:
            "I can’t resist going back to the bar again today. I set off early, a long time before the bar opens, because Riku insisted we spend the mornings hanging out as friends."
            "She forfeited the truth or dare game meaning today she has to be my slave."
            "I can feel a tingling in my loins at the mere thought of all the degenerate stuff I’m going to make her do today."
            scene bg baroutside with dissolve
            "I arrive and knock on the door, Riku soon opens up and welcomes me in, she seems cheerful."
            play music day2 fadein 3.0
            show bg bar with dissolve
            show rikub
            show riku happy
            with dissolve
            riku "Wassup [playername]?"
            mc "Same old, same old, how about you Riku?"
            show riku happy with dissolve
            riku "I’m heckin’ good. My memory is a little fuzzy from that game…  I passed out on the sofa, but I can’t remember when."
            show riku neutral with dissolve
            riku "We fucked, right? My heat is sorted out, and…  Uh…I’ve been feeling more myself and energetic."
            mc "Yeah, I was pretty drunk too. You don’t mind that we slept together?"
            show riku shy with dissolve
            riku "Kinda do, kinda don’t."
            show riku happy with dissolve
            riku "I thought to myself if I enjoy it, fuck it, right? Literally."
            riku "I don’t need to hold myself up to some high standard, if it feels right at the moment, I can just let go."
            mc "That’s a pretty hearty lesson you’ve learnt, I thought you were against sleeping around."
            show riku neutral with dissolve
            riku "Yeah, I’m in a weird transitional period of my life where I’m trying to figure things out. I'm trying to stay open minded, and trying to make myself experience new things that I never got the chance to as an athlete."
            show riku laughing with dissolve
            riku "I do kinda wish you stayed the night though… I woulda given you a blowjob in the morning and everything."
            mc "Sorry about that, I didn’t want to stay and be a nuisance, and it was getting quite late."
            show riku happy with dissolve
            riku "Don’t worry about me, you’re doing your own thing. I’m just one helping hand-job along the way, haha."
            show riku shy with dissolve
            riku "Don’t tell anyone what we did though, I was a little too drunk to really think that one through. I would have preferred to wait a little longer."
            mc "Sure thing, my lips are sealed..."
            riku "What happened, happened though, and I’m glad it did since it quashed my dumb heat."
            show riku happy with dissolve
            riku "Bet you never imagined sex would be part of your employment benefits. That’s your own darn fault for being too sexy for your own good!"
            mc "Me? Sexy? You gotta be kidding!"
            show riku laughing with dissolve
            riku "Are you doubting my standards? Hmm?"
            mc "No, no, not at all! I’m sexy, I got it."
            mc "So what’s on the agenda today, and how is this slave thing going to play out?"
            show riku shy with dissolve
            riku "Slave…?"
            show riku embarrassed with dissolve
            riku "Awhh man, I forgot! Don’t tell me I forfeit that to you at some point during the evening?"
            show riku shy with dissolve
            riku "I’m such a dumbass, I was supposed to make you my slave, not the other way around. How the hell did drunk me give up so easily?"
            mc "You were so sleepy after the last dare, that’s probably what did it."
            riku "Ahh… Yeah that was it, I get sleepy after an orgasm, I probably didn’t even realize I was agreeing to the slave thing."
            riku "It was probably one of those situations where I would have just nodded and agreed with anything and just tried to sleep."
            mc "Yup, you didn’t just lose, you agreed to be my slave."
            riku "How aggravating, I could have beaten you in that game, easily!"
            riku "I clearly wasn’t feeling myself, I let you off easy."
            mc "Sounds like you really wanted me to be your slave."
            show riku neutral with dissolve
            riku "Kinda, I thought it’d be fun."
            riku "But now it looks like I’m the one that has to follow all your orders, which could be fun too…"
            mc "So, I can give you orders?"
            riku "Yup, fair and square, I’ll do anything you want..."
            mc "Anything?"
            show riku horny with dissolve
            riku "Anything for you…"
            "Hmm… So, what would we do today If it was a normal day?"
            "We would go to the gym, then we’d come back here to work, and then we’d probably have some fun."
            "But what if I were to radically change that course of events? I could do anything right now."
            mc "Alright, how about we ditch this joint and head to the boutique to get you some proper slave clothes?"
            show riku embarrassed with dissolve
            riku "Wha? What do you mean by slave clothes?"
            mc "You’ll see, I’m sure I can pick you out a nice outfit."
            riku "Hmph, I don’t know what you’re planning, but by the sounds of it I should call Velour to cover my shift."
            stop music fadeout 3.0
            scene bg black with dissolve
            "…"
            show bg arcadiasuburbs with dissolve
            "She makes a quick call and we leave the bar, today is going to be a wild adventure!"
            show rikub
            show riku neutral
            with dissolve
            riku "No gym today?"
            mc "Don’t worry, you’ll still get your workout."
            show riku embarrassed with dissolve
            riku "Uuu, the heck is that supposed to mean?!"
            menu:
                "Today we’re going to write giant graffiti over the biggest tower in Arcadia castle.":
                    pass
                "We’re going to fuck all day. *Make eye contact* ALL. DAY.":
                    pass
                "I’m going to put you in a jar and jack off into it":
                    pass
            riku "Uhh, really?"
            mc "No, not really."
            mc "There’s no fun in telling you everything."
            show riku shy with dissolve
            riku "Pfft, I’m still going to be difficult and sassy, even while I’m doing your orders."
            "When did she become so tsundere? I guess that isn’t the right word, she’s being a brat because I’m about to make her do tons of embarrassing stuff."
            scene bg boutiquedoor with dissolve
            "The two of us arrive at the boutique, right as it opens."
            if boutiquevisit3 == 1:
                "I’m glad I helped out at the boutique before, with the dress bought and prepared, the trap is set!"
            play music boutique fadein 3.0
            scene bg boutiqueinside with dissolve
            show rikub:
                xpos 250
                ypos 50
            show riku neutral:
                xpos 250
                ypos 50
            show ruby happy:
                xpos 750
                ypos 25
            with dissolve
            "We step inside the boutique shop floor and we’re greeted by Ruby. Riku seems somewhat cheerful right now, let’s see how long that lasts."
            riku "Hey Ruby, how’s life treating you?"
            show ruby laughing with dissolve
            ruby "Wonderful darlings, and how are you two on this lovely morning?"
            riku "That depends on what he says."
            mc "Well, Riku and I are looking for a particular outfit."
            if boutiquevisit1 == 1:
                show ruby happy with dissolve
                ruby "Is that so? I’d be more than happy to help, [playername]."
            show ruby neutral with dissolve
            ruby "Hmm… But this boutique makes a specific selection of clothes, I don’t know if they would really suit Riku."
            show riku shy with dissolve
            riku "You’re totally right Ruby, you said it first."
            riku "Love your stuff, totally not my style though."
            mc "That’s why you’ll look so adorable Riku, the clash!"
            show riku embarrassed with dissolve
            riku "Guh, adorable? The heck are you thinking in that noggin of yours?"
            show ruby laughing with dissolve
            ruby "My, my, are you just going to pretend you haven’t shopped here before, Riku?"
            riku "Shut up! I have not!"
            show ruby happy with dissolve
            ruby "Oh but darling, it’s important that I inform him about your recent purchases so we can find what’s right for you."
            ruby "She picked out this adorable lingerie piece and tried on some cute dresses!"
            mc "Ahah, dresses? And here I was worried Riku didn’t like dresses."
            show riku shy with dissolve
            riku "Meh, what about a dress?"
            mc "I’d like a maid dress."
            show ruby laughing with dissolve
            ruby "Ohoho, really? Delightful!"
            "The sharp Ruby quickly puts the pieces together, the dress I bought earlier was for Riku all along."
            ruby "I’d do that one for 'free' if she could tidy up the boutique a little."
            if boutiquevisit1 == 1:
                ruby "I’m sure you’d rather see that instead of cleaning it up yourself, again, [playername]."
            "Ahaha, I love this girl."
            mc "You serious? I think that’s a great offer, what do you think Riku?"
            riku "Uhh… Do I have to?"
            mc "Yeah, I think so, that’s what you said right, Ruby?"
            show ruby happy with dissolve
            ruby "Goodness, I was jesting, although… Ohoh, how about you try on the dress first before tidying up, Riku?"
            "She heads up to a rack of dresses and picks out the French maid dress from before, it's perfect. It probably isn’t ‘french’ here though."
            show riku angry with dissolve
            riku "Hmph, fine, I’ll put on the stupid dress."
            hide riku
            hide rikub
            with dissolve
            "Riku gets dressed right in front of us, no need for changing rooms in this world!"
            play sound movement
            show rikub maid:
                xpos 250
                ypos 50
            show riku shy:
                xpos 250
                ypos 50
            with dissolve
            riku "Do I need to wear these dumb stockings as well? They’re useless things."
            mc "Stockings? Now we’re talking!"
            ruby "The ponies in the north wear these all the time to stay warm."
            riku "These aren’t even warm, they’re just see-through and sexy…"
            "Riku rolls her eyes as she slips on the stockings one leg at a time."
            show ruby horny with dissolve
            ruby "Sometimes wearing more is sexier than nudity dearie, you’ll do well to remember that when trying to please a man."
            show ruby laughing with dissolve
            ruby "It’s the same reason we wrap our presents during Frostmoon!"
            show riku angry
            with dissolve
            riku "Wearing clothes feels weird…"
            mc "I think you look great Riku, super sexy."
            show ruby happy with dissolve
            ruby "They serve a practical purpose too, now you can tidy up without getting dust coddled in your fur."
            show riku neutral with dissolve
            riku "Hmm, I never thought about it like that…"
            show riku shy with dissolve
            riku "Practicality isn’t enough to make me like it though! Too girly for me."
            show ruby closelaughing with dissolve:
                xpos 750
                ypos 100
            ruby "*Whispering to me* She says that, but she’s definitely the kind of mare to surprise her boyfriend with sexy, girly clothes."
            hide rikub
            show riku asstsun:
                xpos 0
                ypos 0
            with dissolve
            "Me and Ruby watch Riku clean up the boutique with surprising efficiency."
            "She doesn’t huff or fight it; she just gets on with the job."
            "It’d almost be boring if she didn’t regularly lift her tail and accidentally flash her rear."
            "Both me and Ruby would clearly peek, I could practically feel Riku rolling her eyes as she caught on."
            "Something about the dress and stockings makes this far sexier than if she had just been naked."
            menu:
                "Damn Ruby, you were right, the clothing really does accentuate her ass.":
                    show ruby closehappy with dissolve
                    ruby "I for one love the dark contrast of those stockings on her red cheeks, it’s so delightful."
                "I wouldn’t mind seeing you wearing something like this Ruby.":
                    show ruby closehorny with dissolve
                    ruby "Ohoho darling, you’ll have to see me in private for such a thing."
                    ruby "A lady never overshares."
            riku "I know you two are staring at my butt… Guess you’re not even trying to hide it at this point."
            ruby "That dress really brings out your ass! Perhaps you could order me to make a few dresses for your barmaids?"
            hide riku
            show rikub maid:
                xpos 300
                ypos 50
            show riku laughing:
                xpos 300
                ypos 50
            with dissolve
            riku "Dream on!"
            show riku neutral with dissolve
            show ruby neutral with dissolve:
                xpos 750
                ypos 25
            ruby "*Sigh* No one wants to buy clothes…"
            show ruby happy with dissolve
            ruby "Alright dear, you’ve done a wonderful job tidying up the boutique."
            ruby "You can keep the dress if you want, Melody wore it once then gave it to me to sell, but I’ve had {i}no luck!{/i}"
            show riku neutral with dissolve
            riku "I think I’ll wash it and return it, if that’s okay…"
            ruby "Honestly darling, keep it! You two lovers have fun now."
            show riku embarrassed with dissolve
            riku "L-Lovers?!"
            stop music fadeout 3.0
            play ambience ambienceday fadein 3.0
            scene bg worldmapdialogue with dissolve
            show rikub maid
            show riku embarrassed
            with dissolve
            "We step out of the boutique, Riku blushing from ear to ear, but you can tell under her embarrassment that she’s enjoying herself."
            mc "What do you think? A proper slave outfit."
            show riku neutral with dissolve
            riku "Props to your creativity, if this is only the first step to your plan looks like I’m in for more fun."
            riku "More fun, or enough embarrassment to traumatise me forever."
            riku "I’m glad Ruby played along; you’d assume that girl is uptight, but she’s playful."
            mc "Giving us the dress in exchange for some tidying up was quite the deal! I would have felt a tiny bit guilty making you pay for it."
            show riku shy with dissolve
            riku "Yeah well… It’s only one day."
            mc "Alright, let’s head to the wagon, you have some more cleaning up to do."
            riku "Wait, wha? Nooooo…"
            scene bg black with dissolve
            stop music fadeout 3.0
            "…"
            play music challenge fadein 3.0
            scene bg moxiewagonday with dissolve
            if livingwithmoxie == 1:
                "Moxie and I work all day, so while we’re not dirty people, mess can accumulate without our realising, especially dust."
                "By the time we get home in the evening, we’re too tired to give the wagon the nitty gritty tidy up it needs."
                "Notably since there’s no vacuum cleaner, one of us would need to get on our hands and knees to scrub the floor down."
                "Fortunately, I have the exact candidate to go on her hands and knees right now."
            else:
                "While I don’t currently live with Moxie, I bet she’ll appreciate a clean. She’s not a messy person, but she works all day and mess can accumulate rather easily."
                "By the time she gets home in the evening, she's too tired to give the wagon the nitty gritty tidy up it needs."
                "Notably since there’s no vacuum cleaner, she would need to get on her hands and knees to scrub the floor down."
                "Fortunately, I have the perfect candidate to get on her hands and knees right now."
            "If only Moxie was here to watch this amazing sight."
            show rikub maid
            show riku angry
            with dissolve
            riku "You want me to tidy up the wagon? Really? You can make me do anything, and this is what you chose to do?"
            mc "Yeah, slow build-up and all that."
            riku "Let me reiterate because you clearly don't seem to understand, you can make me do anything!"
            mc "Yep, I know."
            riku "Anything, anything!"
            "I sit down on the sofa and let out a hearty exhale."
            riku "You’re just gonna sit there, while I tidy up?"
            mc "Yep, I’ll get some nice upskirt views from this low angle."
            riku "I’ll show you some nice upskirt views you god damn perv!"
            hide rikub
            show riku asstsun
            with dissolve
            "She seems like she’s about to pull me in and choke me under her skirt, but she resists the urge, it would have been hot though."
            hide riku
            show rikub maid
            show riku angry
            with dissolve
            riku "Whatevs, I tidy up the bar a lot anyway, a dusty wooden wagon like this is easy work for maid Riku."
            mc "That’s a cute lil’ name you gave yourself there."
            riku "Yea I know, now stare at my butt while I sweep up, or something."
            mc "With pleasure."
            hide rikub
            show riku asstsun
            with dissolve
            "I lean back into the sofa and get really comfy while Riku tidies up and dusts."
            "As before it’s not hard to get a nice peek at her ass with her short skirt, only made shorter by her tail that causes it to constantly lift upwards."
            show riku assdere with dissolve
            riku "Ohh yeah, you like my butt don’tcha?"
            mc "Hell yeah, work it baby."
            show riku assdere with dissolve
            "I say that with the enthusiasm of receiving the best lap dance in the world, but all she’s doing is dusting a shelf. Still, I gotta encourage the girl!"
            show riku assdere with dissolve
            riku "I may not be packing much heat upstairs, but at least I have a damn good ass!"
            menu:
                "I love small boobs just as much as big ones.":
                    mc "Nothing wrong with adorable small boobies, I love them just as much as larger ones."
                    riku "Awh, you don’t have to say that just to impress me."
                    mc "I’m serious though."
                    riku "Wha, you like small boobs?"
                    mc "Yeah, they’re adorable!"
                    riku "Huh, I always thought men preferred bigger boobs. It’s not like I polled anyone though, I just assumed."
                "As an ass man, I adore your cute butt.":
                    riku "You do?"
                    riku "Lemme just inch my skirt up a little higher so you can appreciate it more."
                    riku "I think I heard once that boob size doesn’t matter, but butt size does!"
                    riku "So I’m lucky that I have a nice butt rather than the alternative."
                    mc "I think the general rule is… Your body is perfect no matter what, Riku."
                    riku "Pffthhh, you adorable bitch."
                    riku "If we hadn’t already slept together, I reckon that one would have sealed the deal."
                    mc "I try my best."
            show riku altass with dissolve
            "She’s finally tidied away a few things and dusted the shelves and table, it’s time for the floor. She wastes no time getting on her hands and knees, sticking her cute butt up and swishing her tail."
            "Fairly sure she’s working her ass on purpose right now; she’s enjoying every moment."
            riku "Damn, I haven’t tried this hard at something since I was an athlete, ahaha."
            mc "You mentioned that earlier, but I didn’t get a chance to ask. What did you mean when you said you missed your chance to be an athlete?"
            show riku asstsun with dissolve
            riku "Huh? You’re asking this now as I’m coughing up dust?"
            riku "Ahh, it’s a long story anyway, I wouldn’t want to bore you."
            mc "You can come and sit next to me; I’ll make you a drink. You deserve the break."
            hide riku
            show rikub maid
            show riku neutral
            with dissolve
            riku "Break? It’s been ten minutes, but I won’t complain."
            stop music fadeout 3.0
            scene bg black with dissolve
            "…"
            show bg moxiewagonday with dissolve
            show riku closemaidneutral with dissolve
            "She sits beside me and gently sips her fresh cup of tea. I spend a few moments answering her questions about me, and then we back-pedal to talking about her."
            riku "Haah, I hope you one up yourself after this maid stuff, make it a real memorable day."
            "I wonder how I’m going to do that? This maid stuff is pretty crazy already."
            show riku closemaidhappy with dissolve
            riku "Anyway, it’s nice getting to know you. No harm in telling you a bit more about me too."
            play music uhoh fadein 10.0
            riku "The athlete stuff is behind me now, but when I was younger, I really wanted to compete at a pro level. I’d always be in the top sports teams at every institution I took part in."
            show riku closemaidshy with dissolve
            riku "I wanted to be, y’know, an athlete."
            mc "Like, racing, but flying?"
            show riku closemaidneutral with dissolve
            riku "Yeah, exactly. In the same way some athletes run, a Pegasus can fly for sport. I always wanted to be the fastest! Even from an early age."
            riku "I wouldn’t just fly casually either; I’d really push myself. I’d time myself and try to beat myself over and over."
            riku "I’d fly long distance and go further every time. Pushing my speed, my endurance, my stamina."
            riku "I’d push myself until my body clicked, ached and blistered."
            mc "That sounds really intense."
            show riku closemaidhappy with dissolve
            riku "Of course, it had to be intense."
            show riku closemaidshy with dissolve
            riku "In these competitive areas, you’re either the best, or you’re nothing. You won’t earn a sustainable wage unless you win medals and get the sponsors."
            show riku closemaidneutral with dissolve
            riku "Hence, you had to practice as much as the best- no, you had to practice MORE than the best."
            riku "8 hours a day? Try 10, how about 12?"
            riku "How about waking up bleary eyed and training immediately for hours on end, until you’re so fatigued you can barely move."
            show riku closemaidshy with dissolve
            riku "That’s your life in such a dangerously competitive landscape."
            riku "Everyone is pushing themselves so hard to be the best. Beyond their limits, and particularly beyond what their competitors are doing."
            show riku closemaidangry with dissolve
            riku "If they train for 10 hours a day, you train for 10 hours and one minute."
            mc "That’s insane competition. If everyone is pushing themselves to do more just to surpass each other, that can’t be healthy at its peak."
            show riku closemaidneutral with dissolve
            riku "Healthy or not, I followed suit; I had a fiery passion that kept me going through the struggle."
            riku "I had a talent, small frame, small breasts. I’m naturally a speedster."
            show riku closemaidhappy with dissolve
            riku "And then, my dream! I achieved it! I got to join a team called the Lightning Bolts, it’s the best team in Arcadia."
            show riku closemaidlaughing with dissolve
            riku "I’m allowed to brag about that. Life-time achievement, and all that fuss."
            mc "Absolutely, brag to your heart’s content."
            show riku closemaidshy with dissolve
            riku "That’s where training became regimented, and it’s also where I started to somewhat lose heart."
            riku "That shit about pushing your limits, training longer hours…"
            show riku closemaidsad with dissolve
            riku "There were some ponies that were so desperate to go beyond pony limits that they resorted to doping and steroids."
            riku "Drugs were used to bolster your potential beyond its limit."
            riku "Lobbying along with some powerful people in the shadows allowed some teams to circumvent any drug tests."
            riku "All they care about is winning and earning money for their sponsors and shareholders."
            riku "So naturally these drugs were pushed on the athletes, especially the talented ones. We were just seen as tools, another means for the rich fatcats to live leisurely."
            riku "’Everyone is doing it’, I was told, ‘If you don’t do it, you’ll just be at a disadvantage’."
            show riku closemaidangry with dissolve
            riku "But I resisted, I didn’t want any of that shit."
            mc "That’s awful, the extent people will go to get a tiny edge in competition is ridiculous."
            riku "It wasn’t just the foul play of doping, there was also tons of bureaucracy and back-stabbing."
            riku "I decided that I would stay true to myself, and fight with the passion that had burned in my heart since I was a young girl."
            show riku closemaidshy with dissolve
            riku "However, the magic was slowly fading for me, I trained harder than ever and yet... I was falling behind my peers."
            riku "I had to put in extra hours to make up for it, and it worked for a while. But like I said, my body clicked, ached, blistered."
            riku "I’d have to take cold baths in the evenings to stop the ache."
            show riku closemaidsad with dissolve
            riku "It was awful, I was pushing myself so much harder every single day."
            riku "Barely had any time for friends, family, almost no time off."
            show riku closemaidshy with dissolve
            riku "That’s when I was starting to doubt myself, should I do the drugs? If I do… then… I could be one of the best."
            riku "A close stallion friend of mine always suggested I do it, he was a great guy, but a bit of a moron."
            "She goes quiet for a few seconds and turns away."
            mc "And, what happened then?"
            show riku closemaidsad with dissolve
            riku "I never even had the opportunity for that brief weakness in will."
            riku "One evening everyone else had already left the academy. Irresponsibly I was still training on my own because I was pushing myself too far."
            show riku closemaidshy with dissolve
            riku "During that training there was an incident, and my thigh cramped hard, it was extremely painful."
            riku "The cramp caused me to briefly falter in my flight, and almost immediatley I smashed into a tree trunk at a speed fast enough to kill me."
            show riku closemaidsad with dissolve
            riku "That same moron friend was staying late because he wanted to ask me on a date, saw me crash, thank god he did."
            riku "And yeah… I was going really fucking fast, I blacked out immediately and woke up in the hospital."
            riku "Only problem was… I lost a month; I severely injured my brain and spine."
            riku "If it wasn’t for the top health treatment I got as a member of the Lightning Bolts, along with magic, the damage might have been permanent too."
            show riku closemaidshy with dissolve
            "She lets out a really long sigh and sits back."
            riku "I was let out of the hospital, and I just kinda realized that I didn’t want to go back."
            show riku closemaidsad with dissolve
            riku "It was like all that passion had just dried up, and I was suddenly terrified at the idea of returning to the Lightning Bolts academy..."
            riku "I tried to go back once but as I walked up to the academy building, I couldn't stop shivering. I couldn't bring myself to enter."
            riku "I never did go back in the end; I never saw anyone from there ever again."
            show riku closemaidshy with dissolve
            riku "I earned a pretty penny on the contract from there though, so I rented out this house in the suburbs and converted it into a bar."
            riku "Every day I’m grateful that I’m still alive."
            riku "But it’s more than surviving the crash… Even before then, I wasn’t really ‘alive’ while I was training."
            riku "Working every day, to sleep, then work in a perpetual cycle of suffering, that isn’t living. It’s just misery, and I don’t want anyone to go through that."
            show riku closemaidneutral with dissolve
            riku "At the bar, I feel alive. I live my own life, at my own pace, and most importantly, I live that life with my friends."
            show riku closemaidlaughing with dissolve
            riku "And some of those friends have benefits, right?"
            "She flashes me a warm smile and kisses me on the cheek."
            show riku closemaidsatisfied with dissolve
            riku "All this made me realize the life I’d missed, while simultaneously not missing that old life at all."
            show riku closemaidneutral with dissolve
            riku "I think a comfortable life like this far outweighs a constant futile struggle."
            riku "I’m not saying you should never challenge yourself, but I think in this life where we’re all going to die and be forgotten anyway… Might as well try to maximise your personal enjoyment, booze, games, gym, heck yeah."
            mc "I’ll drink to that."
            "We clink our mugs together, toasting and say cheers before drinking the last of our heart-warming tea."
            stop music fadeout 10.0
            show riku closemaidlaughing with dissolve
            riku "Ahhh… That was immensely cathartic to tell you, thanks for listening."
            mc "Thanks for opening your heart to me."
            show riku closemaidneutral with dissolve
            riku "No need to get cheesy with that heart bollocks, the only heart you need is the heart my ass makes when I bend over."
            mc "Woah, woah, if you were that eager you could start dusting again."
            show riku closemaidangry with dissolve
            riku "I thought the dusting was just a means to a sexy act where I show you my ass. You weren’t serious about me dusting the entire room were you?"
            mc "Uhhh, actually, I was kinda hoping it’d be both."
            show riku closemaidshy with dissolve
            "She rolls her eyes in such an exaggerated manner her head rolls too."
            riku "All this time I thought this was a trick to see my ass, and you’re sat there genuinely making me tidy up your house."
            menu:
                "Alright fine, let’s skip the dusting.":
                    riku "Skip the dusting? What now, then?"
                    show riku closemaidhorny with dissolve
                    "She seems trepidatious but there’s an eager glow in her eye."
                    mc "I can make you do anything, so of course I’m going to make you do something naughty. That’s the idea, right?"
                "So, you did want to show off your ass? How naughty!":
                    riku "Pfft, I wouldn’t do it if I wasn’t enjoying myself."
                    mc "Ahh… I know, I was teasing you."
                    riku "I knew that! I was just explaining myself!"
                    mc "It’s fine, I know you’re getting off on this as much as I am."
                    show riku closemaidhorny with dissolve
                    riku "Nuh-uh, I’m a reluctant slave to the end."
                    mc "I can always change that by making you beg."
            riku "That’s pretty hot, what do you mean specifically?"
            mc "Figured I might as well make use of your dress, stand up and turn around."
            hide riku
            show rikub maid
            show riku horny
            with dissolve
            riku "Uu, okay..."
            mc "Now lift up your skirt."
            riku "Alright… This isn’t THAT embarrassing; I mean I usually don’t even wear skirts."
            "She says she isn’t embarrassed, but the subtle blush betrays her."
            hide rikub
            show riku closeasstsun
            with dissolve
            "She hoists up her skirt from end to end and reveals her cute butt."
            "It was hard to tell when she was dusting, but upon closer inspection there’s definitely a wet patch on the fabric."
            mc "Guess we could return the maid outfit, but these stockings? No good."
            riku "Wha? What are you talking about? Perv…"
            "I reach forward and start to rub the wet patch."
            mc "Look, you’re so lustful you’ve made the stockings damp."
            riku "Ahh, I see… It’s your fault for being so hot."
            "I focus my rubbing in the area where her clit would be, causing her to squirm in pleasure."
            riku "Aahh… You’re only making it worse, stupid."
            mc "Okay, I’ll stop then."
            riku "*Huff* N-No, actually… You can do it if you want."
            mc "Oho, you’re giving me permission? I thought you were the slave."
            mc "If you want me to keep doing it, I’d prefer some enthusiasm."
            riku "Mm, fine… Please can you keep touching me?"
            mc "Beg for it."
            riku "Ahh, really?"
            "She uncomfortably squirms in place and turns away briefly as she bites her lip, she’s really enjoying this."
            scene bg moxiewagonday
            show rikub maid
            show riku embarrassed
            with dissolve
            riku "Please master, I want you to keep rubbing my pussy, I’m begging you."
            mc "Hmm… Should I really be the one pleasing you? I know you’re in heat, but I feel like I should be the one getting serviced."
            riku "M-Master, I can suck your dick while you rub me off!"
            "She’s not exactly eloquent, but her blunt delivery is pretty good for getting a boner going."
            show riku horny with dissolve
            riku "Ahh, you’re starting to get hard, mmm…"
            mc "You’re surprisingly a pushover when it comes to sex, you know that? I thought you’d be brattier and more dominant."
            riku "What are you talking about? I am bratty and dominant, I am!"
            "I feel like rolling my eyes, maybe Riku is rubbing off on me. Wait, I’m the one that’s supposed to be rubbing her off. Heh, I make myself laugh sometimes."
            show riku shy with dissolve
            riku "Why are you laughing? If you were my slave, you’d get to see just how dominant I can be."
            mc "Yeahhh, maybe next time. What was that thing about sucking my cock?"
            riku "I’ll do it, but is it really okay to do this in Moxie’s wagon?"
            mc "I was doing you a favour by bringing you to the closest place to the boutique, so you wouldn’t have to walk far in your outfit."
            show riku sad with dissolve
            riku "True, true, I think my reputation would literally fucking die."
            mc "Your bar would probably get more popular if you ask me."
            show riku shy with dissolve
            riku "More popular with who? There aren’t enough men around to draw that crowd."
            mc "Shit, you’re right. No maid cafes then…"
            show riku angry with dissolve
            riku "Ech, you’re such a pervert. Anyway, you missed my point, isn’t Moxie going to be pissed off if we have sex here?"
            riku "I’m quite close to her, don’t want to get on her bad side."
            mc "Don’t you know how relaxed she is about these things? I doubt she’d care at all as long as we cleaned up."
            label rikumaidblowjob:
                pass
            play music sex1 fadein 3.0
            show riku horny with dissolve
            riku "Hmm yeah, you're probably right… Alright, sit tight, my tongue is going to do its thing."
            show rikub maidblowjob
            show riku blowjob1
            with dissolve
            play ambience blowjob fadein 3.0
            "She lays down on the sofa and starts to service my currently erect cock with her tongue, sliding it up and down the shaft."
            "Damn it feels good, her tongue is sensational."
            "I reach over and start to rub her pussy, thankfully she’s quite small so I easily reach."
            "I rub at the area her clit would be and she reacts favourably, I can visibly see her relax"
            riku "Ahhh, you’re pretty good at this. You know exactly where to touch."
            mc "Just being myself, it’s not rocket science, right?"
            riku "Mmphh, rocket science? It is for dumb stallions that have no idea how to please a woman."
            mc "That’s probably because they’ve never had to try, it’s always been on the onus of the mares, right?"
            riku "*Slurp*, *Lick* Ain’t that the truth… Like some dumb whore, I used to practice blowjobs on my dildo, just in case I ever needed to show my worth to a stallion."
            riku "Meanwhile they don’t put in half the effort. Most of them don’t bother touching or licking a mare at all, they probably think clitoris is the name of a mythological creature."
            mc "You practiced blowjobs? You don't have to do that just to validate yourself by pleasing a man."
            riku "You say that, but the stallions don’t have to validate themselves by pleasing me either."
            riku "Truth is, practicing blowjobs was worth it, because it means when I find someone worth it, I can give them a damn good blowjob."
            riku "Hehehe, got it?"
            show riku blowjob2 with dissolve
            "She winks at me and starts to work the top of my cock expertly with her twirling tongue."
            "Slowly she started to take in my glans. She keeps bringing her mouth back and forth like waves hitting a beach, teasing me while sucking the sensitive tip."
            "It doesn’t take too long until her mouth is wrapped around my glans. She starts a fucking motion around my shaft while simultaneously working the head with her tongue."
            show riku blowjob1 with dissolve
            riku "Mmphh, donth forget to rub, idiot."
            "Oops I forgot. I decide to peel down her stockings to give me better access. As they slowly come off, they do so with a string of grool connecting to her pussy."
            "She’s incredibly turned on; I waste no time sinking two fingers deep inside her while using my thumb to nimbly tease her clitoris."
            show riku blowjob3 with dissolve
            riku "Aaaahhhh! Yesh! Mmphhhshh… *Sclurrrp* *Suck*"
            "The pleasure from my handywork actively distracts her from the blowjob, she’s stifling moans into my cock and her tongue is moving around sloppily."
            riku "*Shlurp* Ahh, ahh… *Lick, lick* Mm!"
            "It feels no less amazing though, as her lips squeeze around my shaft and constantly bop up and down the neck of my glans like a sloppy mouth fuck. It's causing my orgasm to well up far faster than I was expecting."
            riku "Aahh- mmm… Mmphh, tell me when cumphh…"
            mc "I’m close, you’re too damn good at this!"
            show riku blowjob2 with dissolve
            "My cock began to throb as I approached the point of no return, however Riku surprised me by taking my cock deeper into her mouth."
            show riku blowjob1 with dissolve
            "She allowed my cock to slide all the way in as she effectively deep throated me without gagging, all whilst maintaining sexy bedroom eyes."
            "Her lips wrap around the base of my cock. I could feel her tongue flailing up and down against my shaft, that combined with the lecherous, sloppy, wet noises; it’s all too much. I can’t hold back any longer."
            play sound cum
            show riku blowjob5 with cum
            play sound cum
            show riku blowjob5 with cum
            "I began to forcefully ejaculate, several loads shooting against the back of her throat."
            play sound cum
            show riku blowjob5 with cum
            play sound cum
            show riku blowjob5 with cum
            "Riku’s eyes initially opened wide when she felt hot cum oozing down her throat, then her eyes rolled back, and her pussy tightens around my fingers as she climaxs too."
            riku "Mmmphhh! Mmmmphhhh!!! *Gulp*"
            show riku blowjob6 with dissolve
            "I’m barely pleasuring her right now, yet she was so turned on from her experiences today that she had an easy orgasm."
            stop ambience fadeout 3.0
            "Somehow she manages to swallow every single drop of cum before slipping my cock out of her mouth, a trail of spit coupling my glans and her mouth as she’s left panting for air."
            stop music fadeout 3.0
            scene bg moxiewagonday
            show riku closemaidhorny
            with dissolve
            riku "Haah, haah, aaahh… *Pant, pant*"
            play ambience ambienceday fadein 30.0
            "That got really messy, all the fur around her mouth is sodden and dripping with saliva."
            "Yet, not a single drop of cum to be found."
            if crystalballactivated == 1:
                $ crystalballactivated = 0
                jump cbmenu
            riku "Haaaahhh… Can-*pant*-barely-breathe… Hahh…"
            mc "Overdid it?"
            show riku closemaidlaughing with dissolve
            riku "Eheh, maybe a bit, but you deserved it."
            mc "Pushing your limits as usual!"
            show riku closemaidhorny with dissolve
            riku "How long until you’re ready to go again?"
            mc "Give it at least twenty minutes."
            riku "Can’t you push your limits and fuck me now, hmm? I’ll let you use my butt!"
            mc "I could, but I’d be too sensitive for it to feel good."
            show riku closemaidshy with dissolve
            riku "Awh, fine, I’ll wait… ‘Master’…"
            mc "Calling me master again? You really like being told what to do, don’t you?"
            show riku closemaidangry with dissolve
            riku "Eh, kinda? But I’m a total brat! So, I won’t like it."
            mc "You say that, but you’ve been nothing but willing."
            show riku closemaidneutral with dissolve
            riku "But you haven’t told me to do anything egregious yet."
            mc "She says wearing a maid dress, lifting up her skirt to show off her wet pussy, then deep throating me."
            show riku closemaidshy with dissolve
            riku "Mm… You’re a mean master."
            mc "Tell me, when you decided on the loser’s punishment in that truth or dare game, did you always plan to lose?"
            show riku closemaidembarrassed with dissolve
            riku "Ahhh, no way! I like to order people around too."
            mc "Be honest, you have to follow my orders and that includes telling the truth."
            riku "Yeah, I did want to lose! I did want to be ordered around, but if I won that would have been awesome too. It’s win/win, that’s why I suggested it."
            mc "Yeah that makes sense. What would you have done if you won?"
            show riku closemaidhappy with dissolve
            riku "I dunno, I have a few stray ideas."
            show riku closemaidhorny with dissolve
            riku "I think it would be dope if I had someone to eat me out while I’m in my office working, or while I’m gaming."
            show riku closemaidhappy with dissolve
            riku "Definitely would have made you cook me a nice dinner."
            "Now that’s an idea!"
            riku "Probably woulda made you fuck me again at some point, but that’s a given for friends with benefits, right?"
            mc "We’re friends with benefits?"
            show riku closemaidembarrassed with dissolve
            riku "Oh? Are we not?"
            mc "Guess we could be."
            show riku closemaidhappy with dissolve
            riku "If you’d like to be. You give a good dicking, so I’d be down whenever you want."
            mc "You were a good fuck yourself, Riku…"
            "Riku takes a second to look around Moxie’s wagon."
            show riku closemaidshy with dissolve
            riku "You’re uh… Sleeping with Moxie too, right? Would she be mad?"
            "Honesty is the best policy here, lies will only cause headaches later on."
            mc "Yeah, me and Moxie sleep together."
            mc "She wouldn’t be mad, she actually encouraged me to play around."
            riku "’Play around’? Are you sleeping with others as well?"
            menu:
                "Do you want to know that, or are you just asking because you can’t help yourself.":
                    riku "A bit of both, if you don’t want to tell me, that’s okay."
                "You don’t even know the half of it.":
                    riku "Ahh, half? More than two?"
                    show riku closemaidembarrassed with dissolve
                    riku "Wait no if it’s more than half that means… Four… More than five? Or five and above?"
                    mc "You’re overthinking it."
                    show riku closemaidshy with dissolve
                    riku "Oh, sorry."
                "No, you and Moxie are the only ones.":
                    riku "Oh really?"
                    show riku closemaidhappy with dissolve
                    riku "That makes me feel pretty good, but also kinda weird since me and Moxie are close."
            riku "Is sharing a fuck buddy weird? I don’t know."
            mc "It really depends on the context, if we were to have a threesome that'd certainly normalise it."
            show riku closemaidlaughing with dissolve
            riku "A threesome? I’ve never done one of those before. Ohh gosh, I don't think I could either."
            show riku closemaidneutral with dissolve
            riku "I’m still new to this weird sex culture, I’ve mostly been closeted because of my background."
            show riku closemaidshy with dissolve
            riku "I know I was pissed at my ex-fuck buddy, but I guess I don’t mind it with you, as long as we establish the relationship early."
            mc "Agreed, communication is always vital."
            show riku closemaidneutral with dissolve
            riku "Yeah, I would prefer to have you to myself. But that preference isn’t so overwhelmingly strong that I’d turn down a fun time, you know?"
            mc "I think so, I wouldn’t mind if you slept with others too."
            show riku closemaidlaughing with dissolve
            riku "Ehh, hehe. One step at a time for me I think, I’m too prude to start sleeping around myself."
            scene bg moxiewagonday with dissolve
            show moxie2 closeshocked with dissolve:
                xpos 700
                ypos 0
            play music challenge
            "Catching us both off guard, the door to the wagon creaks open and I can hear Moxie casually humming as she enters with a few boxes of her performance gear. She almost drops them, wide-eyed as she spots us."
            moxie "Oft, you made me jump! Heck!"
            show riku closemaidembarrassed with dissolve:
                xpos 50
                ypos 85
            show moxie2 closehappy with dissolve
            moxie "I really, really, really wasn’t expecting you two to be here. Are you two making lunch?"
            riku "Uh-uhm, no..."
            "I hadn’t even realized, but it’s lunchtime already. I should have expected this to happen."
            show moxie2 closeembarrassed with dissolve
            moxie "Great to see you two, but uhh… Do I even need to ask?"
            show riku closemaidshy with dissolve
            riku "The maid outfit?"
            mc "It’s a long story."
            "Riku shudders in disgust and around the same time Moxie spots the black stockings on the couch."
            show moxie2 closeshy with dissolve
            moxie "Golly, you two have been fuckin’!"
            moxie "In my wagon no less, where was my invitation?"
            show riku closemaidsad with dissolve
            riku "N-No! Invit- no! You know that’s not like me."
            show moxie2 closeneutral with dissolve
            moxie "Oh please, how naïve do you think I am?"
            show moxie2 closelaughing with dissolve
            moxie "It’s just a shame I didn’t get to embarrass you more by walking in on the act, muhaha."
            mc "Actually, we haven’t fucked."
            show moxie2 closesmug with dissolve
            moxie "Is that so?"
            "Moxie smirks and winks at me, I wink back, here we go."
            "Riku seems distressed, she saw both winks."
            mc "You can even check if you want."
            show riku closemaidembarrassed with dissolve
            riku "C-Check? There will be no vagina inspections!"
            moxie "Awh come on Riku, if you don’t let me look, I’ll just have to assume you two were just balls deep."
            riku "N-No way! R-Right?"
            "Riku looks to me, as if seeking orders, she is getting turned on like crazy right now."
            "I utterly love the fact Moxie is playing along, me and her are on the same teasing wavelength for sure. Riku is in for double the trouble."
            mc "Yep, you definitely need to lift up your skirt to prove your innocence."
            riku "Eughh, by Aurora… I’m only doing this because I’d usually be naked anyway…"
            scene bg moxiewagonday with dissolve
            show riku altass2 with dissolve
            "She bites her lip as she slowly raises her skirt, her thighs trembling as her vulva slowly comes into sight."
            "With a smirk, Moxie wastes no time squatting down to take a closer look, going so far as to poke and prod with her finger."
            riku "Eek! Don’t touch it!"
            moxie "Part your legs a little, maid."
            riku "Eugh, fine…"
            "Riku genuinely listens, Moxie may be more commandeering than even I am."
            "Riku’s legs part gently and Moxie spreads apart the pussy lips causing Riku to gasp, she’s trembling even more than before."
            moxie "Yup, no cum in here. What a shame, it might have been fun to lick it out."
            moxie "You two were about to fuck right, maybe I can still lick it out?"
            riku "That’s way too lewd!"
            moxie "Wow though, I can’t believe how wet you are."
            moxie "[playername] does have that effect on mares."
            "Moxie holds Riku close and takes one long lick across the length of her vulva, Riku puts up no resistance, she can’t do anything but throw her head up and moan."
            riku "Aahhh? M-Moxie!?"
            moxie "Mmmm… Tasty…"
            scene bg moxiewagonday with dissolve
            show moxie2 closesmug with dissolve:
                xpos 700
                ypos 0
            show riku closemaidembarrassed with dissolve:
                xpos 50
                ypos 85
            "Moxie stands back up and wipes her wetted muzzle clean before looking towards me and grinning."
            moxie "She’s cute, isn’t she? I think I prefer her in-between my legs though."
            riku "Hmph…"
            mc "I’m surprised by how forward you’re being."
            moxie "Wouldn’t be my first time licking there, hehe."
            riku "Shut up, that was a one-time thing!"
            show moxie2 closelaughing with dissolve
            moxie "Fairly sure I just made it a three-time thing, struggling to keep count?"
            show moxie2 closealthappy with dissolve:
            moxie "I love how feisty she tries to be, yet how compellingly submissive she is under the slightest bit of pressure."
            mc "I had no idea you two have had sex before."
            show riku closemaidembarrassed with dissolve:
                xpos 300
                ypos 85
            riku "It was not sex! Just drunk playing!"
            moxie "It was drunk playing and sex."
            show moxie2 closehappy with dissolve
            moxie "One night, Riku and I were just chilling together, we started playing truth or dare while drinking, and it escalated to lewd proportions."
            moxie "Then we did it again a few days afterwards hehe, then you started to see that gym-buddy and it broke off."
            "Wow, I wonder how many fascinating things I don’t know about these girls? Are they all fucking behind my back?"
            mc "Wait a minute, the exact same thing happened to me."
            show moxie2 closeshocked with dissolve
            moxie "What’s that?"
            show riku closemaidembarrassed with dissolve:
                xpos 200
                ypos 100
            riku "Uh oh."
            mc "Yeah, Riku made me play truth or dare the first time we met, and it escalated."
            show moxie2 closesmug with dissolve
            moxie "Oh really? Our small, red friend is smarter than she lets on."
            show riku closemaidshy with dissolve
            riku "N-No, I just think it’s fun!"
            moxie "Tsk tsk, she’s been playing us this whole time for sexual gratification."
            show moxie2 closelaughing with dissolve
            moxie "Looks like she was just about to succeed again, if I hadn’t come in and saved you last second."
            show riku closemaidsad with dissolve
            riku "Ugh… I’m sorry you two, I shouldn’t act so slutty…"
            riku "I guess I should leave? I feel like a bit of a homewrecker right now."
            show moxie2 closesmug with dissolve
            moxie "Sounds like we need to punish her, what do you think, [playername]?"
            show riku closemaidembarrassed with dissolve
            riku "P-Punish?!"
            mc "You’re right, what should we do?"
            show moxie2 closehorny with dissolve
            moxie "I think she needs a good pounding, how about a spit roast?"
            show riku closemaidshy with dissolve
            riku "Oh gosh, one of you was bad enough, but both of you?"
            mc "It’s decided, come on slave girl, go to the bedroom."
            show riku closemaidembarrassed with dissolve
            riku "Don’t I get a say in this? W-Wait, I’ve been downgraded from a maid to a slave?"
            moxie "Come on you filthy slut, get on the bed."
            show riku closemaidembarrassed with dissolve:
                xpos 50
                ypos 85
            riku "N-Now a slut? That’s so mean!"
            show moxie2 closehorny with dissolve:
                xpos 450
                ypos 0
            play sound spank
            hide riku with hpunch
            "Moxie spanks Riku’s ass causing her to yelp and scurry along, she knows exactly which door leads to the bedroom."
            hide moxie2 with dissolve
            "Moxie undresses and takes a second to whisper something to me before we follow her in."
            show moxie closealthappy with dissolve
            moxie "Psst, she really likes it when you degrade and humiliate her, she’s a complete sub. You should definitely try and push her."
            moxie "Although, considering the maid dress, you’re already doing an excellent job."
            mc "What are we gonna do?"
            show moxie closesmug with dissolve
            moxie "One of us at each end, she can lick me out and you can fuck her."
            mc "Perfect."
            riku "Heyy! Don’t get freaky without me, come on you two!"
            stop music fadeout 3.0
            stop ambience fadeout 3.0
            scene bg black with dissolve
            "…"
            label rikuthreesome:
                pass
            play music sex1 fadein 3.0
            scene bg moxiebedday with dissolve
            show riku altass2 with dissolve
            moxie "You have such a cute butt Riku, you know that?"
            riku "Mmphh, perverts…"
            moxie "Your tail is gorgeous too."
            "She says as she firmly holds the tail out of the way, revealing Riku’s genitals to me."
            riku "Ahhh…"
            "With her other hand, Moxie starts to jack me off and it doesn’t take long for my cock to become fully erect."
            riku "I can’t believe this is happening, one of you was bad enough, but this is too embarrassing!"
            mc "You’re enjoying each and every second of this, admit it."
            riku "No way, I’m not a slut like that…"
            moxie "Hehehe, maybe she isn’t a slut, but her pussy is! Tease her."
            "I start to lift my cock up and down against Riku’s genitals, causing her to quiver with anticipation."
            riku "I love your cock, master!"
            moxie "Now how about I make some better use out of that tongue?"
            hide riku
            show rikub maidthreesome
            show riku threesome1
            with dissolve
            "Moxie crawls up the bed and lays in front of our subservient maid, spreading her legs and subsequently her pussy for Riku."
            moxie "Don’t make me ask, slut."
            "Riku nods and readily gets in between Moxie’s legs, her tongue starting to lap at Moxie’s clit."
            "Moxie brings a fist to one of Riku's braids and grips onto it tightly, holding her down dominantly."
            riku "Mmphhh, mmmm!"
            moxie "Ahh, what a good slut, wasting no time with her tongue at all."
            moxie "Mmmphh, ahhh, and she's great with her tongue as always."
            riku "Mmpphh, I’m only horny because I’m in heat, it’s not fair…"
            moxie "Only because you’re in heat? You weren’t in heat when you let me sit on your face."
            riku "N-Nuu, I was drunk!"
            mc "More excuses? I won’t fuck you until you admit how much of a slut you are."
            riku "Ohhhh… B-But…"
            "I press my cock against her pussy, teasing her by applying pressure against the entrance."
            moxie "Come on slut, you’re so horny you’re dripping all over my bedsheets, just admit how badly you want it."
            riku "Mmmphh, I really want it, but…"
            mc "But what, slave?"
            riku "I-I really want it in the ass, I even prepared for it…"
            mc "Oh? Here?"
            show riku threesome2 with dissolve
            "I abide by her humble request, pressing my cock against her cute butthole."
            riku "Mmphhh fuck yeah, I need it badly, please!"
            moxie "What a surprise, I didn’t take you for an anal queen."
            riku "B-because I’m responsible and don’t want to get pregnant."
            moxie "Ohhh, that’s how you have all the sex you could possibly want. Our little slut has creative solutions."
            riku "Please, I really want it…"
            mc "Mmm, what a cute lil butt, I bet it has seen a lot of action."
            show riku threesome3 with dissolve
            moxie "Lots of pounding from thick cocks like [playername]’s."
            riku "Mmm yes, I’m a butt slut!"
            show riku threesome2 with dissolve
            moxie "Go on, slide your cock deep in her ass, [playername]."
            riku "Yes, yes! Please!"
            "I push the tip of my cock against her pucker, applying pressure, although it’s a tight fit."
            riku "Ghh, ahhh…"
            "I drool a little on the point of contact to add just a tiny bit of lubrication."
            "The wetness helps a lot. As I continue apply pressure to Riku’s pucker it slowly loosens, and I edge myself inside."
            play sound cum
            show riku threesome3 with dissolve
            "The saliva is surprisingly slippery. Before I know it, the tip of my cock is inside, and the rest slides in with ease."
            riku "Mmmm! Fuck yeah! *Lick, schlurp*"
            play ambience sex2 fadein 3.0
            show riku threesome3 with dissolve
            "Riku’s ass is incredibly tight as it squeezes around my shaft, I fuck her gently as she continues to loosen and adjust to my throbbing cock."
            show riku threesome3 with dissolve
            "Her ass has finally started to loosen up now and I’m able to fuck her at a good pace."
            show riku threesome3 with dissolve
            riku "Mmphhh *Lick, lick*! Ahhh *schlurp*."
            show riku threesome3 with dissolve
            "It’s definitely tighter than her pussy, and a lot of the tightness is concentrated at the sphincter which feels particularly amazing as it glides over my glans."
            show riku threesome3 with dissolve
            "There’s more friction too. It feels different overall, but I could probably cum just as easily from this."
            show riku threesome3 with dissolve
            "Meanwhile Moxie’s head is thrown back against the pillow, she’s in utter joy as Riku’s tongue makes miracles on her clit. I’m almost jealous at how much pleasure Moxie is getting out of that."
            show riku threesome3 with dissolve
            if libraryvisit1 == 1:
                "It’s reminding me of how good Penelope was when she was licking me out."
                show riku threesome3 with dissolve
            moxie "Aahhh, ahh! Ahhh! Right there, yes!"
            show riku threesome3 with dissolve
            "She moans while assertively pressing Riku’s muzzle into her clit."
            show riku threesome3 with dissolve
            "Even while being spit roast, Riku is going above and beyond, her hips are rocking back and forth causing her ass to slide up and down my cock, matching my rhythm making for harder thrusts."
            show riku threesome3 with dissolve
            "At this rate, all three of us are going to cum soon."
            show riku threesome3 with dissolve
            "I’m glad it doesn’t take long for a mare in heat to climax, because Riku is rocking her hips far too fast for me to hold back."
            show riku threesome3 with dissolve
            "Eventually her thrusts overpower mine, leaving me staying still behind her as she bounces up and down against my cock. All whilst her tongue drives Moxie ecstatic."
            show riku threesome3 with dissolve
            moxie "Ahhh, I’m gonna come!"
            show riku threesome3 with dissolve
            riku "Mmphhh *Lick, sclurp*."
            show riku threesome3 with dissolve
            "I can’t hold back either, my cock is growing tense and throbbing."
            play sound cum
            show riku threesome4 with cum
            play sound cum
            show riku threesome4 with cum
            "The pressure in my loins reaches its peak as I begin to have a powerful orgasm, ejaculating several loads into Riku’s ass."
            play sound cum
            show riku threesome4 with cum
            play sound cum
            show riku threesome4 with cum
            stop ambience fadeout 3.0
            stop music fadeout 3.0
            "All whilst Moxie wriggles with pleasure, her back arched as she too begins to orgasm."
            show riku threesome4 with dissolve
            show riku threesome5 with dissolve
            "After an intense feeling of euphoria, my climax fades and I pull out, splattering her ass with a few last blasts of jism as I do."
            scene bg moxiebedday with dissolve
            show riku closemaidsatisfied with dissolve:
                xpos 100
                ypos 75
            show moxie closehorny with dissolve:
                xpos 600
                ypos 25
            "Riku lifts up from Moxie’s legs and rolls to the other side of the bed. She looks just as satisfied as Moxie and I, her tongue lulling out dramatically as she pants."
            moxie "Good, isn’t she? I had to jump at the opportunity when I realized you two were about to have sex, hahaha."
            if crystalballactivated == 1:
                $ crystalballactivated = 0
                jump cbmenu
            mc "Yeah she’s a trooper for sure."
            show riku closemaidhappy with dissolve
            riku "That was fun, you two have definitely been my favourite sex partners."
            show moxie closelaughing with dissolve
            moxie "The competition wasn't exactly tough! We’ll do this again, don’t you worry."
            show riku closemaidlaughing with dissolve
            riku "Mmm, yes please, I’ll be your slut any day."
            mc "She isn’t even resisting anymore, she’s completely subservient."
            show moxie closehappy with dissolve
            moxie "Haha, she’s always like this after sex, give her a few hours and she’ll be a brat again."
            show riku closemaidshy with dissolve
            riku "Nuh-uh, I’m a good girl, I’ll do whatever you say."
            mc "Alright, you’re starting to weird me out Riku. I’m going to go grab a shower, anyone of you two ladies want to join me?"
            show moxie closealthappy with dissolve
            moxie "I’ll need to make some lunch and go back to work; slave, you go join him."
            moxie "Wash his back really well."
            show riku closemaidlaughing with dissolve
            riku "Oh thank god, an excuse to get out of this stupid maid outfit."
            mc "There’s the brat we know and love."
            scene bg black with dissolve
            "…"
            show bg wagonshower with dissolve
            play music day2 fadein 3.0
            "The two of us head into the shower and she gives me a good scrubbing. I can’t help myself and I fuck her again while pressing her against the wall."
            "Pounding her ass again and filling it with another load of cum as she loses her mind to pleasure and arousal."
            "She’s even more sheepish than usual as we get out the shower."
            show bg moxiewagonday with dissolve
            "The three of us share the lunch that Moxie cooked before she returns to work, leaving both me and Riku alone for the rest of the day."
            show rikub
            show riku neutral
            with dissolve
            riku "Feels weird taking a day off work, but a day of fucking will probably increase my work-efficiency over the coming days to make up for it."
            mc "How was your first threesome?"
            show riku laughing with dissolve
            riku "Still feels surreal to me, give it a week and I still won’t realize I was in a threesome."
            show riku shy with dissolve
            riku "Trust my slutty ass in heat to get into these kinds of situations."
            mc "You’ve completely surrendered to your sexual nature today."
            show riku horny with dissolve
            riku "Yeah, that twisted part of me wants nothing more than to be used like a slut and a slave."
            riku "I like watching hardcore porn, and I want to try that kinda stuff, but my last partner was boring."
            show riku laughing with dissolve
            riku "So thanks for letting me live out that fantasy, even if it’s a little bit."
            mc "Got any other sick fantasies you want to live out?"
            show riku happy with dissolve
            riku "Pfft, no! Even if I did, I wouldn’t tell you, perv."
            menu:
                "Actually, you have to tell me, I order you to.":
                    show riku embarrassed with dissolve
                    riku "By Aurora, I almost forgot about that slave stuff."
                    riku "Fiiinnee… I’ll tell you what you want to know."
                    show riku shy with dissolve
                    riku "I have this fetish doing it with other species. I usually watch interspecies porn with a mare."
                    mc "Interspecies like me?"
                    riku "Kinda, but not quite."
                    riku "The fact you’re another species does interest me a lot."
                    riku "But I much prefer wolves and dragons, I wanna get dominated, knotted, bred."
                    show riku embarrassed with dissolve
                    "She managed to say that completely straight faced, before clumsily realizing how embarrassing that was to openly say."
                    mc "Sounds like an extension of your desire to be dominated."
                    mc "Which is strange considering you try to make yourself out to be such a strong and independent mare."
                    show riku shy with dissolve
                    riku "Is that strange? I’m a strong woman in my personal life, and I want someone to break that in my sexual life by dominating and overpowering me."
                    riku "Reducing me to bare primal instincts, sex and stuff, right?"
                    mc "You’re making a lot of sense, sounds hot."
                    "I guess that means heat itself is one of her kinks."
                    show riku horny with dissolve
                    riku "That’s why today has been so sexually satisfying for me."
                    riku "Although…"
                "I already have a pretty good idea of what you like.":
                    show riku shy with dissolve
                    riku "I’m not a perv. I just like it rough. That’s normal, right?"
                    mc "Yeah that’s rather normal, although you’re on more of the extreme end."
            show riku embarrassed with dissolve
            riku "Was Moxie serious when she said we’re gonna have more threesomes?"
            mc "Only as serious as you are willing, the two of us often have sex in the evenings anyway."
            mc "If you ever want to join us in the evening, you’re more than welcome."
            "She’d be the star of the show with her sexual prowess, that’s for sure."
            show riku happy with dissolve
            riku "You two can come visit me at the bar if you want some fun, just lemme know. Drinks on me!"
            mc "Thanks, I’ll put you up to that."
            show riku horny with dissolve
            riku "We got another four hours until I should head back, do you want me on top this time?"
            "She’s trying to fuck me again, but I’ve already cum three times in the past two hours. This girl is on a lust high right now."
            mc "How about we go to the gym and have a work-out to release all that pent-up frustration?"
            show riku laughing with dissolve
            riku "Hmm, working out with men usually makes me hornier, but okay!"
            "That should at least buy my dick some time."
            stop music fadeout 3.0
            stop ambience fadeout 3.0
            scene bg black with dissolve
            "…"
            play ambience ambiencenight fadein 3.0
            show bg worldmapnight with dissolve
            if crystalballdayactivated == 1:
                $ crystalballdayactivated = 0
                jump cbmenu
            "The day passes, Riku and I work out at the gym before going back to her place. We have a few drinks, play a few of her games then fuck again before I head home."
            "As you can expect, I don't get paid today. I didn't do any work!"
            if livingwithmoxie == 1:
                show bg moxiewagonlamp with dissolve
                play music wagon fadein 2.0
                "When I get back to the wagon Moxie seems rather relaxed, she’s resting on the sofa after a long day of work."
                show moxie happy with dissolve
                moxie "Sex for lunch really helps kick down that heat, I came back to those afternoon performances feeling positively perky."
                mc "I did not expect today to happen quite like it did."
                "I sit down on the sofa next to Moxie. Many muscles are sore due to the sex and working out I’ve had to do, but it’s not too bad."
                show moxie closebashful with dissolve
                moxie "I can’t say I expected to have my first threesome today either, but I’m glad I did."
                show moxie closelaughing with dissolve
                moxie "Being able to take part of your sexual escapades was a lot of fun."
                show moxie closealthappy with dissolve
                moxie "I’d support bringing more mares that you fuck here, but I think it’d probably be best if we stuck to tag-teaming Riku. That girl has a rocking tongue game."
                mc "She knows how to work her hips too, not to mention that how tight and wet she gets."
                show moxie closesmug with dissolve
                moxie "Is that so? How does it compare to my hips, tightness and wetness?"
                "Oops, I let my mouth speak too freely."
                "At least this experience has allowed Moxie to feel less jealous about me sleeping around."
            elif livingwithbutters == 1:
                show bg buttershousenight with dissolve
                play music butters fadein 2.0
                "When I get back to the cottage Butters seems rather relaxed, she’s resting on the sofa, no doubt after a long day of collecting and brewing ingredients."
                "It would have been nice to go back and talk to Moxie about what happened, but I wouldn't want to miss Butters's excellent cooking."
                show butters dresshappy with dissolve
                butters "Oh hey! Welcome home master."
                "I sit down on the sofa next to Butters. Many muscles are sore due to the sex and working out I’ve had to do, but it’s not too bad."
                mc "I did not expect today to happen quite like it did."
                mc "Hey Butters, would you ever be interested in a threesome?"
                show butters closedressneutral with dissolve
                butters "Uhm, maybe… I’ve never had sex with both holes at once before…"
                show butters closedressangry with dissolve
                butters "Oh wait… The Alraune did that… Drats."
                mc "Oh, uh… I kinda meant two girls. Finding another guy might be hard."
                show butters closedresshappy with dissolve
                butters "I see! You want to invite me to have some fun with another one of your girl friends?"
                mc "Think you could repress your succubus long enough for something like that?"
                show butters closedresslaughing with dissolve
                butters "Mhm, the succubus will repress herself, she daren’t get caught."
                mc "Let’s go to the bar sometime and bring a friend home."
                show butters closedresshappy with dissolve
                butters "Oohh, okie, I like the sound of that."
            stop music fadeout 3.0
            scene bg black with dissolve
            "…"
            jump evening
label barvisitday:
    scene bg black with dissolve
    show bg bar with dissolve
    show rikub
    show riku happy
    with dissolve
    $ rand = renpy.random.randint(1,2)
    if rand == 1 and rikuclimbingsex == 0 and boutiquevisit3 == 1 and farmvisit3 == 1:
        $ rikuclimbingsex = 1
        "You found a secret scene! Requirements met: Visit Riku after beating the bar, boutique and farm routes."
        riku "Hey! You’re here to work, right?"
        mc "Gym, work, and fun, in that order?"
        show riku neutral with d
        riku "Typically, but no gym today. I’m going climbing!"
        mc "Climbing? But you’ve got wings!"
        show riku laughing with d
        riku "Hah, why should that stop me from having some fun? Climbing walls are tons of fun!"
        riku "You should totally come with me; I’ll pay for you if you work at the bar later. How about it? Just think of it as an unusual workout."
        mc "That sounds like a lot of fun. It’ll be a first for me though, think you can show me the ropes?"
        show riku happy with d
        riku "No problem! I love teaching other people."
        jump rikuclimbingsex
    else:
        pass
    riku "Hey! Up for some work and fun, in that order?"
    menu:
        "In order to talk/have sex with Riku I'll need to work with her first."
        "Sure thing.":
            play music day2 fadein 3.0
            riku "Let's do it!"
        "Nah, I have things to do.":
            if fr == 1:
                jump finalworldmap
            jump preworldmap
    scene bg black with dissolve
    $ monies += 25
    "I spend the day with Riku, and earn a pay of 25 monies working at the bar."
    stop ambience fadeout 3.0
    label prerikumenu2:
        pass
    show bg barupstairs with dissolve
    show riku closehappy
    with dissolve
    riku "I have an hour or so before my evening shift, let's spend some time together!"
    mc "Special time reserved just for me? I'm flattered."
    label prerikumenu:
        pass
    play ambience ambiencenight fadein 3.0
    menu rikumenu:
        "Talk" if prismatalks == 0:
            jump rikutalk
        "Sex" if prismasex == 0:
            jump rikusex
        "Leave":
            show riku closehappy with dissolve
            riku "See you later!"
            jump evening
    label rikutalk:
        menu:
            "What's with the bandage on your arm?":
                show riku closelaughing with dissolve
                riku "Ah! It sure took you a while to ask. That's usually one of the first questions people ask me."
                show riku closeneutral with dissolve
                riku "You already know the long of it, but this is my last remaining scar from the big injury I told you about."
                riku "Under the bandage there's no fur, just pink skin. It's weird! So I cover it up."
                show riku closehappy with dissolve
                riku "Heh, but I guess you're entirely pink skin and you pull it off with finesse."
                mc "How did the injury affect your arm of all things?"
                show riku closeshy with dissolve
                riku "Well, it's not a pleasant detail, but some tree branches can be quite... 'sharp', I guess?"
                mc "Ohh, yikes..."
                show riku closeneutral with dissolve
                riku "Doctors said the fur will grow back eventually, for now I like to use the bandages as a reminder to live my life to the fullest."
                mc "Awwhh, that's so sweet..."
                riku "Nothing like turning a symbol of weakness into one of power."
            "Ask her about her unusual hair colour":
                show riku closeshy with dissolve
                riku "Would you believe that my parents wanted to name me Prisma? After the crystal that splits light into a rainbow."
                show riku closehappy with dissolve
                riku "My parents sure had a sense of humour. The hair itself is passed on from my mother, it's natural believe it or not."
                show riku closelaughing with dissolve
                riku "Apparently 'Riku' was the name they were going to give me if my hair wasn't rainbow, but I guess they chickened out in the end!"
                show riku closehappy with dissolve
                mc "I noticed naming conventions around here can be a little odd. Like uh, Honeycrisp, she's named after a type of apple, and primarily farms apples."
                riku "Yeah, back in the 'ye olde days' it was typical to have a name that matched your family's business or career."
                riku "Such as baker for baking, smith for blacksmiths, and more. This naming convention has gradually shifted into a more 'creative' form where people are looking for cute and unique names that are loosely inspired by the family's business."
                mc "What, did your family make rainbows or something?"
                show riku closeneutral with dissolve
                riku "Oh no, it was literally because my hair is rainbow. It's Honeycrisp and Blossom that have names related to apples."
                mc "What's Blossom's relation?"
                show riku closehappy with dissolve
                riku "Apple Blossom is the name of an apple tree I believe, not to mention the connotation with farms and blossoming."
                mc "Well, I didn't expect to learn something about Blossom today."
            "Do you experience any trouble at your bar?":
                show riku closehappy with dissolve
                riku "Trouble? Like a bar fight? Never, Arcadia is such a peaceful location."
                riku "Needless to say, the crime rates are negligible. This society is so finely tuned and well run by the Royal Sisters, that people simply don't turn to crime."
                riku "Those sisters, I forget how old they are, but can you imagine how much experience they have running this country?"
                mc "Yeah, and they don't seem to be corrupt and taking advantage of that power. That was quite common where I'm from."
                riku "It would be easy for them to take advantage of us in their position, but there's no censorship, no ridiculous laws, and tons of freedom. Even the taxes for my bar are low!"
                mc "Although you did mention there was a doping scandal with the Lightning Bolts."
                show riku closeshy with dissolve
                riku "Yeah... While petty crime can be eliminated with great civilian conditions, you'll always get some bureaucrats trying to abuse their power for a competitive advantage."
                riku "And it's not like the Royal Sisters are omniscient, so I don't expect them to stamp out every single scrap of corruption within society."
                show riku closehappy with dissolve
                riku "Still, that's one of the few rare problems in an otherwise peachy city."
                mc "I'll agree there, this place is awesome."
            "Back":
                jump rikumenu
        $ prismatalks = 1
        jump rikumenu
    label rikusex:
        menu:
            "Plan a threesome with Moxie tonight":
                $ prismamoxiethreesome = 1
                $ prismasex = 1
                riku "Oohh, okay! I'm feeling nervous already, but I'll be there."
                jump rikumenu
                label rikumoxiethreesome:
                    "Riku arrives a little later and after some jovial talk, the three of us end up in the bedroom."
                    play music sex1 fadein 3.0
                    scene bg moxiebednight
                    show rikub threesome
                    show riku threesome1
                    with dissolve
                    "Moxie crawls up the bed and lays in front of Riku, spreading her legs and subsequently her pussy for Riku."
                    moxie "Don’t make me ask, slut."
                    "Riku nods and readily gets in between Moxie’s legs, her tongue starting to lap at Moxie’s clit."
                    "Moxie brings one of her hands to one of Riku's braids and grips onto it tightly, holding her down dominantly."
                    riku "Mmphhh, mmmm!"
                    moxie "Ahh, what a good slut, wasting no time with her tongue at all."
                    moxie "Mmmphh, ahhh, and she's great with her tongue as always."
                    riku "Mmpphh, you two are such bad influences, hehe…"
                    moxie "Bad influences? You're the one that got us drunk and seduced us with truth or dare!"
                    riku "N-Nuu, I was drunk!"
                    mc "More excuses? I won’t fuck you until you admit how much of a slut you are."
                    riku "Ohhhh… B-But…"
                    "I press my cock against her pussy, teasing her by applying pressure against the entrance."
                    "She's soaking wet, no doubt she's been anticipating this since we planned the threesome."
                    moxie "Come on slut, you’re so horny you’re dripping all over my bedsheets, just admit how badly you want it."
                    riku "Mmmphh, I really want it, but…"
                    mc "You want it in the ass again, buttslut?"
                    riku "Y-Yeah!"
                    show riku threesome2 with dissolve
                    "I abide by her request, pressing my cock against her cute butthole."
                    riku "Mmphhh fuck yeah, I need it badly, please!"
                    moxie "If I can hear you talk you're not pleasuring me enough!"
                    "I push the tip of my cock against Riku's pucker, applying pressure, although it’s a tight fit."
                    riku "Ghh, ahhh…"
                    "I drool a little on the point of contact to add just a tiny bit of lubrication."
                    "The wetness helps a lot. As I continue apply pressure to Riku’s pucker it slowly loosens, and I edge myself inside."
                    play sound cum
                    show riku threesome3 with dissolve
                    "The saliva is surprisingly slippery. Before I know it, the tip of my cock is inside, and the rest slides in with ease."
                    riku "Mmmm! Fuck yeah! *Lick, schlurp*"
                    play ambience sex2 fadein 3.0
                    "Riku’s ass is incredibly tight as it squeezes around my shaft, I fuck her gently as she continues to loosen and adjust to my throbbing cock."

                    "Her ass has finally started to loosen up now and I’m able to fuck her at a good pace."
                    riku "Mmphhh *Lick, lick*! Ahhh *schlurp*."
                    "It’s definitely tighter than her pussy, and a lot of the tightness is concentrated at the sphincter which feels particularly amazing as it glides over my glans."

                    "There’s more friction too. It feels different overall, but I could probably cum just as easily from this."

                    "Meanwhile Moxie’s head is thrown back against the pillow, she’s in utter joy as Riku’s tongue makes miracles on her clit. I’m almost jealous at how much pleasure Moxie is getting out of that."

                    moxie "Aahhh, ahh! Ahhh! Right there, yes!"

                    "She moans while assertively pressing Riku’s muzzle into her clit."

                    "Even while being spit roast, Riku is going above and beyond, her hips are rocking back and forth causing her ass to slide up and down my cock, matching my rhythm making for harder thrusts."

                    "At this rate, all three of us are going to cum soon."

                    "I’m glad it doesn’t take long for a mare in heat to climax, because Riku is rocking her hips far too fast for me to hold back."

                    "Eventually her thrusts overpower mine, leaving me staying still behind her as she bounces up and down against my cock. All whilst her tongue drives Moxie ecstatic."

                    moxie "Ahhh, I’m gonna come!"

                    riku "Mmphhh *Lick, sclurp*."

                    "I can’t hold back either, my cock is growing tense and throbbing."
                    play sound cum
                    show riku threesome4 with cum
                    play sound cum
                    show riku threesome4 with cum
                    "The pressure in my loins reaches its peak as I begin to have a powerful orgasm, ejaculating several loads into Riku’s ass."
                    play sound cum
                    show riku threesome4 with cum
                    play sound cum
                    show riku threesome4 with cum
                    stop ambience fadeout 3.0
                    stop music fadeout 3.0
                    "All whilst Moxie wriggles with pleasure, her back arched as she too begins to orgasm."
                    show riku threesome4 with dissolve
                    show riku threesome5 with dissolve
                    "After an intense feeling of euphoria, my climax fades and I pull out."
                    scene bg moxiebednight with dissolve
                    "Riku lifts up from Moxie’s legs and rolls to the other side of the bed. She looks just as satisfied as Moxie and I, her tongue lulling out dramatically as she pants."
                    if fr == 1:
                        show moxie closewhorny with dissolve:
                            xpos 600
                            ypos 25
                    else:
                        show moxie closehorny with dissolve:
                            xpos 600
                            ypos 25
                    moxie "Damn Riku... If you're going to be such a good fuck, you gotta visit more often."
                    mc "You can say that again, her ass is so tight."
                    show riku closesatisfied with dissolve:
                        xpos 100
                        ypos 75
                    riku "Hehe, you're both flattering me. Let's go for a second round?"
                    moxie "Eager to dive back into my pussy I see?"
                    play sound cum
                    scene rikub threesome
                    show riku threesome4
                    with moxiespell
                    "With one of Moxie's spells, my cock is inside Riku's ass and fucking her again within seconds."
                    "The three of us fuck like rabbits until we all collapse into a long sleep."
                    scene bg black with dissolve
                    "..."
                    play ambience ambienceday fadein 2.0
                    show bg moxiebedday with dissolve
                    "When I wake up, I'm actually alone in bed. I can hear the girls in the living room chatting."
                    show bg moxiewagonday with dissolve
                    if fr == 1:
                        show moxie whappy with dissolve:
                            xpos 250
                            ypos 0
                    else:
                        show moxie happy with dissolve:
                            xpos 250
                            ypos 0
                    moxie "There's our man! We were thinking about going to the gym."
                    show rikub:
                        xpos 700
                        ypos 35
                    show riku happy:
                        xpos 700
                        ypos 35
                    with dissolve
                    riku "Yeah, do you want to come?"
                    mc "I think I'll get some breakfast and a shower first. I'll see you girls later."
                    moxie "Byee babe!"
                    scene bg moxiewagonday with dissolve
                    jump afteraltmorning
            "Blowjob":
                $ prismasex = 1
                play music sex1 fadein 3.0
                show riku closehorny with dissolve
                riku "Can't say no to that!"
                mc "Even though you're not getting anything out of it?"
                riku "Heh, you must be kiddin', I love giving blowjobs, now come'ere!"
                hide riku
                show rikub blowjob
                show riku blowjob1
                with dissolve
                play ambience blowjob fadein 3.0
                "She lays down on the sofa and starts to service my currently erect cock with her tongue, sliding it up and down the shaft."
                "Damn it feels good, her tongue is sensational."
                riku "Y'know, if you do want to pleasure me, you could always lean over and play with my pussy."
                "I reach over and start to rub her pussy, thankfully she’s quite small so I easily reach."
                "I rub at the area her clit would be, and she reacts favourably, I can visibly see her relax"
                riku "Ahh, mmphh... Perfect, keep up like that and you'll actually make me come."
                show riku blowjob2 with dissolve
                "She winks at me and starts to work the top of my cock expertly with her twirling tongue."
                "Slowly she started to take in my glans. She keeps bringing her mouth back and forth like waves hitting a beach, teasing me while sucking the sensitive tip."
                "It doesn’t take too long until her mouth is wrapped around my glans. She starts a fucking motion around my shaft while simultaneously working the head with her tongue."
                show riku blowjob1 with dissolve
                "She’s incredibly turned on; I easily sink two fingers deep inside her pussy while using my thumb to nimbly tease her clitoris."
                show riku blowjob3 with dissolve
                riku "Aaaahhhh! Yesh! Mmphhhshh… *Sclurrrp* *Suck*"
                "The pleasure from my handywork actively distracts her from the blowjob, she’s stifling moans into my cock and her tongue is moving around sloppily."
                riku "*Shlurp* Ahh, ahh… *Lick, lick* Mm!"
                "It feels no less amazing though, as her lips squeeze around my shaft and constantly bop up and down the neck of my glans like a sloppy mouth fuck. It's causing my orgasm to well up far faster than I was expecting."
                riku "Aahh- mmm… Mmphh, tell me when cumphh…"
                mc "I’m close, you’re too damn good at this!"
                show riku blowjob2 with dissolve
                "My cock began to throb as I approached the point of no return, however Riku surprised me by taking my cock deeper into her mouth."
                show riku blowjob1 with dissolve
                "She allowed my cock to slide all the way in as she effectively deep throated me without gagging, all whilst maintaining sexy bedroom eyes."
                "Her lips wrap around the base of my cock. I could feel her tongue flailing up and down against my shaft, that combined with the lecherous, sloppy, wet noises; it’s all too much. I can’t hold back any longer."
                play sound cum
                show riku blowjob5 with cum
                play sound cum
                show riku blowjob5 with cum
                "I began to forcefully ejaculate, several loads shooting against the back of her throat."
                play sound cum
                show riku blowjob5 with cum
                play sound cum
                show riku blowjob5 with cum
                "Riku’s eyes initially opened wide when she felt hot cum oozing down her throat, then her eyes rolled back, and her pussy tightens around my fingers as she climaxed too."
                riku "Mmmphhh! Mmmmphhhh!!! *Gulp*"
                show riku blowjob6 with dissolve
                "I’m barely pleasuring her right now, yet she was so turned on that she had an easy orgasm."
                stop ambience fadeout 3.0
                "Somehow she manages to swallow every single drop of cum before slipping my cock out of her mouth, a trail of spit coupling my glans and her mouth as she’s left panting for air."
                stop music fadeout 3.0
                hide rikub
                show riku closehorny
                with dissolve
                riku "Haah, haah, aaahh… *Pant, pant*"
                play ambience ambienceday fadein 3.0
                "That got really messy, all the fur around her mouth is sodden and dripping with saliva."
                "Yet, not a single drop of cum to be found."
                riku "Heh, not bad huh? I wonder what the nutritional value of cum is..."
                jump prerikumenu
            "Sideways Sofa Sex":
                play music sex1 fadein 3.0
                $ prismasex = 1
                riku "I feel like getting fucked, wanna take my pussy this time?"
                mc "Show me the goods and I'll get to work."
                hide riku
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
                show riku sofasex2 with dissolve
                "I push myself inside of her and immediately start moving my hips back and forth."
                show riku sofasex2 with dissolve
                show riku sofasex2 with dissolve
                riku "Aahhh, ahhh! I love the way your cock fills me up, mmm..."
                show riku sofasex2 with dissolve
                "I take my time and fuck her gently, savouring the tightness and warmth of her vagina. The long, slow thrusts drive her wild. "
                show riku sofasex2 with dissolve
                "With both my hands I fondle and squish her thick and juicy ass."
                show riku sofasex2 with dissolve
                riku "Mmm… Hehe, you really do love my butt."
                show riku sofasex2 with dissolve
                "She’s so soaking wet, every time I sink deep inside of her it’s accompanied by a saccharine squelching sound."
                show riku sofasex3 with dissolve
                riku "Ahh, ever since we've started fucking, I've been even hornier than usual lately, and even wetter..."
                show riku sofasex3 with dissolve
                "Truly there was a submissive slut ready to escape within Riku all along, she just needed the right key to let it out."
                riku "Spank me [playername], spank your little slut."
                show riku sofasex3 with dissolve
                "She guides my dominant hand and brings it to her ass, I know exactly what to do."
                show riku sofasex4 with dissolve
                riku "Gimme it as hard as last time, aahhh…"
                show riku sofasex4 with dissolve
                play sound spank
                "I raise my dominant hand and bring it down powerfully causing a slap sound, this seems to hit the spot as her eyes roll back and she lets out a satisfied moan."
                show riku sofasex4 with dissolve
                riku "Ohh phuck yesh…"
                show riku sofasex4 with dissolve
                "I can’t help but fuck a little faster, her hips are rocking in response to each thrust too, and her pussy squeezing even tighter around my cock."
                show riku sofasex4 with dissolve
                play sound spank
                riku "Aaahhh, aahhh, ah, ahhh! Oh fuck! I’m coming!!!"
                show riku sofasex4 with dissolve
                play sound spank
                "Spanking her out pushed her over the edge, and she starts to have a strong first orgasm, her hips bucking and her whole-body squirming as the pleasure overwhelms her."
                show riku sofasex4 with dissolve
                "I can feel my cock throbbing in response to her pussy contracting around it, I really could come any second if I let my guard down."
                show riku sofasex4 with dissolve
                riku "Faster Daddy, faster!  Ahhh, ahh! *Pant, pant*."
                show riku sofasex4 with dissolve
                "Why is she suddenly calling me daddy again?! That level of dirty talk is only going to make me cum faster."
                "It doesn’t help that she’s rocking her hips into me, practically fucking me just as hard as I’m fucking her, and damn it feels amazing."
                show riku sofasex4 with dissolve
                riku "Mmphh fuck! Spank me harder! *Pant, pant*."
                show riku sofasex4 with dissolve
                play sound spank
                "I spank harder, while her pussy squeezes and sucks harder around my shaft as if it’s trying to milk my cock. All whilst Riku moans and squeaks with erotic delight."
                show riku sofasex4 with dissolve
                "My orgasm keeps swelling up, I can’t hold back much longer, I’m going to cum!"
                show riku sofasex4 with dissolve
                "Riku arches her back, her eyes roll back and she lets out a sensational moan, as she has her second orgasm."
                show riku sofasex4 with dissolve
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
                stop music fadeout 3.0
                show riku sofasex6 with dissolve
                "As I pull out, a trail of cum still connects us, before it collapses down her thigh."
                stop music fadeout 10.0
                riku "Haah, I-I can barely feel my butt, hahaa. *Pant, pant*."
                show riku sofasex6 with dissolve
                mc "Your butt gets a lot of rough treatment from the spanking, anal and vaginal."
                hide rikub
                show riku closehorny
                with dissolve
                riku "Hahh, just the way I like it, hehe. I wish we had a unicorn right now so we could go for anal seconds!"
                mc "You shoulda said, I could have arranged something."
                jump prerikumenu
            "Anal Ride" if fr == 1:
                $ prismasex = 1
                show riku closehorny with dissolve
                riku "Oohh, that again? I like it, lay down and I’ll service you with my butt."
                play music sex1 fadein 3.0
                scene rikub anal
                show riku ranal1
                with dissolve
                "I lay down on Riku's sofa and she eagerly mounts me."
                "She grinds her plump labia back and forth against the tip of my cock. Occasionally she prods downwards onto it, teasing the idea of penetration."
                "In only a few seconds, her moist pussy has already drooled and dribbled an impressive amount of lubricants onto my cock’s head."
                "That however, is when she surprises me."
                "Moving her hips forward, I suddenly feel my lubricated tip prodding against the tight pucker of her anus."
                riku "Ehehe, butt slut for life!"
                play sound cum
                play ambience sex fadeout 3.0
                show riku ranal2 with dissolve
                "Her sphincter eases around cock and she slowly take me inside."
                "God damn, her ass feels so fucking good though. The tight ring slowly descends my shaft until she has my entire cock at hilt."
                mc "Damn Riku, where'd you get so good at this? God damn that feels good."
                riku "What can I say? Maybe my athleticism and speed is just too much for the average 'human' to handle!"
                "Pressing a hand against my chest, she lifts herself up slowly. The tightness of her ass scaling up each and every nerve ending of my throbbing shaft until it reaches the glans."
                "And then she sinks back down again, reigniting another flash of pleasure."
                "And again, again, again. She fucks me with passion, precision and speed; relentlessly providing my cock with immense pleasure."
                show riku ranal3 with dissolve
                riku "Mmphh, mmm! *Slap, slap, slap! * *Squish, slap! * You like my butt, don’cha?"
                "It wasn’t just me enjoying this though. Riku’s elation would have been obvious from her body language, but the really amazing thing is her pussy which constantly drips and squirts onto my pelvis from the light orgasms she’s experiencing."
                riku "Ahhhaa, mmm! Use me, fuck me, I’m all yours, [playername]!"
                "Her petite breasts shake wildly as she continues to deliver more vigorous thrusts, her ass pumping away at my cock."
                "As she starts feeling better and better, her eyes roll back and her fervent moaning intensifies as she nears her climax."
                "In a surge of energy, she races to an orgasm, her body shivering and pucker tensing."
                riku "Haahh, ahhh, g-gonna come, haahhh, yesss, yesss!"
                "My throbbing cock stiffens and my muscles grow tense as her assault on my cock brings me extremely close to cumming."
                play sound cum
                show riku ranal5 with cum
                play sound cum
                show riku ranal5 with cum
                "The additional speed is enough as we push past both our limits. Climaxing, my cock starts spraying thick loads of cum into her butt."
                play sound cum
                show riku ranal5 with cum
                play sound cum
                show riku ranal5 with cum
                riku "Haahh, yesssshhhh! F-Fuck! Fill my belly!"
                stop music fadeout 3.0
                stop ambience fadeout 3.0
                show riku ranal6 with dissolve
                "Riku excitedly rides out both our orgasms."
                "Satisfied, she huffs and slides my cock out with a pop."
                scene bg barupstairs with dissolve
                show rikub
                show riku laughing
                with dissolve
                riku "Phew that was really good! Sorry if I made you cum too quickly."
                riku "Maybe we could go shower together?"
                mc "Sure thing."
                scene bg black with dissolve
                scene bg barupstairs with dissolve
                "After a quick shower, Riku and I return to the sofa with a canned drink each."
                "This is relaxing, I could get used to this."
                show riku closehappy
                with dissolve
                jump prerikumenu
            "Back":
                jump rikumenu

        stop music fadeout 3.0
        scene bg black with dissolve
        "..."
        jump evening
label rikuclimbingsex:
    stop music fadeout 5.0
    stop ambience fadeout 5.0
    scene bg black with dissolve
    "Later..."
    play music farm fadein 5.0
    show bg climbingcentre with d
    show rikub climbing1
    show riku climbing1
    with dissolve
    riku "Simple enough when you get the hang of it, right? One limb at a time."
    riku "Stick to all three colours at first, but the better you get, the fewer colours you can use."
    mc "Ahh, so one wall can have multiple difficulties. Interesting!"
    riku "Heh, you’re still so slow on the beginner difficulty. Not that I’d expect you to keep up with me!"
    mc "Why would I want to keep up with you? The view from just behind you is excellent!"
    show riku climbing2 with d
    riku "Wah?! Have you been staring at my ass?"
    mc "Stare is a harsh word… It’s just kinda… there, above me, where I’m looking."
    show riku climbing3 with d
    riku "Eep! This got ten times more embarrassing."
    mc "What’s the deal? You’re usually nude anyway."
    riku "Pft, yeah, but… Not normally so exposed to a man I’m sexually attracted to."
    scene bg climbingcentre with d
    "The two of us step down from the climbing wall and look around the room. It’s a sports centre divided into several sections, and this is just one of those."
    "Thing is, the room is completely empty apart from us. A benefit of coming here at 8:30AM."
    mc "You thinking what I’m thinking?"
    show rikub
    show riku angry
    with d
    riku "Huh? What? Are you thinking about my ass?"
    mc "Yes, I guess. Ever had sex on a climbing wall?"
    show riku embarrassed with d
    riku "What kind of outlandish question is that? Oh shit, {i}that’s{/i} what you were thinking?"
    riku "You degenerate! Can’t I go anywhere without a sex scene? Is Moxie gonna walk in here and pin me down?"
    mc "Don’t you worry, just me and you."
    show riku shy with d
    riku "Hmph… Well… ‘Course I wanna fuck you now you’ve teased me. But how on earth am I supposed to have sex with you on the climbing wall? There’s no room."
    mc "Easy, I’ll be on the ground, and you’ll be clinging on tightly."
    show riku embarrassed with d
    riku "That’s the dumbest idea I’ve ever heard!"
    mc "Think of it like a challenge. Can you hold on until you’ve been creampied?"
    show riku horny with d
    riku "You’re on. We’re doing this."
    "Heh, Riku is so easy to lead on."
    show riku happy with d
    "Riku: Heh, [playername] is so easy to lead on."
    hide riku
    hide rikub
    with d
    "Anyway, Riku gets into position on the climbing frame. Given the actual position required to have sex with her, I won’t get a good view of her ass. But the image of her glorious ass is burned into my mind."
    show rikub climbing2
    show riku climbing2
    with dissolve
    play music sex1 fadeout 10.0
    "On my knees, I shuffle closer and start to rub her pussy. Spreading her lips. Teasing her clit. All the motions that’ll tease her so she can readily take my cock."
    riku "Heyy, what’re you teasing me for? I thought we were going to have sex."
    mc "All I said is that you have to hold on until I’ve filled you up. I didn’t specify any conditions."
    show riku climbing3 with d
    riku "Damn! No fair! You are real low! You know that?"
    mc "Just think of this as payback for that truth or dare game."
    show riku climbing2 with d
    riku "You already got payback for that!"
    mc "Ohh yeah…"
    riku "I bet you're loving this, aren't you?"
    mc "Nooo, of course not."
    "I am totally loving this."
    "To my surprise, as my fingers brush against her pussy, she’s already very wet."
    mc "How are you this wet already?"
    riku "Ehh, well… I’m kinda always this wet…"
    mc "That’s nice to know."
    "I bring the tip of my dick towards her pussy, but, instead of entering deeper, I teasingly glide my glans up and down the length of her vulva."
    show riku climbing3 with d
    riku "Mmphh… Come on, man... Teasing me like that is mean!"
    mc "Is the challenge too hard for you?"
    show riku climbing2 with d
    riku "Ghh, ahh… No way!"
    play sound cum
    show riku climbing5 with d
    play ambience sex fadein 20.0
    "I reposition my cock at her entrance and seamlessly push in, causing Riku to let off a cute moan. Her insides were soaking wet, allowing me to effortlessly slide in all the way."
    "I savour every inch of penetration, moving slowly forward until her entrance is tightly wrapped around the base of my cock. Even she can’t stay frustrated when it feels this good."
    riku "*Siiighh* That’s some good dick…"
    show riku climbing4 with d
    riku "You’re not uh, planning on going that slowly this entire time, are you? We are kind of in a public place."
    mc "Relax, if anyone comes inside, we’re in subtle enough of a position to pull out and not seem suspicious."
    riku "Mmphh.. If you say so…"
    show riku climbing5 with d
    "I begin thrusting, back and forth. I deliberately slide my cock almost all the way out, before allowing it to sink back in."
    "These deep thrusts always seem to drive Riku wild with pleasure, especially at the peak, where my cock seems to grind on an erogenous zone deep inside of her."
    "She manages to keep her body steadfast on the climbing wall. But she's also managing to keep her body loose enough to bounce along with the rutting. Her cute small breasts jiggle ever so slightly, and her soft butt cushioning the peak of each thrust."
    show riku climbing4 with d
    riku "Ahh… *Pant* I should have you on the wall while I ride you, make you see how it feels. Hah."
    mc "I bet it still feels good."
    show riku climbing5 with d
    riku "Mmpphh, I was never going to argue that… Your cock is really nice."
    "Even in the precarious position, her body reacts favourably to each pleasurable action. Her pussy occasionally squeezing, and she stifles a few moans."
    "Her arms don’t even seem slightly tired, but I haven’t forgotten how much of a physical specimen the unsuspecting Riku really is."
    "Let’s see how she handles it when I thrust even faster."
    riku "Oh, [playername]… That’s good, ahhh… Keep going that deep… Aaaahhhnn…"
    "Ah, she’s starting to really enjoy it! Her moans are starting to echo throughout the empty climbing facility, accompanied by lewd wet noises from the sex."
    "I kept going, thrusting deep inside her and soon I could feel her vagina tremble and tighten around my throbbing shaft. Is she getting close to coming already? She’s such a perv."
    riku "Ahhh… This feels too good, I’m gonna… Ahhh…"
    riku "I can’t take it any longer, ahh… I’m gonna come! Ahhhh!"
    "Yeah, she’s coming already. I can feel her insides vigorously contracting around my member in an effort to make me cum, and it’s working quite well."
    "I continue to fuck Riku’s pussy as she wriggles in pleasure. By pushing hard and faster I progressively get closer to climaxing myself."
    riku "Cum for me! I want you… *Pant* …Fill my pussy up with your cum! Ah ahhhh!"
    "Riku’s cute moans become one of the main things pushing me over the edge, and  soon enough, I’m no longer able to hold back."
    play sound cum
    show riku climbing6 with cum
    play sound cum
    show riku climbing6 with cum
    "My throbbing cock explodes deep inside, as I did, her vagina tightly gripped around my shaft, wringing even more cum out of it as we continued to fuck during our climaxes."
    play sound cum
    show riku climbing6 with cum
    play sound cum
    show riku climbing6 with cum
    riku "Ahhh… I can feel it, oh gosh, there’s so much, it’s so hot… Ahhhhh…"
    "I keep thrusting my hips throughout the orgasms. Several more loads of cum seeps deep into her vagina and womb."
    stop ambience fadeout 2.0
    show riku climbing7 with d
    "As my orgasm peaks and fades, I pull myself out of Riku’s pussy, some of my cum dripping out as I do"
    riku "Oohh… Ahh *Pant* Told you I could do it…"
    stop music fadeout 1.0
    play sound movement
    scene bg climbingcentre with d
    "Even though she says that, she weakly gets off the climbing wall and slumps over. Her arms much be a little worn out from hanging in place for so long."
    play music melodytheme
    show melody fufufu with d:
        xpos 75
        ypos 75
    melody "Bloody hell."
    show blossom embarrassed with d:
        xpos 450
        ypos 75
    blossom "You were right, Mel! It’s always [playername] making trouble."
    mc "Eh? H-Hey, how long have you been there?"
    show rikub:
        xpos 750
        ypos 50
    show riku embarrassed:
        xpos 750
        ypos 50
    with d
    riku "Oh, those two? They arrived about halfway in."
    mc "And you didn’t say anything?"
    show riku laughing with d
    riku "Meh, they’re all right, aren’t they? Hahaha."
    show blossom awkward with d
    blossom "Yeah, I mean, we’ve all already done it."
    show melody sadistic with d
    melody "He just can’t keep it to himself, can he? He has to go and fuck every mare he sees at any opportunity he can."
    show riku neutral with d
    riku "Hahaha. You’re making me feel a bit guilty now, Melody."
    show melody happy with d
    melody "Oh, my apologies, Riku. My bullying was entirely directed at that perv, not you."
    show blossom happy with d
    blossom "Uhm anyway, who’s up for some more climbing?"
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene bg black with dissolve
    if crystalballactivated == 1:
        jump cbmenu

    $ secretsunlocked += 1
    "Later on..."
    jump prerikumenu2


label barvisitevening:
    show bg bar with dissolve
    play music day2 fadein 3.0
    "Even at this time the bar is bright and busy."
    if doggirl1 == 1 and wolfgirl1 == 1 and doubledog == 0:
        $ doubledog = 1
        jump doubledoggo
    menu eveningbarmenu:
        "Who should I talk to?"
        "[doggirl]" if rand >= 3:
            # rosa
            if doggirl1 == 0:
                "There's a cute smol dog girl sat alone at the bar, her legs swaying back and forth on the stool."
                "Looks like she's waiting for someone to approach her, I'll take my chance."
                show rosa char with dissolve
                if monies == 0:
                    mc "Hey, how's it going?"
                    doggirl "Ahh, just drinking by my lonesome. Care to join me?"
                    mc "With a cute girl like yourself? I'd love to."
                    doggirl "How about a whiskey with cola? I'll buy two."
                    mc "Ohh, that's very sweet of you. The name's [playername] by the way, when I saw you I just knew I had to say hi."
                else:
                    mc "Hey, fancy a drink? I'm buying."
                    doggirl "Ohh! This is a surprise, how about a whiskey with cola?"
                    mc "Awesome, I'll get two. The name's [playername] by the way, when I saw such a cute girl by herself I just knew I had to say hi."
                $ doggirl = "Rosa"
                doggirl "My name's Rosa, and it's not every day someone else does the approaching. Least not a charming man such as yourself."
                mc "Really? I thought you'd be quite popular, you are beautiful."
                doggirl "Hehe... I'm not popular at all, the stallions around here are much more interested in mares."
                doggirl "If I ever want to talk to someone I have to do the approaching and drink buying, honestly this is overwhelming."
                mc "Well, I'm not exactly clued in with the local culture."
                doggirl "Hehe, you're not from around here, I can tell that much."
                mc "What about you? I think you're the first... what's your species called?"
                doggirl "Just call me a dog girl! And actually, I am from around here! I work in the city as an accountant."
                stop music fadeout 3.0
                scene bg black with dissolve
                "Rosa and I talk at length while drinking more and more alcohol."
                "With more booze she gets increasingly giggly and flirty, after two hours of impassioned conversation she blushes and asks me if I'd walk her home."
                "But she wasn't planning on letting me walk back that night."
            else:
                "It's her again! That crazy bundle of sexual energy."
                show rosa char with dissolve
                doggirl "Ohh, [playername]! It's great to see you."
                mc "How about a whiskey and cola, Rosa?"
                doggirl "Hehe, I'll pay for the next round. You really make an unpopular girl like me feel cherished."
                stop music fadeout 3.0
                scene bg black with dissolve
                "Two hours later..."
            play music sex1 fadein 3.0
            stop ambience fadeout 10.0
            scene bg rosabedroom
            show rosa sex1
            with dissolve
            if doggirl1 == 0:
                doggirl "Haahh, f-fuck! I betcha didn't know us doggies go into heat too."
                doggirl "T-That's right, hehehe, I'm your little bitch tonight."
            else:
                doggirl "F-fuck me [playername]! I have a lust that only your magical cock can sate!"
            "The drunken dog girl slurs her lustful words and spreads her cheeks."
            if doggirl1 == 0:
                doggirl "I'm no stranger to a stallion cock in the asssss, so you can fuck me any which way you want, sexy."
                "She's so much smaller than I am, but if she says she can take it, I'll give it to her."
            else:
                doggirl "Maybe give my other hole some attention this time? I love being FUCKED in both equally."
            menu:
                "Vaginal":
                    "I kneel in position, thoughts of sliding my cock deep into her pussy slowly drive my drunken state into a frenzied lust."
                    "Her pussy is drooling with sexual lubricants, giving the vague idea that she has been anticipating this for a while."
                    "Rosa coos as I get into position and press my erection against her delicate folds."
                    play sound cum
                    show rosa sexv1 with dissolve
                    "Her tail won't stop thrashing around, so I grab it and pull it whilst simultaneously sinking my member into the tight, welcoming warmth of her vagina."
                    "She yelps at the feeling of the first insertion, although the blissful and eager expression on her face signals that she wants more."
                    doggirl "Mmphhh, eheh, I didn't take you for a rough lover..."
                    play ambience sex fadein 3.0
                    "I grab her by the ass for leverage and begin slow thrusts, giving her tight pussy time to adjust to my thick shaft."
                    doggirl "Aahh, ahhh... T-That's sho fuckin' gooood! Haaah, ahhh, aaaaahhhhhhhh!"
                    "Gradually I increase the tempo, the sound of our lovemaking increasing in volume as she moans, gasps and pants with increasing volume; she's an extremely vocal lover."
                    "Before long, I'm pounding her plump pussy so hard it makes her entire body and bed jiggle back and forth."
                    "The drunk dog girl seems to lose herself in the moment, her thighs quivering and her tensed fingers grappling at the bedsheets."
                    doggirl "Aahhh, aaaahhhh! *Schlick, schlick!* Ahhhh, fuck me! Ahhhhhhhh!"
                    play sound spank
                    "With her tail already being pulled, I add to the roughness by giving her furry ass a hard slap, the thwack of my palm ripples her bubbily butt and causes her to cry out in euphoria."
                    doggirl "Phaaahhhh aahhh, f-fuck! I-I want you! Cum in me, please!"
                    "She barely finds the word between a mix of moans and incoherent gibberish."
                    doggirl "Aahhh, ahhh! *Schlick, squelch, prod!* Fuck me! Ravage my p-pussy! Hahhh, fill me with cum!"
                    "Rosa's entire body shudders as her words escaped on erratic breath, her increasingly lewd words alone are pushing me to an early orgasm, even against my attempts to hold back and savour her pussy."
                    doggirl "AAHHHH! BREED ME LIKE A BITCH! CUM IN ME! I WANT IT ALL! AAHHHHH-HAAAAHH!!"
                    "She enthusiastically howls as her body is overwhelmed with an orgasm to be jealous of, all whilst I ferociously fuck her cunt."
                    "Her clenching insides drive me over the point of no return, and I can feel the release surging through my nethers."
                    play sound cum
                    show rosa sexv2 with cum
                    play sound cum
                    show rosa sexv2 with cum
                    "The slutty dog finally gets her wish as I begin to shoot my hot load into her fuckhole, enveloping her insides with my seed."
                    play sound cum
                    show rosa sexv2 with cum
                    play sound cum
                    show rosa sexv2 with cum
                    doggirl "Yesss, haaahh... Yeeeesssssss... Haah.... Haaah..."
                    stop ambience fadeout 3.0
                    show rosa sexv3 with dissolve
                    "My exhausted partner swoons as she catches her breath, with a deep breath of my own I pull loose and cuddle up to her side."
                    doggirl "By the sisters, that was... amazing... I didn't think I could cum that hard..."
                    doggirl "F-Fuck stallions, I mean, no, don't fuck stallions! Fuck you! Haha, fuck you, fuck you... I-I'm sleepy..."
                    "With her as the little spoon, I give her one last sensual kiss before the two of us drift off to sleep."
                "Anal":
                    "I kneel in position, thoughts of sliding my cock deep into her ass slowly drive my drunken state into a frenzied lust."
                    "Her pussy may be drooling with desire, but the tight ass on this small dog girl will provide more of a challenge."
                    doggirl "Hehe, if you wanna put it up my butt, there's some lube in the bedside drawer."
                    "Rosa coos as I apply the cool, sensual lubrication and then press my erection against her pucker."
                    play sound cum
                    show rosa sexa1 with dissolve
                    "Her tail won't stop thrashing around, so I grab it and pull it whilst simultaneously sinking my member into the tight, welcoming warmth of her ass."
                    "She yelps at the feeling of the first insertion, although the blissful and eager expression on her face signals that she wants more."
                    doggirl "Mmphhh, eheh, I didn't take you for a rough lover..."
                    play ambience sex fadein 3.0
                    "I grab her by the ass for leverage and begin slow thrusts, her ass clenches around my shaft, giving way to a soft and slick massaging beyond."
                    doggirl "Aahh, ahhh... T-That's sho fuckin' gooood! Haaah, ahhh, aaaaahhhhhhhh!"
                    "Gradually I increase the tempo, the sound of our lovemaking increasing in volume as she moans, gasps and pants with increasing volume; she's an extremely vocal lover."
                    "Her anal experience is clear, and before long, I'm pounding her ass so hard it makes her entire body and bed jiggle back and forth."
                    "The drunk dog girl seems to lose herself in the moment, her thighs quivering and her tensed fingers grappling at the bedsheets."
                    doggirl "Aahhh, aaaahhhh! *Schlick, schlick!* Ahhhh, fuck me! Ahhhhhhhh!"
                    "With her tail already being pulled, I add to the roughness by giving her furry ass a hard slap, the thwack of my palm ripples her bubbily butt and causes her to cry out in euphoria."
                    doggirl "Phaaahhhh aahhh, f-fuck! I-I want you! Cum in me, please!"
                    "She barely finds the word between a mix of moans and incoherent gibberish."
                    doggirl "Aahhh, ahhh! *Schlick, squelch, prod!* Fuck me! Ravage my a-ass! Hahhh, fill me with cum!"
                    "Rosa's entire body shudders as her words escaped on erratic breath, her increasingly lewd words alone are pushing me to an early orgasm, even against my attempts to hold back and savour her ass."
                    doggirl "AAHHHH! BREED ME LIKE A BITCH! CUM IN ME! I WANT IT ALL! AAHHHHH-HAAAAHH."
                    "She enthusiastically howls as her body is overwhelmed with an orgasm to be jealous of, all whilst I ferociously fuck her asshole."
                    "Her clenching insides drive me over the point of no return, and I can feel the release surging through my nethers."
                    play sound cum
                    show rosa sexa2 with cum
                    play sound cum
                    show rosa sexa2 with cum
                    "The slutty dog finally gets her wish as I begin to shoot my hot load into her fuckhole, enveloping her insides with my seed."
                    play sound cum
                    show rosa sexa2 with cum
                    play sound cum
                    show rosa sexa2 with cum
                    doggirl "Yesss, haaahh... Yeeeesssssss... Haah.... Haaah..."
                    stop ambience fadeout 3.0
                    show rosa sexa3 with dissolve
                    "My exhausted partner swoons as she catches her breath, with a deep breath of my own I pull loose and cuddle up to her side."
                    doggirl "By the sisters, that was... amazing... I didn't think I could cum that hard..."
                    doggirl "F-Fuck stallions, I mean, no, don't fuck stallions! Fuck you! Haha, fuck you, fuck you... I-I'm sleepy..."
                    "With her as the little spoon, I give her one last sensual kiss before the two of us drift off to sleep."
            stop music fadeout 2.0
            scene bg black with dissolve
            "Our morning is short-lived, as a business lady she needs to get to work, so we end up parting ways early."
            if doggirl1 == 0:
                $ doggirl1 = 1
                "However, she tells me that she'd really like to do this again sometime. We exchange addresses for magic mail, and vow to perhaps meet each other again in the bar."
            else:
                "She tells me that if I show up in the bar, she'll drop anything to come talk to me now."
            jump altmorning
        "[wolfgirl]" if rand <= 2:
            # hilda
            if wolfgirl1 == 0:
                "The wolf girl barely gives me a chance to approach before she notices me looking her way and approachs me herself."
                show hilda char with dissolve:
                    xpos 360
                    ypos 0
                wolfgirl "Hey! It's always nice seeing another non-pony around here, the name's Hilda. How about yourself?"
                "Building up the courage to approach is hard, so it's nice to have the tables turned."
                $ wolfgirl = "Hilda"
                mc "Hey Hilda, I'm [playername], where abouts are you from?"
                wolfgirl "I'm an adventurer so I've always been on the road. But I like using Arcadia as a hub to sell my loot, and take on bounties."
                mc "An adventurer, huh? I've never met one before."
                wolfgirl "It's a more pleasant word than 'mercenary', I take odd jobs from anonymous employers. Sometimes I could be clearing monsters, collecting rare ingredients, or delivering packages."
                mc "Sounds like a lot of fun, I'm surprised a society like this has such a niche."
                wolfgirl "Hehe, green around the ears are ya? I can see why you'd say that if you live in Arcadia, this is by far the safest place in the country. If you were to travel somewhere else though, there's plenty of work opportunities for an adventurer like myself."
                wolfgirl "By the way, can I get ya a drink? Nothing like a good drink to unwind after a long day of work."
                mc "Agree with you there, how about some cider?"
            else:
                "With her sharp eyes, Hilda picks me out in the crowd and saunters over with a grin."
                show hilda char with dissolve:
                    xpos 360
                    ypos 0
                wolfgirl "Hey sexy, ready for a fun night of deja vu?"
                mc "Forget deja vu, let's make it even better than last time."
                wolfgirl "Oohh, you're such a catch, lemme get ya a drink, ehehe."
            stop music fadeout 3.0
            scene bg black with dissolve
            if wolfgirl1 == 0:
                "Hilda and I get to know each other, soon she starts to flirt with me and the reason she approached me becomes clear."
            else:
                "Hilda and I enjoy chatting and getting drunk together before things get flirty."
            "After a couple of hours, she invites me to her place..."
            scene bg hildabedroom with dissolve
            show hilda sex1 with dissolve
            play music sex1 fadein 3.0
            if wolfgirl1 == 0:
                wolfgirl "I've been eyeing up that delicious cock all night, now pick a hole big boy."
            else:
                wolfgirl "In all my years of adventuring, ya might be one of my favourite fucks yet, gimmie some sugar, lover!"
            menu:
                "Vaginal":
                    stop ambience fadeout 10.0
                    "With her legs lifted up, I have a clear view of her wet pussy."
                    show hilda sex2 with dissolve
                    play sound cum
                    "*Schlick*"
                    wolfgirl "Like what ya see?"
                    show hilda sex1 with dissolve
                    "I begin to fondle my cock into an erection... When I'm ready, I grab the wolf girl's hips and pull her towards me."
                    if wolfgirl1 == 0:
                        wolfgirl "Eep! That's the thickest cock I've ever seen!"
                    else:
                        wolfgirl "Mmm, I love how thick your species' cocks are! Way better than a stallion, and you can fuck way longer than a canine."
                    "I tap my cock on her furry butt; enjoying the soft feeling as Hilda anxiously awaits my next move. However, I choose to tease her a little longer, playing with her pussy and engaging in extra foreplay."
                    "Her anxiety grows into impatience as I tease and massage her cute butt, her attempts at grinding against me do not go unnoticed."
                    wolfgirl "C'mon! Stahp teasing ya stud!"
                    play sound cum
                    show hilda sexv1 with dissolve
                    pause 0.3
                    play sound spank
                    "I giggle and give her ass a playful slap as I position my cock at the lips of her hot pussy, and with one thrust I plunge my cock into the warmth and wetness."
                    wolfgirl "Haaahh, th-that's really- haah, good!"
                    mc "Made only better by the teasing."
                    play ambience sex fadein 2.0
                    "I roughly pound the wolf girl's pussy, maintaining a firm grip on her thighs, she keeps her legs raised for the duration making it even tighter."
                    "The sound of our sexes slapping against each other mix and echo with her moans and howls of delight. It truly is an erotic symphony to the ears."
                    "I keep up for a few minutes, fucking her while occasionally slapping her ass and playing with her tits. I can feel her orgasm starting to come."
                    wolfgirl "Aahhhh, w-what a good cock! I-I'm I'm gonna, I-I'm coming! Awwwwoooooooooo!"
                    "She climaxes, her pussy clenches around my member as she squeals with pleasure. But I'm not done yet, perhaps with a bit of whiskey dick, I still have some more fucking to do."
                    "I grit my teeth and continue to pulverize her pussy, driving my cock deeper and faster than before, causing Hilda's body to jiggle back and forth along the bedsheets."
                    wolfgirl "Haaaahhh, y-you're crazy! F-FUCK! Aaaahhhhhh! *Squish, squelch!*"
                    "Still in an orgasmic daze, Hilda claws and grasps the bedsheets so aggressively that her claws threaten to tear the fabric, her quivering thighs struggling to remain upright."
                    "I can feel my orgasm finally begin to boil up, and no doubt my wolf companion has already been racked to the core by a second orgasm; judging by her hysteric movements and moans."
                    play sound cum
                    show hilda sexv2 with cum
                    play sound cum
                    show hilda sexv2 with cum
                    "My orgasm finally arrives and overwhelms me with its glory, my vision turns white as a torrent of thick jism spews into Hilda's pussy and womb."
                    play sound cum
                    show hilda sexv2 with cum
                    play sound cum
                    show hilda sexv2 with cum
                    stop ambience fadeout 3.0
                    "Three loads, six, then nine. The wolf's pussy is filled to the brim, so much that it readily oozes and spills out."
                    show hilda sex3 with dissolve
                    "As I pull out, a thick droplet of cum drips down over her anus and pools in the fur of her tail."
                    stop music fadeout 3.0
                    wolfgirl "Haahh, t-that was one hell of a fuck, [playername]..."
                    mc "You're just so sexy, I couldn't resist."
                    show hilda sex4 with dissolve
                    "*Schlick*, I spread her pussy and admire my work, this action causes Hilda to giggle."
                "Anal":
                    stop ambience fadeout 10.0
                    "With her legs lifted up, I have a clear view of her wet pussy; and under that, her tight pucker."
                    show hilda sex2 with dissolve
                    play sound cum
                    "*Schlick*"
                    wolfgirl "Like what ya see?"
                    show hilda sex1 with dissolve
                    "I begin to fondle my cock into an erection, when I'm ready, I grab the wolf girl's hips and pull her towards me."
                    if wolfgirl1 == 0:
                        wolfgirl "Eep! That's the thickest cock I've ever seen! T-That'll barely fit in my butt!"
                        "I tap my cock on her furry butt; enjoying the soft feeling as Hilda anxiously awaits my next move. I prod the tip against her pucker and I'm immediately met with notable resistance."
                        wolfgirl "*Pant*, m-maybe try spitting?"
                    else:
                        wolfgirl "Mmm, wanna do it in my ass? Just a tiny bit of drool should let you slide deep inside..."
                    "With a gracious amount of drool applied to the tip of my cock I try pressing my member against her sphincter again, that combined with her relaxation..."
                    play sound cum
                    show hilda sexa1 with dissolve
                    wolfgirl "Haaah! It's in! Pheewww, that feels good... I like it when it hurts, hehe."
                    play sound spank
                    "I giggle and give her ass a playful slap as I allow my cock to sink deeper into the warmth and wetness."
                    wolfgirl "Haaahh, th-that's really- haah, good!"
                    play ambience sex2 fadein 2.0
                    "Starting slowly, I gently fuck the wolf girl's ass allowing her time to adjust to my girth. The tightness, especially around the base of my cock, is immense."
                    "It's clearly not her first time experiencing anal though, and before long I'm able to speed up. I maintain a firm grip on her hips for leverage while she keeps her legs raised for the duration, making it even tighter."
                    "The sound of our sexes slapping against each other mix and echo with her moans and howls of delight. It truly is an erotic symphony to the ears."
                    play sound spank
                    "I keep up for a few minutes, fucking her while occasionally slapping her ass and playing with her tits. I can feel her orgasm starting to come."
                    wolfgirl "Aahhhh, w-what a good cock! I-I'm I'm gonna, I-I'm coming! Awwwwoooooooooo!"
                    "She climaxes, her ass clenches around my member as she squeals with pleasure. But I'm not done yet, perhaps with a bit of whiskey dick, I still have some more fucking to do."
                    "I grit my teeth and continue to pulverize her rump, driving my cock deeper and faster than before, causing Hilda's body to jiggle back and forth along the bedsheets."
                    wolfgirl "Haaaahhh, y-you're crazy! F-FUCK! Aaaahhhhhh! *Squish, squelch!*"
                    "Still in an orgasmic daze, Hilda claws and grasps the bedsheets so aggressively that her claws threaten to tear the fabric, her quivering thighs struggling to remain upright."
                    "I can feel my orgasm finally begin to boil up, and no doubt my wolf companion has already been racked to the core by a second orgasm; judging by her hysteric movements and moans."
                    play sound cum
                    show hilda sexa2 with cum
                    play sound cum
                    show hilda sexa2 with cum
                    "My orgasm finally arrives and overwhelms me with its glory, my vision turns white as a torrent of thick jism spews into Hilda's ass."
                    play sound cum
                    show hilda sexa2 with cum
                    play sound cum
                    show hilda sexa2 with cum
                    stop ambience fadeout 3.0
                    "Three loads, six, then nine. The wolf's butt is filled to the brim, so much that it readily oozes and spills out."
                    show hilda sex3 with dissolve
                    "As I pull out, a thick droplet of cum drips down over her anus and pools in the fur of her tail."
                    stop music fadeout 3.0
                    if wolfgirl1 == 0:
                        wolfgirl "Haahh, fuck... I don't know when I became such a masochist in bed, but that pain felt so good."
                        wolfgirl "Next time, and there will be a next time, ya gotta pull my tail!"
                    else:
                        wolfgirl "Haahh, fuck... Ya cock is a wild ride, you're giving the men of my species a tough act to follow up on."
            scene bg black with dissolve
            $ wolfgirl1 = 1
            "Finally spent, the both of us resign to snuggling together in the comfortable bed."
            "We wake up fairly early in the morning and actually decide to have another session of sex before parting ways."
            "She tells me to catch her in the bar again sometime, she won't pass the opportunity if she sees me alone."
            jump altmorning
        "Midna" if rand == 2 and midnabar == 1 or rand == 3 and midnabar == 1:
            if midnasexd == 0:
                $ midnasexd = 1
                "Ah, there's the blacksmith from the market, Midna, right? She offered to buy me a drink if she saw me here, time to cash in."
                show midna happy with dissolve
                mc "Hey Midna, great to see you."
                midna "Hey man, about time someone attractive came along."
                mc "The stallions not treating you well?"
                show midna with dissolve
                midna "Eh, those fuckers can't handle a woman like me, my ex was a dragon after all."
                "Looking around, there are a few stallions in here, but they're {i}all{/i} paired with a mare, or two."
                "In contrast, there are far more mares alone or amongst themselves."
                show midna happy with dissolve
                midna "Hey, let me get you a drink?"
                mc "Heh, you trying to get lucky?"
                midna "You know it lad, I gotta soften you up with some booze first tho, right?"
                mc "I'll take something strong."
                midna "I like your style."
                stop music fadeout 3.0
                scene bg black with dissolve
                "Midna and I chat about various interesting topics as we progressively get more drunk."
                "Midna is not a flirty type, she's more the type to outright ask for sex."
                show bg midnabedroom
                show midna pet1 with dissolve
                play music sex1
                stop ambience fadeout 10.0
                "However, she is surprisingly kinky. She has this red collar with a leash."
                midna "Aye, I like it as rough as I am rough around the edges!"
                midna "I want you to treat me like a pet, and pull my leash while you fuck me, master!"
                "Her attitude and fetish are an odd combination, but my erection doesn't care."
                "As I contemplate the delicious possibilities, I waste no time shuffling into position on the bed."
                "Her mare pheromones are coming across unusually strong, causing my cock to throb and drip with precum."
                play sound cum
                show midna pet2 with dissolve
                "I take hold of her leash with one hand, and align the tip of my cock with the other and I finally push myself in."
                midna "Aahh, yes master! Yer naughty Kitty's pussy needs your cock so badly!"
                "K-Kitty? Whatever, I sink into the depths of her inviting pussy and push as far as I can, her insides caress every inch of my shaft until she takes me to the hilt."
                show midna pet3 with dissolve
                midna "Mmphh, does master like Kitty's tight pussy?"
                "It is surprisingly tight, it would seem that Midna is purposely clenching her vagina to please my cock."
                show midna pet2 with dissolve
                midna "Ohh, pull the leash tighter mwaster!"
                play ambience sex
                "I pull the leash and the well-strung collar chokes the kitten-roleplaying mare while I begin to hump her."
                "Her hips gyrate back and forth in tandem with my movements, ensuring that each thrust slides into her deepest and most sensitive areas."
                "Truly Midna's technique is exquisite, my cock is already throbbing with pleasure."
                "The two of us drunkenly and hornily rut at an increasing intensity, my grip constantly tugging and teasing at the leash choking her more."
                "Her tail thrashes about excitedly as each thrust gets faster and harder, causing her teardrop breasts to jiggle back and forth."
                show midna pet3 with dissolve
                midna "Haahh, m-master your cock is gonna make me come! Haaahhh!"
                "She wraps her legs around my hips and pulls me closer, her encouraging words spur on a faster fuck and a tighter pull on the leash."
                "Midna's moans escalate as I speed up, after about twenty seconds of consistent pleasure a small gush of squirt escapes her pussy as she climaxes."
                midna "Aaahhh! I-I'm coming master! Aaahhhh!"
                "She screams, almost neighing, as her vagina clenches tightly around my cock and threatens to make me cum almost immediately."
                midna "Master, fill Kitty's pussy up with your cum!"
                "Her encouraging words are just enough to push me past the point of no return."
                play sound cum
                show midna pet4 with cum
                play sound cum
                show midna pet4 with cum
                "My cock tightens as the first of many loads of cum splatter against Midna's insides, she cries out in delight at the sensation of hot cum gushing inside of her."
                play sound cum
                show midna pet4 with cum
                play sound cum
                show midna pet4 with cum
                midna "Nyaa, master's cumming inside my pussy! Breed me, master! Hehe."
                stop ambience fadeout 3.0
                "Excess drops of cum escape the seal formed by my cock, smearing her fortunately white bedsheets with the results of our coupling."
                show midna pet5 with dissolve
                "The two of us are utterly satisfied."
                show midna pet4 with dissolve
                midna "Mmm, I like my new master..."
                mc "New master? Are you dedicating yourself to me or something?"
                stop music fadeout 3.0
                show midna pet5 with dissolve
                midna "Well, when I have this collar on anyway, lad, ahaha."
                scene bg black with dissolve
                "I can't say I expected Midna to have a fetish like that, but sometimes people are impossible to predict."
                "You never truly know someone until you sleep with them. After this, I may never look at Midna the same way."
                "We snuggle and sleep together as lovers, and by morning she's back to her usual self."
                play ambience ambienceday
                show bg worldmapdaynoui with dissolve
                "We walk together as she goes to setup her market stall, and I return home."
                show midna happy with dissolve
                midna "Don't forget to come see me again lad, I'll give you a small discount at the market, and in the bar? Drinks are on me."
                $ midnadiscount = 1
                mc "You're too good to me, Midna."
                midna "Only the best for mwaster!"
                hide midna with dissolve
                "What a girl."
                jump altmorning
            else:
                "It's the kitten roleplaying Midna, my cock tingles just at the thought of approaching her, she really was good in bed."
                show midna happy with dissolve
                mc "Hey Midna, great to see you."
                midna "Hey man, I've been thinking about you."
                mc "Oh really? Of my charming good looks and personality I imagine."
                midna "Actually, I thought about what you said about 'dedicating' myself to you. Is that something you like?"
                mc "What do you mean?"
                midna "Ah well, y'know... I won't sleep around and stuff."
                mc "That's up to you, I'm still going to sleep around, just being honest."
                midna "Heh, you're such a fuckin' player."
                midna "My fetish is being 'owned' though, so I don't really give a shit if you sleep around."
                midna "Actually, is that my pussy getting moist or is it even hotter if you sleep around?"
                mc "Well, being 'owned' and being 'lovers' are different dynamics, if I sleep with others that adds to the ownership dynamic because it makes you more of an object."
                midna "Awh yeah, a technical breakdown of my fetish, that's the stuff."
                midna "Look, I'm really horny, do you wanna skip the booze and just go fuck?"
                mc "Suppose I could."
                midna "Let's get outta this joint so I can start roleplaying!"
                stop music fadeout 3.0
                scene bg black with dissolve
                "Midna and I hastily go to her house."
                show bg midnabedroom
                show midna pet1 with dissolve
                play music sex1
                stop ambience fadeout 10.0
                "With her red collar tightly on, and leash presented to me, her owner..."
                midna "Come on master, fuck your kitten! Breed her like a slut!"
                "As I contemplate the delicious possibilities, I waste no time shuffling into position on the bed."
                "Her mare pheromones are unusually strong as before, causing my cock to throb and drip with precum."
                play sound cum
                show midna pet2 with dissolve
                "I take hold of her leash with one hand, and align the tip of my cock with the other and I finally push myself in."
                midna "Aahh, yes master! Yer naughty Kitty's pussy needs your cock so badly!"
                "I sink into the depths of her inviting pussy and push as far as I can, her insides caress every inch of my shaft until she takes me to the hilt."
                show midna pet3 with dissolve
                midna "Mmphh, does master like Kitty's tight pussy?"
                mc "Mmmhh yeah, Kitty's pussy feels so fucking good."
                midna "Ahah, thank you so much master!"
                show midna pet2 with dissolve
                play ambience sex
                "I pull the leash and the well-strung collar chokes the kitten-roleplaying mare while I begin to hump her."
                "Her hips gyrate back and forth in tandem with my movements, ensuring that each thrust slides into her deepest and most sensitive areas."
                "Truly Midna's technique is exquisite, my cock is already throbbing with pleasure."
                show midna pet3 with dissolve
                midna "Haahh, m-master your cock is gonna make me come! Haaahhh!"
                "She wraps her legs around my hips and pulls me closer, her encouraging words spur on a faster fuck and a tighter pull on the leash."
                "Midna's moans escalate as I speed up, after about twenty seconds of consistent pleasure a small gush of squirt escapes her pussy as she climaxes."
                midna "Aaahhh! I-I'm coming master! Aaahhhh!"
                "She screams, almost neighing, as her vagina clenches tightly around my cock and threatens to make me cum almost immediately."
                midna "Master, fill Kitty's pussy up with your cum!"
                "Her encouraging words are just enough to push me past the point of no return."
                play sound cum
                show midna pet4 with cum
                play sound cum
                show midna pet4 with cum
                "My cock tightens as the first of many loads of cum splatter against Midna's insides, she cries out in delight at the sensation of hot cum gushing inside of her."
                play sound cum
                show midna pet4 with cum
                play sound cum
                show midna pet4 with cum
                midna "Nyaa, master's cumming inside my pussy!"
                stop ambience fadeout 3.0
                "Excess drops of cum escape the seal formed by my cock, smearing her fortunately white bedsheets with the results of our coupling."
                show midna pet5 with dissolve
                "The two of us are utterly satisfied."
                show midna pet4 with dissolve
                midna "Mmm, I like being your kitty..."
                stop music fadeout 3.0
                show midna pet5 with dissolve
                scene bg black with dissolve
                "We snuggle and sleep together as lovers, and by morning she's back to her usual self."
                play ambience ambienceday
                show bg worldmapdaynoui with dissolve
                "We walk together as she goes to setup her market stall, and I return home."
                jump altmorning
        "Butters" if rand2 >= 3 and forestvisit3 == 1 and barvisit2 == 1:
            if buttersrikuthreesome == 0:
                $ buttersrikuthreesome = 1
                show butters dresshappy with dissolve:
                    xpos 550
                    ypos 10
                if livingwithbutters == 1:
                    "Butters decided to come with me to the bar tonight, so I'll keep her some company rather than chatting up another girl."
                    "As we order a drink and take a seat, Riku joins us during her shift."
                else:
                    "I spot Butters having a drink, as I sit down and say hello, a third person shows up!"
                show rikub:
                    xpos 150
                    ypos 50
                show riku happy:
                    xpos 150
                    ypos 50
                with d
                riku "Hey, I haven't seen you in ages Butters, how's it going?"
                butters "Ohh, hello Riku. I'm sorry I've been so quiet lately, I had some important business to take care of recently."
                show riku laughing with dissolve
                riku "I see you've had a chance to meet the fine [playername] though!"
                show butters dresslaughing with dissolve
                butters "Hehe, he is good, isn't he?"
                mc "Awh girls, you flatter me."
                show riku neutral with dissolve
                riku "My shift is ending soon, so how about I join you and grab the next round of drinks?"
                mc "Sounds good to me, right Butters?"
                show butters dresshappy with dissolve
                butters "Uhm, yeah! Thank you Riku."
                hide riku
                hide rikub
                with dissolve
                "Riku disappears momentarily to finish off her shift leaving Butters and I to chat."
                show butters dressneutral with dissolve
                butters "Hmm... [playername], I don't know how well I'll be able to handle my drink."
                mc "What? I'm sure you'll be fine, you can always stop if you're feeling unwell."
                butters "W-well, I haven't had anything to drink in a very, very long time, that means I'll be a 'lightweight', right?"
                mc "That's a good thing though, you'll get drunk faster!"
                show butters dresslaughing with dissolve
                butters "Ooohh, drunk faster? That's a good thing? Okay!"
                stop music fadeout 3.0
                scene bg black with dissolve
                "One hour later..."
                show bg bar with dissolve
                show butters dresshorny:
                    xpos 550
                    ypos 10
                show rikub:
                    xpos 150
                    ypos 50
                show riku happy:
                    xpos 150
                    ypos 50
                with d
                play music challenge fadein 2.0
                butters "Gaahahaaa, I swear if I ever seeeee thaaaat plant again, I'll return the favour!"
                show riku embarrassed with dissolve
                riku "I can't believe you actually found such a scary Alraune in Arcadia!"
                mc "It's a long story..."
                show butters dressangry with dissolve
                butters "Pshhh, yeeeaaah, weellll... Thaaat plant can go fuck herself next time!"
                show riku laughing with dissolve
                riku "Butters is really opening up after a few drinks! I didn't expect this."
                butters "O-Opening up? I'm not some cheeeaap slut that just opens up for any man!"
                show riku embarrassed with dissolve
                mc "She didn't mean opening your legs."
                show butters dresshorny with dissolve
                butters "For you [playername]? Any time! Aaahahaha."
                show riku happy with dissolve
                riku "O-Oh my, I didn't realize you two had a relationship like that."
                mc "Ahh, yeah... That came out quite bluntly, but Butters and I are close."
                show riku embarrassed with dissolve
                riku "W-Wow, you really are good with the ladies."
                butters "Good with 'em? I'm the one on-top more often than not, lemme show you!"
                show butters closedresshorny with dissolve:
                    xpos 450
                    ypos 10
                "The lecherously drunk Butters tries to crawl onto my lap."
                mc "Wahh? What are you doing, Butters?"
                butters "Ehehe, I'm just sitting on your lap [playername], I'm not gonna fuck you in the bar!"
                "She says that, but she's very subtly grinding against me. The mental fortitude required to avoid getting an erection is intense."
                show riku laughing with dissolve
                riku "Phew, you had me worried for a second there..."
                butters "As tempting as it maaay beeee... We can do that when we get home, right babe?"
                mc "Uhh, sure! But wouldn't it be more fun if Riku joined in?"
                show riku embarrassed with dissolve
                riku "Huh, what?"
                butters "Ohh, of course, you should play with us Rikki!"
                show riku shy with dissolve
                riku "Hmph... Sure, I'm in..."
                "Riku takes a long chug from her cider; finishing it off, before she offers an idea."
                riku "How about the three of us take this conversation upstairs? I think we're disturbing some of the patrons."
                mc "I think that's a great idea, come on Butters."
                show butters dresssad with dissolve
                butters "Wait, where are we going? Whaa..."
                scene bg black with dissolve
                show bg barupstairsnight with dissolve
                show rikub:
                    xpos 150
                    ypos 50
                show riku embarrassed:
                    xpos 150
                    ypos 50
                with dissolve
                riku "We can go wild here, o-oh, you're already taking off your clothes."
                mc "Come on Butters, behave yourself! Oh, wait, I guess taking off your clothes isn't actually naughty."
                show butters horny with dissolve
                butters "Being drunk is so wonderful! I can finally do and say anything I want!"
                riku "Woah! Butters, you have bat wings?"
                butters "Oh! I do! D-Do you like them?"
                riku "Yeah! They're so cool, I had no idea!"
                butters "Awwwhh youuu, they're not as awesome as your wings! C'mere!"
                stop music fadeout 3.0
                show bg barupstairsnight with vpunch
                hide rikub
                hide riku
                hide butters
                with moveoutbottom
                "The drunk Butters pushes Riku down, and the duo start making out with each other. Riku is too submissive, and probably horny, to resist."
                "To my surprise though, Riku gets the upperhand on Butters and straddles her."
                play music sex1 fadein 3.0
                show riku buttersthreesome1 with dissolve
                riku "Ehehe, my turn to be in charge for once."
                butters "Mmphh, wait... P-Riku... I-I've never done it with a girl before."
                "That's technically not true, but I won't say anything."
                riku "Is that so? Well... you're not doing it with just a girl tonight..."
                riku "You're up [playername], sate this slut's lust."
                mc "Impressive... I wasn't expecting you to act so dominant Riku."
                riku "Hehe, I picked up a few tricks from you and Moxie. You and her are such bad influences after all..."
                butters "Less talkies, more cummies! I really want that cock inside me... Ahhh..."
                riku "Need some oral help getting it up?"
                mc "I'm good, just keep teasing our plaything."
                "Riku shuts up the rambling Butters with a tongue-filled kiss as I position myself between Butters' legs."
                "I tap my cock against Butters' thick furry thighs as my erection gradually grows, some precum already dripping from the tip."
                "Butters quivers in anticipation as she gently spreads her legs wider, her needy and wet pussy revealing itself to me."
                "Meanwhile Riku moves between kissing Butters' lips, teasing her neck and nibbling her nipples, each action eliciting sweet moans from the drunken Butters."
                play sound cum
                show riku buttersthreesome2 with dissolve
                "Not willing to waste anymore time, I prod the tip of my cock against Butters' pussy before pushing deeper."
                butters "Aahhh, yessshh! I love your cock, [playername]!"
                "I can feel the heat emnating from her juicy cunt as I sink inside, Butters' legs wrapping around me to pull me in as deep as possible."
                "While I fuck, Riku teases around Butters' neck, it's evidently a sensitive erogenous zone for the girl; her body wriggles in delight at the mere touch."
                butters "Aahh, yeeesss! It feels so goooood! You two are being shooo nice to me..."
                riku "Mmphh, it's fun being in control for once, but I can't believe I let you encourage me into another threesome! You really are the best, and the worst, [playername]."
                mc "Beats masturbating alone in the evening, doesn't it?"
                riku "Hmphh, yeah your cock is 'okay', I guess, heh."
                butters "[playername]'s cock ish tha best!"
                play ambience sex fadein 3.0
                "Butters grind her hips back and forth against my shaft as she tries to fuck herself upon me, although her drunken movements are laughable at best."
                butters "Ahhh, ahhhh, yeaaahhh! It's even better when drunk, ehehehe!"
                riku "I never expected Butters to be the type that gets horny when she's drunk!"
                "Riku resumes teasing Butters with her tongue, whilst I properly serve Butters by pinning her down and humping her plump pussy."
                "Butters gasps and grins lecherously as I forcefully pound her, soon she's unable to hold back squeals and moans of joy."
                butters "Ohhh, yes, yes, yes! Give it to me! Ahhhaaaahhh!"
                riku "Yeahh, fuck her hard [playername]! Her reactions are so cute!"
                "Her sopping wet pussy lets me fuck as hard as I can, and with no care to drag this pleasure on, I can already feel my orgasm drawing near."
                play sound cum
                show riku buttersthreesome3 with cum
                play sound cum
                show riku buttersthreesome3 with cum
                "With a few last vicious, deep thrusts that cause the entire sofa to rock back and forth, we both orgasm together."
                play sound cum
                show riku buttersthreesome3 with cum
                play sound cum
                show riku buttersthreesome3 with cum
                stop ambience fadeout 3.0
                "The potent eruption of cum paints her insides all the way to her womb, so much so that it copiously leaks out and the eager Riku cleans up the point of our connection."
                "With our orgasms over, we slump over the sofa together."
                scene bg barupstairsnight with dissolve
                "Despite being neglected in the act, Riku seems satisfied, but not satisfied enough..."
                show riku closehorny with dissolve:
                    xpos 50
                    ypos 75
                riku "Alright, let's take fifteen minutes and go again, hehehe."
                show butters closehorny with dissolve:
                    xpos 400
                    ypos 10
                butters "Yeah, yeah! I want more!"
                stop music fadeout 3.0
                scene bg black with dissolve
                "We go back and forth for what feels like hours, these two girls have an insatiable appetite for sex."
                "Eventually all three of us end up cuddled in bed together."
                play ambience ambienceday
                show bg barupstairs with dissolve
                show butters neutral with dissolve:
                    xpos 650
                    ypos 10
                butters "Ohh, ohh, my head..."
                show rikub:
                    xpos 150
                    ypos 50
                show riku happy:
                    xpos 150
                    ypos 50
                with dissolve
                riku "[playername], get this mare some water!"
                "I give Butters a cold bottle of water from the fridge and she timidly sips on it."
                butters "Hey Riku... You gotta forget about these bat wings, and my tattoo, okay?"
                riku "Hm? Sure, I won't tell anyone."
                show butters happy with dissolve
                butters "Thank you so much, and for last night too, that was a lot of fun."
                riku "Heh, don't worry about it, I enjoyed last night too."
                play sound dressing
                show butters dresshappy with dissolve
                if livingwithbutters == 1:
                    butters "Phew... We best get home."
                    riku "You're always welcome back, see ya!"
                    scene bg black with dissolve
                    "Butters and I return to the cottage, she has a slow, lazy morning to recover."
                    jump afteraltmorning
                else:
                    butters "Phew... I best get home."
                    riku "You're always welcome back, see ya!"
                    scene bg black with dissolve
                    "The three of us go our separate ways as I return to Moxie's wagon."
                    jump altmorning
            else:
                $ buttersrikuthreesome = 1
                show butters dresshappy with dissolve:
                    xpos 550
                    ypos 10
                if livingwithbutters == 1:
                    "Butters decided to come with me to the bar tonight, so I'll keep her some company rather than chatting up another girl."
                    "As we order a drink and take a seat, Riku joins us during her shift."
                else:
                    "I spot Butters having a drink, as I sit down and say hello, a third person shows up!"
                show rikub:
                    xpos 150
                    ypos 50
                show riku happy:
                    xpos 150
                    ypos 50
                with d
                riku "Hey, it's always nice to see some friendly faces again!"
                butters "Hehe, you provide such a good customer service, I just had to come back!"
                show riku laughing with dissolve
                riku "Be sure to tell all your friends!"
                show butters dresslaughing with dissolve
                butters "Hehe, exactly how much do you want me to tell them?"
                mc "Wanna do the same thing as last time?"
                show riku neutral with dissolve
                riku "You picked a good day for it, my shift is going to end soon. Start with a few drinks and I'll be back in 15 minutes."
                stop music fadeout 3.0
                scene bg black with dissolve
                "One hour later..."
                show bg barupstairsnight
                show butters dresshorny:
                    xpos 550
                    ypos 10
                show rikub:
                    xpos 150
                    ypos 50
                show riku happy :
                    xpos 150
                    ypos 50
                with d
                play music challenge fadein 2.0
                show butters horny with dissolve
                butters "Heeheehee, I can't believe I'm drunk again! I'm not usually like this, I'm really shy, ahaha!"
                show riku embarrassed with dissolve
                riku "It's fine Butters, I know you drunk and sober."
                mc "A few drinks can bring the best out of anyone!"
                show riku laughing with dissolve
                riku "It certainly brought out something, just look how amazing her boobs are!"
                riku "It's a crime to hide those badonkas."
                butters "If you like them so much, why don't you come and get a closer look at them Prisie?"
                riku "I might just take you up on that offer!"
                butters "It wasn't an offer!"
                stop music fadeout 3.0
                show bg barupstairsnight with vpunch
                hide riku
                hide rikub
                hide butters
                with moveoutbottom
                riku "Waaahh!"
                "The drunk Butters pushes Riku down, and the duo start making out with each other. Riku is too submissive, and probably horny, to resist."
                "Like before, Riku gets the upperhand on Butters and straddles her."
                play music sex1 fadein 3.0
                show riku buttersthreesome1 with dissolve
                riku "Ehehe, you're far too drunk to hold me down."
                butters "Ish not fair! We've had the same to drink!"
                riku "Is that so? Well, you need to learn how to handle your drink as well as you handle your dick."
                butters "Ohh dick! Yes, lets have another threesome!"
                riku "You hear that [playername]?"
                mc "Not quite, can you speak up Butters?"
                butters "Pweease! I want your cock, please fuck me [playername]!"
                "Riku shuts up the rambling Butters with a tongue-filled kiss as I position myself between Butters' legs."
                "I tap my cock against Butters' thick furry thighs as my erection gradually grows, some precum already dripping from the tip."
                "Butters quivers in anticipation as she gently spreads her legs wider, her needy and wet pussy revealing itself to me."
                "Meanwhile Riku moves between kissing Butters' lips, teasing her neck and nibbling her nipples, each action eliciting sweet moans from the drunken Butters."
                play sound cum
                show riku buttersthreesome2 with dissolve
                "Not willing to waste anymore time, I prod the tip of my cock against Butters' pussy before pushing deeper."
                butters "Aahhh, yessshh! I love your cock [playername]!"
                "I can feel the heat emanating from her juicy cunt as I sink inside, Butters' legs wrapping around me to pull me in as deep as possible."
                "While I fuck, Riku teases around Butters' neck, it's evidently a sensitive erogenous zone for the girl; her body wriggles in delight at the mere touch."
                butters "Aahh, yeeesss! It feels so goooood! You two are being shooo nice to me..."
                riku "Mmphh, you're just so fun to play with Butters!"
                butters "Riku's tongue and [playername]'s cock are tha best!"
                play ambience sex fadein 3.0
                "Butters grind her hips back and forth against my shaft as she tries to fuck herself upon me, although her drunken movements are laughable at best."
                butters "Ahhh, ahhhh, yeaaahhh! It's even better when drunk, ehehehe!"
                riku "I can't believe how horny you get when you're drunk, even I'm not this bad!"
                "Riku resumes teasing Butters with her tongue, whilst I properly serve Butters by pinning her down and humping her plump pussy."
                "Butters gasps and grins lecherously as I forcefully pound her, soon she's unable to hold back squeals and moans of joy."
                butters "Ohhh, yes, yes, yes! Give it to me! Ahhhaaaahhh!"
                riku "Yeahh, fuck her hard [playername]! Her reactions are so cute!"
                "Her sopping wet pussy lets me fuck as hard as I can, and with no care to drag this pleasure on, I can already feel my orgasm drawing near."
                play sound cum
                show riku buttersthreesome3 with cum
                play sound cum
                show riku buttersthreesome3 with cum
                "With a few last vicious, deep, thrusts that cause the entire sofa to rock back and forth, we both orgasm together."
                play sound cum
                show riku buttersthreesome3 with cum
                play sound cum
                show riku buttersthreesome3 with cum
                stop ambience fadeout 3.0
                "The potent eruption of cum paints her insides all the way to her womb, so much so that it copiously leaks out and the eager Riku cleans up the point of our connection."
                "With our orgasms over, we slump over the sofa together."
                scene bg barupstairsnight with vpunch
                "Despite being neglected in the act, Riku seems satisfied, but not satisfied enough..."
                show riku closehorny with dissolve:
                    xpos 50
                    ypos 75
                riku "Alright, let's take fifteen minutes and go again, hehehe."
                show butters closehorny with dissolve:
                    xpos 400
                    ypos 0
                butters "Yeah, yeah! I want more!"
                stop music fadeout 3.0
                scene bg black with dissolve
                "We go back and forth for what feels like hours, these two girls have an insatiable appetite for sex."
                "Eventually all three of us end up cuddled in bed together."
                play ambience ambienceday
                show bg barupstairs with dissolve
                show butters neutral with dissolve:
                    xpos 650
                    ypos 10
                butters "Having water before going to sleep was a great idea Riku, my head doesn't hurt at all!"
                show rikub:
                    xpos 150
                    ypos 75
                show riku happy:
                    xpos 150
                    ypos 75
                with d
                riku "Yeahhh, you gotta stay hydrated after a night of drinking."
                show butters happy with dissolve
                butters "Thank you so much, and for last night too, that was a lot of fun."
                riku "Heh, don't worry about it, I enjoyed last night too."
                play sound dressing
                show butters dresshappy with dissolve
                if livingwithbutters == 1:
                    butters "Phew... We best get home."
                    riku "You're always welcome back, see ya!"
                    scene bg black with dissolve
                    "Butters and I return to the cottage, she has a slow, lazy morning to recover."
                    jump afteraltmorning
                else:
                    butters "Phew... I best get home."
                    riku "You're always welcome back, see ya!"
                    scene bg black with dissolve
                    "The three of us go our separate ways as I return to Moxie's wagon."
                    jump altmorning
        "Leave":
            stop music fadeout 1.0
            if fr == 1:
                jump finalworldmapnight
            jump worldmapnight
    if fr == 1:
        jump finalworldmapnight
    jump worldmapnight

    label doubledoggo:
        stop ambience fadeout 40.0
        "You found a secret scene! Requirements met: Sleep around too much..."

        "Ah, it’s one of my favourite canine gals."
        show rosa char with d
        doggirl "Hey [playername]!"
        mc "Hey Rosa. how’s it-?"
        "Uh oh."
        show hilda char:
            xpos 700
            ypos 0
        wolfgirl "Oh, [playername]. I saw you in the corner of my eye and thought I’d say hello. Are you with a friend?"
        doggirl "Hehe, you could say that. I think? But I’m more of a…"
        mc "Friend, yes. You’re both my friends."
        "This situation has become complicated."
        wolfgirl "Well, I could use the company. Do you two want drinks?"
        "Or… maybe not?"
        doggirl "Hell yeah! Anyone offering to buy me a drink is welcome to be a friend. Come sit next to me."
        wolfgirl "Perfect. Let’s set a tab up. Me, then you, then [playername]."
        stop music fadeout 3.0
        scene bg black with dissolve
        "…"
        show doubleb doggo
        show double doggo1
        with d
        "How do I keep finding myself in these situations?"
        "I swear, it’s the girls that come onto me every time."
        "Hilda threw a few compliments Rosa’s way, and for some reason the dog girl blurted out that she swings both ways."
        "For a moment, I was almost worried I was going to be the third wheel. But they’re both desperately eager for my cock right now."
        play music sex1 fadein 3.0
        wolfgirl "So, sexy. Who’s the lucky lady to get it first?"
        mc "I couldn’t dishonour either of you lovely girls by choosing. So how about a game of rock, paper, scissors?"
        doggirl "Heh, the loser has to slurp the juices off his cock."
        wolfgirl "You’re on, little girl."
        "Rock."
        "Paper."
        "Scissors!"
        wolfgirl "Ah?!"
        doggirl "No way?!"
        mc "A draw!"
        "Rock."
        "Paper."
        "Scissors!"
        doggirl "Huh?!"
        wolfgirl "Unbelievable!"
        mc "Another draw!"
        doggirl "Sheeeeesh…"
        doggirl "Alriiight, fuck it. Take Hilda first. I for one am actually pretty aroused at the idea of slurping her juices off your cock."
        wolfgirl "Heh, that was some fine projection when you declared the loser’s punishment."
        doggirl "I wouldn’t have picked a punishment that I wouldn’t enjoy, hehehe."
        wolfgirl "You sneaky bitch."
        mc "Alright, I’m ready."
        "Erection in hand, I bring it between the girls, their eyes glued to it."
        wolfgirl "C’mere, [playername], my pussy is soaking."
        "As I move into position, one of my hands is drawn to her fluffy breast, my fingers digging into the softness."
        "My other hand wraps itself to her mons, pressing tenderly against her as I position my cock beneath her rear and prepare to push inside."
        play sound cum
        show double doggo2 with d
        "Holding her steady, I push forwards. The tip of my cock slips through her wet folds and penetrates her tightness."
        wolfgirl "Ahhh… So thick! Ahhh…"
        "Hilda arches her back into me slightly as I fill her up entirely. A hot wetness slowly coats my cock, dripping freely from the wolf’s pussy."
        play ambience sex fadein 2.0
        show double doggo3 with d
        doggirl "By Aurora, I wish that was me."
        "I continue to caress Hilda’s supple breasts while I gently rock my hips back and forth. She moans with approval as I tweak her stiff nipples."
        "Rosa practically drools as she watches closely. She can’t help but play with Hilda’s other breast."
        "As the passion steadily increases, the two girls occasionally experiment with tongue kissing, and Rosa particularly enjoys suckling on Hilda’s breasts."
        show double doggo2 with d
        "From behind, I can’t see everything Rosa does, but judging by the occasional touch against my balls, she’s rubbing Hilda’s clitoris too."
        "The double assault of pleasure causes the wolf girl to slowly lose composure, her breathing growing heavy and moans becoming more frequent."
        "I don’t speed up, but she does, with her ass bouncing up and down my cock greedily. Her back arching into me even further, as if her entire body is just melting into me."
        "The frantic movements of her ass mirror the rapid wagging of her tail. Her slick pussy clenching and contracting as she reaches the heights of pleasure."
        wolfgirl "Cum in me, cum in me!"
        "Hilda’s entire body quivers as she’s possessed by a powerful orgasm. The spasms of pleasure make her pussy feel even tighter, and she manages to keep the vigorous rhythm of her ass bouncing against me."
        "I squeeze her hips and pound into her fervently, my entire body growing tense as my orgasm stirs."
        play sound cum
        show double doggo4 with cum
        play sound cum
        show double doggo4 with cum
        "Flipped like a switch, my vision swims with white and all sensations are replaced with euphoria. My cock erupts thick loads of semen into her awaiting cunt, plastering her warm inner walls with white."
        play sound cum
        show double doggo4 with cum
        play sound cum
        show double doggo4 with cum
        wolfgirl "Ahh, ahh, yes! Yes!"
        show double doggo5 with d
        stop ambience fadeout 2.0
        "The wolf girl’s entire body trembles as I pull out with a pop, splattering her ass with a few stray drops of cum."
        scene bg rosabedroom with d
        show rosa bj with d
        "Almost immediately, Rosa catches me off guard and slips my cock into her muzzle. Her tongue coils around my shaft and slurps all of the cum and sexual fluids off."
        "It’s initially a little sensitive, but I actually find myself getting hard again under the dog’s skillful tongue."
        scene doubleb doggo
        show double doggo5
        with d
        doggirl "Mmphh, mmm… *Lick, lick* Haahh… My turn?"
        mc "Well, since you asked kindly."
        wolfgirl "My turn to tease you, mehehe."
        "The two girls resume their initial presenting positions. Their asses presented to me, and the bodies presented to each other, allowing all three of us easy access to tease and play with another."
        "As I approach the dog girl’s bubble butt, her eyes follow every motion in anticipation. If her tail’s non-stop wagging is any indication of her excitement, you’d think this was the most fun she’d ever had in her life."
        play sound cum
        show double doggo6 with d
        "Dick in hand, I push the tip of my erection against her soft folds and they easily part, inviting me inside."
        "The dog girl coos and shivers at the sensation of being filled up. Her insides occasionally twitching as I push to the hilt."
        doggirl "Ohhh yesss… I looove this dick."
        wolfgirl "Wanna kidnap him?"
        doggirl "Oh can we? Can we keep him as a pet? Hehe."
        mc "I think you two would much rather be owned by me, isn’t that right?"
        doggirl "Is that an offer? Hehe."
        play sound spank
        show double doggo7 with d
        play ambience sex fadein 2.0
        "Rosa slaps her ass, giving me the cue to fuck. Hilda takes it as her own cue to start groping and kissing Rosa, their lips entwining as I begin my thrusting."
        "My current partner’s pussy is much tighter, due to her being a smaller girl, but I swear she’s even wetter than Hilda was."
        "Her pussy is practically oozing with excessive lubricants. It makes it so easy to pound her ass."
        "And having just orgasmed earlier, I’m able to move much faster and aggressively without the fear of cumming too soon."
        "The hungry pussy adores it as it clenches around my shaft, especially at the hilt of each thrust. Her thighs do these cute twitches in response to the pleasure too."
        doggirl "Mmphh, mmm… If you keep g-going this fast… I-I can’t even concentrate on kissing."
        "I gyrate my hips not only to keep the thrusts hard and fast, but also to grind against some of the most sensitive areas deep inside of her."
        "Moans spill from her mouth with each thrust, as she gets closer and closer to orgasm."
        doggirl "Oohh Aurora, f---fuuuuck! Ahh, ahhh…"
        wolfgirl "Hehe, she’s coming so hard. It’s so cute!"
        "Her cunt squeezes tightly, almost sucking me in with each push of my hips. Her pussy squirting ever so slightly, dripping onto my thighs."
        "I keep moving faster, while Hilda teases the climaxing dog girl in any way she can. Hilda tweaks her nipples, rubs her clit, kisses her neck. Rosa’s mind is being attacked from almost every angle."
        "It doesn’t take me too long to build myself up to a second orgasm, my cock finally tightening as the familiar feeling rises in my nether."
        play sound cum
        show double doggo8 with cum
        play sound cum
        show double doggo8 with cum
        "The first few loads of cum shoot into Rosa’s pussy, and she definitely acknowledges it as she throws her head back and moans out a hearty ‘Yeesssss!’"
        play sound cum
        show double doggo8 with cum
        play sound cum
        show double doggo8 with cum
        "A second load shortly follows, pumping straight into the dog girl’s womb."
        "The two of us continue rutting until our orgasms slowly fizzle, and we essentially fall forward into a cuddle"
        stop ambience fadeout 2.0
        stop music fadeout 10.0
        scene bg rosabedroom with d
        "A cuddle which Hilda gladly takes advantage of, leaving me in the middle of them on Hilda’s bed."
        "Ahhh… Two extremely soft lupine girls cuddling me from either side."
        wolfgirl "I’ve done a lot of crazy things in my life, but this is definitely the wildest."
        doggirl "Hehe, that was actually my first threesome too."
        mc "What am I going to do with you two, huh?"
        wolfgirl "Mmmpmhh, I’m sleepy…"
        doggirl "Let’s snuggglleeee…"
        scene bg black with d
        if crystalballactivated == 1:
            jump cbmenu
        $ secretsunlocked += 1
        "The three of us snuggle together, soon falling into a deep sleep."
        "Early in the morning, Hilda and I return to our homes."
        jump altmorning
