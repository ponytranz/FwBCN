label dawntalksex:
    if dawnltr == 1 and dawnvisit == 1:
        jump dawnvisit2
    if dawnvisit < 3 and dawntalk == 1:
        "She isn't up there."
        jump nightclubmenu
    "I go up the stairs to the VIP section of the nightclub where Dawn often resides."
    show dawn dresshorny with dissolve
    $ rand = renpy.random.randint(1,3)
    if rand == 1:
        dawn "Couldn't keep away, could you kitten?"
    elif rand == 2:
        dawn "Can I sit on your lap, duckling?"
    elif rand == 3:
        dawn "I was just having dirty thoughts about you."
    if dawnltr == 2 and dawnvisit == 3:
        dawn "I'm guessing you got my letter? That offer is only available early in the morning. Be sure to cash it in."
        "Hmm... Wonder what that's about."
    label dawntalksexmenu:
        show dawn dresshappy with dissolve
        if dawnvisit < 3 and dawntalk == 1:
            dawn "Well, dearie, I'm afraid I have some business to attend to."
            dawn "Be sure to visit me in the morning for our little adventure."
            hide dawn with dissolve
            jump nightclubmenu
    menu:
        "Talk" if dawntalk == 0:
            jump dawntalk
        "Sex" if dawnvisit > 2:
            jump dawnsex
        "Go Downstairs":
            dawn "See you soon, dearie."
            hide dawn with dissolve
            jump nightclubmenu
    label dawntalk:
        menu dawntalkmenu:
            "What did you spend five years doing in the human colorful world?":
                $ dawntalk = 1
                show dawn dressneutral with dissolve
                dawn "Ahh, they were mostly boring times unfortunately. I spent a lot of that time simply gaining an education, and working various jobs."
                mc "Why'd you do that?"
                show dawn dresshappy with dissolve
                dawn "It was mostly field studying to learn more about that universe. That universe was of particular interest because it lacked magic but still maintained various similarities."
                mc "Huh, so what did you figure out?"
                show dawn dressneutral with dissolve
                dawn "Well... It would seem that there is very little shared history between the two worlds. But a surprisingly large overlap in individuals."
                dawn "The heck is causing that? I'm afraid I still don't have an answer."
                dawn "But I still have that nagging acknowledgement that there are infinite universes, so truly anything is possible."
                dawn "Maybe I was wrong to get so caught up in a handpicked universe, but I was a lot more bright-eyed and juvenile back then."
                mc "Awh, bless you, Dawn."
                show dawn dresshappy with dissolve
                dawn "Mmmhehe, if only I had met a man such as yourself in that universe, it could have been a lot more fun."
                mc "Speaking of, how was your love life there? You must have been in a pretty similar position to me."
                show dawn dresslaughing with dissolve
                dawn "Ah, haha... Well... You have to remember that I'm a pony in disguise."
                mc "Not a fact I could easily forget."
                show dawn dressangry with dissolve
                dawn "It took me a long time to get over that aspect. I mean serious self-confidence issues."
                dawn "Even now, one of the reasons I'm wearing the dress is because I'm not entirely comfortable in my body, but... I find it increasingly easier to open up to people the closer I get to them."
                show dawn dressneutral with dissolve
                dawn "But I also had a small issue of avoiding attachment, because I saw myself as a guest in the alternate universe."
                dawn "It genuinely took me two years until I was finally comfortable and had a group of friends that helped ease me into the more social aspects of that world."
                show dawn dresshappy with dissolve
                dawn "And yeah, maybe there was a guy, or two... But I never found myself committing, I think you can imagine why, kitten..."
                menu:
                    "Yeah, after all, I'm your true love.":
                        show dawn dresshorny with dissolve
                        dawn "Is that so? Perhaps you can teach me more about 'true love', then?"
                    "A girl like you can't be tied down by a single man.":
                        show dawn dresshorny with dissolve
                        dawn "I don't know about that duckling... I only need a single rope, a single man, and I'll be satisfied all night..."
                    "The men in that universe were losers anyway.":
                        show dawn dresshorny with dissolve
                        dawn "They kinda were, yeah... The girls weren't so bad though, hehe."
                    "Yeah, it'd probably be bad to get too attached to someone if you're only going to leave them.":
                        show dawn dresssatisfied with dissolve
                        dawn "Exactly, duckling."
                jump dawntalksexmenu
            "How were your years in the pony world?":
                $ dawntalk = 1
                show dawn dressneutral with dissolve
                dawn "Hmm... Allow me to reminisce for a few moments. You're essentially asking me to boil down my entire childhood and teens..."
                mc "I suppose we can just discuss the tail end. You were the Queen's student, weren't you? That's not a common position."
                show dawn dresshappy with dissolve
                dawn "Oh, right! I was scouted from a young age, most are based on their potential. This led me to extra lessons at first, nothing overly intensive for a filly."
                dawn "But instead of going to a regular school, I seemed to have high enough scores in some aptitudes to enter a special Arcadian school."
                show dawn dresssatisfied with dissolve
                dawn "And- I, uh... Not to brag, but I was the top of even that class."
                mc "That's awesome!"
                show dawn dresshappy with dissolve
                dawn "That's what I get for being a nerd that likes to learn as much as another classmate might like to play video games or sport."
                dawn "I'd stay up past my bedtime studying, ahhaaa... I'm such a loser."
                menu:
                    "You might think that makes you a loser, but staying up to 3:00am playing video games is probably worse...":
                        show dawn dressangry with dissolve
                        dawn "Well, I'm no stranger to staying up late playing video games either..."
                        mc "Yeah, me neither..."
                        show dawn dresssatisfied with dissolve
                        dawn "Loser high five?"
                        "We high five."
                    "I think that's an extremely positive and admirable quality.":
                        show dawn dresslaughing with dissolve
                        dawn "Thank you! I had a lot of support from family and friends."
                    "Interesting... I also have something for you to study past your bedtime.":
                        show dawn dresshorny with dissolve
                        dawn "Is that so, dearie? You've hit a soft spot inside me, because I just loooove to study anatomy, mmmhehe..."
                show dawn dresshappy with dissolve
                dawn "Despite my aptitude, I didn't really want to be the Queen's student. Or at the very least, the extra baggage lumped in with that meal deal."
                dawn "So, here I am with my unusual occupation. Mostly working with Selene instead of Aurora."
                dawn "While I do have a loving family that I often visit, I don't have many friends and no partner, so this was an easy job for me to take."
                show dawn dressneutral with dissolve
                dawn "I mean, I do have friends, but they all graduated and drifted away... You know how it is."
                menu:
                    "I certainly do... Making friends sucks as you get old.":
                        show dawn dresshappy with dissolve
                        dawn "It sure does. That's why I chose to run a nightclub over another boring coffee shop, plenty of great social opportunities."
                        dawn "Now I have three friends!"
                        mc "Oh yeah?"
                        show dawn dresssatisfied with dissolve
                        dawn "Mhm. You, Aurora and Selene!"
                        mc "Oh..."
                        show dawn dressneutral with dissolve
                        dawn "Yeah... Turns out it's not easy making friends when you swap between universes so often. It's a very depersonalising experience."
                    "I'll be your friend Dawn.":
                        show dawn dresshappy with dissolve
                        dawn "And what an amazing friend you are... I don't think I'll need any other with you around, kitten..."
                        dawn "Perhaps you can show me just how great of a friend you can be later?"
                        mc "I might have to get some assistance from another little friend to help out."
                        show dawn dresshorny with dissolve
                        dawn "Mmmhehe, you called it little! But I know that isn't exactly accurate..."
                    "How did someone as flirtatious as you not get a partner?":
                        show dawn dresshorny with dissolve
                        dawn "Mmhehe, you must have a strange impression of me, [playername]..."
                        dawn "I'm only flirtatious around {i}you{/i}!"
                        mc "Woah... That's awesome."
                jump dawntalksexmenu
            "Would you let me have sex with you while you're in your pony form?":
                $ dawntalk = 1
                show dawn dresshorny with dissolve
                dawn "Hmm? You want some horse pussy?"
                mc "Uhm, well... I was just curious."
                mc "For someone in an alledged disguise, you've never once dropped it while we were alone. Even when we were asleep."
                show dawn dresshappy with dissolve
                dawn "And I never will, dearie. The disguise spell lasts almost a month regardless, so sleep is no issue."
                "I don't know a lot about magic, but I know that's an extremely impressive magical feat for a unicorn... Dawn is pretty awesome, eh?"
                mc "May I ask why not?"
                show dawn dressneutral with dissolve
                dawn "It just wouldn't feel right exposing myself in such a way around you... I would feel diminished in a sense."
                mc "I see... Appearing in this form makes you feel like my equal?"
                show dawn dressangry with dissolve
                dawn "Perhaps... I am rather self-conscious about these things, so I apologize if it troubles you."
                mc "That makes sense, actually. You've been disguised like this for years, especially in that human world."
                show dawn dresshorny with dissolve
                dawn "Ohh, sheesh... The thought of you fucking me like that is rather arousing, but I'll have to decline..."
                show dawn dressangry with dissolve
                dawn "For now..."
                jump dawntalksexmenu
            "Back":
                jump dawntalksexmenu
    label dawnsex:
        show dawn dresshorny with dissolve
        dawn "Are you going to buy me a drink first? Hehe."
        menu:
            "Blowjob":
                jump dawnblowjob
            "Reverse Cowgirl":
                jump dawnrcg
            "Changed my mind":
                jump dawntalksexmenu
        label dawnblowjob:
            stop music fadeout 3.0
            scene bg black with dissolve
            "The two of us spend an hour together drinking and having fun before we find ourselves drunkenly kissing in her bedroom."
            show bg dawnsroomnight with dissolve
            mc "You keeping the dress on?"
            show dawn dresssatisfied with dissolve:
                xpos 475
                ypos 20
            dawn "Don'tcha think it's more fun that way? Kinda squeezes my boobs together too."
            show dawn dresshorny with dissolve:
                linear 1.0 ypos 200
            "She leans down and her fingers seductively crawl up my thigh until they’re tentatively at the base of my cock, which is rapidly growing to an erection."
            show dawn dresssatisfied with dissolve
            dawn "Oh my… Did I do this?"
            play music sex1 fadein 3.0
            scene dawnb blowjob
            show dawn blowjob1
            with dissolve
            "She grins and adjusts until her face is even closer to the tip. The subtle removal of her dress’s shoulder straps so her breasts spill out wasn’t missed."
            play ambience blowjob fadein 2.0
            "Despite her usual slow burn flirtatious nature, she’s doesn't tease me and immediately take my cock into her mouth, lustfully sucking at the head while her tongue flickers at the tip."
            "Simultaneously she takes to time to adjust herself so her breasts are brazenly pushed against my shaft, where she continues to fondle her breasts enticingly now that they’re in perfect view."
            dawn "Do you like my breasts, kitten? I feel like the beauty of a bosom is taken for granted in this world. *Slurp, lick*"
            mc "I love every inch of your body, Dawn."
            dawn "You always know just what I want to hear..."
            "Her piercing bedroom eyes make me weak, her hot mouth slowly consuming more and more of my sensitive throbbing cock."
            "Her long mare tongue eagerly working my shaft as it swirls and twirls against every available inch."
            dawn "Since you like my breasts so much, how about we make this a paizuri and a blowjob…"
            "She readjusts herself again, using her arms to squish her breasts around the base of my shaft."
            show dawn blowjob2 with dissolve
            "Dawn smirks as she lewdly drools around the connection and provides a few small thrusts. It’s impressive how warm and tight a mare’s breasts can feel."
            "Working her tits with her arms, she indirectly pushes and slides them along the length of my shaft, giving shallow pumps to my broad cock, while her tantalising tongue works wonders on my tip."
            "The combination of these two pleasures may just be enough to bring me to an orgasm, especially so as she speeds up the efforts of her titfuck."
            show dawn blowjob1 with dissolve
            dawn "Mmmphh… Mmm… *Schlurp, lick* Your cock is so soft and tasty, hehe."
            mc "T-Tasty?"
            dawn "Mmmphh, mmphh… Ish time for yoush to cumsh! Mm, mmmm…"
            dawn "Ten… Nine… Eight…"
            show dawn blowjob2 with dissolve
            "She giggles causing her mouth to vibrate slightly. She closes her eyes as she redoubles her effort, her purpose to bring me to an orgasm is clear."
            dawn "Seven… six… five…"
            "My cock throbs and grows increasingly tight as the pressure of my orgasm slowly rises. The feeling between her soft, pillowy tits becomes increasingly pleasureful."
            dawn "Four… three… tw- wah?"
            play sound cum
            show dawn blowjob3 with cum
            play sound cum
            show dawn blowjob3 with cum
            "The mounting pressure comes to a boiling point as I inadvertently thrust into her mouth and begin to unload."
            play sound cum
            show dawn blowjob3 with cum
            play sound cum
            show dawn blowjob3 with cum
            stop ambience fadeout 3.0
            "Dawn dutifully pushes her head forward, deepthroating my cock as the semen splashes the back of her throat with several thick loads."
            show dawn blowjob4 with dissolve
            stop music fadeout 3.0
            "She swallows down each droplet before she pulls out and sighs."
            dawn "Ohh, you’re an impatient man…"
            scene bg dawnsroomnight with dissolve
            show dawn dresshorny with dissolve
            play ambience ambiencenight fadein 3.0
            "Without a droplet of semen to be seen, she slips the straps of her dress back up and smirks."
            dawn "Just how I like them."
            mc "You give a damn good blowjob."
            show dawn dresshappy with dissolve
            dawn "Heh, thanks. As you can imagine, I'm used to human equipment."
            mc "What was with the timer?"
            show dawn dresshorny with dissolve
            dawn "Ah, the timer is a psychological thing, the body prepares itself to ejaculate as if commanded."
            show dawn dressneutral with dissolve
            dawn "I guess it works?"
            mc "You put a lot of thought into this."
            show dawn dresshorny with dissolve
            dawn "I like to please, especially you, dearie."
            scene bg black with dissolve
            stop ambience fadeout 3.0
            "We spend the rest of the evening in each others company before going to bed together."
            "What's this? A double bed? What an exciting development! Oh, wait... This is just two single beds put next to each other."
            "We go our separate ways in the morning."
            jump altmorning
        label dawnrcg:
            stop music fadeout 3.0
            scene bg black with dissolve
            "The two of us spend an hour together drinking and having fun before we find ourselves drunkenly kissing in her bedroom."
            show bg dawnsroomnight with dissolve
            show dawn dresshorny with dissolve
            dawn "Won't be needing this..."
            hide dawn with dissolve
            play sound movement
            show dawn satisfied with dissolve:
                xalign 0.5
                ypos 20
                linear 0.5 xalign 0.5 ypos 200
            "She suddenly crawls over me and drops her weight onto my thighs, her ass and tits jiggling alluringly."
            play music sex1 fadeout 3.0
            hide dawn
            show dawnb sex:
                xalign 0.5
                yalign 0
            show dawn sex1:
                xalign 0.5
                yalign 0
            with dissolve
            "Backing her hips slightly, my throbbing cock is slotted between her ass cheeks."
            "Pushing my cock back somewhat with her rump, she positions our genitalia in such a way that she can grind them together."
            show dawn sex2 with dissolve
            "Her dripping wet labia dragging back and forth against my throbbing member repeatedly, all whilst she looks deeply into my eyes."
            "As she starts to focus her slightly parted lips against the tip of my cock, she moans slightly as she becomes increasingly aroused."
            dawn "I must say, I'm becoming rather fond of your cock. I've started fantasising about it often."
            mc "And how do those fantasies go?"
            dawn "Well... They usually start like... this..."
            play sound cum
            show dawn sex3 with cum
            "She pushes down, spreading her vulva around my shaft as she sinks further and further down. Biting her glossy lips as she reaches the hilt, a slight shiver encompassing her body."
            dawn "Aahhh... That's good..."
            "It’s tight, warm, and wet. Even motionless, her pussy squeezes and sucks around my member, eliciting pleasure from each and every nerve ending."
            "Through constant flirting and playing hard to get, the satisfaction of penetrating the alluring Dawn significantly adds to the pleasure."
            "Cooing slightly, she adjusts to my girth, arching her back and rubbing her clit in the meantime; her nipples fully erect."
            show dawn sex4 with dissolve
            dawn "Mmmm… My entire body feels like it's on fire for you..."
            play ambience sex fadein 3.0
            "She closes her eyes tightly for a moment as she begins to grind her hips up and down."
            "It doesn't take long for Dawn to adjust to my girth as she accelerates her riding to higher levels of bliss."
            show dawn sex3 with dissolve
            dawn "Ahh, oohhh, don’t you dare cum until I’ve had my own, mmhehe…"
            mc "That’s quite the challenge with the most seductive mare in Arcadia."
            dawn "I'll rub my clit just in case you can't handle me today, hehe, but I know I can rely on you, kitten."
            show dawn sex4 with dissolve
            "She takes her time and rides at an average and pleasurable pace. Her ample yellow ass practically hypnotises me as I drink in every detail."
            "The tightness of her pussy, the lips that grip against my shaft, and her cute butthole that I’d totally want to put a thumb in if this was doggystyle."
            "My lover’s pussy constantly squeezes and clenches around me, similar to how Ruby performs in bed, squeezing and milking in rhythmic motions as if she’s truly trying to make me blow my load."
            "Dawn giggles almost knowingly of this fact, letting her orgasm first may be quite the challenge indeed. You can trust Dawn to make sex a flirtatious back and forth game."
            "Gritting my teeth slightly, I start to grind my own hips back and forth against her, bouncing her up and down, causing her ass and tits to bounce."
            show dawn sex3 with dissolve
            dawn "Oohhh, such an impatient man! Mmmhehe, oohhh, keep doing it like that, nice and deep! Ahh, yeahh!"
            "Perfect, she reacts with pure euphoria to each of my deep thrusts, while she constantly rubs her clit."
            "Bending my knees and tensing my thighs, I overwhelm any attempt she has to grind against me. Turning her into a willing participant of the act as I pound her pussy from below."
            show dawn sex4 with dissolve
            dawn "Ahh, ahh, ohh, ahhh! Y-You’re g-gonna-! Ahhhh!"
            "She squeaks and shivers, her back arches and my cock pushes against her g-spot. She can barely contain herself; her mind slowly eroding due to the pleasure."
            "Any attempt at speech failing as moans escape her mouth and her body is consumed in pleasure."
            dawn "Ahhh, ahhh, y-yes! Ahhh, c-com-ahhh, ahhhhh!"
            "Internal contractions around my cock signal her climax, allowing me to lower my guard to my own orgasm."
            "My cock reacts almost immediately as it thickens and throbs, my muscles growing tense with the building force of my orgasm as it surges through my body."
            play sound cum
            show dawn sex5 with cum
            play sound cum
            show dawn sex5 with cum
            "Dawn’s almost gives way as she feels the first torrent of cum unload inside of her, the warm thick cum filling her womb and vagina."
            play sound cum
            show dawn sex5 with cum
            play sound cum
            show dawn sex5 with cum
            "My lover pants, her tongue hanging lewdly from her mouth as I pump my final few loads of cum into her womb."
            stop music fadeout 5.0
            stop ambience fadeout 3.0
            scene bg dawnsroomnight with dissolve
            show dawn horny with dissolve
            dawn "I just adore being filled by you, it makes me feel so pleasant inside."
            mc "That must be the oxytocin doing its work."
            dawn "I don't need that to know how amazing you are, kitten. Come-hither, let's snuggle."
            scene bg black with dissolve
            "I sleep incredibly well post-sex and with a little alcohol in my system."
            "In the morning we regretfully part ways."
            jump altmorning
