label deepforest:
    if forestmonies == 55:
        menu:
            "Go deep into the forest?"
            "Yeah!":
                jump deepforestvisit
            "No way!":
                if worldmap == 2:
                    jump worldmapnight
                else:
                    jump finalworldmapnight
    else:
        "I don't really have a reason to explore deep into the woods, I might even get lost without proper preparation."
        "It'd be fun in a mysterious and creepy way though... Maybe if I had some more equipment I could go for a small hike around the area to fill an evening."
        if worldmap == 2:
            jump worldmapnight
        else:
            jump finalworldmapnight
label deepforestvisit:
    if zoe == 0:
        $ zoe += 1
        jump zoe1
    elif zoe == 1:
        $ zoe += 1
        jump zoe2
    elif zoe == 2:
        jump zoe2

label zoe1:
    "I’ve never stepped far from Arcadia. Even though there’s an entire brand-new world out there."
    scene bg forestnight with d
    "So, here we go, some deep woods exploration for fun. While I’m out here, I could collect some berries for Butters' potions."
    "But really, I’m not interested in work."
    "I’ve been working almost every day for longer than I can imagine. Sometimes it’s nice to just get some fresh air."
    show bg farm6night1 with d
    "Some peace and quiet under the starlit sky will certainly help relieve some stress."
    if melodyeveningvisit1 == 1:
        "It almost reminds me of my evening walk with Melody."
    show bg forestnight with d
    "I did decide to bring my leather armour, it certainly provides some comfort."
    "Even though I’ve gotten used to walking around on my bare feet, the leather shoes are especially nice in the dark."
    "And a scimitar on my back, just in case, but I’ve yet to find a scenario where I’ve needed to use this. I suppose that's the point."
    if melodyeveningvisit1 == 1:
        "Bringing a weapon is a bit more extreme than my walk with Melody, but it feels nice to have a backup plan."
    else:
        "I know this is just going to be a leisurely walk, but it feels nice to have a backup plan."
    "There’s the usual and fairly clear path towards Butters' cottage, then a clearing. I think I’ll do a horse shoe path that’ll lead me back to clearing, or worst-case scenario Honey’s farm."
    "Between the full moon, and the lights of Arcadia city, it’s almost impossible to get lost between these two landmarks."
    "I stretch and set off. The sound of the chirping crickets being my only accompaniment as I step through the deeper woods."
    play sound movement
    show bg forestnight2 with d
    "There’s the occasional shuffling bush, but that’s easily written off as a woodland critter, of which there are many in this area."
    "In the day, the woods are so peaceful and harmonic. In the dark, it’s seemingly hostile, yet exciting."
    "Rather quickly along my walk, I discover my first curiosity within the woods."
    show bg foresthouse2 with d
    "There’s another clearing, and another cottage that’s not too different from Butters’. It’d make sense that there’d be a few of these built around. Even these deep woods feel tamed with a quaint hospitality."
    "It seems that whoever lives in this one isn't home, so I bypass the cottage and continue onwards."
    show bg farm2night with d
    "When I eventually stumble upon a second clearing with a hill that pokes through the trees, I take the opportunity to climb to the top."
    "The hill is impressive, from here I can just peer over most of the trees, and can even see the two cottages poke through."
    "And while Arcadia village is obscured from this angle, the dizzyingly tall castle continues to dwarf me."
    mc "Ahh… This is nice."
    show bg farm6night1 with d
    "I lay down on the grass and enjoy the soft breeze as I gaze into the stars…"
    "*Rustle, rustle*…"
    "*Whisper, whisper*…"
    show bg farm2night with d
    show lamp1
    with d
    pause 1.0
    show lamp2
    hide lamp1
    with d
    pause 0.5
    "My ears prick slightly, at the sounds of some distant movement. Seems like I’m not the only person that decided to have a small peruse around the woods. I spot the orange light of a lantern to the east of my hill perch."
    show lamp3
    hide lamp2
    with d
    pause 1.0
    scene bg farm2night
    with d
    pause 0.5
    "I half-heartedly keep an eye on the light as it continues ahead ignorant to me, but it does pique my curiosity when it spontaneously turns off, and the once chatty whisperings melt into a silence."
    "Hmm…"
    "I should probably head back."
    show pink with d
    "I crick my neck and stand up, and as I do, a certain sickly-sweet scent hits my nose."
    "*Sniff, sniff*"
    "What a strange and indescribable scent…"
    "I can almost directly pinpoint the origin too, the same location the lamp went out."
    "Somewhat allured, I follow the tantalizing scent with the justification that anyone carrying a lamp is probably just a friendly anthropomorph."
    "But I’m not as naïve as I once was, I’ve worked with Butters a few times and learnt a lot in our time together. Therefore, I take a cautious approach as I crouch behind some bushes and investigate the smell."
    "This heavy scent, if my experiences with Butters are correct, it’s purposely designed to attract males. But… Why would that scent be relevant to the quiet woods at a time like this?"
    "And that’s when she comes into view."
    show zoeb doggystyle
    show zoe doggystyle1
    with d
    "It’s… a zebra? A zebra anthropomorph!"
    "She isn’t even trying to hide herself, and the contrasting stripes of white on the zebra girl shine in the moonlight."
    "I, however, am yet to reveal myself as I crouch behind the bushes."
    "It’s hard to really assume a context for this situation, but I have to assume that she’s waiting for someone, or something…"
    "Especially given that strange scent that attracts males… It’s so effective, that it managed to attract me when I was planning on completely ignoring this. I feel like a bit of a monke brain right now."
    unknown "The time is nigh, now don’t be shy…"
    "Is... is she talking to me?"
    unknown "That’s right big boy, no need for tours, I’m all yours..."
    "She isn’t looking my way, so by all means, she isn’t talking to me…"
    "But… Who, then?"
    unknown "Don’t you want to find a nice place to cum in? I’ll even let you put a thumb in..."
    "Alright, this is getting weird."
    "Just gonna, slowly leave…"
    play sound movement
    "*Rustle, rustle*… !"
    scene bg forestnight with d
    "Something, above me?"
    "Falling out from the trees, none other than Butters nimbly drops before me."
    show butters robeneutral with d
    mc "B-B…! *Whispering* Butters?"
    butters "Phew, it’s just you! Heh, I thought maybe I’d been spotted."
    mc "What’s going on?"
    show butters robehappy with d
    butters "Ah, it must look pretty strange, right?"
    mc "No kidding."
    show butters robeneutral with d
    butters "Well, Zoe over there... she’s hoping to attract a werewolf for some 'fun'. I’m here to moderate, and I have a potion to revert both the lycanthropy of the werewolf, and herself."
    mc "Ah, you’re trying to lure in a werewolf with sex, and then cure them."
    show butters robeangry with d
    butters "Yup. I told Zoe I wouldn’t help her sleep with Mr. Wolfies anymore unless we helped them."
    mc "That’s what this strange bonerific scent is for, then?"
    show butters robeneutral with d
    butters "Yeah, is that what brought you here? Hehe, sorry for tricking you. Usually anthropomorphs can’t smell it unless they’re very close, but a werewolf’s sharp nose can smell it from up to ten kilometres away."
    mc "Ah, it’s fine. I was relaxing on a nearby hill when I saw the glow of your lantern."
    mc "I should have realized it was you, after all, anyone else would probably just use a torch."
    scene zoeb doggystyle
    show zoe doggystyle1
    with d
    zo "Come ooonn, big boyyy… There’s no need to be coy! Take me like the beast you are!"
    mc "Hmm… How long does this usually take?"
    scene bg forestnight
    show butters robeneutral
    with d
    butters "Well, we were going to wait for at least an hour… But…"
    mc "But?"
    show butters robesad with d
    butters "I keep telling her that the full moon already passed during the day, and it’s currently a waning gibbous…"
    mc "The full moon started and stopped during the day?"
    show butters robeneutral with d
    butters "Yeah, it’s a rookie mistake to just assume the moon operates only by nightfall."
    butters "And technically a full moon only lasts within an instant, which causes the werewolf transformation, and then the transformation only lasts a few hours…"
    butters "But she insists, and I can’t really blame her for trying…"
    show butters robehappy with d
    butters "…And… I’m getting paid."
    "She winks and leans back on a tree."
    mc "Your friend sounds stubborn."
    show butters robeneutral with d
    butters "Perhaps stubborn, but also simply hornier than her eyes can see."
    mc "I guess I’ll keep you company."
    scene zoeb doggystyle
    show zoe doggystyle2
    with d
    zo "Uuughh… Butters you were right, I don't think anyone's coming…"
    zo "It’s {i}always{/i} night time in fiction… Just my luck…"
    scene bg forestnight
    show butters robehappy
    with d
    butters "What do you think about Zoe?"
    menu:
        "She seems a little crazy.":
            butters "Anyone that chooses to live in the forest is probably a little crazy."
            butters "And I know the expression is to not stick your dick in crazy, but I heard you should always try it at least once."
            mc "Hmm... You raise good points."
        "She has a really nice ass":
            butters "What do you think would happen if you walked up and told her that right now?"
            mc "Is that a challenge?"
        "I always wanted to bang a Zebra, let's do this!":
            pass
    show butters robelaughing with d
    butters "Hehe, yeah, I think you’re more than capable enough to satisfy her."
    mc "What would she think?"
    show butters robehappy with d
    butters "Hehe, try your luck! I just want to see what her reaction would be to a human!"
    mc "Heh, that does sound amusing. Alright, I’ll do it."
    show butters robelaughing with d
    butters "Okies, if you’re successful, I’ll be up in this tree masturbating if you need me."
    "I don’t know if it’s the strange tantalising aroma making me do this, or the hot zebra ass, but I find myself going along with this strange situation a little easier than anticipated."
    "Dropping my scimitar and leather armour beside Butters and her chosen tree, I step into the opening and catch Zoe’s attention."
    play music sex1 fadein 3.0
    scene zoeb doggystyle
    show zoe doggystyle1
    with d
    zo "Ooohh, you, you’re, you…"
    zo "A male! A male… Perhaps you are looking for someone to nail?"
    mc "A rhyming Zebra?"
    zo "Indeed young man, do you like what you see? I shall offer it to thee."
    "Wiggle wiggle, her butt goes. I choose to play a little hard to get though, crossing my arms and raising an eyebrow."
    "She begins flaunting her pussy like a target, her tail swishing back and forth, while the witches hat she placed on her butt nearly falls off."
    mc "You want it pretty badly, don’t you?"
    zo "Are you not convinced? There’s no trick, I just want dick."
    menu:
        "Alright, get ready for a poundin'":
            pass
        "Once you go Zebra, you'll never go back.":
            pass
        "You must think I stick my dick in any random ass I stumble upon in the woods, don'cha?":
            zo "Only the best of ass here, I am a lady of class."
            mc "A lady of class? Sorry, but if this is 'classy' in this world I'm more out of touch than I realized."
            zo "There is no fear, only a world of pleasure here."
            "I peer behind me for a second while thinking. I bet Butters sent me in here on purpose so she wouldn't have to wait an hour, that's uncharacteristically crafty of her."
            mc "Alright..."
        "And what makes you think I want to give you any? I don't even know who you are.":
            zo "There is no fear, only a world of pleasure here."
            mc "Hmm..."
            "I peer behind me for a second while thinking. I bet Butters sent me in here on purpose so she wouldn't have to wait an hour, that's uncharacteristically crafty of her."
            mc "Alright..."
    mc "But you do have some explaining to do afterwards."
    zo "Absolutely, I shall explain, after I’ve been reined."
    "I could tease her for a few more rhymes, especially since she sometimes takes pause to think of suitable words. Although the ‘rein’ rhyme was pretty genius considering she’s equine. She has probably used that one before."
    mc "If you want it so badly, then I won’t disappoint."
    "As I get into position before her presented rear, she exudes a high level of excitement, her tail swishes so fervently it keeps brushing against me."
    "The sweet flowery aroma that attracted me here combined with the smell of sex heightens my need to pound her pussy, almost to a beguiling degree."
    play sound cum
    show zoe doggystylev1 with d
    "Her drippy pussy is clearly wet and ready, so I skip teasing and begin the session by aligning the tip of my cock against her pussy and pushing inside."
    "Immediately I sink into the pleasant warmth of her depths, her lips parting bit by bit as it easily accepts me to the hilt in a single smooth motion."
    zo "Ahhhh, ahh… I’m so appreciative that you were present, because that feels extremely pleasant."
    play ambience sex fadein 3.0
    "Her hips twitch as I pull back and sink back in, beginning to rut her at a pleasureful pace for the both of us."
    "Zoe was so wet from the start, she was clearly anticipating this and prepared for it. So it’s not too surprising that she accepted me even if I perhaps wasn’t quite what she wanted."
    "The lustful wetness does allow me to pound her as fast as I want though, choosing to alternate between fast thrusting and then slowing myself down as to pace myself."
    "Each movement causes friction against her swollen clit, and deep sensitive spots within her pussy, filling the zebra girl with bliss."
    show zoe doggystylev2 with d
    zo "Aaahhh, haaahhh, that’s it, I want you to fill me with your seed."
    "Hm, she didn’t rhyme that time. I clearly have my priorities wrong if I’m thinking about that right now, but this zebra girl is an enigma to me on so many levels."
    zo "Aahhahah, yesss... That’s good, keep going at that speed!"
    "Oh, there’s the rhyme! I thrust into my lover at the requested pace, rocking her back and forth against the grass while her toes curl and thighs quiver."
    "Doesn’t seem like it’ll take long for her to reach an orgasm, and indeed she does achieve one far before my own, as the mare squeals happily."
    "Her moans grow in lustful intensity, that coupled with the wet schlicking of her pussy, it's pretty much the only thing I can hear as we rut in the dark woods."
    "After her first orgasm, almost impatiently, I feel her own hips begin to rise and fall on my cock. Matching my own pace with some immediacy, and then outmatching it as she speeds up."
    "Her hip movements make her sexual experience immediately clear; she’s done toying around with me, and now she’s going to make me cum."
    "I grab her hips and commit to the accelerating pace, adding a third sound of our bodies slapping together to the mix."
    zo "Ahh, such a sly dog, ahh ahhhh… You’re certainly not a shy lover."
    "My cock begins to twitch and get tighter as my impending orgasm draws closer and closer."
    zo "Now, cum in me, I want it all…"
    "At a certain point my orgasm is all but confirmed, but it still takes a few seconds to escape. I use that time to push my body as far as it’ll go, fucking as hard as I can, to push to the heights of euphoria."
    play sound cum
    show zoe doggystylev3 with cum
    play sound cum
    show zoe doggystylev3 with cum
    "And then in one moment of intense bliss, my cock releases its load deep into the waiting mare."
    play sound cum
    show zoe doggystylev3 with cum
    play sound cum
    show zoe doggystylev3 with cum
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    zo "Ahh, yess, that’s it… Fill up my womb, until there’s simply no room!"
    show zoe doggystylecum with d
    "With one final load of cum, I finally empty my balls into the zebra, and she slumps onto the grass, panting."
    "I follow her example, lying beside her voluptuous breasts."
    "I peek around the tree tops while I’m laid down, but it’s so dark that I can’t make out Butters at all."
    scene bg forestnight
    show zoeb
    show zoe satisfied
    with d
    play ambience ambiencenight fadein 3.0
    "Eventually Zoe stands up and brushes off some stray strands of grass from her fur coat."
    zo "Phew… I was worried no one would come after all. It was certainly a close-call."
    "Right, I already know why she’s here, but she doesn’t know why I’m here. This is a good chance to ask her some questions."
    mc "That was fun, I still have questions though. Care to humour me?"
    show zoe happy with d
    zo "Yes, since you did such an incredible task, I’ll answer anything you ask. My name is Zoe, and you are?"
    mc "Call me [playername], I live nearby in Arcadia. You caught me during an evening adventure."
    show zoe satisfied with d
    zo "Ahh, I see, it's my pleasure, [playername]. Perhaps you saw my humble cottage, I often leave it to indulge in some frottage."
    "Ahh, so she's the occupant of that cottage? I wonder why I've never met her before if she's friends with Butters."
    "Time to pursue this line of questioning further."
    $ zwud = 0
    $ zwit = 0
    $ zbut = 0
    label zoetalkmenu:
        show zoe happy with d
    menu:
        "What were you doing out here?" if zwud == 0:
            $ zwud = 1
            zo "Ahh, mhehe… I was looking for a good time before bedtime, got it?"
            mc "Looking for a good time, in the middle of the woods, with some strange man attracting scent?"
            show zoe horny with d
            zo "It worked, didn’t it? My methods are perhaps unusual, but it gets the job done. This little scent attracts any hun, it’s the perfect fuel."
            mc "True enough, but I have to assume you didn’t get what you wanted."
            show zoe laughing with d
            zo "Perhaps not, but I found you more than enough fun to play around, though I certainly wasn’t expecting anyone from the town."
            zo "In truth, I was hunting for a very specific type of chap. But it would seem I mistimed my little trap."
            mc "Hmph… I feel pretty silly for getting caught up in this."
            show zoe satisfied with d
            zo "Was my pussy not satisfying enough for you? It certainly wringed out enough dew, mhehe."
            mc "I just feel like I ought to stop sleeping with every single thing I see. It’s beginning to get out of hand."
            show zoe neutral with d
            zo "Oh my… Part of the problem, am I?"
            jump zoetalkmenu
        "Are you a Witch?" if zwit == 0:
            $ zwit = 1
            show zoe laughing with d
            zo "A Witch is certainly what some fairy tales could refer to an individual such as myself. However, under the veil, I know no magic."
            show zoe happy with d
            zo "All I know is the mysterious art of alchemy."
            mc "Should you really be telling me that so leisurely? I thought alchemy was a secret."
            show zoe horny with d
            zo "A secret? No. A societal ignorance? Perhaps."
            zo "Most of my care-free customers simply misattribute my wares as not magical, despite the reality."
            zo "Although, that’s because I keep my most magical brews to myself. Some of them are too dangerous to leave the shelf."
            mc "Makes sense that you’d only sell basic wares, then."
            show zoe happy with d
            zo "There are two forest ‘witches’ that you ought to be wary of."
            zo "Mhehe, I kid, we’re very friendly actually. If you visit me again, I may even offer you some more love."
            jump zoetalkmenu
        "Do you know someone called Butters?" if zbut == 0:
            $ zbut = 1
            show zoe neutral with d
            zo "I do indeed, Butters was my alchemical friend. She came to Arcadia initially to work with me in alchemy twenty years ago. Together we can make an impressive blend."
            mc "Hm… That’s longer than I’ve been alive. You don’t mind if I ask, do you?"
            show zoe laughing with d
            zo "My age? I believe someone of your generation may refer to me as a ‘MILF’. I can’t think of a single word that rhymes with MILF, though."
            mc "That’s all I need to know. Hell yeah."
            show zoe neutral with d
            zo "And so, you know of Butters too?"
            mc "Indeed I do, I’m a close friend of hers, actually. I’m surprised you and I haven’t met."
            show zoe angry with d
            zo "How curious. She and I haven’t seen each other much lately, I had accidentally made her furious, and we fell apart."
            mc "Huh? What did you do?"
            show zoe neutral with d
            zo "Mmm, something about werewolves… I needn't bore you with detail."
            mc "Right… I think I get it."
            "I wonder if she gets annoyed if you interrupt her before she finishes her rhyme."
            jump zoetalkmenu
        "(Conclude)":
            pass
    show zoe satisfied with d
    zo "Okay, just as soon as you came out of the blue, now it’s time to shoo."
    mc "You’re telling me to leave?"
    show zoe happy with d
    zo "Would you rather stick around? I have beauty sleep to get. Maybe visit me again at my cottage someday, and we can dick around."
    scene bg forestnight
    show zoeb:
        xpos 150
        ypos 30
    show zoe neutral:
        xpos 150
        ypos 30
    show butters robehappy:
        xpos 550
        ypos 30
    with d
    butters "That’ll be fine, Zoe. I’ll be taking him."
    show zoe angry with d
    zo "Ahh, Butters, you were correct, as usual…"
    show butters robesad with d
    butters "I told you, you were being delusional."
    show zoe neutral with d
    zo "Was this man part of your plan?"
    show butters robeangry with d
    butters "Plan? What are you trying to say? I took part in no scam."
    mc "Oh come on, you can’t both be rhyming with each other."
    show butters robeneutral with d
    butters "Hehe, sorry! I just like playing along sometimes."
    mc "Alright, but why do you do it, Zoe?"
    show zoe laughing with d
    zo "What’s wrong with it, son? Don’t you like to have fun?"
    mc "Bruh… If it requires rhyming every word, I don’t want none."
    show zoe horny with d
    zo "That’s a shame… I loved making you cum."
    show butters robehappy with d
    butters "Alright everyone, it’s getting late. Let's make like a tree and split."
    mc "What a strange walk this turned out to be."
    scene bg forestnight
    show butters robeneutral
    with d
    "Zoe takes her leave, returning in the direction of the other cottage, while Butters and I return to hers."
    scene bg buttershousenight with d
    show butters robeneutral with d
    butters "Ah sheesh… I suppose that was a pretty fun end to the night. Everything is better when you’re involved."
    mc "Is that your old work partner, then? You know, before you and I started to work together a lot."
    mc "I sensed a little bit of tension between you two."
    play sound movement
    show butters sad with d
    "Butters gets changed as she replies."
    butters "Indeed, we worked together for a long time. Although there has been some minor turbulence within our more recent relations. We just can’t seem to agree on anything anymore."
    butters "It’s like she always has something to prove compared to me, an inferiority complex which she self imposes. This leads to her trying to show off, for validation or ego, I couldn't say."
    butters "But the insecurity it brings just leaves her stubborn and standoffish."
    play sound movement
    show butters dressangry with d
    butters "Oh, and that rhyming thing? She just does it for attention. Everyone thinks it’s a funny quirk, but I dunno… To her it’s just another way to try and show off."
    menu:
        "You sound pretty bitter, there must have been something big that made you fall out.":
            show butters dresssad with d
            butters "Well… The last straw for me was the werewolves incident."
            butters "They’re not actually native to this area, she purposely infected someone for her sick fetish!"
        "She doesn’t seem so bad to me.":
            show butters dresssad with d
            butters "Well… Maybe I’m being unfair because I’m currently seeing every aspect of her from a negative light."
            butters "I’ve had a lot of time to dwell on those negatives too, especially because of the recent incident."
            mc "Incident?"
            show butters dressangry with d
            butters "She purposely infected someone with lycanthropy for her sick fetish"
        "I agree, she was so busy trying to rhyme her sentences together that she barely managed to say anything of substance.":
            show butters dresssad with d
            butters "Heh, you meanie… She’s still a really good alchemist, but she’s always been a few pegs behind me, and as a result she’s always tried to outdo me."
            butters "But it’s pretty hard to outdo someone with twice your age and experience."
            butters "I’m fairly sure she can brew her own anti-lycanthropy potions now, but I’m still going to help her cure the werewolves in the area."
            mc "What’s up with the werewolves I keep hearing about?"
            show butters dressneutral with d
            butters "Well… They’re not actually native to this area, she purposely infected someone for her sick fetish"

    mc "Woah, that’s pretty heavy."
    show butters dressangry with d
    butters "I was so pissed off that I swore I’d never work with her again…"
    butters "But here I am, having cured my succubification, so I wanted to try and cure that werewolf too."
    show butters dressneutral with d
    butters "Problem is, there are probably a few of them now…"
    mc "Oh dear! We're all at risk."
    show butters dressangry with d
    butters "Zoe thinks there's just the one male and a few submissive females, but it’s hard to keep track. For all we know, there could be another one from tonight."
    butters "It’s quite the stressful job because it’s almost impossible to identify the curse in regular individuals."
    butters "As long as we can get all the males that’ll typically fix the problem though, female werewolves only mate with other werewolves. But I guess bite infections are still a possiblity..."
    show butters dresssad with d
    butters "So anyway, that’ll be what I do every full moon for about half a year."
    butters "Watching from the trees with two servings of the potion. The only time a werewolf really lets its guard down is when they’re knotted in a female."
    mc "I think I totally understand why you’re pissed off."
    mc "Surprised you let me fuck her, then. You could have just left her to sit around for the hour."
    show butters dresshappy with d
    butters "Ah, I’m not so cruel. I figured you’d still have fun with a thick MILF like her."
    butters "Take her offer to go visit her too, I don’t mind."
    butters "Maybe a normal man will help knock some sense into her."
    mc "Ah-ha! You think if she sleeps with me, she’ll stop being such a werewolf fucker?"
    show butters dresslaughing with d
    butters "Mehh, you’re certainly good enough at sex to take that lustful energy of hers and put it somewhere else."
    mc "Oh well, I don’t mind."
    show butters dresshappy with d
    butters "And thanks for saving about forty-five minutes of my life. Imagine if I had to wait that entire time!"
    mc "Maybe call me next month? Hah."
    if livingwithbutters == 1:
        jump eveningbuttersmenu
    else:
        mc "I’m gonna go back to the wagon. See you later Butters."
        butters "Bye-bye [playername]."
        scene bg black with dissolve
        jump eveningmoxie1
    ###################################################
