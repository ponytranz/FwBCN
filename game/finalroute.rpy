    ## if every route is complete
    ## if living with Butters
label finalroute:
    if livingwithbutters == 1:
        scene bg buttershouse with dissolve
        "After I do my daily routine, I receive a magic mail from Moxie."
        "She wants to see me, preferably ‘now’. It’s probably because her interview with Selene is today. I should go give her some emotional support."
    else:
        scene bg moxiebedday with dissolve
        "After I do my daily routine, I can hear Moxie is still in the main room rambling to herself."
        "Her interview with Selene is today, so I’ll give her some emotional support."
        "Although, she’s taking it surprisingly well; she doesn’t seem nervous at all."
    play ambience ambienceday
    scene bg moxiewagonday with dissolve
    $ finalroute = 1
    "I pop my head into the main room of the wagon to spot Moxie staring outside of the window and towards the castle."
    play music wagon fadein 3.0
    show moxie shocked with dissolve
    moxie "Ah, [playername], it’s you!"
    mc "Observant as ever, Mox!"
    show moxie shy with dissolve
    moxie "There’s something weird going on. I don’t know how to describe it, but lately I’ve been feeling myself less and less."
    mc "Is the stress of the interview getting you down? I bet it’s not easy to find out how powerful you are, and what those responsibilities entail."
    show moxie neutral with dissolve
    moxie "Perhaps, but… something doesn’t quite feel right… I feel like there’s more to this hidden power inside me, something that feels sinister and dangerous..."
    mc "That’s why Selene is going to tutor you, so you can control your power, right?"
    stop music fadeout 20.0
    stop ambience fadeout 10.0
    show moxie shy with dissolve
    moxie "Selene… Did you have sex with her?"
    mc "Uhh, wow Moxie, that’s quite the question."
    mc "I’ve only seen her twice… I’m not that much of a stud, y’know."
    show moxie neutral with dissolve
    moxie "{b}[playername]!{/b} Did you or did you not have sex with Selene?"
    mc "I really shouldn’t say… I mean she’s a princess, I don’t want to create a controversy."
    show moxie shocked with dissolve
    moxie "Oh my goodness, and you’ve also fucked Lily and the other ‘elements’…"
    moxie "Lily, Honeycrisp, Ruby, Riku, Cream and Butters… And now Selene, they’re all taken care of."
    show moxie shy with dissolve
    moxie "So that just leaves Aurora… Is that enough? No… She’s probably too powerful…"
    moxie "I can’t believe this happened. You were mine and Penelope’s little pet project, but I never anticipated you going and fucking one of the princesses."
    moxie "You’ve single-handedly made my job a billion times easier."
    mc "What are you talking about? Why are you acting so weird, Moxie?"
    show moxie angry with dissolve
    moxie "Hmm… I’ve been a little irate all day, I’ve been sensing a strange magic from both the royal sisters."
    moxie "I guess it’s because you’ve fucked Selene, but… I’m feeling that same magic from Aurora too…"
    show moxie shocked with dissolve
    play music lips fadein 10.0
    moxie "No… Don’t tell me…"
    moxie "[playername], have you had sex with {i}AURORA?{/i}"
    "I try to feign an answer, or even an excuse, but Aurora’s spell prevents anything related to the event from escaping my mouth."
    show moxie angry with dissolve
    show black with dissolve:
            alpha 0.5
            parallel:
                0.30
                alpha 0.5
                repeat
            parallel:
                0.5
                alpha 0.475
                repeat
    moxie "You can’t talk about it…? You DID fuck her!"
    mc "It doesn’t matter…"
    show moxie mystery with dissolve
    moxie "..."
    moxie "I’ve won…"
    play sound thunder1
    show bg thirdwagon1 with cum
    moxie "I’ve {b}WON{/b}!"
    play sound thunder2
    show moxie death with cum
    moxie "Ahahaah, ahhahahaa, it was so easy! I can’t believe it!"
    play sound thunder2
    show moxie md2 with cum:
        xpos 640 ypos 720
        linear 0.5 xpos 640 ypos 720
        linear 0.5 xpos 641 ypos 721
        linear 0.5 xpos 639 ypos 719
        alpha 0.9
        parallel:
            0.30
            alpha 0.8
            repeat
        parallel:
            0.5
            alpha 0.9
            repeat
        repeat
    moxie "You were designed to be nothing more than a pawn to create some loyal underlings, but you ended up winning the game by yourself!"
    mc "What are you talking about Moxie? What game?"
    play sound thunder2
    show moxie md3 with cum:
        alpha 0.9
        xpos 640 ypos 720
        linear 0.4 xpos 640 ypos 720
        linear 0.4 xpos 643 ypos 723
        linear 0.4 xpos 637 ypos 717
        parallel:
            0.30
            alpha 0.9
            repeat
        parallel:
            0.5
            alpha 0.8
            repeat
        repeat
    moxie "Enough with this Moxie bullshit, it’s time for me to reveal my true form!"
    play sound transition1
    stop music fadeout 1.0
    show black with dissolve:
        alpha 0.9
        xpos 640 ypos 720
        linear 0.4 xpos 640 ypos 720
        linear 0.4 xpos 643 ypos 723
        linear 0.4 xpos 637 ypos 717
        parallel:
            0.30
            alpha 0.9
            repeat
        parallel:
            0.5
            alpha 0.8
            repeat
    scene bg black with dissolve
    "..."
    show bg thirdwagon1 with s
    pause 1.0
    show morrigan silhoutte with dissolve
    pause 0.5
    unknown "I’m the new Queen of Arcadia!"
    ##
    play sound thunder2
    play music morrigan
    show morrigan happy with cum
    morrigan "You can call me, Morrigan!"
    morrigan "Ahh, this form is so much more fitting of a Queen, unlike that sickly blue mare."
    mc "W-What, Moxie? What’s going on?"
    show morrigan neutral with dissolve
    morrigan "Ohh, I am so much more than your ‘Moxie’, my underling."
    mc "Are you the same person? Or is this some kind of magical trickery?"
    show morrigan happy with dissolve
    morrigan "Darling, do calm down. She and I are one and the same. I just had to don dear ‘Moxie’ as a disguise."
    mc "I don’t understand, what’s going on?"
    show morrigan neutral with dissolve
    morrigan "My faithful servant, bear witness to my ascendency to the throne!"
    show morrigan death with dissolve
    morrigan "With this spell, I shall activate the seed of obedience you planted into each and every mare you’ve slept with!"
    morrigan "Follow me and obey, loyal pets! You’re now under the rule of Queen Morrigan, Penelope, and [playername] until further notice!"
    play sound thunder2
    scene bg castlethrone with cum
    show aurorab dress
    show aurora neutral
    with dissolve
    pause 0.5
    show aurora cneutral with morriganspell
    scene bg selenebedroom with dissolve
    show selene satisfied with dissolve
    pause 0.5
    show selene cneutral with morriganspell
    scene bg dusklightbedroom with dissolve
    show lilyb
    show lily laughing
    with dissolve
    pause 0.5
    show lily cshy with morriganspell
    scene bg boutiquekitchen with dissolve
    show ruby happy:
        xpos 250
        ypos 30
    show melody happy:
        xpos 750
        ypos 80
    with dissolve
    pause 0.5
    show ruby cneutral with morriganspell
    show melody csadistic with morriganspell
    scene bg thirdwagon2 with dissolve
    play ambience ambiencerain
    ## show Aurora, Luna, Lily and Ruby turning their eyes green
    "Harrowingly the atmosphere in Arcadia changes almost immediately, rain starts dribbling down from increasingly grey clouds."
    show morrigan evilhappy with dissolve
    morrigan "Oh my, it started raining… Usually Aurora controls the weather, so that means you really did fuck her, impressive!"
    mc "What are you talking about? What does this have to do with the mares I’ve slept with?"
    show morrigan neutral with dissolve
    morrigan "Isn’t it obvious? When you arrived in Arcadia via my spell, I cast several powerful beguilement spells on you."
    morrigan "The first was to make you almost irresistibly attractive and overwhelmingly arousing to many a mare."
    mc "Hmph, that certainly explains my absurd luck…"
    show morrigan happy with dissolve
    morrigan "The second spell… any mare you sleep with becomes {i}my slave{/i}."

    menu:
        "Slave? That’s awful!":
            show morrigan laughing with dissolve
            morrigan "Oh it’s not so bad, because they hopelessly enjoy each and every moment they serve under me."
            morrigan "They’ll absolutely beg to be under my command, and would actively fight against any attempts to break those shackles."
        "I’m glad I could have helped, my Queen.":
            show morrigan neutral with dissolve
            morrigan "I would never have achieved this power so soon without you, my loyal servant."
    show morrigan evilhappy with dissolve
    morrigan "You were never supposed to sleep with royalty, my plan was to infiltrate Arcadia from the inside as Moxie. But I’d say there’s been a change of plan."
    ## penelope appears
    play sound open
    "Sprinting with urgency, Penelope pushes the wagon door open and stumbles in panting and dripping wet from the rain."
    show penelope neutral with dissolve:
        xpos 850
        ypos 65
    penelope "Your majesty! I came as soon as I saw the rain! Has It happened? Have we done it?!"
    show morrigan neutral with dissolve
    morrigan "Calm down Penelope, thanks to the success of [playername], we have all the time in the world to take over the city."
    show penelope shocked with dissolve
    penelope "Oh my goodness, I told you that using Mox- uhh… How much does [playername] know?"
    mc "What’s going on? Penelope? Mox- Morrigan? You two are both in on this?"
    show morrigan laughing with dissolve
    morrigan "[playername], meet Penelope my loyal spymaster, and current second in command of the Morrigan empire."
    play sound genericmagic
    show penelope chappy with morriganspell
    penelope "Pleasure to finally meet you, [playername]."
    penelope "Phew, feels good to finally break that disguise."
    show morrigan evilhappy with dissolve
    morrigan "Even with my pride, I’ll admit that the majority of the success in this plan can be attributed to both you and her."
    show penelope chappy with dissolve
    penelope "Anything for you, your majesty."

    $ persistent.morrigan = 1
    scene bg black with dissolve
    stop music fadeout 1.0
    stop ambience fadeout 1.0

    menu:
        "Would you like to save?"
        "Yes":
            call screen save
        "No":
            pass
    morrigan "So, [playername]. I still have use for someone such as yourself."
    play ambience ambiencerain
    show bg thirdwagon2 with dissolve
    show morrigan evilhappy with dissolve
    morrigan "I am offering you a position as the third in my command, do you accept?"
    menu:
        "Of course, your majesty…":
            show morrigan happy with dissolve
            morrigan "Wonderful, with everything settled, I believe we have a meeting with the Royal Sisters."
            show penelope claughing with dissolve:
                xpos 900
                ypos 65
            penelope "Good job newbie, you’ll be rewarded greatly under servitude of our new Queen."
            mc "I sure hope so…"
            stop music fadeout 1.0
            stop ambience fadeout 1.0
            scene bg black with dissolve
            jump badend
        "No way! I refuse!":
            pass
    play music lips fadein 10.0
    show morrigan angry with dissolve
    show penelope cangry with dissolve:
        xpos 900
        ypos 65
    penelope "Refuse? How dare you, that’s our Queen you’re talking to!"
    mc "I don’t know who you are Morrigan, but you’re definitely not the Moxie I know…"
    mc "There’s no way I’ll be part of this enslavement and entrapment of society!"
    play sound thunder1
    show bg thirdwagon3 with cum:
        xpos 640 ypos 720
        linear 0.5 xpos 640 ypos 720
        linear 0.5 xpos 641 ypos 721
        linear 0.5 xpos 639 ypos 719
        repeat
    show black:
            alpha 0.1
            parallel:
                0.30
                alpha 0.1
                repeat
            parallel:
                0.5
                alpha 0.15
                repeat
    show morrigan evilhappy with dissolve
    morrigan "*Giggles* And what are you going to do about it, human?"
    morrigan "You truly are powerless, why don’t you behave yourself and listen to the woman that brought you into this world?"
    mc "No… I couldn’t… Knowing I’ve done this to all my friends, all the people that have trusted me…"
    mc "And you two, I trusted you! You were my first friends, and you both lied to me!"
    show morrigan happy with dissolve
    morrigan "*Giggle* Friends? If you join me, you’ll have a harem of every mare you could possibly want, including your so called ‘friends’."
    morrigan "They’ll even act just as before; you’ll get to live your absolute dream."
    show morrigan laughing with dissolve
    morrigan "All you have to do is join me!"

    menu:
        "I’ll never join you!":
            pass
        "A harem? Alright, I’ll join you…":
            show morrigan evilhappy with dissolve
            morrigan "Wonderful, with everything settled, I believe we have a meeting with the Royal Sisters."
            show penelope claughing with dissolve
            penelope "Good job newbie, you’ll be rewarded greatly under servitude of our new Queen."
            mc "I sure hope so…"
            jump badend
    ### bad end

    mc "Enough of this, I’m leaving!"
    play sound open
    stop music fadeout 4.0
    "With a huff, I leave the wagon…"
    scene bg black with dissolve
    pause 0.5
    scene bg thirdwagon2 with dissolve
    show penelope cneutral with dissolve:
        xpos 250
        ypos 50
    penelope "Hmph, why are you even bothering with this useless pawn, your majesty? He’s served his purpose and can be disposed of now."
    penelope "Don’t tell me you’ve let yourself become influenced by your own spells."
    show morrigan laughing with dissolve:
        xpos 750
        ypos 0
    morrigan "*Giggles* Perhaps... They were powerful spells, I think it’d be nice to have him around, don’t you?"
    show penelope cangry with dissolve
    penelope "Tch… I have no strong opinion on the matter, I can only offer suggestions…"
    penelope "But you can see why I never let him fuck me, that’s for damn sure…"
    show morrigan evilhappy with dissolve
    morrigan "He has nowhere else to go. When he sees the state of his friends, he’ll come back, I’m sure of it..."
    morrigan "But for now, I believe I had an interview with the Royal Sisters, yes?"
    show penelope cneutral with dissolve
    penelope "Right you are, your majesty."

    scene bg black with dissolve

    ### worldmap 1
    show bg cworldmapnoui with s
    "Stepping out the wagon and into the world, rain relentlessly hits my cold skin."
    "Unsure where to go, or what to do. The world feels so strange and alien."
    "I need to meet my friends to see if they’re okay, but if it’s as bad as Morrigan said, I may have doomed Arcadia…"
    jump cworldmap

label worldmapcode:
    screen cworldmapscreen():
        imagemap:
            ground "bg cworldmap.png"
            hover "bg cworldmaphover.png"

            hotspot (0, 300, 290, 210) clicked Jump("clibrary")
            hotspot (895, 305, 140, 140) clicked Jump ("cwagon")
            hotspot (380, 190, 107, 100) clicked Jump ("cfarm")
            hotspot (480, 250, 90, 90) clicked Jump ("cbakery")
            hotspot (575, 360, 75, 75) clicked Jump ("cbar")
            hotspot (200, 225, 90, 90) clicked Jump ("cforest")
            hotspot (1130, 270, 150, 175) clicked Jump ("cboutique")
            hotspot (830, 180, 175, 140) clicked Jump ("ccastle")

            hotspot (920, 0, 108, 125)  clicked Jump("ctodolist")
            hotspot (1025, 0, 138, 125)  clicked Jump ("cinventory")
            hotspot (1165, 0, 108, 125)  action ShowMenu("preferences")
        text "{b}[monies]{/b}":
            xalign 0.22
            yalign 0.0225
        text "{b}Day [days]{/b}":
            xalign 0.065
            yalign 0.0225
label cworldmap:
    if cfarcom == 1 and cboucom == 1 and cbarcom == 1 and cbakcom == 1 and clibcom == 1:
        jump treemeeting
    hide screen todolist with dissolve
    play ambience ambiencerain fadeout 1.0
    label cworldmap1:
        scene bg cworldmapnoui with dissolve
        call screen cworldmapscreen with dissolve
label ctodolist:
    show todolist with dissolve
    "... This list, was it Morrigan's?"
    hide todolist with dissolve
    call screen cworldmapscreen with dissolve
label cinventory:
    show bg cworldmapnoui with dissolve
    menu cinventorymenu:
        "Inventory":
            jump cinventorymenu
        "Moxie's Satchel":
            jump cinventorymenu
        "[chocolates] Chocolates" if chocolates >= 1:
            jump cinventorymenu
        "[roses] Roses" if roses >= 1:
            jump cinventorymenu
        "City Permit" if libraryvisit3 == 1:
            jump cinventorymenu
        "Hooks and Ropes" if rope == 1:
            jump cinventorymenu
        "Leather Armor" if leatherarmor == 1:
            jump cinventorymenu
        "Scimitar" if scimitar == 1:
            jump cinventorymenu
        "Back":
            jump cworldmap1

    #### Butters meet
label ccastle:
    if cforvisit == 1:
        "I'll save you Moxie, just you wait..."
    else:
        "I could give up and find Morrigan, but... There must be some way out of this nightmare!"
    jump cworldmap1
label cwagon:
    show bg thirdwagon2 with dissolve
    if crystalballactivated == 1:
        "Should I return to the real world? (Crystal Ball)"
        menu:
            "Should I return to the real world? (Crystal Ball)"
            "Yes":
                $ crystalballactivated = 0
                jump cbmenu
            "No":
                jump cworldmap1
    else:
        "The wagon is empty."

    jump cworldmap1