label dawnvisits:
    label dawnvisit2:
        $ dawnvisit += 1
        "I look around for Dawn, but in truth I don’t have a very good means of finding her."
        "Fortunately, a contrasting flash of blue in the sea of red and pinks catches the corner of my eye. The upper floor is visible from down here and I manage to spot Dawn’s blue flowery dress upstairs."
        "I make my way up, unfortunately the top of the staircase has a ‘VIP only’ sign chained across it… That’s somewhat frustrating."
        "But Dawn herself unhooks the chain and allows me past."
        mc "VIP, hmm, me?"
        show dawn dresshorny with dissolve
        if fr == 1:
            dawn "Absolutely, kitten. You’re so very important. You helped defeat Morrigan and saved Arcadia, you'll always be welcome in my club."
            mc "Not for free, I take it?"
            dawn "Afraid not, I have a business to run! Mmmhehe, but I’m simply delighted that you came to play with me regardless."
        else:
            dawn "Absolutely, kitten. You’re so very important. I’m simply delighted that you came to play with me."
        "This area is entirely empty apart from her. She returns to sitting at an empty bar, sipping on a tall glass of scarlet wine as she overlooks the club."
        "There’s a second wine glass beside her, and she pours me a glass without even asking."
        show dawn dresshappy with dissolve
        dawn "My treat darling, I fully intend to soften you up, before getting you hard again… Mmmhehe…"
        "I sit down on a stool beside her and take a sip. It tastes really good, it’s not like wine from my universe at all. No offense, wine from my universe."
        mc "Thanks Dawn, I take it you didn’t just invite me here to test my endurance in not getting an erection."
        show dawn dresslaughing with dissolve
        dawn "Oh kitten, if I was testing that, you’d be throbbing right now…"
        mc "Ahh- that’s enough about that."
        "I seriously just felt my loins tingle, it’s a good thing no one else is up here."
        show dawn dresshappy with dissolve
        dawn "But you’re correct, Mr. Detective, I have a requirement that only a human like yourself can fulfil."
        mc "Human? How do you-…"
        show dawn dresslaughing with dissolve
        dawn "Mmmhehe, I know all about you cute little humans. I’ve never seen one naked before though. I do believe you’ve stolen a part of my innocence that I’ll never get back."
        mc "How do you know, Dawn?"
        show dawn dressneutral with dissolve
        dawn "Tell me, do you know of the mirror portals?"
        mc "The mirror-… The mirror-."
        mc "Huh? The mirror-…"
        "What’s this? The air isn’t escaping my mouth, it’s oddly uncomfortable."
        "Oh shit! How could I forget?"
        "Aurora’s spell prevents me from talking about this, it’s extremely sensitive information and I was just about to tell this potential James Bond villain mare all about it."
        show dawn dresshappy with dissolve
        dawn "Ohhh, cat got your tongue? I haven’t even sat on your face yet… Mmmhehehe."
        dawn "So… You do know about them. *Sip*"
        mc "How do I know I can trust you?"
        show dawn dressneutral with dissolve
        dawn "Ooohh, you don't trust me? It’s fine, darling, I’m also a stray kitten…"
        mc "You’re from… another universe?"
        "Ah, I can mention that, just not the mirror portals. Phew."
        show dawn dresslaughing with dissolve
        dawn "Indeed Mr. Detective, I believe an interview is appropriate, is it not?"
        show dawn dresshorny with dissolve
        dawn "If you can get my panties to drop in less than twenty questions, I’ll give you a very special reward…"
        mc "Ah- wha-?!"
        "Why am I flustered? I’ve never been flustered like this with a mare before!"
        dawn "Just kidding!"
        "Ah… Of course, she’s messing around with me… How could I fall for that?"
        show dawn dresssatisfied with dissolve
        dawn "I’m not wearing any panties… So, you’ve already won. *Sip*"
        mc "*Gulp*"
        show dawn dresshorny with dissolve
        dawn "Time for your reward... I'll tell you exactly what you'd like to know."
        show dawn dresshappy with dissolve
        dawn "I was from another universe too. But I came here of my own accord."
        dawn "I actually come and go from the ‘pony’ and colourful human portals quite often, although the ‘pony’ world was my original."
        mc "You were seriously a four-legged pony?"
        show dawn dresshorny with dissolve
        dawn "Mhm, I’ve been a professional at getting on all fours my entire life."
        mc "But… You’re not on all fours right now, you’re standing just like me."
        show dawn dresssatisfied with dissolve
        dawn "Oh? You’d like me to get on all fours right now? And here I thought I was the bad influence; you truly are a devilish boy."
        mc "Y-You know what I mean..."
        show dawn dresshappy with dissolve
        dawn "I used to simply call this my ‘disguise’, but in truth it’s a lot more than that."
        show dawn dresshorny with dissolve
        dawn "What I'm currently residing in is a real body through and through. Perhaps you’d like to undress me to find out?"
        mc "What’s with the dress, anyway?"
        show dawn dresshappy with dissolve
        dawn "Ah, it’s something I grew rather attached to in the five years I spent in the colourful human world. I thought it’d only be natural to wear such a garment here."
        dawn "Fufu, you seem to have taken to the nudity quite well. Let me guess, was it all the mares complimenting and seducing you?"
        "Hmm… Was it? I think it was mostly Moxie and the fact I had no other clothes to wear."
        mc "Uhm, that aside… What are you doing hopping around universes? That’s rather abnormal, wouldn’t you say?"
        show dawn dressneutral with dissolve
        dawn "Mm, you don’t know? My, my, Aurora should have mentioned something…"
        show dawn dressangry with dissolve
        dawn "I used to be another Aurora’s student. However, I found it a little too stressful, it was ruining my complexion, so I resigned."
        "Do ponies have complexions?"
        show dawn dresshappy with dissolve
        dawn "Hmm, I wonder if 'she' knows that such a position is a life sentence… Perhaps not, I shall keep my lips sealed for now."
        mc "Hm? So, you’re not her student anymore?"
        show dawn dressneutral with dissolve
        dawn "I am not, however, in my position I was still fully trained and capable of many marvellous career paths."
        dawn "I decided to become an interuniversal scholar, I work with various Auroras and Selenes across four different universes."
        mc "Wow, that’s seriously, seriously amazing!"
        show dawn dresshappy with dissolve
        dawn "Naturally, this universe is my central hub."
        mc "Hm? Why’s that?"
        show dawn dresslaughing with dissolve
        dawn "Isn’t it obvious, kitten? Opposable thumbs, AND magic."
        dawn "Ooohh, and of course, you’re here, kitten."
        "She playfully blows me a kiss before sipping some more wine."
        show dawn dresshappy with dissolve
        dawn "But, I must ask, why are you here? Answering this question is the very reason I requested you."
        mc "Well… Truth is, I have no family, or friends, or a place to stay in my old universe. Because… I already exist in my old universe."
        show dawn dresssatisfied with dissolve
        dawn "Ah? The plot thickens… This wine has too many calories… *Sigh… Sip*"
        show dawn dresshappy with dissolve
        dawn "Indulge me some more? It seems that my theory was clearly completely off, you didn’t come from those portals at all, did you?"
        mc "I did not, I was teleported here atom by atom by a mare called Moxie. While investigating I discovered the-… alternate universes, and it’s generally accepted that I came from the ‘human’ universe where the original me still exists."
        show dawn dresslaughing with dissolve
        dawn "Ahh… That’s rare, you truly are a one of a kind man… Oh wait, no you aren’t! Mmmheheh."
        mc "I have a question too, why can’t I have a disguise like yours?"
        show dawn dresshappy with dissolve
        dawn "I’m afraid the answer will disappoint you, my little duckling… Only a unicorn can don a magical disguise. If I were to cast a spell on you, it’d only have a tenth of the duration."
        mc "Doesn’t that take a lot of magical power?"
        show dawn dresssatisfied with dissolve
        dawn "*Sip* Who do you take me for? Mmmhaha! The disguise does occasionally wear itself out."
        show dawn dresshorny with dissolve
        dawn "Ever had sex with a real pony before?"
        mc "OBVIOUSLY NOT!"
        show dawn dressneutral with dissolve
        dawn "Oh, shame! *Sip*"
        "Perhaps that outburst was a little rude, she is originally a pony after all… Still… *Shudder*"
        show dawn dresshappy with dissolve
        dawn "Well, my wine and I have had a small discussion, and we’ve come to an agreement."
        dawn "I’d like to bring you along on one of my interuniversal trips, specifically to your universe."
        dawn "I believe your knowledge of that world will be invaluable, would you help me gather some information?"
        dawn "I’ll make it really, really worth your while..."
        "There it is again, that tingle in my loins… But there's more important things about what she just said than getting my dick wet."
        mc "Sure, it’ll be fun for nostalgic purposes. You’ll have to get me some clothes though."
        show dawn dresshorny with dissolve
        dawn "Oh my, I’ll be responsible for dressing you? Mmmhehe, only if you undress me, kitten…"
        mc "You’ve got a deal."
        "We clink our wine glasses together before finishing our drinks."
        show dawn dresshappy with dissolve
        dawn "Let's talk. I'm sure you're interested in me, and I am ever so interested in yourself, duckling..."
        $ dawnv2c11 = 0
        $ dawnv2c12 = 0
        $ dawnv2c13 = 0
        $ dawnv2c14 = 0
        label dawnv2c1:
            if dawnv2c1 == 4:
                jump dawnv2c1b
        menu:
            "What shall we discuss?"
            "Are you friends with any of the mares I know?" if dawnv2c11 == 0:
                $ dawnv2c11 = 1
                $ dawnv2c1 += 1
                show dawn dresshappy with dissolve
                dawn "That's to put it lightly. I know them all, and I know them from different universes."
                dawn "I suppose the question is, who do you want to know about?"
                mc "Uhm... Good point. How about Moxie?"
                show dawn dresslaughing with dissolve
                dawn "Ahh, I love that gal. She and I have a few things we can relate to in almost every universe."
                show dawn dresshappy with dissolve
                dawn "Although I've yet to meet her in this universe. I hope she's doing well."
                mc "I'd say so, she can't stop smiling."
                show dawn dresshorny with dissolve
                dawn "Who can when you're around?"
                mc "How about Lily?"
                show dawn dressneutral with dissolve
                dawn "Lily is surprisingly different in every single universe... Yeah, that might sound strange."
                dawn "The pony universe, the human universes and the anthro universes all have very different Lilys."
                dawn "The pony universe's seems to be the most successful, she's already a-"
                if fr == 1:
                    dawn "- Well, she became an alicorn about three years earlier."
                else:
                    dawn "Oh- spoilers. I nearly told you some classified information."
                mc "Oh, really? Alright, well you've piqued my interest."
                mc "I guess the parallel universes aren't copy and paste then."
                show dawn dresshappy with dissolve
                dawn "Far from it."
                mc "Uhm, how about Penelope then? Last person."
                show dawn dressneutral with dissolve
                dawn "Penelope? Never heard of her."
                mc "Huh? She's the girl that works at Lily's library."
                show dawn dresshappy with dissolve
                dawn "Hmm... Maybe they have a different name. It's not like names or even gender is locked by universe."
                mc "Weird..."
                if fr == 1:
                    mc "Do you think that has anything to do with Morrigan?"
                    show dawn dressneutral with dissolve
                    dawn "Potentially. The events that just transpired are unique to this universe."
                else:
                    dawn "It can be sometimes. I've often had my jaw dropped when I discovered some weird connection."
                jump dawnv2c1
            "You mentioned you'd make it 'worth' my while if I helped you. Can we discuss the reward?" if dawnv2c12 == 0:
                $ dawnv2c12 = 1
                $ dawnv2c1 += 1
                show dawn dressneutral with dissolve
                dawn "I hope you're not one of those men that don't pick up on hints."
                mc "Oh don't worry, I'm well aware of the hints. But you also don't seem like the type of girl that'd use 'that' as a reward."
                show dawn dresshorny with dissolve
                dawn "Heh, I really shouldn't underestimate you. Apologies, dearie."
                dawn "Allow the thought of your reward to ruminate in my mind. I believe I'll think of something you find more than satisfying."
                jump dawnv2c1
            "What's your original universe like?" if dawnv2c13 == 0:
                $ dawnv2c13 = 1
                $ dawnv2c1 += 1
                show dawn dressneutral with dissolve
                dawn "The pony universe was certainly interesting... But now that I've had the opportunity to enjoy fingers and hands, it feels strange to go back."
                mc "It must be even worse for ponies without magic..."
                show dawn dresshappy with dissolve
                dawn "Many objects and technologies in that universe are built around hooves, but if it wasn't for magic everything would be extremely basic."
                dawn "Although I'll admit, the tenacity of sentience makes me believe that given enough time, even sentient ponies could make amazing technologies."
                dawn "Regardless, the class division in that world is wider due to the obvious advantages wings and magic have."
                mc  "Sheesh... I'd be so jealous if I was a regular pony in a world of flying and magic ponies."
                show dawn dresslaughing with dissolve
                dawn "Isn't that more or less your current position?"
                mc "Good point..."
                show dawn dresshappy with dissolve
                dawn "And are you particularly perturbed by your lack of magic?"
                mc "Not really, I've always lived this way."
                show dawn dresssatisfied with dissolve
                dawn "Now you know how most regular ponies feel."
                mc "I see... Interesting!"
                mc "Still, no fingers..."
                show dawn dressneutral with dissolve
                dawn "It's a nightmare, I know!"
                dawn "You know, kitten, that neatly ties into the reason I got this job in the first place."
                mc "Oh yeah? What's that?"
                show dawn dressangry with dissolve
                dawn "How the hell did two significantly different universes end up with so many similarities?"
                mc "Hm... That's an interesting question, do you have an answer?"
                show dawn dressneutral with dissolve
                dawn "Not yet... But I have a theory I'm working on."
                dawn "I won't bore you with that now. The current time is for drinking and fun!"
                jump dawnv2c1
            "What do you do in your spare time?" if dawnv2c14 == 0:
                $ dawnv2c14 = 1
                $ dawnv2c1 += 1
                show dawn dresssatisfied with dissolve
                dawn "Oh, you know... I like to read, I'm a bit of a nerd so I actually enjoy reading boring ol' history books!"
                dawn "When I find a good thread, I just can't stop pulling. Then all of a sudden it's 3:00am!"
                mc "That's a remarkable quality, to have such a degree of passion in an academia area. Most people would be bored brainless by that."
                show dawn dresshappy with dissolve
                dawn "I tend to agree, dearie. I fit my role like a glove. Aurora always had a great eye for this type of thing, so even after I refused to be her student, she offered this to me instead."
                dawn "Unfortunately, I spend a lot of time between worlds, so I'm not part of any public activities. But I go to the gym in the coloured human world about once a week."
                show dawn dresslaughing with dissolve
                dawn "Oh, and I also play the guitar!"
                mc "Hah, the guitar, eh? Yet another reason for you to avoid the pony world."
                show dawn dressneutral with dissolve
                dawn "Mhmm, true..."
                mc "How'd you come about owning this nightclub? If you're often between universes wouldn't it be difficult to run?"
                show dawn dresslaughing with dissolve
                dawn "Mmmhehe, maybe! But I'm the owner, not the manager. That means I don't actually have to do anything, ahaha!"
                show dawn dresshappy with dissolve
                dawn "Occasionally I'll have to make some decisions, it's not like I slack off."
                dawn "I also own a coffee shop in my original universe."
                mc "Really? So you're an entrepreneur as well as an interuniversal scholar."
                dawn "I wish! Both businesses were loaned to me from anthropomorph Aurora and pony Aurora, since it's important I have at least some minor funds for my ventures. It's not like the currency can be converted between universes."
                dawn "In the human worlds, I tend to just use magic to duplicate money, but we needn't linger on that."
                mc "Wait, I actually do want to linger! Why can't you duplicate money in this world?"
                show dawn dresslaughing with dissolve
                dawn "Mmmaha, I forget just how truly new you are. All the money from magical societies are protected from fraud."
                show dawn dresshappy with dissolve
                dawn "Every note has a special spell placed on it. This spell unlike most is permanent, and few know how to cast it."
                dawn "Most machines won't even accept fraudulent monies, and shops have technologies that'll detect false currency."
                dawn "I'm guessing whenever a new batch of money is printed, Selene protects them all at once."
                mc "Hm... I see. Despite all the benefits of magic, there really are some strange things you can't take for granted."
                show dawn dressangry with dissolve
                dawn "Yeah, there's a lot of unique considerations for a magic based society."
                dawn "And as you can imagine, there's always an opposing group to any ideology. There're some that think we shouldn't have currency at all, and just use magic to create or form objects."
                dawn "They think the idea of currency is limiting and only serves to disadvantage certain folk."
                show dawn dressneutral with dissolve
                dawn "But those groups are totally disregarding all the magicless folk, we need to make the world fair for them too."
                mc "Yeah, I agree with you there."
                "Hmm... There might be more to this magical society than I thought."
                jump dawnv2c1
            "(Conclude talking)":
                jump dawnv2c1c
        label dawnv2c1b:
            show dawn dresshappy with dissolve
            "Dawn and I chatter amongst ourselves for a few more minutes, until we've both finished... Woah, the entire bottle of wine is empty! That was some expensive stuff too."
            show dawn dresshorny with dissolve
            dawn "Mmmhehe, care to dance?"
            jump dawnv2c1d
        label dawnv2c1c:
            show dawn dresshorny with dissolve
            dawn "I'd love too. Shall we?"
        label dawnv2c1d:
            pass
        hide dawn with dissolve
        "Under a spell, Dawn carries me by hand to the dance floor."
        scene bg black with dissolve
        stop music fadeout 3.0
        play ambience ambiencenight fadein 6.0
        "Before either of us know it, a night filled with fun escapes us and we’re eating takeaway together while chilling in her living space."
        show bg dawnsroomnight with dissolve
        show dawn dresssatisfied with dissolve
        dawn "Mmmph, I loooove this pizza, mmm mmm!"
        mc "The fries are really good too; the combo meal was a great suggestion."
        show dawn dresshorny with dissolve
        dawn "Don’t eat too much before vigorous exercise, darling."
        mc "Hm? Vigor-ohh… You’re flirting with me again."
        show dawn dresshappy with dissolve
        dawn "Mmhehe. I’m always flirting with you, and yet, you’ve seen less of me than any other mare you’ve ever laid your eyes upon."
        mc "That’s true, but I almost got an upskirt earlier when you walked over me."
        show dawn dresshorny with dissolve
        dawn "Hehe, what lies under my skirt? Perhaps it’s a mystery for a detective like yourself."
        "Oh? Her hand reaches for her thigh and slowly rides up her skirt."
        "With each passing second, I can see more and more of her exposed fur…"
        "Is this finally happening?"
        show dawn dresssatisfied with dissolve
        dawn "Oohhh, did your cock just twitch? Looks like it wants to come out to play; it wouldn’t be the only thing…"
        mc "Ah? You were staring at it?"
        show dawn dresshappy with dissolve
        dawn "And where were you staring?"
        dawn "Mmm… I’m still hungry… Can you lie down?"
        mc "Huh? What correlation do those two things have? Do you want some of my fries?"
        show dawn dresshorny with dissolve
        dawn "Take a hint, big boy…"
        hide dawn with dissolve
        label dawnv2bj:
            pass
        "Dawn crawls over to me and pushes me down onto the soft carpet. Now I’m really getting erect!"
        show dawn dresshorny with dissolve:
            xalign 0.5
            ypos 300
        "She straddles my thighs, then brings one hand under her dress and between her legs."
        "I can merely hear an obscene schlicking sound which causes my member to stand to attention in record time."
        show dawn dresssatisfied with dissolve
        dawn "Want to see how wet I am?"
        mc "Uhm… Yeah?"
        show dawn dresshorny with dissolve
        dawn "She playfully lifts her fingers into a peace sign; there are a few trails of grool connecting the two fingers."
        dawn "Now… What am I going to do to you, exactly? You’re like a wild devil dancing in the palm of my hand."
        "She leans down and her fingers seductively crawl up my thigh until they’re tentatively at the base of my twitching erection."
        show dawn dresssatisfied with dissolve
        dawn "Oh my… Did I do this?"
        play music sex1 fadein 3.0
        scene dawnb blowjob
        show dawn blowjob1
        with dissolve
        "She grins and adjusts her position until her face is even closer to the tip. The subtle removal of her dress’s shoulder straps so her breasts spill out wasn’t missed."
        play ambience blowjob fadein 2.0
        "Despite her usual slow burn flirtatious nature, she’s quick to take my cock into her mouth, lustfully sucking at the head while her tongue flickers at the tip."
        "Simultaneously she takes to time to adjust herself so her breasts are brazenly pushed against my shaft, where she continues to fondle her breasts enticingly now that they’re in perfect view."
        dawn "You finally saw something under my dress, mmhehe, like what you see, my little duckling? *Slurp, lick*"
        "I nod as her piercing bedroom eyes make me weak, her hot mouth slowly consuming more and more of my sensitive throbbing cock."
        "Her long mare tongue eagerly working my shaft as it swirls and twirls against every available inch."
        dawn "You like my breasts, don’t you? How about we make this a paizuri and a blowjob…"
        "She readjusts herself again, using her arms to squish her breasts around the base of my shaft."
        show dawn blowjob2 with dissolve
        "Dawn smirks as she lewdly drools around the connection and provides a few small thrusts. It’s impressive how warm and tight a mare’s breasts can feel."
        "Working her tits with her arms, she indirectly pushes and slides them along the length of my shaft, giving shallow pumps to my broad cock, while her tantalising tongue works wonders on my tip."
        "The combination of these two pleasures may just be enough to bring me to an orgasm, especially so as she speeds up the efforts of her titfuck."
        show dawn blowjob1 with dissolve
        dawn "Mmmphh… Mmm… *Schlurp, lick* Your cock is so soft and tasty, hehe."
        mc "T-Tasty?"
        dawn "Mmmphh, mmphh… Ish time for yoush to cumsh! Mm, mmmm…"
        dawn "Ten… Nine… Eight…"
        show dawn blowjob2 with dissolve
        "She giggles causing her mouth to vibrate slightly. She closes her eyes as she redoubles her effort, her purpose to bring me to an orgasm is clear."
        dawn "Seven… six… five…"
        "My cock throbs and grows increasingly tight as the pressure of my orgasm slowly rises. The feeling between her soft, pillowy tits becomes increasingly pleasureful."
        dawn "Four… three… tw- wah?"
        play sound cum
        show dawn blowjob3 with cum
        play sound cum
        show dawn blowjob3 with cum
        "The mounting pressure comes to a boiling point as I inadvertently thrust into her mouth and begin to unload."
        play sound cum
        show dawn blowjob3 with cum
        play sound cum
        show dawn blowjob3 with cum
        stop ambience fadeout 3.0
        "Dawn dutifully pushes her head forward, deepthroating my cock as the semen splashes the back of her throat with several thick loads."
        show dawn blowjob4 with dissolve
        stop music fadeout 3.0
        "She swallows down each droplet before she pulls out and sighs."
        dawn "Ohh, you’re an impatient man…"
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        scene bg dawnsroomnight with dissolve
        show dawn dresshorny with dissolve
        play ambience ambiencenight fadein 3.0
        "Without a droplet of semen to be seen, she slips the straps of her dress back up and smirks."
        dawn "Just how I like them."
        mc "Oohh, I’m exhausted…"
        show dawn dresshappy with dissolve
        dawn "Oh yes, all that laying around while a woman did all the work must have been very tiring for you, my wittle kitten. I hope you'll be able to keep up next time."
        mc "It was more the dancing, actually… Well, never mind... That was really good."
        "I stand up and stretch before going to grab my satchel."
        show dawn dresshorny with dissolve
        dawn "Considering how late it is, I simply couldn’t ask you to walk all the way home… So, stray kitten, will you stay here tonight?"
        mc "Ah, I’d really appreciate that. Thank you, Dawn."
        show dawn dresssatisfied with dissolve
        dawn "Ohh, oh my… I’ve made a big mistake... I just realized; I only have a single bed!"
        show dawn dresshappy with dissolve
        dawn "A single, single bed! That means, we’d have to cuddle up very, very close…"
        mc "Oh… Really? But you have such an important role, you own a nightclub and-"
        show dawn dresshorny with dissolve
        dawn "And you have such broad shoulders too… I guess that means I’ll have to be on top…"
        mc "I can sleep on the couch, if you’d like."
        show dawn dressangry with dissolve
        dawn "Heavens forbid, can’t you take a hint? You can be my teddy bear tonight."
        hide dawn with dissolve
        "She pulls me along into her bedroom… Yeah, she really does have a single bed."
        scene bg dawnsroomnight with dissolve
        mc "Hey, this means I’ll finally get to see you naked!"
        show dawn dresssatisfied with dissolve
        dawn "Oh, will it? Let’s see if your eyesight lives up to your pet name, kitten."
        scene bg black with dissolve
        "Before I can even reply, she has turned off the light and closed the door…"
        "The room is literally pitch black; I cannot see a single thing."
        play sound movement
        "The only thing to reach my senses is a teasing giggle and the sound of fabric being removed."
        play sound movement
        "Ah, I can hear the sound of someone getting into bed."
        dawn "Over here, lover… Follow the sound of my melodious voice…"
        "I shimmy over carefully in the dark, wanting to not stub my toe. The moment I get close to the bed the playful mare pulls me into a cuddle."
        play sound movement
        "*Shuffle, shuffle* She leads my head to a pillow, pulls the covers around us both and wraps her body around mine."
        "Ooohh, she’s naked… Her thighs are wrapped around me too. If it wasn’t for my recent ejaculation, I’d definitely be getting a boner."
        "She’s extremely warm, and she has a distinctly pleasant perfume on."
        "This is nice…"
        dawn "Goodnight, dearie..."
        mc "Sleep well."
        "Guess I’ll see her naked in the morning, then…"
        stop ambience fadeout 2.0
        "…"
        play ambience ambienceday fadein 3.0
        "Ahhh…"
        "I’m… cold…"
        show bg dawnsroomnight with dissolve
        "Sheesh, from the moment my head hit the pillow I was out like a light."
        "I sit up and look around the dimly lit room. The door is ajar; looks like I’m alone."
        show bg dawnsroom with dissolve
        "I get up and stretch as I walk into the main room, Dawn is tapping away at a mechanical keyboard as she turns to greet me."
        show dawn dresshappy with dissolve
        dawn "You slept like a…. *Yaaawwn*… Sorry, it’s hard for me to come up with innuendos in the morning…"
        "Awh… She’s fully dressed…"
        "Same clothes as yesterday too. Does she just keep several of the same dress in a closet, or something?"
        if dawnv2c14 == 1:
            "Maybe she used magic to duplicate a lot of them, heh."
            "Wait... I know that duplicating money isn't allowed, but what about duplicating other things? I should pester Moxie about this later."
        mc "Good morning, Dawn. What time is it?"
        show dawn dresslaughing with dissolve
        dawn "Mmm… Looks like it’s 7:30am, not bad, kitten. I half expected you to be the sleep-in type."
        mc "Ah, not really. I have too many important things going on to stay in bed all day."
        show dawn dresshappy with dissolve
        dawn "Oh? I bet I could change your mind, hehe."
        show dawn dressneutral with dissolve
        dawn "Ahhh, also… Sorry about the blowjob last night, I can get remarkably thirsty when I’m drunk."
        mc "Don’t worry about it, I guess I’m used to it. I’ve never had someone apologize though, what gives?"
        show dawn dresshorny with dissolve
        dawn "Oh? Hehehe, I was planning on saving the sexual acts until after our little adventure."
        dawn "My, my… I hope you don’t think I’m some kind of easy sleazy gal."
        dawn "Well, you know what they say, darling… Every good girl can become a devishly naughty one for the right guy..."
        mc "*Gulp* Understood, ma’am!"
        show dawn dresshappy with dissolve
        dawn "Goodness me, well… I’m going to shower, masturbate, and do some work."
        dawn "Come visit me any morning before around… 8:30ish. Even today, if you want. Just use the doorbell on the back of the nightclub."
        mc "Sure thing, see you later Dawn."
        show dawn dresshorny with dissolve
        dawn "I’ll be thinking about you, Kitten. Jaa ne."
        hide dawn with dissolve
        "Hm? Thinking about me for what?"
        "Ooohh..."
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        scene bg black with dissolve
        jump altmorning

        ## Day 2
    label dawnvisit3:
        $ dawnvisit += 1
        scene bg arcadiaalley with dissolve
        stop music fadeout 3.0
        "Alright, here’s the backdoor of the nightclub."
        "Come to think of it, looking up from where I’m stood, isn’t that where Dawn’s desktop computer is? Her window’s open too."
        mc "Hey, Dawn!"
        "Ah, she heard me."
        dawn "Helllooo duckling! Were my earlier instructions too hard for you to follow?"
        mc "What, you mean the doorbell? I just thought it’d be more fun to call out to you."
        dawn "Ah, well. I can’t actually let you in unless you buzz the door first, you dolt!"
        "Oh, now I feel a little stupid."
        "I press the doorbell and it lets out a dull buzz. After a few seconds there’s a click, and the door has automatically unlocked."
        "As I open the door and move to step inside- "
        play music dawn fadein 3.0
        show dawn dresshappy with dissolve
        dawn "Well, let’s be off to the castle then!"
        mc "Wait, you're just leaving? That means I didn’t need to buzz the door!"
        show dawn dresslaughing with dissolve
        dawn "Think of it as a little test! If you couldn’t play with that button, how are you ever going to play with mine?"
        "She winks and skips past me. I can’t even complain when her teasing always ends in such a delectable innuendo."
        scene bg black with dissolve
        scene bg castlelivingroom with dissolve
        "We make our way to the castle, through the usual corridors and to Aurora’s living quarters."
        show aurorab dress:
            xpos 0
            ypos -20
        show aurora happy:
            xpos 0
            ypos -20
        with dissolve
        aurora "Greetings Dawn, [playername]. Certainly not a combination of people I was expecting, but it makes a lot of sense that you two would bond."
        show dawn dresshappy with dissolve:
            xpos 750
            ypos 30
        dawn "Ahh, you really should have told me there was such a special man available for the taking."
        show aurora laughing with dissolve
        aurora "My apologies Dawn, I was going to include him in the next month’s report."
        show dawn dresslaughing with dissolve
        dawn "No need, I’ve successfully claimed him for the day!"
        show aurora happy with dissolve
        aurora "My, I’m jealous! How are you doing anyway, Dawn?"
        show dawn dresshappy with dissolve
        dawn "Really good, with [playername]’s information I might be able to expand my boundary theories."
        show aurora surprised with dissolve
        aurora "Ohh, I see. Will you be using the mirror portals?"
        dawn "Yeah, if that’s okay with you. Me and [playername] are going on a small trip."
        dawn "I’ve got a few books to return to the normie human world, and I’d like to bring [playername] too."
        show aurora neutral with dissolve
        aurora "Mm, [playername] too? I suppose I can allow it, since it may be his universe after all…"
        aurora "But you shouldn’t have told anyone about that, [playername]…"
        mc "Well uh, I didn’t…"
        show dawn dresssatisfied with dissolve
        dawn "It was all my intuition, your majesty. He’ll be immensely useful for my studies, so it was inevitable that I’d sniff him out."
        show aurora laughing with dissolve
        aurora "That is certainly true… Very well, let us not keep each other any longer. Safe journeys to the both of you."
        mc "Thank you, Aurora."
        stop ambience fadeout 3.0
        stop music fadeout 3.0
        scene bg castlemirrors1 with dissolve
        ## into the mirror room
        play ambience ambiencecave
        mc "So, uhh Dawn… When do I get some clothes? I believe I did ask for some."
        show dawn dresshorny with dissolve
        dawn "Don’t worry, my cute wittle adorable kitten! When you enter the portal, there are clothes prepared for you to immediately wear."
        mc "Oh really? That’s pretty convenient, I can imagine why that’d be necessary."
        show dawn dresshappy with dissolve
        dawn "One more thing, I’d rather not bore you by bringing you to the library, especially since there’s something far more interesting you could be doing in the meantime…"
        mc "What do you mean?"
        show dawn dresssatisfied with dissolve
        dawn "There’s a lady on the other side, she’s a total cougar."
        dawn "Perhaps it’d be in your best interest to get to know her {i}very well{/i} in the half an hour I’ll be gone."
        mc "Like… have sex with her...?"
        show dawn dresshappy with dissolve
        dawn "Call it a challenge."
        mc "W-Wha? What do you get out of that?"
        show dawn dresshorny with dissolve
        dawn "Wouldn’t you like to know, mmmhehehehe…"
        hide dawn with dissolve
        "Dawn leaves me somewhat confused as she steps into the center portal and immediately vanishes from sight…"
        "A challenge to have sex with a ‘cougar’? I wanna have sex with you Dawn, not some random human."
        "I can’t predict this girl at all. That’s the last thought on my mind as I enter the portal and for the first time…"
        stop ambience fadeout 3.0
        play sound transition1
        scene bg black with pixellate
        "..."
        show bg humancloset with s
        "Where am I?"
        "Looks like some kind of closet, and we just slipped out of a mirror on the wall."
        "I can see some clothes. The feeling of even this very small space makes me feel nostalgic, as sweet summer dresses rest upon clothing hangers, with the light smell of fabric softener."
        "The simple clothing closet is a rarity in a world like Arcadia..."
        "I'm finally back..."
        "My old universe. Or at least, a very similar one."
        dawn "A-ha! My old jacket. The dress is perhaps a little too fancy for this universe, so this should help me blend in a bit."
        show dawn humanhorny with dissolve:
            xpos 250
            ypos 15
        dawn "How do I look?"
        mc "Great! The blonde hair is a nice touch for your human disguise. Although your dress may still raise some eyebrows."
        mc "But... Are {i}all{/i} the clothes in here for women?"
        show dawn humanhappy with dissolve
        dawn "Of course they are! Who else is gonna be using these portals?"
        dawn "I can hear someone outside, get ready!"
        "Before I can even complain, Dawn swings the closet door wide open..."
        play music aurora fadein 5.0
        show bg humanoffice with dissolve
        show principalaurora shappy with dissolve:
            xpos 750
            ypos 0
        paurora "Phew, and here I thought my closet was haunted again. Come on in, dearies, no need to be shy."
        "… AH?! I’M THE ONLY ONE THAT’S NAKED!"
        show principalaurora shorny with dissolve
        paurora "Who's our new and lewd friend?"
        "Oh my god, you'd think I'd be used to being nude in front of women, but I feel so embarrassed right now."
        show principalaurora shappy with dissolve
        paurora "Goodness me, did the wormhole not copy his clothing? What a strange occurrence, perhaps I should study it…?"
        show dawn humanlaughing with dissolve
        dawn "[playername], meet Principal Aurora. PhD in theoretical physics, and the only person in the entire world to know about this portal."
        show principalaurora slaughing with dissolve
        paurora "It's pleasure- I mean, it's a pleasure to make your acquaintance."
        mc "Ahhhh… N-Nice to meet you?"
        "No way… A human version of Aurora? Living in my world?"
        "That’s impossible, right? There’s no way this lady is thousands of years old. She can’t be any older than thirty."
        "And the hair... There's no way that's natural, right?"
        "Damn though... Principal Aurora has kinda got it going on."
        "So, what’s the deal? I don’t understand this universe thing at all."
        show principalaurora shappy with dissolve
        paurora "Mmm… So, is there anything I can help you with today, Dawn?"
        show dawn humanhappy with dissolve
        dawn "Yeah, if that’s okay with you. This duckling and I have some business here."
        dawn "I’ve got a few books to return to the library. While I do that, do you think you could look after him? I need to buy him some clothes."
        show principalaurora shorny with dissolve
        paurora "Mm, [playername]? I suppose I can allow it… Give us, say… thirty minutes?"
        show dawn humanhorny with dissolve
        dawn "Heh... I see..."
        dawn "In that case, you can count on me, I shan’t be a minute earlier!"
        "Huh? That’s strange… Why is Aurora deciding the timeframe? Shouldn't Dawn be deciding that?"
        show dawn humanhappy with dissolve
        dawn "Oh, and don’t worry [playername], there’s nothing you know that you can’t tell the fine principal here, so proceed to spill your mouth! Hehe."
        hide dawn with dissolve
        "And then Dawn leaves… Oh jeez, I’m still naked! Why am I so embarrassed about this after doing it casually for so long?"
        show principalaurora shappy:
            xpos 750
            linear 1.0 xpos 475
        paurora "Hmm… It’s nice to meet you, [playername]. Are you a subordinate of Dawn, by chance?"
        "Oh god, she's so hot..."
        "Did she just call me a subordinate? I guess this Aurora doesn’t seem to know nearly as much as the other…"
        "It makes sense, not having magic would make a huge difference."
        mc "Not exactly, I’m more of a sightseer. I’m here for nostalgic purposes, since this is the universe I’m originally from."
        show principalaurora sneutral with dissolve
        paurora "Oh my, and here I thought that was forbidden."
        paurora "So, you're not another creature in disguise, like Dawn? I’ve only encountered Dawn using these portals."
        mc "Ah, it’s complicated… Anyway, how do you know about this portal?"
        show principalaurora shappy with dissolve
        paurora "I’ll be honest, it just showed up here one day… And later, another version of my sister and I appeared!"
        "I see, it makes sense that a portal in Aurora’s house would be closely linked to the Aurora of another universe."
        show principalaurora slaughing with dissolve
        paurora "It’s truly an honour to know that my alternate universe selves are so successful and amazing! I even dyed my hair just like hers."
        paurora "What has the other universe been like for you? I’ve only heard brief snippets from Dawn."
        menu:
            "The girls are really horny over there. Like, you have no idea!":
                show principalaurora shorny with dissolve
                paurora "Oh my, is that so? I guess that isn’t so different after all, hehe!"
            "Mostly working and meeting new people.":
                show principalaurora shappy with dissolve
                paurora "Ohh, I see!"
            "They can do magic, and some of them can fly! Oh, and they're all ponies!":
                show principalaurora shappy with dissolve
                paurora "Mhm, mhm. I've heard of these things before, although they seem quite new to you."
        paurora "I suppose I don’t actually know how long you’ve been there."
        mc "Must have been about [days] days now…"
        show principalaurora slaughing with dissolve
        paurora "Ahh, I see. Are you returning to this universe, then?"
        mc "Actually, no. I’m going to stay in the other universe. I have nothing here for me anymore. It’s complicated."
        "I know Dawn said there’s nothing I know that Aurora doesn’t. But, actually, there are things I know that not even Dawn knows."
        show principalaurora sneutral with dissolve
        paurora "Oohh, what a shame…"
        mc "It’s not so bad."
        show principalaurora shappy with dissolve
        paurora "Guess it can’t be helped."
        "The conversation is slowing down a little… And I’m still naked…"
        "Wait… Is this… the cougar?"
        "Is Aurora the cougar I was challenged to sleep with by Dawn?"
        "I'm not sure who I'm more ashamed in... Myself for not realizing Aurora was the cougar, or Dawn for so obviously setting us up. Sheesh, that girl…"
        stop music fadeout 30.0
        menu:
            "Unfortunately, that world doesn’t have any girls as beautiful as you":
                show principalaurora shorny with dissolve
                paurora "Ohh, myyyy… You’re such a flatterer, [playername]. I know that can’t be entirely true, because there’s another version of me! *Giggle*"
            "Unfortunately, all my old family and friends aren’t in that world.":
                show principalaurora sneutral with dissolve
                paurora "Ahh, that’s a shame. It must have been difficult for you to acclimatize."

        show principalaurora slaughing with dissolve
        paurora "I hope the mares have been treating you right, dearie! My, if I could pry, I wonder what the sex life of a man like you is like?"
        paurora "Must be good! *Giggle*"
        menu:
            "Sometimes I miss the feeling of a human, that’s one of the reasons I came here.":
                show principalaurora shorny with dissolve
                paurora "Ohh…"
                "Aurora’s expression turns to bedroom eyes for a second. I think I hit a soft spot."
                "She steps towards me and whispers seductively…"
                paurora "Would you like to see just how amazing it can feel?"
            "Ponies are pretty nice; their fur is really soft.":
                show principalaurora shorny with dissolve
                paurora "I bet, I bet… But how does it compare to the soft, supple curves to a human lady?"
        menu:
            "I’ve never done it with a human before.":
                show principalaurora shappy with dissolve
                paurora "There’s a first time for everything… It’d be such a shame for you to never find out."
                show principalaurora shorny with dissolve
                paurora "Darling… may I?"
                mc "*Gulp*"
            "About the same":
                show principalaurora shorny with dissolve
                paurora "Is that a challenge, darling? Here, bring your hands to my hips."
                mc "Oh? Okay…"
                "Turns out that was just a ploy to get closer to me, as she presses her bosom against my chest."

        "My cock is starting to stiffen slightly, and that fact isn’t going unnoticed."
        show principalaurora shappy with dissolve
        paurora "Mmm, if we keep this up, you’ll get an erection…"
        mc "That wouldn’t be so bad, specifically if someone were to help me do something about it."
        show principalaurora shorny with dissolve
        paurora "Perhaps I can make you more comfortable by doing this…"
        label ppclsex:
            pass
        hide principalaurora with dissolve
        play sound movement
        "…"
        show principalaurora laughing with dissolve:
            xalign 0.5
        paurora "There we go, now we’re even! *Giggles*"
        mc "Oh lord, you really know how to get what you want, don’t you?"
        show principalaurora horny with dissolve
        paurora "Mmm… I think I have a lady boner that requires taking care of too. *Giggles*"
        paurora "Think you can help me, big boy?"
        "The woman who is so blatantly a cougar, wraps her slender fingers around my growing cock and gently starts to jack me off into a full throbbing erection."
        mc "*Twitch, throb*"
        "Sheesh, just who's idea was this in the first place? Dawn's or Principal Aurora's?"
        show principalaurora happy with dissolve
        paurora "Okay darling, sit back on my desk for a second."
        mc "Are we going to do reverse standing cowgirl?"
        show principalaurora horny with dissolve
        paurora "Even better, darling."
        stop music fadeout 3.0
        scene bg black with dissolve
        "…"
        paurora "Perfect, babe… Now lift my legs up, and lock them with your elbows."
        play sound movement
        mc "Huh, like this?"
        play music sex1 fadein 3.0
        show principalaurorab sex
        show principalaurora sex1
        with dissolve
        paurora "Ohhh, yes! Ooohh... I’m so wet."
        play sound cum
        show principalaurora sex2 with dissolve
        "She lustfully wiggles her hips until the tip of my cock immediately slides in, she was so quick that I barely had time to adjust to this strange position."
        "Simply having my dick inside a human female feels different. I was a virgin before I appeared in Arcadia, but I wasn’t anticipating it to be so different to a mare."
        "I’m not even moving, but from the mere penetration she’s panting like a mare in heat, I guess that’s no different."
        paurora "Go wild! Haah, haah."
        "I’m as hard as I’ve ever been, and her pussy is constantly dripping with feminine arousal around my cock."
        play ambience sex fadein 3.0
        "I push my hips forward, and my cock slides with surprising ease and depth. The angle of penetration from this position is more efficient than I had anticipated."
        "It feels incredibly pleasurable as I repeatedly plunge into the depths of Aurora’s tight warm pussy, especially as it constantly squeezes around each and every inch of my shaft."
        paurora "Ohh myy, you’re a big boy… The moment I saw you nude, I just knew, hehe."
        "I’m fortunate that there’s a mirror in the corner of the room, allowing me to admire her body even from this angle. She looks so sexy right now, and she’s all mine."
        "As my cock gets wetter and slicker with her juices, I find myself able to increase my pace as the motions get smoother."
        paurora "Mmm… No need to hold back, [playername], I’ve been wet and ready for a thrashing ever since Dawn left."
        "I push back and start fucking the horny principal even harder. As our skin connects the lack of fur causes an even more satisfying slap sound than I’m used to."
        "Also, unlike a mare, a human’s pussy doesn’t get as wet. Perhaps it’s because a mares need more lubricants to handle a stallion’s cock."
        "Regardless, the reduced amount of wetness increases the friction and tight feeling of her pussy immensely."
        "Having sex with another human shouldn’t feel so alien and unusual. Truly, I’m a special case."
        show principalaurora sex3 with dissolve
        paurora "Ahhh, jesus, what do they teach you over there? Mmm, mmmphh, you’re a good fuck!"
        "She flinches and quivers under my grasp, my cock plunging repeatedly into her deepest and most sensitive spots."
        "As I speed up my fucking, her entire body wriggles more, especially her large breasts which rock back and forth in tandem with each thrust."
        "She’s so squishy and soft, almost her entire body ripples like a body of water receiving a droplet."
        "And this increased friction… It feels really good, I can already feel my orgasm building, my mind going white with pleasure."
        paurora "Ooohh, ohh, I’m so close! You’re gonna make me lose my mind! Haahh, aaah!"
        "Even though I try to hold back my orgasm, her moaning causes it to rise almost immediately."
        play sound cum
        show principalaurora sex4 with cum
        "The moment I feel her pussy clench around my shaft, my orgasm hits, exploding forcefully from my tip, borderline prematurely."
        play sound cum
        show principalaurora sex4 with cum
        "The cougar's pussy has me beat, I can't hold back as I relentlessly unload my cum deep inside her."
        play sound cum
        show principalaurora sex4 with cum
        "Aurora’s body arches and coils as a full-body orgasm consumes her. I continuously and recklessly pound her pussy for each droplet of pleasure it’s worth."
        "In my lust, I don’t slow down a second, continuing to fuck her throu-!!!"
        scene bg humanoffice with dissolve
        show dawn humanneutral with dissolve
        dawn "…"
        mc "…"
        play sound cum
        show principalaurorab sex
        show principalaurora sex4
        with cum
        paurora "Ahh, ahhh, yess! Ahhh!"
        play sound cum
        show principalaurora sex5 with cum
        "Greedy as ever, Dawn turns the end of this rutting into an unexpected threesome."
        "Taking advantage of our orgasmic states, she kneels down and licks the point of our connection, catching any stray droplets of cum with her tongue."
        dawn "Mmpphh, mmm... So delicious..."
        show principalaurora sex6 with dissolve
        stop ambience fadeout 3.0
        stop music fadeout 3.0
        "Aurora’s pussy mercilessly milks me until the very end of my orgasm."
        "With my ejaculation subsided, Dawn wastes no time pulling my erection out and taking the tip into her mouth as she cleans the cum off it."
        "With that done, she turns her attention to Aurora’s sloppy pussy, as the one holding Aurora up, I don’t even have the opportunity to sidle away."
        dawn "Mmm… mmm…"
        paurora "Ahh, D-Dawn… Ahhh… I… Ahhh."
        dawn "Heresh yours clothesh! *Slurp, lick*"
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        scene bg humanoffice with dissolve
        show dawn humanhorny with dissolve:
            xpos 250
            ypos 15
        "Dawn stands up, wipes her mouth and hands me a bag that she had dropped at the door. I let Aurora down and go to put the clothes on."
        show principalaurora neutral with dissolve:
            xpos 750
        paurora "That wasn't anywhere close to thirty minutes, you cheeky girl."
        dawn "Mmmhehe, it wasn't?"
        paurora "And... hey, [playername]…"
        mc "Ah, yeah? Sorry, I’m not really sure what to say yet. My mind’s still processing what just happened."
        play music challenge fadein 3.0
        paurora "That doesn’t matter… You… came inside… You idiot, what if I get pregnant?"
        show dawn humanneutral with dissolve
        mc "P-Pregnant?!"
        "Oh shit! That’s not something I’ve thought about in fuckin’ ages! Of course I can get this Aurora pregnant, damnit!"
        show dawn humanlaughing with dissolve
        dawn "You could have just let me swallow it all, tsk tsk."
        mc "What’s with you walking in here and participating anyway? That was unexpected!"
        show dawn humanhorny with dissolve
        dawn "Awhh, there’s no way I’m letting you two have all the fun today…"
        paurora "Jeeeez, I’m probably ovulating around this time of the month too…"
        "Ah… All three of us are definitely on different pages."
        "This Aurora is nothing like the one I know, she’s so much more eccentric."
        "I kinda feel bad though."
        mc "Uhm, want me to get an emergency pill?"
        show dawn humanlaughing with dissolve
        dawn "Don’tcha worry, we’ll get one when we’re out. Won’t we, [playername]? We’re coming back here anyway. "
        show principalaurora horny with dissolve
        paurora "Very well... I'll be here until 5:00pm."
        paurora "That was quite pleasant, [playername]. I hope I was able to make this trip sufficiently ‘nostalgic’. *Giggle*"
        show dawn humanhorny with dissolve
        dawn "I bet I’ll need to buy myself some too, considering all the fun we’re going to have."
        mc "Fairly sure I can’t get you pregnant, Dawn."
        show dawn humanlaughing with dissolve
        dawn "I’m going to make you cum in me so much, the eggs will have no choice!"
        mc "That’s by far the strangest thing you’ve ever said to me."
        show dawn humanhappy with dissolve
        dawn "Sounds like I haven’t been trying hard enough if that’s the strangest thing…"
        show principalaurora happy with dissolve
        paurora "Come on, you troublemakers. Shoo now."
        stop music fadeout 3.0
        scene bg black with dissolve
        "…"
        play music dawn fadein 3.0
        play ambience ambienceday fadein 3.0
        show bg humancity with dissolve
        mc "It feels so weird to be back… In my hometown no less."
        mc "I suppose it makes sense that Arcadia and its citizens would be so close to my original home."
        show dawn humanhorny with dissolve
        dawn "Yep, you could say that this human town is Arcadia, if not in name, in spirit. If we run into you, let’s see if he’s up for a threesome."
        mc "That’d be an awkward conversation, fortunately I’d be at college at this time."
        mc "By the way, anything you want to know in particular?"
        show dawn humanhappy with dissolve
        dawn "If you could tell me about some interesting books and technologies, that would be great."
        dawn "Additionally, while I expect you’re not an expert, I’d like to know about the potential history and past of this universe."
        mc "Alright, try me."
        hide dawn with dissolve
        "I spend a while answering Dawn’s questions as we wander. It’s so nostalgic, I can’t help but stop and stare."
        "It’s almost impossible to believe that a magical world was hiding under my nose and in a random cougar’s mirror this entire time."
        "Then again, there’s always the strong chance that this isn’t my original universe. What are the odds that this wormhole happened to lead to my exact original universe?"
        "I know for a fact that the odds are one in infinity. I’m not sure if it’s more naïve to ignore that fact, or simply accept it and not care."
        "All I know is that this universe is a good enough representation of my old home."
        scene bg humanstreet with dissolve
        show dawn humanhappy with dissolve
        dawn "Well, here we are. This here’s my apartment."
        mc "You own property here? How’d you manage that?"
        show dawn humanhorny with dissolve
        dawn "This world is far too easy to cheat with magic. I can simply conjure fake money here, there’s no magic counterfeit checking."
        scene bg humanapartment with dissolve
        "We step into Dawn’s apartment. It's extremely nice here, the rent must be pretty high."
        "She stretches as she finds herself at a similar looking desktop setup as the other universe."
        "Actually, everything is similar, almost too similar. Could this be the ‘other’ Dawn’s home too? Hm… Doubt it."
        show dawn humanhappy with dissolve
        dawn "So, what do you think? I know I said I’d bring you here to ‘ask questions’ and pester you for information…"
        dawn "But the truth is, I just wanted to give you the opportunity to re-experience your old world again."
        show dawn humanneutral with dissolve
        dawn "*Siiigh* But do you need to look so dejected? I thought you’d be happier than this…"
        mc "I’m extremely grateful for the opportunity. I apologize that I haven’t been smiling much, I’ve been feeling rather melancholic about it."
        show dawn humanhappy with dissolve
        dawn "I thought maybe… Maybe you’d want to live here, in my apartment?"
        dawn "I mean, did it even occur to Aurora that maybe you’d want to stay in this world, even with nothing…?"
        "She wants me to live here?"
        "It wouldn't be so bad... Especially if Dawn is around, a magical girlfriend is always a plus..."
        "But..."
        mc "Well… that was certainly one of the reasons I didn’t come back. No home, no house, no possessions."
        mc "And while I appreciate your offer, I’ve long given up any desire to return here."
        show dawn humanhappy with dissolve
        dawn "Hm? I mean, it’s not that I blame you. I just think a choice is better than nothing."
        mc "You see... To be back in this world, with all my friends and family, yet unable to ever communicate with them... It's a complicated feeling."
        mc "You’ve helped bring back a lot of memories, but they’re memories that are perhaps best left alone."
        mc "If I stayed here, I’d be worried about family, friends and more."
        mc "But… In Arcadia, I essentially have a family, and friends."
        mc "Well, maybe a ‘family’ is stretching the definition."
        "Especially since I fuck most of them."
        mc "But truly, the people there are so kind and welcoming."
        show dawn humanneutral with dissolve
        dawn "Don’t feel like you’d be throwing away their kindness if you chose to stay here…"
        dawn "Mm… But, it’s not like I disagree. This world can be somewhat cold and unforgiving."
        mc "I’m glad everyone is so open-hearted in Arcadia; it made the transition far easier."
        mc "It was less like dying and starting again from the beginning, it was more like going to heaven."
        show dawn humanhappy with dissolve
        dawn "Psshhh, if it’s heaven, then why have you been sinning so much? Mmmhehe!"
        dawn "Anyway, let me pack a few things I came for, and then we’ll be off."
        show dawn humanneutral with dissolve
        dawn "Watching you stare off into the distance like a lost puppy is aching my heart."
        stop music fadeout 3.0
        scene bg black with dissolve
        "…"
        scene bg humanoffice with dissolve
        show principalaurora shappy with dissolve:
            xpos 750
        play music day2 fadein 3.0
        paurora "Welcome back, and just before closing time, you had me worried for a moment."
        show dawn humanhappy with dissolve:
            xpos 250
            ypos 20
        dawn "Sorry Aurora, I was just squeezing out as much of [playername] as possible."
        show principalaurora slaughing with dissolve
        paurora "My, what a popular man…"
        mc "Nothing of the sort happened!"
        show dawn humanlaughing with dissolve
        dawn "Yet! Mmhehe!"
        show principalaurora shorny with dissolve
        paurora "You certainly picked me the best you could, hehe. I wasn't expecting him to be a natural human, though!"
        mc "Wait, what does that mean?!"
        paurora "Oh? Did I say too much?"
        show dawn humanhorny with dissolve
        dawn "You let that slip on purpose, Aura. I know your game, heh."
        dawn "Here are your pills."
        show principalaurora shappy with dissolve
        paurora "Thank you, darlings! There are quite a lot here, I only needed one…"
        show dawn humanhappy with dissolve
        dawn "What do you mean? You’ll need the others for the next time [playername] creampies you."
        mc "Next time?"
        show principalaurora shorny with dissolve
        paurora "Oohh, next time… I see, I see… The office is always open for that sort of business from between 8:00am to 9:00am. *Giggle*"
        if auroravisit1 == 1:
            "Oh great, now I have the option of fucking both Auroras every morning. Is there some kind of converging universe phenomena that I’m yet to understand?"
        else:
            pass
        "I can't believe Dawn set me up like this. I'm both elated and a teeny bit offended."
        show dawn humanhorny with dissolve
        dawn "I’d offer him now, I truly would, but I need to have my fill, got it? *Wink*"
        show principalaurora slaughing with dissolve
        paurora "Violate him for me, darling!"
        mc "V-Violate?!"
        show dawn humanlaughing with dissolve
        dawn "Enough talk, come ooonnn…"
        scene bg humancloset with dissolve
        "Practically dragging me by the collar of my jacket, Dawn pushes me into the closet with the mirror and we’re whisked away into the anthro world."
        stop music fadeout 3.0
        play sound transition1
        scene bg black with dissolve
        pause 2.0
        scene bg castlemirrors1 with dissolve
        "And we're back!"
        show bg castlehallway with dissolve
        show bg arcadiastreetsnoui with dissolve
        "Walking through the streets while fully clothed is certainly a strange experience. I never thought I'd think that, but these are strange times indeed."
        show bg dawnsroom with dissolve

        ## Universe talk
        stop ambience fadeout 100.0
        play music dawn
        "We return to her abode on the first floor of the nightclub. It’s rather fortunate that the rooms are so well soundproofed."
        "I guess that’d be a given, you’d get no sleep otherwise."
        show dawn dresshappy with dissolve:
            xalign 0.5
        dawn "Thank you for your help. With a second set of hands we were able to bring back tons of goodies."
        mc "Yeah, don’t worry about it."
        "I place the two bags I’m carrying down and curiously look at a few objects inside it."
        "A book on anatomy, a holiday brochure, a high school history book, a dictionary…"
        "And a few other things which I imagine are for leisure, including some chocolates, a... vibrating dildo... and a smartphone."
        "A smartphone, huh? Now that’s an interesting little device that we don’t see in this world."
        show dawn dresslaughing with dissolve
        dawn "Ah, I see you found my new phone! To tell you the truth, I’m pretty familiar with this magical piece of technology, we had them in the other human universe."
        mc "Oh really? I guess if there’s a demand, it’ll get made. Truly, the differences between these universes are subtle, but the implications are significant."
        show dawn dresshappy with dissolve
        dawn "They sure are, kitten. And studying subtle differences between universes is my role, I use it to expand our interuniversal understanding."
        show dawn dresshappy with dissolve:
            xalign 0.5
            linear 0.5 ypos 150
        "Dawn moves over to sit by the sofa, so I join her and sit on the other side. It’s a pretty small sofa, small enough that our bodies are pushed into contact. Is all the furniture here like this? Pfft."
        dawn "A simple question like 'Why does that world have phones, while this one doesn’t', may seem like a minor branch, but it significantly affects how the world develops."
        dawn "Let’s say, if we used a ‘dating app’ on a phone to meet up. Well suddenly, it would seem that in every universe without ‘phones’ we’d never meet up to make sweet love."
        mc "What a cruel existence that would be, truly we’re living in the best of timelines."
        show dawn dresshorny with dissolve
        dawn "Hehe, oh please, if you keep flattering me, you’ll ruin my panties."
        mc "Oh, you’re wearing them today?"
        show dawn dresssatisfied with dissolve
        dawn "Mmm, let me check…."
        hide dawn with dissolve
        "She turns around and blatantly… ‘checks’ out of sight, before returning her gaze to me and shrugging smugly."
        show dawn dresshorny with dissolve:
            xalign 0.5
            ypos 150
        dawn "Schrodinger’s panties!"
        show dawn dressneutral with dissolve
        dawn "Don’t you think it’s strange?"
        mc "Yeah, you are pretty strange! Hah, got’em."
        show dawn dresshappy with dissolve
        dawn "Hmph! You saw Aurora in that other world, and that was definitely Aurora, correct?"
        mc "Sure was, without a doubt that’s the alternate universe Aurora."
        show dawn dressneutral with dissolve
        dawn "Okay, but that’s weird, isn’t it? That universe is extraordinarily different in technology, culture and history."
        dawn "So what are the odds that despite all this branching, a character like Aurora managed to still exist? And furthermore, there’s also a Moxie, a Selene, a Melody, and more…"
        dawn "There are also counterparts to Riku, Lily, Ruby and more, although you may struggle to recognize them, since they have different eye colour, hair colour, and human hair instead of a mane."
        dawn "This more 'normal' aspect of your human world isn't carried over to the 'colourful' human world. Strange, isn't it?"
        mc "That reminds me, the Moxie I first met in my universe has brown hair."
        mc "Wow, I wonder if I’ve ever met anyone in both universes and simply not realized."
        mc "You bring up a great point though, the odds of that seem exceedingly low."
        mc "Is seems like there must be some type of ‘rubberbanding’ that makes certain individuals such as Riku always exist in a universe. Even if the implications surrounding her existence are dramatically different."
        show dawn dresshappy with dissolve
        dawn "Not a bad theory, detective kitten, but… is that really true?"
        dawn "What if both universes were only similar right ‘NOW’, like two infinitely long non-parallel lines approaching each other, colliding and then flying away to never meet again."
        dawn "The closer the lines are, the more similar they are… Wouldn’t you agree that’s a more accurate assessment?"
        mc "You certainly raise a good point, but that still means there has to be a type of ‘rubberbanding’, no?"
        mc "How else are the lines ever going to intersect. I mean, what are the odds of two completely unique universes, with completely different circumstances, suddenly gaining similarities over a few decades. Only for those similarities to fade."
        show dawn dresssatisfied with dissolve
        dawn "Well… Perhaps the odds are higher than you’d think."
        show dawn dresshappy with dissolve
        dawn "The odds that such a universe exist, are infinite to one, because… there are infinite universes."
        dawn "So these ideas we’ve discussed, no matter how insane they seem, are inevitable."
        mc "Ahh… I’ve fallen for the availability bias… I was thinking about the mirror portals too much."
        mc "I hadn’t considered that those particular universes were handpicked out of a pool of infinite. May I ask why, or how?"
        show dawn dressneutral with dissolve
        dawn "Certainly… It’s pretty interesting that you just mentioned the mirrors, considering you were gagging on your own words before."
        mc "Oh, that’s true… Weird, did Aurora take the spell off me this morning?"
        show dawn dresshorny with dissolve
        dawn "I doubt Aurora would have cast such a basic spell on you that it wouldn’t adapt based on her knowledge of what you’d be allowed to say to whom… But, what do I know? Hehe."
        mc "I see, so I can only give information Aurora consents me to give… Interesting, perhaps weird, but I’m not going to complain."
        show dawn dresslaughing with dissolve
        dawn "The wormholes in the mirror room is a biased sample size, based on a certain amount of ‘boundary’."
        "Ah… This almost certainly means that the ‘human’ universe we visited earlier isn’t mine."
        "I guess that’s just even more evidence that I’ve been reborn and should focus on living my new life."
        mc "Boundaries? I think I’ve heard about that before. That’s the unit of measurement for how much ‘magic’ power is needed to interact with the other side."
        show dawn dresshappy with dissolve
        dawn "You already knew? I guess it’d only be natural for you to know something so advanced as Moxie’s closest friend, I’m jealous! Hehe."
        dawn "But yes, I’m the one that’s studying this idea of ‘boundary’. It’s complicated, and there are plenty of nuanced ideas we could discuss."
        dawn "The reason why the mirror rooms aren’t all identical universes with single displaced atoms are because Selene only chose universes with a sufficiently high boundary."
        dawn "Specially chosen because each of the universes include both Aurora and Selene, and also a ‘different species’, although it became apparent that we had two human universes after some research."
        dawn "Currently, I’m studying to see if boundary levels fluctuate or change at all."
        dawn "Now we’ve handpicked the universes, I’d like to observe how they change over time."
        dawn "If the boundary of a universe is fixed, that means a universe will always keep a consistent amount of similarities, exactly like the ‘rubber banding’ you described."
        dawn "If the boundary constantly rises as some may surmise, it’ll be like my two infinitely long intersecting lines idea."
        dawn "But it’s also possible that the boundary merely fluctuates, like a 2D double helix."
        dawn "Or perhaps we’re just thinking about this the wrong way, who knows. That’s the fun of science!"
        mc "That’s really amazing, Dawn."
        show dawn dressneutral with dissolve
        dawn "Ahhh, it’s not so crazy, the studying is in such an infancy I barely feel like I’m doing anything productive at all."
        show dawn dresshappy with dissolve
        dawn "I’ll probably pass away before any of my research bears fruit, simply because most of the universal similarities are generational."
        show dawn dressneutral with dissolve
        dawn "In one hundred years, it's completely possible that not a single person will exists in all the mirror portal universes simultaneously. Except pony and anthro alicorns."
        dawn "Ohhh well…"
        dawn "All this talk is making me horny."
        mc "H-Horny?! No one but you would make such a drastic conversational shift."
        show dawn dresshorny with dissolve
        dawn "Hey, it’s not my fault there’s a naked dude sat next to me. You could have kept your new clothes on, but noooooooo, you just had to embrace your nudity."
        dawn "How do you think I feel having your penis in my peripheral vision the entire time and being forced to imagine incredibly naughty acts?"
        mc "N-Naughty, huh? Haven’t you gotten used to nudity yet?"
        show dawn dresssatisfied with dissolve
        dawn "Mmm, perhaps you’re right. Maybe I should remove my dress…"
        dawn "At least, I could do you the courtesy of removing her, mmheheh."
        dawn "Stand to attention big boy, you’re about to witness a miracle…"
        hide dawn with dissolve
        stop music fadeout 2.0
        "Is she talking to me, my dick, or both of us simultaneously?"
        play sound movement
        "Oh! She’s actually doing it; she’s removing her dress…"
        play music library
        show dawn satisfied with dissolve
        mc "I knew it, no panties at all!"
        show dawn horny with dissolve
        dawn "Oohh, I am wearing panties! They’re just invisible, here, come pat your hand between my legs to check!"
        "Pat, pat… She’s lying… Nice…"
        show dawn satisfied with dissolve
        dawn "Oh my, you’re getting an erection so easily. Well, if I had a cock, I’d probably already have been creating a tent in my dress, so I guess I’m even worse than you, hehe!"
        mc "I'll admit, I was starting to think you had a surprise underneath the dress."
        show dawn horny with dissolve
        dawn "Is this not a marvellous surprise?"
        mc "Well... It is, but you know what I mean."
        show dawn satisfied with dissolve
        dawn "I do, but it's just an ordinary female body. Like any of the other thousands of mares in Arcadia!"
        dawn "But you got the chance to see me unwrapped like a present after days of anticipation, it’s no wonder you’re so stiff over basic nudity."
        mc "That’s a good point, there’s really no excuse to get an erection over only seeing a nude woman anymore. But… you’re no average woman, that’s for sure."
        label dawnv3sex:
            pass
        show dawn horny with dissolve
        dawn "Well, aren’t you glad I wore a dress now? Mmmhehe!"
        dawn "You know, as a pony, my ass was always exposed… Like so…"
        show dawn butt with dissolve
        "Dawn swings around on the sofa and seductively bends at the hips to reveal her ass. My member stands to attention almost immediately at the erotic sight."
        dawn "All we had was our tails for decency… Like so..."
        "Swish, swish… Her tail flicks back and forth, making little attempt to hide her wet labia."
        dawn "All the stallions would notice, and get excited. A little like how you’re getting excited now."
        dawn "And during heat, it’d be so easy to just give in to those primal, biological urges for sex…"
        dawn "To just… close your eyes, lay your tail aside and… Mmhehe…"
        show dawn horny with dissolve
        dawn "I wanna feel that thick cock sliding inside of me…"
        mc "… You’re such a tease."
        show dawn satisfied with dissolve
        dawn "I know, my little duckling… At this point, I can’t contain myself…"
        hide dawn with dissolve
        "She suddenly crawls over me and drops her weight onto my thighs, her ass and tits jiggling alluringly."
        play music sex1 fadeout 3.0
        show dawnb sex
        show dawn sex1
        with dissolve
        "Backing her hips slightly, my throbbing cock is slotted between her ass cheeks."
        "Pushing my cock back somewhat with her rump, she positions our genitalia in such a way that she can grind them together."
        show dawn sex2 with dissolve
        "Her dripping wet labia dragging back and forth against my stiff member repeatedly, all whilst she looks deeply into my eyes."
        "She starts to press her slightly parted pussy lips against the tip of my cock, moaning more and more as she becomes increasingly aroused."
        dawn "This is it, kitten. Welcome to a new universe of pleasure…"
        play sound cum
        show dawn sex3 with cum
        "She pushes down, spreading her vulva around my shaft as she sinks further and further down. Biting her glossy lips as she reaches the hilt, a slight shiver encompassing her body."
        dawn "Aahhh...."
        "It’s tight, warm, and wet. Even motionless, her pussy squeezes and sucks around my member, eliciting pleasure from each and every nerve ending."
        "Through constant flirting and playing hard to get, the pure satisfaction of finally penetrating the alluring Dawn significantly adds to the pleasure. I’ll definitely have to hold myself back so I don’t cum prematurely like I did earlier with Aurora."
        "Cooing slightly, she adjusts to my girth, arching her back and rubbing her clit in the meantime; her nipples fully erect."
        show dawn sex4 with dissolve
        dawn "Mmmm… What a perfect fit, truly like a key in lock."
        play ambience sex fadein 3.0
        "She closes her eyes tightly for a moment as she begins to grind her hips up and down."
        "Dawn is taking this quite slowly, perhaps she’s not as experienced as one would assume. If she’s had sex with a stallion before, size shouldn’t be a problem for her, perhaps she’s only had sex with humans."
        show dawn sex3 with dissolve
        dawn "Ahh, oohhh, don’t you dare cum until I’ve had my own, mmhehe…"
        mc "That’s quite the challenge after your slew of seduction."
        dawn "Hehe, I’ll keep my fingers on my clit in that case."
        show dawn sex4 with dissolve
        "She accelerates to an average and pleasurable pace, her ample yellow ass practically hypnotising me as I drink in every detail."
        "The tightness of her pussy, the lips that grip against my shaft, and her cute butthole that I’d totally want to put a thumb in if this was doggystyle."
        if boutiquevisit2 == 1:
            "My lover’s pussy constantly squeezes and clenches around me, similar to how Ruby performs in bed, squeezing and milking in rhythmic motions as if she’s truly trying to make me blow my load."
        else:
            "My lover’s pussy constantly squeezes and clenches around me, squeezing and milking in rhythmic motions as if she’s truly trying to make me blow my load."
        "Dawn giggles almost knowingly of this fact, letting her orgasm first may be quite the challenge indeed. You can trust Dawn to make sex a flirtatious back and forth game."
        "Gritting my teeth slightly, I start to grind my own hips back and forth against her, bouncing her up and down, causing her ass and tits to bounce."
        "Taking initiative like this allows me to pace myself, while still pleasuring her deeply."
        show dawn sex3 with dissolve
        dawn "Oohhh, such an impatient man! Mmmhehe, oohhh, keep doing it like that, nice and deep! Ahh, yeahh!"
        "Perfect, she reacts with pure euphoria to each of my deep thrusts, while she constantly rubs her clit."
        "Bending my knees and tensing my thighs, I overwhelm any attempt she has to grind against me. Turning her into a willing participant of the act as I pound her pussy from below."
        show dawn sex4 with dissolve
        dawn "Ahh, ahh, ohh, ahhh! Y-You’re g-gonna-! Ahhhh!"
        "She squeaks and shivers, her back arches and my cock pushes against her g-spot. She can barely contain herself; her mind slowly eroding due to the pleasure."
        "Any attempt at speech failing as moans escape her mouth and her body is consumed in pleasure."
        dawn "Ahhh, ahhh, y-yes! Ahhh, c-com-ahhh, ahhhhh!"
        "Internal contractions around my cock signal her climax, allowing me to lower my guard to my own orgasm."
        "My cock reacts almost immediately as it thickens and throbs, my muscles growing tense with the building force of my orgasm as it surges through my body."
        play sound cum
        show dawn sex5 with cum
        play sound cum
        show dawn sex5 with cum
        "Dawn almost gives way as she feels the first torrent of cum unload inside of her, the warm thick cum filling her womb and vagina."
        play sound cum
        show dawn sex5 with cum
        play sound cum
        show dawn sex5 with cum
        "My lover pants, her tongue hanging lewdly from her mouth as I pump my final few loads of cum into her womb."
        stop music fadeout 5.0
        scene bg black with dissolve
        "At this point, she falls back onto me, no longer reverse cowgirl anymore. The rutting however, does not let up until our orgasms finally fade."
        stop ambience fadeout 3.0
        "For a while she continues to lay on top of me, recovering in post-orgasmic glow. I take advantage by cuddling her, and soon she turns around and reciprocates."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        scene bg dawnsroomnight with dissolve
        "I don’t remember when, but at some point, we must have fallen asleep."
        play ambience ambiencenight fadein 3.0
        "When I woke up, it was completely night time."
        "I probably woke up because it’s cold, one of the windows has been open this entire time. Dawn’s still happily snoozing though, her fur coat keeping her warm."
        "Deciding to move from the sofa to the bedroom, I lift her up and carry her there. She’s shockingly light, not to be rude, but I don’t struggle at all."
        "I don’t even think she stirs from her sleep as I tuck us both into her unfortunately small single bed."
        stop ambience fadeout 3.0
        scene bg black with dissolve
        "…"
        play ambience ambienceday fadein 3.0
        scene bg dawnsroom with dissolve
        show dawn satisfied with dissolve:
            xalign 0.5
            ypos 150
        dawn "Mmm… If you’re gonna make this a regular occurrence, I’ll need a bigger bed…"
        mc "Ah... What time is it?"
        show dawn happy with dissolve
        dawn "Uhhmm… 7:30am, and as much as I’d love to spend the rest of the day here by your side, I really need a shower."
        mc "No worries... *Yawn* I wonder what I’ll do today."
        show dawn horny with dissolve
        dawn "Ahh, you should have said that earlier, I could have made an innuendo about ‘doing’ me… She’s purring just at the thought of it."
        mc "I’m a little too sleepy for that."
        show dawn happy with dissolve
        dawn "And here I thought you were an unstoppable force of sex… What exactly are you planning to do in this new world anyway? You’re certainly in a peculiar position, kitten."
        dawn "I can’t imagine you’ll be spending your entire life wooing bachelorettes, well… I can..."
        mc "Hmm…"
        show dawn horny with dissolve
        dawn "Maybe you should hook up with one of the royal sisters so you’d be set for life, or perhaps you’re more of a harem ending guy, pfft, such a greedy man…"
        mc "Heyy, I didn’t say anything. I’m just trying to get a career, so I’m trying out a lot of jobs and meeting a lot of people to see what fits me the best."
        show dawn laughing with dissolve
        dawn "Ohh, I see… Well, unfortunately I don’t have anything for you here, however, leisure is important, kitten. Don’t forget to come to the nightclub, as long as I’m here you’ll never be alone at night, hehe…"
        mc "Thanks Dawn, and thank you for the trip yesterday, I really appreciated that."
        show dawn horny with dissolve
        dawn "I'll be seeing you, duckling."
        mc "Count on it, Dawn."
        hide dawn with dissolve
        scene bg black with dissolve
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        "After stretching a little, I return home."
        jump altmorning



        ## Day 3:
        ##


        ##
    label dawnvisit4:
        $ dawnvisit += 1
        show bg arcadiaalley with dissolve
        stop music fadeout 3.0
        "I arrive at the back of the nightclub, and knock on the door sensibly this time."
        "Bzzzt…"
        dawn "Hello, the girl that was in your wet dream last night speaking, who’s this?"
        mc "It’s me, [playername], and how did you know about my wet dream?"
        dawn "Oh darling, you were so great last night, mmhehe."
        "Bzzzt…"
        "The feed cuts and the door opens."
        scene bg dawnsroom with dissolve
        show dawn dresshappy with dissolve
        play music dawn fadein 3.0
        dawn "So wonderful of you to join me again, you’re certainly proving to become a reliable man. Which is why I’d like you to take advantage of me."
        menu:
            "Huh?":
                pass
            "Gladly":
                pass
            "Can you take advantage of me too?":
                dawn "You know me well, kitten!"
        show dawn dresshorny with dissolve
        dawn "I have three day coupons for the spa, this one’s for you!"
        mc "The spa? You mean the spa-brothel that has a big menu in the reception listing several sexual acts for a price?"
        show dawn dresssatisfied with dissolve
        dawn "Mmmmhhmmm, we’re going to have a spa day! It’s going to be great! But goodness, you’re such a pervert, it’s a spa and a brothel, not a spa-brothel."
        mc "Ah, so there are non-sexual functions too?"
        show dawn dressneutral with dissolve
        dawn "Oh my goodness, kitten. I hope you realized what you just admitted to."
        mc "… Shit, you got me."
        mc "Who’s the special third wheel?"
        show dawn dresshappy with dissolve
        dawn "I just found out a certain someone has recently acquired a pair of gorgeous wings…"
        dawn "Lily, a student of the Queen has officially begun her training, hmm?"
        dawn "As someone that was once in the exact same position as her, I’d like to take the opportunity to congratulate her, and perhaps give her some advice."
        dawn "She’ll certainly need it, I don’t know if that girl realizes how hard it’s about to get."
        dawn "Oh, and by the way… You’re the third wheel, the ‘wingman’ you could say."
        mc "Hm? Whatchu mean?"
        show dawn dresshorny with dissolve
        dawn "I need someone that’s good at lubrication, to help the conversation flow as smooth as butter…"
        mc "You’re planning on seducing her?!"
        show dawn dresssatisfied with dissolve

        dawn "Haven’t realized yet? I have a plan to seduce {i}everyone{/i} I meet."
        dawn "Welcome to the world of girl love, it's slippery when wet!"
        menu:
            "But I thought what we had was special!":
                show dawn dressneutral with dissolve
                dawn "Oh dearie, it is special!"
                dawn "Why do you think I'm inviting you with me? I couldn't be without you."
                dawn "Don't let my jokes get to your head too much."
                show dawn dresssatisfied with dissolve
            "Everyone? What's your body count?":
                show dawn dresshorny with dissolve
                dawn "In this world? Guess it's 'one', as of recently."
                mc "Ah, that's me!"
                show dawn dresssatisfied with dissolve
                dawn "Congrats, detective. You took my anthro virginity!"
            "I got that reference.":
                show dawn dresslaughing with dissolve
                dawn "Hehe, yeah. I'm only joking."
            "Oh yeah? Bold words coming from the the most clothed mare in the entire city.":
                show dawn dresssatisfied with dissolve
                dawn "Oohh, you got me dearie, mmhehe. What a shambling mess of contradictions I am today."
        dawn "Why do you think I have a single bed, darling? You’re the one that broke it in."
        mc "Really? I would have assumed otherwise by your demeanour."
        show dawn dresshappy with dissolve
        dawn "Mmmhehe, I think I understand where this misplaced train of thought is choo-choo-chooing from."
        dawn "You have no idea what wearing clothing in this culture symbolises, do you?"
        mc "It symbolises something? No, I wasn’t aware of that at all."
        show dawn dresslaughing with dissolve
        dawn "If an individual, particularly a mare, wears clothing… It’s a very strong indicator that they have no interest in relationships, or sexual encounters."
        mc "Wait… Seriously?"
        scene bg buttershouse
        show butters dresslaughing
        with dissolve
        "That’s why… Butters always wore that dress, and even to this day."
        scene bg thirdwagon2
        show morrigan evilhappy
        with dissolve
        "Holy shit! This is why Morrigan-Moxie was so eager on making me adapt to my nudity, she wanted me to be as open and available to the mares as possible from the beginning."
        scene bg dawnsroom with dissolve
        show dawn dresshorny with dissolve
        dawn "Indeed… Hehe, I’d never had sex in this body before I met you, I wasn’t even planning on it."
        dawn "But you’re a remarkably charming and nostalgic gentleman for a lady such as myself, one that had lived around humans for half a decade."
        mc "I see… So, you’re not interested, but you’re not exactly against it."
        show dawn dresshappy with dissolve
        dawn "Naturally, I find wearing clothing useful as an inhabitant that wasn’t originally from this universe, especially since I run a nightclub, hehe."
        mc "I barely see anyone wear clothes though, not even mares or stallions in relationships, so it sounds like a pretty niche thing."
        show dawn dresslaughing with dissolve
        dawn "Yeah, you could say that. You may have noticed that the royalty wear dresses in public too, same reason."
        mc "Ahh… I’m glad you told me, there’re still so many subtle things ingrained in this world that I’d never assume."
        show dawn dresshorny with dissolve
        dawn "However, in this particular circumstance, your ignorance was bliss…"
        dawn "Now, let’s plan how we’re going to indulge Lily today…"
        mc "Plan?"
        scene bg black with dissolve
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        "…"
        "Holy shit... What a plan..."
        "One hour later, approximately 8:45am…"
        show bg dusklightbedroom with dissolve
        play ambience ambienceday fadein 3.0
        play music lily
        show lilyb w:
            xalign 0.5
            ypos 20
        show lily happy:
            xalign 0.5
            ypos 20
        with dissolve
        lily "Good morning [playername], it’s always nice to see you. I can’t thank you enough for what you’ve done for this city and country."
        mc "Hey, you’ve thanked me enough for all that, Lil. I think it’s time we all did something for you."
        show lily surprised with dissolve
        lily "Oh? For me? Aha, I mean… I barely…"
        mc "Nah, I don’t want you to undermine your accomplishments. All I want you to do for today, is to accept this all-day spa coupon."
        mc "You’re definitely due a day of relaxation, you’ve been working non-stop since we squashed the bug."
        show lily laughing with dissolve
        lily "That’s the nicest thing ever! My goodness, [playername]… I absolutely will, I mean, as long as you’ll be there, right?"
        "I suppose Dawn would say ‘hook, line and sinker’, however, I’m just looking forward to having a nice day out with Lily. She really needs this."
        mc "Of course, I’ve got my coupon right here! I hope you don’t mind, but a friend and I organised this just for you."
        show lilyb w:
            xalign 0.5
            linear 0.5 xalign 0.8
        show lily happy:
            xalign 0.5
            linear 0.5 xalign 0.8
        show dawn dresslaughing:
            xpos 250
            ypos 20
        with qd
        dawn "Mmhhmmm, nice to meet you Lily, you can call me Dawnie!"
        show lily surprised with dissolve
        lily "D-Dawn?! I haven’t seen you in a year!"
        "Huh? Dawn said she's never met Lily before, so what is Lily talking about?"
        "Well shit, that wasn't part of the plan. Lily must be referring to the 'other' Dawn..."
        show dawn dressneutral with dissolve
        dawn "Ahah, well, you know me... I've been... very busy!"
        dawn "Let me just blow your mind for a second time, I can tell you that I used to be a princess candidate. Figured you could use a little advice."
        show lily laughing with dissolve
        lily "Ohhh! I really like the idea of that, I’ll let Aurora know that I’ll be taking the day off."
        show dawn dresshappy with dissolve
        dawn "Sure thing, kitten. No rush, the coupon goes until 5:00pm."
        show lily happy with dissolve
        lily "Okie! I’ll be one second."
        hide lily

        hide lilyb
        with qd
        show dawn dresshappy:
            linear 0.5 xpos 500
        mc "Hey, your plan worked, she’s totally pumped."
        show dawn dresslaughing with dissolve
        dawn "For a girl like Lily, you need to subtly build up her confidence. If we had unloaded everything on her all at once, she would have been overwhelmed, shy and defensive."
        mc "You seem to know her pretty well, but I think you’re overthinking it."
        show dawn dressneutral with dissolve
        dawn "Ahh, I overthink all the time, darling. I know her from other universes. Truth be told, I was the one nervous to meet an old friend in a new form."
        mc "She seemed to recognize you. But this is your first time meeting, isn't it?"
        show dawn dressangry with dissolve
        dawn "Yeah, I noticed that too... Naturally I'm aware of my counterpart, but I've never met her."
        show dawn dresshappy with dissolve
        dawn "I wonder if she's as cool as I am, mmhehe."
        mc "You're setting an unreasonably high bar there."
        show dawn dresslaughing with dissolve
        dawn "Well, if anyone can meet that, it'd be me!"
        show dawn dresshappy with dissolve
        dawn "Anyway, where did kitten get off to? Is she writing an entire letter?"
        mc "You’re calling her kitten too? I thought that was my pet name."
        show dawn dresshorny with dissolve
        dawn "Mmmhehe, want me to upgrade yours to ‘tiger’ to distinguish yourself?"
        mc "Actually, nah. I like ‘kitten’, whenever you say it, you exude confidence and sexual prowess."
        show dawn dresssatisfied with dissolve
        dawn "Is that so… Do I often exude myself upon you in your thoughts? Hehe."
        show lilyb w:
            xpos 800
            ypos 20
        show lily happy:
            xpos 800
            ypos 20
        with dissolve
        lily "Hello, thanks for waiting, let’s go!"
        show dawn dresshappy with dissolve
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        dawn "Let's go indeed!"
        scene bg black with dissolve
        "…"
        play music dawn fadein 3.0
        show bg sparoom with dissolve
        "When we arrive at the spa, the three of us get a small sauna and jacuzzi to ourselves."
        "The girls fully disrobe, even letting their hair down as Dawn removes her ponytail and Lily her ribbon."
        "About an hour in, we find ourselves chilling out in the sauna together."
        show dawnlily sauna1 with qd:
            xalign 0.5
            yalign 0
        dawn "Aaaaahhhhhh…."
        mc "Little cramped in here, isn't it?"
        show dawnlily sauna3 with dissolve
        dawn "Why don't you come sit on my lap? Hehe, or the other way round!"
        mc "I'll be alright for now, Dawn."
        dawn "Your loss, dearie!"
        show dawnlily sauna1 with dissolve
        dawn "This sauna is simply the best… Mmm…"
        lily "Ooohh, it really is..."
        lily "By the way, Dawn, I saw your new dress. It's a very beautiful, but it seems like a shame to hide such a nice body."
        show dawnlily sauna2 with dissolve
        dawn "Well darling, with the dress gone, you know what that means… hahah."
        lily "Ohh, Dawn… Hehe…"
        "I wonder if Lily’s unbound libido extends to women too. I guess we won’t have to wait long to find out, especially if I’m around to act as a catalyst."
        show dawnlily sauna1 with dissolve
        mc "How’re you finding the new lessons, Lily? You must have been practicing for this even before the incident with Morrigan, right?"
        lily "Ah, well… The curriculum got pushed around a little."
        lily "I was supposed to earn the right to be an alicorn by proving myself, but I was neglecting the social aspect."
        dawn "Mm… Kitten, you have no idea how important that is in the role of royalty."
        dawn "All your talent is meaningless if you can’t communicate and socialize effectively. All your knowledge would go to waste."
        lily "Yeah, I was pretty naïve back then. Defeating Morrigan proved beyond a doubt to Aurora that I could be the next to govern Arcadia, however, she’s very aware of my weaknesses."
        dawn "I bet she’s grinding you hard on fixing that."
        lily "She really is! I wasn’t expecting it, but she’s really pulling all the stops. She’s forcing me to make conversation with strangers as part of the training, and it’s so nerve-wracking."
        mc "She definitely has to take it a lot more seriously after the incident, I got the feeling she was a little content previously."
        dawn "Yeah, but Aurora can be a total hard-ass if she wants to be. Ain’t that right Lily?"
        lily "Hehe, you got that right… Oh, b-but we shouldn’t say that! She could overhear us!"
        show dawnlily sauna3 with dissolve
        dawn "Ahaha, she’s such a voyeur. I wonder if she’s watched any of us make love?"
        "… I shouldn’t say anything."
        "Wait, why is Dawn staring at me?"
        lily "I don’t think Aurora would do that. She’s too busy with her duties, why would she act like a horny teen?"
        dawn "*Giggle* You’re right, kitten. I must be projecting about wanting to watch you and [playername] make love."
        show dawnlily sauna2 with dissolve
        lily "O-Oh! Ahh, I-I mean…"
        "Ahh, sheesh… You can read Lily like a book, if I don’t interject it’d be pretty obvious to Dawn that we have quite the sexual history."
        menu:
            "What’s wrong Lily? Maybe Dawn can give you advice on your sex life.":
                "Wow, I just said that out loud. Dawn is a bad influence."
                lily "E-Eep! D-Do you think I need advice?"
                dawn "Oohh? What an unusual development…"

            "Don’t tease Lily too much, we’re here to relax.":
                dawn "Awh, my apologies, Lil. But you know, sex can be really relaxing too."
                lily "Ohh? Yeah, I suppose it can…"
                "Sex, huh? I wasn't expecting  her to be this forward about it."
                "Sex is allowed in these private rooms, but would Lily be okay with that?"

            "I don’t know where you got that idea from Dawn, Lily’s too innocent for that.":
                dawn "Oh, really? I figured she may be a virgin. I guess I have a lot to teach her after all, mmhehe."
                lily "H-Hey, now it feels like you’re both ganging up on me."
                "That wasn’t really my intention, but I guess I was a little patronising."
        show dawnlily sauna2:
            linear 4.0 yalign 0.8
        dawn "You have such a gorgeous body, Lil… Your ass looks like an especially delectable treat. Mmm…"
        lily "Hah… Uhm, t-thank you… I am quite proud of my butt."
        dawn "Absolutely darling, what do you think, [playername]?"
        mc "I- uhm…"
        lily "It’s okay, you can be honest…"
        "Ah… She adjusted herself so I can clearly see her pussy…"
        "She’s really wet. Well, of course she’s wet… It’s Lily, self-proclaimed as my slut and cum-dumpster."
        mc "Yeah, it’s a really nice ass."
        "Woah, Dawn just spread her legs…"
        "She’s not leaving much to the imagination by sitting like that… And… she’s really wet too."
        "Lily notices too, I can tell she's into it by the way she bites her lip…"
        show dawnlily sauna3:
            linear 4.0 yalign 0
        dawn "Pheeww, it’s getting so hot in here… And not just the temperature…"
        lily "That’s such a naughty pose, Dawn. You’re going to give [playername] an erection."
        dawn "Wouldn’t that be fun, hehe. Are you getting a ladyboner too, Lil?"
        show dawnlily sauna2 with dissolve
        "Dawn runs her hand up and down Lily’s thigh, she shivers and her tail instinctively flickers back and forth."
        "Woah, these two are getting along like wildfire."
        show dawnlily sauna1 with dissolve
        lily "Ooo… D-Dawn… I can tell you look really aroused…"
        dawn "Oh? You’re looking, kitten? If you purr for me, perhaps I’ll let you do more than just look…"
        show dawnlily sauna2 with dissolve
        lily "Aahh, D-Dawn… T-Touch me…"
        "A very sexually dominant girl, and a very sexually submissive girl. It makes sense."
        "But I didn’t think they’d get along this fucking well!"
        label dawnv4threesome:
            pass
        show dawnlily sauna2:
            linear 4.0 yalign 0.8
        "Dawn’s hand slips between Lily’s thighs to specifically target her clit. Sheesh, she didn’t waste any time teasing her at all!"
        lily "Ahhh, ahh, y-yes… Ooohh…"
        stop music fadeout 3.0
        dawn "And you were accusing me of being aroused? Look how soaking wet you are. I bet you got like this imagining [playername] fucking you, you’re such a slut."
        lily "Y-Yeah! I-I’m s-such a slut… Ahhh, that feels so good."
        "Holy crap, I got an erection so fast. My tip’s even dripping with precum and it’s only been a few seconds."
        dawn "Turn around, slut. I wanna get a taste of that juicy pussy."
        scene bg black with dissolve
        "…"
        play music sex1 fadein 3.0
        play ambience blowjob fadein 3.0
        show dawnlily facesitting1 with dissolve:
            xalign 0.5
            yalign 0
        dawn "Mmmm, mmphh, you’re so fucking delicious, kitten. Keep purring for me…"
        lily "Ahhh, ahhhh, o-ohmigosh! Ahhhh!"
        show dawnlily facesitting1:
            linear 4.0 yalign 1.0
        "Damn, Dawn got such a good reading on what type of lover Lily is in bed."
        "It’s brave to dirty talk this intensely when it’s your first time with someone, but Dawn has Lily completely figured out."
        "I can’t help but masturbate as I watch the two mares get it on. Dawn’s tongue flickering across Lily’s clit and driving her wild."
        show dawnlily facesitting1:
            linear 4.0 yalign 0.5
        lily "I-I’m… Y-You’re gonna make me come, ahhh! Ahhh!"
        dawn "*Lick, slurp, lick* Already? Sheeeshhh! *Lick, lick*"
        lily "Ahh-ahh! Yes, yes! Yes, yes, yesss! Ahhh!"
        show dawnlily facesitting1:
            linear 4.0 yalign 0.8
        "Lily’s entire body convulses as she’s consumed in orgasmic pleasure, her hips rocking into Dawn’s mouth as she grinds against it."
        "She came already? Dawn must be really skilled with her tongue."
        "I can vouch for that, she made me cum really fast the last time she gave me a blowjob."
        stop ambience fadeout 3.0
        lily "Ahhh, Daaaawwwnn…"
        dawn "Mmm, mmmmm… Hehehe…"
        scene bg sauna with dissolve
        "The two girls briefly separate, and as Dawn wipes the wetness from her muzzle she's already planning her next move."
        show dawn horny with dissolve
        dawn "For the next part of our performance, we’ll need a volunteer from the audience."
        dawn "Come sit right here Lil, yeah, that’s right…"
        hide dawn with dissolve
        "Almost beguiled, Lily follows each and every order as the two girls sit back on the benches."
        dawn "Come here, [playername]..."
        show dawnlilyb vaginal
        show dawnlily vaginal1
        with dissolve
        dawn "Hehe, I didn’t even need to ask her to spread her legs."
        lily "Y-Yeah, I want you, [playername]… I really want you right now."
        "I teasingly press the tip against her pussy, but I don't push in."
        mc "I didn’t quite hear that, try again?"
        lily "I-I really want you to fuck me, [playername]! I-I’m your cum-dumpster! Ahh… M-My pussy is all twitchy!"
        dawn "Ooohh, hehe, you two really do have a deeper relationship than I expected… I’m expecting great things, [playername]."
        "My eyes lock onto Lily’s glistening pussy, moist from the steaming air, Dawn’s saliva, and her own plentiful lubricant."
        "Dawn runs a slender finger around the labia, squishing and manipulating the pussy in obscene ways, as to beckon me to plunge inside."
        play sound cum
        show dawnlily vaginal2 with dissolve
        "The horny mare moans loudly as I push forward, sliding my cock deep into her warmth and wetness."
        lily "Ahhhaaaa, oohhh, yes! I’ve already come, b-but this feels even better than usual, ahh…"
        dawn "Well darling, I plan to make a three-course meal out of you. Each dish will get more and more delicious…"
        play ambience sex fadein 3.0
        "Her greedy pussy squeezes and generously coats my shaft in her juices, allowing my girthy cock to easily slip backwards and start a rhythm of fucking."
        "Lily pants and moans with happiness and lust as I pound her needy cunt, Dawn adding to the pleasure with tactful movements on her erogenous zones."
        show dawnlily vaginal1 with dissolve
        lily "Ahhh, y-you two… Y-You’re going to drive me w-wild, ahahhaa… I-It’s not even breeding season, b-but… It’s so good… Ahhh!"
        dawn "There we go, let all that sexual frustration out… We can’t have a princess who acts like a complete slut, can we? Or maybe you’d like to train to be a princess of love instead, hmm?"
        "For some reason, this line of dirty talking arouses Lily even more, her pussy clenching as I plunge deeper yet."
        "She watches with pure admiration and delight as my cock slides deep inside of her, she twitches slightly as she even manages to squirt a little, splattering our point of connection."
        show dawnlily vaginal2 with dissolve
        lily "I-I’m gonna… Ahh, y-you’re gonna make me… Ahhh!"
        "With an expression of determination, Dawn starts to rub her clit faster, as if she was holding back to overwhelm Lil at the right moment."
        dawn "Yess, yess… What an obedient little slut, come for me now… Come for me…"
        "Smirking, I furiously push forward, rutting with increased speed and intensity. Lily’s entire body rocks, even her petite breasts jiggling, as she begins to orgasm."
        show dawnlily vaginal3 with dissolve
        lily "Aaahaaaa, I-I’m coming! M-Master and mistress, c-coming!"
        "Lily’s body begins to convulse as she has another strong orgasm, her pussy clenching and sucking around my throbbing cock as my own orgasm prepares to set itself loose."
        play sound cum
        show dawnlily vaginal4 with cum
        play sound cum
        show dawnlily vaginal4 with cum
        "Pushing deep and bottoming out into Lily’s pussy, my cock unloads straight into her womb. But I continue fucking, and splatter her entire pussy with several loads of cum."
        play sound cum
        show dawnlily vaginal4 with cum
        play sound cum
        show dawnlily vaginal4 with cum
        stop ambience fadeout 3.0
        "Her pussy milks and squeezes me until I finally finish ejaculating, and finally pull out."
        show dawnlily vaginal5 with dissolve
        lily "Haahh, aaahhh… So good, b-best day ever…"
        scene bg sauna with dissolve
        show dawn satisfied with dissolve:
            xpos 275
            ypos 20
        dawn "Now, now… This is an ‘all-day’ spa coupon, we can’t call it quits quite yet…"
        dawn "After all, I still have so much to teach you, future princess…"
        show dawn horny with moxiespell
        "Casting a spell on me, Dawn removes the post-orgasm sensitivity from my cock, and I’m suddenly ready to go again."
        "Which is great, I definitely want to go again."
        dawn "Let’s see here… You got really wet, so maybe…"
        hide dawn with dissolve
        lily "*Gulp* What are you doing, Dawn? Aa-ahh?"
        scene lily csex5 with dissolve
        "Dawn’s fingers stray slightly under Lily’s vulva, finding her tight anus and poking it with a finger."
        "Thanks to the copious wetness dripping down from the previous rutting, the pucker is practically as well lubricated as her pussy, causing Dawn’s finger to slip in with ease."
        lily "Oh! Th-That feels… different…"
        lily "A-Are you sure?"
        dawn "Be a good girl now… Close your eyes, and relax…"
        scene lily csex5 with dissolve
        lily "Y-Yeah, anything for you…"
        mc "You really have her wrapped around your finger."
        dawn "Mmmhehe, and you don’t? She’s seems to be your little slut before mine…"
        dawn "Here, she should be ready."
        scene lily csex5 with dissolve
        lily "Eee?! Really? We're doing that?"
        show dawnlilyb anal
        show dawnlily anal1
        with dissolve
        "Attacking from the side, Dawn pushes Lily into a pseudo-sixty-nine position and begins to teasingly lap at her swollen clit."
        "Despite vocalising her uncertainty, Lily’s legs open wide and her ass is completely ready and available."
        dawn "Well… Let’s not keep the slutty princess waiting, hmm?"
        "With one hand, Dawn spreads Lily’s cheeks slightly and I find myself getting straight into the same position as before."
        "I align the tip of my erection, still slick from the vaginal sex, and press it against Lily’s tightly puckered backdoor."
        play sound cum
        show dawnlily anal2 with dissolve
        "She gasps at the pressure on her tender ass. As she makes an effort to relax, my cock soon sinks deeply into her slippery, warm depths, all while Dawn watches with glee."
        lily "Ooohhh, it feels so different… I like it, I like it a lot… Hehe… Now I can really be a cum dumpster, cum in all my holes… Hehe…"
        dawn "Sheesh… You really have been a bad influence on her, [playername]."
        mc "Hey, she was always like this! I just helped her be more confident about it."
        play ambience sex fadein 3.0
        dawn "Mmm, just ask me if you need some drool, hehe… *Lick, drip, lick*"
        "After giving Lily a few seconds to adjust to the girth, I plunge further forward until I’m hilted, then I pull back about three quarters of the way and pump back in."
        show dawnlily anal3 with dissolve
        "And again, and again. Each thrust becomes easier, and more apparently pleasurable for Lily who is moaning more and more."
        "Mare’s pussies are extremely wet, so the anus is a welcome area of friction. Especially the sphincter itself which acts like a tight iron ring, which glides back and forth along my shaft."
        "It feels especially pleasurable if I let it roll across my sensitive glans, I can feel her twitching and throbbing."
        lily "Oohhh, ahhh, it feels even bigger! Ahaa, seems like I love your cock anywhere, [playername]!"
        "Dawn’s tongue continues to flicker against Lily’s clit, eliciting light orgasms and squirts from her, serving to glaze my cock in even more lubricant."
        "With Lily’s anus fully adjusted to the girth of my cock, I thrust at a stimulating pace, making her cute tits jiggle back and forth, and taking care not to let Dawn's horn poke me."
        lily "Oohh fuck, I-I’ve never felt anything this good! Ahh, aahhh!"
        dawn "Good girl, just lose yourself to the pleasure, the ecstasy."
        "The combination of the anal sex and focused cunnilingus overwhelmed the purple mare, and send her into a series of powerful orgasms."
        "Her pussy begins to contract and her thighs quiver, her moans growing so loud that they may even escape the sound proof sauna."
        "After another twenty seconds of pounding her ass, the fatigue from the heat and constant sweating in the sauna slowly takes over. Fortunately, before exhaustion becomes a concern, my own climax manages to arrive."
        play sound cum
        show dawnlily anal4 with cum
        play sound cum
        show dawnlily anal4 with cum
        "Slamming deeply into her with fervour, my entire shaft is alight with pleasure as it begins to unload several thick ropes of cum into her ass."
        play sound cum
        show dawnlily anal4 with cum
        play sound cum
        show dawnlily anal4 with cum
        "Her silken insides drawing as much cum as possible as it squeezes and sucks."
        stop ambience fadeout 3.0
        stop music fadeout 3.0
        scene bg sauna with dissolve
        "As if released from shackles, a sense of exhaustion consumes my body as I pull out and sit down on the bench."
        mc "Looks like the heat’s getting to me, girls. There are better places to have sex than the sauna."
        "Dawn keeps her tongue locked onto Lily’s clit until she’s completely sure their orgasm is over."
        "Before Lily can even start catching her breath, Dawn surprises her with a messy kiss."
        show dawn satisfied with dissolve:
            xpos 275
            ypos 20
        dawn "Mmfwaahhh, dessert was deliiicious!"
        show lilyb w:
            xpos 725
            ypos 20
        show lily horny:
            xpos 725
            ypos 20
        with dissolve
        lily "Uuuu, that was so hot…"
        "The two girls sigh blissfully."
        "The three of us agree it’d probably be best if we went and washed up again."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        scene bg black with dissolve
        "Other than that, we spent a lot of time in the jacuzzi, and had some non-happy ending massages."
        "A few hours later…"
        play music dawn fadein 3.0
        scene bg dusklightbedroom with dissolve
        show dawnlily facesitting2 with dissolve:
            xalign 0.5
            yalign 0.5
        play ambience blowjob fadein 3.0
        dawn "Mmphh, mmm, such a slutty princess, hah, aahh… *Lick*"
        lily "F-Fuck, aahh, haaah, k-keep going!"
        "Yeah, these two have been flirting back and forth all day. They didn’t even make it to the bed."
        "Come to think of it, there was barely any advice given to Lily about becoming a princess."
        "The spa day was awesome though, we had sex in the morning, and it'd only be natural that the girls are horny again so many hours later."
        "Given that it's just past 5:00pm, the question is, should I stay or should I go?"
        menu:
            "Stay here with them for the night":
                $ dawnltr = 3
                "Ah, fuck it, why not?"
                mc "Hey, spread those cheeks, Lily could definitely use a good fuckin’ too."
                dawn "Mmmphh, great idea, darlingsh! *Lick*"
                lily "Ahhaa, [playername]… Aahh, I want to feel you in my pussy again, ahh…"
                mc "Lay down for me… There we go."
                scene dawnlily vaginal6 with dissolve
                stop ambience fadeout 3.0
                lily "Ahhh, ohhh… I-I’m such a slut, aren’t I? Ahh, h-how could I ever be a princess with such a filthy mind?"
                dawn "It’s obvious to me that you’re utterly obsessed with our friend’s cock."
                lily "Uuu… M-Maybe… I-It just feels so good!"
                dawn "There, there… Let it all out of your system…"
                play sound cum
                scene dawnlily vaginal7 with cum
                "The two of us fuck, and fuck, and fuck."
                "We really did let it all out of our system. I might not want to have sex for a few days after this."
                "Ahh, who am I kidding? Who’s next?"
                mc "Hey Dawn, cast the spell and bend over for me."
                dawn "Oohoh, growl for me, tiger..."
                stop music fadeout 3.0
                scene bg black with dissolve
                "…"
                "In the morning…"
                play ambience ambienceday fadein 3.0
                scene bg dusklightbedroom with dissolve
                show lilyb w:
                    xpos 250 ypos 20
                show lily happy:
                    xpos 250
                    ypos 20
                with dissolve
                lily "I guess we’re all fuckbuddies now… I never thought my sex life would blossom like this!"
                show dawn dresshappy with dissolve:
                    xpos 750
                    ypos 20
                dawn "Isn’t it magical, Lil? Being fuckbuddies, I mean."
                dawn "A normal friendship, with all the benefits of sex, lust and pleasure. I wonder why it isn’t more normalised."
                mc "Yeah, yeah, I get the point. Friendship with Benefits."
                show lily neutral with dissolve
                lily "Goodness… Before I met you, I was a virgin… But look at me now!"
                show dawn dresshorny with dissolve
                dawn "Woo! Quite the bad influence, aren’t you, [playername]?"
                show lily surprised with dissolve
                lily "Noooo, he’s been a great influence! I’ve learnt so many things, got to have so many experiences and I even took some big steps to combat my shyness."
                show dawn dresssatisfied with dissolve
                dawn "Hehe, we all love [playername]."
                show lily laughing with dissolve
                lily "Yeah! Thank you [playername], you’ve done so much for me, and Arcadia!"
                mc "Awh, I should be thanking you two for making my time here in Arcadia so great."
                show dawn dresshappy with dissolve
                dawn "More great times await you, all you need to do is come and see me in the evening."
                show lily horny with dissolve
                lily "D-Does that apply to me?"
                show dawn dresshorny with dissolve
                dawn "Mmm, yeah! Yes, it does, I don’t think I’m finished with either of you… *Giggle*"
                "I’m still somewhat in disbelief at the events of yesterday, I wasn’t expecting these two to start having sex right in front of me."
                scene bg black with dissolve
                if crystalballdayactivated == 1:
                    $ crystalballdayactivated = 0
                    jump cbmenu

                "Anyway, the three of us go our separate ways, and I return home."
                "If I want to spend some time with Dawn again, I’ll just need to visit her at the nightclub during the evening."
                jump altmorning
            "Leave them to it":
                $ dawnltr = 3
                stop ambience fadeout 10.0
                mc "Have fun you two, I’m going to head home."
                dawn "Mmphh *Lick* Goodbaii, darlingsh!"
                lily "Ahaahh, y-yeah! Uh-humm, c-cum back soon!"
                dawn "Hehe, we both love you, [playername]. *Lick, lick*"
                lily "Yeaahhhhh! Thank you [playername], you’ve done so much for me, and Arcadia!"
                mc "Awh, I should be thanking you two for making my time here in Arcadia so great."
                dawn "More great times await you, all you need to do is come and see me in the evening."
                lily "D-Does that apply to me? Ahh, ahh..."
                dawn "Mmm, yeah! Yes, it does, now shut up, slut!"
                lily "Ahh, sorry mistress!"
                scene bg black with dissolve
                if crystalballdayactivated == 1:
                    $ crystalballdayactivated = 0
                    jump cbmenu

                "If I want to spend some time with Dawn again, I’ll just need to visit her at the nightclub during the evening."
                "…"
                jump evening
    label dawnvisit5:
        show dawn2 happy with dissolve
        dawn2 "I live in one of the cute cottages near the city wall. Thank you so much for helping me. I'm not quite as strong as a handsome man such as yourself."
        "She's definitely 'Dawn', albeit a slightly tamer version. Like a PG-13 Dawn, which is ironic considering this one's butt naked."
        "I wonder how the two have avoided each other for so long. Although it's not exactly like I know what 'dress Dawn' gets up to."
        "Maybe they simply haven't avoided each other, and they're good friends. But it's not like I can mention that at the risk of revealing something that's supposed to be classified."
        scene bg arcadiasuburbs with dissolve
        show dawn2 laughing with dissolve
        dawn2 "So, tell me about yourself, [playername]! What settlement or country do you hail from?"
        "This charade again. I'm pretty used to this by now though."
        mc "I'm from a pretty faraway land, not many have heard of it, it's called uhh, Humania... Definitely a different country, but I couldn't say which, it's private."
        show dawn2 neutral with dissolve
        dawn2 "Oh? That's rather mysterious, if the information is 'classified', you don't need to tell me."
        dawn2 "I'm aware that as a friend of Lily, you might be privy to all sorts of juicy info that you can't indulge."
        mc "Ahh, I'm glad you understand. What about yourself, Dawn? I've heard good things from your friends."
        show dawn2 happy with dissolve
        dawn2 "Have you really? I'm surprised they speak of me much at all."
        dawn2 "Well, given that I used to be in Lily's position, the topic may have come up once or twice."
        mc "You used to be a princess candidate too?"
        show dawn2 neutral with dissolve
        dawn2 "I certainly did, but I decided that wasn't for me. It's a little like a three thousand year prison sentence, hehe. I love my freedom."
        "This all sounds familiar, but what's the catch?"
        mc "What do you do now?"
        show dawn2 angry with dissolve
        dawn2 "Well, Aurora offered me several other jobs. I'm not even sure if I can tell you, but I had to decline because a lot of them were very commital."
        dawn2 "I had a boyfriend at the time, so I couldn't just leave!"
        "Ah-ha! There it is. This Dawn had a partner that she didn't want to give up, and that's why she didn't become an interuniversal scholar."
        "What a subtle change... I wonder what aspect of being anthropomorphic over four-legged pushed that difference."
        "Should I even ask?"
        show dawn2 neutral with dissolve
        dawn2 "Mm... Well, I'm single now, that's all in the past. I'm just a teacher at the college."
        mc "That's a good position for someone like yourself, you seem quite passionate about learning."
        show dawn2 happy with dissolve
        dawn2 "Indeed I am... You're certainly good at reading people."
        mc "You were a princess candidate, so you're clearly a remarkable person."
        show dawn2 horny with dissolve
        dawn2 "Heh, you flatter me. Perhaps such flattery is best left indoors, specifically... here's my house."
        "That line almost sounded like something the other Dawn would say, hehe."
        "Dawn leads me to exactly what she had specified earlier, a cute cottage in the shade of the city wall."
        "As we step inside, it looks a lot more decorated and lived in than any of the other Dawn's settlements."
        scene bg dawnhouse with dissolve
        mc "Where do you want these groceries?"
        show dawn2 happy with dissolve
        dawn2 "Just through to the kitchen here, by the time I put them away the kettle should be done boiling."
        scene bg dawnkitchen with dissolve
        "I step through into the kitchen and stand by while Dawn puts away some groceries."
        "In the short time I've come to know this new Dawn, I feel like I've gained a remarkable insight into her life already."
        "However, I'm wondering if she actually invited me here for... well, sex."
        "It seems too obvious, too easy for Dawn. Especially considering the other Dawn took things slow with me."
        "I just can't imagine a less flirtatious version deciding to sleep with me on a whim. Although I imagine I could flirt with her to get to such a position."
        menu:
            "Tea takes a long time to cool, think you can wait that long?":
                show dawn2 horny with dissolve
                dawn2 "Oh my, what are you implying?"
                dawn2 "Are you the type to get fiesty as soon as we're away prying eyes? I know I am..."
                mc "Tell me more about yourself, I'm listening."
                show dawn2 satisfied with dissolve
                dawn2 "Well dearie, flirting while I put bread away isn't the most seductive action, so allow me to finish up here."
            "I'll make the tea, don't worry about it.":
                show dawn2 happy with dissolve
                dawn2 "Okies dearie."
                dawn2 "Two sugars for me, and maybe a little milk depending on how strong you like it."
                mc "Milk? Was that a joke?"
                show dawn2 horny with dissolve
                dawn2 "You're the one making the tea, dearie, how about you decide?"
                "Phew... I don't think I could handle having sex under the aphrodisiac milk again, it can't be good for my heart."
                hide dawn2 with dissolve
                "It seems that she doesn't actually own any milk, but the implications stand..."
        hide dawn2 with dissolve
        stop music fadeout 13.0
        stop ambience fadeout 3.0
        "Dawn finishes putting away the groceries and we take a cup of tea each back into the main room."
        scene bg dawnhouse with dissolve
        "Ah, this Dawn owns a much bigger sofa, so we can both comfortable sit without being squashed into body contact, although that certainly has its benefits too."
        show dawn2 satisfied with dissolve:
            xalign 0.5
            ypos 200
        dawn2 "Aahhh, this tea is so delicious."
        mc "Mm, it's a little too hot for me to drink it yet."
        show dawn2 happy with dissolve
        dawn2 "So, you knew me, huh?"
        mc "Yeah, I've heard snippets from the time I've spent with Lily."
        show dawn2 neutral with dissolve
        dawn2 "And is that the truth?"
        menu:
            "Yeah, you weren't mentioned much.":
                pass
            "Why would I lie?":
                pass
        dawn2 "And you just so happened to recognize me enough to call out to me from 'snippets' you'd heard about me from Lily?"
        menu:
            "Yeah, I-":
                pass
            "Of cou-":
                pass
            "No, it-":
                pass
        show dawn2 angry with dissolve
        play music eyesofthewind
        dawn2 "Who the hell are you? How do you really know about me?"
        menu:
            "What's with the suspicion? I'm just a dude that knows stuff.":
                pass
            "I'm a nobody, really. I've only been living here for [days] days.":
                pass
            "It's the truth! I'm close with Aurora, Lily and others!":
                pass
        show dawn2 neutral with dissolve
        dawn2 "Hmph... I singled you out because you seem rather trustworthy, with your connections and all..."
        dawn2 "I think my assumption is right, I'm glad I've still got some intuition with these things."
        mc "Uhh, care to explain what you're talking about, then?"
        show dawn2 angry with dissolve
        dawn2 "This is a little creepy, it makes my skin shiver, especially considering the recent 'Morphling' incident..."
        dawn2 "But, there have been... 'Sightings' of me, sightings that I don't recall."
        dawn2 "And to top that off, strange rumours about myself being at a nightclub that I've never visited before."
        dawn2 "You're one of many unusual occurrences in my life recently, just what the heck is happening?"
        menu:
            "Do you think there's a Morphling disguising themselves as you?":
                show dawn2 neutral with dissolve
                dawn2 "Eugh, what a creepy possibility… I’d be a perfect disguise target too."
                dawn2 "I’m relevant enough to get places, as an ex-princess candidate and tutor, but not enough to raise suspicion."
                "That’s a pretty similar criteria for Moxie, heh."
            "Sounds like you're being paranoid.":
                show dawn2 neutral with dissolve
                dawn2 "Paranoid? Paranoia is characterised by delusions… I have had people literally come up to me, and said they had conversations with me that never happened!"
            "That is weird, what do you think is going on?":
                show dawn2 neutral with dissolve
                dawn2 "I have no idea…"
        show dawn2 angry with dissolve
        dawn2 "You seemed pretty confident that you knew me at the market. The moment I didn’t recognize you, your face dropped and you stuttered your words."
        dawn2 "So pardon my accusatory tone, but I believe you’re directly roped into these strange circumstances."
        dawn2 "And furthermore, your body language indicated that you had something to hide."
        "Awh shit!"
        "This girl is far more intelligent than I am, she’ll run circles around me at this rate."
        mc "I-uhh…"
        mc "I don’t know what to say."
        show dawn2 neutral with dissolve
        dawn2 "Hmm…"
        stop music fadeout 15.0
        dawn2 "It seems like I won’t be getting anything out of you, will I?"
        mc "It would seem that way."
        show dawn2 angry with dissolve
        play ambience ambienceday fadein 10.0
        dawn2 "Very well… I hope I haven’t soured the mood. I haven’t had a guest in a long time, least not one as impressive as a hero like yourself."
        show dawn2 happy with dissolve
        dawn2 "I wasn’t lying earlier, I’m actually rather enamoured at the idea of sharing a drink of tea with the man that helped defeat Morrigan."
        dawn2 "Little known fact, but I was Aurora’s student at a time where tensions between the Morrigan and Arcadia were quite high."
        dawn2 "Some time after I left, the ‘Elements’ initiative began with Lily taking the helm as she took over my position as princess candidate."
        show dawn2 laughing with dissolve
        dawn2 "And when a morphling army attempted to take over Arcadia, they were given a thrashing! It was spectacular!"
        show dawn2 neutral with dissolve
        dawn2 "Ah-, you probably already know this though, don’t you?"
        mc "I’m vaguely aware, although the most recent events were very different. Rather than use a frontal assault, Morrigan had planted a spy and used a disguise to infiltrate the system."
        "Just going to leave out the part where I brainwashed everyone and then cured them via sex…"
        show dawn2 angry with dissolve
        dawn2 "Ohh! *Shudder* She’s defeated, yes?"
        mc "Yeah, completely eradicated. You don’t need to worry about Morrigan disguising themselves as you."
        show dawn2 happy with dissolve
        dawn2 "Thank goodness… I had briefly thought that may be the case."
        mc "Morrigan had chosen Moxie’s body, not only as a disguise but as a vessel. Moxie is currently fine."
        show dawn2 laughing with dissolve
        dawn2 "More than fine I’d say, she seems to be a princess candidate herself!"
        mc "Heh, yeah. I think she might be blood related to Princess Selene, but over many generations."
        show dawn2 happy with dissolve
        dawn2 "Well now, it seems anything you involve yourself in becomes incredibly successful."
        dawn2 "Be sure to spread some of that magic this way."
        mc "Well, I could, but the method I use to spread that ‘magic’ may surprise you."
        show dawn2 horny with dissolve
        dawn2 "Oh? Tell me more, kitten…"
        mc "Come sit on my lap, and I’ll tell you exactly what you want to hear, duckling."
        dawn2 "Oohh, mmhehe."
        "Using some of the seduction tricks I learnt from the other Dawn, combined with some rough knowledge of what the other Dawn likes in bed, I decide to try and seduce her..."
        label dawnv5ds:
            pass
        show dawn2 closehorny with dissolve:
            xalign 0.5
            yalign 1
        "She shimmies over and does indeed sit on my lap in a ladylike manner."
        show dawn2 closesatisfied with dissolve
        dawn2 "Oh my, do I feel something poking me already?"
        mc "You sure do, and I’m not even erect yet."
        show dawn2 closehorny with dissolve
        dawn2 "Psshh, you could at least pretend to be subtle, mmhehe…"
        mc "Subtlety was never my speciality, but I bet you’ll love my actual speciality…"
        show dawn2 closelaughing with dissolve
        dawn2 "Ohh, pray tell, dearie…"
        mc "Let’s just say that the girl always gets her's first. My equipment would put a stallion to shame…"
        show dawn2 closehappy with dissolve
        dawn2 "Is that so? Are you saying that from experience, or are you a cocky little boy?"
        mc "Wouldn’t you like to find out?"
        show dawn2 closesatisfied with dissolve
        dawn2 "You talk a lot of big game, but can you really keep up with a lady such as myself?"
        mc "Heh, I wouldn’t worry about that, Dawn. I know exactly where and how to handle a girl like you."
        show dawn2 closehappy with dissolve
        dawn2 "Ohh! Well… From what I can feel, you’re certainly starting to feel ‘big’ down there…"
        mc "You haven't felt anything yet."
        show dawn2 closehorny with dissolve
        dawn2 "Fiiine, fiiine… If you’re so amazing, a lady like myself couldn’t possibly turn down such a kind offer."
        dawn2 "Let’s see if you live up to the hype, hero…"
        mc "I’m warning you, no man will ever feel as good after this."
        show dawn2 closesatisfied with dissolve
        dawn2 "I dare you to make that happen, mmhehe…"
        scene bg dawnhouse2 with dissolve
        play music sex1 fadein 3.0
        show dawnb doggystyle
        show dawn doggystyle1
        with dissolve
        "She certainly made me work for it, but she finally gives in and presents herself on the sofa. Her gorgeous rear exposed, and all mine."
        dawn2 "A horny teacher, that’s one for the bucket list!"
        mc "And a man of a unique species, should be a treat for both of us."
        dawn2 "You’ve got that right…"
        dawn2 "I’m usually not this easy, but oh well… You seem to have made me all gooey."
        dawn2 "I suppose I’ll let you claim your reward."
        "Her wide rear sways freely, and her tail purposely moves out of the side to give the best view possible."
        "This invitation is all I need as I kneel into position behind her voluptuous ass."
        "At this point I’m fully erect, and my lover’s labia has become fully soaked in anticipation of our rutting."
        "Lust drips down her pussy as I grind my erect member against it, feeling around for her entrance with my tip."
        play sound cum
        show dawn doggystyle2 with dissolve
        "I bring my hands to her hips and push forward. Her wet folds yield as they delightfully purse around my shaft as I plunge deeper."
        play ambience sex fadein 3.0
        "Her pussy grips tightly, intently squeezing my member to such deliberation that she infectiously giggles. The grip may be tight, but the obscene amount of lubricant allows me to easily begin fucking."
        dawn2 "What a fat cock! You’re full of surprises, hehe."
        mc "Did you think it was small? Pfft."
        dawn2 "Not at all, dearie. I just didn’t think it’d be such a perfect fit, the lack of bumps and ridges is really nice."
        "Mares complimenting my cock will never get old. Sorry stallions, but I’m here to steal your girls."
        "Moans occasionally slip from Dawn’s mouth as she’s slowly consumed with pleasure, my deep sensual thrusts overwhelming her most sensitive spots with repeated friction."
        "This type of deep fucking elicits substantial pleasure from Dawn, her body genuinely quivers and spasms as sparks of euphoria shoot through her nerves."
        show dawn doggystyle3 with dissolve
        dawn2 "Ahh, haaahh… Y-Yeah, you lived up to the hype, ahh…"
        mc "It’s been sixty seconds, Dawn."
        dawn2 "Ohh yesssss, then keep going, keep going! Ahhh-haaahhh…"
        "Keep going I shall… I grab her ass with both hands as leverage and start to pump faster, her rump occasionally pushing back into me, desperate for more pleasure."
        "The intensity of our sex escalates to such a position where her entire body rocks back and forth on the sofa, her breasts shamelessly swaying back and forth, and her tail lashing around excitedly."
        "Her pussy grips my cock with increasing tightness as she nears her orgasm and as I increase the pace of my rutting as I ready to time my own with hers."
        show dawn doggystyle4 with dissolve
        dawn2 "Ahh, aaahhhaaa… I’m getting close! Right there, keep going just like that, ahh, aaahh, aaahhh!"
        "Lewd sounds constantly spill from her increasingly soaking wet folds, that combined with her increasingly verbose moans, and the light patting sound when my skin connects with her fur provide a sexual harmony to the ears."
        "After a few minutes at this frantic thrusting pace, I can soon feel the familiar pressure of an orgasm building up with me. Simultaneously, it seems my lover is approaching her limits too, as her thighs quiver and eyes roll back."
        dawn2 "Ohhohhhhh-fuuuuck! C-Coming! Ahh aaahhh!"
        "Powerfully, Dawn is consumed in what seems to be a full body orgasm. Her pussy starts to contract around my cock, intensifying the pleasure and accelerating my rising orgasm."
        play sound cum
        show dawn doggystyle5 with cum
        play sound cum
        show dawn doggystyle5 with cum
        "I thrust until I can’t hold it back anymore, and as a brief sensation of euphoria washes over me, the cum begins go gush out, filling Dawn as much as I’m able."
        play sound cum
        show dawn doggystyle5 with cum
        play sound cum
        show dawn doggystyle5 with cum
        dawn2 "Ahh, fill me up! Ahhh, yessshhh!"
        stop ambience fadeout 3.0
        stop music fadeout 3.0
        show dawn doggystyle6 with dissolve
        "Only once I’ve completely finished the last of my climax, I pull my member out, along with some cum which haplessly drips down her yellow thigh."
        "Released from a bind, Dawn flops down onto the sofa and lets out a satisfied sigh, followed by a giggle."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        hide dawn
        hide dawnb
        with dissolve
        show dawn2 satisfied with dissolve:
            xalign 0.5
            ypos 200
        dawn2 "Hehe… I knew you’d be a good partner in bed, ah heck, we didn’t even make it to the bed, that’s just how good of a partner you are."
        mc "You knew? I guess you did say you have good intuition."
        show dawn2 happy with dissolve
        dawn2 "Ahaha, true! I suppose even a little part of me invited you here with the intention of doing this."
        mc "I’ll be honest, the interview about sightings of some other ‘Dawn’ really surprised me."
        show dawn2 horny with dissolve
        dawn2 "Ahh, yeah… Sorry about that! I guess I tricked you by luring you in here with the implication of sex… But I guess I made good on that unspoken promise, right Kitten?"
        mc "Hey, I’m just glad we had a good time togeth-"
        show dawn2 neutral with dissolve
        play sound knock
        "*Knock knock… knockity knock knock."
        show dawn2 angry with dissolve
        dawn2 "Oh sheesh, the door at a time like this?"
        hide dawn2 with dissolve
        "Dawn plods upwards, she quickly grabs a tissue and tries to wipe as much cum away as she can."
        "Once cleaned up, she quickly moves to answer the door."
        scene bg black with dissolve
        "As the door is opened..."
        scene bg dawndoor with dissolve
        play music challenge
        show dawn dresshappy with dissolve:
            xpos 700
            ypos 20
        dressdawn "Hello, is this-"
        mc "Dawn?!"
        show dawn dressneutral with dissolve
        dressdawn "[playername]?!"
        show dawn2 neutral with dissolve:
            xpos 225
            ypos 20
        dawn2 "Me?!"
        dressdawn "Dawn!"
        mc "What are you doing here?"
        show dawn2 angry with dissolve
        dawn2 "Awh damnit, I knew there was something going on! And you’re in on it too, [playername]!"
        show dawn dressangry with dissolve
        dressdawn "Wait, wait! I can explain, in fact, I’m here to explain!"
        show dawn2 neutral with dissolve
        dawn2 "Hmph, fine… What you have to say better be good… ‘Me’."
        show dawn dresshappy with dissolve
        dressdawn "May I come in? There’s a lot that needs to be said."
        show dawn2 angry with dissolve
        dawn2 "Alright, if you must…"
        scene bg dawnhouse with dissolve
        show dawn dresslaughing with dissolve:
            xpos 225
            ypos 20
        dressdawn "It’s rather convenient that you’re here, [playername], you can vouch for my story."
        mc "I guess?!"
        show dawn2 angry with dissolve:
            xpos 700
            ypos 20
        dawn2 "[playername], I trusted you! But you were hiding something from me that entire time!"
        mc "Hey, why are you mad at me but not Dawn?"
        show dawn dresshappy with dissolve
        dressdawn "Mmmhehe, I couldn’t possibility stay mad at myself, kitten."
        mc "She's not mad at herself, it's you!"
        dressdawn "Regardless... I’m here to settle this, it wasn’t [playername]’s place to reveal this classified information. Please redirect the blame to me, understood?"
        show dawn2 neutral with dissolve
        dawn2 "Well, okay… Spit it out."
        show dawn dressneutral with dissolve
        dressdawn "I am you, but from another universe, and I don’t think I need to spend too long dwelling on the circumstances of that. I simply took the job that you didn’t."
        show dawn dresshappy with dissolve
        dressdawn "I am an interuniversal scholar."
        "The dress clad Dawn nudges me."
        mc "Oh! I can vouch for this."
        show dawn2 angry with dissolve
        dawn2 "Fuck me… Seriously? That makes a lot of sense…"
        show dawn dresshappy with dissolve
        dressdawn "Yes… I’ve been spending a lot more time in this universe due to the appearance of a certain irresistible man, namely [playername]."
        dressdawn "And when I went to the spa and was mistaken for you, I knew I had to introduce myself and clear the air."
        show dawn2 happy with dissolve
        dawn2 "I appreciate that. I was starting to notice something ‘off’: rumours, sightings, and conversations I hadn’t had."
        show dawn dresslaughing with dissolve
        dressdawn "Heh, yeah… It was getting a little awkward for me too."
        show dawn2 neutral with dissolve
        dawn2 "I have so many questions… Where to begin?"
        show dawn dresssatisfied with dissolve
        dressdawn "I’ll get to each and every one, I’ve cleared my entire schedule for today just for you."
        dressdawn "But first, I had an idea to absolve our non-unique identity."
        show dawn2 happy with dissolve
        dawn2 "That is quite important, your idea?"
        show dawn dresshappy with dissolve
        dressdawn "As far as anybody else is concerned, we’re twins. Easily identifiable by my different hair and dress. If anyone asks, my new name shall be Sunset."
        show dawn2 laughing with dissolve
        dawn2 "I always thought it’d be fun to have a twin!"
        show dawn dresssatisfied with dissolve
        dressdawn "Me too! Hehe."
        show dawn2 happy with dissolve
        dawn2 "I can tell we’re going to be great friends."
        show dawn dresshappy with dissolve
        dressdawn "Let us not forget our good friend here, [playername], he’s the only one that’s allowed to know this little detail apart from the royal sisters themselves."
        mc "Yeah, I’m from a different universe too, actually."
        show dawn2 neutral with dissolve
        dawn2 "Oh, holy shit… Who else is from a different universe?!"
        show dawn dresslaughing with dissolve
        dressdawn "I think every single person from an alternative universe is in this room right now."
        show dawn dressangry with dissolve
        dressdawn "Uhm, so… I have a question… What the hell are you doing here, [playername]?"
        mc "I was actually tricked into coming here because Dawn was suspicious of me."
        show dawn2 neutral with dissolve
        dawn2 "Sorry! Although, I suppose it wasn’t much of a trick in the end…"
        show dawn2 angry with dissolve
        dawn2 "You lied to me, and then slept with me anyway! Sheesh, what an impudent man."
        show dawn dresshorny with dissolve
        dressdawn "Whaaa?! My, my, Kitten… You really must adore me, all of me, mmhehe..."
        mc "Jeez, you would say that, Dawn. Why can't you be angry like a normal girl?"
        show dawn2 angry with dissolve
        dawn2 "And he’s involved with you too? I feel mildly cheated."
        mc "That's more like it!"
        show dawn dresssatisfied with dissolve
        dressdawn "Hey, finders keepers, dearie!"
        "They’re arguing over that? Phew, I guess I got off easier than I expected."
        show dawn2 horny with dissolve
        dawn2 "Hey, I know what you’re thinking, [playername]."
        mc "Oh? You do?"
        show dawn2 laughing with dissolve
        dawn2 "Yep, and it’s a no. No double Dawn threesomes!"
        mc "I wasn’t thinki-"
        show dawn2 happy with dissolve
        dawn2 "If the other Dawn is anything like me, I’m fairly certain you’re not into it either, are you?"
        show dawn dresshorny with dissolve
        dressdawn "I couldn’t possibly say, mmhehe."
        dressdawn "I think two of us would be too overwhelming to the poor duckling, so how about we just take turns?"
        show dawn2 neutral with dissolve
        dawn2 "Actually, I think I’ll pass. I got carried away earlier, but I think it’ll be too strange to sleep with [playername] again knowing all of this."
        "Oh? A girl is rejecting me? That’s oddly refreshing."
        show dawn dresshappy with dissolve
        dressdawn "More for me then, right Kitten?"
        mc "Yeah, I think that’s a reasonable outcome."
        show dawn2 laughing with dissolve
        dawn2 "I think that’s all the immediate issues resolved, so onto questions!"
        show dawn dresssatisfied with dissolve
        dressdawn "I have some for you too, dearie."
        show dawn2 happy with dissolve
        dawn2 "Let’s take turns, then. What’s the job like, and what do you actually do here?"
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        scene bg black with s
        "The two Dawns talk it out, and I frequently join in on the conversations to add some levity."
        "They get along as well as two best friends that have known each other for years. Watching this certainly makes me wonder how I’d get along with my own alternate universe counterpart."
        "A few hours later, all is said and done. Pony Dawn and I return to her place, I’ll probably never see Anthro Dawn again, but I won’t soon be forgetting today's events."
        "Back in the nightclub…"
        play music nightclub
        scene bg nightclub with dissolve
        show dawn dressneutral with dissolve
        dawn "I really should reprimand for you sleeping with her, but I’m simultaneously flattered."
        mc "She made me work for it! Although she was flirty, it wasn’t quite as flirty as you."
        show dawn dressangry with dissolve
        dawn "I was going to say, I wouldn’t have anticipated myself to be so…  {i}easy{/i}, I guess?"
        dawn "Although that might be the more prudish side of me speaking, a side that became prominent in my time at the colourful human universe."
        mc "This Dawn seems to be a little more sexually experienced, having had boyfriends and what not."
        show dawn dresshappy with dissolve
        dawn "Ah, quite. She’s had six more years in this world to develop in that aspect, so she probably doesn’t hold the act of sex as highly as I do."
        dawn "Is she as good in bed as I am? Mmmhehe."
        mc "The only way you’re finding an answer to that, is if you build up the courage for that double Dawn threesome."
        show dawn dresshorny with dissolve
        dawn "Hehe, not going to happen, sorry kitten!"
        dawn "But I’ll let you do me twice, would that satisfy you?"
        mc "It certainly would…"
        dawn "Well, that's enough trouble for one day, but what about the evening? Will you be joining me?"
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        $ dawnvisit = 5
        if fr == 1:
            $ worldmap = 4
        jump dawntalksexmenu






        ## asks about weird sightings and rumours about her

        jump evening
