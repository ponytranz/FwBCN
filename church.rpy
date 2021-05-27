label church:
    if augustavisit == 0:
        jump augustavisit1
    elif augustavisit == 1:
        jump augustavisit1b
    elif augustavisit == 2:
        jump augustavisit2
    else:
        jump augustapost
    label augustapost:
        ## Visiting, Talk, Sex, Work.
        stop ambience fadeout 3.0
        play music church fadein 3.0
        scene bg church with dissolve
        "I step into the large halls of the church, and there's one priestess that immediately catches my attention."
        show augusta nunlaughing with dissolve
        augusta "Hello, have you come to pray with me? Ah-ha, I bet you won’t fall for that one again."
        augusta "Come on, let’s go bang some chicks! I have three lined up this morning, I can join you on the first, then give you the other two and pay you 25 monies."
        mc "Woah, woah, woah. I haven't agreed to anything yet!"
        show augusta nunhappy with dissolve
        augusta "Ah, sure. What's up then?"
        label augustamenu:
            show augusta nunhappy with dissolve
        menu:
            "Research Progress":
                if aurpa1 == 0:
                    $ aurpa1 = 1
                    augusta "Currently I've witnessed you perform in three acts of sexual intercourse."
                    augusta "The first was you and I through the box."
                    augusta "The second was an interesting test with another mare in the box."
                    mc "So you admit that was a test?"
                    show augusta nunlaughing with dissolve
                    augusta "Let's not get caught up on the little things."
                    show augusta nunhappy with dissolve
                    augusta "Thirdly, there was the reverse cowgirl incident, where we nearly fucked each other to death."
                    mc "Minor exaggeration."
                    mc "What's next?"
                    show augusta nunsatisfied with dissolve
                    augusta "I'd like to see how you perform with some other mares. With that, I should have sufficient knowledge of your unique capacities as a sexual creature."
                    mc "You got it, boss."
                elif aure == 0:
                    show augusta nunsatisfied with dissolve
                    augusta "Research complete! Now I know exactly what kind of spells and movements to make you squeal with pleasure."
                else:
                    show augusta nunneutral with dissolve
                    augusta "I'd like to see you perform [aure] more acts at work."
                jump augustamenu
            "Work":
                stop ambience fadeout 3.0
                $ monies += 25
                show augusta nunsatisfied with dissolve
                augusta "Perfect... I have my own room at the back of the church, where customers pay highly to get the best services we can offer."
                show augusta nunhappy with dissolve
                augusta "I believe you're a perfect fit."
                augusta "After that, I’ll assign you to a few on your own to earn your pay."
                mc "Alright, let's get this done with."
                scene bg churchbackroom with dissolve
                show augusta happy with dissolve
                $ auredone = 0
                if aure == 0 or aure == -3:
                    $ auredone = 1
                    $ aure = renpy.random.randint(1,3)
                pass
                if aure == 3:
                    show holeb yellow with dissolve
                    unknown "Hello, uhmm... I'm here to have sex, yeah, heh... Who is it I'm fucking today?"
                    augusta "Greetings, you have access to a wonderful combination today. The best priestess and priest in the entire church."
                    unknown "O-Oh my, I hope that doesn't cost extra..."
                    augusta "Not at all! *Spank*"
                    play sound spank
                    unknown "Eep!"
                elif aure == 2:
                    show holeb grey with dissolve
                    unknown "Hey... I'm ready to have sex now..."
                    augusta "You certainly are, just look at how wet you are!"
                    unknown "Mhm... I'm very wet... Can you do something about it?"
                    augusta "Absolutely, before you even know it, you'll have a cock sinking deeply into those tight lips."
                    unknown "I like the sound of that..."
                elif aure == 1:
                    show holeb red with dissolve
                    unknown "Is that two sets of footsteps I can hear, darlings?"
                    augusta "Certainly is, for such a charming lady such as yourself we've decided to provide you with our best service."
                    unknown "Ahh, the anticipation is palpable."
                    unknown "I am truly soaked, please go as hard as you'd like in any hole you want."
                    augusta "Hey, maybe we could take a hole each. Thoughts, [playername]?"
                show augusta happy with dissolve
                augusta "What's your plan of attack?"
                menu:
                    "Who’s going to fuck the mare?"
                    "Let Augusta do it (Futa x Female)":
                        play music sex1 fadein 3.0
                        augusta "I love it when I'm involved. Let us began."
                        "Removing her Nun's habit, Augusta positions herself in front of the customer."
                        play sound movement
                        show hole augusta1 with dissolve
                        augusta "Alright, time to conjure a big ol' cock."
                        play sound genericspell
                        show hole augusta1 with moxiespell
                        "With a magical glow, a glorious cock forms between Augusta’s legs and she quickly gets into position."
                        "Her rapidly hardening horse-cock brushes against the awaiting mare's glistening and occasionally throbbing pussy."
                        play sound cum
                        show hole augusta2 with dissolve
                        "I can’t take my eyes off the sight as the flaring cock pushes against the mare’s nether lips, sliding them apart and eliciting several moans from both girls."
                        "And then with a boisterous thrust, Augusta plunges her cock to the hilt, straight past the ridge."
                        "The receiver squeals with pleasure, and maybe a little bit of pain. Her legs rattling the restraints as her hips shake."
                        play ambience sex fadein 3.0
                        "Pulling back slightly, Augusta pushes herself back in at an increasing pace. Repeatedly pounding every inch of her gigantic cock into the other mare."
                        "The willing partner writhes with pleasure, getting fucked exactly as she wanted. Her hips constantly pushing back into Augusta’s hips, hungry for the full length of the cock."
                        augusta "You’re not gonna just stand there and watch like a fuckin’ virgin, are ya? Aha!"
                        "She flashes me a smirk, she clearly noticed my erection. Although I’m not exactly sure what I should be doing in a situation like this."
                        menu:
                            "Fuck Augusta in her pussy, while she fucks the customer.":
                                $ autrain = 1
                                "I smirk and position myself behind Augusta. Although slightly flustered, she takes the hint and bends over into the wall slightly."
                                play sound cum

                                show hole train1 with dissolve

                                "She slows down slightly as I press the tip of my cock against her labia. Her pussy is already dripping wet allowing me to easily sink inside."
                                augusta "Oohhh, this always feel crazy good!"
                                "My cock plunges deep into Augusta’s pussy pushing her forward, and in turn she thrusts her hips."
                                "It takes us a few moments to perfect the rhythm, but before we know it, we’re both fucking in tandem with each other."
                                "Augusta is really loving it as she feels the double dosage of pleasure from her cock implement as well as the sensations from her pussy."
                                "She can barely contain herself as she literally moans more than the customer, whom she tightly grips the ass of just to stay standing."
                                "The movements become sloppy and primal, merely humping our hips back and forth to draw out as much pleasure as possible."
                                "The three of us manage to settle into a pretty intense rhythm of rutting. Each of us fucking at odd intervals."
                                "The soundproofed room still manages to echo slightly with moans and grunts of sexual pleasure from all three of us."
                                "Augusta bites her lips and her hips begin to move faster, I have to up my pace to keep up. She must be pushing for our orgasms."
                                play sound cum
                                show hole train2 with cum
                                "Suddenly Augusta’s cock erupts, unloading a mighty amount of cum deep into the customer’s pussy. Her pussy simultaneously tightens around my cock, squeezing it mercilessly to the point where I find myself overwhelmed with the satisfaction of a powerful orgasm."
                                play sound cum
                                show hole train3 with cum
                                play sound cum
                                show hole train3 with cum
                                "Explosively, the three of us orgasm almost concurrently as jets of cum unload deep into each of the mare’s wombs."
                                play sound cum
                                show hole train3 with cum
                                play sound cum
                                show hole train3 with cum
                                play sound cum
                                show hole train3 with cum
                                play sound cum
                                show hole train3 with cum
                                "The two of us eagerly fuck through the duration of our climaxes, getting every droplet of pleasure as possible before the high wears off and our cocks begin to grow sensitive."
                                show hole cum with dissolve
                                "Augusta and I pull out with a schlick leaving two sloppy, well-fucked pussies. Both of the mares are left satisfied and catching their breath."
                            "Double penetrate the customer.":
                                $ audp = 1
                                "I nod and position myself slightly to the side of Augusta. She takes the hint and gives me enough room to position my cock at the customer’s ass."
                                "The princess slows down slightly as I press the tip of my cock against the patron's pucker, which is soaking wet due to the drippings of vaginal lubricants from the passionate futa fuck."
                                play sound cum
                                show hole dp1 with dissolve
                                "The tip of my cock slips in with surprising ease, and there’s no protest from the customer. She relaxes her ass, allowing me to sink all the way in."
                                "Wasting no time, both Augusta and I resume thrusting, albeit slightly slower than before. The customer is fucking loving it though, each successful hilt of a cock causes her to squeak with pure ecstasy."
                                "Since Augusta and I are both slightly at an angle to the genitals, instead of parallel to them, it’s slightly awkward at first, but the sheer wetness of her sexual lubricants allows the both of us to gradually speed up, and eventually freely pound both her ass and pussy."
                                "The three of us manage to settle into a pretty intense rhythm of rutting. Each of us fucking the hole at odd intervals."
                                "The soundproofed room still manages to echo slightly with moans and grunts of sexual pleasure from all three of us."
                                "Augusta bites her lips and winks at me, as if to signal that she’s close. Her hips begin to move faster, and I up my pace to keep up. This lewd situation clearly excites her."
                                "The customer is clearly in ecstasy too, as she seems to have another orgasm. Both of her holes clenching and contracting around our cocks as her hips buck wildly."
                                "My cock throbs and grows tense in response to the almost painful tightness. Augusta also grits her teeth as her cock flares; both our orgasms seem imminent."
                                play sound cum
                                show hole dp2 with cum
                                play sound cum
                                show hole dp2 with cum
                                "Explosively, the two of us orgasm almost simultaneously as jets of cum unload deep into the mare’s womb and ass."
                                play sound cum
                                show hole dp2 with cum
                                play sound cum
                                show hole dp2 with cum
                                "Augusta unloads so much cum that it begins to unceremoniously spurt out, drenching both her pussy and ass."
                                "The two of us eagerly fuck through the duration of our climaxes, getting every droplet of pleasure as possible before the high wears off and our cocks begin to grow sensitive."
                                show hole cum with dissolve
                                "Augusta and I pull out with a schlick leaving a sloppy, well-fucked pussy and a very satisfied customer catching their breath on the other side of the wall."
                            "Masturbate":
                                $ auma = 1
                                "I shrug and begin to masturbate while I watch. I’m pretty damn aroused already, so it’s a quality fap."
                                "The two mares settle into a pretty intense rhythm of rutting, the soundproofed room still managing to echo with the moans and grunts of sexual pleasure from the three of us."
                                "Augusta bites her lip and winks while watching me masturbate, her hips moving faster and tongue lolling slightly as the sight clearly excites her."
                                "She’s clearly enjoying each and every thrust of her futa cock, and I don’t doubt the customer has enjoyed one or two orgasms by now."
                                "The futa cock throbs, Augusta grits her teeth and squeezes her lover’s jiggling ass as she undergoes an explosive orgasm."
                                "Clinging as tightly to the customer’s ass as she can, both the mare between orgasming uncontrollably."
                                play sound cum
                                show hole augusta3 with cum
                                play sound cum
                                show hole augusta3 with cum
                                "The futa cock unloads so much cum into the mare that it begins to unceremoniously spurt out."
                                play sound cum
                                show hole augusta3 with cum
                                play sound cum
                                show hole augusta3 with cum
                                "Such a lewd sight is enough to push me over the edge too, as I begin to release my load too. I aim over the receiving mare’s thighs and pussy, splattering her fur with even more hot cum."
                                "They fuck long and hard together through the climax, until it gradually peaks and falls for the three of us. "
                                show hole cum with dissolve
                                "Augusta pulls out with a schlick leaving a sloppy, well-fucked pussy and a very satisfied customer catching their breath on the other side of the wall."
                        show hole cum with dissolve
                        stop ambience fadeout 1.0
                        stop music fadeout 3.0
                        "With a quick glow, Augusta’s cock completely vanishes and she resumes her womanly self."
                        scene bg churchbackroom with dissolve
                        show augusta laughing with dissolve
                        augusta "Phew… Great job! I’d say you're impressive, but after your display the last time we met, this is just a regular occurrence for you and your wondercock, ain’t it?"
                    "I’ll do it.":
                        $ auvaginal = 1
                        play music sex1 fadein 3.0
                        hide augusta with dissolve
                        "Erection already in hand, I return to the mare’s awaiting pussy. I can see Augusta in the side of my eye beginning to rub her pussy unceremoniously."
                        play sound cum
                        show hole vaginal1 with dissolve

                        "I press the tip of my cock against the soaking wet labia and push my shaft in with ease, sinking deeply into the mare’s pussy in a single smooth motion."
                        play ambience sex fadein 3.0
                        "As smooth as my movements are however, the squirms of pleasure and satisfaction from the customer are undeniable. Her tail swishing from back and forth, as her tight pussy eases to my girth, and her hips wriggle up and down like they’re begging for more."
                        "Several moans escape her lips into the echoing wooden box as I continuously thrust in and out of her."
                        "And then, Augusta who had been rubbing her pussy closes the distance, a sly grin on her face as she licks her lips."
                        "My cock throbs a little in anticipation of Augusta’s next action. She kneels down slightly, bringing her face towards the point of sex and starts to lick at the connection."
                        "Graciously toying with the customer’s clit and occasionally brushing against my cock."
                        "Normally the pleasure of a tongue against my shaft would be somewhat unnoticed relative to the tightness and warmth of a pussy, but for some reason this goddess, princess, whatever of love’s tongue feels exceedingly pleasurable at the mere touch."
                        "The customer writhes with pleasure, several moans slipping out in lustful excess as her senses are assaulted by both Augusta and I."
                        "The three of us settle into a pleasurable rhythm of sex, I pound the pussy while Augusta’s lolling tongue adds her special charm to the mixture."
                        "After only about twenty seconds, I can feel her pussy clenching, wringing tightly around my shaft as she climaxes."
                        "I’m sure I’d cum prematurely too if I kept going at this pace, so I slow down slightly, to savour the pleasure for a little longer, particularly enjoying the feeling of her pussy contracting around my shaft."
                        stop ambience fadeout 2.0
                        "And then something I didn’t expect happens. Augusta wraps her hand around my cock, forcing me into a complete halt while one third of my cock’s tip is still warmly inside the customer."
                        augusta "Are you ready? I’m going to make you cum inside this mare now…"
                        "Before I can even question her, her hand begins to move back and forth my member. For a moment I assume I’m crazy, but her hand and grip feel just as good as a pussy, maybe even better."
                        "Even with part of my cock still nestled within the mare, Augusta manages to find that hand job sweet spot that I’d often use to reach climax while masturbating."
                        "She focuses on that sensation and speeds up, jacking me off into the mare. My cock easily grows tense, the tip enlarging and throbbing inside the customer."
                        "Augusta wasn’t joking, I’m gonna cum! Her masturbatory technique currently rivals my own, and she’s starting to move even faster!"
                        play sound cum
                        show hole vaginal2 with cum
                        play sound cum
                        show hole vaginal2 with cum
                        "*Spurt, spurt* Suddenly my orgasm is reached and several jets of jism are released into the mare’s needy pussy."
                        play sound cum
                        show hole vaginal2 with cum
                        play sound cum
                        show hole vaginal2 with cum
                        "The princess jacks me off vigorously into the customer’s pussy throughout the entire climax."
                        "As my orgasm fades, Augusta returns upright and sucks off a stray drop of cum from her finger."
                        show hole cum with dissolve
                        "I barely have to pull out of the well-fucked pussy. Despite the lack of thrusting in the last part, the customer is still very satisfied and catching their breath on the other side of the wall."
                        mc "W-What was that all about?"
                        scene bg churchbackroom with dissolve
                        show augusta happy with dissolve
                        augusta "Ah-ha, that’s a fetish I have. I like to jack dudes off into other mare’s pussies."
                        mc "Ohhh… Hmm… You know, I can kinda understand why you’d like that."
                augusta "Another satisfied customer. Let's give the gal some peace."
                play music church fadein 2.0
                scene bg church with dissolve
                show augusta nunhappy with dissolve
                if auredone == 1:
                    $ auredone = 0
                    $ aure = 0
                elif aure == 3:
                    $ aure -= 1
                    augusta "As I've seen before, that was another fantastic performance."
                    augusta "It would seem your phallus is pretty similar to other species, however I had previously noted one big difference. As you might know, Stallions have evolved a ridge."
                    show augusta nunneutral with dissolve
                    augusta "It is theorised that this ridge is to help clear a female's vagina of a previous lover's sperm, to help better facilitate an alpha dominated hierarchy."
                    augusta "In other words, the better the stallion is at clearing cum from the vaginas of the females, the more likely he'll spread his seed over the others."
                    mc "Very... interesting... And a little gross."
                    mc "So humans don't have this ridge?"
                    show augusta nunsatisfied with dissolve
                    augusta "On the contrary, after close inspection your penis does seem to have this ridge in the location that separates the head from the shaft."
                    mc "The glans area? You know, I've never really considered that."
                    show augusta nunneutral with dissolve
                    augusta "Yeah, it would seem your species had some similar leanings in terms of natural selection."
                    augusta "*Sigh* Natural selection is a strange beast."
                    show augusta nunhappy with dissolve
                    augusta "Hopefully next time I can tell you a little more about my findings on the human male's sexual anatomy."
                    menu:
                        "You're crazy, but okay!":
                            show augusta nunsatisfied with dissolve
                            augusta "Perfect!"
                        "How'd you get all that information from just watching me?":
                            show augusta nunsatisfied with dissolve
                            augusta "I've got a good eye for these things. And heck, how different can your penis possibly be anyway?"
                            mc "Fair enough, maybe figure out why I last longer than stallions next time."
                            show augusta nunneutral with dissolve
                            augusta "Curious, I'll look into it."
                        "I feel like a test subject.":
                            show augusta nunlaughing with dissolve
                            augusta "Oohh, boohoo, poor [playername] getting paid to fuck mares with a goddess of love."
                            mc "Alright, I get your point."
                elif aure == 2:
                    $ aure -= 1
                    show augusta nunhappy with dissolve
                    augusta "Another amazing performance. I've really been wondering why exactly you last so long compared to... literally every other anthropomorph in the UEC!"
                    augusta "And I think I'm about to hit the last nail on the coffin!"
                    mc "Hit me with your best shot."
                    show augusta nunsatisfied with dissolve
                    augusta "Okay, here's my theory. Most anthropomorphs have developed reproductive cycles, which naturally vary between species, but they're generally quite quick."
                    augusta "natural selection has simply decided that mating needs to be quick, and that'd make a lot of damn sense, natural selection only cares about how many babies you have."
                    augusta "Who's gonna have more children? Mr. One Pump Chump or Señor Twenty Pamp Champ?"
                    mc "Ahaha, alright, I get your point."
                    show augusta nunneutral with dissolve
                    augusta "However, it would seem that in your species, natural selection didn't deem a fast 'nut' time to be an effective method of spreading your genes."
                    augusta "Your penis seems to have lost its ability to quickly ejaculate on a short notice, which is likely conducive to forming stronger bonds with single mates."
                    augusta "Does your species have a lot more males, by chance?"
                    mc "It certainly does, I'm impressed you got that by simply watching me fuck."
                    show augusta nunhappy with dissolve
                    augusta "I thought so. It would seem there's a slight correlation between the gender ratio of a species and the time to ejaculate."
                    augusta "The more females to males, the faster a male needs to ejaculate, and the less time needed to spend building a 'relationship'. Get it?"
                    mc "Got it! I'm actually very impressed by this one."
                    show augusta nunlaughing with dissolve
                    augusta "Thank you, I am pretty amazing aren't I?"
                elif aure == 1:
                    $ aure -= 1
                    show augusta nunhappy with dissolve
                    augusta "Well, I think I've learnt just about everything I'll be able to just from watching you, and I don't think it'd be overly worth investigating much more."
                    mc "What you've found already has been quite impressive. I've enjoyed working with you, Augusta."
                    augusta "And I with yourself."
                    augusta "Overall, it would seem that your penis has been evolved with the partner's pleasure more in mind than the average species. Count yourself lucky, or rather the girls you find yourself with."
                    mc "Ahh, as if I needed another reason to be popular."
                    augusta "Ah-ha, quite the Arcadian heart-throb, aren't you?"
                    augusta "I guess I mentioned a reward of some kind, and I think I finally figured out something worth your time."
                    augusta "Take this key and keep it safe in your satchel. It lets you into a special room in the art gallery with canvas that I have personally blessed."
                    augusta "When you look into the canvas, you'll be able to see past sexual encounters perfectly form."
                    show augusta nunlaughing with dissolve
                    augusta "It's a private room too, there are tissues, ah-ha!"
                    mc "Thank you, Augusta. That's an awesome reward, I knew you wouldn't let me down."
                    $ artgallery = 1
                show augusta nunhappy with dissolve
                augusta "Another job well done earlier, and thanks for the fun, [playername]."
                augusta "Two more girls today and you can collect your pay from Sylphi."
                mc "Got it. See you later, boss."
                stop music fadeout 3.0
                scene bg black with dissolve
                "One short work day later..."
                jump evening
            "Sex with you?" if augustasex == 0:
                $ augustasex = 1
                augusta "Ah, sure! I'm always lookin' for a good fuckin'!"
                augusta "Same as before? I'll drive you wild."
                mc "Sounds good to me."
                label augustareversecowgirl:
                    scene bg churchroom with dissolve
                    play music sex1 fadeout 3.0
                    scene augusta cowgirl1 with dissolve
                    "She twirls around and sits her cushiony ass on my thighs, her tail excitedly swishing back and forth."
                    "Gently she backs into me, until my cock is cushioned between her ass cheeks, some slight contact on her genitals."
                    "With expert circular hip movements, she then massages my cock with her ass until it’s throbbingly erect."
                    augusta "Ooohhh… I like your cock, bro…"
                    "Satisfied with her work, she lifts her butt even further so the tip of my cock is mushed up against her vulva."
                    "Swaying her bubble butt back and forth seductively, she uses her right hand to hold my throbbing member steady as she guides it inside."
                    play sound cum
                    show augusta cowgirl2 with dissolve
                    "Pushing her rear down, she keeps going until I’m completely submerged in her wet and ready pussy. Did she have that buttplug in the entire time? Sneaky."
                    augusta "Ah-ha, I knew your juicy cock couldn’t resist such an amazing pussy like mine… With just a little zap of magic, I’m going to make you feel so, so, so good…"
                    play sound genericspell
                    show augusta cowgirl2 with moxiespell
                    "She winks as she casts a subtle spell. I don’t feel anything at first, but I’m sure the effects will soon become apparent."
                    "Her pussy squeezes slightly, reminding me of how amazing her warm insides feel. A few drops of pre-cum escape my tip as she begins to work her hips like a true goddess of sex."
                    "It’s all in the hips with this mare as she begins to swing them in little circles with the grace of a dancer."
                    "Her circular movements gradually become elliptical as her tight lips slide up and down the base of my shaft with increasingly long thrusts."
                    "Each thrust gaining intensity and vigour… *Thwap… thwap… thwap… thwap, thwap, thwap! *"
                    show augusta cowgirl3 with dissolve
                    "As a lover of pleasure herself, her movements are expertly hitting all the pleasure points deep within her pussy while also creating some friction on her clit."
                    augusta "Haahh, haahh… How is it? This will always be the best sex you’ll ever feel, dearie…"
                    "She may be right, although her technique is slow right now, her purposeful movements are maximising and heightening the pleasure I feel… It’s really fucking good."
                    augusta "Of course, this is just the starter… But I think it’s time for the main course, don’t you?"
                    "Augusta drops her weight down and lets out a satisfying moan as she sinks all the way down my cock again. She then shimmies around in place for a few seconds as she gets into a comfortable position… A comfortable position for what?"
                    augusta "Ready, babe? This is how a goddess of love fucks, there’s no shame in cumming prematurely, ah-ha!"
                    play ambience sex fadein 3.0
                    show augusta cowgirl4 with dissolve
                    "Augusta doesn’t wait for an answer, her bubble butt begins bouncing up and down rapidly, her tight wet pussy squeezing and clenching the entire time."
                    "*Thwapthwapthwapthwapthwapthwap!!!*"
                    augusta "Ahhh, yess, yeeessss! Stuff me full of your cum!"
                    "My teeth grit and muscles grow tense as an explosive wave of pleasure consumes my body. The feeling borders on overwhelming, the sheer ecstasy numbing my brain to such heights I could even faint."
                    "I can feel a wave of heat running through my groin as my orgasm builds aggressively quick, I’m barely able to hold back for thirty seconds of her rutting."
                    "Ah?! I’m cumming already! The pleasure I feel is consistently orgasmic, so I barely noticed the difference when I began to ejaculate."
                    play sound cum
                    show augusta cowgirl5 with cum
                    play sound cum
                    show augusta cowgirl5 with cum
                    augusta "Ahhhahhh! That’s it! Ooohhh, mmmhhphhh! Let it all out, ahhhh, let it all out! *Thwap, thwap, thwap!"
                    play sound cum
                    show augusta cowgirl5 with cum
                    play sound cum
                    show augusta cowgirl5 with cum
                    "Cum begins pouring into her womb, almost excessively. Augusta’s eyes roll back as she experiences an equally powerful orgasm, her body twisting so much that even her riding falters."
                    play sound cum
                    show augusta cowgirl5 with cum
                    play sound cum
                    show augusta cowgirl5 with cum
                    "She babbles almost incoherently with each blast of cum, her pussy squeezing tighter and tighter, milking my throbbing cock the entire time."
                    play sound cum
                    show augusta cowgirl5 with cum
                    play sound cum
                    show augusta cowgirl5 with cum
                    "She and my orgasm keep going far past the point I knew possible; it feels like she’s borderline showing off as she wrings my cock for the most messy and powerful orgasm she possibly can."
                    "I could swear her toned belly almost distends from the amount of cum unloaded inside her; if anything, my balls feel lighter, that’s for sure."
                    show augusta cowgirl6 with dissolve
                    stop ambience fadeout 2.0
                    stop music fadeout 5.0
                    "Eventually she slows down, only letting my cock go at the moment the discomfort from sensitivity overrides the feeling of pleasure."
                    augusta "Mmphh… And here’s the dessert, dearie…"
                    "Even now, Augusta is a stickler for the obscene as she rises her rear slightly and allows me to watch the waterfall of whiteness drip from her thigh-gap."
                    scene bg churchroom with dissolve
                    play ambience ambienceday fadein 3.0
                    show augusta happy with dissolve
                    augusta "Alright, lovely. The morning is still young, we best return downstairs."
                    play music church fadein 3.0
                    scene bg church with dissolve
                    jump augustamenu
            "Leave":
                augusta "Later, ya virgin."
                jump city
    label augustavisit1:
        $ augustavisit += 1
        stop music fadeout 3.0
        "There's a building here that looks like a church, or at least a place of prayer."
        "Naturally I'm curious, I haven't heard anyone mention much of religion."
        "I doubt it’s anything like a church that I’m used to. In Arcadia there are god-like beings walking among everyday people like myself."
        play music church fadein 3.0

        stop ambience fadeout 3.0
        scene bg church with dissolve
        "Out of curiosity, I step inside the building and notice several statues of alicorns and a few people dotted around chatting, praying or appreciating the architecture."
        "That makes sense to me. It seems like a place of remembrance and respect, although it doesn't seem like there are any statues of the royal sisters here. Is that because they're still alive?"
        "There is one outlying statue in the centre, just before a grand altar…"
        "While the statue isn’t larger than the others, there's a lot of focus drawn to it, so I assume this church is mainly worshipping this deity."
        "A plaque on the alter reads, ‘Augusta, Goddess of Love’."
        "As I’m prospecting the centre statue, someone surprises me from behind."
        show augusta nunhappy with dissolve
        unknown "Greetings, you are…"
        if fr == 1:
            show augusta nunsatisfied with dissolve
            unknown "Aahh-ha! [playername]! I’ve heard great things about you."
        else:
            show augusta nunsatisfied with dissolve
            unknown "I believe you’re [playername], correct?"

        "This unicorn… she looks like she's cosplaying a slutty catholic nun. That’s certainly bizarre."
        "I’m curious to find out more about this mare, but first, how does she know me?"
        menu:
            "Who the hell are you?":
                $ augname = 1
                unknown "Sorry for not introducing myself properly, I was a little excited."
                amora "I am a priestess of love, Amora; it is my pleasure to make your acquaintance."
            "Why are you dressed like it's Halloween?":
                show augusta nunneutral with dissolve
                unknown "Why, this is ordinary attire for a priestess of love. It is built with certain fuctions in mind."
                "I'll bet..."
            "How do you know who I am?":
                mc "Yeah, so you’ve heard about me?"
        show augusta nunhappy with dissolve
        if fr == 1:
            unknown "It would seem your accolades proceed you. I’d like to thank you for saving Arcadia."
        else:
            unknown "Sorry, it’s a little rude, but there has been some gossip about a strange humanoid called [playername]."
        show augusta nunneutral with dissolve
        if augname == 0:
            unknown "Sorry for not introducing myself properly, I was a little excited."
            amora "I am a priestess of love, Amora; it is my pleasure to make your acquaintance."
        menu:
            "Sooo... You work here?":
                mc "It’s nice to meet you too. So, you work here?"
                amora "I perform rites and duties within the church, it’s one of my many responsibilities. Have you come to pay your respects?"
            "That dress really makes your features 'pop'.":
                show augusta nunlaughing with dissolve
                amora "As is intended... Sorry, it would seem my nipples like to poke through the fabric quite often."
            "I hope you're one of those nuns that does the opposite of celibacy.":
                show augusta nunlaughing with dissolve
                amora "Are there any other types?"
                "Best universe ever!"
        show augusta nunhappy with dissolve
        amora "May I ask, why is it that you've come here, young one?"
        menu:
            "I came here to chew bubblegum, and fuck.":
                mc "And your pink fur is exactly the flavour I need."
                show augusta nunlaughing with dissolve
                amora "I... see... In that case, I think it's only fair that I show you more about this church..."
            "I'm here because I'm curious about this world's culture and religion":
                mc "To tell you the truth, I was just stricken with curiosity and awe. I don’t know much about Arcadia so I’m interested in the culture and religion."
                show augusta nunneutral with dissolve
                amora "Ahh, of course you don’t. In that case..."
            "Honestly, I have no idea. I might head out now.":
                show augusta nunneutral with dissolve
                amora "Ah, there's no need to be hasty. There is a lot of fun to be had at the church."
                mc "Pfft... That's something I thought I'd never hear in my lifetime."
        show augusta nunhappy with dissolve
        amora "Allow me to be your guide for this religion of love. With your consent, I can immerse you in the full experience this church has to offer."
        menu:
            "Experience the Church of Love.":
                jump augustavisit1c
            "Pass for now":
                show augusta nunsad with dissolve
                amora "Ahh… That is a shame, I did feel a strong connection with you."
                "She shakes her head, smiles and bows to me."
                show augusta nunhappy with dissolve
                amora "Thank you for coming here today. Do seek me again if you'd like to see what a priestess of love can do."
                hide augusta with dissolve
                "Well, that was weird. What exactly would a 'full experience' from a priest of love be like anyway?"
                "I think I'm just being beyond idealistic if I assume it's sex... But, maybe..."
                jump city

        label augustavisit1b:
            play music church fadein 3.0
            stop ambience fadeout 3.0
            scene bg church with s
            show augusta nunhappy with dissolve
            amora "Greetings [playername], have you decided join our church?"
            mc "Well... I don't know about that, I barely know anything about your religion."
            show augusta nunsatisfied with dissolve
            amora "Worry not, young one. I can show you the full experience, all you need to do is ask."
            menu:
                "Experience the Church of Love.":
                    jump augustavisit1c
                "Pass for now":
                    show augusta nunsad with dissolve
                    amora "Ahh… That is a shame, I did feel a strong connection with you."
                    "She shakes her head, smiles and bows to me."
                    show augusta nunhappy with dissolve
                    amora "Thank you for coming here today. Do seek me again if you'd like to see what a priestess of love can do."
                    hide augusta with dissolve
                    "Well, that was weird. What exactly would a 'full experience' from a priest of love be like anyway?"
                    jump city

        label augustavisit1c:
            pass
            $ augustavisit += 1

        "Hmm… This is either going to be really sexy, or really boring… And I really can’t figure out which one it’ll be yet."
        mc "Very well, I’d love a miniature crash course in this area of Arcadian culture."
        show augusta nunhappy with dissolve
        amora "Lovely! [playername] please don’t take this request lightly, however, I would like to extend an invitation to pray to Augusta together, do you accept?"
        mc "Umm… Sure?"
        amora "Very well. Follow my lead."
        hide augusta
        scene bg churchaltar
        with dissolve
        "Amora and I kneel together before a grand altar in the centre. I’m not sure what I should do, but I’ve committed."
        "I follow her lead, but she doesn’t do anything other than kneel in such a way that her butt and heels touch, then she closes her eyes."
        "Her expression is one of pure meditation, as if she resigned all thought and spread her consciousness to her physical being to live wholly in the moment."
        "Alright, here I go… I close my eyes and repeatedly tell myself to relax."
        "Relax, relax, relax… relax… relax… relax…"
        "Tension within my body gently eases and melts away as I tune into the world around me."
        "After around thirty seconds we finish and she turns around to me smiling."
        show bg church
        show augusta nunhappy
        with dissolve
        amora "Ahh… I felt it, didn’t you? Our connection… Thank you for coming here today [playername]…"
        "Uh... What is she talking about?"
        menu:
            "Yeah, we have a really deep bond. I think we should explore it some more.":
                show augusta nunsatisfied with dissolve
                amora "I absolutely agree... Ohh, that fills me with such elation, [playername]"
                "Woops, that felt a little manipulative."
            "I didn't feel jack shit.":
                show augusta nunlaughing with dissolve
                amora "Yah well, your posture was pretty shit! Ah-ha!"
                mc "E-Excuse me?"
                show augusta nunhappy with dissolve
                amora "My apologies [playername]... That was very unprofessional of me. Allow me to make it up to you."
            "My balls feel a bit tingly, is that normal?":
                show augusta nunhappy with dissolve
                amora "Actually, yes! Many males claim such a phenomena. I can only assume that means you were attuned well to my vibrational levels."
                "Ehh...?"
        show augusta nunsatisfied with dissolve
        amora "I like you [playername], and I’d like to perform a proper ritual with you, for the Goddess of Love."
        amora "That is, if you’d like."
        mc "Hmm, a proper ritual? Sure, I’m curious."
        show augusta nunhappy with dissolve
        amora "Very well, please come with me."
        stop music fadeout 3.0
        scene bg black with dissolve
        "Without even really considering the situation, I find myself somewhat allured by the nun figure as I follow her deeper into the cathedral, to a room at the back."
        "I’m not sure where she’s taking me, but I’m hoping that the nun outfit is just for show because I’m eager to get acquainted with her body."
        "As we pass multiple doorways covered in black curtains, I can hear vague voices on the way… I try to make them out, but each room seems to be well sound proofed."
        scene bg churchbackroom with dissolve
        play music augusta fadein 3.0
        "Before I know it, she leads me into one of those very rooms. It’s strange, yet cozy…?"
        "Actually, I take that back, this is far from cozy."
        "It's just a wooden box."
        "It’s unmistakably still a religious room by design."
        "There's something that stands out to me though, one part of the wall has a random hole with a black curtain draped over it as to obscure the other side."
        mc "Just what kind of ritual is this?"
        show augusta nunhappy with dissolve
        amora "Stay here, and allow me to show you…"
        hide augusta with dissolve
        "I watch as the mare disappears behind a fairly subtle door in the wall. I hadn't even noticed!"
        "Hmm... Seems like she went to the other side of the hole."
        "I can hear some dull echoing knocks against wood as Amora fumbles around the other side of the seemingly hollow wall."
        "And then… I realize exactly what this room is for."
        "She shimmies through the hole, and hoists her feet onto some comfortable hangers."
        scene holeb augusta with dissolve
        "Immediately her pussy is spread and available, somewhat shimmering from a lustful display of grool and juice."
        "Oh my god, holy shit, Jesus Christ, this is certainly enough to make me religious."
        mc "So, this is what a ‘priestess of love’ does?"
        "She’s like a reverse nun, then."
        amora "We make love as a sign of worship and prayer to Augusta, the Goddess of Love, Lust and Fertility."
        amora "We worship and share in feelings of pleasure and arousal."
        "She should have finished the conversation before getting into position… With this wall between us and her legs open spread eagle, it feels like I’m in some sort of strange sexy confessional…"
        mc "So, the priestesses offer themselves to the public for your goddess?"
        amora "It has been proven to be a highly effective method of spreading faith."
        mc "Yeah, I can believe that..."
        amora "However, you’re incorrect with your assumption. It’s not public; y-you usually have to pay first…"
        "Oops, did I offend her? She let me in here for free, so I just assumed..."
        mc "Hmm… Right, if it was freely available to the public, this place would be far too popular."
        amora "Not everyone is deserving of Augusta’s blessing, you however… I was serious when I told you I’d let you fully experience the church of love."
        amora "Think of it as a gift to welcome you into this new world. Others pay thousands of monies to indulge in such an honour."
        "So, it is an extremely fancy religious brothel… I guess it makes sense that something like this would exist."
        "There must be several other priestesses of love getting pounded in this church right now. Or more likely, priests of love pounding."
        mc "I don't see how this is a ritual, but I do seem pretty horny right now, so I'm down."

        amora "When a male and female pray together to Augusta, it's a divine act…"
        amora "When we prayed together, Augusta sensed our prayers and blessed us, guaranteeing our imminent love-making."

        "Ah?! Wait, she’s right… I do feel compelled to have sex right now, I even agreed to follow her without even thinking."
        "And here I am dick in hand about to fuck her, and I've barely even considered the circumstances."
        mc "I basically agreed to have sex with you the moment we prayed together?"
        amora "What else do you pray to the goddess of love for? We prayed for love, lust and fertility together."
        amora "Augusta sensed our prayers and blessed the two of us, imbuing us with the sexual spirit and desire to make love with each other."
        amora "And now… We’ll become one, through the act of love."
        mc "So... That's literally my fate? I'll fuck you in the future no matter what?"
        amora "Indeed, that's the power of a goddess for you."
        amora "Of course, it only works with consenting partners. Do you have a soft spot for me? Hehe, I knew it'd work."
        mc "Ehh... You got me there."
        "The act of love I get... but through a wall?! She’s definitely crazy, but crazy-hot."
        amora "And through a bountiful seed, you shall be bestowed with great power."
        mc "Really? I’ll gain power if I have sex with you?"
        amora "We priestesses are personally blessed by Augusta herself; we gain and give power through the act of love."
        amora "Indeed, if you fill me with a bountiful seed, you shall feel reinvigorated and energised."
        "She makes a good argument, and now I’m damn curious to find out what’ll happen if I do cum in her… After all, magic does exist in this world."
        stop music fadeout 4.0
        amora "Now, enough talk… Are you ready for the best fuck in Arcadia?"
        "I tap my currently erect cock on her thigh. I decided long ago that I'll fuck her, blessing from a goddess or not."
        "Her pussy is already glistening with lubricant as I gently slide my tip up and down the moist lips."
        play music sex1 fadein 3.0
        play sound cum
        show hole vaginal1 with dissolve
        "Lining her vagina up with the head of my cock, I slowly push myself inside."
        "Amora gasps as I sink inwards, her entire pussy engulfing my cock. The inside of her slick slit is exceptionally pleasureful, it really does feel like there’s magic enhancing this feeling."
        amora "Oohh, that’s good… I want you to really give it to me, fill me with your love…"
        play ambience sex
        "She wriggles happily beneath me as I rock back and forth, gradually picking up speed."
        "I go faster and faster, her light gasps turn into soft reverberated moans, and then squeals of delight."
        "It’s almost regretful that this wall keeps us apart, I'd love to see her body, breasts and face... but this is a professional establishment after all."
        amora "Oooohhh, yesss... I'm getting close, really close..."
        "Already? The blessing must be giving her a lot of pleasure too. I feel like I could cum prematurely if I let my guard down, it feels that fucking good."
        "My crotch slaps lewdly against her squelching pussy, as I fuck her harder and faster. I feel genuinely invigorated already, as if I have a well-rested bonus."
        "I’m already teetering on the edge of my orgasm, and Amora seems to be climaxing as her body quivers and insides contract."
        amora "Oohh, ohhhh! Coming, oohh...! S-So good!"
        "That was by far the easiest orgasm I've ever gotten from a partner. But I keep holding out on my own climax as I continue to savour the delectable pleasure of this priestess's pussy."
        amora "Isn’t this great? The more you give the more you get, [playername]! *Pant, pant*"
        "My cock tenses as the need to orgasm rises. The cries of pleasure from my lover only spur that desire further."
        "Her warm pussy squeezes continually around each inch of my sensitive shaft, attempting to wring me from head to hilt."
        "The intensity and pressure of the rutting rises far beyond any previous lovers, as if the foreshadowed magic was enhancing every sensation."
        amora "Cum inside me, [playername]! Fill me with your love! Ahh, ahhh!"
        play sound cum
        show hole vaginal2 with fcum
        play sound cum
        show hole vaginal2 with fcum
        play sound cum
        show hole vaginal2 with fcum
        play sound cum
        show hole vaginal2 with fcum
        "Unable to hold back any further, my cock unloads into Amora’s sloppy pussy, soaking it with an unusually high amount of semen which seeps deep into her womb."
        play sound cum
        show hole vaginal2 with fcum
        play sound cum
        show hole vaginal2 with fcum
        "Amora seems to gain immeasurable pleasure from the act of ejaculation itself, as her body wracks into another orgasm."
        play sound cum
        show hole vaginal2 with fcum
        play sound cum
        show hole vaginal2 with fcum
        "I fuck throughout my entire orgasm, and I’m certain it lasts a little longer than usual."
        stop ambience fadeout 3.0
        show hole cum with dissolve
        stop music fadeout 3.0
        "Even as I pull out, I feel satisfied and energised. While not quite enough that I could go again, I just feel ‘good’, there’s no other way to really describe it."
        "Oh, and Amora is still quivering in post-orgasmic bliss. I can only guess that a priestess of love in a world like this is going to be one passionate fucker."
        mc "Uhm, should I leave now? I’m sure you have other customers."
        amora "W-Wait! I’m coming out!"
        scene bg churchbackroom with dissolve
        mc "Huh?"
        play music augusta fadein 3.0
        "Awkwardly fumbling, she vanishes under the curtain and returns through the door in the hollow wall."
        show augusta nunlaughing with dissolve
        "Still completely adorned in her nun’s habit. She did put her stockings back on though, probably removed them earlier so they wouldn't get stained."
        show augusta nunhappy with dissolve
        amora "*Pant*… Thank you for completing this ritual with me, how would you rate your experience with the church?"
        menu augustareview:
            "5/5":
                mc "Hmm, pretty good if you ask me. I was sceptical at first, but I feel great."
                show augusta nunsatisfied with dissolve
                amora "Ah-ha, splendid! You were just what I needed to end my shift."
                amora "Say, how about we go and celebrate with a few brewskies?"
            "4/5":
                show augusta nunhappy with dissolve
                amora "Ahh, another satisfied custom- uh, patron?"
                amora "Say, how about we go and celebrate with a few brewskies?"
            "3/5":
                show augusta nunneutral with dissolve
                amora "Well... I was kind of hoping it'd be higher... Since I'm a priestess of love, and all."
                amora "Say, maybe we could raise that score with a few brewskies, how about it?"
            "2/5":
                show augusta nunsad with dissolve
                amora "A-A two?! Do you have any idea who I am?"
                mc "No..."
                show augusta nunneutral with dissolve
                amora "... Well... I'm good at sex! So... If you think it's a 2, that must be your fault."
                mc "Well... All you did was lay there and take it. Were you really expecting anything higher than a two?"
                amora "?! Holy shit... You're right..."
                amora "I need to hear more about this... Come, join me at the bar and we'll discuss some stratgies to improve the church's service. I'll pay!"
            "1/5":
                if augustareview15 == 0:
                    $ augustareview15 = 1
                    show augusta nunangry with dissolve
                    amora "Fuck you too, buddy. I ain't gotta put up with that kind of bullshit."
                    amora "Give me an honest review!"
                    jump augustareview
                else:
                    show augusta nunsad with dissolve
                    amora "Sigh... Whatever, man..."
                    amora "I'm gonna go drown myself in some alcohol. Wanna join me?"
        mc "You are the strangest nun I’ve ever met. Why is your shift ending before 9:00am anyway? Were you on the ol’ nightshift?"
        show augusta nunlaughing with dissolve
        amora "Come on dummy, why do you always have to ask questions? Take the hint and join me today!"
        mc "Alright fine."
        stop ambience fadeout 3.0
        stop music fadeout 3.0
        scene bg arcadiastreets with dissolve
        "As we leave the church together, her demeanour noticeably changes."
        "From the stoic priestess, she has gradually softened to a less professional and more playful exterior."
        show augusta nunhappy with dissolve
        "However, she still hasn’t taken off her habit. What’s the deal with that?"
        play music aurora
        scene bg bar with dissolve
        "Anyway, she leads me to her favourite tavern. One of the few places in the city that bothers selling alcoholic beverages this early in the day."
        "As she buys the first round, Amora and I settle down at a table and start talking."
        "I’ve had sex with this mare but in truth I barely know her."
        mc "So, what’s your story Amora?"
        show augusta nunneutral with dissolve
        amora "Uhh, m-my story? Hmm… That’s a tough question…"
        amora "I suppose you could call me a very devoted individual in regards to all things ‘love’, and ‘lust’."
        mc "Mhm, but what exactly does that mean? I’m still a little confused about this religion."
        show augusta nunhappy with dissolve
        amora "It really is just a place where we celebrate love and lust, that church was the first location where legal prostitution took place."
        amora "However, we dressed the place with terms like ‘priestess’, and made it fancy. It helped with the social stigma."
        mc "And you decided to work there?"
        show augusta nunlaughing with dissolve
        amora "Of course! I adore it. Everything about the act of love, even when I was younger, I’d endlessly read romantic fiction."
        "How old is this girl anyway? Anywhere from 18 to 30 I presume, but that's such a wide berth. I'm so bad at gauging the age of ponies."
        show augusta nunhappy with dissolve
        amora "I want to share these positive feelings with others. Forget any social stigma, and fuck the people that look down on you for having fun."
        amora "This is true jubilation, reached through the act of making love! Even better with the blessing of a goddess on our back!"
        $ augceleselene = 0
        menu augustajubilation:
            "Is the goddess real? Like Aurora and Selene?" if augceleselene == 0:
                $ augceleselene = 1
                amora "Perhaps she is... Have you heard of her?"
                if selenevisit1 == 1:
                    mc "I think Selene mentioned her once to me... Augusta, yeah? So I guess she does exist."
                else:
                    mc "I don't think so. But I'm assuming she must exist in a real form."
                amora "You are correct. Although I have only met her sparingly, she has many responsibilities."
                jump augustajubilation
            "Interesting perspective. I'm not sure I entirely agree, but I respect it.":
                show augusta nunneutral with dissolve
                amora "Most people don't really view us as a religion, but more as a sex positive establishment."
                amora "No one really 'worships' Augusta, she's just a deity that has influence."
                amora "You don't really need to agree with our beliefs to participate, that's my point."
            "Compelling argument, I generally agree.":
                show augusta nunhappy with dissolve
                amora "Most people don't really view us as a religion, but more as an sex positive establishment."
                amora "No one really 'worships' Augusta, she's just a deity that has influence."
                amora "I'm sure some of our customers have no interest in our beliefs. However, those that do will certainly be more receptive to our magics."
                if libraryvisit1 == 1:
                    mc "Ah, yeah. The psychology of magic and all that."
                else:
                    mc "Is that so? Interesting."
            "Yeah! Fuck the social stigma against sex!":
                show augusta nunhappy with dissolve
                amora "Hell yeah, brother!"
                amora "You know, that's the exact kind of personality that can get you far in my industry."
            "Your church is just a fancy brothel. I don't need that pretentious crap about jubilation.":
                show augusta nunlaughing with dissolve
                amora "You didn't seem to mind when you were balls deep earlier!"
                mc "Yeah, well... Someone tricked me into a sex pact."
        show augusta nunneutral with dissolve
        mc "Why the walls and holes though? I feel like that divides the two people, making the act less about loving a partner and more about simply fucking."
        show augusta nunlaughing with dissolve
        amora "Ahh… That’s because… Most of our customers are female!"
        mc "Wait… the hole… is for the customer?!"
        show augusta nunhappy with dissolve
        amora "A lot of our female customers expressed a desire to remain anonymous while paying for sex, and there’s nowhere else that provides such a service in Arcadia."
        amora "That's the church's niche. Any mare can come here, disconnect from her being, and be serviced by a priest, or priestess, until she’s fully satisfied."
        mc "That's certainly interesting... Call it culture shock."
        show augusta nunsatisfied with dissolve
        amora "Ah, so you’re interested? Would you like to become a priest of love for our church?"
        mc "You mean, I’d be having sex with customers?"
        show augusta nunlaughing with dissolve
        amora "Yes! I’ll pay you well. In fact, what we did earlier, we can think of it as a successful interview of sorts."
        show augusta nunhappy with dissolve
        $ bapol1 = 0
        menu bapol:
            "Become a Priest of Love?"
            "Wait, interview? ARE YOU SCOUTING ME RIGHT NOW?" if bapol1 == 0:
                $ bapol1 = 1
                play sound genericspell
                show augusta nunhappy with moxiespell
                amora "Whaaat? No waaaay..."
                mc "Oh, okay..."
                "Huh, that's weird... What were we talking about again?"
                jump bapol
            "Get paid to fuck people? Sure!":
                show augusta nunsatisfied with dissolve
                amora "Oh delightful! You will be such a wonderful addition to our congregation!"
            "Come on, do you really think I'm that easy?":
                show augusta nunsatisfied with dissolve
                amora "Awh… But you’d be so popular, pleeeeaaasee?"
                play sound genericspell
                show augusta nunhappy with moxiespell
                mc "Oh, maybe..."
        stop music
        hide augusta with dissolve
        unknown "That’s quite enough, Augusta."
        show augusta nunsad with dissolve:
            xpos 750 ypos 30
        amora "Eep! It’s my boss!"
        play music challenge
        show aurorab dress:
            xpos 25
            ypos 0
        show aurora angry:
            xpos 25
            ypos 0
        with dissolve
        aurora "Tsk, I am disappointed in you Augusta. Why are you grooming [playername] into joining your church?"
        show augusta nunangry with dissolve
        amora "Uhmm, uhhhmm, ahhhh…"
        show aurora neutral with dissolve
        aurora "And take off your disguise, you are not fooling anyone."
        play sound movement
        show augusta sad with dissolve
        augusta "Fine… Sorry your majesty. Yes, yes, I am Augusta, the princess/goddess of love."
        mc "Woah, I was certainly fucking fooled. What’s going on here?"
        show aurora angry with dissolve
        aurora "I’d quite like to know too. I check up on [playername] for one second and you’re trying to indoctrinate him."
        augusta "B-But he's such a good fuck..."
        aurora "You must understand that [playername] is new to this world and needs to be treated with respect and care."
        aurora "He is not yours to play around with…"
        show augusta neutral with dissolve
        augusta "I-I know, but I was totally looking out for him! It’s not like I was forcing him!"
        aurora "At least be honest with him about your identity, and stop casting magic on him to make him think you’re a divine power, it is giving me second hand embarrassment."
        show augusta sad with dissolve
        augusta "Sorry boss… ;-;"
        show aurora neutral with dissolve
        aurora "I shall take my leave, stay well [playername], and stay out of trouble Augusta, you're far too old for this kind of juvenile foolery..."
        hide aurorab
        hide aurora
        with dissolve
        stop music fadeout 3.0
        "Aurora leaves as promptly as she arrived. She’s a busy woman, I have no doubt…"
        show augusta neutral with dissolve:
            linear 0.5 xpos 475
        augusta "Awh man… This is totally lame, I can’t believe Aurora busted me in front of you, so embarrassing…"
        play music augusta
        mc "So… You’re not Amora? You’re the alicorn from the statue!"
        show augusta laughing with dissolve
        augusta "Yep, ya got me! Surprised?"
        mc "You don’t look anything like that statue!"
        show augusta happy with dissolve
        augusta "Oh please, I was 1000 years younger in that statue, and my hair was completely different!"
        mc "One thousand?! You're so much older than I thought!"
        show augusta satisfied with dissolve
        augusta "Oh sheesh, just rub my biggest insecurity in my face why don't you?"
        mc "Why the disguise? You didn’t need to trick me Augusta…"
        show augusta neutral with dissolve
        augusta "Gimmie a break, I’ve been told off enough today. I just like disguising myself as a priestess and getting some of the good dick every once and a while."
        augusta "There usually aren’t enough male customers to go around… But when I saw the lost lamb of you, my eyes lit up!"
        mc "What are you, a wolf? Seriously, what the heck’s so special about me?"
        show augusta happy with dissolve
        augusta "Uhh, duhhh! You’re like, some hot alien dude. Of course, I wanna ride on that."
        show augusta satisfied with dissolve
        augusta "You're the bucket list checkbox I never knew I had! TICK! Ah-ha!"
        mc "…"
        mc "Least you’re honest…"
        show augusta happy with dissolve
        augusta "Ah-ha! That’s me! I’m one of the sluttiest mares in Arcadia, I fuck simply because it feels good, and I preach it with my own religion! How ‘bout that?"
        mc "Pretty impressive. Got any good stories?"
        show augusta laughing with dissolve
        augusta "Good stories? Hmm… Well, I’ve basically exhausted the idea of a bucket list by doing everything you could imagine. Nothing gross though, I'm a total germophobe!"
        show augusta happy with dissolve
        augusta "I’ve been in countless gangbangs, I’ve been knotted in both my pussy and ass simultaneously, and my body count is easily fifty times my age."
        mc "50 x 1,000.... 50,000?! ...That’s almost a brand-new partner every week… for one thousand years… Fuck..."
        mc "That’s really impressive for a mare. Uh, fuck, isn't the population of Arcadia only 25,000?!"
        show augusta laughing with dissolve
        augusta "A new 25,000 every one hundred years, ah-ha!"
        augusta "And I guess you’re this week’s fix!"
        show augusta happy with dissolve
        augusta "Your cock was pretty damn good, [playername]! If you’re lucky, I’ll let you have another go at my pristine goddess body."
        show augusta laughing with dissolve
        augusta "Anyway, I gotta get going. Truth is, I only have a few hours in the morning free."
        augusta "Come see me again and we can have a few more brewskies! Oh- shit, I got an even better idea!"
        show augusta happy with dissolve
        augusta "Tomorrow, or whenever really, come to the church and I’ll give you a gift to make up for tricking ya!"
        mc "Oh? Sure, I’m interested in getting to know the real you."
        show augusta satisfied with dissolve
        augusta "Awwhh, you really mean that…? Now I feel bad for tricking you at all!"
        show augusta laughing with dissolve
        augusta "Well… Whatever! See ya later, virgin!"
        hide augusta with dissolve
        mc "Virgin? B-But we literally had sex…"
        "It was too late, she had already fled the bar…"
        "I can’t get a read on that mare, that’s for sure."
        scene bg black with dissolve
        "I return home..."
        jump evening
    label augustavisit2:
        $ augustavisit += 1
        stop ambience fadeout 3.0
        play music church fadeout 3.0
        scene bg church with dissolve
        "I return to the church. There’s a light bustle of people as before. There must be some people here to pray, for luck in their lovelife, or something."
        "But also I bet some people are here for the ‘side’ business I recently discovered."
        "A church of love, that celebrate via sex… What a bizarre discovery."
        "Anyway, where’s ‘Amora’? It shouldn’t be too hard to find her, there aren’t many priestesses and their habits really stand out."
        "But… I really can’t find her anywhere."
        "As I’m pondering around, I find myself near those ‘back rooms’ from before. I can still vaguely here soft voice-like sounds from inside."
        "Curiosity gets the better of me, Augusta might be in here so I peer inside."
        scene bg churchbackroom with dissolve
        "As long as I don’t unveil any black curtains, I should be fine, I’m not impeding on anyone’s privacy then."
        "However, someone’s privacy seems to impede on me."
        scene holeb scoots with dissolve
        "At the end of one of the halls, there’s an open room with the black curtain tied open. Naturally I peer inside and immediately see a mare in the hole contraption."
        unknown "Hey, is that you? Why’s it taking so long? I hope this doesn’t affect how much time I have."
        mc "Oh, uhm… I-I’m not-"
        unknown "Don’t waste my time! I’ve got work in an hour!"
        menu:
            "Fuck her":
                "I close the curtain behind me, and move into position in front of the hole, and the 'hole'."
                "I caress the mare’s soft thighs to signal that I’m here, slowly bringing my fingers to her pussy, as I then begin to tease her by rubbing her clit."
                unknown "Oohh, nice! Ehehe... I’mma be quiet now."
                play music augusta fadeout 3.0
                show augusta closelaughing with dissolve:
                    xalign 1.0
                    ypos -125
                augusta "My my… What is this? Someone trying to steal my client?"
            "No way!":
                mc "Sorry, I’m just a customer. Do you want me to close the curtain?"
                unknown "Whaat? Where’s the priestess?"
                play music augusta fadeout 3.0
                show augusta closelaughing with dissolve:
                    xalign 1.0
                    ypos -125
                augusta "Riiight here. Sorry I’m late dearies."
                show augusta closehappy with dissolve
                augusta "Here, allow {i}me{/i} to close the curtain."
        show augusta closehappy with dissolve
        augusta "Ah-ha, you’re so eager [playername]! I haven’t even officially hired you, and you’re seconds away from humping the first exposed mare you see."
        unknown "Hey, what’s going on?"
        mc "It's not what it-"
        show augusta closesatisfied with dissolve
        augusta "We don’t have time to waste [playername], are you gonna, or am I gonna?"
        $ auma = 0
        $ autrain = 0
        $ audp = 0
        $ auvaginal = 0
        menu:
            "Who’s going to fuck the mare?"
            "Let Augusta do it (Futa x Female)":
                play music sex1 fadein 3.0
                mc "You’re going to do it? I think I’d like to see that."
                unknown "Yeh, me too! Now get on with it, yer burning a hole in my wallet with all this yapping!"
                "Removing her Nun's habit, Augusta positions herself in front of the customer."
                play sound movement
                hide augusta
                show hole augusta1
                with dissolve
                augusta "Oohh, she’s pushy ain’t she? I like them pushy."
                play sound genericspell
                show hole augusta1 with moxiespell
                "With a magical glow, a glorious cock forms between Augusta’s legs and she quickly gets into position."
                "Her rapidly hardening horse-cock brushes against the awaiting orange mare's glistening and occasionally throbbing pussy."
                play sound cum
                show hole augusta2 with dissolve
                "I can’t take my eyes off the sight as the flaring cock pushes against the mare’s nether lips, sliding them apart and eliciting several moans from both girls."
                "And then with a boisterous thrust, Augusta plunges her cock to the hilt, straight past the ridge."
                "The receiver squeals with pleasure, and maybe a little bit of pain. Her legs rattling the restraints as her hips shake."
                play ambience sex fadein 3.0
                "Pulling back slightly, Augusta pushes herself back in at an increasing pace. Repeatedly pounding every inch of her gigantic cock into the other mare."
                "The willing partner writhes with pleasure, getting fucked exactly as she wanted. Her hips constantly pushing back into Augusta’s hips, hungry for the full length of the cock."
                augusta "You’re not gonna just stand there and watch like a fuckin’ virgin, are ya? Aha!"
                "She flashes me a smirk, she clearly noticed my erection. Although I’m not exactly sure what I should be doing in a situation like this."
                menu:
                    "Fuck Augusta in her pussy, while she fucks the customer.":
                        $ autrain = 1
                        "I smirk and position myself behind Augusta. Although slightly flustered, she takes the hint and bends over into the wall slightly."
                        play sound cum
                        show hole train1 with dissolve
                        "She slows down slightly as I press the tip of my cock against her labia. Her pussy is already dripping wet allowing me to easily sink inside."
                        augusta "Oohhh, haven’t done this in a while… Ah-ha!"
                        "My cock plunges deep into Augusta’s pussy pushing her forward, and in turn she thrusts her hips."
                        "It takes us a few moments to perfect the rhythm, but before we know it, we’re both fucking in tandem with each other."
                        "Augusta is really loving it as she feels the double dosage of pleasure from her cock implement as well as the sensations from her pussy."
                        "She can barely contain herself as she literally moans more than the customer, whom she tightly grips the ass of just to stay standing."
                        "The movements become sloppy and primal, merely humping our hips back and forth to draw out as much pleasure as possible."
                        "The three of us manage to settle into a pretty intense rhythm of rutting. Each of us fucking at odd intervals."
                        "The soundproofed room still manages to echo slightly with moans and grunts of sexual pleasure from all three of us."
                        "Augusta bites her lips and her hips begin to move faster, I have to up my pace to keep up. She must be pushing for our orgasms."
                        play sound cum
                        show hole train2 with cum
                        "Suddenly Augusta’s cock erupts, unloading a mighty amount of cum deep into the customer’s pussy. Her pussy simultaneously tightens around my cock, squeezing it mercilessly to the point where I find myself overwhelmed with the satisfaction of a powerful orgasm."
                        play sound cum
                        show hole train3 with cum
                        play sound cum
                        show hole train3 with cum
                        "Explosively, the three of us orgasm almost concurrently as jets of cum unload deep into each of the mare’s wombs."
                        play sound cum
                        show hole train3 with cum
                        play sound cum
                        show hole train3 with cum
                        "The two of us eagerly fuck through the duration of our climaxes, getting every droplet of pleasure as possible before the high wears off and our cocks begin to grow sensitive."
                        show hole cum with dissolve
                        "Augusta and I pull out with a schlick leaving two sloppy, well-fucked pussies. Both of the mares are left satisfied and catching their breath."
                    "Double penetrate the customer.":
                        $ audp = 1
                        "I nod and position myself slightly to the side of Augusta. She takes the hint and gives me enough room to position my cock at the customer’s ass."
                        "The princess slows down slightly as I press the tip of my cock against the patron's pucker, which is soaking wet due to the drippings of vaginal lubricants from the passionate futa fuck."
                        play sound cum
                        show hole dp1 with dissolve
                        "The tip of my cock slips in with surprising ease, and there’s no protest from the customer. She relaxes her ass, allowing me to sink all the way in."
                        "Wasting no time, both Augusta and I resume thrusting, albeit slightly slower than before. The customer is fucking loving it though, each successful hilt of a cock causes her to squeak with pure ecstasy."
                        "Since Augusta and I are both slightly at an angle to the genitals, instead of parallel to them, it’s slightly awkward at first, but the sheer wetness of her sexual lubricants allows the both of us to gradually speed up, and eventually freely pound both her ass and pussy."
                        "The three of us manage to settle into a pretty intense rhythm of rutting. Each of us fucking a hole at odd intervals."
                        "The soundproofed room still manages to echo slightly with moans and grunts of sexual pleasure from all three of us."
                        "Augusta bites her lips and winks at me, as if to signal that she’s close. Her hips begin to move faster, and I up my pace to keep up. This lewd situation clearly excites her."
                        "The customer is clearly in ecstasy too, as she seems to have another orgasm. Both of her holes clenching and contracting around our cocks as her hips buck wildly."
                        "My cock throbs and grows tense in response to the almost painful tightness. Augusta also grits her teeth as her cock flares; both our orgasms seem imminent."
                        play sound cum
                        show hole dp2 with cum
                        play sound cum
                        show hole dp2 with cum
                        "Explosively, the two of us orgasm almost simultaneously as jets of cum unload deep into the mare’s womb and ass."
                        play sound cum
                        show hole dp2 with cum
                        play sound cum
                        show hole dp2 with cum
                        "Augusta unloads so much cum that it begins to unceremoniously spurt out, drenching both her pussy and ass."
                        "The two of us eagerly fuck through the duration of our climaxes, getting every droplet of pleasure as possible before the high wears off and our cocks begin to grow sensitive."
                        show hole cum with dissolve
                        "Augusta and I pull out with a schlick leaving a sloppy, well-fucked pussy and a very satisfied customer catching their breath on the other side of the wall."
                    "Masturbate":
                        $ auma = 1
                        "I shrug and begin to masturbate while I watch. I’m pretty damn aroused already, so it’s a quality fap."
                        "The two mares settle into a pretty intense rhythm of rutting, the room filled with moans and grunts of sexual pleasure from the three of us."
                        "Augusta bites her lip and winks while watching me masturbate, her hips moving faster and tongue lolling slightly as the sight clearly excites her."
                        "She’s clearly enjoying each and every thrust of her futa cock, and I don’t doubt the customer has enjoyed one or two orgasms by now."
                        "The futa cock throbs, Augusta grits her teeth and squeezes her lover’s jiggling ass as she undergoes an explosive orgasm."
                        "Clinging as tightly to the customer’s ass as she can, both the mares begin orgasming uncontrollably."
                        play sound cum
                        show hole augusta3 with cum
                        play sound cum
                        show hole augusta3 with cum
                        "The futa cock unloads so much cum into the mare that it begins to unceremoniously spurt out."
                        play sound cum
                        show hole augusta3 with cum
                        play sound cum
                        show hole augusta3 with cum
                        "Such a lewd sight is enough to push me over the edge too, as I begin to release my load. I aim over the receiving mare’s thighs and pussy, splattering her fur with even more hot cum."
                        "They fuck long and hard together through the climax, until it gradually peaks and falls for the three of us. "
                        show hole cum with dissolve
                        "Augusta pulls out with a schlick leaving a sloppy, well-fucked pussy and a very satisfied customer catching their breath on the other side of the wall."
                show hole cum with moxiespell
                stop ambience fadeout 1.0
                stop music fadeout 3.0
                "With a quick glow, Augusta’s cock completely vanishes and she resumes her womanly self."
                scene bg churchbackroom with dissolve
                show augusta laughing with dissolve
                augusta "Phew… Great job! I’d say you're impressive, but after your display the last time we met, this is just a regular occurrence for you and your wondercock, ain’t it?"
                if auma == 1:
                    mc "Well… All I did was masturbate; it wasn’t nearly as impressive as you."
                else:
                    mc "That was quite a unique experience…"
            "I’ll do it.":
                $ auvaginal = 1
                play music sex1 fadein 3.0
                hide augusta with dissolve
                "Erection already in hand, I return to the mare’s awaiting pussy. I can see Augusta in the side of my eye beginning to rub her  pussy unceremoniously."
                play sound cum
                show hole vaginal1 with dissolve
                "I press the tip of my cock against the soaking wet labia and push my shaft in with ease, sinking deeply into the mare’s pussy in a single smooth motion."
                play ambience sex fadein 3.0
                "As smooth as my movements are however, the squirms of pleasure and satisfaction from the customer are undeniable. Her tail swishing from back and forth, as her tight pussy eases to my girth, and her hips wriggle up and down like they’re begging for more."
                "Several moans escape her lips into the echoing wooden box as I continuously thrust in and out of her."
                "And then, Augusta who had been rubbing her pussy closes the distance, a sly grin on her face as she licks her lips."
                "My cock throbs a little in anticipation of Augusta’s next action. She kneels down slightly, bringing her face towards the point of sex and starts to lick at the connection."
                "Graciously toying with the customer’s clit and occasionally brushing against my cock."
                "Normally the pleasure of a tongue against my shaft would be somewhat unnoticed relative to the tightness and warmth of a pussy, but for some reason this goddess, princess, whatever of love’s tongue feels exceedingly pleasurable at the mere touch."
                "The customer writhes with pleasure, several moans slipping out in lustful excess as her senses are assaulted by both Augusta and I."
                "The three of us settle into a pleasurable rhythm of sex, I pound the pussy while Augusta’s lolling tongue adds her special charm to the mixture."
                "After only about twenty seconds, I can feel her pussy clenching, wringing tightly around my shaft as she climaxes."
                "I’m sure I’d cum prematurely too if I kept going at this pace, so I slow down slightly, to savour the pleasure for a little longer, particularly enjoying the feeling of her pussy contracting around my shaft."
                stop ambience fadeout 2.0
                "And then something I didn’t expect happens. Augusta wraps her hand around my cock, forcing me into a complete halt while one third of my cock’s tip is still warmly inside the customer."
                augusta "Are you ready? I’m going to make you cum inside this mare now…"
                "Before I can even question her, her hand begins to move back and forth around my member. For a moment I assume I’m crazy, but her hand and grip feel just as good as a pussy, maybe even better."
                "Even with part of my cock still nestled within the mare, Augusta manages to find that hand job sweet spot that I’d often use to reach climax while masturbating."
                "She focuses on that sensation and speeds up, jacking me off into the mare. My cock easily grows tense, the tip enlarging and throbbing inside the customer."
                "Augusta wasn’t joking, I’m gonna cum! Her masturbatory technique currently rivals my own, and she’s starting to move even faster!"
                play sound cum
                show hole vaginal2 with cum
                play sound cum
                show hole vaginal2 with cum
                "*Spurt, spurt* Suddenly my orgasm is reached and several jets of jism are released into the mare’s needy pussy."
                play sound cum
                show hole vaginal2 with cum
                play sound cum
                show hole vaginal2 with cum
                "The princess jacks me off vigorously into the customer’s pussy throughout the entire climax."
                "As my orgasm fades, Augusta returns upright and sucks off a stray drop of cum from her finger."
                show hole vaginal2 with dissolve
                "I barely have to pull out of the well-fucked pussy. Despite the lack of thrusting in the last part, the customer is still very satisfied and catching their breath on the other side of the wall."
                mc "W-What was that all about?"
                scene bg churchbackroom with dissolve
                show augusta happy with dissolve
                augusta "Ah-ha, that’s a fetish I have. I like to jack dudes off into other mare’s pussies."
                mc "Ohhh… Hmm… You know, I can kinda understand why you’d like that."
        ## after sex scene
        stop music fadeout 2.0
        scene bg churchcorridor with dissolve
        "Augusta ushers us out of the room, and we walk elsewhere. I’m not sure where, I’m just following."
        show augusta happy with dissolve
        augusta "Let’s not keep the customer waiting, we need to leave and give her some privacy."
        augusta "There’s a public shower/washroom we could go to, however, I think I’d rather bring you upstairs to my private room."
        menu:
            "Hold up, I gotta get to work before it’s too late":
                show augusta laughing with dissolve
                augusta "Work? Ah-ha! Is that a little wink-wink nudge-nudge? Fiiine, I’ll pay you for helping me with that one mare!"
                mc "Oh, I wasn’t implying tha-"
                show augusta happy with dissolve
                augusta "Aha! If you want your 20 monies, you’ll have to come upstairs to collect!"
                if auma == 1:
                    "But I barely did anything…"
                    "At least not as impressive as you."
                    augusta "You were like a cheerleader! And you kept my customer company while I was late. You can have my pay."
                else:
                    "Damn, she’s good…"
            "Sure, I’ve got time":
                show augusta laughing with dissolve
                augusta "Wonderful! In here, up the stairs and into my little love den."
        scene bg churchroom with dissolve
        "We go upstairs into a private room. I hadn’t quite anticipated such a lavish living area within this church, but I’m not exactly well antiquated with church interior design."
        "I wonder what the ‘gift’ she mentioned at the bar is?"
        play music augusta fadein 3.0
        show augusta happy with dissolve
        augusta "Here ya go, 20 monies. Not much, but think of it as your share for handling that mare."
        $ monies += 20
        if auma == 1:
            mc "Hmm… Did standing there and masturbating really bring you that much joy?"
            augusta "Absolutely! That was lots of fun. Next time though, you should join in!"
        else:
            mc "Thanks Augusta. I guess you got the last laugh in the end."
        show augusta laughing with dissolve
        augusta "So, you might remember that I mentioned a ‘gift’ if you came here again… Well, change of plans!"
        augusta "You’ll have to wait another, let’s say… fifteen to twenty minutes until I give it to you."
        mc "So... the gift is sex? I should have seen that coming to be fair."
        show augusta happy with dissolve
        augusta "Oh? Are you disappointed?"
        mc "Of course not, sex with the ‘goddess’ of love is surely a high honour."
        show augusta laughing with dissolve
        augusta "Ahahaha, yeah right! Tell another joke!"
        mc "Oh right, fucking people is kind of your thing. How the heck did you even end up in a position like that? Surely at one point you were just a normal person, right?"
        show augusta happy with dissolve
        augusta "Hmm, that’s complicated… The princess of love role is passed down not through family, but more through the church itself, and I was once a regular ol’ passionate priestess of this church."
        augusta "So in that sense, I guess I was never normal! Ah-ha, I’ve always been a complete degenerate and proud."
        mc "So, okay… How did you get the promotion of a literal fucking lifetime?"
        show augusta satisfied with dissolve
        augusta "Well my darling, it was with impeccable timing, commitment and a few parties."
        show augusta happy with dissolve
        augusta "Me and the ol’ Princess were great friends; we even fucked a few times. Actually, there are quite a few church orgies, even to this day!"
        show augusta neutral with dissolve
        augusta "Ah, I got distracted by sex again…"
        show augusta happy with dissolve
        augusta "Anyway, the old princess recognised that she’d eventually need to pass on the title and retire. So, she decided to give me an intermediary role while she ‘trained’ me in the magic and arts required to be a princess of love."
        mc "Train? What is there to possibly learn about... uh... you know?"
        show augusta laughing with dissolve
        augusta "Ah-ha, you got me there! It’s not exactly cosmic magic, but I fit the criteria and kinda fell into this position through luck."
        mc "Luck, huh? Surely there was something remarkable about you."
        show augusta happy with dissolve
        augusta "Well… It seems pretty pathetic even for a cum-dumpster like me to say I got the role because I was ‘great at the sex’, but that’s pretty much it, yeah."
        mc "Hmm… Why is there a princess of love at all, then? What’s your role in Arcadian society beyond running this church?"
        show augusta satisfied with dissolve
        augusta "You’d be surprised how powerful of a chip a sex goddess is when bargaining with other countries."
        show augusta happy with dissolve
        augusta "And believe it or not, but I do a lot of small political things on the side."
        show augusta laughing with dissolve
        augusta "You see, Selene and Aurora are pretty kick ass, but they still need a few extras to help run the country. I’m a key figure in international relations."
        augusta "I’ll often be travelling, and fuckin’, while the royal sisters can do their duty here."
        mc "Well now! I wasn’t expecting that, you may be more than meets the eye."
        mc "I bet you have a ton of experience after 1,000 years on the job then. You might be a perfect person to teach me about the world."
        show augusta satisfied with dissolve
        augusta "Exactly! That’s totally why I decided to prey on you earlier in my Amora disguise, ah-ha! It’s totally not because I was curious how you’d bone."
        mc "Jeeez, you really do think with your pussy instead of your brain."
        show augusta happy with dissolve
        augusta "Yup! You’re right about both things. I could be a pretty useful asset to teach you about this world…"
        augusta "So how about it? Care to ask a well-traversed Queen of lore about this new world?"
        $ lqir = 0
        $ lqbc = 0
        $ lqmr = 0
        $ lqrl = 0
        label lorequeen:
            show augusta happy with dissolve
        menu:
            "How are international relations?" if lqir == 0:
                $ lqir = 1
                show augusta neutral with dissolve
                augusta "You're not going to win any awards for interesting questions. But I suppose politics can be interesting to some people."
                mc "You don't even like politics?"
                show augusta laughing with dissolve
                augusta "I'm more self-concerned. I like things when I'm involved in them, especially when I can add my seductive touch."
                mc "Okay, but how's the bigger picture?"
                show augusta neutral with dissolve
                augusta "Generally peace, peace, peace. Alicorns aren't the only 'supreme' beings as some god-fearing civilians would say. We also have the Sphinx, Elder Dragons, and Demon Royalty."
                mc "Demons, huh? Those are traditionally seen as evil in my culture."
                show augusta happy with dissolve
                augusta "Really? The word demon originates from 'spirit' or 'divine power', there is no connotation of evil contained within that name, and none in their culture either."
                show augusta angry with dissolve
                augusta "But there are also more evil beings, such as the 'Morphlings'."
                augusta "Which is why powerful alliances amongst friendly and more peaceful inhabitants form. I'm on the council for relations between six local countries called the UEC."
                "On a council? I feel a bit rude to assume she's not really fit for that kind of position."
                "There's probably a lot more to Augusta than meets the eye. She is over one thousand years old after all."
                "I mean... just picture how much I've grown in my short lifetime. How much can you grow over a substantially longer one?"
                mc "Do the other countries primarily consist of other species?"
                show augusta laughing with dissolve
                augusta "Yeah, generally. Since we can only breed with our own kind. Perfect for me, right? Ah-ha."
                show augusta happy with dissolve
                augusta "There are a few smaller anarchy-esque groups, such as the 'taurs, and some lupines in the north."
                augusta "They generally keep and operate to themselves in villages, but many have generally made taxless peace and trading agreements with Arcadia."
                augusta "Arcadia and the surrounding countries are run very well with carefully distributed economies."
                augusta "This is thanks to extremely old, wise and experienced leaders that are dedicated to running the country in the interest of everyone."
                augusta "We're fortunate to rarely have corrupt leaders rise to power, but there will always be disagreements and petty spats."
                mc "Sounds like the UEC would make quick work out of a corrupt leader if they do show up."
                show augusta angry with dissolve
                augusta "I find that true corruption doesn't lend itself well to allies, no matter how charismatic the dictator thinks they may be."
                augusta "What's more dangerous is a collection of people that think they're absolute in their corruption, and deem it the 'greater good'."
                augusta "That's how you get Morphlings..."
                if fr == 1:
                    show augusta happy with dissolve
                    augusta "But you did a pretty good job of squashing those bugs for good."
                    mc "They won't try to get revenge, will they?"
                    augusta "Nah, their Queen was their only chess piece of value. The others can't do anything except disguise themselves for short periods of time."
                    augusta "And their numbers right now are low, since they're an all female race that can only breed with males of other species; most men won't fuck a morphling, they'd have to get tricked into it through a disguise."
                    augusta "Well, with any luck, perhaps Penelope can help the group turn a new leaf. But as far as I'm concerned, it'll take a few generations before I can let what they've attempted go."
                jump lorequeen
            "What's a Morphling?" if lqir == 1 and fr == 0 and lqmr == 0:
                $ lqmr = 1
                show augusta angry with dissolve
                augusta "Ah, nasty bug creatures. They're pretty similar to us ponies, but they specialise in deception, backstabbing and disguise."
                augusta "You could quite accurately call them our mortal enemies. But right now they're weak as hell, even their Queen lost all her power after a recent scuffle."
                jump lorequeen
            "Do you really fuck as a 'bargaining' chip?" if lqbc == 0:
                $ lqbc = 1
                show augusta neutral with dissolve
                augusta "Oh hell, that's merely an employment bonus. I'd fuck 'em anyway if they were interesting enough."
                show augusta satisfied with dissolve
                augusta "But then again, getting a juicy political deal is a lot easier when you're fucking the man signing the paper, ah-ha!"
                mc "I'm torn between: 'Wow, that's awesome and empowering', and 'holy shit, that's a dangerous precedent'."
                show augusta laughing with dissolve
                augusta "Ah-ha, you don't need to fuckin' lecture me, I've heard it all."
                augusta "I know I'm not exactly playing a fair game. But these deals are mostly to the benefit of everyone, rather than for personal gain."
                show augusta happy with dissolve
                augusta "Anyway, I have a personal rule, and it's actually deeply ingrained within my own religion. 'Don't use sex for personal benefit.'"
                augusta "The church donates the majority of net profits, after all the employees are fairly paid of course."
                mc "Respectable. That's awesome and empowering!"
                show augusta laughing with dissolve
                augusta "Bitch, I know it."
                jump lorequeen
            "How far reaching is your 'religion'?" if lqrl == 0:
                $ lqrl = 1
                show augusta happy with dissolve
                augusta "I mostly spread my teachings to reduce the stigma around all things sex."
                show augusta laughing with dissolve
                augusta "I currently have four churchs! One in Arcadia, one in the Dragon Lands, then two in Sel'Dua."
                show augusta happy with dissolve
                augusta "You see, that's what's uniquely powerful about being a Goddess of Love."
                augusta "Put yourself in the feet of a Goddess of Sun, or Moon, and try getting people to buy into your beliefs and politics. Almost impossible."
                augusta "I mean, there are no churches of Selene or Aurora out there, right?"
                augusta "But me? Well, my predecessor and I had it figured out."
                augusta "Once you have that church built, get a few customers, and the people like what they see, you gain some really nice leverage."
                mc "... You might actually be a genius."
                show augusta laughing with dissolve
                augusta "You're only just figuring this out?"
                mc "I think I figured out why you were chosen to become the goddess, that's for sure."
                show augusta satisfied with dissolve
                augusta "Ah-ha! Times were pretty different back then, but I was always  street smart."
                jump lorequeen
            "Also, I wanted to know about... (Conclude)":
                stop music fadeout 3.0
                play ambience ambienceday fadein 3.0
        scene bg black with dissolve
        "Augusta and I spend another half-hour chatting about herself, myself, local culture and lore."
        "If this was a cRPG, I'd probably have gained an additional skill point in lore, or something."
        scene bg churchroom with dissolve
        show augusta happy with dissolve
        mc "So you're telling me they have two cocks? Like, horizontally, or vertically?"
        show augusta neutral with dissolve
        augusta "Yup! Vertically! Bit of a gimmick after a while though."
        mc "Do the females have two vaginas?"
        show augusta satisfied with dissolve
        augusta "That's the craziest part, they don't!"
        mc "Huh... That certainly gives you some options, doesn't it?"
        show augusta laughing with dissolve
        augusta "Two girls or double penetration, right? Ah-ha!"
        show augusta happy with dissolve
        augusta "Anyway, enough about those fuckers."
        augusta "Since Aurora told me off, I have decided I want to help you in some way to make up for it, and I have a proposition that might interest you."
        augusta "First, I’d like to ‘soft’ hire you. No priest bullshit, you can just come in here and work whenever you want for good money."
        mc "Oh... You’re giving me the option to work as a prostitute?"
        show augusta laughing with dissolve
        augusta "Optional, of course, optional!"
        show augusta happy with dissolve
        augusta "The best part is you can visit me regularly, and each time you do, I can teach you a bit more about the city, country, anything you want."
        mc "That would be pretty good."
        mc "And… you’ll probably want to fuck me too, right?"
        show augusta laughing with dissolve
        augusta "Ahh, that’s a given, aha! I still have a lot more to learn about you, and I love to learn by practice..."
        show augusta happy with dissolve
        "The love goddess leans slightly towards me and licks her lips. I doubt anyone could resist her lecherous advances."
        show augusta satisfied with dissolve
        augusta "I must say, you’re one of the finer fucks I’ve had in a long time."
        show augusta happy with dissolve
        stop ambience fadeout 3.0
        augusta "And I’m the kind of girl that likes to really squeeze out as much fun from her toys as possible…"
        augusta "I really want another go with you, and this time without holding back. No walls, no disguises."
        if fr == 1:
            augusta "Think of this as a ‘thank you’ fuck for saving all of Arcadia, ah-ha!"
        else:
            augusta "Think of this as an ‘apology’ fuck for tricking you before, ah-ha!"

        ##use the predrawn reverse cowgirl of Cadance
        play music sex1 fadeout 3.0
        scene augusta cowgirl1 with dissolve
        "She twirls around and sits her cushiony ass on my thighs, her tail excitedly swishing back and forth."
        "Gently she backs into me, until my cock is cushioned between her ass cheeks, some slight contact on her genitals."
        "With expert circular hip movements, she then massages my cock with her ass until it’s throbbingly erect."
        augusta "Ooohhh… I like your cock, bro…"
        "Satisfied with her work, she lifts her butt even further so the tip of my cock is mushed up against her vulva."
        "Swaying her bubble butt back and forth seductively, she uses her right hand to hold my throbbing member steady as she guides it inside."
        play sound cum
        show augusta cowgirl2 with dissolve
        "Pushing her rear down, she keeps going until I’m completely submerged in her wet and ready pussy. Did she have that buttplug in the entire time? Sneaky."
        augusta "Ah-ha, I knew your juicy cock couldn’t resist such an amazing pussy like mine… With just a little zap of magic, I’m going to make you feel so, so, so good…"
        play sound genericspell
        show augusta cowgirl2 with moxiespell
        "She winks as she casts a subtle spell. I don’t feel anything at first, but I’m sure the effects will soon become apparent."
        "Her pussy squeezes slightly, reminding me of how amazing her warm insides feel. A few drops of pre-cum escape my tip as she begins to work her hips like a true goddess of sex."
        "It’s all in the hips with this mare as she begins to swing them in little circles with the grace of a dancer."
        "Her circular movements gradually become elliptical as her tight lips slide up and down the base of my shaft with increasingly long thrusts."
        "Each thrust gaining intensity and vigour… *Thwap… thwap… thwap… thwap, thwap, thwap! *"
        show augusta cowgirl3 with dissolve
        "As a lover of pleasure herself, her movements are expertly hitting all the pleasure points deep within her pussy while also creating some friction on her clit."
        augusta "Haahh, haahh… How is it? This is the best sex you’ll ever feel, dearie…"
        "She may be right, although her technique is slow right now, her purposeful movements are maximising and heightening the pleasure I feel… It’s really fucking good."
        augusta "Of course, this is just the starter… But I think it’s time for the main course, don’t you?"
        "Augusta drops her weight down and lets out a satisfying moan as she sinks all the way down my cock again. She then shimmies around in place for a few seconds as she gets into a comfortable position… A comfortable position for what?"
        augusta "Ready, babe? This is how a goddess of love fucks, there’s no shame in cumming prematurely, ah-ha!"
        play ambience sex fadein 3.0
        show augusta cowgirl4 with dissolve
        "Augusta doesn’t wait for an answer, her bubble butt begins bouncing up and down rapidly, her tight wet pussy squeezing and clenching the entire time."
        "*Thwapthwapthwapthwapthwapthwap!!!*"
        augusta "Ahhh, yess, yeeessss! Stuff me full of your cum!"
        "My teeth grit and muscles grow tense as an explosive wave of pleasure consumes my body. The feeling borders on overwhelming, the sheer ecstasy numbing my brain to such heights I could even faint."
        "I can feel a wave of heat running through my groin as my orgasm builds aggressively quick, I’m barely able to hold back for thirty seconds of her rutting."
        "Ah?! I’m cumming already! The pleasure I feel is consistently orgasmic, so I barely noticed the difference when I began to ejaculate."
        play sound cum
        show augusta cowgirl5 with cum
        play sound cum
        show augusta cowgirl5 with cum
        augusta "Ahhhahhh! That’s it! Ooohhh, mmmhhphhh! Let it all out, ahhhh, let it all out! *Thwap, thwap, thwap!*"
        play sound cum
        show augusta cowgirl5 with cum
        play sound cum
        show augusta cowgirl5 with cum
        "Cum begins pouring into her womb, almost excessively. Augusta’s eyes roll back as she experiences an equally powerful orgasm, her body twisting so much that even her riding falters."
        play sound cum
        show augusta cowgirl5 with cum
        play sound cum
        show augusta cowgirl5 with cum
        "She babbles almost incoherently with each blast of cum, her pussy squeezing tighter and tighter, milking my throbbing cock the entire time."
        play sound cum
        show augusta cowgirl5 with cum
        play sound cum
        show augusta cowgirl5 with cum
        "She and my orgasm keep going far past the point I knew possible; it feels like she’s borderline showing off as she wrings my cock for the most messy and powerful orgasm she possibly can."
        "I could swear her toned belly almost distends from the amount of cum unloaded inside her; if anything, my balls feel lighter, that’s for sure."
        show augusta cowgirl6 with dissolve
        stop ambience fadeout 2.0
        stop music fadeout 5.0
        "Eventually she slows down, only letting my cock go at the moment the discomfort from sensitivity overrides the feeling of pleasure."
        augusta "Mmphh… And here’s the dessert, dearie…"
        "Even now, Augusta is a stickler for the obscene as she rises her rear slightly and allows me to watch the waterfall of whiteness drip from her thigh-gap."
        scene bg churchroom with dissolve
        play ambience ambienceday fadein 3.0
        "Although she doesn’t remain in place for too long as she crashes onto the sofa, idly rubbing her pussy while catching her breath with an expression of pure satisfaction."
        show augusta satisfied with dissolve
        augusta "Usually I tailor my technique in sex to the species, but I wasn’t quite sure how to deal with you, so I just used my usual stallion method."
        augusta "Stallions usually cum too fast, so I spend eighty percent of the time going slowly and driving them wild with pleasure, before the explosive finish."
        augusta "But you? Oh fuck, I actually came first… Ah-ha! That’s not supposed to happen, hehehe…"
        mc "Yeah, I last a little longer than your contemporaries, usually a pleasant surprise for the mares."
        show augusta happy with dissolve
        play music day2 fadein 10.0
        augusta "Ah-ha… Thing is, due to my role, I actually share your pleasure too… So, you made me orgasm once, and when that ended you had your orgasm causing me to orgasm again…"
        show augusta laughing with dissolve
        augusta "So I had an orgasm for like… an entire minute. That’s bad for my heart, dude. Ah-ha!"
        mc "You’re telling me, you almost made me black out from the pleasure."
        show augusta happy with dissolve
        augusta "Alright, I fuckin’ admit it, I was showing off because you’re from another universe… But you’re definitely no virgin, ahh… hahaaa… Phew…"
        show augusta satisfied with dissolve
        augusta "Maybe I should just take today off and chill out…"
        show augusta angry with dissolve
        augusta "Mmm… Nah! I have important work to do."
        "Augusta tries to bounce up off the sofa, however her quivering thighs almost give out."
        show augusta laughing with dissolve
        augusta "Grrr… You were a formidable foe, [playername]. However, next time, it’ll be I who is victorious!"
        mc "Yeah yeah, you’re all talk, ‘goddess of love’!"
        show augusta happy with dissolve
        augusta "Hmph, you’ve got some pep. I wonder if Aurora would still be pissed if I offered to make you a priest…"
        augusta "I mean, is that something you’d want? You could come here and work with a few customers; a man with your stamina could outperform a lot of the priests, especially with some milk supplements."
        mc "I’ll think about it… Becoming an isekai prostitute wasn’t exactly a dream of mine."
        show augusta satisfied with dissolve
        augusta "Ahh, you still have some deeply ingrained biases. If you’re that fussy, just come here and fuck me instead! I need to study your anthropology and entomology so I can give you the best sexual service possible."
        hide augusta with dissolve
        "Is that something she does with all species? I guess it’s lucky that I’m the only person in this entire species."
        "That explains the titles for the books on her bookshelves."
        "Ultimate Guide to Pleasuring Stallions 25th edition – Princess Augusta, Princess Ophelia."
        "Ultimate Guide to Pleasuring Lupines 10th edition – Princess Augusta."
        "Ultimate Guide to… eh? What’s a gastropod? Wait, what the fuck?"
        show augusta happy with dissolve
        augusta "Heh, I see you’re eyeing up the books. I doubt I’ll release a book on you; however, these books are only secondary to my passion for the study of anthropological mating habits."
        augusta "I failed to tell you this earlier, but if you come and work here, I want to watch you, and maybe even participate!"
        mc "Sheesh, you’re a real handful Augusta, a real damn handful."
        show augusta laughing with dissolve
        augusta "Ah-ha, I see the wisdom from the eye of infinity has unsealed! Come forth my reign of lust and consume the lands! Ah-hahaha!"
        mc "Alright, I’m leaving, bye-bye."
        show augusta sad with dissolve
        augusta "Ah- I was just kidding! Do come back!"
        menu:
            "Fine, I’ll help you study… 'me'.":
                show augusta laughing with dissolve
                augusta "Ah-ha, perfect! Here’s the regime I concocted for us last night."
                "Regime?!"
                show augusta happy with dissolve
                augusta "I’d like to see you perform at least three more acts on a mare, and I’ll pay you 25 monies for each."
                show augusta satisfied with dissolve
                if auma == 1:
                    augusta "You masturbated while watching earlier, that was very interesting. Try participating next time, though!"
                elif autrain == 1:
                    augusta "That little sex train was a fun experiment! Let's try you on the girl next time."
                elif audp == 1:
                    augusta "You wasted no time sticking it up that mare's butt. You're a brave soul, [playername]. Let's try another mare, another hole next time."
                elif auvaginal == 1:
                    augusta "You easily bested the quality of sex that most of my priests offer when you fucked that mare earlier..."
                    augusta "But I bet you can do more than just that."
                show augusta happy with dissolve
                augusta "Ideally I’d like a good diversity of acts too, so I may participate to aid that cause."
                mc "What do I get for participating in all of your  little 'experiments'?"
                show augusta neutral with dissolve
                augusta "Well, uhh... Maybe a free book?"
                mc "No reward, then?"
                show augusta laughing with dissolve
                augusta "As they say, the journey is the real reward! Ah-ha!"
                mc "Fiiinee… But don’t expect my undying devotion to the cause."
            "Mmm… maybe…":
                show augusta laughing with dissolve
                augusta "Maybe is better than no! Ah-ha, I the goddess of love will lure you in with the promise of more lustful acts!"
        show augusta happy with dissolve
        augusta "You seem unmotivated, however! Perhaps now you’re simply enjoying a post-coital/post-masturbatory absence of primal thoughts, but within the next few days you’ll come crawling back."
        mc "Do you have any idea how many times I have sex a week? By Aurora, maybe I should be the god of love."
        show augusta angry with dissolve
        augusta "Eh?! How often?!"
        mc "... Uhhmm... Like... More than you."
        show augusta neutral with dissolve
        augusta "You really are tough competition… I’ll have to do something about this, hmm!"
        hide augusta with dissolve
        "With simply a passive wave, Augusta leaves the room and returns downstairs."
        "I hope she doesn’t try to snuff me the next time we have sex. There are a lot of things I'm willing to try, but not that."
        "Wait, more importantly… Why the hell did she just leave me in her house?"
        "Wait, is that more important? My priorities are all off today. Her eccentricity has fried my brain circuits."
        show augusta laughing with dissolve
        augusta "Oh! Shiit, I totally just left you in my living room, didn't I?"
        augusta "Allow me to show you out, [playername], my bad, ah-ha!"
        scene bg black with dissolve

        "Later that evening..."
        jump evening