label cforest:
    if cforvisit == 1:
        "It'd be a waste of time to go back to Butters right now, I've got a sex quota to meet."
        call screen cworldmapscreen with dissolve
    $ cforvisit = 1
    scene bg cforest with dissolve
    "It's a long walk to the forest, but fortunately the trees provide cover from the rain."
    "I arrive at the cottage and knock on the door, Butters promptly answers."
    stop music
    play ambience raindistantthunder
    scene bg cbuttershouse with dissolve
    show butters dresshappy with dissolve
    play music butters fadein 10.0
    butters "Hello [playername]. Miserable weather, I wonder what’s going on."
    mc "B-Butters? You’re alright!"
    show butters dresslaughing with dissolve
    butters "Mhm, a little rain won’t hurt me [playername], I’m a tough bunny!"
    mc "No, I mean… You’re not brainwashed, are you?"
    show butters dresssurprised with dissolve
    butters "Brainwashed? What are you talking about? It’s not raining so hard that it’s seeping through my skull."
    mc "Sheesh… I mean Morrigan said the royal sisters and ‘elements’ had been brainwashed, but you seem fine!"
    show butters dressangry with dissolve
    butters "Morrigan? That’s bad news… what you just said, is it true?"
    mc "Yeah, but you seem fine… I’m not really sure what’s going on…"
    show butters dresssurprised with dissolve
    butters "Jesus, shit! You son of a bitch! Morrigan is an evil morphling that I helped defeat in the past."
    show butters dressangry with dissolve
    butters "Lily, myself, and the other elements repelled her army a few years ago when they tried to take over Arcadia."
    butters "Moments earlier I sensed a dark magic… I overlooked it as my succubus side playing up, but that must have been the power that was trying to brainwash me."
    mc "Maybe, but why didn’t it affect you?"
    show butters dressneutral with dissolve
    butters "That’s an easy one, I’m at least temporarily immune to that kind of dark magic thanks to the Dewblossom potion we brewed recently."
    mc "I see… That means everyone else really is screwed then. We should make a potion to save them too!"
    show butters dressangry with dissolve
    butters "Hm... We don’t have time to collect the ingredients, and I only have enough for one person left. If Morrigan’s magic has already enslaved the royal sisters, we have less than a day before she’ll have siphoned all their magic…"
    butters "They’ll be weaker than even you or I if we wait too long… they’ll be killed, or worse: reduced to breeding vessels…"
    mc "Yikes, we have to save them!"
    show butters dresssad with dissolve
    butters "Hmm… Think Butters, think…"
    butters "[playername], how did Morrigan brainwash everyone? I don’t understand how she could get away with this."
    mc "She used me… She cast some type of magic on me that caused everyone I had sex with to become a slave to her."
    show butters dressneutral with dissolve
    butters "I can’t believe you slept with everyone, b-but that’s not really the point… That explains how the royal sisters didn’t notice…"
    butters "It’s such a subtle spell, but it’s so powerful because it activates internally."
    mc "What are we gonna do Butters? I have this cursed dick and I think I doomed Arcadia because of it!"
    show butters dresssurprised with dissolve
    butters "Cursed… dick? Just like I had a cursed... uhm, pussy…? That gives me an idea!"
    butters "I think we have one chance. It might not work, but it’s the least we can do to try and save Arcadia."
    butters "Do you remember when I said a potion of Gelatine and Folium Polypus would turn someone into a nymph?"
    mc "Vaguely, but the Dewblossom reversed that effect, right?"
    show butters dresshappy with dissolve
    butters "Precisely, that ‘reversed’ potion removed the ‘sexual curse’, which caused me to drain life from anyone I fuck."
    butters "But more than that, it gave me an immunity to the brainwashing spell as well. As we've already deduced, the potion cures both!"
    butters "[playername], I think the only choice we have right now is for you to also drink the potion that cured me!"
    "Butters, who has a habit of always making two servings per brew, hands me her last ‘Succubus Cure’ potion."
    mc "I don’t understand, what’s the point in removing this spell? That’ll remove the spell from me, but it won’t fix anyone else."
    show butters dressneutral with dissolve
    butters "Well [playername]… This potion cured me, right? But how long has it been since I digested it? Quite a while! The potion remained in my system and cured me of both curses."
    butters "My theory to explain this phenomenon is that when you digest this potion, it has a constant cleansing effect around the genitals."
    butters "A powerful cleansing effect too! We had sex quite a few times and I'm completely fine."
    butters "So... if you drink the potion you'll also get a cleansing effect around your genitals, and then if you have sex with a girl suffering from a sexual curse or spell, you might just cure them from the residual power of the potion."
    mc "Your theory is interesting, but why didn't {i}you{/i} cure me when we had sex then?"
    mc "If this cleansing effect idea is true, then you should have cured me."
    butters "Heh, I like your rebuttal, but I think it works exactly because you're male and can implant 'genetic material' internally."
    butters "I, as a female, am unable to spread the effect into you because my sexual fluids were only against the skin of your penis."
    #butters "Specifically… The potion we brewed has an effect on sexual fluids. The reason I don't drain life anymore is because my natural lubrications were altered, and the reason you didn't brainwash me is because your brainwashing semen was 'neutralised'."
    butters "You'll need to cum inside each girl one more time, hopefully your semen will carry enough of the potion’s effect and save the girls in the same way it saved me."
    butters "Considering the potion’s effect has stayed within me long enough to prevent my brainwashing, I’m confident it’ll work."
    mc "Holy bunnies Butters, you’re a genius!"
    show butters dresslaughing with dissolve
    butters "Heh! All my alchemy experience was useful after all."
    show butters dresshappy with dissolve
    butters "I bet it won’t be too hard convincing each of the elements to sleep with you again, if they were brainwashed by you, they’ll be drooling over your cock."
    mc "Right… What a beautiful irony that I’ll be curing people with the instrument of their demise."
    show butters dresslaughing with dissolve
    butters "No need to be poetic, you’re just doing more fucking."
    "I take a deep breath before swallowing the potion. It’s clumpy and disgusting; the taste and smell are foul."
    "I do think the potion is taking effect though, but it’s hard to say for sure. I can feel a strange tingle in my loins, as if a weight is being lifted."
    mc "Did it work?"
    show butters dressneutral with dissolve
    butters "Hm… Only one way to find out, you need to go and fuck the other elements."
    mc "Who and what are these ‘elements’ I keep hearing about?"
    show butters dresshappy with dissolve
    butters "The Elements of Har’Mony, of course!"
    show butters dresssad with dissolve
    butters "Although we haven’t been active for almost five years now, so I’m not surprised you haven’t heard about it."
    butters "Myself, Lily, Honeycrisp, Ruby, Riku and Cream."
    show butters dresshappy with dissolve
    butters "We’re blessed guardians of Arcadia, designated by Aurora and Selene themselves."
    butters "When even their power is not enough, we six can combine to vanquish any evil."
    butters "I’m the element of fire, Lily is lightning, Honeycrisp is earth, Ruby is water, Riku is air and Cream is ice."
    mc "Wow! Do you guys have elemental powers based on those?"
    show butters dresslaughing with dissolve
    butters "Nah, they’re just fancy words that vaguely correspond to our personalities! It was Riku's idea because she wanted us to sound cooler."
    show butters dresshappy with dissolve
    butters "Deep down in our hearts is a power that can be accessed if we combine, Lily is the conduit for that power."
    butters "Together, we easily defeated Morrigan and her army in the past when they tried to invade Arcadia. It was such a one-sided affair it was almost pitiful, and Morrigan was let go."
    show butters dressneutral with dissolve
    butters "Now she’s returned… Well, we’ll need to finish her off properly this time, and with your help. Ohhh, I hope this works!"
    butters "You need to sleep with each and every element, explain to them what happened as quickly as you can, and tell them to meet with Lily; then we can coordinate our next move."
    show butters dresslaughing with dissolve
    butters "Hehe, you’ll be an honorary element of cum!"
    mc "I think I’ll pass on the title, but I’ll absolutely get to work curing everyone."
    show butters dresshappy with dissolve
    butters "Perfect, there’s no time left to talk. Try to take no longer than two hours fucking everyone. Let’s say 10:30am, let’s all meet at the tree at 10:30am!"
    butters "There’s no one else better suited for this job than you [playername]! Go, go, go!"
    mc "I’ve been practicing for this moment ever since I arrived in Arcadia, I’ll save this city in the best way I know!"
    "Butters nods and I sprint out of the cottage."
    stop music fadeout 3.0
    scene bg cforest with dissolve
    "I hope this works!"
    scene bg black with dissolve
    ### small scene of Morrigan siphoning the Princesses power, Penelope and Morrigan arguing about you, and then a lone scene of Penelope wondering why Morrigan doesn’t love her
    "Meanwhile in the castle…"
    play music morrigan
    play sound thunder2
    show bg ccastlethrone with cum
    show morrigan laughing with dissolve
    morrigan "Call me mistress, I like the sound of that."
    show aurorab:
        xpos -200
        ypos 50
    show aurora cneutral:
        xpos -200
        ypos 50
    with dissolve
    aurora "Yes mistress, anything for you mistress."
    show selene cneutral with dissolve:
        xpos 775
        ypos 50
    selene "Drain all my power dry mistress, I’m nothing but a worthless toy for you."
    scene bg ccastlethrone with dissolve
    show penelope chappy with dissolve:
        xpos 750
        ypos 50
    penelope "Hehehe, they’re so pathetic! What are you going to do with them after they’re drained?"
    show morrigan evilhappy with dissolve:
        xpos 250
        ypos 0
    morrigan "Sexually? I think it’d be more satisfying to leave these two to the drones when I’m done."
    morrigan "I wonder just how many cocks these royal whores can take at once… Hehe, it’d be more fun masturbating to that show than having them pleasure me."
    show penelope claughing with dissolve
    penelope "Perfectly degrading for old royalty, I love it."
    show penelope chappy with dissolve
    penelope "What about you my Queen? Have you decided on a mate yet? With magic, I’d be perfectly happy to pro-"
    show morrigan angry with dissolve
    morrigan "No, Penelope. I’ve told you this before, you will not be my mate."
    show penelope csad with dissolve
    penelope "B-But my Queen, I’ll do anything for you! Why can’t we sleep together like we used to?"
    show morrigan shy with dissolve
    morrigan "That was different… You were just supplying me with love to grow my power."
    show penelope cshy with dissolve
    penelope "Tch, this is because of [playername], isn’t it?"
    show morrigan sad with dissolve
    morrigan "You know a male is a far better fit for a Queen such as myself, his magically enhanced semen was plentiful and gave me so much love."
    morrigan "And he’d make a perfect mate for breeding, I do hope he returns sometime…"
    show penelope cangry with dissolve
    penelope "Damnit Morrigan, just brainwash him!"
    show morrigan angry with dissolve
    morrigan "No, brainwashing is for slaves, not lovers or true devotees such as yourself, Penelope. You already know that."
    penelope "But he won’t come back, why don’t you understand that he only liked Moxie? How could you fall for your own love spells?"
    play sound thunder
    show morrigan death with cum
    morrigan "Silence Penelope, I have NOT fallen under the influence of my love spells. I will not put up with such nonsense from you."
    show morrigan angry with dissolve
    morrigan "We both know he’s a non-threat, regardless of whether he returns or not."
    morrigan "If he bothers you so much, then go and bring him here yourself, at least you'll be useful to me then."
    hide penelope with dissolve
    "Penelope grunts and storms out of the throne room, leaving Morrigan to siphon the power of the sisters."
    stop music fadeout 3.0
    scene bg ccastle with dissolve
    show penelope csad with dissolve
    penelope "Eugh… Morrigan… Why won’t you love me?"
    penelope "I-I love you so much… My Queen, without you I’m nothing…"
    penelope "Maybe that [playername] guy was onto something when he told me I was loving in the wrong way… Maybe I am too obsessed with the Queen..."
    penelope "I wonder what he’s doing now? How does he feel knowing he’s been betrayed and lost everything?"
    penelope "I adore Morrigan, but she has no empathy…"
    scene bg black with dissolve
    "..."

    ###
    show bg cworldmapnoui with dissolve
    "I should save Lily next, although saving anyone is important right now."
    jump cworldmap
    #### Lily meet, with and without meeting Butters, and sex.
label clibrary:
    if clibcom == 1:
        "There's no time to visit Lily again, I need to continue my sex conquest!"
        call screen cworldmapscreen with dissolve
    play ambience raindistantthunder fadein 3.0
    if clibvisit == 0:
        show bg ctree with dissolve
        "I hammer on the library door in an attempt to get a response, but to no avail."
        "I try opening the door and it’s unlocked! Penelope must have been in such a rush that she didn’t even bother locking it."
        show bg cdusklightbedroom with dissolve
        "I rush upstairs and into Lily’s bedroom to see her nonchalantly on her bed browsing the web."
        "Nothing seems out of the ordinary, that is until she turns to face me."
        show lilyb
        show lily chappy
        with dissolve
        lily "Ohh, master! Thank you so much for blessing me with this gift, my eyes have truly been opened to the beauty of our new Queen, Morrigan."
        mc "Damnit… I feel so bad for getting you caught up in this mess."
        show lily chorny with dissolve
        lily "Have you come to make me your filthy slut again?"
        lily "I’d love for you to fill me up with your cum, maybe you can make me one of your breeding whores so we can strengthen Morrigan’s army?"
        "She’s still eager to fuck…"
    else:
        show bg ctree with dissolve
        "I enter into the library again, the door still uncaringly unlocked, although it's my fault for not locking it behind me this time."
        show bg cdusklightbedroom with dissolve
        "I return upstairs to Lily's room where I catch her masturbating."
        show lilyb
        show lily chorny
        with dissolve
        lily "M-Master! You've returned, I was just thinking about you!"
    if cforvisit == 1:
        mc "That's good, I was just thinking about you too, how about I help you out there?"
        show lily laughing with dissolve
        lily "Oh my gosh, yes!"
    else:
        $ clibvisit = 1
        lily "Wanna do the naughties together?"
        "What the heck am I supposed to do? Is Arcadia doomed? Should I just give up?"
        mc "I'm gonna head out, sorry Lily."
        jump cworldmap
    show lily csex1 with dissolve
    play music sex1
    "The brainwashed mare jumps up from the bed and leans over a counter, wiggling her dripping crotch in my direction, her tail fluttering back and forth excitedly."
    lily "I want you to bend me over and fuck me silly, master!"
    "Watching such a lustful display causes me to easily get an erection. I didn’t even have to ask, or order her, she just assumed the position."
    mc "Very well, I’ll make you my personal breeding slut."
    "I close the distance and prod the tip of my cock against her wet labia, not willing to waste any more time than I need to."
    lily "Mmphh, your big, powerful cock is going to breed a perfect army for our Queen!"
    play sound cum
    show lily csex2 with dissolve
    "I thrust my hips forward, plunging my cock into the depths of her tightness in an instant."
    "Lily coos and starts to rhythmically grind her butt back and forth playfully, as her pussy eases to the girth of my cock."
    play ambience sex fadeout 2.0
    play sound spank
    "But I’m not interested in being playful right now. With an admonishing spank on her ass, she yelps and I start to pound her pussy."
    lily "Hahh! S-So eager master! I hope my t-taaaaahhh, ahhh!"
    "The pleasure overrides her ability to talk, any attempt at words is replaced with a lustful moan."
    lily "Gaahh, M-Mahhhstarr is so roughhh todayyyhhh!"
    "I just need to cum in her to stop this brainwashing, and as usual Lily's tight pussy easily brings me close."
    "My cock grows tighter and harder as it throbs in her clenching pussy."
    "She’s been indulging in light orgasmic pleasure repeatedly during the entire session. Her squelching pussy is dripping with an overabundance of juices and lust."
    show lily csex3 with dissolve
    lily "Hahhh, you’re getting even harder! Y-You’re gonna make me come!"
    "Lily's pussy clenches around my member, rhythmically increasing the pleasure with each passing second."
    "I grit my teeth and pull on her tail as a familiar feeling in my taint signals an impending orgasm."
    play sound cum
    show lily csex4 with cum
    play sound cum
    show lily csex4 with cum
    "With a few last deep thrusts my cock finally releases its load deep into her vagina and womb."
    play sound cum
    show lily csex4 with cum
    play sound cum
    show lily csex4 with cum
    stop music fadeout 5.0
    stop ambience fadeout 5.0
    lily "Kyaaaahhhh, I want you to breed me like the slut I am! Fill my belly with your cum!"
    "Satisfied, I pull out and leave Lily panting on the counter as she continues to enjoy her longer orgasm."
    show lily csex5 with dissolve
    lily "Haahh, haah, yes! So much thick cum, I loo…ve… eeehhh?"
    "Almost immediately her green eyes return to a deep blue hue as Morrigan’s brainwashing curse is lifted."
    lily "O-Oh my goodness, I can’t… W-What? Morrigan! I need to stop Morrigan!"
    play sound movement
    scene bg cdusklightbedroom with hpunch
    "Almost stumbling from the counter, her quivering thighs let out as she falls onto the floor."
    show lilyb close
    show lily closesad
    with dissolve
    lily "Uuuuu… What’s going on?"
    play ambience raindistantthunder
    scene bg black with dissolve
    "I spend a few minutes explaining the situation as succinctly as possible, bringing Lily to a deep understanding."
    scene bg cdusklightbedroom with dissolve
    show lilyb close
    show lily closesurprised
    with dissolve
    lily "I can't believe it… So Morrigan has also brainwashed the Royal Sisters like this too…? This is bad!"
    show lily closeangry with dissolve
    lily "I can’t believe she’s using you and Moxie like that… A-And Penelope! I had no idea!"
    mc "'Using Moxie'? What do you mean Lily? Morrigan is Moxie, she told me that."
    show lily closesurprised with dissolve
    lily "No, no, you don’t understand! Morrigan is a Morphling, not only does she have the ability to shapeshift into any form, but she also has the ability to possess hosts…"
    mc "A host? She’s taken over Moxie’s body?"
    show lily closeshy with dissolve
    lily "Yes, that’s why she’s such a dangerous foe, because she truly could be anyone… It makes sense that they decided to use Moxie though, because of her powers…"
    lily "It’s most likely that Morrigan and Penelope groomed and used Moxie’s special abilities to summon you, and then used you as a pawn…"
    mc "Ahh… So… Moxie is a real person? The Moxie I know?"
    show lily closeneutral with dissolve
    lily "Mhm, the Moxie we know is still alive inside that shared body of Morrigan’s. The Moxie you know is real."
    lily "I’m not sure when Morrigan started possessing her, but it would seem she let a lot of Moxie’s original personality shine, because I didn’t notice any difference."
    mc "Why is Morrigan using Moxie’s body? Why can’t she just let her go?"
    show lily closeangry with dissolve
    lily "That’ll be because of Moxie’s unique and useful powers. Penelope and I had vague suspicions of such when we first met Moxie, I hadn’t anticipated that  was an interloper though…"
    lily "If Morrigan siphons enough power from the royal sisters, specifically Selene, Moxie will no longer be useful and will be disposed of… That’s our losing condition."
    lily "All that matters is defeating Morrigan as soon as we can, that way we’ll save Moxie."
    show lily closeshy with dissolve
    lily "And, you’re not at fault for any of this."
    $ clibcom = 1
    ## alt if she’s the last to be cured lily "Now you’ve cured everyone, you’re a hero."
    if cfarcom == 1 and cboucom == 1 and cbarcom == 1 and cbakcom == 1:
        $ lilfulast = 1
        lily "Now it’s our turn. Thank you for curing everyone!"
        lily "I’ll need to quickly come up with a plan. Could you go downstairs and let the girls in for me? I'll be down in five minutes."
        jump treemeeting
    else:
        lily "For now, you need to continue your mission. Reverse everyone’s brainwashing and tell them to come to the tree, I’ll devise a plan as quickly as I can."
    jump cworldmap
label cfarm:
    #### Honeycrisp meet, with and without meeting Butters, and sex
    if cfarcom == 1:
        "There's no time to visit Honey and Blossom again, I need to continue my fucking escapade!"
        call screen cworldmapscreen with dissolve
    play ambience raindistantthunder fadein 3.0
    if cfarvisit == 0:
        $ cfarvisit = 1
        show bg cfarm with dissolve
        "I make the trek to the farmhouse. It must be miserable for Honeycrisp to work in this rain."
        "If I recall, the royal sisters had previously controlled the rain so it only rained overnight around 3:00am."
        "Only Blossom is inside, no doubt Honey is still working hard outside."
        show bg farmkitchen with dissolve
        show blossom happy with dissolve
        blossom "Hello [playername], are you here to give us some orders?"
        "Awh... Not her too..."
        "The brainwashing doesn’t change personality much. It’s interesting that they follow my orders as well as Morrigan’s."
        "I wonder if that’s Morrigan’s choice? She didn’t need to make these mares follow my orders, but she did seem unusually enamoured with me."
        mc "Where’s Honey?"
        show blossom laughing with dissolve
        blossom "She’s outside farming, so you and I are all alone today."
        mc "So she’s still working even under Morrigan’s influence?"
        show blossom happy with dissolve
        blossom "Of course, we need food for the brood."
        mc "How do you get orders from her?"
        show blossom shocked with dissolve
        blossom "I think we can get telepathic orders. We’ve already been ordered to ‘obey’ our new Queen, Penelope and you. So, I guess we’re just doing what we’d do normally."
        show blossom happy with dissolve
        blossom "I’m doing an assignment for college, see?"
        "Interesting, so without orders they just perform as they would usually based on their previous personalities?"
        mc "Very useful, thank you Blossom."
    else:
        show bg cfarm with dissolve
        "I make the trek to the farmhouse. It must be miserable for Honeycrisp to work in this rain."
        show bg farmkitchen with dissolve
        "As I enter the kitchen, Blossom is munching on some raisins while working on her assignment."
        show blossom shocked with dissolve
        blossom "Ohh, you're back! Here, let me get you a towel mister."
        mc "Thank you Blossom."
        "Ahh sheesh... She's so sweet, I feel even worse for corrupting her now."
    if cforvisit == 0:
        show blossom bashful with dissolve
        blossom "Would you like any tea? Maybe with some milk? Eheh..."
        mc "Nah... I'm gonna head out, sorry Blossom."
        jump cworldmap
    else:
        pass
    stop music fadeout 5.0
    mc "Let’s do this quickly… I’m going to get Honeycrisp and we’re all going to have sex."
    show blossom bashful with dissolve
    blossom "O-Oh! Oh my, absolutely mister. I’ll prepare the bedroom."
    hide blossom with dissolve
    "She certainly would never agree to that if she wasn’t brainwashed, it seems ordering her overrides her personality."
    "I’m not sure if I need to sleep with Blossom, but I’d feel better if I removed the spell from her too; I’ll cure them both at once."
    "There are some other individuals in Arcadia that I won’t have the chance to cure, I’m hoping the brainwashing reverts when we defeat Morrigan."
    "I’ll just need a tiny bit of milk to keep my erection going for both girls, it should help with the other mares as well."
    show bg cfarm with dissolve
    "I take a quick sip of some of Anna’s milk and walk out to the farm fields where I see Honey hard at work."
    $ milk3 = 1
    show honeycrisp nchappy with dissolve
    honeycrisp "Howdy stud!"
    show honeycrisp ncneutral with dissolve
    honeycrisp "What’re ya doing here in this weather? I couldn't make ya work with me in this rain."
    mc "I’ve got an important order straight from the Queen, I need to have sex with you and Blossom."
    show honeycrisp ncshocked with dissolve
    honeycrisp "Well I’ll be, I haven’t heard anything from the Queen; but if it’s coming from you, it must be true."
    mc "{i}Exactly!{/i} Blossom is preparing your bedroom I think, let’s go."
    show honeycrisp nchorny with dissolve
    honeycrisp "Absolutely stud, me and my little sister will always be eager to serve."
    "I almost feel bad for manipulating these brainwashed girls, but this is far easier and faster; and time is something we don’t have a lot of."
    scene bg black with dissolve
    play music sex1 fadein 3.0
    show honeyblossomb threesome
    show honeyblossom threesome1
    with dissolve
    "The sisters present themselves eagerly on the bed, their pussies soaked with lust and their expression glazed with need and obedience."
    "Thanks to the milk, my cock is throbbingly erect, it won’t take long to cure these girls."
    honeycrisp "Ahh stud, I’m so grateful that you’ve decided to bless us with sex today."
    blossom "Y-Yeah, even though it’s embarrassing to do it with my sister…"
    honeycrisp "Ah Blossom, you’re still immature if you’re letting little things like that worry you. We need to accept the gift [playername] gave us, how about you fuck her first, stud?"
    blossom "Of course, I’m an obedient servant for our Queen… a-and I’m always willing to do it, if it’s with you…"
    "Blossom lowers her eyes slightly as I lean in. Her expression is shy, but she still licks her lips as my cock nears her aching pussy."
    "She blushes as I take hold of her fuzzy thighs and move closer. I rub the head of my member against her dripping snatch, coating my tip with her wetness."
    play sound cum
    show honeyblossom threesome2 with dissolve
    play ambience sex fadein 3.0
    "With enough of her juices gleaming on my glans to act as lubricant, I align her slippery pussy with my cock and push forward."
    "Parting her lips, she moans with relief as I slowly enter her. However, I don’t give her time to savour the feeling, as I immediately begin humping her slick pussy."
    blossom "Haahh, yesshh… This is so good, I’m so glad the three of us can enjoy this together…"
    honeycrisp "You’re such a good gal Blossom, you’ll make for a perfect babe to serve [playername] and the Queen."
    show honeyblossom threesome3 with dissolve
    blossom "Y-Yes, I want to serve, make me your toy [playername]!"
    "It’s curious to note that the girls never touch each other, it’d be against their personalities to do that without an order. As tempted as I may be to make them kiss, or touch each other, that’d be incredibly irresponsible of me."
    "However, that doesn’t stop Blossom from enjoying this, her pussy twitches as I go harder; fucking her with such force that even her tiny tits bounce up and down."
    blossom "Ohhh, oooohhh! [playername]! Y-You’re going so fast today! Oohh… You’re gonna make me come!"
    "Within a few moments I could feel her vagina clamp around my girth, wringing it as she easily reached her climax. No doubt she must have been masturbating in here before Honey and I arrived."
    "The aphrodisiac milk combined with the fastest pumping I’m able, I can’t stand the tightness of her pussy for long."
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
    "I almost forgot how powerful Anna’s milk was, even a small amount made my orgasm feel mind-blowing."
    blossom "Ooohh, mmmphhh, s-so good!"
    show honeyblossom threesome5 with dissolve
    "Recklessly, I pull out as a last few spurts of cum splatter over Blossom’s tummy and I move over to Honeycrisp."
    honeycrisp "Dang stud, y’all crazy today!"
    play sound cum
    play ambience sex fadein 3.0
    show honeyblossom threesome6 with dissolve
    "Honey’s pussy was already drenched with her lubricative fluids allowing me to sink to the hilt in a single motion."
    "Resuming sex at the same intensity as before, Honeycrisp’s back arches and toes curl in response to the immediate spike in pleasure."
    blossom "Mm… I see…Cum inside her too, [playername]…"
    honeycrisp "Yeah stud! Ahhh, ahh, gimmie your cum too, mmphh!"
    "Honey fucks a lot more proactively than Blossom did, her hips bucking towards me and clashing with each thrust; making my job a lot easier."
    "Together we rut, the disgusting lewd squelching sounds are more than enough to make Blossom blush."
    show honeyblossom threesome7 with dissolve
    honeycrisp "Haahh, ahhh, don’t hold out on me stud! This is the Queen’s order after all!"
    "It takes a frustratingly long time to achieve a second orgasm in a row, even with the help of the milk."
    "But Honeycrisp’s moans and movements help close the distance, as my cock returns to its close to climax throbbing state."
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
    "Together we both pull away, a few stray loads of jism splattering her pelvis as she lay panting."
    show honeyblossom threesome9 with dissolve
    "Honeycrisp’s eyes slowly lose the corrupted green hue and return to…"
    "Oh! she had green eyes anyway, of course."
    "Wait! Blossom has green eyes too! That means Blossom isn’t brainwashed right now either!"
    "Did she just lay there cured the entire time watching me fuck her sister?"
    play ambience raindistantthunder fadein 5.0
    scene bg honeycrispbed with dissolve
    show honeycrisp ncshocked with dissolve:
        xpos 250
        ypos 30
    honeycrisp "Huh? What? ... Morrigan got me? Grr, that bitch will pay!"
    show blossom sad with dissolve:
        xpos 750
        ypos 75
    blossom "Phew… I think we’re both fine now…"
    show honeycrisp ncangry with dissolve
    honeycrisp "Mess with me, fine, mess with my little sister? I’m going to fucking ruin her."
    honeycrisp "Grr, I’m so angry… Thanks for saving us stud; I’m not exactly sure what you did, I guess ya have some kinda magical cum?"
    mc "Yeah, good intuition. Let me explain the plan."
    scene bg black with dissolve
    show bg farmkitchen with dissolve
    show honeycrisp ncneutral with dissolve:
        xpos 250
        ypos 30
    show blossom sad with dissolve:
        xpos 750
        ypos 75
    "With a quick explanation, Honeycrisp agrees to meet with us at the tree."
    blossom "Thank you so much for saving us [playername], I’m so shook knowing that I was a slave like that."
    honeycrisp "Did y’all really need to have us both at the same time? Ah, forget I’m even asking that, of course you did… But, still…"
    if confessedsexwithblossom == 0:
        honeycrisp "It’s a very strange way to find out you and Blossom have been sleeping together behind my back…"
        show blossom shocked with dissolve:
            xpos 750
            ypos 75
        blossom "Eep! H-He did imply that, didn’t he? I-I’m sorry sis…"
        show honeycrisp ncsatisfied with dissolve:
            xpos 250
            ypos 30
        honeycrisp "*Sigh* I’m really not bothered about that right now; we’ve got more important things to deal with."
    show honeycrisp nchappy with dissolve
    honeycrisp "Go on [playername], use your magic dick or whatever! We're counting on you."
    $ cfarcom = 1
    jump cworldmap