label dawnshowersex:
    play music dawn fadein 5.0
    stop ambience fadeout 5.0
    "You've unlocked a secret scene! Requirements met: Visit the nightclub during the day after having sex with Dawn."
    "I ring the buzzer, not expecting a reply since it’s the morning. However, to my surprise, I hear a dull buzz in response."
    scene bg dawnsroom with d
    "I open the door, let myself into the back of the nightclub, and walk up to Dawn’s living area."
    "Hm… Well, this is strange. There’s no one here!"
    "Who on earth let me in?"
    "I walk around her main room for a little while until my ears gently pick up the sound of a running shower."
    "Ahh, I see. She let me in and immediately got into the shower…"
    "Knowing Dawn, that’s probably a subtle invitation."
    "I take the risk and peek into the bathroom. Lo and behold, there are two towels folded on the floor. Cheeky."
    show dawnb shower
    show dawn shower1
    with d
    dawn "Apologies for starting before you, but I had to make sure I washed my hair."
    mc "While I’ve already showered this morning, I really feel like I could go for another."
    dawn "Do join me, little bunny rabbit. Maybe you can help clean some areas I can’t reach."
    "As I step into the spacious shower cubical, I’ve pretty much already got an erection. It’s probably a Pavlovian response whenever I’m around Dawn at this point."
    dawn "Having you around really makes my kitten purr. Don’t be shy, give her a stroke."
    "I wrap my hand around her hips and start to rub her pussy from the front, getting a good angle on her clit."
    play music sex1 fadeout 10.0
    dawn "Mmphh, that’s right… You know exactly how to make a woman yours, and, I’m all yours…"
    "Somewhat mimicking my own movements, her hand wraps around to my front and starts jerking off my cock."
    "As blood starts to rush to my nether, my cock tightens and throbs. I make a second move; two of my fingers slip between her wet lips, and sink into her pussy."
    "Beyond the water from the shower, her pussy is starting to moisten with natural lubricants. Perhaps even enough to take me already."
    "As I rub, her own rubbing hastens on my throbbing erection, causing a small amount of precum to drip from my tip."
    "After some more teasing of her pussy, a few moans slip out between ragged breaths."
    dawn "Ahh, aahh… Move your hand out the way, and I’ll slide your cock in."
    "I do as she says without an ounce of reluctance, her hand pumping my cock back and forth in a tight grip the entire time."
    play sound cum
    show dawn shower2 with d
    "While swaying her hips back and forth like a seductress, she guides me in with her hand and backs into me until I’m fully inserted, pressing me against one of the cubical walls in the process."
    dawn "Mmmphh… Such a thick and long cock… I can feel it throbbing all over my sensitive pussy, mmmhh…"
    dawn "Keep your back steady against the wall, kitten. I’m going to ride your cock."
    play ambience sex fadein 5.0
    "Rolling her hips to perfection, Dawn’s pussy glides up and down my cock in perfectly smooth motions."
    "Her lips do grip tight around my shaft, but my cock easily slides back in every time with a lewd schlick."
    dawn  "Yesss, that’s it, ohhhh my gosh…"
    "The more Dawn gets into it, the further her back arches against my chest, and the more moans spill freely from her mouth."
    "I start to slowly move my hips back and forth, fucking her gently and savouring the tightness of her vagina in response to her more vigorous bouncing"
    "My cock was as hard as it could be, as every inch was squeezed and pleasured. Dawn was enjoying it just as much too, sweet moans escaping her lips with each thrust she made."
    dawn  "Ahaahh, aahhhh... I heard shower sex was overrated, but you know how to make everything amazing, don’t you, kitten?"
    mc "I think I’ll have to give you all the credit for this one. You move your hips like a goddess."
    dawn "I’ll take your word for it. You’d know how a goddess fucks after all, hehe."
    "Since we were fucking while standing, her legs weren’t far apart making her even tighter around my throbbing shaft."
    "The result was ecstasy, beyond amazing."
    "As I looked up at Dawn’s face I could tell by her elated expression that she is loving this even more than me."
    dawn  "Haaa, ahhh! Ohh, ahhh! *Pant, pant*"
    dawn  "Ah- Ahhh! F-Fuck, I think I’m coming already!"
    "At her pounding pace, she managed to push herself over the edge. Her insides started to constrict in rhythmical waves, tightening around the base of my cock, squeezing, and sucking tightly."
    "Not only that, but she starts to fuck even faster in the moment. Her entire body reacting with elation to each thrust as she desperately moves her hips back and forth to derive as much pleasure as possible."
    "It was at this moment where I was entranced by the way her cute breasts bounced with each movement of her hips."
    "With both my hands free, I started to massage them, caressing them and tweaking her sensitive nipples."
    dawn  "Hahhh, haahh… Mmmphh, that’s right, baby. How about you rub my clit too?"
    "Although a little harder to rub, I bring my hand down to her rocking hips and try to lock-on to her clit. Rubbing around her while she rides me. Erratically at first, but eventually I get into the rhythm and keep my finger firmly on her clit."
    dawn  "Ooohhh, aah… Aah, aaahh! Sex with you is {i}so{/i} much better than any of my previous partners. Ahh, ahhh…"
    dawn "I think I know precisely the speed I need to get you off by now, so, here goes…"
    "Her thrusts quickly accelerate. At this speed the slapping sound of our wet bodies colliding echoes throughout the cubical."
    "That combined with the lewd wet noises from our point of contact spurs me on even more."
    "I kept my finger working her nipple and clit, hoping to squeeze another orgasm out of her before my impending climax is let loose."
    dawn  "Aahhh, oohhh… I’m getting close again!"
    "I could also feel the pressure building as my cock throbbed and shaft tightened. I wouldn’t be able to hold it much longer."
    mc "I’m going to cum!"
    dawn  "Yes, yes! Cum inside me, [playername]! Let’s come together! Ahh, ahhhh!"
    play sound cum
    show dawn shower3 with cum
    play sound cum
    show dawn shower3 with cum
    "Cum exploded out the tip of my cock as I relentlessly pounded her pussy."
    play sound cum
    show dawn shower3 with cum
    play sound cum
    show dawn shower3 with cum
    stop ambience fadeout 7.0
    stop music fadeout 10.0
    "She came too, shivering and moaning in ecstasy, while I kept pumping her insides with semen."
    show dawn shower5 with d
    dawn  "Haaa… Haaahh… *Pant* What a treat you are, duckling…"
    "My orgasm eventually faded, and my hips came to a stop. I didn’t immediately pull out, instead she leans back and we embrace for a few moments."
    dawn  "Mmphh, you came a lot…"
    mc "Hard not to when it feels that good."
    dawn "Hehe, I’m glad I caught you early in the morning."
    dawn "Let’s finish up here, shall we?"
    scene bg dawnsroom with d
    "I step out the shower and begin to dry myself first, and then Dawn joins me a few moments later."
    show dawn satisfied with d
    "Living with another mare, I’m used to it taking a while for them to dry after a shower. They sometimes resort to a blow-dryer."
    "But Dawn impresses me yet again by using a spell to blow dry herself."
    "And with such efficiency too, she manages to dry herself around the same time I finish."
    show dawn happy with d
    dawn "Ahh… I feel all fluffy and fuzzy. Come here, give me a hug before I get dressed."
    play sound movement
    show dawn laughing with hpunch
    "Ahhh… She’s so soft and warm… I’ll never get bored of these soft fluffy waifus."
    show dawn happy with d
    dawn "Mmm… Such a shame that I must be off to work."
    play sound movement
    show dawn dresshappy with d
    dawn "But it was a pleasure catching you before then, [playername]. I do hope to see you again sometime."
    mc "You can bet on it."
    show dawn dresshorny with d
    dawn "Until then, I’ll be thinking about you."
    scene bg black with d
    "We leave the building, and she goes to the castle to work."
    if crystalballactivated == 1:
        jump cbmenu
    $ secretsunlocked += 1
    jump city