label zoe2:
    if zoevisit1 == 0:
        $ zoevisit1 = 1
        scene bg forestnight with d
        "Alright, let’s visit the {i}other{/i} witch in the woods."
        "Now that I know a little more about her from Butters, I’m interested to hear if she has a side to this story."
        "I walk through the woods until I stumble upon the second cottage, barely remembering the correct way as I stumble around."
        show bg foresthouse2 with d
        "But eventually, west to Butters’ cottage, I find Zoe’s abode."
        show bg zoehouse with d
        "I knock on the wooden door, and she lets me in."
        show zoeb
        show zoe horny
        with d
        zo "Greetings [playername]. Are you here to give my pussy a beating?"
        mc "Hey Zoe, sheesh, you didn't waste any time. How about you just bend over now why don't you?"
        mc "I suppose by being here I did take you up on that offer though, didn’t I?"
        show zoe satisfied with d
        zo "When I’m done screwing with you, you’ll feel like new."
        "She seductively wiggles her hips, exuding big MILF energy right now."
        mc "I see you’ve taken a liking to me, even though I’m not like your werewolf lovers."
        show zoe angry with d
        zo "Ah, she told you? It’s true, I do like the occasional canine to screw."
        zo "But I suppose you’re not so bad between the full moons. I’d be driven mad if I could only have sex once a month."
        mc "And uh, you made this individual you were hunting for last night a werewolf on purpose?"
        show zoe neutral with d
        zo "Ahh… *Sigh* There was an accident, but Butters claimed I was entirely at fault for my carelessness."
        zo "It’s true, I had a lycanthropy potion… but it was never my intention to give it to someone. Now the curse has spread through sex and biting. It has become quite the stress."
        menu:
            "Butters didn’t seem to think it was an accident…":
                show zoe angry with d
                zo "I empathise with that position. What are the odds that a known wolf fetishist would ‘accidentally’ sell a man an unlabelled lycanthropy potion instead of the product they wanted?"
            "How do you mislabel such an important potion?":
                show zoe angry with d
                zo "Butters had always been critical of my habits, and I always rolled my eyes and acted irate. But she was correct, my habit to not label any of my potions has certainly placed a lot of problems on my plate."
            "Mistakes happen, as long as you try to make amends that’s okay, right?":
                show zoe angry with d
                zo "My actions have caused a lot of grief. The situation should have been far more brief, but my carelessness caused the curse to spread further than it should have."

        show zoe neutral with d
        zo "Yes, I am partially guilty, that is my admission. But it was still an accident, and only recently Butters has come around to see my side of the story, so the two of us tried to cure the victim."
        mc "How many are there?"
        show zoe happy with d
        zo "Hard to say. Our hands are tied due to male werewolves and their predisposition to spread it."
        zo "We’ll need to keep that at bay. When we first met, you saw my method. Using a special pheromone fragrance, we can lure all male werewolves in about a ten-kilometre radius until they just stop coming."
        mc "Uh, what if multiple arrive?"
        show zoe satisfied with d
        zo "I can take a few, then Butters can cure them after they’re exhausted from their screw."
        mc "And the females?"
        show zoe happy with d
        zo "Typically docile and only sought out by the males. Butters is currently trying to concoct a method to detect them, which is great."
        "We should probably get Lily to help, or even Princess Selene. They probably haven't even noticed 2-3 infections, but I bet they can easily nip the problem in the bud."
        zo "If we don’t control the situation, we’ll definitely draw the ire of Princess Selene at this rate. I could do without a prison sentence."
        mc "Hm... I really don't think avoiding help is the solution."
        menu:
            "If you want my advice, it’s time to act real fucking humble, listen to Butters and get this done right.":
                show zoe neutral with d
                zo "*Nods* Yes, this has been a lesson in humility."

            "Whatever man, you deserve this for your carelessness.":
                show zoe neutral with d
                zo "I deserve this? I’m not even the one suffering. It’s them, and they don’t deserve that."

            "Enough about fucking werewolves, how about fucking me instead?":
                show zoe horny with d
                zo "*Sigh* You’re just as bad as they are. But I like a bad boy."

            "Can’t I have a go at a female werewolf if you find one?":
                show zoe neutral with d
                zo "I suppose such a thing could be arranged. Is that something you’re into? I didn’t realize your fetishes were also deranged."

        mc "Hmph…"
        "At that moment, a familiar green figure enters the room."
        scene bg zoehouse
        show alraune neutral:
            xpos 450
            ypos 135
        with d
        alraune "Ah? It’s you!"
        mc "The Alraune from the cave? What are you doing here?"
        show alraune angry with d
        alraune "I live here, dummy!"
        show zoeb:
            xpos 100
            ypos 30
        show zoe happy:
            xpos 100
            ypos 30
        with d
        zo "Mhm, the Alraune here is my pet. She means no threat."
        mc "You know this ‘pet’ molested Butters and I once, right?"
        show zoe angry with d
        zo "Is this true? I shall have to discipline you, Alraune."
        show alraune neutral with d
        alraune "Wha? It was consensual, you bully!"
        alraune "Look, come here [playername]."
        "She comes closer and whispers into my ear."
        show zoe neutral with d
        show alraune horny
        with d
        alraune "*Whisper* Please cut me a break! She’ll be on my ass all month otherwise."
        alraune "*Whisper* I’ll let you bang me if you do!"
        menu:
            "Alright, molestation was a bit of an extreme way to phrase it. We all had a good and consensual time.":
                show alraune laughing with d
                alraune "Yep, yep! What do you think, Zoe?"
                show zoe neutral with d
                zo "Well, I can overlook a small instance of hyperbole from [playername], as long as you were behaving."
                show alraune happy with d
                alraune "Phhhewwww…"

            "Nope, she totally molested us both. She needs some discipline.":
                show zoe angry
                show alraune neutral
                with d
                alraune "Oh come on! It was only some light jovial molestation!"
                mc "There is no such thing!"
                zo "I see… In that case… The only punishment I can think of as an alchemist is one of equivalent exchange."
                zo "Alraune, you must sexually please [playername] to repent. Hopefully one day you can stop acting like an ass, and stop harassing every man you pass."
                "You know, Zoe is really growing on me right now."
                show alraune angry with d
                alraune "Awwwhh maaannn…"
                mc "Why are you complaining? That’s exactly what you said you’d do when you whispered in my ear."
                show alraune neutral with d
                alraune "Yeah but, I hate being told what to do, even if I was gonna do it anyway! Hehe."
        show zoe horny with d
        zo "You seem to be popular in this house, [playername]. Who will you be accompanying tonight?"
    else:
        show bg zoehouse
        show zoeb:
            xpos 100
            ypos 30
        show zoe happy:
            xpos 100
            ypos 30
        with d
        zo "Greetings, [playername]. Always a welcome guest in this household."
        show alraune laughing with dissolve:
            xpos 450
            ypos 135
        if alraunesex == 1 and alraunec == 0:
            $ alraunec = 1
            alraune "Oh my gosh, [playername]! Come here!"
            mc "Huh?"
            "She leads me into her bedroom."
            scene bg poyobedroom with d
            show alraune happy with dissolve
            alraune "Look, our child!"
            mc "Ah?!"
            "She holds out a potted plant towards me. It's a single green stem in some soil."
            mc "Uhh, this thing is our child?"
            show alraune laughing with dissolve
            alraune "Yep! Isn't she soooo cute?"
            mc "Oh, uh, yeah... Is this an Alraune too?"
            show alraune neutral with dissolve
            alraune "Well, she could be in about ten years. For now, it's just a rose!"
            mc "My semen contributed into making a rose? Woah..."
            show alraune happy with dissolve
            alraune "Let's make lots more! Okay?"
            "Man, maybe I oughta be more careful about who I choose to cum in."
            show alraune horny with dissolve
            alraune "For now, um, maybe you want to have some fun with Zoe too? You can pick one of us if you want!"
            scene bg zoehouse
            show zoeb:
                xpos 100
                ypos 30
            show zoe happy:
                xpos 100
                ypos 30
            show alraune laughing:
                xpos 450
                ypos 135
            with d
        else:
            alraune "Hiya! Gonna stay the evening again? You’ll have to pick a lovely lady to spend that time with."
        stop ambience fadeout 20.0

    menu:
        "Sex with Zoe":
            zo "Sorry my dear pet, but [playername] has chosen me today. You needn’t fret, I’m sure you’ll be on his list next."
            alraune "Yeah yeah, whatevs!"
            scene bg zoehouse
            show zoeb
            show zoe horny
            with d
            "Alraune leaves the room, giving us some privacy."
            zo "How would you like to do this?"
            menu:
                "Doggystyle":
                    jump zoedog
                "Leg-up Sideways (NEW!)" if zoelum == 0:
                    jump zoelum
                "Leg-Up Sideways" if zoelum == 1:
                    jump zoelum
            label zoedog:
                show zoe neutral with d
                zo "Would you like to do this one outside? It’ll make it feel fierce and primal while you rut my backside."
                mc "Suppose we could. The fresh air will stave off the sweat."
                scene bg forestnight with d
                "The two of us take a few steps out into the forest clearing of her cottage and she goes prone down in a patch of grass."
                play music sex1 fadein 3.0
                show zoeb doggystyle
                show zoe doggystyle1
                with d
                mc "Has anyone told you that your ass is sublime?"
                zo "Considering your equally appreciable cock, you can take my ass anytime."
                mc "Hah, you used my own words to rhyme. I wonder when this gimmick will get old."
                "As I get into position before her presented rear, she exudes a high level of excitement, her tail swishes so fervently it keeps brushing against me."
                "The sweet flowery aroma that attracted me here combined with the smell of sex heightens my need to pound her pussy, almost to a beguiling degree."
                play sound cum
                show zoe doggystylev1 with d
                "Her drippy pussy is clearly wet and ready, so I skip teasing and begin the session by pressing aligning the tip of my cock against her pussy and pushing inside."
                "Immediately I sink into the pleasant warmth of her depths, her lips parting bit by bit as it easily accepts me to the hilt in a single smooth motion."
                zo "Ahhhh, ahh… I’m so appreciative that you were present, because that feels extremely pleasant."
                play ambience sex fadein 3.0
                "Her hips twitch as I pull back and sink back in, beginning to rut her at a pleasureful pace for the both of us."
                "Zoe was so wet from the start, she was clearly anticipating this and prepared for it. So it’s not too surprising that she accepted me even if I perhaps wasn’t quite what she wanted."
                "The lustful wetness does allow me to pound her as fast as I want though, choosing to alternate between fast thrusting and then slowing myself down as to pace myself."
                "Each movement causes friction against her swollen clit, and deep sensitive spots within her pussy, filling the zebra girl with bliss."
                zo "Aaahhh, haaahhh, that’s it, I want you to fill me with your seed."
                "Hm, she didn’t rhyme that time. I clearly have my priorities wrong if I’m thinking about that right now, but this zebra girl is an enigma to me on so many levels."
                show zoe doggystylev2 with d
                zo "Aahhahah, yesss... That’s good, keep going at that speed!"
                "Oh, there’s the rhyme! I thrust into my lover at the requested pace, rocking her back and forth against the grass while her toes curl and thighs quiver."
                "Doesn’t seem like it’ll take long for her to reach an orgasm, and indeed she does achieve one far before my own as the mare squeals happily."
                "Her moans grow in lustful intensity, that coupled with the wet schlicking of her pussy, it's pretty much the only thing I can hear as we rut in the dark woods."
                "After her first orgasm, almost impatiently, I feel her hips begin to rock back and forth on my cock. Matching my own pace with some immediacy, and then outmatching it as she speeds up."
                "Her hip movements make her sexual experience immediately clear; she’s done toying around with me, and now she’s going to make me cum."
                "I grab her hips and commit to the accelerating pace, adding a third sound of our bodies slapping together to the mix."
                zo "Ahh, such a sly dog, ahh ahhhh… You’re certainly not a shy lover."
                "My cock begins to twitch and get tighter as my impending orgasm draws closer and closer."
                zo "Now, cum in me I want it all…"
                "At a certain point my orgasm is all but confirmed, but it still takes a few seconds to escape. I use that time to push my body as far as it’ll go, fucking as hard as I can, to push to the heights of euphoria."
                play sound cum
                show zoe doggystylev3 with cum
                play sound cum
                show zoe doggystylev3 with cum
                "And then in one moment of intense bliss, my cock releases its load deep into the waiting mare."
                play sound cum
                show zoe doggystylev3 with cum
                play sound cum
                show zoe doggystylev3 with cum
                zo "Ahh, yess, that’s it… Fill up my womb, until there’s simply no room!"
                stop ambience fadeout 3.0
                stop music fadeout 3.0
                show zoe doggystylecum with d
                "With one final load of cum, I finally empty my balls in the zebra and she slumps onto the grass, panting."
                "I follow her example, lying beside her and resting my head on her voluptuous breasts."
                scene bg black with d
                "After the two of us catch our breathes in the cool outside air for a few moments, we return inside and spend the evening together."
                "In the morning, I return home bright and early."
                $ zoedog = 1
                jump altmorning
            label zoelum:
                zo "Simply splendid, let us begin immediately."
                show bg honeycrispbed
                play music sex1 fadein 3.0
                show zoeb lum
                show zoe lum1
                with d
                "Taking me to her bed, she lays down on her side and soon her legs are spread. Her pussy dripping with anticipation as she presents herself to me."
                zo "I have something that needs to be attended… See how wet my pussy is?  It must be amended."
                "I’d be lying if I said my attention wasn’t immediately drawn to her pussy."
                mc "This promises to be good. Jiggle that ass for me."
                "One of her hands even spreads her ass slightly, wiggling back on forth on my command, and giving me a great view of her genitals."
                "Her pillowy assets really are on full display in this position, allowing my cock to readily come to attention as I stroke it."
                "Zoe looks back at me and grins, anticipating my large cock as I approach and get into position between her legs."
                "Like many denizens of Arcadia, she’s horny as heck and ready for a pounding. Almost with obedience she eyes up my cock eagerly as I begin to poke and prod it against her puffy labia."
                if zoelum == 0:
                    show zoe lum2 with d
                    zo "Hahh… Such a delicious looking cock. I can’t believe my luck having stumbled upon you in the forest while you were on a walk."
                    mc "We’re both lucky. I get to fuck a gorgeous Zebra girl, and you get one of the best fucks in the city."
                    show zoe lum1 with d
                    zo "Phew, and you’re not all talk either… I can’t contest your words, you may be just as good as a wolf man, if not a little bit better."
                    mc "Heh, sounds like I still have something to prove."
                    show zoe lum2 with d
                    "She blushes slightly and returns her gaze to my cock, seemingly impatient and needy as she uses her hand to spread her lips slightly."
                    zo "Actions, my boy."
                else:
                    show zoe lum2 with d
                    zo "Haahh… I always get slightly uncharacteristically giddy in anticipation of sex with you, [playername]…"
                    "She blushes slightly and returns her gaze to my cock, seemingly impatient and needy as she uses her hand to spread her lips slightly."
                play sound cum
                show zoe lum3 with d
                play ambience sex fadein 3.0
                "I align and push my shaft against her nether lips, slipping into her wetness and parting her pussy with ease, as I sink into the warmth."
                "Her pussy sucks me inside with ease, her grool coating my entire cock and easily lubricates the tightness of her squeezing walls."
                "As I hold onto her thigh, this position allows me to slide to her absolute depths with ease."
                "And as I pull outwards, I’m able to do long, satisfying, deep thrusts which not only pleasure each inch of my cock, but satisfy her deepest and most sensitive spots."
                zo "Ahhh, aaahhhh! That’s right, slide that cock deep into me, fill us both with joy."
                "Panting and moaning slightly, Zoe caresses and teases her large breasts and erect nipples as I begin to hump her pussy."
                "My deep thrusts gradually pick up pace and her internal squeezing gets more intense, as the pleasure begins to build up within us."
                "With a spare hand entirely free, I find my thumb rubbing her clit intently, while my cock likely creates some friction on her g-spot."
                "The result is a zebra that throws her head back in bliss, and moans loudly. Her thick body mesmerising, as it jiggles back and forth on the bed."
                show zoe lum4 with d
                zo "Gooshh, yess… Keep rubbing my clit, keep rubbing, just like that…"
                "I maintain this exact pace in both my fucking and rubbing, and almost visibly I can see the orgasm building within my lover."
                "Until finally it erupts, and Zoe begins twitching as her pussy spasms around the base of my cock."
                "Contractions attempt to wring my shaft, although I had paced myself well enough as to not be too close to cumming quite yet."

                if zoelum == 0:
                    "I had something to prove with this girl. I had already planned to give her at least one more orgasm in an attempt to really blow her mind."
                    show zoe lum3 with d
                    zo "Haahhh, y-you’re still going? I’m used to the man cumming by now, haah…"
                    mc "Heh, stubborn further than your eyes can see. I’m no wolf, I’m a man."
                else:
                    show zoe lum3 with d
                    mc "Ready for orgasm two? Don’t lose your mind."

                zo "Come on then big man, show this witch some real magic."
                "Gripping onto her thigh tightly, I start to pump faster into her slick pussy."
                "Her lubricants are so plentiful that I’d barely be able to feel anything if it wasn’t for the incredible tightness of her insides. Tightness that she intentionally increases by tensing her muscles."
                "Kneading her own breasts, and tweaking her sensitive nipples, she lavishly indulges in the second assault of intense pleasure as my finger begins to focus on her clit again."
                show zoe lum4 with d
                "Her back arches and teeth grit together as she struggles to hold herself together. Her entire body wriggling and spasming with a lack of control."
                "At this speed and intensity, I could feel my orgasm begin to rise too. My cock grows tight as the familiar urge to unload rises."
                "The pleasure of her insides squeezing my throbbing shaft is really enough to push me straight over the edge."
                "And fortunately, as I finally reach the potent ecstasy of my own powerful orgasm, my lover rolls her eyes back and moans out."
                zo "Aahhh, coming! Cum with me!"
                play sound cum
                show zoe lum5 with cum
                play sound cum
                show zoe lum5 with cum
                "The cum was already surging within me, and finally it erupts deeply into Zoe."
                play sound cum
                show zoe lum5 with cum
                play sound cum
                show zoe lum5 with cum
                "Her pussy and womb are filled by an above average load from my cock, all whilst she moans in an orgasmic delight and spurs my last few fatigued thrusts on."
                play sound cum
                show zoe lum6 with d
                stop music fadeout 2.0
                stop ambience fadeout 2.0
                "And as soon as my orgasm dries up, that fatigue finally overwhelms as I sit back limp, pulling my member out of her with a schlick."
                if zoelum == 0:
                    mc "Phew, how was that?"
                    show zoe lum7 with d
                    zo "Pfft, you were just showing off how good you are in bed."
                    zo "But, that {i}was{/i} tremendous, even compared to a Funris… Maybe… maybe, I have a new favourite instead."
                    mc "Hah, I bet you’d say that to anyone after sex."
                    show zoe lum6 with d
                    zo "Ihihi, I find myself unable to deny such an accusation."
                    zo "If you were trying to impress me because Butters told you to, don’t worry about it."
                    scene bg honeycrispbed with d
                    show zoeb
                    show zoe happy
                    with d
                    zo "I don’t know if her, or your intention was to ‘fuck’ the fetish out of me, but honestly that’d be silly."
                    zo "I told her I’d never turn anyone into a werewolf just to sate my own desires, and that remains true."
                    zo "Not only do ordinary wolf men exist..."
                    zo "But I, like any other mare, just go to the spa, or church when I’m horny. I very rarely practice my fetishes, like most others, I imagine."
                    mc "Is that so? Maybe I’ve misinterpreted what kind of person you are because of your falling out with Butters."
                    show zoe horny with d
                    zo "Mmm… Is that so? If you were going to interpret me as anything, can it be a sexy mommy?"
                    mc "Hm, maybe…"
                    mc "Also, you stopped rhyming."
                    show zoe satisfied with d
                    zo "Because I’m tiiireed, I’ll be asleep in ten minutes… I can’t keep that up all the time."
                    mc "Alright Zoe, let’s snuggle."
                    show zoe horny with d
                    zo "That’s fine with me. After a good nap I shall be able to rhyme."
                else:
                    zo "Phew… That was amazing…"
                    scene bg honeycrispbed with d
                    "Zoe slumps from her side to her back and spreads out like a starfish."
                    "Given her pillowy features, I crawl over her and cuddle."
                    "In an unexpected turn of events however, she rolls on top of me and squashes my face in her breasts."
                    show zoeb
                    show zoe satisfied
                    with d
                    zo "I’ll make you a really good breakfast tomorrow morning. Least I can do for the booty call."
                    mc "*Words muffled in breasts* Sounds good."
                scene bg black with dissolve
                "The two of us snooze while snuggled together."
                "I return home early in the morning."
                $ zoelum = 1
                jump altmorning
        "Sex with Alraune":
            if alraunesex == 0:
                show alraune neutral with d
                alraune "Bleh, you’re totally gonna knock me up if you cum inside… I guess I can live with that."
                alraune "Come on then, let’s go to my room."
                scene bg poyobedroom with d
                "I step into a fairly regular room. This little pet relationship is reminding me of Butters and Poyo a little."
                mc "So, this’ll be a bit of revenge for last time, then."
                show alraune laughing with d
                alraune "Meh, if you must see it that way. I suppose that did come back to bite me in the ass."
                alraune "This is what I get, my punishment for being a little naughty!"
                show alraune horny with d
                alraune "So, I’ll let you do it, fuck me, fill me, and knock me up!"
                "I squint at the Alraune slightly confused, having absolutely no logistical idea of how to actually fuck her, considering there’s a giant plant bulb in the way."
                mc "Okay, I’m just wondering what the best method to go about doing this is…"
                show alraune neutral with d
                alraune "Oh my gosh, is it your first time too?!"
                mc "Uh, no, it’s just… How do I reach your pussy? Even if you were to bend over your leaves are in the way."
                show alraune happy with d
                alraune "Ohhh, hehehe… There’s room for two in this bulb you know… It’s ‘designed’ that way, hehehe…"
            else:
                show alraune neutral with d
                alraune "Again? I guess I did ask!"
                alraune "I dunno what’s come over me lately, but I’m just a total slut lately, heh."
                scene bg poyobedroom with d
                "I step into a fairly regular room. As before there isn’t much here other than basic entertainment and some storage. A plant girl sure doesn’t need much to distract her."
                "And there’s no distraction for Alraune too, as she immediately begins acting sexually."
            show alraune horny with d
            "She leans back slightly and spreads her pussy, her legs although they do separate at the hips seem to be stuck together at the base resulting in an interesting angle."
            "And indeed, she is correct, there’s a noticeable area before her within her flower…"
            "Cautiously, I step closer, pulling aside leaves as I get adjacent to the rose bud."
            alraune "Don’t be shy… The dew feels great!"
            "I dip my finger into the pinkish goop, and not particularly to my surprise, it’s the exact pink aphrodisiac from the cave before."
            "Fortunately, her leaves also relieve the effects of that aphrodisiac, so I forgo caution and begin to lift myself into the bud."
            play music sex1 fadein 3.0
            scene alrauneb sex
            show alraune sex1
            with d
            mc "Aaaahhhh…"
            "Warmth and comfort like a hug consume my body as I step into the pleasant bulb."
            mc "This is really nice… We’re pretty damn close to each other though."
            if alraunesex == 0:
                alraune "Oh fuck, I’m not the only one getting extremely horny, right? Ohh, gosh…"
            else:
                alraune "I think I get it now… When a man steps into my pool it immediately actives some kind of sex instinct, it makes me sooooo hornyyyy."

            "I’m already half erect at this point, and immediately tingles of the aphrodisiac aid in bringing out the other half of that erection."
            "Within a few seconds, my precum dripping erection is pressed against her belly."
            if alraunesex == 0:
                show alraune sex2 with d
                alraune "Hahh, gosh, I think I just started ovulating…"
                mc "Does your species do that around a male?"
                alraune "Mhm… Whenever one steps into my flower, hehe…"
                alraune "I guess that means you’ll have to pollinate me…"
            else:
                show alraune sex2 with d
                alraune "Haahh, gosh, pollinate me with your seed!"
            "She bashfully giggles as she takes my cock and guides it between her legs."
            "With my tip poking at her entrance, I grasp both of her hips and push in."
            if alraunesex == 0:
                show alraune sex1 with d
                mc "This purple liquid really does wonders for an erection, aren’t you always horny?"
                alraune "Me, h-horny? Yessshhh!"
                mc "No, I mean…"
                alraune "Fuck me, fuck me!"
                mc "Oookay, you got it."
            else:
                show alraune sex1 with d
                alraune "Ahh, haaahhh… Ahhhh… This feels far too good… Like… I can’t tell who’s more drunk on arousal, you or me."
            play ambience sex fadein 3.0
            show alraune sex2 with d
            "She leans back as I thrust forward, giving me as much room as possible in this unusual angle of penetration."
            "Despite the Alraune’s large overall body, her feminine frame is petite as I handle her. My hands almost encompassing both her hips as I tightly grip her for leverage. Her breasts bobbing up and down with the force of each thrust."
            "Her cute breasts, and their function of which I’m not entirely sure, sport two green nipples which had become noticeably puffy and erect since penetration."
            "Tweaking and teasing the nipples results in girlish moans escaping from my lover, as it appears, they’re sensitive like any other girl."
            show alraune sex3 with d
            "And as my hand explores the rest of my lover, I also find my way down to her pussy, teasing around for a clitoris to rub which greatly excites her also."
            "Regarding her pussy, the tightness is naturally immense with her thighs locked together, creating a sensation similar to standing sex."
            "And the purple aphrodisiac enhances the sensation, to such a degree that it probably robs me of free will, and forces me to fuck."
            "Come to think of it, that’s probably how Alraunes ‘catch’ their mates."
            if alraunesex == 0:
                show alraune sex2 with d
                alraune "Ahhhhah, I want you to cum in me lots and lots!"
                mc "Hang on… Am I not just cumming inside you once?!"
                alraune "Nooooo, I want a lot more cummies than that!"
            else:
                show alraune sex2 with d
                alraune "Fill me up with your cummies!"
            "I gulp, and just focus on the fucking, there isn’t a lot I can do since my mind is so beguiled and focused on sex."
            "Her internal juices which completely coat my member allow me to thrust faster, but I soon realize that her internal juices are exactly the same purple liquid that I’m currently standing in."
            "This purple liquid sends pleasureful tingles throughout my cock which travel through my body like a wave of euphoria."
            "All thought without regard to sex leaves my mind, as I pummel her tight green plant pussy. It squeezes and suckles around my cock with an increasing aggression, as if it’s purposely trying to milk me."
            "All of these sensations send me into a spiral of intoxicated pleasure. Overcome with lust, my hips accelerate and I pound the alraune with all my effort."
            "She yelps with surprise, letting out a giggle and then a moan as pleasure also crashes through her. My cock repeatedly pumping into the deepest reaches of her warm flesh."
            show alraune sex3 with d
            alraune "Yesss, yesss, ahhaaahhhh… Fuck me, fuck me!"
            "It doesn’t take too long for a tension in my taint to arise, signalling an impending orgasm."
            alraune "Oh my goshh, aaaaahhh!"
            "Since she doesn’t shut up moaning, I temporarily press my thumb into her mouth to suckle on, which she gratefully does."
            "Ironically, this action only seems to excite her more as her entire body quivers with orgasmic bliss, the very leaves and petals of the flower trembling with pleasure."
            "And with her orgasm, mine isn’t too far off either. Her slick pussy squeezes one last time and triumphantly it almost immediately pushes me over the edge as my cock swells and prepares to unload."
            "Trembling, my member releases a hot load of cum directly into her pussy."
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            "The release is powerful enough to send shivers down my spine, as a truly inhuman amount of jizz pours out of me and fills my lover up to the brim."
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            stop ambience fadeout 3.0
            stop music fadeout 15.0
            "Even when my orgasm dissipates however, the positioning keeps my cock lodged deep inside her, and the aphrodisiac keeps me very much erect."
            "Despite that, for the briefest moment my mind is clear. Taking some initiative, I pinch off a tiny bit of her leaf and nibble it to quell the overwhelming effects of the purple goo."
            if alraunesex == 0:
                show alraune sex6 with d
                alraune "Owww! What was that for? Bully!"
                mc "Mmph? *Munch* Sorry, I didn’t realize that’d hurt you."
            else:
                show alraune sex6 with d
                alraune "Eep, easy on the leaves…"
                mc "I wonder how fast these things grow… Like, could you run out?"
                alraune "Nahh, all my body parts grow back, eventually."
                alraune "Although if my brain is damaged and regrown, I could be a completely different person! Weird, right?"
                mc "Is that true? I guess I’ll take your word for it."
            show alraune sex5 with d
            "Almost immediately, the aphrodisiac seems to wear off, and my cock returns to the state you’d expect after an orgasm: soft and sensitive."
            scene bg poyobedroom with d
            "And with that, I take the opportunity to slip out of the Alraune’s sex trap. The purple liquid treating me like I’m hydrophobic, and not coming with me, leaving me completely dry as I step out."
            if alraunesex == 0:
                show alraune neutral with d
                alraune "Ohh man… But I’m still so horny! You’re such a dick!"
                alraune "And there’s no way you got me pregnant after one time…"
                alraune "You’re going to have to fuck me lots and lots! Okay?"
                mc "Yeah, yeah… I just didn’t want you to put me in a coma."
                show alraune horny with d
                alraune "Pfft, I couldn’t even have sex with you without your consent anyway. With my body, there’s almost no natural position where I can be on top. All I can do is use my feeder, and that’s no fun…"
                mc "Yeah, and that’s exactly why you have the aphrodisiac to trick men into taking the initiative."
                mc "I won’t fall for your trick this time. But I might have sex with you again in the future, that was exceedingly pleasureful."
                show alraune laughing with d
                alraune "Oh, you will? That’d really make my day!"
                show alraune neutral with d
                alraune "Oh, and in the morning, can you give me some cum for breakfast? I’d love that!"
                mc "Damn, you’re so needy when it comes to my cum. But I don't think I'll be sticking around for that long."
                show alraune happy with d
                alraune "Least I tried! That’s a monster girl for you! Hehe."
            else:
                show alraune neutral with d
                alraune "Hmm… It seems that as soon as you step out of my plant, that sex instinct fades pretty quickly… I can breathe easy with that knowledge."
                show alraune happy with d
                alraune "You’re pretty sly nibbling on some leaf between orgasms."
                alraune "Most men would be far too focused on sex to do that."
                mc "What can I say, my aversion to death is greater than my need for sex."
                show alraune laughing with d
                alraune "Hehe, as if I would hurt you!"
            $ alraunesex = 1
            scene bg black with d
            "The two of us eventually settle down, but she doesn’t have a bed because she just sleeps in her flower."
            "So I end up going back home to sleep."
            jump sleep
        "Hunt Werewolves" if zoelum == 1 and fr == 1 and werewolfsex == 0:
            "You found a secret scene! Requirements were: Max out Zoe's affection and beat Morrigan."
            $ werewolfsex = 1
            zo "Feeling brave? Or perhaps there's something else you crave."
            mc "I thought I'd take you up on that offer, and perhaps I could be an adequate 'distraction' for catching a female werewolf."
            zo "Yes, I quite like that plan. Would you be willing to join us? Butters has this plan of hers that could solve this predicament before the next full moon even occurs."
            mc "Sure thing, send me a magic mail with the time and date."
            scene bg black with dissolve
            "..."
            $ days += 2
            "Three days later, 11:00PM"
            label werewolfhunting:
                pass
            play ambience ambiencenight fadein 3.0
            scene bg forestnight
            show zoeb:
                xpos 50
                ypos 30
            show zoe happy:
                xpos 50
                ypos 30
            if fr == 1:
                show lilyb w:
                    xpos 400
                    ypos 75
            else:
                show lilyb:
                    xpos 400
                    ypos 75
            show lily happy:
                xpos 400
                ypos 75
            show butters dressneutral:
                xpos 650
                ypos 30
            with dissolve
            "I join Butters, Zoe and Lily in the forest clearing from before."
            "We should be just a far enough distance to use the special pheromones from before to attract werewolves, but not random citizens from the suburbs."
            "Butters had asked Lily to come and help us. Considering Butters' previous reluctance to work with a pony, I'm proud that she earnestly asked for help."
            "Lily has really enabled us to clean up this problem with her magical abilities."
            show butters dresshappy with d
            butters "Based on Lily's scouting, we believe there is a male and a female werewolf."
            "This time is a little different. We have a pheromone to attract not only the missing male werewolf, but the missing female werewolf too."
            mc "How are we going to give them both the potion?"
            show zoe horny with d
            zo "The same way as before. We'll be tonight's score."
            show butters dressneutral with d
            butters "Mhm, we'll be using both Zoe and you as bait. Zoe will administer the potion after she has been knotted, and you are more than capable of transmitting it through your semen."
            mc "Won't the male and female werewolf try to have sex with each other?"
            show butters dresshappy with d
            butters "Not if we stagger the pheromones. I believe it'd be best to use the male pheromone first, so the ladies here don't get too horny."
            mc "A really well-thought-out plan. All right, as per usual, my dick is at your service."
            show lily horny with d
            lily "This is quite a wild plan... Are you sure you want to be the bait Zoe? I'd be more than happy to take your place, I'm quite self-sacrificing like that."
            show zoe laughing with d
            zo "Absolutely not dear, I fear that I could never impose such a difficult task on one such as yourself."
            show lily neutral with d
            lily "Oh truly, it's no imposition, Zoe. I am the kind of team player that doesn't mind taking one for the team. So, by all means, I'll happily be the bait for the werewolf."
            show butters dresslaughing with d
            butters "Sorry Lily, but we'll need you on standby as a magic user just in case."
            show lily happy with d
            lily "Understood..."
            show zoe happy with d
            zo "Okay ladies and gentleman, five minutes until we begin our plan."
            hide lilyb
            hide lily
            hide butters
            with d
            if fr == 0:
                "The other girls nod, and Butters lifts Lily into a safe position in the tree."
            else:
                "The other girls nod, and the two of them fly up into the trees."
            "The darkness of the leaves keeps them out of sight, but we can still hear them."

            butters "You can masturbate all you want while we watch, Lily."
            lily "M-Masturbate? N-No, I wouldn't do that..."
            butters "Oh? I will. This aphrodisiac is strong stuff. Maybe I can help you out, hehe."
            lily "That won't be necessary! I-I'm going to sit on the other side of the tree, okay?"
            butters "Have fuuun..."

            mc "How are you feeling, Zoe?"
            show zoe satisfied with d
            zo "After we help the civilians, I'll be relieved."
            zo "I hope Butters and I can repair our working relationship. It was never my intention to have aggrieved."
            mc "We all make mistakes. You probably know this better than me that Butters can be frosty towards certain people, but for her that was always a defense mechanism because of her curse."
            mc "I think we'll both see her develop into a much brighter and happier person, especially now that her curse has been lifted."
            show zoe happy with d
            zo "You really are sweet. Hanging around you is always a treat."

            "A few more moments go by, and then Lily gives off the signal!"
            play sound woosh
            show white with d
            hide white with d
            "A bright surge of magic briefly waves through the forest, illuminating the surroundings and blowing the foliage with a gust."
            "And then, back to darkness."
            "That spell should have just triggered the werewolf transformations of our targets. Lily is a helpful ally indeed. If it wasn’t for her we’d have to wait almost an entire month between each attempt."
            show zoe horny with d
            zo "See you on the other side, [playername]."
            scene bg forestnight with d
            "She winks and disappears to her specific site, about 30 meters away."
            "The fragrant pheromones targeted for the male werewolf are already open to the air and beginning to permeate."
            "Hm, so both Lily and Butters will primarily be watching me, huh? The perverts."
            "Still, we agreed on a ten-minute gap between the two pheromones, so I'll have to wait to see if the male werewolf comes first."
            "Guess I’ll sit down over here under a tree. Hidden away enough to avoid the ire of a curious male werewolf."
            "Around five minutes in, a notable ruckus among the bushes alerts me."
            "It would appear our first target has arrived and is making its way to Zoe’s location."
            "Hmm, should I watch?"
            menu:
                "Watch Zoe and the werewolf for five minutes.":
                    stop ambience fadeout 5.0
                    "I can’t resist. I wonder if she’s talking to it in rhyme."
                    "I wander a few meters towards her, peeking through some trees and flora to get a stealthy glimpse."
                    show zoeb doggystyle
                    show zoe doggystyle1
                    with d
                    "Low and behold, in what I can only assume is her favourite position, she’s courting the canine who is curiously approaching."
                    zo "Oohh, you’re a big bad boy, aren’t you? Do you like the view? Hehe."
                    "Curiosity soon turns to desire, as the wolf approaches the Zebra’s rear. Its already throbbing member pokes and prods around her labia."
                    "It keeps missing in its state of arousal and adrenaline. I can somewhat relate to how it must feel, the powerful aphrodisiacs were enough to give me a slight erection, how would it affect a creature that is estimated to be ten times more sensitive to it?"
                    show zoe doggystylew1
                    with d
                    play sound cum
                    "Oh- it’s in!"
                    zo "Ahhhh, yesss… Press that fat wolf cock as deep as you can, big boy."
                    play ambience sex fadein 1.0
                    "The bulbous red cock of the wolf launches itself into Zoe’s voluptuous ass, and he frantically thrusts back and forth with such an intensity that Zoe’s entire body rocks back and forth."
                    "You can tell that just for a moment they’re both in complete bliss as Zoe’s entire body seems to scrunch up."
                    "However, this experience would prove to be short lived as the wolf began to gradually slow down, slower and then stopping."
                    show zoe doggystylew2
                    with d
                    play sound cum
                    "Having fully knotted Zoe, he hunches over and pants in a drowsy state."
                    stop ambience fadeout 5.0
                    zo "Wha? That was barely ten seconds! I wasn’t even close to coming! Don’t stop, keep plumbing! Damnit…"
                    "I can’t help but giggle slightly under my breath."
                    "Zoe looks bemused as she lays there while being pumped full of cum."
                    "She reaches over to a nearby bag and takes out the lycanthropy cure. Taking advantage of the Werewolf’s immobility, she manages to make him drink it."
                    "Although she barely had to try, he seemed pretty thirsty."
                    zo "Alright, give it a few minutes and he’ll be back to normal and extremely confused… That is if he doesn’t remain snoozed…"
                    mc "She talking to me? No, I guess not. She just has a habit of talking aloud, I guess."
                    play ambience ambiencenight fadein 5.0
                    "Alright, my turn. I bet I can have a lot more fun with a female werewolf than Zoe did with her counterpart."

                "No way.":
                    "It’d be a little strange to watch that."
                    "I shrug and sit back in my hidden spot while I wait for an additional five minutes."
            scene bg black with dissolve
            "…"
            scene bg forestnight with d
            "It's almost time."
            "First things first, I need to drink this lycanthropy cure, that way my semen will be able to cure the female werewolf."
            "I don’t actually know if this method is easier than force-feeding her the cure, but I’m not complaining. Sex might be my new favourite method of medicine delivery."
            "Okay, the female pheromone Butters created can attract one from up to ten kilometers."
            "It’ll also have the effect of making all the nearby mares horny, which is fun too. Maybe Butters will let me keep it."
            "I uncork the pheromones and allow them to permeate into the air while I standby."
            "I’m starting to get irritatingly horny thanks to the male affecting pheromones, so I’m definitely ready for this."
            "I click my tongue while leaning back on a tree, trying to ignore my throbbing erection."
            label werewolfsex:
                pass
            "And as I turn, I come face to face with…"
            play music danger fadein 1.0
            show werewolfblack with d
            "A werewolf? It’s already here?!"
            "She’s staring me down, sniffing curiously as she takes a few steps closer."
            "Typically, they’re docile and don’t force themselves on mates. So, it’s actually my responsibility to take charge here."
            "Hoping that she’d be receptive to my advances, I-"
            play music challenge fadein 1.0
            show werewolf with d
            "Oh."
            "Zoe wasn’t kidding, these are really submissive."
            "I bring my hand to my cock and jack myself off as the female werewolf watches with glee, her tongue lecherously sliding across her lips."
            mc "Can you turn around for me? I’m going to fuck you."
            scene werewolfb sex
            show werewolf sex1
            with d
            "To my shock, she nods and turns to expose herself to me, her tail wagging back and forth more like a dog than a wolf."
            "I grab her by her plush rump and draw her closer. She submissively leans in to every gesture enthusiastically. Her pussy already gleaming with blatant desire."
            play music sex1 fadein 3.0
            "I tap the tip of my dick against her pussy before slightly pushing forward, allowing my member to grind against her lips and clit."
            "My lover shivers and pants as I continue to rub against her with several teasing motions. Her hips sway into each movement with increasing fervour and her pussy begins to drip shimmering lubricants onto my shaft."
            "With a slight adjustment, I prod my cock against her entrance and push forward, parting the lips of her pussy in one slick motion as I plunge inwards."
            play sound cum
            show werewolf sex2
            with d
            "As I sink into her enrapturing depths the wolf girl thrusts her hips up to meet mine, each inch deeper encapsulating my cock with an acutely fulfilling warmth and pleasure."
            "Once fully inserted she immediately makes her input known, as several intentional squeezes of her internal muscles around my cock make me yearn for more."
            play ambience sex fadein 2.0
            "With one hand gripping her fluffy hips, and another finding itself tugging at the base of her lashing tail, I begin to pound her in a manner that could be described as rough and primal."
            "The two of us heavily under the effects of the aphrodisiacs have temporarily resigned ourselves to the carnal, wanting only to indulge in as much pleasure as possible."
            "It’s admittedly difficult to not overdo it and immediately cum, especially after long exposure to the male pheromones warmed my loins up to a state of high sensitivity."
            "However, my lover is more than satisfied with my paced thrusts, her pussy only seeming to get wetter as the tufts of fur around her labia dampen."
            "And she seems to be getting closer to an orgasm, her fingers clearly digging into the grass, her teeth clenching and ass pushing back eagerly."
            "Feeling particularly dominant, I raise my hand and give her fluffy posterior a rough spank."
            play sound spank
            "While her thick fur does a particularly excellent job of dampening it, the arousing effect is no less obvious as my lover squeals in delight. Her pussy walls temporarily squeeze me in the aftermath."
            play sound spank
            "And with a second focused spank, combined with increasingly unrelenting thrusts on her rump, her entire body seems to shiver and spasm with orgasmic pleasure."
            "Her tight pussy is doing an admirable job of milking me, but I’m too experienced to let myself cum so early in a once in a life-time session of sex."
            stop ambience fadeout 3.0
            "And so, I temporarily stop."
            show werewolf sex5 with d
            "My lover, whose face has parked itself in the grass with her tongue lulling, a position not too wholly different from how I imagine Zoe right now, catches her breath post orgasm."
            play sound cum
            play ambience sex fadein 2.0
            show werewolf sex2 with d
            "After around twenty seconds of pause, the furnace of passion reignites as my cock pushes back inside."
            "The wolf girl actively moans upon insertion, her tail rapidly swaying back and forth as I fuck her again."
            "With a quick tug of her tail, her pussy tightens, and with an occasional spank every half minute or so, her entire body racks with pleasure."
            "I’m fairly sure every other denizen in the forest right now can hear our passionate, animalistic rutting. Each thrust going from base to hilt, each thrust rocking my lover’s entire body back and forth."
            "Every squeeze of the wolf girl’s pussy brings me closer and closer. Every time I tug her tail, or spank her voluptuous fluffy butt, she only gets tighter."
            "And finally, amidst what appears to be my lover’s second climax, I can feel the inescapable rise of my orgasm."
            "That feeling in my loins builds explosively, like no regular orgasm, it’s an overwhelming and powerful feeling that seems to encompass my entire body."
            "I can already tell this is going to be an orgasm that rocks me to the core."
            "My body tenses up as I push hard, and push fast against my lover. Preparing to overflow, thrusting as fast and hard as I can."
            play sound cum
            show werewolf sex3
            with cum
            play sound cum
            show werewolf sex3
            with cum
            "And in one instant, cum splatters from my cock, spilling into the wolf’s pussy and overflowing it."
            play sound cum
            show werewolf sex3
            with cum
            play sound cum
            show werewolf sex3
            with cum
            stop ambience fadeout 5.0
            "My mind is completely filled with a bright fuzzy feeling of euphoria."
            stop music fadeout 3.0
            "The two of us ride our orgasms out until the heightened sensitivity wears off and physical fatigue sets in."
            scene bg forestnight with d
            "The effects of the alchemical potion certainly don’t waste time. I almost disbelieve my eyes as the werewolf undergoes a transformation right in front of me."
            "Her fur subtly changes from thick and bushy to the sheer coat you’d expect from a pony."
            "Indeed, the girl is immediately transforming back."
            play ambience ambiencenight fadein 3.0
            show claire neutral with d
            if musicstudio == 1:
                "Oh woah. It’s Claire!"
                mc "Are you okay, Claire?"

            elif spavisit == 1:
                "Is this the girl that works in the spa? Woah, I hope not!"
                "Can you imagine how bad the werewolf situation could be if one of the most successful sex workers had contracted the curse?"
                mc "Are you okay?"

            else:
                "I’m not sure who this is. I do hope she’s okay though."
                mc "Are you okay?"

            claire "Ahh… I suppose I’m feeling a little better now."
            claire "I… I’m sorry about that, I really shouldn’t have had sex with you…"
            claire "Goodness me. I have a boyfriend, yet here I am, transforming into a wolf and doing stupid things like that."
            claire "I have no self-control…"
            if crystalballactivated == 1:
                jump cbmenu

            play sound movement
            show butters dresshappy:
                xpos 0
                ypos 30
            show lilyb w:
                xpos 800
                ypos 75
            show lily neutral:
                xpos 800
                ypos 75
            with d
            "Dropping from the trees, the cavalry arrive to help explain the situation."
            butters "Don’t worry, you can’t be blamed for anything that happens under a lycanthropy transformation. But fortunately, you’re now completely cured!"
            show claire happy with d
            claire "R-Really? That is wonderful news! Ohh, can you cure my boyfriend too? That’s how we both got into this mess actually."
            show lily embarrassed with d
            lily "Ohh, the other werewolf? I guess he’s over…"
            show claire neutral with d
            claire "Lee? What are you doing, why are you fucking that Zebra?!"
            hide claire
            show butters dressneutral
            with d
            butters "Uh oh."
            show lily laughing with d
            lily "I’m sure they’ll be able to talk it out. They both kind of cheated out of necessity, right?"
            mc "Yeah, but he isn’t even a werewolf right now, he’s completely in control of his actions."
            show lily neutral with d
            lily "Oh dear."
            show butters dressangry with d
            butters "Tsk, Zoe! We had an agreement!"
            hide butters
            show lily laughing
            with d
            lily "Now they’re both mad."
            mc "Jeez, what are we going to do with those two?"
            scene bg black with d
            "…"
            scene bg buttershousenight with d
            play music butters
            show zoeb:
                xpos 0
                ypos 30
            show zoe happy:
                xpos 0
                ypos 30
            show lilyb w:
                xpos 400
                ypos 75
            show lily happy:
                xpos 400
                ypos 75
            show butters dressneutral:
                xpos 750
                ypos 30
            with dissolve
            zo "Phew, that’s everyone sorted. I’m glad the werewolf threat is thwarted."
            show lily laughing with d
            lily "And I’m glad they managed to rekindle their relationship through this ordeal."
            show butters dressangry with d
            butters "Although you really ought not to have continued having sex with him, Zoe. I’ll admonish you for that."
            show lily neutral with d
            show zoe angry with d
            zo "But… I wasn’t satisfied after the werewolf session, and he took initiative! So I question, how is that my fault?"
            show butters dresssad with d
            butters "Am I being too harsh? Maybe… It’s just…"
            show zoe neutral with d
            zo "Hey Butters… I’m really sorry for screwing this situation."
            zo "I know, I keep fucking everything up… I know I’m not as good as you, and I never will be… But I really do try because I admire you so much…"
            zo "So I’m sorry if I ever seem a little show-offish, or attention seeking, but… It’s so hard for me, because… well…"
            show butters dresssad:
                linear 1.0 xpos 600 ypos 30
            butters "Because of how hard I am on you?"
            show butters dresssad:
                linear 1.0 xpos 400 ypos 30
            butters "I… know… I think, in many ways I always knew."
            show lily neutral:
                linear 1.0 xpos 800
            show lilyb w:
                linear 1.0 xpos 800
            butters "I was always scared of other people, and while trying to keep you at a distance I treated you awfully."
            butters "The one that should be looking for forgiveness here isn’t you, but it’s me…"
            butters "I won’t look for an excuse through my curse, or my succubus alternative personality. I know that it was me, and only me that treated you so poorly."
            butters "And for that, there’s no excuse, and I can only give you my absolute apology."
            butters "For too many years I’ve allowed that toxicity to build within me, and consume me. I’ve pushed away so many kind and generous people, just like Lily."
            lily "Huh? Y-Yeah..."
            butters "But, no more. Thanks to you, Lily and [playername], I think perhaps I’ve been able to escape my ‘curse’."
            butters "And that curse wasn’t becoming a succubus… That curse was being unable to let anyone into my life…"
            show zoe happy with d
            zo "Butters… I don’t know what to say…"
            show butters dresshappy with d
            butters "You don't have to say anything Zoe. I had some fine wine prepared for the very occasion of curing all the werewolves. Let’s drink the night away and celebrate!"
            mc "Now that’s what I’m talking about!"
            show lily embarrassed with d
            stop music fadeout 3.0
            lily "Uwah, a sudden party? I’m not socially prepared!"
            scene bg black with dissolve
            "…"
            scene bg buttershousenight with d
            play music augusta
            show zoeb:
                xpos 0
                ypos 30
            show zoe laughing:
                xpos 0
                ypos 30
            show lilyb w:
                xpos 400
                ypos 75
            show lily laughing:
                xpos 400
                ypos 75
            show butters dresslaughing:
                xpos 750
                ypos 30
            with dissolve
            everyone "Cheers!"
            show lily embarrassed with d
            lily "It’s so far past my bedtime… Maybe I should-"
            show zoe happy with d
            zo "Here Lil, how about another glass? We can keep going until the sun rises, either that or I’m on my ass!"
            show lily happy with d
            lily "Haha, I don’t think anyone will be on their ass tonight, right?"
            show butters dresshorny with d
            butters "Depends on what the sexiest man in the room has to say about that, haahaaa…"
            mc "Is that me?"
            if crystalballdayactivated == 1:
                jump cbmenu

            $ secretsunlocked += 1
            scene bg buttershousenight
            show slimegirl:
                xpos 700
                ypos 300
            with d
            if devilsex == 0:
                poyo "Yo, this party is lit."
                show devil horny:
                    xpos 150
                    ypos 10
                with d
                unknown "Heyy, you’re [playername], right? Phew, you were always so scary before, but now like, you’re pretty cute! *Hic*"
                mc "Hello, I don't believe we've met?"
                show devil happy with d
                devil "My name is like, ‘Devil’, and I think Butters is my mom, but I don’t know the details."
                mc "Poyo... what did you do?"
                poyo "I gave Devil this potion and she became a smoking hot anthropomorph. Isn’t it awesome?"
                show devil horny with d
                devil "Come on, [playername], come and give me some tummy rubs in the guest bedroom."
                "The bunny girl takes my hand and strings me along in front of everyone else. I can even hear some light cheers from the crowd."
                "Fortunately, I’m just drunk enough to think ‘fuck it, time to get some bunny pussy.'"
                "You found a secret scene! Requirements met: Bang the bunny."
            elif devilsex == 1:
                poyo "Yo, this party is lit."
                show devil horny:
                    xpos 150
                    ypos 10
                with d
                devil "Heyy, [playername]! *Hic* We really gotta meet like this more often!"
                mc "Oh Devil, you appear to have transformed, was that your doing, Poyo?"
                show devil happy with d
                devil "Yup, I have a special party pass, hehe! *Hic*"
                mc "Oh no. This isn’t the first time you’ve ever had alcohol, is it?"
                show devil horny with d
                devil "How about you come and give me some tummy rubs in the guest bedroom, y’know, just like old times? *Hic*"
                mc "You know, it might be a good idea if I did, just to keep an eye on you."
                "The bunny girl takes my hand and strings me along in front of everyone else. I can even hear some light cheers from the crowd."
                "Fortunately, I’m just drunk enough to think ‘fuck it, time to get some bunny pussy.'"
            scene bg black with dissolve
            play sound movement
            scene devilb sex
            show devil sex1
            with d
            stop music fadeout 10.0
            "Devil falls down on her back and shows me what she means. I can recognize what she’s referring to: legs-up missionary."
            "She looks up to me with heated captivation, while her hand slyly moves to her privates, and begins to rub her supple folds."
            "And they really are supple. I'd dare say this Bunny's body is unquestionably perfect. Is this perhaps a consequence of the potion and transformation associated with it?"
            devil "Is this good? I am making myself wet and ready to take you."
            mc "Very good, keep going."
            if devilsex == 0:
                devil "It’ll be my first time, so I want to make sure I’m ready."
            else:
                devil "It's easy to get wet with you. You are very sexy."
            play music sex1 fadein 10.0
            "My cock rapidly stiffens as the two us watch each other masturbate. The pleasure seems rather new to Devil as she fidgets and squirms in reaction to the pleasure."
            "Her wide eyes are intensely locked onto my erection; she really enjoys watching the way it moves."
            "Her pussy gradually gets wetter as her fingers rub up and down its length. Soon, and almost impatiently, her hand withdraws. A trail of wetness connects her fingers signalling that she's wet enough."
            devil "Okay… Put it in me! I want to feel really good."
            "She lays back further into the bedding, raising her rump a little further. Her tail twitches with anticipation."
            "I nod and get into position, my cock fully erect and prepared to give this bunny the fuck of a lifetime."
            "Shuffling closer, I align my shaft with her tight fluffy labia and gently press the tip forward."
            "She’s incredibly wet, wetter than I’d expect considering we haven’t been going long, but regardless she’s still immensely tight."
            play sound cum
            "My first push inwards is met with some slight resistance, and because of the wetness I slip off and grind against her clit."
            devil "Oohh… Did it start? That felt good!"
            mc "Not quite yet. You’re really tight, Devil."
            devil "Mmm, well, I’m only a small little bunny."
            play sound cum
            show devil sex2 with d
            "With a second, more carefully aligned push, I manage to pop inside and sink in with relative ease. But the intense tightness remains like a fist's grip around my cock."
            "Her hands desperately grasp the bedsheets for support. Initially you suspect she may be in pain, but her face is showing absolute pleasure as she throws her head back and moans."
            devil "I want it, I want more! Please give me more!"
            play ambience sex fadein 5.0
            "Her pussy twitches as I pull out, and as I thrust forwards it almost feels like I’m sucked back in by the tightness."
            "And again, and again, she gently eases around my girth and it becomes even more pleasureful for the two of us."
            "The hilt of each thrust is so comfortable as well; her soft fur feels fantastic as it brushes against my skin. I’ve never wanted to treat something so soft so rough."
            "The lust gradually takes control of me as I begin pounding into her bunny butt at a steady pace. Her squelching, wet pussy is so tight it threatens to make me cum if I were to ever speed up."
            devil "Haaahhh… This’s sooo good… Rub my tummy too!"
            "While that may be the strangest request I’ve ever had during sex, my one-track mind doesn’t even double take as one of my hands begins to caress her sensitive tummy, while I pump in and out of her pussy."
            "She trembles at the sensation of sex and rubbing, her insides gripping particularly tightly as if she just achieved an orgasm."
            devil "Haahhh, yesss… I looove youuu, soooo muuuuch…"
            "Her pussy feels so good right now, it’s like I’m in heaven. A heaven full of anthropomorphic girls I can fuck to my heart’s content."
            "The pressure of my orgasm signals its imminence. I grunt and try to hold back a little longer to relish each and every second with my lover."
            "But eventually, her pussy is just too pleasureful, and as my body gives in, I decide to push to my limit and rut her as fast as I can."
            devil "Hooohh my gosh, oh my gosh! Aaaahhh!"
            play sound cum
            show devil sex3 with cum
            play sound cum
            show devil sex3 with cum
            "An eruption of cum launches from my tip filling up the tiny bunny’s pussy and womb almost entirely."
            play sound cum
            show devil sex3 with cum
            play sound cum
            show devil sex3 with cum
            "The two of us continue to fuck passionately throughout the duration of my orgasm. Shivers of pleasure running down my spine with each deep thrust in my hyper-sensitive state."
            devil "Haaahhh… My eyes are swimming, haahhh… Everything went all white and fuzzy, aheh…"
            mc "Me too, Bun, me too…"
            show devil sex4 with d
            stop music fadeout 3.0
            stop ambience fadeout 3.0
            "After filling her to the brim, I gradually come to a stop and pull out."
            "A few droplets of cum ooze down her pristine white fur, almost entirely camouflaged if it weren’t for her cute pink pussy serving as contrast."
            "With a deep breath, I drag myself to her side and my bunny lover takes the initiative to cradle me close in a cozy embrace."
            scene bg black with dissolve
            "Soon enough, we fall asleep while cuddled."
            "In the morning, I find myself waking up next to an actual white bunny snoozing on a pillow."
            "Well, that was weird."
            if devilsex == 0:
                $ secretsunlocked += 1
            else:
                pass
            $ devilsex = 1
            jump altmorning
        "Back":
            jump worldmap