label cboutique:
    #### Ruby meet, with and without meeting Butters, and sex
    if cboucom == 1:
        "I don't have enough time to meet with Ruby and the devil, I need to complete my sleeping mission!"
        call screen cworldmapscreen with dissolve
    play ambience raindistantthunder fadein 3.0
    if cbouvisit == 0:
        show bg cboutiquedoor with dissolve
        $ cbouvisit = 1
        "I run to Ruby’s boutique and knock on the door."
        show bg cboutique with dissolve
        "Almost immediately she lets me in, she’s working on a dress on the shop floor."
        "But there’s no mistaking it, she’s brainwashed."
        show ruby chappy with dissolve:
            xpos 400
            ypos 30
        ruby "It’s so wonderful to see you darling! Do come in, are you here to work today?"
        mc "Work? No, no…"
        show ruby laughing with dissolve
        ruby "Ahah, of course not! You’re too important to work at this boutique now."
        "Since the brainwashing, she seems to have gained some kind of knowledge about the situation, but how much?"
        mc "What do you mean, Ruby?  Why am I too important now?"
        show ruby chappy with dissolve
        ruby "Because you’re third in command of Morrigan’s kingdom, of course!"
        mc "Right… Third in command? Morrigan really brainwashed you with those orders?"
        show ruby cneutral with dissolve
        ruby "No need to be so vulgar darling, I don’t see myself as brainwashed, I’m merely enlightened!"
        play music yanderecomplex fadeout 3.0
        show melody csadistic with dissolve:
            xpos 750
            ypos 75
        melody "Oh my gosh, wormy master! I didn’t think you’d visit us peasants anymore since you became royalty, or whatever."
        mc "Ah, you’re here too, that’s perfect."
        melody "Oh really, wormy master? Are you gonna give us some disgusting orders? Maybe turn us into breeding drones? Gross, gross, gross!"
        show ruby chappy with dissolve
        ruby "I for one would love the honour of being a breeding drone for you, although I don’t know the spell for pregnancy…"
        mc "No one’s gonna become a breeding drone! Alright?"
        melody "Mehehe, wormaster doesn’t have the balls to get two amazing slaves like us pregnant!"
        mc "God damnit, why are you so standoffish, even as my slave?"
        show melody chappy with dissolve
        melody "Ehehe, because I know that’s exactly what you want, even under your orders."
        mc "Hmph, so you’d stop if I asked."
        show melody cneutral with dissolve
        melody "… B-But I don’t wanna stop! You jerk! Power abuser! Don’t ever order me to stop being myself!"
        "Can’t say I was expecting her personality to come through so strongly, but it’s endearing to say the least."
        stop music fadeout 3.0
    else:
        show bg cboutiquedoor with dissolve
        "I return to Ruby's boutique and let myself in."
        show bg cboutique with dissolve
        "Ruby and Melody are still lounging around on the ground floor."
        show melody csadistic with dissolve:
            xpos 750
            ypos 75
        melody "Ohh sheesh, you're here to order us around again..."
        show ruby cneutral with dissolve:
            xpos 400
            ypos 30
        ruby "Stand to attention Mel, we live to serve!"
    if cforvisit == 1:
        pass
    else:
        mc "Alright, everyone calm down. I think I'm just gonna leave, okay?"
        show ruby cneutral with dissolve
        ruby "Awhh, Mel... You scared him away."
        show melody cneutral with dissolve
        melody "I'm sorry! You can stay!"
        mc "Don't worry, it's nothing to do with you Melody."
        show melody chappy with dissolve
        melody "Ooookayy..."
        jump cworldmap
    stop music fadeout 5.0
    mc "Alright, let’s get this done quickly."
    $ cboucom = 1
    mc "I finally want that threesome."
    show melody cneutral with dissolve
    melody "WAH? Y-You utter scoundrel, you perv! You disgusting sack of flesh!"
    "Is she REFUSING my order?"
    show melody csadistic with dissolve
    melody "Alright, come on Rubes, let’s have a threesome."
    "Oh, nevermind."
    show ruby chorny with dissolve
    ruby "Of course, anything for our master. Let’s make this as pleasing and special as possible to thank him for enlightening us."
    show melody chappy with dissolve
    melody "Well, I’m more interested in making it as pleasurable as possible for me."
    melody "Lay down on that table ya slut, and I’m gonna get on top of you."
    scene bg cboutique with dissolve
    "Without needing to say another word, the two girls get into a lewd position, spreading their legs and lips for me."
    play music sex1 fadein 3.0
    show rubymelody threesomec1 with dissolve
    mc "Ahh, you’re gonna hate me for this afterwards, Melody."
    melody "Too right, ya sicko! Now hurry up and fuck me so I can complete this order and serve the kingdom!"
    ruby "Nooo, take your time! Our bodies are yours to enjoy!"
    melody "Yeah, yeah… I bet this perv planned this from the moment he met us."
    mc "I can’t say it wasn’t on my to-do list."
    "On the edge of one of the boutique tables, the girls are stacked on top of each other, their legs interlocked as their labia brush against each other slightly."
    melody "Maybe you can make me your personal breeding slut, eh champ? Ehehehe…"
    "Melody’s pussy drools slightly onto Ruby’s, creating a lewd connection between the two."
    show rubymelody threesomec2 with dissolve
    "After admiring the sight for perhaps a little too long, I position myself adjacent to the table and figure out which girl would be best to bring back first."
    play sound cum
    play ambience sex fadein 3.0
    show rubymelody threesomec3 with dissolve
    "I figure Ruby would be more understanding of the situation, so I line the tip of my cock against her vagina and push forward."
    ruby "Ohhh!  "
    melody "Ugghh, you would pick her first! You’re so shallow…"
    "My cock sinks into Ruby, enjoying the intense tightness of her pussy. Her thighs quiver as I plunge each and every inch inside."
    mc "I’m saving the best for last."
    melody "Save your niceties and fuck my whore sis, will ya?"
    "The slightly immoral situation excites all three of us."
    "Melody’s pussy drips onto the point of connection of her sister and I."
    "While Ruby’s hot and enticing walls tighten around my throbbing member."
    "As I fuck Ruby, it’s hard to forget just how experienced Ruby is at using the muscles in her pelvis to squeeze and tease my cock."
    ruby "Mmmhhh, your dick feels so great darling!"
    melody "Hmph… I coulda waited outside while you two rutted like pigs."
    "With Melody’s butt available to me, I give it a light slap to shut her up."
    play sound spank
    melody "Kffh? Nnhhh… You bastard, you better save enough energy to fuck me too."
    "Ruby’s entire body quivers with excitement, her pussy clamps down in intervals, squeezing my cock as it buries itself inside of her."
    "It seems Ruby is getting a lot of additional pleasure being watched. This kind of perverted situation is perfect to get someone like her off."
    "Her hips wouldn’t stop meekly shaking in an attempt to maximise the pleasure, inadvertently grinding her clit with her sister’s."
    show rubymelody threesomec4 with dissolve
    melody "Agghh?! Y-You’re fucking like a crazy person sis! Nnnghh…"
    "Despite what she said, her hips are also subtly moving back and forth; the sisters now grinding together while I pound into Ruby’s sopping wet pussy."
    ruby "T-This is t-too much, ahhh, I-I’m cominnggg! I’m cooommminnggg! I’m coommmmiingggg!!  "
    "Putting some more strength into my limbs, I push myself as fast as possible to orgasm. Aided by Ruby’s rhythmic orgasmic contractions, I was soon pushed to my limit."
    play sound cum
    show rubymelody threesomec5 with cum
    play sound cum
    show rubymelody threesomec5 with cum
    "Finally, unable to bear it, I blew a huge load into the climaxing mare."
    play sound cum
    show rubymelody threesomec5 with cum
    play sound cum
    show rubymelody threesomec5 with cum
    "Like a rushing wave, her pussy was immediately filled with my hot seed."
    show rubymelody threesomec6 with dissolve
    ruby "Mmmphhhh, ohhh my gosshhhhh! I can’t believe my little sister is watching me being creampied!"
    melody "The hell?! Did you really just say that? Is that what’s getting you off? That’s disgustin- mmmgghhh?!"
    show rubymelody threesomec8 with dissolve
    "Catching Melody off guard, I plunge my cock into her tight snatch."
    "She’s so immensely wet that I sink in even faster than I expected. Her pussy is usually tighter than this, but she’s so aroused that she accepts my girth far easier."
    "Ruby was still paralyzed in the glow of her orgasm, the spell quickly wearing off on her. Meanwhile Melody’s body twitches, and her toes curl in response to the sudden spike of pleasure."
    melody "Ahahahhh, haaahhhh, finally, you fucker! Nnghhh, surprised a man like you has the energy to go immediately."
    "It’s said in science that a man can go immediately if there’s another girl to copulate with, but she’s right, it is hard to go again immediately."
    "It takes a while for my cock to harden as much as it was before my orgasm, but Melody’s tight throbbing pussy easily brings our rutting back up to speed."
    melody "Wait, Ruby, what’s happened to your eyes?"
    ruby "Haahhh… Melody, follow his orders, okay?"
    "With a quick understanding of the situation, it seems Ruby has been cured from the brainwashing."
    melody "U-Uhm, o-okay sis? Wormy boy, hurry up and cum! Something’s wrong with Rubes."
    "I breathe a sigh of relief as Melody resumes the rutting. If she had figured out something was wrong, she might have caused some trouble; preventing me from curing her, and maybe even snitching to the Queen herself."
    "I pound Melody’s pussy with enough force to keep her from focusing on anything else, ideally pushing any thoughts out of her mind other than pure pleasure."
    melody "Hahh, haah, haah, gfffhhh, yes, t-that’s it, ya horny bastard!"
    "She was aching with desire and quickly forgot about Ruby's eyes, as her body relaxed and melted into Ruby’s."
    "With each thrust, both of the girls wiggled back and forth. Their clits still brushed against each other, the occasional moan still escaping from Ruby."
    "I grit my teeth, as pleasurable as this is, it’s still extremely difficult to orgasm twice in a row. I can feel slight signs of fatigue building up in my muscles, that’s the worst-case scenario, I need to maintain my speed to reach orgasm."
    show rubymelody threesomec9 with dissolve
    ruby "Mmmphh, Melody, your order is to milk as much cum from [playername]’s cock as possible, come on!"
    melody "Gyyaaahhh, ah-ahm trying, I can’t focus!"
    ruby "Don’t hold back sis, grind your hips into him a little."
    melody "Y-Yeah, haah, ghh… I-I’m the one that fucks, ahh-ah, I’ll make you cum, master!"
    "Melody’s ass starts bouncing up and down almost immediately with vigour and energy, matching the pure intensity of my own thrusts and rocking the entire table."
    "Indirectly the amount of clit rubbing from the intense fuck causes Ruby to wriggle with pleasure below us"
    ruby "Kyaaahh, y-you’re gonna make me come first, mmphh, mmm, s-sis!"
    melody "S-shut up with that sis shit! Y-you’re putting me off!"
    melody "Cum for me damnit! [playername]!"
    "Pounding my dick against her ass, that familiar feeling of climax finally began to rise."
    play sound cum
    show rubymelody threesomec10 with cum
    play sound cum
    show rubymelody threesomec10 with cum
    "My throbbing cock began pumping seed deep into Melody’s pussy and womb. The feeling of my hot cum seeping inside resulted in her own reactionary orgasm."
    play sound cum
    show rubymelody threesomec10 with cum
    play sound cum
    show rubymelody threesomec10 with cum
    melody "Yess, aaagghhh, that’s it!! Mm! Mmmm!"
    ruby "Ahh, f-fuck, y-you made me come too- aa-ah and I’m not even brainwashed! Uhahh…"
    "I piston in and out of Melody’s squeezing insides for my entire orgasm, maximising the pleasure of the experience. Even though pleasure isn’t part of my mission, no one will blame me for enjoying her pussy for a few extra seconds."
    show rubymelody threesomec11 with dissolve
    stop music fadeout 3.0
    play ambience raindistantthunder fadeout 3.0
    "As I pull out, a drop of cum splatters down onto Ruby’s pussy. The sight may truly be the lewdest thing I’ve had the pleasure of encountering in Arcadia."
    scene bg cboutique with vpunch
    "Although that sight is short lived because as soon as Melody’s brainwashing vanishes, she springs up like a shocked cat; rolling off the table onto the floor, like escaping a live grenade."
    "This action leaves Ruby laying on the table, panting and confused."
    show ruby neutral with dissolve:
        xpos 300
        ypos 30
    ruby "Uhm, Mel?"
    show melody neutral with dissolve:
        xpos 800
        ypos 500
    melody "I need to dye my fur, change my identity, move far away..."
    show melody angry with dissolve
    melody "You two… YOU TWO!"
    melody "WHAT WERE YOU THINKING?! THAT WAS SO EMBARRASSING! WE JUST DID AN INCEST!"
    ruby "Well… I think [playername]’s cum saved us from Morrigan's brainwashing… And it wasn’t {i}‘incest’{/i} incest, right?"
    hide melody with dissolve
    show melody neutral with dissolve:
        xpos 700
        ypos 80
    melody "Ugh, whatever… He should have respected our boundaries…"
    melody "But y’know, I’m not exactly keen on having some evil bitch order me around like that, that’s out of my boundaries even more!"
    show melody angry with dissolve
    melody "Fuck, what did I say earlier about being a breeding slut?"
    melody "For some reason Morrigan’s brainwashing gave me an overwhelming desire to get impregnated as a breeding drone or whatever, gross…I guess you have my gratitude, [playername]."
    show ruby sad with dissolve
    ruby "I’m afraid if it wasn’t for [playername], we’d likely all be subservient hosts for breeding Morrigan’s army."
    show melody neutral with dissolve
    melody "I’m not sure what’s worse, being breeding stock, or being brainwashed to enjoy it…"
    scene bg black with dissolve
    "I give the two girls a quick overview of the plan, and tell Ruby to meet me at the tree library soon."
    show bg cboutique with dissolve
    show melody sadistic with dissolve:
        xpos 700
        ypos 80
    melody "Well, look at Mr. Hero over here. Still, there’s one thing that shocked me… I can’t believe how much of a slut you are."
    melody "I was totally right about you, the only reason you came to the boutique was to sleep with us!"
    show ruby laughing with dissolve:
        xpos 300
        ypos 30
    ruby "Now, now, Melody. You know that’s not fair; we came onto him."
    show melody fufufu with dissolve
    melody "Yeah, well… Apparently it was just because he has some kind of magic that makes him irresistible…"
    melody "If this was a hentai, the tags would be ‘ugly bastard’ and ‘hypnosis’."
    "Hentai is a {i}thing{/i} in this world? I got some homework to do after all this is over! Wait a minute..."
    mc "Hey, I’m not ugly!"
    show melody angry with dissolve
    melody "How would I know? Maybe the spell changes your appearance too! That would explain why you look so handsome and cute."
    mc "Hm… I don’t think it does that…"
    show ruby neutral with dissolve
    ruby "Actually… I think the spell is gone, so you just complimented the real [playername]."
    show melody happy with dissolve
    melody "Heh, I know that… Go on, go fuck the other girls, you damn alpha bastard. Just don’t expect me to be part of your harem!"
    mc "Will do, catch you two later."
    jump cworldmap
label cbar:
    if cbarcom == 1:
        "I don't have time to meet with Riku, I need to complete my fucking conquest!"
        call screen cworldmapscreen with dissolve
    play ambience raindistantthunder fadein 3.0
    if cforvisit == 0:
        pass
    else:
        jump cbar2
    if cbarvisit == 0:
        $ cbarvisit = 1
        show bg bar with dissolve
        "I visit the bar. Knocking on the door, Riku shortly lets me in."
        show rikub
        show riku cneutral
        with dissolve
        riku "You're here early! Although you're always welcome, especially with recent events, eh?"
        mc "Yeah, I guess, how's it going?"
        show riku chappy with dissolve
        riku "I'm really pumped to be supporting Queen Morrigan! I'm looking forward to whatever orders she gives us."
        riku "Do you think you can drop any hints about what she has planned for us?"
        mc "Honestly, I have no clue, do you know anything?"
        show riku cneutral with dissolve
        riku "Well... Me and the other elements did kick her ass in the past, so she'll probably want a teeny bit of revenge..."
        riku "That's what makes me want to serve her even more! To prove my loyalty despite my past."
        mc "Do you think she can be defeated again?"
        show riku laughing with dissolve
        riku "Pfft, no way, our Queen kicks ass!"
        "Hmm... That's interesting, she doesn't know who else is brainwashed, does she?"
        "So there probably isn't a hivemind."
        mc "Thanks for the information Riku, maybe I'll see you again."
        show riku cneutral with dissolve
        riku "Hopefully! Later kid."
        jump cworldmap
    else:
        show bg bar with dissolve
        "I check the bar again, Riku lets me in."
        show rikub
        show riku cneutral
        with dissolve
        riku "Back already? What's up? I'm not going to the gym for a while yet."
        mc "Ah, uhm, maybe I'll come back later then."
        show riku chappy with dissolve
        riku "Sure thing, uhm... Try to stay out of the rain, 'kay?"
        mc "Yeah, sure."
        jump cworldmap
    label cbar2:
        pass
    stop music fadeout 5.0
    $ cbarcom = 1
    show bg bar with dissolve
    "I’ll visit the bar next; it should be a quick in-and-out experience."
    "As I knock on the door, the green-eyed Riku opens the door with her usual merriment."
    "To her, it really feels like nothing’s wrong."
    show rikub
    show riku cneutral
    with dissolve
    riku "Hey, how’s it goin’? I was just getting ready to go to the gym, are you coming with?"
    mc "Hey Riku… Are you really going to the gym at this time?"
    show riku chappy with dissolve
    riku "Of course, our Queen doesn’t have any urgent orders; so, I’ll just operate as normal."
    riku "I’m not doing anything wrong, am I?"
    mc "Oh, no, of course not… But the Queen has ordered me to fuck you."
    show riku cneutral with dissolve
    riku "Huh? I haven’t received any orders like that… You’re not gonna knock me up with magic, are you?"
    mc "I’m not gonna knock you up, it’s just to raise morale."
    show riku chorny with dissolve
    riku "Alright boss, don’t need an order for that one. Let’s go upstairs and you can have your fill."
    mc "Actually, let me take you right here and now."
    show riku chappy with dissolve
    riku "Oh? Whatever you say, boss."
    hide rikub
    show riku facesitting2
    with dissolve
    "She bends over the bar’s counter and wiggles her petite butt. I like it when everything goes to plan."
    "But this is no good, I can’t fuck all these girls standing up; I need to save some energy."
    "Who better to fuck me than Riku herself? She has so much energy and sexual prowess that she could make me cum even faster than I could."
    mc "Actually, do you think you can be on top?"
    hide riku
    show rikub
    show riku chorny
    with dissolve
    riku "Oohh, that’s a first for us… Okay, lay down and I’ll service you with my butt."
    play music sex1 fadein 3.0
    show rikub anal
    show riku canal1
    with dissolve
    "I lay down on one of the sofas at the back of the bar, and Riku eagerly mounts me."
    "She grinds her plump labia back and forth against the tip of my cock. Occasionally she prods downwards onto it, teasing the idea of penetration."
    "In only a few seconds, her moist pussy has already drooled and dribbled an impressive amount of lubricants onto my cock’s head."
    "That however, is when she surprises me."
    "Moving her hips forward, I suddenly feel my lubricated tip prodding against the tight pucker of her anus."
    riku "Ehehe, you never told me which hole you wanted!"
    play sound cum
    play ambience sex fadeout 3.0
    show riku canal2 with dissolve
    "Before I can even protest, her sphincter eases around my cock and she slowly takes me inside. I can only hope that I can cure her from anal too."
    "Also… I’m gonna need to wash after this now. So much for Riku being faster."
    "God damn, her ass feels so fucking good though. The tight ring slowly descends my shaft until she has my entire cock at hilt."
    riku "Mmmphh, heh, I’m gonna be your butt slut until the end."
    mc "Damn Riku, I didn’t expect you to have this more dominant side."
    riku "What can I say? I need a bit of revenge for all your shenanigans!"
    "Pressing a hand against my chest, she lifts herself up slowly. The tightness of her ass scaling up each and every nerve ending of my throbbing shaft until it reaches the glans."
    "And then she sinks back down again, reigniting another flash of pleasure."
    "And again, again, again. She fucks me with passion, precision and speed; relentlessly providing my cock with immense pleasure."
    show riku canal3 with dissolve
    riku "Mmphh, mmm! *Slap, slap, slap! * *Squish, slap! * You like my butt, don’cha?"
    "It wasn’t just me enjoying this though. Riku’s elation would have been obvious from her body language, but the really amazing thing is her pussy which constantly drips and squirts onto my pelvis from the light orgasms she’s experiencing."
    riku "Ahhhaa, mmm! Use me, fuck me, I’m all yours, [playername]!"
    "Her petite breasts shake wildly as she continues to deliver more vigorous thrusts, her ass pumping away at my cock."
    "As she starts feeling better and better, her eyes roll back and her fervent moaning intensifies as she nears her climax."
    "In a surge of energy, she races to an orgasm, her body shivering and pucker tensing."
    show riku ranal5 with dissolve
    riku "Haahh, ahhh, g-gonna come, haahhh, yesss, yesss!"
    "My throbbing cock stiffens and my muscles grow tense as her assault on my cock brings me extremely close to cumming."
    play sound cum
    show riku ranal6 with cum
    play sound cum
    show riku ranal6 with cum
    "The additional speed is enough as we push past both our limits. Climaxing, my cock starts spraying thick loads of cum into her butt."
    play sound cum
    show riku ranal6 with cum
    play sound cum
    show riku ranal6 with cum
    riku "Haahh, yesssshhhh! F-Fuck! Fill my belly!"
    stop music fadeout 3.0
    play ambience raindistantthunder fadeout 3.0
    "Riku excitedly rides out both our orgasms."
    "Satisfied, she huffs and slides my cock out with a pop."
    scene bg bar with dissolve
    show rikub
    show riku laughing
    with dissolve
    riku "Phew! that was really good!"
    show riku shy with dissolve
    riku "Heyyy, wait a minute… Why was I thinking Morrigan was my Queen earlier?"
    mc "Ahh perfect. Even though it was anal, my dick still snapped you out of your brainwashing."
    show riku embarrassed with dissolve
    riku "Hmm, I don’t get it, but it sounds like you have some explaining to do."
    mc "I certainly do, so listen up!"
    scene bg black with dissolve
    "I give Riku a quick explanation of the events, and she agrees to meet at Lily’s tree at the designated time."
    "I have a quick five-minute shower to clean up and reinvigorate."
    show bg bar with dissolve
    show rikub
    show riku angry
    with dissolve
    riku "Curse Morrigan, I can’t believe she used you and Moxie like that…"
    riku "She’s really gone and made it personal for me, I’m fuming with anger."
    mc "Your red fur can't get any redder. Don’t worry, we’ll get her."
    show riku happy with dissolve
    riku "Heck yes we will, we’re all gonna save Moxie together, promise!"
    "She gives me a thumbs up and I set off."
    jump cworldmap
label cbakery:
    #### Cream meet, with and without meeting Butters, and sex
    if cbakcom == 1:
        "I don't have time to fuck Cream again, there are others that need my dick!"
        call screen cworldmapscreen with dissolve
    play ambience raindistantthunder fadein 3.0
    if cbakvisit == 0:
        $ cbakvisit = 1
        show bg cbakery with dissolve
        "When I arrive at the bakery it’s open and running business as usual. Cream is working the till, and baking cakes simultaneously, despite her brainwashing."
        show cream chappy with dissolve
        cream "Gotta bake, gotta cake, all for our new Queenie!"
        cream "Wanna help, [playername]? I’ll pay ya!"
        mc "What happened Cream, you have a new Queen?"
        show cream laughing with dissolve
        cream "Yup! You were the one that enlightened me, I think!"
        mc "How do you know that, exactly?"
        show cream cneutral with dissolve
        cream "Gosh, I don’t really know… For some reason, I just know I really have to do a good job serving the Queen, Penelope and you."
        cream "And it’s all your fault! Ehehe…"
        mc "I wonder if there’s some kind of soft hivemind… Cream, do you know if anyone else is brainwa- enlightened?"
        show cream chappy with dissolve
        cream "I dunno, I saw a customer with green eyes earlier, does that count?"
        mc "Eh, no… I guess it’s not a hivemind then, thank goodness, it’d be terrible if Morrigan could tell if she was losing influence."
        show cream laughing with dissolve
        cream "Nahh, there’s no way she could do that! That’s why she needs to siphon up all the energy from the royal sisters!"
        mc "Now how the hell do you know that?"
        show cream cneutral with dissolve
        cream "Oh, uhm?! I have no idea, ahah!"
    else:
        "I return to the bakery which is still operating as normal."
        show bg cbakery with dissolve
        show cream chappy with dissolve
        cream "Heyyy, you're still fumbling around? Need something to do?"
        mc "Kinda, I'm a bit lost right now."
        show cream chorny with dissolve
        cream "Awh bless you, would you like a cake, maybe some cummies?"

    if cforvisit == 0:
        mc "I don't really feel like working or buying anything, so I'll just leave."
        cream "Okie dokie! Maybe you should go see Butters? She can look after you in this miserable weather."
        mc "Hmm... That's a bit random, but thanks for the suggestion."
        jump cworldmap
    else:
        pass
    stop music fadeout 5.0
    $ cbakcom = 1
    mc "I need you to close the store for a few minutes, I need to cum in you, the fate of the world depends on it."
    show cream chorny with dissolve
    cream "Awwhh! I bet you say that to all the girls, [playername]"
    mc "Only recently…"
    show cream laughing with dissolve
    cream "Okie, well, I can’t argue with cummies (or your order)!"
    hide cream with dissolve
    "Cream temporarily closes the shop and just as she closes the curtains she bends over on the counter."
    play music sex1 fadein 3.0
    show cream csex1 with dissolve
    cream "I’ll be the cream if you’ll be the pie, hehe…"
    "No time for foreplay, and no need with this girl. Her crotch is always a soaking mess that’s ready for cock."
    "Her messy tail swishes back and forth as I position myself behind her quivering pussy."
    play sound cum
    play ambience sex fadein 3.0
    show cream csex2 with dissolve
    "Stroking my cock to full attention, I press it against her dripping fuck-hole. Grasping her hips firmly, I slowly thrust in, her body moving back into mine."
    cream "Ahhahaheheaaahh! So goooood, hehe! Faster, faster!"
    "I start thrusting, and she thrusts back with equal energy."
    "As I kept smacking my hips into Cream’s thick ass, it created an obscene slapping sound."
    cream "Mmphh, yesh! Ohhh, it feels great! Whether it’s for the Queen or you, I love it when you take me!"
    "She may be brainwashed, but she’s still one of the many mares that have become obsessed with my human cock in the time I’ve been in Arcadia."
    "*Squish, slap, squish, slap!*"
    show cream csex3 with dissolve
    cream "Mmphh, mm, mm!  Ohhh, your cock is pounding so hard! Ahhhaahhhhhaaa!"
    "Maybe it’s due to Morrigan’s magic, but there’s no denying the abnormal pleasure I’m able to give Cream as her body shudders with lust and she tightly clings onto the bakery counter."
    "Taking a note from previous sexual encounters, I reach over and start groping her large tits from behind, squeezing them and toying with her sensitive nipples."
    cream "Ahaaa, m-my nipples? They’re sooo sensitive!! Kyahhhaaaa! I love it!"
    "The combined pleasure of our sex and my teasing makes Cream’s legs tremble with pleasure."
    "She howled in ecstasy as I kept up the pace, anyone walking past the bakery right now would definitely be able to hear her slutty moaning."
    cream "Ghhhhaaaaahhh! C-Coming, your cock is making me come! Ooohhh!!"
    "After only two minutes of rutting her pussy is already contracting and squeezing around my thick cock, plunging me into intense pleasure."
    "Her pussy was already a tight delight, but now I can’t hold back any longer; my orgasm rapidly wells up."
    play sound cum
    show cream csex4 with cum
    play sound cum
    show cream csex4 with cum
    "My cock explodes inside her. My cum coats her insides while her orgasming pussy clamps down tightly around my shaft, milking as much cum as it can out of me."
    play sound cum
    show cream csex4 with cum
    play sound cum
    show cream csex4 with cum
    stop ambience fadeout 3.0
    stop music fadeout 3.0
    "As I pull out, her body twitches and jerks as she continues to climax; drool spilling from her lips."
    show cream csex5 with dissolve
    cream "Ooohh… Ohh… Your cock fucked me so good! It filled me up so much with its thick hot cum, I love it so much…"
    "She sinks down onto the counter and pants in the afterglow of her orgasm, clearly enjoying the feeling of my hot cum inside her."
    "And, just as I had hoped, the spell wears off."
    show cream csex6 with dissolve
    cream "Oohhh?! Well that’s weird, it feels like I just spent this morning being brainwashed by Morrigan… Am I being delirious?"
    cream "Did I remember that right, [playername]?"
    play ambience raindistantthunder fadein 3.0
    scene bg black with dissolve
    "I quickly explain everything to Cream, including the plan and the time we need to meet up at the tree."
    show bg cbakery with dissolve
    show cream sad with dissolve
    cream "Ohh my gosh, oh my gosh! I’m totally not prepared to fight a big bad! She totally caught me with my tail up!"
    cream "And she would have gotten away with it too, if it wasn’t for you being such a kind soul."
    mc "I am fortunate in a sense that no one blames me for this, so far anyway."
    show cream angry with dissolve
    cream "How could anyone blame you? You’re a victim in this too!"
    cream "We’ll get justice for everyone, and then have the most amazing party afterwards to celebrate!"
    mc "You got a deal, Cream. Okay, let’s go!"
    show cream happy with dissolve
    cream "Yes! See you at the treehouse!"
    jump cworldmap
label treemeeting:
    ### Tree meeting
    # needs to  begin differently if  you fuck Lily last
    scene bg black with dissolve
    "Meanwhile in the castle…"
    play music morrigan
    play sound thunder2
    show bg ccastlethrone
    show morrigan evilhappy
    show aurorab:
        xpos -200
        ypos 100
    show aurora cneutral:
        xpos -200
        ypos 100
    show selene cneutral:
        xpos 775
        ypos 100
    with cum
    morrigan "There we go... Nearly half absorbed..."
    morrigan "I feel so powerful! Is this how strong an alicorn is?"
    morrigan "If I'm twice as strong as even this, no one would be able to stop me! Ihihi!"
    aurora "I... feel dizzy... Mistress..."
    show morrigan death with dissolve
    morrigan "Shut it, minion."
    scene bg ccastlethrone with dissolve
    show penelope chappy with dissolve:
        xpos 750
        ypos 50
    penelope "Everything going well?"
    show morrigan evilhappy with dissolve:
        xpos 250
        ypos 0
    morrigan "Oh, you're back! Where's [playername]?"
    show penelope cshocked with dissolve
    penelope "[playername]? Sheesh, why are you so obsessed with him? How am I supposed to know where he is?"
    show morrigan angry with dissolve
    morrigan "What a fucking useless spymaster you turned out to be..."
    show penelope csad with dissolve
    penelope "I'm sorry, your majesty... Is there anything else I can do for you?"
    show morrigan laughing with dissolve
    morrigan "Hmm... You're pretty useless to me now that I have all this power. Maybe stick around and become a breeding drone after I clear out Arcadia."
    show penelope cshocked with dissolve
    penelope "Breeding drone? Clear out Arcadia? What are you planning?"
    show morrigan happy with dissolve
    morrigan "Well... I was considering keeping the elements and sisters for [playername]'s harem, but if he isn't interested then I'll just kill them."
    show penelope cangry with dissolve
    penelope "Kill them? You can't! You promised there would be no violence!"
    show morrigan laughing with dissolve
    morrigan "Nothing violent about it, it'll be a peaceful and respectable execution, ihihi!"
    show morrigan evilhappy with dissolve
    morrigan "But maaayybe if you can convince [playername] to come back, I'd have a vested interest in keeping his little harem alive."
    show penelope csad with dissolve
    penelope "Morrigan! I am ashamed! I told you that I'd only help if there was no killing. You must respect that!"
    show morrigan angry with dissolve
    morrigan "Hah, respect, you? You're just a minion. You're lucky that I deem to notice you."
    show penelope cangry with dissolve
    penelope "Ah- minion? You're awful! My Que... no... I can't..."
    show morrigan pissed with dissolve
    morrigan "Then fuck off, you'll only burden me with your softness at this rate."
    stop music fadeout 2.0
    hide penelope with dissolve
    "Penelope grits her teeth before storming out of the throne room."
    play sound thunder2
    show morrigan death with cum
    morrigan "Time for some good ol' fashioned revenge. I want to kill one of these pony bastards for each of my own they slaughtered."


    scene bg clibrary with dissolve
    "Back at the library..."
    if lilfulast == 1:
        "After sleeping with Lily, I went downstairs to the library just before the meet time."
        "What impeccable timing, my dick really held out on me. Drinking that milk was a great idea, I don’t think I would have enough stamina to fuck the little sisters without it."
        "Downstairs quite a few of the girls are already here and are discussing tactics."
        "Soon, Lily returns after a quick brainstorm to plan, although she didn't have very long. I probably should have slept with her first..."
    else:
        stop music fadeout 10.0
        "Having finished fucking the last of the elements, I have ten minutes to return to the treehouse."
        "What impeccable timing, my dick really held out on me. Drinking that milk was a great idea, I don’t think I would have enough stamina to fuck the little sisters without it."
        "When I return, quite a few of the girls are already here and are discussing tactics."
        jump skipaltreemeeting

    label skipaltreemeeting:
        pass
    play ambience raindistantthunder fadein 3.0
    play music eyesofthewind
    "Naturally, as someone Morrigan potentially trusts, I’m playing a key role…"
    show lilyb:
        xpos 400
        ypos 40
    show lily neutral:
        xpos 400
        ypos 40
    with dissolve
    lily "Judging by the situation, it seems natural that Morrigan has used the authority of the Royal Sisters to bypass the guards."
    lily "Right now, Morrigan and the sisters will be alone somewhere as the siphoning process commences, it’ll only take a total of five hours to drain them dry using her dark powers."
    show butters dresssurprised with dissolve:
        xpos -50
        ypos 0
    butters "And it has been two hours so far… That means the sisters have already lost about 40 percent of their power no matter what… M-Maybe even more before we’re finished!"
    show lily shy with dissolve
    lily "Yes… It’s devastating… By the time we confront Morrigan we need to assume she’s as powerful as an alicorn and definitely more powerful than the sisters."
    show honeycrisp ncangry with dissolve:
        xpos 850
        ypos 20
    honeycrisp "Well that’s alright, ain’t it? Us elements are more powerful than an alicorn. That’s why Aurora and Selene made us the elements, so we can take care of threats even more dangerous than that."
    hide butters
    show ruby sad:
        xpos 75
        ypos 40
    with dissolve
    ruby "And we were still all brainwashed… What fools we are."
    hide honeycrisp
    show rikub:
        xpos 850
        ypos 55
    show riku neutral:
        xpos 850
        ypos 55
    with dissolve
    riku "Look, there’s no point in worrying about what happened, let’s focus on the mission and get it done, ‘kay?"
    show lily neutral with dissolve
    lily "Riku is correct, every minute is a tangible loss of power for the sisters."
    lily "The moment Morrigan discovers that we’re no longer under her control, and hence a threat, she may do something drastic."
    show riku embarrassed with dissolve
    riku "Such as?"
    show lily angry with dissolve
    lily "Perhaps she’ll turn the sisters against us, that’d be an uncomfortable fight…"
    hide ruby with dissolve
    show honeycrisp ncangry with dissolve:
        xpos 0
        ypos 20
    honeycrisp "There’s no way we’d win in a fight against a super powered Morrigan and both sisters!"
    show riku angry with dissolve
    riku "Tch, what the heck do we do? If that bitch is gonna play unfair and use the weakened Queen and Princess as meat bags, we need to find a way to separate the two!"
    play sound open
    scene bg library
    show penelope cshocked with dissolve:
        xpos 825
        ypos 40
    "In a sprint, Penelope sprints into the tree library. She spots us, and comes over while panting."
    penelope "You guys... You're all... okay?"
    show lilyb:
        xpos 400
        ypos 40
    show lily surprised:
        xpos 400
        ypos 40
    show rikub:
        xpos 0
        ypos 55
    show riku angry:
        xpos 0
        ypos 55
    with dissolve
    riku "Why you... I heard about everything! Come on girls, let's get her quickly!"
    show penelope sad with dissolve
    penelope "No, wait! I'm here to help! Morrigan... she's gone crazy! She wants to kill everyone!"
    hide rikub
    hide riku
    show honeycrisp ncangry:
        xpos 0
        ypos 40
    with dissolve
    honeycrisp "Yeah? And? It's because of you betraying us that we got into this whole mess!"
    show lily neutral with dissolve
    lily "Girls, let's hear her out... She seems genuinely distressed right now."
    show honeycrisp ncneutral with dissolve
    honeycrisp "Hmph, fine... But if I don't like what you've got to say, I won't pull my punches."
    hide lily
    hide lilyb
    show cream embarrassed:
        xpos 300
        ypos 40
    with dissolve
    butters "I can't believe Penelope is a morphling..."
    show penelope cshy with dissolve
    penelope "Yes, well... I first have to deeply apologize for everything I've done..."
    penelope "I appreciate that an apology is not enough, but as far as I'm concerned, it's more important that I do everything in my power to revert this catastrophic mistake, and for that I'll need your help."
    penelope "I thought I could trust Morrigan to be a fair ruler, I thought I'd helped her become a better person... But I was wrong, so wrong..."
    show honeycrisp shy with dissolve
    honeycrisp "... What do y'all think? She tellin' the truth?"
    hide honeycrisp
    show lilyb:
        xpos 0
        ypos 40
    show lily neutral:
        xpos 0
        ypos 40
    with dissolve
    lily "All of Penny's actions right now fit her personality, wouldn't you say? She was always kind and loving. Always wanted to help others and bring the best out of them."
    lily "I'm far more surprised by her uncharacteristic betrayal, than I am of how she's acting now..."
    lily "I... trust you, Penelope."
    lily "And since you know Morrigan better than the rest of us, do you have a plan?"
    show penelope cneutral with dissolve
    penelope "A plan? I might have an idea... But you'll have to explain to me how you broke the brainwashing."
    hide cream
    show butters dresshappy:
        xpos 300
        ypos 25
    with dissolve
    butters "That'll be [playername]'s magical cum! One womb full of that will almost instantly knock out the brainwashing."
    show penelope chappy with dissolve
    penelope "Well damn, I don't know what you did, but that's pretty convinient!"
    penelope "I'd say we have two priorities right now. One, evacuate the castle, and two, break the brainwashing of Aurora and Selene."
    penelope "There's absolutely no way we can fight three alicorn-power creatures at once. And even if we defeat Morrigan, unless we completely kill her, the brainwashing won't fade and the sisters will attack."
    show butters dressangry
    show lily surprised
    with dissolve
    lily "*Gasp* I didn't know that!"
    show penelope cneutral with dissolve
    penelope "But I have an idea... I'm sorry to ask you of this, [playername], but you're the only person that can fool her."
    mc "I'm listening..."
    show penelope cshy with dissolve
    penelope "Perhaps you noticed, but the truth is, Moxie-Morrigan is pretty obsessed with you, [playername]... I think it's because some remnants of Moxie's personality still currently reside within Morrigan."
    penelope "If you can convince her to let you sleep with the sisters, which should be pretty easy, you could cure their brainwashing and she’d no longer be able to use them as shields."
    mc "Putting my dick to good use, I like it."
    show penelope chappy with dissolve
    penelope "And! While we're doing that, we can evacuate the castle. We'll have about fifteen minutes."
    show lily neutral with dissolve
    lily "That's a great idea... Once she has lost control of the sisters, it will be far easier for us."
    lily "As soon as the six of us have a clear shot of Morrigan, we can immediately burn her in one super-powerful blast. Well… Maybe not too powerful, I don’t want to hurt Moxie…"
    hide butters
    show honeycrisp ncneutral:
        xpos 350
        ypos 30
    with dissolve
    honeycrisp "Don't hold back too much Lily, we gotta eradicate that bug."
    hide lily
    hide lilyb
    show rikub:
        xpos 0
        ypos 40
    show riku happy:
        xpos 0
        ypos 40
    with dissolve
    riku "Wait, am I hearing this right, [playername]’s job is to sleep with the Queen and Princess? Guess it’s not the first time, hah!"
    hide penelope
    show butters dresshappy:
        xpos 700
        ypos 0
    with dissolve
    butters "My my, I can’t believe [playername] managed to sleep with them both..."
    show cream laughing with dissolve:
        xpos 525
        ypos 30
    cream "Come on you guys, it was totally obvious that he's a huge player!"
    scene bg library
    show lilyb
    show lily shy
    with dissolve
    lily "Guh, y-you guys! Now is not the time for expository banter! Tease him after we save Arcadia!"
    lily "[playername], it’s likely that Morrigan won’t leave the sisters alone with you. Meaning you’ll likely be having sex with them while she’s siphoning."
    lily "And as you know, the moment you cum inside them, they’ll turn…"
    mc "I see… Timing is crucial then; I have to cum in them both at once."
    show ruby happy:
        xpos 850
        ypos 40
    with dissolve
    ruby "And as soon as Morrigan notices she’s lost control, we need to immediately jump in while she’s defenseless!"
    show lily happy with dissolve
    lily "She’ll still be extremely powerful, but with no meat shields she won’t be able to stop us from charging up the elements, it’ll be checkmate."
    show penelope chappy with dissolve:
        xpos 0
        ypos 40
    penelope "Perfect... If anyone can do it, it's you Lily..."
    show lily neutral with dissolve
    lily "Are you sure about this, Penelope? You're shaking..."
    show penelope csatisfied with dissolve
    penelope "I... I'm sure... I'll focus on the evacuating..."
    mc "Okay, let’s do this…"
    stop ambience fadeout 2.0
    stop music fadeout 2.0
    scene bg black with dissolve
    "..."
label confrontingmorrigan:
    #### Confronting Morrigan on your own
    show bg ccastle with dissolve
    "When I arrive at the castle, the guards seem none-the-wiser as they escort me to Queen Aurora’s personal chambers."
    "Although they do seem notably disgruntled, there’s bickering amongst them."
    guard1 "Why did the Queen just let that witch past?"
    guard2 "Wasn’t that Morrigan?"
    guard3 "I don’t know, is she a diplomat from another country?"
    guard4 "Shut up you three, you can’t argue with the Queen’s orders."
    guard1 "Dude, her eyes were green! Isn’t that weird?"
    guard4 "Orders are orders, the eye colour Queen Aurora felt like using today isn’t our concern."
    guard3 "I wonder if she dons disguises and sneaks out of the castle?"
    "Okay, so these guards are completely useless."
    "I arrive in Aurora’s quarters, as before I’m left alone thanks to my personal connection with the Queen, as concubinator I can secretly come and go whenever I want."
    show bg castlelivingroom with dissolve
    "I peek in the living room, no one there."
    show bg bathroom with dissolve
    "Bathroom empty, gym empty…"
    show bg ccastle with dissolve
    "She’s not here at all."
    scene bg black with dissolve
    "I go down the spiral staircase that Aurora once took me up, and enter the throne room from the back."
    show bg ccastlethrone with dissolve
    "There, on the throne!"
    play sound thunder
    play music morrigan
    show morrigan laughing
    show aurorab:
        xpos 0
        ypos 475
    show aurora satisfied:
        xpos 0
        ypos 475
    show selene satisfied:
        xpos 600
        ypos 475
    show bg ccastlethrone
    with cum
    morrigan "Well, well, well! I knew you’d be back, ‘alpha’, ihihihee!"
    mc "Mm… Morrigan…"
    show morrigan happy with dissolve
    morrigan "I couldn’t resist putting these girl’s tongues to good use. Gosh, I had no idea the ex-royalty around here were such good carpet munchers!"
    aurora "Mmphh, yoursh pusshhyy is shoo tastyyy my Queen!!"
    selene "Haahh, ohh, [playername] is here!  Maybe we’ll be bred today!"
    show morrigan laughing with  dissolve
    morrigan "They’re even better than Penelope! *Giggles* Damn, where did that rat get off to anyway?"
    mc "They do look like a lot of fun."
    hide aurora
    hide aurorab
    hide selene
    show morrigan neutral
    with dissolve
    morrigan "Have you decided to join me, [playername]?"
    "I grit my teeth and try to come up with a conversation that'll lack suspicion and lead to having sex with the sisters."
    "I need to appear slightly stand-offish, otherwise Morrigan will be sceptical of my sudden change in heart."
    mc "Are you really Moxie? Tell me the truth, is this what you always wanted?"
    show morrigan angry with dissolve
    morrigan "Hmph… I mean… That’s a complicated question, I am Moxie and I’m not!"
    mc "That’s what you said last time, but I felt like you were dodging the question…"
    show morrigan sad with dissolve
    morrigan "Eh… What are you talking about? I am Moxie and Morrigan, we’re the same person."
    morrigan "Wait, did one of the Elements of Har’Mony tell you about me?"
    "Shit, did I blow it already?! I should have just kept my damn mouth shut!"
    show morrigan evilhappy with dissolve
    morrigan "Sheesh, of course those yappy bastards bragged about that… No wonder you were so hesitant when I revealed myself and told you I was called Morrigan."
    "No, I’m fine… She thinks someone told me before the brainwashing…"
    show morrigan happy with dissolve
    morrigan "I guess we got off on a bad foot, shit happens! But what I wanna know, is how much do you know?"
    "Her tone is a confusing mixture of sincere and sinister; I don't know why, she just exudes a hostile aura. I feel like I need to be very careful with what I say next."
    mc "I don’t know a lot… But I want to know how much of you is the Moxie I knew."
    mc "All the times we’ve talked together, all the times you opened your heart to me, was that you, or Moxie?"
    mc "Are you the same girl that wants to fill the world with cheer and excitement? I don’t believe it."
    show morrigan oof with dissolve
    morrigan "Tch… I-I am the Moxie you knew, this is what I want!"
    show morrigan sad with dissolve
    morrigan "It’s complicated… You still love me though, don’t you [playername]?"
    morrigan "We’ve been through so much together, I’m sorry I had to hide some things from you. It was always to protect you!"
    "She's lying! She truly is an evil creature using Moxie and her name like this..."
    "But... Why would she lie? She has all the power, why lie to keep me around..?"
    "Maybe it's what Penelope said before... There's a part of Moxie still in Morrigan that's 'protecting' me. Otherwise, Morrigan would have no reason to keep me around, she could kill me whenever she wanted."
    "That'd make sense, right? If Morrigan had some control of Moxie before, then the reverse must be true while they share the same body, right?"
    "I’ll play along regardless, it’s the only way I’ll be able to complete the plan. If I’m too confrontational now I’ll blow it."
    show morrigan angry with dissolve
    morrigan "It’s these two bitches that ruined everything for me, they stole my kingdom!"
    morrigan "Arcadia was supposed to be mine! These warmongers took it from my family!"
    morrigan "It was my birth right! These two are nothing but dictators, all they know is how to force people to live the way they want, with their morals and ideas of ‘good’ and ‘evil’."
    morrigan "But who gave them the right to dictate that?"
    show aurorab:
        xpos 0
        ypos 475
    show aurora cneutral:
        xpos 0
        ypos 475
    with dissolve
    aurora "I’m sho shorry my Queen!"
    show morrigan evilhappy with dissolve
    morrigan "Less talk, more tongue."
    hide aurora
    hide aurorab
    with dissolve
    mc "Alright, I believe you Morrigan… I haven't been here very long, so Arcadia doesn’t mean much to me. What I really want is for things to go back to the way they were before."
    mc "I want to live a comfortable life with you, and to be able to sleep with others."
    show morrigan laughing with dissolve
    morrigan "Ohh, perfect! Have you finally decided to enjoy a harem of any girl you could possibly want?"
    mc "Guess I’ve got nothing better to do, it’ll take me a while to get used to your new ‘Morrigan’ form though, Moxie."
    show morrigan happy with dissolve
    morrigan "Ooohh, music to my ears…  I’ll make it worth it, you’ll have me, these slutty alicorns, and any one of those girls you fucked since you arrived- no, even more than just that!"
    morrigan "You’ll be a part of my inner circle, and you’ll become a respected member of my empire."
    "What makes her think I want to be part of {i}her{/i} empire? She’s either deluded or completely lacking empathy if she thinks I’d be okay with this."
    mc "Sounds great! How about we start with the ex-royalty? Lemme smash."
    show morrigan evilhappy with dissolve
    morrigan "Ohoh, eager! But I like the sound of that a lot…"
    morrigan "Well, as tempted as I am to join in the fun, I need to focus on siphoning their power."
    morrigan "I’ll happily watch the show though."
    morrigan "Aurora, Selene, get on top of each other and mash your pussies together!"
    "This is my third incestuous threesome of the day, what are the odds of that?"
    scene bg black with dissolve
    aurora "Yes my Queen!"
    selene "I’ll go on top!"
    play music sex1 fadein 5.0
    show auroraseleneb threesome
    show auroraselene cthreesome1
    with dissolve
    "Even though I’m only doing this to cure them, I’d be lying if I said I didn’t enjoy it a little."
    "They both look so happy too, as they wiggle their butts and flick their tails with lustful enthusiasm."
    play sound cum
    play ambience sex fadein 3.0
    show auroraselene cthreesome2 with dissolve
    "Considering my sex strategy, I get an idea. Rather than penetrate either one of them, I slide my cock between their labia."
    "They’re both wet enough to easily let my cock slide back and forth."
    selene "Ohhh, I can feel your cock throbbing against my clit!"
    "As I push my cock forward, their labia and vulva squish against my shaft providing a suitable tightness concentrated in one area."
    morrigan "Oohh? That’s an interesting method."
    mc "I’m gonna tease these sluts first, and make them beg before I give them any penetration."
    morrigan "Meheheh, I love it!"
    "With this technique, I won’t even have to move; which is great, because I’m exhausted from all this fucking."
    mc "Alright bitches, grind on my cock!"
    aurora "Yes sir! Let’s go sis!"
    "The horny mares grind their hips back and forth. Their technique is sloppy at first, but they soon find a rhythm which compliments each other’s movements."
    "Both mares apply pressure as their pussies slip back and forth, the sensation perfectly pleasuring my glans; sucking and squishing like penetration."
    selene "Ahhh, ahh, why can’t you just put it inside? *Squish, squish*"
    aurora "Sister! Be quiet and grind! Ohhh, ahhh…"
    morrigan "Ihihihi, they’re so subservient! It’s so pathetic and I love it."
    "With overwhelming desire, their pussies drip and squirt all over my cock and each other, leaving my cock with a glistening sheen which allows them to move even faster."
    "As amazing as the pressure from their scissoring feels, I’ll never be able to cum from just this, especially after having previously ejaculated so many times."
    "Straining myself slightly, I begin to thrust back and forth, squishing and indenting their labia as they try to keep up."
    selene "Ohh, ohhhh, yes! Keep pushing my clit like that!"
    aurora "I hope you don’t waste your cummies on our tummies! *Squish, grind, squelch*"
    morrigan "Hmm… It’s taking you a while to cum. Their technique must be bad, they’re probably weak from the siphoning, hehe."
    morrigan "But don’t worry, I’ll put that strength to good use when I bed you tonight."
    "With all three of us grinding against each other, the sensations are increased and I get ever closer to my important climax."
    "The sisters hump like rabbits as they try to steal as much pleasure as they can, fortunately that serves my purposes too."
    show auroraselene cthreesome3 with dissolve
    aurora "Ahh, ohhh, harder sis, grind harder! It’s too hard on the bottom, aaahhhh!"
    selene "Ohh f-fuuuck! I-I’m gonna come, I’m coming from just grinding on this cock! Ahh, ahh! *Squish, grind*"
    morrigan "Goodness, this is positively obscene, the noises are so lewd! Ihihihi!"
    "Selene’s pussy contracts and squirts slightly as she orgasms, her hips bucking and applying more pressure to my cock."
    "Aurora, frustrated that she hasn’t achieved orgasm from her more awkward position, irately pushes back with more vigour."
    morrigan "They’re so controlled by their pleasure! Ihihih, they’ll do anything to get more of it! If I realized they were such whores for pleasure, I wouldn’t have even bothered brainwashing them *giggles*!"
    "The increase of intensity from both sides rapidly begins to overwhelm my cock, finally I can feel that familiar tension in my taint."
    "My cock stiffens and my muscles grow tense, my mind clouds up as a potent orgasm rises throughout my core."
    selene "Ahhhaa, ghhaahh! *Pant, pant* *Squish, squirt*"
    aurora "F-Finally, I-I’m gonna come, yesshh! I’m coming for you [playername], gimme your cummies too!"
    "This is it! Instantly I pull back from the sisters to their immediate dismay, as I deny them pleasure from their orgasms."
    play sound cum
    show auroraselene cthreesome5 with cum
    play sound cum
    show auroraselene cthreesome5 with cum
    "However as if to rectify that problem, with one thrust I plunge my cock into Selene’s pussy, just as my cock erupts, and launches several loads deep into her womb."
    play sound cum
    show auroraselene cthreesome5 with cum
    play sound cum
    show auroraselene cthreesome5 with cum
    "Less than a second after, I pull back and lunge my shaft deep into Aurora’s pussy, a stray dollop of cum escaping and splattering her vulva."
    play sound cum
    show auroraselene cthreesome6 with cum
    play sound cum
    show auroraselene cthreesome6 with cum
    stop ambience fadeout 3.0
    "Sinking into the white mare, I breathe a sigh of relief as I unload the second half of my orgasm into her womb."
    show auroraselene cthreesome6 with dissolve

    "I did it, I came in both of them…"
    morrigan "What the hell kind of trick was that?  I {i}loved{/i} it! Filling both those breeding whores up was so perfect."
    scene bg black with dissolve
    "…"

label finale:
    scene bg ccastlethrone with dissolve
    ### shading over their faces, they look mad
    play music danger
    "And so, it begins..."
    show selene bangry at right with dissolve
    selene "Who are you calling breeding whores?"
    show aurora bangry at left with dissolve
    aurora "Morrigan… You’ve gone too far this time…"
    scene bg ccastlethrone with dissolve
    show morrigan angry with dissolve
    morrigan "Eh? Ehhh?!? M-My control, it’s gone? What hap- "
    show morrigan sad with dissolve
    morrigan "No… The cum?! [playername]! You used my own weapon against me?"
    show morrigan happy with dissolve
    morrigan "No matter, hehehe! I’ve absorbed so much power that you two can’t oppose me!"
    morrigan "I’ll make you breeding whores with or without your consent! With or without brainwashing!"
    morrigan "It’s too late! I’m too powerful! You’re all mine now! Feel the wrath of Morrig- guh?"
    scene bg ccastlethrone with dissolve
    show white with dissolve:
            alpha 0.5
            parallel:
                0.30
                alpha 0.5
                repeat
            parallel:
                0.5
                alpha 0.475
                repeat
    show lilyb:
        xpos 400
        ypos 40
    show lily angry:
        xpos 400
        ypos 40
    with dissolve
    lily "Now, girls! Begin formation! Ruby, Selene, Aurora, make a barrier!"
    show ruby happy with dissolve:
        xpos 850
        ypos 40
    ruby "Queen, Princess and [playername], over here!"
    scene bg ccastlethrone
    show morrigan angry
    show white:
            alpha 0.6
            parallel:
                0.40
                alpha 0.5
                repeat
            parallel:
                0.5
                alpha 0.475
                repeat
    with dissolve
    morrigan "W-Wha? What the hell?"
    scene bg ccastlethrone:
        xpos 0 ypos 0
        parallel:
            linear 0.4 xpos 0 ypos 0
            linear 0.4 xpos 3 ypos 3
            linear 0.4 xpos -3 ypos -3
            repeat
    show white:
            alpha 0.6
            parallel:
                0.40
                alpha 0.5
                repeat
            parallel:
                0.5
                alpha 0.475
                repeat
    show lily white
    with dissolve
    "The three of us take cover behind a growing surge of energy culminating in Lily’s horn."
    show bg ccastlethrone:
        xpos 0 ypos 0
        parallel:
            linear 0.3 xpos 0 ypos 0
            linear 0.3 xpos 5 ypos 5
            linear 0.3 xpos -5 ypos -5
            repeat
    show white:
            alpha 0.7
            parallel:
                0.50
                alpha 0.5
                repeat
            parallel:
                0.6
                alpha 0.475
                repeat
    "Each of the Elements of Har’Mony feed energy to her, and she acts like a conduit."
    show bg ccastlethrone with None:
        xpos 0 ypos 0
        parallel:
            linear 0.2 xpos 5 ypos -5
            linear 0.2 xpos 5 ypos 5
            linear 0.2 xpos -5 ypos -5
            linear 0.2 xpos -5 ypos 5
            repeat
    show white with None:
            alpha 0.8
            parallel:
                0.60
                alpha 0.5
                repeat
            parallel:
                0.7
                alpha 0.475
                repeat
    play sound morriganattack1
    show magic attack1 with hpunch
    play sound morriganattack2
    show magic attack2 with hpunch
    play sound morriganattack3
    show magic attack3 with hpunch
    play sound morriganattack1
    show magic attack4 with hpunch
    play sound morriganattack2
    show magic attack5 with hpunch
    "No matter how much Morrigan tries to attack with powerful whip magics, magic arrows, or anything lethal that she can fathom, her magic is merely absorbed by the great energy."
    scene bg white with dissolve
    show morrigan oof with dissolve
    morrigan "I-Impossible!! Y-You’re all supposed to be… brain… washed…"
    scene bg white with dissolve
    show lily white with dissolve
    lily "Morrigan, it’s over!"
    stop music fadeout 3.0
    play sound gameendblast
    ### blast noise
    scene bg white with dissolve
    "An overwhelming powerful surge of energy concentrated directly at Morrigan floods the room with a blinding white aura."
    play sound transition1
    "..."
    scene bg ccastlethrone with dissolve
    show lilyb:
        xpos 150
        ypos 50
    show lily angry:
        xpos 150
        ypos 50
    with dissolve
    lily "Did we do it?"
    lily "No… N-No way!"
    play music prismaserenade
    show morrigan oof with dissolve:
        xpos 750
        ypos 0
    morrigan "Tch, that really fucking hurt! You cunt!"
    ## crunchy smash sound
    play sound thunder2
    show magic attack1 with hpunch
    show lily shy:
        linear 0.5 xpos -500
    show lilyb:
        linear 0.5 xpos -500
    with morriganspell
    hide magic attack1 with hpunch
    "With a quick surge of magical energy, Morrigan lashes Lily across the chest with a quick whip."
    "It’s powerful, but aimless as it lashes Lily’s chest and shoulder, knocking her down to the ground. She’s okay, but too weak to get back up."
    show morrigan death with dissolve:
        linear 0.5 xpos 500
    morrigan "Did you really think some Deus Ex Machina bullshit could stop my rise to power?"
    morrigan "I am so sick of you all!"
    ## alt Morrigan being really fucking angry
    morrigan "Forget breeding whores, I’m just gonna fucking kill you."
    "With overwhelming murderous intent, Morrigan closes the distance between herself and us."
    scene bg ccastlethrone
    show selene angry:
        xpos 750
        ypos 50
    show aurorab:
        xpos 0
        ypos 50
    show aurora angry:
        xpos 0
        ypos 50
    with dissolve
    aurora "We’ll do everything in our power, to stop you!"
    play sound magic2
    ## magic sound
    show white with dissolve
    hide white with dissolve
    play sound magic3
    show sunmoonspell with dissolve:
        xpos 500
        ypos 100
    "Together the royal sisters combine their magic, a powerful spell of sun and moon surges towards Morrigan."
    play sound thunder2
    show magic attack2 with hpunch
    show sunmoonspell with dissolve:
        linear 0.3 xpos -500
    show bg ccastlethrone with hpunch
    hide magic attack2
    show aurora surprised
    show selene surprised
    with morriganspell
    "But it’s instantly deflected to the side."
    ## bricky bassy smash sound
    "The impact shakes the entire room as it leaves sizable cracks and holes in the brickwork, thank goodness that didn’t hit anyone."
    scene bg ccastlethrone
    show morrigan oof
    with dissolve
    morrigan "IT’S USELESS! GET OUT OF MY WAY!"
    scene bg ccastlethrone
    show selene angry:
        xpos 750
        ypos 50
    show aurorab:
        xpos 0
        ypos 50
    show aurora angry:
        xpos 0
        ypos 50
    play sound thunder2
    with dissolve
    show selene surprised with morriganspell:
        xpos 750
        ypos 50
        linear 0.5 xpos -700
    show bg ccastlethrone with hpunch
    play sound thunder2
    show aurorab:
        xpos 50
        ypos 50
        linear 0.5 xpos 1850
    show aurora surprised:
        xpos 50
        ypos 50
        linear 0.5 xpos 1850
    with morriganspell
    scene bg ccastlethrone with hpunch
    "With a retaliation, Morrigan uses telekinesis to launch them both into the walls, with such power that the impact is almost comparable to the reflected blast of the sisters. Both of them instantly incapacitated."
    "Even now, her power is devastating and incomparable. Not the elements nor the royal sisters can stop her."
    show honeycrisp ncangry:
        xpos 250
        ypos 50
    show rikub:
        xpos 750
        ypos 70
    show riku angry:
        xpos 750
        ypos 70
    with dissolve
    play sound thunder2
    show honeycrisp ncshocked with dissolve:
        xpos 250
        ypos 50
        linear 0.5 xpos -500
    play sound thunder2
    show rikub:
        xpos 750
        ypos 70
        linear 0.5 xpos 1850
    show riku embarrassed:
        xpos 750
        ypos 70
        linear 0.5 xpos 1850
    with dissolve
    show bg ccastlethrone with hpunch
    ## less powerful magic sound
    "Honeycrisp and Riku attempt to launch themselves at the insane pseudo-Goddness, but their failures are the most miserable of all as they’re thrown back like trash."
    show morrigan oof with dissolve
    "The other mares stand terrified in position, knowing that any braveness would end in folly."
    "What is she doing? She keeps walking forward… She… She’s coming for me!"
    ## really pissed morrigan
    show morrigan pissed with dissolve
    play sound distantbang
    morrigan "You… YOU DID THIS!"
    play sound distantbang
    morrigan "You ruined everything!"
    play sound distantbang
    morrigan "I brought you into this world, so now I’m gonna take you out of it!"
    stop music fadeout 1.0
    play sound thunder2
    show blood with morriganspell
    mc "Guh!"
    play sound distantbang
    pause 0.5
    play sound distantbang
    "With a magically imbued claw-hand, she plunged it through my chest faster than my mind could interpret the action."
    ## ears ringing sound
    # image goes blurry
    show blood2 with hpunch
    play sound distantbang
    pause 1.1
    play sound distantbang
    "My vision goes blurry, and my ears ring painfully, drowning out the desperate cries of the girls."
    show blood3 with hpunch
    play sound distantbang
    pause 1.1
    play sound distantbang
    "As I wearily look downwards, Morrigan retracts her hand from my chest, leaving a sizable wound."
    ## morrigan shocked
    show blood4 with hpunch
    play sound distantbang
    pause 1.1
    play sound distantbang
    show white with dissolve:
            alpha 0.3
            parallel:
                0.50
                alpha 0.5
                repeat
            parallel:
                0.6
                alpha 0.475
                repeat
    morrigan "No… No! NO!!"
    play sound distantbang
    pause 1.1
    play sound distantbang
    morrigan "Ahhhhhhhh, AHHHHHHHHHHHHHHHHHH!! How could this happen, how could I do this?"
    play sound distantbang
    pause 1.1
    play sound distantbang
    morrigan "Noooooooooooooo!!"
    play sound distantbang
    pause 1.1
    play sound distantbang
    morrigan "This is horrible, this is the worst! I hate this! Stop it, stop it!"
    play sound distantbang
    pause 1.1
    play sound distantbang
    scene bg white with dissolve
    "Suddenly the world was lost in a pale white light, I couldn’t tell if it was my body failing me or an aura of magic."
    "But as the light slowly dissipated, my vision slowly returned. The hole in my chest began sealing, the intense pain fading."
    "Is Morrigan healing me?"
    "No… It’s…"
    play music wagon2
    show moxie sad with s:
        xpos 500
        ypos 20
    mc "Moxie!"
    moxie "Oh my goodness… I-I can’t believe it…"
    show bg ccastlethrone with dissolve
    show moxie sad:
        linear 0.5 xpos 750 ypos 20
    show morrigan oof with dissolve:
        xpos 250
        ypos 20
    morrigan "W-What the hell is this? I lost control of my host?!"
    "Before me stood both Moxie and Morrigan who had split."
    show moxie tears with dissolve
    moxie "Thank goodness, Lily’s blast weakened Morrigan enough for us to split…"
    moxie "Are you okay, [playername]? I’m so sorry!"
    show morrigan pissed with dissolve
    morrigan "W-What is this bullshit? There's no way I lost control, y-you should be weak..."
    show moxie angry with dissolve
    moxie "Haven’t you noticed Morrigan? When we split, I took half of your power; you’re weak."
    show morrigan happy with dissolve
    morrigan "Weak? *Giggles* Look around you, those are the real weaklings."
    morrigan "Lily, ass kicked. Aurora and Selene, incapacitated."
    morrigan "Do you really think you can stop me all by yourself?"
    show moxie neutral with dissolve
    moxie "I can try, damnit…"
    show morrigan laughing with dissolve
    morrigan "Ihihihi, even if our power is equal, you’re a pathetic and useless magic caster. You’re three thousand years too early to match up against me."
    show moxie smug with dissolve
    moxie "Pathetic and useless, huh? Is that why you needed my power to enact your plan?"
    moxie "Without me, you’re the useless one."
    show morrigan oof with dissolve
    morrigan "I don’t need you anymore! You just held me back with your lovey-dovey feelings!"
    play sound morriganattack1
    show magic attack1 with hpunch
    play sound morriganattack2
    show magic attack2 with hpunch
    play sound morriganattack3
    show magic attack3 with hpunch
    "Morrigan attacks Moxie multiple times with powerful lashes, but each is deflected with ease."
    # morrigan surprised needed
    hide magic attack3 with dissolve
    morrigan "… Huuuhh…? What the hell?"
    show moxie smug with dissolve
    moxie "Hohoh… So that’s how it is…"
    moxie "The reason the elements didn’t vaporise you is because Lily didn’t use the full power of the elements, she didn’t want to kill me too."
    show morrigan oof with dissolve
    morrigan "So what? You’re telling me that she held back because she didn’t want to hurt a friend? That’ll be your downfall!"
    show moxie angry with dissolve
    moxie "On the contrary, that exact friendship is our strength."
    moxie "Because of Lily, you’re weak and injured; I’m still at full strength."
    moxie "And because of that, I had the opportunity to overpower your control and split from you. Lily... You truly are amazing."
    show morrigan angry with dissolve
    stop music fadeout 3.0
    morrigan "So what? I’m still far more talented and experienced than you! Take this!!"
    play sound thunder2
    play music minikillyourself
    scene bg ccastlethrone
    show moxie angry
    play sound morriganattack1
    show magic attack1 with hpunch
    play sound morriganattack2
    show magic attack2 with hpunch
    play sound morriganattack3
    show magic attack3 with hpunch
    play sound morriganattack1
    show magic attack4 with hpunch
    play sound morriganattack2
    show magic attack5 with hpunch
    ### DIFFERENT SOUND FOR MOXIE'S MAGIC
    scene bg ccastlethrone
    show morrigan pissed
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    play sound moxiespell1
    show magic attack9 with hpunch
    play sound moxiespell2
    show magic attack10 with hpunch
    "The two super-powered mares duke it out, slugging at each other with various magical blows."
    "At this point, all the bystanders beholding to the sheer display of power have hidden behind cover."
    scene bg ccastlethrone with dissolve
    show ruby closeshy with dissolve
    "Since Moxie’s magic wasn’t quite enough to heal me fully, Ruby comes to my side, and tries her best to bandage and heal me."
    ruby "Phew, it's not too serious, you'll be fine [playername]."
    scene bg ccastlethrone with dissolve
    show moxie angry with dissolve:
        xpos 750
        ypos 20
    show morrigan oof with dissolve:
        xpos 250
        ypos 20
    play sound morriganattack1
    show magic attack1 with hpunch
    play sound morriganattack2
    show magic attack2 with hpunch
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    hide magic with dissolve
    "What Morrigan said is true, her experience with magic is giving her a slight edge. But Moxie’s healthy condition is allowing her to push Morrigan further than she might expect."
    play sound morriganattack1
    show magic attack1 with hpunch
    play sound morriganattack2
    show magic attack2 with hpunch
    play sound morriganattack3
    show magic attack3 with hpunch
    "Lash, beam, arrow, slash, all deflected by Moxie’s shield."
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    "But the reverse is true, any offense by Moxie is impervious to Morrigan’s concentrated shield."
    play sound morriganattack1
    show magic attack1 with hpunch
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound morriganattack2
    show magic attack2 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound morriganattack3
    show magic attack3 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    play sound morriganattack1
    show magic attack4 with hpunch
    play sound moxiespell1
    show magic attack9 with hpunch
    play sound morriganattack2
    show magic attack5 with hpunch
    play sound moxiespell2
    show magic attack10 with hpunch
    "It’s like a slugging match, they’re trading extremely powerful blows with complete concentration."
    show magic attack3 with hpunch
    play sound moxiespell1
    show magic attack10 with hpunch
    play sound morriganattack2
    "Wounds and cuts gradually wear the two down as the occasional spell penetrates or blindsides their shield."
    scene bg ccastlethrone with dissolve
    show honeycrisp closeangry with dissolve:
        xpos 0
        ypos 50
    honeycrisp "We’ve got to do something, they’re evenly matched!"
    show butters closedresssad with dissolve:
        xpos 450
        ypos 20
    butters "Anything we try will just be deflected by those magic shields; we’d be nothing but a hinderance!"
    hide honeycrisp with dissolve
    show cream closesad with dissolve:
        xpos 0
        ypos 50
    cream "But maybe it’ll be a distraction long enough for Moxie to get a good blow!"
    hide butters with dissolve
    show ruby closeangry with dissolve:
        xpos 550
        ypos 85
    ruby "If we get involved, we’ll be turned into dust…"
    hide cream with dissolve
    show lilyb close:
        xpos 0
        ypos 65
    show lily closesad:
        xpos 0
        ypos 65
    with dissolve
    lily "Ugh… Girls…"
    show ruby closeshocked with dissolve
    ruby "Lily, are you okay darling? Let me heal you too."
    show lily closeangry with dissolve
    lily "My head is throbbing, but… That doesn’t matter right now, stabilise [playername]’s condition and charge up another Har'Mony blast."
    show ruby closeangry with dissolve
    ruby "Mhm, let’s do it."
    scene bg ccastlethrone with dissolve
    show moxie angry with dissolve:
        xpos 750
        ypos 20
    show morrigan oof with dissolve:
        xpos 250
        ypos 20
    "Moxie’s expression never once faltered, the pure composure that she had so often used in her theatrical performances put Morrigan on edge."
    "Never once did Moxie show a weakness, even as her muscles began to ache or as she took the occasional hit."
    play sound morriganattack1
    show magic attack1 with hpunch
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound morriganattack2
    show magic attack2 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound morriganattack3
    show magic attack3 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    play sound morriganattack1
    show magic attack4 with hpunch
    play sound moxiespell1
    show magic attack9 with hpunch
    play sound morriganattack2
    show magic attack5 with hpunch
    play sound moxiespell2
    show magic attack10 with hpunch
    play sound thunder2
    hide magic attack10 with cum
    "Immediately the air between the two pseudo-gods exploded with sparks as the intensity of the magic soared."
    "While it’d be easy to assume the girls were getting gradually weaker as they kept fighting, the opposite was true."
    "They were quickly acclimating to their new exponentially large magic pools through a trial by fire."
    "Even they didn’t know the full extent of their new alicorn power."
    stop music fadeout 2.0
    moxie "I will purge you Morrigan, and correct all the wrong doings that you stained my hands with!"
    show morrigan death with dissolve
    morrigan "Ihihihi, know your place Moxie!"
    show morrigan:
        linear 0.2 xpos -600
    show moxie:
        linear 0.2 xpos 1800
    play music morriganbattle
    play sound towerspell
    scene bg ccastlethrone with hpunch
    scene bg ccastlethrone with hpunch
    scene bg ccastlethrone with hpunch
    "The very roof of the castle caved in as their battle took to the skies, rubble and debris littering the once sacred throne room."
    "Fortunately, this put a barrier between the warring mares and the bystanders watching in awe."
    play ambience thunderstorm
    show bg darksky1 with dissolve
    show moxie angry with dissolve:
        xpos 470
    play sound morriganattack1
    show magic attack1 with hpunch
    play sound morriganattack2
    show magic attack2 with hpunch
    play sound morriganattack3
    show magic attack3 with hpunch
    play sound morriganattack1
    show magic attack4 with hpunch
    play sound morriganattack2
    show magic attack5 with hpunch
    show magic shield with qd
    play sound smash
    show magic shatter with qd
    hide magic shatter with qd
    show moxie angry:
        xpos 470
        linear 0.2 xpos 1800
    scene bg darksky2 with qd
    show moxie angry with qd:
        linear 0.2 xpos 450
    play sound thundercharge
    show purple lightning with qd
    show bg darksky2 with hpunch
    show purple lightning1 with qd
    show bg darksky2 with hpunch
    show purple lightning2 with qd
    show bg darksky2 with hpunch
    show purple lightning3 with qd
    show bg darksky2 with hpunch
    play sound thunder2
    scene bg white with hpunch
    show bg ccastlethrone with qd
    show morrigan oof with dissolve
    play sound distantbang
    pause 0.2
    play sound thunder2
    show white with dissolve
    hide morrigan oof with hpunch
    hide white with qd
    play sound genericmagic
    show morrigan2 with morriganspell:
        xpos 200
    show bg ccastlethrone with hpunch
    play sound genericmagic
    show morrigan3 with morriganspell:
        xpos 800
    show bg ccastlethrone with hpunch
    play sound genericmagic
    show morrigan laughing with morriganspell:
        xpos 500
    show morrigan death with dissolve
    play sound thundercharge
    show green lightning with qd
    show morrigan2:
        linear 0.2 xpos -600
    show morrigan3:
        linear 0.2 xpos 1800
    scene bg black with dissolve
    play sound gameendblast
    show magic attack1 with hpunch
    show magic attack2 with hpunch
    show magic attack3 with hpunch
    show magic attack4 with hpunch
    show magic attack5 with hpunch
    show magice attack1 with hpunch
    show magice attack2 with hpunch
    show magice attack3 with hpunch
    show magice attack4 with hpunch
    show magice attack5 with hpunch
    play sound thunder2
    scene bg white with dissolve
    show moxie smug with dissolve
    show magic shield with dissolve
    show bg darksky2 with dissolve
    play sound smash
    hide magic shield with pixellate
    pause 0.5
    scene bg darksky1 with dissolve
    show morrigan pissed with dissolve
    pause 0.5
    scene bg ccastlethrone
    show rikub:
        xpos 0
        ypos 75
    show riku embarrassed:
        xpos 0
        ypos 75
    with dissolve
    riku "N-No way!? I can’t keep track of their movements at all anymore!"
    show cream embarrassed with dissolve:
        xpos 200
        ypos 50
    cream "Holy shit!!"
    show aurorab:
        xpos 400
        ypos 0
    show aurora angry:
        xpos 400
        ypos 0
    with dissolve
    aurora "Selene, the last of our power, let’s make a protective barrier!"
    show selene angry with dissolve:
        xpos 750
        ypos 0
    selene "Right! Stay back girls, things are about to heat up!"

    scene bg darksky2 with dissolve
    show morrigan happy with dissolve
    morrigan "*Giggle* How do you like this? The power of a goddess!"
    scene bg darksky1 with dissolve
    show moxie angry with dissolve
    play sound morriganattack1
    show magic attack1 with hpunch
    play sound morriganattack2
    show magic attack2 with hpunch
    show magic shield with qd
    hide magic shield with dissolve
    moxie "You think you’ll win?"
    scene bg darksky2 with dissolve
    show morrigan death with dissolve
    morrigan "*Cackle* Yes, absolutely! I’m prepared to wreck this whole city to win! Watch meeee! Ihihihih!"
    scene bg black with dissolve
    play sound towerspell
    pause 0.5
    play sound2 distantbang
    show tower 1 with dissolve
    play sound2 distantbang
    show tower 2 with dissolve
    play sound2 distantbang
    show tower 3 with dissolve
    play sound2 thunder2
    show tower 4 with cum
    "With a crunch of powerful magic that warps the very air, two giant towers of Arcadia are torn from their foundation and lifted into the air."
    "The very earth tremored and shifted as the castle was split."
    scene bg castledebris
    show penelope cshocked with dissolve
    "Debris almost swallowed up Penelope who had been watching from the side-lines. Morrigan had in-fact noticed she was there and ignored her regardless of the danger she might have been put in."
    penelope "W-What the? Morrigan, what are you doing? Ahhh!"
    scene bg black with qd
    play sound thunder2
    show tower 4 with cum
    "At either side of Morrigan’s shoulders were the two castle turrets, 100 meters long, and threatening to tear a hole through the sky itself."
    show morrigan pissed with dissolve
    "Enjoying the feeling of her overwhelming power, Morrigan soared up between the gap of the two towers, sneering over the entire castle with absolute dominance."
    morrigan "Ihihihihahayaaaa, I don’t think you can deflect this!"
    morrigan "Even if you do, the pure density of the rubble and bricks will shower the whole city in destruction! *Cackle*"
    scene bg darksky4 with dissolve
    show moxie angry with dissolve
    moxie "Are you done running your mouth?"
    scene bg black with qd
    play sound thunder2
    show tower 4 with cum
    play sound2 genericmagic
    show tower 5 with morriganspell
    show morrigan death with dissolve
    morrigan "Ihihihi, I’ll wipe that smug look off your face…"
    play sound towerspell
    scene bg black with qd
    "The towers launched towards Moxie, shattering as the overwhelming power of magic barely held the crumbling structures together."
    play sound rainoffire
    show mheavy attack1 with qd
    play sound2 rainoffire
    show mheavy attack2 with qd
    play sound rainoffire
    show mheavy attack3 with qd
    play sound2 rainoffire
    show mheavy attack4 with qd
    play sound rainoffire
    show mheavy attack1 with qd
    play sound2 rainoffire
    show mheavy attack2 with qd
    play sound rainoffire
    show mheavy attack3 with qd
    play sound2 rainoffire
    show mheavy attack4 with qd
    play sound2 rainoffire
    "What resulted was a beautiful slurry of shrapnel, capable of piercing the earth; firing like a sea of death."
    scene bg castledebris with dissolve
    show penelope csad with dissolve
    "From one side of the battlefield Penelope begged the Queen to cease her destruction."
    penelope "What are you doing my Queen?! You promised me that it wouldn't be like this! Stop, stop!"
    scene bg ccastlethrone with dissolve
    show lilyb
    show lily angry
    with dissolve
    "From the other side, Lily yelled out to Moxie."
    lily "Don’t worry Moxie, the castle has been evacuated! Do your best!"
    scene bg darksky4 with dissolve
    show moxie neutral with qd
    moxie "Right, in that case… Two can play at that…"
    play sound thunder2
    play sound2 towerspell
    show moxie angry
    show bg burningsky1 with cum
    "The sky was blemished with a blazing incandescent red as the castle crumbled from the structural damage Morrigan had caused."
    "There was another tower falling that Moxie took advantage of, imbuing the falling structure with magic, she used it as a shield to block the tidal wave of rocks and shrapnel launched by Morrigan."
    play sound rainoffire
    show mheavy attack1 with qd
    play sound2 rainoffire
    show mheavy attack2 with qd
    play sound rainoffire
    show mheavy attack3 with qd
    play sound2 rainoffire
    show mheavy attack4 with qd
    play sound rainoffire
    show mheavy attack1 with qd
    play sound2 rainoffire
    show mheavy attack2 with qd
    play sound rainoffire
    show mheavy attack3 with qd
    play sound2 rainoffire
    show mheavy attack4 with qd
    play sound2 rainoffire
    play sound2 towerspell
    "And it worked; tens of thousands of rocks were blocked by the floating tower. Not a single stray rock managed to find itself near Moxie or the bystanders."
    scene bg burningsky2 with qd
    "With the collision over, the towers were reduced to nothing but a mass of rocks and debris as they collapsed to the ground lifeless."
    show morrigan happy with qd
    morrigan "Not afraid to get your hands dirtied with blood, are you? Ihihihi, how many people do you think were in that tower that you just killed?! *Cackle, cackle*"
    scene bg burningsky3 with qd
    show moxie angry with qd
    moxie "Hmph, no one was in that tower, don’t try to bluff me with that manipulative bullshit."
    moxie "It’s my turn now, you won’t catch me resorting to such dirty tactics!"
    play sound genericmagic
    show magic javelin1 with qd
    pause 1.0
    play sound genericmagic
    show magic javelin2 with dissolve
    play sound genericmagic
    show magic javelin3 with dissolve
    play sound genericmagic
    show magic javelin4 with dissolve
    play sound genericmagic
    show magic javelin5 with dissolve
    "With pure magic, Moxie formed her own weapon. An innumerable group of magical javelins formed around her."
    "With such an overwhelming display, Moxie felt certain that victory was within her grasp."
    moxie "Using your surroundings in such a reckless way was idiotic, you gave me a chance to concentrate my magic into these weapons."
    scene bg burningsky2 with qd
    show morrigan death with dissolve
    morrigan "So you were using all that time to charge up your magic? Perhaps I underestimated you Moxie, truly impreeeesssiivee!!"
    morrigan "But do you think I’m so naïve to not do the exact same thiiinnngg?"
    play sound gameendblast
    show mheavy attack5 with hpunch
    play sound2 rainoffire
    show mheavy attack6 with hpunch
    play sound rainoffire
    show mheavy attack7 with hpunch
    play sound2 rainoffire
    show mheavy attack8 with hpunch
    play sound rainoffire
    show mheavy attack5 with hpunch
    play sound2 rainoffire
    show mheavy attack6 with hpunch
    play sound rainoffire
    show mheavy attack7 with hpunch
    play sound2 rainoffire
    show mheavy attack8 with hpunch
    "With a snap, Moxie launched the army of javelins directly towards Morrigan with complete accuracy. Each acting with the velocity and power of a lightning bolt."
    play sound thunder2
    scene bg white with dissolve
    show bg darksky3 with dissolve
    play sound thunder2
    show golem 1 with hpunch
    play sound2 thunder2
    show golem 2 with hpunch
    play sound thunder2
    show golem 3 with hpunch
    play sound2 thunder2
    show golem 4 with hpunch
    play sound thunder
    show golem 5 with cum
    "Morrigan herself exploded with a radiant green aura as she used the stone from the mountain itself. With an extremely powerful alteration spell, she turned the mountains into powerful giant golems."
    "Each of the golems reached 50 meters high, able to protect Morrigan with massive stone bodies so gargantuan they could eclipse the sun."
    "The mountain range itself had been converted into an army. Morrigan who hid behind them was like a true insect in comparison."
    scene bg darksky4 with dissolve
    show moxie angry with qd
    moxie "Ghh, do you really think some rocks are going to stop magic this powerful?"
    scene bg darksky3 with qd
    show golem 5 with qd
    play sound thunder2
    scene golem 6 with morriganspell
    "Milliseconds before the impact of Moxie’s attack, green lightning sprayed and crackled from Morrigan’s horn, illuminating each of the golems and applying a concentrated dose of her magic to each one."
    show magic shield2
    show mheavy attack5 with qd
    play sound2 rainoffire
    show mheavy attack6 with qd
    play sound rainoffire
    show mheavy attack7 with qd
    play sound2 rainoffire
    show mheavy attack8 with qd
    play sound smash
    hide mheavy attack8 with hpunch
    hide magic shield2 with dissolve
    "Like a rain of comets, each of the javelins shattered and crumbled as the agile mountain golems flawlessly intercepted the attack."
    scene bg darksky4 with dissolve
    show moxie shy with dissolve
    moxie "How did we get here… This is ridiculous…"
    scene golem 6 with dissolve
    show morrigan laughing with dissolve
    morrigan "Struggling to keep up? Hah! You could barely lift a book with telekinesis last week, you’re completely outmatched!"
    scene bg darksky4 with dissolve
    show moxie angry with dissolve
    moxie "No, that's wrong! You were sharing my body… Which means we shared magic pools, so your magic was equally as pathetic!"
    scene golem 6  with dissolve
    show morrigan happy with dissolve
    morrigan "Is that so? Allow me to show you how to do that javelin attack properly, and you’ll see that we’re far from equal!"
    hide morrigan with morriganspell
    play sound thunder2
    show golem 7 with hpunch
    "A storm of energy consumed the golems. The magic imbuing them morphed into javelins of pure lightning crackling with potent magical power."
    "Each golem resumed a Zeus-like throwing stance as they prepared to launch an attack that Moxie was completely unprepared to defend against."
    "Moxie scoffed; she must have been certain that she’d be able to block this attack with her magic shield, even without time to bolster a proper defence."
    "The very earth itself quaked with a thunderous sound as the golems slammed their feet down and deftly spun the lightning javelins in their arms simply for style, before throwing each of them up into the air."
    play sound thunder
    scene bg black with cum
    show bg javelinsky with hpunch
    moxie "What the-? Why the sky?"
    "The javelins pierced the clouds as they rose, and as they fell, they did so multiplicatively as each split into a rain of murder. A few javelins had become a thousand."
    play sound gameendblast
    show bg javelinsky2 with hpunch
    show bg javelinsky3 with hpunch
    show bg javelinsky2 with hpunch
    show bg javelinsky3 with hpunch
    show bg javelinsky2 with hpunch
    show bg javelinsky3 with hpunch
    "Each of the many thousand lightning bolts all targeted directly at Moxie."
    scene bg darksky4 with dissolve
    show moxie angry with dissolve
    pause 0.5
    play sound genericmagic
    hide moxie with dissolve
    pause 0.5
    play sound thunder2
    show bg javelinsky2 with hpunch
    show bg javelinsky3 with hpunch
    "However, just before impact she vanishes!"
    ## boom boom boom
    "Anyone watching would assume that Moxie had been destroyed, the barrage consumed an entire 30-meter volume in a storm for exhaustively long seconds."
    scene bg darksky3 with dissolve
    show morrigan pissed with dissolve
    "However, Morrigan sensed something was wrong."
    morrigan "Ghh, did I… win?"
    "Morrigan froze, growing increasingly tense and anxious."
    play sound genericmagic
    show moxie angry with dissolve:
        xpos 800
        ypos 0
    "Using a power practiced for many nights, Moxie reappeared behind Morrigan."
    moxie "It’s over."
    morrigan "N-No way, invisibility?!"
    show morrigan oof
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    play sound moxiespell1
    show magic attack9 with hpunch
    play sound moxiespell2
    show magic attack10 with hpunch
    "Morrigan grit her teeth as Moxie released an aggressive magical attack from behind."
    "Morrigan was stuck, she couldn't turn around to attack, all she could was defend in this vulnerable position."
    "Moxie's magic was point blank and concentrated directly at all Morrigan’s vital areas. If Morrigan let down her shield even for a second, she'd be decimated."
    "This immediate close-range barrage hit Morrigan directly, and even though she tried to shield it, she was on the backfoot."
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    play sound moxiespell1
    show magic attack9 with hpunch
    play sound moxiespell2
    show magic attack10 with hpunch
    "Spear, after sword after javelin, Moxie gave it her all. Morrigan couldn’t even begin to retaliate. Even if she did, the magical mess of close-range lights blinded her eyes."
    "At this point, it was no longer mere weapons attacking Morrigan, but a tornado of magic endlessly crashing into her shield."
    morrigan "Mountain golems, stop her!"
    scene golem 6 with dissolve
    "From this advantageous position, even the golems were incapable of retaliating."
    play sound towerspell
    show golem 8 with dissolve
    "No longer imbued by Morrigan’s magic, any attempt to close the distance shredded their stone bodies. Not even rain could enter the sphere of destruction as it was instantly boiled."
    show moxie angry with qd:
        xpos 800
        ypos 0
    show morrigan oof with qd
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    play sound moxiespell1
    show magic attack9 with hpunch
    play sound moxiespell2
    show magic attack10 with hpunch
    "At an increasing rate, magical slashes pierced Morrigan’s shield, she was growing weaker by the second."
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    play sound moxiespell1
    show magic attack9 with hpunch
    play sound moxiespell2
    show magic attack10 with hpunch
    "All whilst Moxie only increased the offensive, growing more concentrated and deadly."
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    play sound moxiespell1
    show magic attack9 with hpunch
    play sound moxiespell2
    show magic attack10 with hpunch
    "Morrigan was going to be blended in this cacophony."
    play sound moxiespell1
    show magic attack6 with hpunch
    play sound moxiespell2
    show magic attack7 with hpunch
    play sound moxiespell3
    show magic attack8 with hpunch
    play sound moxiespell1
    show magic attack9 with hpunch
    play sound moxiespell2
    show magic attack10 with hpunch
    show magic shield2
    play sound smash
    show magic shatter2
    scene bg white with dissolve
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    "And then, in that instant, Morrigan's shield shattered!"
    "The battle was over, Arcadia had won."
    scene bg darksky1 with dissolve
    play ambience ambiencerain fadein 3.0
    "With a flash, all magic finally ceased."
    "The golems lost their magic and returned to stone as the sky grew dull."
    "From the empty castle below, the elements, myself and the royal sisters had been watching the fight unblinkingly."
    "As emotions gently cooled, the sound of rain and wind returned, the occasional snap of lightning ringing and blinding."
    show morrigan oof
    show blood
    show moxie angry:
        xpos 800
        ypos 0
    with qd
    "Morrigan had been pierced by a beam of energy, in the exact same location she had hit me previously."
    morrigan "Grrhh, guhh… *Cough* Ghhh… You got me…"
    "The pierced mare tried to grin, she tried taking her death with pride; but she repeatedly failed to keep composure, only making her appear more pathetic."
    hide blood with dissolve
    hide morrigan with moveoutbottom
    "Moxie sheathes her magical beam, causing Morrigan to fall to the ground; pale and weak."
    scene bg ccastlethrone with dissolve
    show morrigan oof with dissolve:
        xpos 100
        ypos 400
    show moxie angry with qd:
        xpos 800
        ypos 0
    moxie "It's finally done..."
    play music lips
    show morrigan death with morriganspell
    play sound thunder2
    show magic attack2 with hpunch
    show blood with qd
    show moxie shocked with qd:
        linear 0.2 xpos 800 ypos 400
    hide blood with qd
    hide magic attack2
    "In a millisecond, a beam of magic punctured Moxie’s thigh. It was some of the last scrapings of Morrigan’s waning power, and Moxie had been distracted enough for it to be a direct hit."
    morrigan "You fool! Ahahaha, you dare look down on me?! *Cough*"
    "Moxie fell down clutching her thigh, pain like nothing she had ever felt before seared through her body."
    show moxie tears with dissolve
    moxie "Y-You bitch… Argh, ahhh! Ahh, damnit, you were acting?!"
    show morrigan pissed with dissolve
    morrigan "Echh, ghhh… I told you Moxie, I’ll do anything for this! You’re far too naïve to beat me!"
    morrigan "It’s over, I’ve won! Dieee, die!!"
    "It was only a small wound, but the pain was real, Moxie raised her magical shield once again and prepared to finish off Morrigan."
    "Both pierced and injured, both girls on the verge of defeat, prepared to enter one final and desperate clash of magic."
    "That is until…"
    show lily white with dissolve
    lily "Elements, fire now!"
    show morrigan oof with dissolve
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    morrigan "You?! Lily!! I-I’LL KILL YOU ALL…"
    play sound gameendblast
    scene bg white with dissolve
    show bg white with hpunch
    show bg white with hpunch
    show bg white with hpunch
    show bg white with hpunch
    "With one final blast, the wreckage of the castle was consumed in light."
    "As it settled, Morrigan was utterly vaporised."
    "Utterly, vaporised."
    $ persistent.morrigan = 0
    play ambience raindistantthunder
    scene bg ccastlethrone with dissolve
    play music PeaceSerenity
    show moxie closetears with dissolve:
        xpos 50
    moxie "Ohhh, goshhh… that was so tiring… Eugh, my thigh, it’s bleeding… can’t move an inch…"
    mc "Moxie, are you okay?"
    show moxie closesad with dissolve
    moxie "Y-Yeah, help me, I need a bandage…"
    show selene closeneutral with dissolve:
        xpos 400
    selene "Here, let me tend to your wounds."
    moxie "Where’s Morrigan, what happened? Did we win?"
    hide selene with qd
    show lilyb close:
        xpos 500
        ypos 65
    show lily closehappy :
        xpos 500
        ypos 65
    with dissolve
    lily "Yep, we got her! Blasted into a million pieces! And we couldn't have done it without you."
    show moxie closesatisfied with dissolve
    moxie "Thank you…"
    "Moxie closes her eyes, she’s not sleeping, but she’s clearly exhausted."
    scene bg ccastlethrone with dissolve
    mc "Just what the hell was Morrigan, and those ‘morphlings’ anyway? What a crazy situation to find myself in."
    show aurorab:
        xpos -50
        ypos 0
    show aurora neutral:
        xpos -50 ypos 0
    with dissolve
    aurora "Morrigan is, or rather was, the corrupt leader of the morphlings, a species similar to unicorns. We've had to repeatedly deal with her aggressions over the past millenia."
    show selene satisfied with dissolve:
        xpos 300 ypos 0
    selene "No matter how much we attempted peaceful cohabitation, Morrigan and her lineage would always abuse their powers… Forcing us into repeated bitter wars... to the detriment of us, and even her own species."
    show aurora angry with dissolve
    aurora "We’ve had trouble with Morrigan for an extremely long time. This incident may be the closest she has ever gotten to winning though."
    show lilyb:
        xpos 750
        ypos 50
    show lily surprised:
        xpos 750
        ypos 50
    with dissolve
    lily "Can we expect any retaliation from her brood?"
    show aurora neutral with dissolve
    aurora "Hmm… I doubt her brood cares much for what she's been doing. Didn't you notice that she was operating more or less alone?"
    lily "Ohh, that's true! Even Penelope came to help us."
    show selene sad with dissolve
    selene "It's true, there has been much political strife among the morphlings as of late."
    selene "That doesn't excuse my carelessness... I’m so sorry sis, I really should have noticed [playername]’s curse, and Moxie was being used as a host... I feel so pathetic..."
    show aurora happy with dissolve
    aurora "Please don't apologize... Morphling magic is inherently difficult for us to detect... I couldn't even tell that my pupil's housemate was a morphling! How do you think I feel?"
    aurora "As far as I’m concerned, no one here is to blame, not you, nor Moxie, nor [playername]."
    scene bg ccastlethrone with dissolve
    show penelope cangry with dissolve:
        xpos 750 ypos 50
    "Running in the throne room in a deranged panic, Penelope emerges, her eyes quickly scanning the room."
    penelope "Morrigan? Where is she? Did she surrender?!"
    show lilyb:
        xpos 250 ypos 50
    show lily angry:
        xpos 250 ypos 50
    with dissolve
    lily "She's gone... It's finally over."
    show penelope csad with dissolve
    penelope "No way... I thought..."
    scene bg ccastlethrone with qd
    show moxie closesad with dissolve
    moxie "P-Penny… Why?"
    "Moxie tries to stand up, but slumps down as her body fails her; fatigue overwhelming her body after the big fight."
    scene bg ccastlethrone with dissolve
    show penelope csad with dissolve:
        xpos 750 ypos 50
    penelope "Moxie? Oh my god, your thigh… Are you okay?"
    scene bg ccastlethrone with qd
    show moxie closesad with dissolve
    moxie "Ugh, Penny… Why did you betray us?"
    scene bg ccastlethrone with dissolve
    show penelope cshy with dissolve:
        xpos 750 ypos 75
    penelope "I never wanted this! I just wanted peace and prosperity for my species... Morrigan always told me that she'd make everything right when she was restored to the throne..."
    show aurorab:
        xpos 100 ypos 0
    show aurora neutral :
        xpos 100 ypos 0
    with dissolve
    aurora "Morrigan mislead you, peace was never her intent."
    show penelope csad with dissolve
    penelope "No way… My Queen…"
    "Penelope broke down, everyone watched, aghast by the emotional outburst. No one could have foreseen her reaction."
    show penelope cshy with dissolve
    penelope "I never wanted it to be like this... When we first arrived in Arcadia, she told me that she wouldn’t hurt anyone!"
    penelope "But... I heard her... She said she wanted to kill everyone…"
    show aurora shy with dissolve
    aurora "She would have let all of Arcadia burn in her hubris, even if that meant killing you in the collateral."
    show penelope csad with dissolve
    penelope "… Y-Yeah… I was in that tower she lifted; she knew I was! God damnit!"
    penelope "I nearly died… Yet the way she looked at me, so cold and uncaring…"
    "Penelope holds herself and shivers, clearer inspection of her body reveals some nasty cuts and injuries from the collateral damage on one of her legs."
    show aurora neutral with dissolve
    aurora "Is that really the type of person you want ruling over the country? Someone willing to sacrifice everyone, even their closest allies?"
    penelope "I know she was always childish, but I really thought I could change her…"
    mc "Penelope, don’t forget that everything that has happened was your plan…"
    penelope "Huh? What are you saying?"
    mc "{i}You{/i} were the one that suggested that Moxie should summon a familiar, {i}you{/i} were the person that realized my potential and convinced me to stay."
    mc "{i}You{/i} were the one that wanted to make me a pawn, and {i}you{/i} got me to work and hence sleep with the elements."
    show penelope cshy with dissolve
    penelope "S-So? I mean… s-sorry…"
    mc "You seem to think Morrigan was special, but from my perspective... You're the mastermind, and even in your genius, you let yourself be used by Morrigan."
    mc "You did all of this just to all appease a childish tyrant that sat at home, doing nothing but having sex and hiding behind her host."
    mc "Morrigan contributed nothing. She didn’t even respect you to the very end. As soon as you wore out your use, she abandoned you."
    show penelope csad with dissolve
    penelope "But… I did it to make her happy… I-I loved her…"
    mc "Penelope… Morrigan never cared about you, she was using you from the beginning."
    show penelope csad with dissolve
    penelope "*Sob* She almost killed me, [playername]! She looked me right in the eye as she tore the foundation of the castle from beneath my feet!"
    penelope "*Sob, sob*"
    penelope "Maybe... this was for the best..."
    penelope "I hope we as a species can move on, and learn from this."
    "As the castle guards finally arrived, Penelope slumped down and raised her hands in surrender."
    "She was nearly arrested, but Aurora and Lily agreed it’d be best to work with her through this."
    "Someone could assume that the castle guards were slacking on the job, but in reality, it has only been four minutes since I creampied the Queen and Princess."
    scene bg ccastlethrone with dissolve
    show selene neutral with dissolve:
        xpos 850
        ypos 0
    selene "Can you stand, Moxie?"
    show moxie shy with dissolve:
        xpos 600
        ypos 0
    moxie "Yeah, I think so. Thanks Selene, it feels better now."
    show selene angry with dissolve
    selene "I tried healing your injuries a little, but ugh… I’m so weak. It might even be better to get the castle doctors in here, which is embarrassing to say. Morrigan really took a lot of juice out of us, I feel like half the alicorn I was."
    show aurorab:
        xpos -150
        ypos 0
    show aurora neutral:
        xpos -150
        ypos 0
    with dissolve
    aurora "It’s not like it all went to waste, Moxie gained half of our lost power."
    show moxie sad with dissolve
    moxie "Uhm… If my math is right, does that mean I’m just as powerful as one of you were?"
    show selene neutral with dissolve
    selene "Seems that way."
    show moxie shocked with dissolve
    moxie "Please, take the energy back then! I don’t deserve it!"
    show selene laughing with dissolve
    selene "Heh, gosh… Aurora, what do you think?"
    show aurora satisfied with dissolve
    aurora "Well… It’s ten years earlier than I anticipated making this decision, but with the recent shift of power, I think we need to tell our students their real purpose."
    show lilyb:
        xpos 300 ypos 50
    show lily surprised :
        xpos 300 ypos 50
    with dissolve
    lily "Real… purpose?"
    show aurora happy with dissolve
    aurora "The true purpose of our students is to take our places as guardians for Arcadia."
    show moxie sad with dissolve
    moxie "But… I’m not a student…"
    show selene happy with dissolve
    selene "You may have missed the interview Moxie, tsk tsk! But you’ve more than proven your capability."
    selene "Earlier, you even achieved an amazing display of invisibility, completely separating your body from the physical realm whilst still moving."
    show moxie shocked with dissolve
    moxie "I did?! I-I thought I was just cloaked..."
    show selene laughing with dissolve
    selene "Hah, you didn’t even notice? Sheesh, I have a lot to teach you."
    selene "It’ll take many years, and a lot of teaching, but we’ll make you alicorns too."
    show moxie embarrassed with dissolve
    moxie "No way! Really?!"
    show aurora laughing with dissolve
    aurora "Why wait? You two deserve this honour for saving Arcadia."
    show selene surprised with dissolve
    selene "Really Aurora, right now?"
    show aurora happy with dissolve
    aurora "Sure, it’d be nice to have a fancy coronation in a few years, but I always thought we put too much emphasis on what is ultimately the addition of wings."
    aurora "Wings, right? They’ve earned that much; they can both fly anyway."
    show selene happy with dissolve
    selene "Well, there’s also… Ah, nevermind. Let’s do it!"
    show aurora laughing with dissolve
    aurora "Moxie and Lily, as recognition of saving Arcadia and as a collateral for becoming a future guardian for the city, I extend an offer to each of you."
    aurora "Would you like to become alicorns, right now?"
    show moxie happy with dissolve
    moxie "Ohmygosh, yesss!"
    show selene laughing with dissolve
    selene "This noodlehead is already as powerful as one anyway. If she knew the spell, she could do it herself."
    show lily neutral with dissolve
    lily "B-But what about me? I’m not that powerful…"
    show aurora happy with dissolve
    aurora "Hah, Lily, humble as ever. You have more potential than even I did as a filly."
    show lily happy with dissolve
    lily "If you believe in me your majesty, then I accept."
    show aurora laughing with dissolve
    aurora "So it’s settled, let the coronation begin!"
    show white with dissolve
    play sound transition1
    pause 2.0
    show lilyb w
    show lily happy
    show moxie wshocked
    hide white
    with s
    moxie "Woahhh, wings! They’re so cool!"
    show lily surprised with dissolve
    lily "Curious, I feel like my magic pools have deepened already."
    "While Moxie was playing with her new wings, Lily was pondering the intricacies of alicorn magic"
    aurora "Now you two are alicorns, you’ll need to help us repair the castle!"
    show moxie wshocked with dissolve
    moxie "Wahhh?!"
    show lily laughing with dissolve
    lily "No way, you tricked us!"
    show selene laughing with dissolve
    selene "Ehehehe, you work for us now!"
    show rikub:
        xpos 150
        ypos 80
    show riku happy:
        xpos 150
        ypos 80
    with dissolve
    riku "We’ll help out too!"
    show ruby neutral with dissolve:
        xpos 850
        ypos 50
    ruby "Goodness me, this part of the castle is truly a mess. It’s so fortunate that the damage didn’t extend to the city."
    scene bg ccastlethrone
    show aurorab:
        xpos -150
        ypos 0
    show aurora happy:
        xpos -150
        ypos 0
    with dissolve
    aurora "And to the rest of you, [playername] and the elements. Each of you played a pivotal part in saving Arcadia, you’ll all be bestowed with great gifts and honour as a thank you."
    show cream happy with dissolve:
        xpos 200
        ypos 50
    cream "Awh yes! Your gifts are always the best Queen!"
    aurora "As soon as we restore the castle…"
    show cream sad with dissolve
    cream "Oh, darn…"
    show selene neutral with dissolve:
        xpos 850
        ypos 0
    selene "*Yawn* I think the fastest way to restore the castle right now would be for the four alicorns to have power naps so we can get our magic back. Oh yeah, and get Augusta up here."
    show aurora satisfied with dissolve
    aurora "Yeah, this is going to take a while… Fortunately the damage is localised, and thanks to Penelope's fantastic plan, everyone evacuated."
    aurora "I’ll have my guards and staff take over from here, so let’s take a break before we get to work..."
    stop music fadeout 3.0
    scene bg black with dissolve
    play ambience ambienceday fadein 3.0
    show bg pgworldmapnoui with dissolve
    "After the skirmish, life in Arcadia managed to return to normal. A few towers may have been destroyed, and the mountain range partially transformed, but for a magical society these issues could be remedied in only a month."
    "I was still injured from Morrigan’s attack, if it wasn’t for Moxie and Ruby’s immediate healing, it could have been much worse. A castle doctor treated me further and I got the all-clear, only a small scar on my chest indicating anything happened at all."
    "Moxie was fortunate that nothing vital was punctured in her thigh. She got off even easier than I did with only a quick blood transfusion and bandage temporarily around her thigh."
    "After everyone was checked and treated by medical staff, we gathered to enjoy a feast of food to regain our strength. Later we joined with castle staff and disaster recovery teams to help with the immediate damage and effort."
    play ambience ambiencenight fadein 3.0
    show bg pgworldmapnightnoui with dissolve
    "That night, Moxie and I stayed in a bedroom in the castle. Both of us were utterly exhausted as we laid on the bed together."
    show bg castlebedroom with dissolve
    play music wagon2 fadein 3.0
    show moxie closewneutral with dissolve
    moxie "Ooohhh maaaan… I’m so glad that’s over… I hated being stuck in Morrigan’s body…"
    mc "You were aware of it the entire time?"
    show moxie closewshy with dissolve
    moxie "A little, I guess? I didn’t realize I was a host for a morphling, but I noticed there was {i}something{/i} wrong with me... But I couldn’t even speak out to tell anyone that something was wrong, it was so weird!"
    moxie "I’m really sorry that I dragged you into this disaster, [playername]."
    mc "Why apologize? If you hadn’t have done that, I literally wouldn’t exist, remember? And even more importantly, I wouldn’t have had the opportunity to meet you. "
    show moxie closewbashful with dissolve
    moxie "Heh, you’re such a sweet talker, as usual."
    mc "Was Morrigan always a part of you since we met?"
    show moxie closewneutral with dissolve
    moxie "Yeah, I think so… It must have been months before we met, even. I’m still pondering on whether they chose me because of my unusual powers or not. I guess I could ask Penny, but a part of me doesn't even care anymore."
    mc "I remember when I first teleported into the wagon, you kept referring to me as a ‘slave’ and wanting to give me orders."
    show moxie closewhappy with dissolve
    moxie "Heh, I think Morrigan just wanted to make a brainless familiar to order around, even she was surprised when you showed up."
    show moxie closewneutral with dissolve
    moxie "I kinda gathered that Morrigan didn't have much faith in my abilities, but Penelope kept insisting on using my body as an experiment... *Sigh*..."
    moxie "I'm not angry with Penelope, just... disappointed."
    moxie "I know I can find it in my heart to forgive her though, she was clearly mislead and manipulated."
    mc "You didn't notice anything weird while Morrigan was using you as a host? Any suspicious behaviour or activity?"
    moxie "Well... Morrigan had a lot of influence on my thoughts and emotions while we shared a body… There were things I couldn't do, or say, because of her."
    show moxie closewshocked with dissolve
    moxie "But the opposite was also true! That’s why Morrigan had a soft spot for you at first, it was because of me!  That softness gave you the opportunity to cure all the brainwashed mares."
    mc "Awhh, so even then you were looking out for me."
    show moxie closewneutral with dissolve
    moxie "You must have noticed too, but as soon as Morrigan and I separated, she became crazy and ruthless!"
    mc "Ohh? {i}All{/i} the niceties of that fiend were from you?"
    show moxie closewshy with dissolve
    moxie "Pretty much, she was a cold bitch…"
    moxie "And because of that, now that Morrigan is gone, there might be some small differences in my personality… I can think of one big thing, actually…"
    mc "What’s that?"
    show moxie closewembarrassed with dissolve
    moxie "Uhmm… It would seem I tricked you into sleeping with everyone, I'm sorry!"
    mc "Oh?!"
    show moxie closewbashful with dissolve
    moxie "Eeee, Morrigan’s influence kept making me ask you to sleep around for her brainwashing purposes, but that’s not like me at all!"
    mc "Oh, you don't like it when I sleep around?"
    show moxie closewhappy with dissolve
    moxie "Well... That's up to you, I don't mind it..."
    show moxie closewlaughing with dissolve
    moxie "It's pretty hot getting to sleep with such a stud, but that's just my biology talking."
    show moxie closewalthappy with dissolve
    mc "Phew, I’ve lost count of the number of girls that want to fuck me."
    show moxie closewsmug with dissolve
    moxie "Well… Are you ever gonna settle down?"
    mc "I’ll let you know when all this is over and life regains a little normality."
    show moxie closewbashful with dissolve
    moxie "Fiiiine…"
    mc "Do you think you still summoned me because I’m the ‘one’, like Selene described?"
    show moxie closewshy with dissolve
    moxie "Maybe… But I realize now that the whole ‘give me what I want most’ schtick also applied to Morrigan."
    moxie "She really wanted a male to sleep with and use as a pawn too… I guess that muddies the idea, it could have been Morrigan’s extremely powerful and specific desire that created you, rather than me."
    moxie "And... No offence, you were a fucking efficient pawn! Literally, fucking- efficient, get it? Heh..."
    mc "Heh... My bad…"
    mc "I guess it doesn’t really matter who summoned me. Dwelling on the past won’t help us move on. What matters is what we do now."
    show moxie closewsatisfied with dissolve
    moxie "Well… You know what I wanna do now?"
    mc "Hm? What’s that?"
    show moxie closewhorny with dissolve
    moxie "I wannaaaaaa, I really wannnaa… Fuck!"
    "She may be exhausted, but she always has enough energy reserved for sex."
    mc "Oh yeah? If you have the energy, show me how alicorn Moxie does it."
    show moxie closewsmug with dissolve
    moxie "Ohoho, I will! I’ll make all the trouble you’ve gone through worth it."
    mc "Uhm, could you use a spell to make it feel better? I’ve had so much sex today that my little dude is feeling tired."
    show moxie closewsad with dissolve
    moxie "Ah, right… I forgot that you basically fucked {i}everyone{/i} today…"
    show moxie closewlaughing with dissolve
    moxie "Damn, you really did turn out to become that Arcadian alpha I mentioned when we first met."
    moxie "Hmm, maybe this spell will work on men too! It’s one that I use on my clit sometimes when masturbating; it usually makes it feel a little better."
    stop music fadeout 15.0
    play sound genericspell
    show moxie closewalthappy with moxiespell
    "With a glow of Moxie’s horn, a spell is put upon my cock."
    "A building sensation rises in me, and the blood rapidly flows to my nether."
    mc "It feels… amazing!"
    "It’s like my cock has been blessed with a threshold of immense pleasure. With the effortless spell, Moxie has left my cock throbbing and dripping with precum in ten seconds flat."
    "It was so pleasureful I could almost lose myself to the building lust, it was difficult not to immediately masturbate or pin Moxie down and fuck; but I resisted because I’m a good boy."
    show moxie closewlaughing with dissolve
    moxie "Oohh, it’s not usually this good… Must be my alicorn touch, hehe."
    moxie "I’m gonna try it on me too."
    play sound genericspell
    show moxie closewlaughing with moxiespell
    "Moxie casts another spell and rubs her pussy a little. She’s already wet, but that’s not exactly a surprise to me anymore."
    show moxie closewembarrassed with dissolve
    moxie "Woah… WOAH!! That’s way better than usua- ahhh, haaahhh, oh gosh!"
    moxie "It’s like, it’s like a vibrator is being pressed on my clit, mmmmphh!"
    "Moxie lecherously lifts her legs up; spreading eagle. My cock stiffens and pulses in response."
    show moxie closewhorny with dissolve
    moxie "Is it just meee, or does this spell really make you wanna get fuuucked?"
    mc "Hmm, yeah… There is a slight itch in my shaft that makes me really want to fill up a pussy."
    play music sex1 fadein 3.0
    show moxie bmissionary1 with dissolve
    "Moxie falls back onto the bed and spreads her legs."
    moxie "Oh really? That’s perfect, because I feel so empty right now…"
    "As I get into position, her tail rises up; obscuring her pussy."
    "With a light giggle her tail then playfully swipes at me, bristles of her hair softly rubbing over my tense shaft."
    mc "Damn, this spell you’ve put on me made even that feel good."
    moxie "Ahah, don’t cum yet!"
    "I get a nice long view at her soaked pussy, her cute clit twitching as I align my cock with her moist cunt."
    play sound cum
    show moxie bmissionary2 with dissolve
    "I press my girthy cock against her entrance and it sinks into the warmth and wetness. It’s immensely pleasurable around my throbbing member, almost too pleasurable as her insides squeeze and suck my magically enhanced cock."
    play sound cum
    show moxie bmissionary3 with cum
    play sound cum
    show moxie bmissionary3 with cum
    play sound cum
    show moxie bmissionary3 with cum
    mc "Oh-…"
    play sound cum
    show moxie bmissionary3 with cum
    play sound cum
    show moxie bmissionary3 with cum
    play sound cum
    show moxie bmissionary3 with cum
    "My guard was down, and the overwhelming pleasure caused me to ejaculate almost immediately upon penetrating her tight pussy. I hadn’t realized my cock was this sensitive from the spell."
    show moxie bmissionary4 with dissolve
    moxie "Ahh, noooo! I told you not to cuuuum! That was way too soon!!"
    mc "It’s your spells fault! Oh, hang on… *Throb, throb* I think I can keep going."
    moxie "Niiiiiceee."
    show moxie bmissionary4 with dissolve
    play ambience sex fadein 3.0
    "I start to hump her perfect, dripping pussy. Schlicking and sliding back and forth with ease as the cum froths, bubbles and mixes with her juices."
    "Her pussy feels even hotter and wetter than usual, occasional contractions deep inside intensify the pleasure."
    show moxie bmissionary5 with dissolve
    moxie "Ahhhahahaieee, I-I’m coming, a-already! Ahhaahhh, ooohhh, mmmphhh!"
    "Moxie moans and squirms as a full-body orgasm racks her with pleasure."
    "Her spell seems to have dramatically increased the baseline of pleasure that we experience, so we’re both stuck in a state of near-orgasm pleasure until it wears off."
    "Sixty seconds into our passionate rutting, I can already feel my second orgasm boiling up."
    show moxie bmissionary4 with dissolve
    moxie "Oooofft, ghhh, I-I made the spell too strong, we’re totally gonna lose our minds!"
    "Her body ignores her concern as her hips continually wriggle and push into me as a means to maximise the pleasure she receives."
    "With both of our bodies dancing in tune, another orgasm consumes my body and mind with euphoria."
    play sound cum
    show moxie bmissionary6 with cum
    play sound cum
    show moxie bmissionary6 with cum
    moxie "Aaahhh, aaahhaaahh, y-you’re c-ccuumminngg?!? Ahhh, agains?!"
    play sound cum
    show moxie bmissionary6 with cum
    play sound cum
    show moxie bmissionary6 with cum
    "Moxie’s already cum-filled pussy is repeatedly splattered in excess, some of the jism filling her womb, some of it leaking out at our point of connection."
    "Without missing a beat, I keep fucking my lover. She lustfully moans throughout, high-pitched squeaks of enjoyment and pleasure constantly spilling from her lips."
    "She writhes and pants, her pristine blue fur growing moist with sweat. At this point she can barely form sentences between her moans."
    show moxie bmissionary7 with dissolve
    moxie "Ooohh, I-I’aahmmm, aahhhh, I-ahh! C-Comminiggghh, agaaainn?! Ahhahaahhh!"
    "Yep, she’s completely inarticulate as she loses herself in the ecstasy of her second orgasm."
    "I thrust hard into her clenching pussy, it squeezes and sucks around my cock relentlessly."
    "Squirts of her juices drip and dribble from her thighs with each body-rocking impact."
    show moxie bmissionary6 with dissolve
    moxie "F-Fuck, ahhhhh, ahhh… It’s so good! I want more! Ahhhh, fuck me more!"
    "I fuck her faster, pounding her insides with every ounce of strength my body can muster. Truly my fatigue will override my pleasure and slow me down at this rate."
    "Her hips rock with just as much vigour as mine, each of us fucking hard, fast and desperate."
    "I can feel my cock twitching again, her consistently clenching pussy combined with my thrusts is too much to endure."
    play sound cum
    show moxie bmissionary6 with cum
    play sound cum
    show moxie bmissionary6 with cum
    "Cum erupts from my cock, glazing her hot pussy in complete white; her pussy and womb completely stuffed with my semen."
    play sound cum
    show moxie bmissionary6 with cum
    play sound cum
    show moxie bmissionary6 with cum
    stop ambience fadeout 3.0
    "Moxie has the chance to indulge in another climax too, her body thrashing around wildly; lost in control by an explosive orgasm."
    "Too exhausted to continue thrusting, I fall to the side completely spent; my cock still twitching."
    show moxie bmissionary8 with dissolve
    moxie "Haahh… I don’t know my own power… *Pant, pant*"
    mc "Learn a spell to keep us both cool and full of energy next time."
    scene bg castlebedroom with dissolve
    mc "Woah-!"
    play ambience blowjob
    show moxieb blowjobcastlew
    show moxie blowjob1
    with dissolve
    "Clearly not completely satisfied with the pounding, Moxie’s lips wrap around my cock. Her tongue eagerly slurps up all the residue cum."
    show moxie blowjob2 with dissolve
    moxie "Mmphh, moreee cummiessshhh plsshh!"
    show moxie blowjob3 with dissolve
    "Her tongue swirls round and round my throbbing glans as she tries to milk me for another orgasm."
    "The mare’s hand still between her legs, fervently rubbing in a near-perpetual state of orgasm."
    "With the addition of her other hand jacking me off, it takes almost no time at all for Moxie to push me to another orgasm."
    play sound cum
    show moxie blowjob4 with cum
    play sound cum
    show moxie blowjob4 with cum
    "Taking my cock deep in her mouth, she accepts the copious amounts of semen as it splashes against her throat."
    play sound cum
    show moxie blowjob5 with cum
    play sound cum
    show moxie blowjob5 with cum
    stop ambience fadeout 3.0
    stop music fadeout 3.0
    pause 1.0
    hide moxieb
    hide moxie
    with dissolve
    "Satisfied, she rolls to the side, masturbating into a stupor. Her hips bucking and thighs quivering as she seems to have yet another orgasm."
    "And then almost in a blink of the eye, the heightened rush of pleasure dissipates as my cock rapidly turns semi-erect and Moxie woozily sits up-right."
    show moxie closewbashful with dissolve
    moxie "Phew… *Pant* Sorry about that!"
    mc "Hey, hey! What happened?"
    show moxie closewlaughing with dissolve
    moxie "Well… it’s a masturbation spell, it’s only supposed to last five minutes. As you can probably guess, I accidentally turbo charged it with my new supa magic!"
    show moxie closewalthappy with dissolve
    moxie "You sure came a lot… Are you feeling alright?"
    mc "Hmm… Tired… Came 12 times today…"
    show moxie closewlaughing with dissolve
    show moxie closewshy with dissolve
    show moxie closewsatisfied with dissolve
    "Moxie doesn’t know whether to feel proud, guilty or satisfied as her face mixes and matches between the three emotions."
    hide moxie with hpunch
    "I don’t let that confusion remain for long, as I move in for the passionate kiss, which we carry under the blankets. With heads on pillows, we snuggle together in loving embrace until we drift off to sleep."
    scene bg black with dissolve
    "..."
    play ambience ambienceday fadein 2.0
    play music daytheme fadein 2.0
    scene bg pgworldmapnoui with dissolve
    "Early next morning."
    "Life returned to normalcy rather quickly, it was fortunate that Morrigan was defeated as promptly as she was."
    "It’s still a shock to everyone that Lily and Moxie had become alicorns."
    "While Aurora said she had already intended on making Lily an alicorn for many years, Moxie was an unusual circumstance."
    "The power of the Royal Sisters was split four ways by Morrigan's influence."
    "Leaving Aurora and Selene at 20 percent each, then Morrigan and Moxie at 30 percent each."
    "The power of the royal sisters was cripplingly crushed by over a half. Imagine having half your muscles deteriorate, or half your intelligence vanish."
    "And at their age it became increasingly difficult to get that power back, in the same way learning new things gets harder with age."
    "Moxie with her new surge of power was brimming with potential, it’d be a mistake not to invest in her."
    "And making her an alicorn was the perfect theatrical boon needed to sell her on the gruelling road to becoming royalty."
    "That’s how Selene explained it to us anyway."
    show bg castlehallway with dissolve
    show moxie wshocked with hpunch:
        xpos 250
        ypos 30
    moxie "So… I’m gonna be a princess, or something?"
    show selene dresslaughing with dissolve:
        xpos 550
        ypos 0
    selene "Hmm, I haven’t thought about it. It’s not like we’re explicitly a monarchy…"
    mc "It would be weird if Moxie and Lily were both princesses at the same time."
    show moxie wbashful with dissolve
    moxie "Yeah! People would get the wrong idea!"
    show selene dresshappy with dissolve
    selene "True, I guess Lily would be a prime minister, and you’d be a deputy minister."
    selene "Anyway, thanks for helping with the reconstruction; both of you."
    show moxie whappy with dissolve
    moxie "Flying around and using telekinesis helped me acclimate to my new body, it was a lot of fun."
    show selene dresslaughing with dissolve
    selene "Glad to hear it. I’ve taken it upon myself to give you your first pay checks and a bonus for your roles in saving Arcadia."
    "Selene hands us two checks of 1,000 monies!"
    if fr == 0:
        $ monies += 1000
    else:
        pass
    show moxie wshocked with dissolve
    moxie "Woaahhhohh! Nice!"
    mc "Damn, that’s a lot… Thank you Selene."
    "While Moxie is marvelling at the money, Selene whispers to me…"
    show selene dresshorny with dissolve
    selene "And of course, if you want the other part of {i}your{/i} reward, just visit me at night, stud… If I’m going to retire soon, I’ll need to settle down, got it? *Giggle*"
    show moxie wshy with dissolve
    moxie "Hm? What are you two talking about?"
    show selene dresshappy with dissolve
    selene "I was just telling [playername] that we’ll leave construction to a company from now on, so that’ll give you and me a chance to focus on lessons."
    show moxie wneutralhappy with dissolve
    moxie "Ahh, they’ll be held during the evening, right?"
    show selene dresslaughing with dissolve
    selene "Afraid so! But I’ll be fair with my timing, 8:00pm to 12:00am seem reasonable?"
    show moxie whappy with dissolve
    moxie "You got it!"
    mc "Four hours every evening? That’s gonna be tough!"
    show selene dresshappy with dissolve
    selene "And what about you, [playername]? If there’s something else you want, I can help ‘nudge’ things in a direction you might like."
    "What exactly is she implying? Hmm…"
    mc "I’m not sure yet, I’ve definitely got a few big decisions to make. I might take you up on that offer though."
    show selene dresssatisfied with dissolve
    selene "Heheh, alright then. Stay safe you two, no more world ending disasters."
    show moxie wlaughing with dissolve
    moxie "No promises!"
    scene bg castlehall with dissolve
    "We step out of Selene’s living quarters where a familiar face is waiting."
    show penelope cshy with dissolve:
        xpos 750
        ypos 50
    penelope "Um, are you guys done?"
    show moxie whappy with dissolve:
        xpos 250
        ypos 0
    moxie "Yup, I have the rest of the day off, and all the Elements of Har’Mony are back to work."
    show penelope cneutral with dissolve
    penelope "Ahh… You don’t seem mad at all, even after what I did… Morrigan used to get so angry at me when I messed up, but everyone here is being so nice to me…"
    show moxie walthappy with dissolve
    moxie "Those are the values Arcadia and its people teach us, they’re even values you helped teach me. Deep down you know the right thing to do."
    moxie "I bet Aurora gave you an earful about that, what did she talk to you about?"
    show penelope csad with dissolve
    penelope "Well… I’m slowly figuring things out. I’m a little shaky, but I came here because I really wanted to apologize to you Moxie…"
    show moxie wneutralhappy with dissolve
    moxie "Awh … I accept your apology; I still think of you as a dear friend, our interactions weren’t purely Morrigan talking."
    show penelope csatisfied with dissolve
    penelope "I guess that explains why you were so much nicer back then, compared to how Morrigan usually is."
    penelope "So… We’re still friends?"
    show moxie whappy with dissolve
    moxie "Of course! To be honest, I just want things to go back to normal as soon as possible."
    show penelope chappy with dissolve
    penelope "Thank you Moxie."
    show moxie wshy with dissolve
    moxie "What's next for you? It can't be easy."
    show penelope cneutral with dissolve
    penelope "Well... Fingers crossed I can become an ambassador between Arcadia and the remaining morphling hive..."
    show moxie wshocked with dissolve
    moxie "Yikes, that probably won't be easy!"
    show penelope cshy with dissolve
    penelope "Eheh, probably not. But I think there will be plenty of jaded morphlings eager to reintegrate back into society. The hive has been impoverished for five years now."
    penelope "Before that though, I’m going to apologize to Lily next, I think it’ll take a little longer for her to forgive me."
    show moxie walthappy with dissolve
    moxie "Perhaps, but even Lily is becoming more open minded lately."
    moxie "As long as you behave, right?"
    show penelope cshy with dissolve
    penelope "Yeah! I’m not going to cause any more trouble, I never wanted to! My simple actions were blown far beyond what I wanted."
    show moxie wlaughing with dissolve
    moxie "Very well then, otherwise I’ll have to kick your butt!"
    show penelope chappy with dissolve
    penelope "Mmh, it’s weird hearing that from you, but kinda nice. You’ll make a good princess in the future."
    show moxie wshocked with dissolve
    moxie "P-Princess?! S-Sure…"
    show penelope claughing with dissolve

    penelope "Later, you two."
    mc "Take care."
    scene bg moxiewagonday with dissolve
    "Moxie and I leave the castle and city together as we return to the wagon."
    show moxie wsatisfied with dissolve
    moxie "Oh my gosshh, I’m still so exhausted! My wings are kinda aching, like a muscle I haven’t used before!"
    mc "I guess that’s true? You should rest, your lessons with Selene start tomorrow."
    show moxie wlaughing with dissolve
    moxie "She certainly doesn't waste any time. Kinda ironic that Morrigan was using me to take over the kingdom, but now in my future I’ll potentially run it. If she had only been patient and waited another 20 years… Hehehehe!"
    mc "You certainly have a lot to live up to."
    show moxie walthappy with dissolve
    moxie "But you’ll always be here, by my side. That’ll give me enough strength to push through anything!"
    mc "Just like you broke Morrigan’s control; you can do anything if you try hard enough, you’ve demonstrated that much."
    show moxie wsad with dissolve
    moxie "Yeah… When I saw her gut you… I broke down and with some of the siphoned power I tore her influence away."
    show moxie wembarrassed with dissolve
    moxie "Oh, speaking of Morrigan’s influence! I think you’ve got an important job left to do!"
    mc "What’s that?"
    show moxie wbashful with dissolve
    moxie "There are still some girls you haven’t cured, aren’t there?"
    mc "Wait, you mean they’re still brainwashed?!"
    show moxie walthappy with dissolve
    moxie "Well, no… they’re not brainwashed anymore, their eyes are back to normal, but they’re still technically under the influence of her magic."
    mc "Riiight… I’ve got some cleaning up to do then. Let’s see here…"
    show moxie whappy with dissolve
    moxie "Well, I’m gonna nap in the meantime, don't have too much fun!"
    hide moxie with dissolve
    "Congratulations, wielding your trusty cock, you’re the saviour of Arcadia! Don’t worry, you don’t really have to go and sleep with every other character to ‘cure’ them."
    "In addition to 1,000 monies, you’ve also unlocked some new things!"
    "1. You’ve unlocked all the new sex scenes from the last route, they can be accessed by interacting with characters during the day or evening, and asking them from the ‘sex’ option."
    "This includes: Lily standing sex, Cream standing sex, Riku riding anal, Melody + Ruby threesome, Honey + Blossom threesome, and Aurora + Selene threesome. Although the threesomes may take some convincing!"
    "2. There is also a new unseen sex scene with Penelope, prospect her at the library!"
    "3. The final two parts to Dawn's route can now be accessed."
    "4. Don't forget the 100 percent completion bonus!"
    $ days += 1
    $ fr = 1
    jump prefinalworldmap

    ## bad end
label badend:
    stop music fadeout 2.0
    stop ambience fadeout 2.0
    scene bg black with dissolve
    "..."
    "Two years later…"
    "..."
    play music morrigan fadein 1.0
    show bg cworldmapnoui with dissolve
    "And with that decision, Morrigan went on to rule Arcadia."
    "She absorbed every droplet of magical energy from both ex-Queen Aurora and ex-Princess Selene."
    "And she ruled with a mighty fist."
    scene bg black with dissolve
    show morrigan groupcun1 with dissolve
    "The mares I had brainwashed were turned into breeding slaves, and constant breeding slowly transformed them into egg laying Morphlings"
    show morrigan groupcun2 with s
    "Not even Penelope managed to escape this fate, as she was half-betrayed into becoming a breeding slave too."
    "And who was responsible for impregnating all these mares to strengthen the army?"
    show morrigan harem1 with dissolve
    "That was my job, I’d have sex with several of the mares per day, impregnating them through magic."
    "Morrigan could have used anyone to do this, yet she entrusted me to do it. I always wondered why she chose me, but I had no room to complain."
    show morrigan harem2 with s
    "While Morrigan’s army grew in strength, society in Arcadia slowly crumbled into a lawless land of debauchery and sin."
    "The only remaining residents were crooked, brainwashed or Morphlings."
    "So, what was my position beside sleeping with the mares that had once welcomed me to this world?"
    "I was Morrigan’s… boyfriend, I guess? It’s not like it was an official position, but for some reason Morrigan kept me around for loving."
    "She always had a soft spot for me, so I gulped down any complaints and tried to live the best life I could in the circumstances."
    "It wasn’t so bad, I had great food, entertainment, sexy girls. I’d be lying if I said I wasn’t enjoying myself, but… I always had some regrets for my decisions."
    stop music fadeout 1.0
    scene bg black with dissolve
    "I know this isn’t right. I know this is awful. But I had no choice, right?"
    play music sex1 fadein 2.0
    show morrigan sex1 with dissolve
    morrigan "Ihihihi, excellent job today stud, I think you got cute lil’ Lily pregnant again."
    morrigan "Once the drones lay another batch of eggs, we’ll be able to occupy another city, and with my power, there will be no one to oppose me!"
    morrigan "Oh, but enough about those whores, it’s time for you to service your Queen!"
    "Every night I’d fuck Morrigan, she was a creature that gained strength purely from the act of sex itself."
    "I grab my cock and guide it smoothly up and down Morrigan’s wet and waiting cunt."
    play sound cum
    show morrigan sex2 with dissolve
    "She gasps as I enter her tightness; her hips eagerly pushing upwards, forcing me deeper."
    play ambience sex
    "Her vaginal muscles contract tightly around my cock, squeezing wonderfully with each thrust."
    "I hold onto my lover, kissing and caressing her body as we make love."
    morrigan "You’re the best, babe… No other man in all the world can compete with you…"
    show morrigan sex3 with dissolve
    "She moans lewdly as she abandons her queenly visage for a more loving and passionate tone. Her legs wrapping around my waist, burying just a little more of my cock inside her with each thrust."
    "Morrigan likes to talk big, but in bed she’s a complete softy. It almost reminds me of Moxie… Well, I guess she is Moxie, right?"
    "Fucking her with quick, short strokes that keep the two of us locked close together, her internal muscles contract faster now."
    show morrigan sex2 with dissolve
    morrigan "Haahh, haah… Maybe one day I can bear your child too… Hahh, mmmmphh… *Squelch, squish*"
    show morrigan sex3 with dissolve
    "Her lavish vaginal lubricants leak all over my shaft allowing me to fuck relentlessly."
    "Moaning lustfully, her body begins to squirm as rising pleasure takes control, her large breasts jiggling back and forth with each thrust."
    "Some light orgasms cause Morrigan to squirt juices between our sexes, her pussy twitches as it tries to wring me for every drop of cum it can."
    "Morrigan’s special Morphling pussy is far more efficient at milking cocks than your average monster girl, it constantly tightens and squeezes at multiple pleasure points that could push an amateur to the edge in only a minute."
    "However, I’ve fucked Morrigan over 1000 times now, I can overcome the assault to my senses and continue to a new level of pleasure and satisfaction."
    show morrigan sex2 with dissolve
    morrigan "Ahhh! Oh god, oh yes! Haaahh, k-keep going! Ooohhh!"
    show morrigan sex3 with dissolve
    "Her light orgasm quickly becomes a full blown one under the assault of my consistent pounding."
    morrigan "Ahhh, yes, yesss babe! Oohh, fuck! *Squish, slap, squish*!"
    "My lover throws her head back as her entire body contorts from the sensations."
    "I continue pumping my cock back and forth as best as I’m able, but even I can’t handle the spasming of her pussy for long as the feeling of climax rises in my loins."
    "Despite having already fucked multiple other mares today, the orgasm is as potent as two intense climaxes simultaneously."
    "In response, I intensify my rutting even more, pounding in and out of the Queen almost recklessly."
    "Eventually pleasure consumes my body, and we both cry out in pleasure as my cock erupts within her."
    play sound cum
    show morrigan sex4 with cum
    play sound cum
    show morrigan sex4 with cum
    "Morrigan doesn’t just gain power when someone cums inside her, she also gains an immense amount of pleasure rivalling that of the very male orgasm filling her."
    play sound cum
    show morrigan sex4 with cum
    play sound cum
    show morrigan sex4 with cum
    "The feeling of hot cum surging and pulsing within Morrigan throws her into an immediate second orgasm, her back arching and her breasts jiggling wildly as she thrashes on the bed."
    play sound cum
    show morrigan sex4 with cum
    play sound cum
    show morrigan sex4 with cum
    "We continue fucking throughout the immense pleasure of our orgasms, until we both slowly come back to reality."
    show morrigan sex6 with dissolve
    stop ambience fadeout 3.0
    stop music fadeout 4.0
    "I pull out and cuddle next to my Queen ‘girlfriend’."
    show morrigan sex7 with dissolve
    "I guess I could get used to this…"
    show morrigan sex8 with dissolve
    "But… Every night I fall asleep, I wonder if there was another way?"
    scene bg black with dissolve
    "The End"
    if crystalballactivated == 1:
        $ crystalballactivated = 0
        jump cbmenu
    return
