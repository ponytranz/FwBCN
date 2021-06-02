label forest:
    $ forestvisits += 1
    if forestvisits == 1:
        $ monies += 35
        $ forestvisit1 = 1
        jump forestvisit1
    elif forestvisits == 2:
        $ monies += 35
        $ forestvisit2 = 1
        jump forestvisit2
    else:
        $ forestvisit3 = 1
        jump buttersmenu
label forestvisit1:
    stop music fadeout 0.5
    play music hopelessness
    pause 0.5
    "There’s a mysterious girl living in the forest, and I can go work with her."
    "What could possibly go wrong? Other than the fact I might get lost on the way there."
    show bg foresthouseexterior with dissolve
    "Thankfully, there’s a fairly explicit path that leads me surprisingly deep through the woods, and straight to a clearing with a beautiful cottage in the middle."
    "As I make my way up to the cottage’s door, I scout out the surroundings and see nothing out of the ordinary. And nothing that would suggest what kind of work I’ll be doing here."
    "There's just a lot of plants, flowers and foliage. Am I going to be gardening?"
    "I knock on the door of the cottage and I can momentarily hear some footsteps inside getting closer, but then all goes quiet."
    "All of the windows are covered with curtains, but I can’t shake the feeling I’m being observed right now."
    "That worry is soon alleviated when the door gently opens ajar, and a meek mare peeks through the crack."
    play music butters fadeout 30.0
    "Her eyes initially squint at me, before widening. She then opens the door all the way and greets me with a smile."
    show butters dresslaughing with dissolve
    butters "Oh me, oh my, what an adorable animal. I haven’t seen a creature such as yourself before."
    "To my bewilderment, this mare is wearing beautiful and extravagant clothing, almost completely covering her furry body."
    "I’ve never felt so naked as I do right now."
    show butters dresshappy with dissolve
    butters "Do come in to my wonderous home, all animals of the forest are more than welcome."
    mc "Animal? I’m not… I mean, I technically am, but…"
    show butters dresssurprised with dissolve
    butters "Oh my, you can talk my language? You must be really intelligent, how exciting!"
    "While these compliments are heartwarming, I can't help but feel somewhat patronised."
    hide butters with dissolve
    show bg buttershouse with dissolve
    "I take a step inside of her home, the cottage looks even more beautiful from the inside, it’s finely decorated and well-kept."
    "Each room is full of seemingly rare trinkets and shiny baubles that would make even the most dedicated collectors jealous."
    "What's more is there's an adorable snow-white bunny scooting around on the floor, seemingly running away from me because I'm a stranger."
    "Wait, the bunny is an actual bunny, does that mean there are no anthropomorphic bunnies? Or does this mean there are actual four-legged ponies?"
    "I realize I’m lost in thought as Butters leans over to peek at me from the side."
    show butters closedresslaughing with dissolve
    butters "Do you like my pet bunny? She’s called Devil because she’s a naughty lil’ devil."
    mc "Ohh, what a ‘unique’ name..."
    "Unique was the nicest thing I could think of saying, the name has me a tad disappointed. I was hoping it’d be called fluffy, or something normal."
    show butters closedressneutral with dissolve
    butters "I’m sorry for my initial wariness, I thought you may be another pesky pony."
    mc "Pesky pony? Nah, I’m a full-blooded human."
    show butters closedressneutral with dissolve
    butters "Ohhh, a hue-man!"
    butters "I have no idea what one of those is."
    show butters closedresshappy with dissolve
    butters "Is it like the word hue, and man combined? Are there different coloured hue-men?"
    mc "I’ll praise your intuition, but I’m afraid it’s H U man, not H U E man."
    mc "Anyway, what’s so pesky about ponies? Aren't you a pony?"
    show butters closedressneutral with dissolve
    butters "Hehe, I guess I am? I dunno mister, ponies overwhelm me."
    show butters closedresssad with dissolve
    butters "I don't really like them, I prefer to be around animals."
    "She taps the tips of her index fingers together; I wonder if this is the shyness that Moxie mentioned."
    "Shyness turned into loneliness, turned into resentment perhaps. Not an unlikely situation."
    mc "I’ll be honest, I’m not a woodland animal, I live with the ponies in the suburbs."
    show butters closedresssurprised with dissolve
    butters "Oh blue skies! You’re one of them too?"
    show butters dresssad with dissolve
    "She shrinks into herself, her body language becoming defensive and timid."
    "Maybe I should have kept up the animal charade."
    menu:
        "Just kidding, I’m actually an animal.":
            butters "Oh? I mean we’re all animals I guess…"
            "Crap, she’s onto me."
            show butters dressneutral with dissolve
            butters "I was just hoping you wouldn’t associate with those pony types."
            mc "I wouldn’t say I particularly associate with them, I barely know them."
            butters "Ohh, you’re different?"
            mc "I guess so. What about you?"
            show butters dresshappy with dissolve
            butters "I’m different too! People like you and me need to look after each other."
        "I’m new to Arcadia, before I came here, I have never seen an anthropomorphic pony before.":
            show butters dressneutral with dissolve
            butters "Ohh, so you’re not like them?"
            mc "I am in some ways, but different in others, you’ll have to get to know me."
            show butters dresshappy with dissolve
            butters "Hmm, I see… This poses some interesting possibilities."
            show butters dresssurprised with dissolve
            butters "Can you do magic?"
            mc "Magic? I’m afraid not, I didn’t even know it existed until I got to Arcadia."
            show butters dresshappy with dissolve
            butters "Fiddlesticks, just my luck."
    butters "Uhm, pardon my asking, but what kind of creature is a human?"
    mc "I’ve never really thought about it, an evolved primate I guess."
    show butters dresshappy with dissolve
    butters "Ohh... Like, a monkey?"
    mc "Well, not really a monkey... But humans are a little different to the bipedal ponies around here."
    mc "I don’t have any fur, my species has a 50/50 gender split, we don’t go into heat, and there are subtle anatomy differences here and there."
    if barvisit1 == 1:
        mc "If Riku is any comparison, humans are definitely not as strong as ponies are."
        "Makes sense considering how strong horses and ponies are in my world."
    show butters closedresslaughing with dissolve
    "The clothed mare breathes a sigh of relief, once again closing the distance between us as she looks over my nude body while smiling."
    show butters closedresssurprised with dissolve
    butters "Ohh, nature is fascinating, I wonder what evolutionary niche you have."
    mc "Niche? What like?"
    show butters closedresshappy with dissolve
    butters "All ponies are strong, unicorns can cast magic, pegasi and dragons can fly, neko have incredible agility, et cetera."
    "I guess the niche of human’s would be intelligence, but that is more or less lost in a world of anthropomorphs."
    "Even if humans are more intelligent, I am far from the pinnacle of that mantra."
    mc "Can I ask you a question? You seem quite knowledgeable"
    show butters closedresslaughing with dissolve
    butters "Ask away, my little human companion."
    mc "Oh, by the way, my name is [playername]."
    show butters closedresshappy with dissolve
    butters "Hehe, I was starting to think you didn’t have a name. I'm Butters."
    mc "So, you have a cute bunny that hops around on all fours... I was wondering if there were anthropomorphic bunnies in this world too?"
    butters "Indeed there are, the path of evolution split somewhere along the line."
    "Interesting, I think chimpanzees fulfill that role for humans."
    mc "Does that mean there are four legged ponies too? I haven’t seen any."
    show butters closedresssurprised with dissolve
    butters "You mean a horse?"
    mc "A horse? Oooohhhh… That's what you call them? Explains why Moxie got offended when I called her a horse."
    show butters closedressneutral with dissolve
    butters "Heheh, duhh."
    mc "Anyway, enough expository banter, I came here to work."
    show butters closedresslaughing with dissolve
    butters "You sure you don’t want tummy rubs and treats?"
    mc "Is that an option?"
    show butters closedresshappy with dissolve
    butters "I was just about to give Devil hers; you can join in if you’d like."
    menu forestvisitmenu1:
        "Tummy rubs and treats pls":
            "Butters takes out a bag of mixed leafy greens. My disappointment grows as I realize I probably won’t enjoy the same kind of treats as a bunny."
            show butters closedresslaughing with dissolve
            butters "Here you go, tasty leaves!"
            mc "Actually, I think I’ll pass on the greens."
            show butters closedressneutral with dissolve
            butters "Ohh, okay. Sorry mister, I don't know what humans like to eat."
            "She nibbles on the leaf she was just offering to me, before placing some in a bowl which Devil readily starts to munch."
            show butters closedresslaughing with dissolve
            butters "Time for tummy rubs."
            "Her hand starts to innocently wave up and down on my tummy."
            butters "Is this good?"
            "She wears soft fabric gloves, and her touch is delicate, resulting in a comfortable sensation."
            mc "That feels really nice."
            "She speeds up and adds some gentle scratches into the mix."
            show butters closedresshappy with dissolve
            butters "There we go, good boy."
            mc "Ohhh, that's the stuff. I can see why pets love this."
            "She then moves onto Devil who readily nuzzles into her hand."
            "I could get used to being coddled here."
            jump forestvisitmenu1
        "Penelope sent me to work.":
            show butters closedresssurprised with dissolve
            butters "Ohh me oh my, you’re that guy."
            show butters closedressneutral with dissolve
            butters "I'm lucky to have the perfect worker show up at a time like this."
    butters "I'm sorry I mistook you for an animal at first."
    menu forestvisitmenu2:
        "I’m serious, you can treat me like a pet, this is nice.":
            show butters closedresslaughing with dissolve
            butters "Okay, mister, you’ll be a good boy and work for me then?"
            mc "Yeah, I sure will, what do you have in store for me?"
            jump forestvisitmenu2
        "What kind of work will I be doing here?":
            show butters closedresshappy with dissolve
            butters "I’m an alchemist, and I’m searching for some essential ingredients for my most important potion yet."
            butters "I've been waiting to hire someone special for a while, and you seem like the right man for the job."
            "She probably means she's been waiting to hire someone that isn't a pony."
            butters "There are several ingredients I require that we can only get by exploring hazardous caves."
    mc "What are those?"
    show butters dresshappy with dissolve
    "She walks over to a pinboard full of writings and notes. It's enough that you'd assume she's writing a thesis, it's almost manic."
    butters "I need gelatine from a slime monster for a transmorphation potion, leaf clippings from a folium polypus, and a full Dewblossom."
    label forestvisit1choice1:
        menu:
            "Slime monster?":
                mc "Sounds scary, are they dangerous?"
                butters "Not particularly, although it can be problematic if they try to put slime inside you."
                mc "Inside you? What?"
                show butters dresshorny with dissolve
                butters "That’s one of the best ways to get gelatine though, keep an eye out for me."
                mc "Uhh, okay?"
                jump forestvisit1choice1
            "Folium Polypus?":
                show butters dressneutral with dissolve
                butters "Spooky living plants with many writhing, wriggling vines."
                butters "In scary books, they allegedly trap creatures with the vines until they rot and turn into nutrients for the plant."
                mc "That’s utterly terrifying."
                show butters dresshappy with dissolve
                butters "Hehe, it is, isn’t it?"
                butters "Fortunately, these plants are just that, plants! You can easily snap the vines and walk away. The only ‘nutrients’ it’ll ever get is from tiny bugs."
                mc "Oooohhhh, it’s like a Venus fly trap."
                show butters dresslaughing with dissolve
                butters "Yeah! Penis fly traps, you're right! "
                "What."
                show butters dresshappy with dissolve
                butters "The Folium Polypus tries to suck fluid out of larger creatures, so it may try to force its vines into your orifices."
                mc "Okay, it just got terrifying again."
                butters "It’s okay [playername], it’s just a plant!"
                jump forestvisit1choice1
            "Dewblossom?":
                show butters dresshappy with dissolve
                butters "They’re a unique flower that wards off evil, they only grow in cold and moist locations, as long as the sun shines on it."
                mc "Doesn’t seem too bad."
                mc "I’ve never been spelunking before, but it should be okay if we’re prepared, right?"
                show butters dresslaughing with dissolve
                butters "Of course, everything will be just fine. I’ll look after you."
                jump forestvisit1choice1
            "What do you need those for? (Conclude)":
                show butters dresshappy with dissolve
                butters "You know that unicorns can cast magic, right?"
    mc "Yeah, not quite sure how or why though."
    butters "Wouldn’t it be exciting if you could do magic without having a horn?"
    mc "That would be dope."
    show butters dressneutral with dissolve
    butters "D-Dope…?"
    mc "I meant to say delightful, my bad."
    show butters dresshappy with dissolve
    butters "Delightful!"
    butters "With a pinch of unicorn dust and some relevant alchemical ingredients, you can cast spells too!"
    butters "Unicorns can use their brains to think of the magic spell they want. For us, ingredients are necessary to direct the power of the spell."
    butters "A lot of trial and error is required, but I think I’m onto something big!"
    label forestvisit1choice2:
    menu:
        "I need to ask, what is unicorn dust?":
            show butters dressneutral with dissolve
            butters "Why are you pulling that face? It’s nothing bad!"
            butters "When a unicorn casts a spell, you see a poof that correlates to their eye colour, right? There’s always a small amount of dust that is usually lost to the wind."
            "She does a dramatic explosion motion by waving her arms."
            show butters dresshappy with dissolve
            butters "It has been recently discovered, and I've known for even longer, a tiny amount of that can be harnessed for real alchemy."
            mc "Phew, ‘unicorn dust,’ okay."
            jump forestvisit1choice2
        "What kind of potion are you trying to brew?":
            butters "I’m experimenting with transformations right now; I can’t say too much, because it would be embarrassing when nothing happens."
            butters "What I do know is that slime gelatine has a unique amorphous property that allows it to take any shape."
            butters "This results in transformational magic."
            mc "Transformation? Like gender changing magic?"
            show butters dresslaughing with dissolve
            butters "Yeah! You sure know your stuff."
            show butters dresshappy with dissolve
            butters "I’m hoping the folium polypus and dewblossom have the right transformational result."
            "Leaves from a raping tentacle plant and a moist flower, what the heck is that going to turn you into? A tree?"
            jump forestvisit1choice2
        "Is there any difference between alchemy and magic?":
            show butters dresssatisfied with dissolve
            butters "Subtle differences, most alchemy takes the form of potions which can be used at any time."
            show butters dresshappy with dissolve
            butters "All you need is a sip and at any time you can have the effects. And they last longer, because the ingredients and unicorn dust take time to digest through the body."
            butters "You could say, it’s more potent and powerful because of this."
            show butters dressneutral with dissolve
            butters "Sometimes too powerful, the body can absorb the effects of the ingredients, and they uhh…"
            butters "’Stick’."
            "Her trepidation around her description suggests a deeper history, especially with the amount of trial and error this girl must have done."
            "Who knows what she's seen and done when trying out random potions?"
            mc "Are you saying the effects can be permanent?"
            butters "Sometimes, yes."
            mc "From what I’ve heard, that sounds rather illegal…"
            show butters dresshappy with dissolve
            butters "Ehehe, kinda, but alchemy is so out of public knowledge there are no laws!"
            butters "If no one knows about it, there's no harm in it."
            mc "How do you know about it?"
            show butters dresslaughing with dissolve
            butters "Top secret."
            "She says that with a playful tone, like she definitely doesn’t want to talk about it, but there’s something interesting to be discovered here."
            jump forestvisit1choice2
        "Sounds exciting, I’m in. (Conclude)":
            show butters dresslaughing with dissolve
            butters "Wonderful, I’m so excited to be working with someone on my cave trip."
    show butters dresshappy with dissolve
    butters "I’ll pay you well if we get everything. It’ll take almost all day, so it’s the least you deserve for being such a helpful human."
    mc "Aren’t you worried about working with a male all day? Y'know, because of heat."
    if days >= 6:
        "There have been a few occasions where I’ve worked with mares that have been distracted by their heat now, it’ll probably be the same with Butters."
    butters "Heat? Is it that time of year already? I didn't even realize..."
    mc "You're not in heat?"
    show butters dresslaughing with dissolve
    butters "Me? No worries, we can work all day and I’ll be just fine. I appreciate your concern."
    "Maybe she’s older than she looks, ponies seem to age really well since fur hides their wrinkles."
    "Still, Butters does look young... Maybe she’s just finished her heat, or it hasn’t started."
    butters "Oh, one more thing before we head out. I'm going to get a change of clothes."
    hide butters with dissolve
    "She picks up a knapsack and nods to me before going to change in another room."
    show bg black with dissolve
    show bg buttershouse with dissolve
    show butters robehappy with dissolve
    "After a few minutes, she comes out still well clothed, although this time her cleavage is a little more loose due to the lack of a bra."
    "Her new clothes definitely show their wear; they're frayed, dirtied and ripped."
    butters "Ready [playername]?"
    mc "Are we leaving already? Don’t I need anything? Armour, weapon, healing potions?"
    show butters robelaughing with dissolve
    butters "I don’t think so, we’re just tackling some slimy gals and plants. It’s not like we’re going minotaur hunting again."
    "’Again’, I shudder."
    scene bg black with dissolve
    stop music fadeout  3.0
    stop ambience fadeout 3.0
    "..."
    show bg farm2 with dissolve
    "The two of us head out through the forest, me butt naked and Butters clad in her ripped robes."
    "In the end, all we brought was a lantern."
    show bg caveentrance with dissolve
    play ambience ambiencecave fadein 3.0
    "Eventually we reach a cave entrance, this must be where the fun begins."
    show butters robeneutral with dissolve
    butters "Okay, once we head inside everything will be different, caves are wild and untamed compared to the forest."
    butters "You’ll have to keep an eye and an ear out."
    mc "Really wish I had some clothes, and maybe a long pointy stick right now."
    show butters robehappy with dissolve
    butters "Oh bless you, animals don’t wear clothes, so don’t worry about it."
    show bg cave with dissolve
    show butters robeneutral with dissolve
    "We take cautious steps through the cave, illuminated by Butters’ lantern."
    "Our concern is mostly the environment and terrain rather than a scary monster."
    butters "Watch your footing, especially in the rockier areas."
    "Even though I've gotten used to walking around barefoot, walking over the cold, hard rocks is very uncomfortable. Unlike the surprisingly agile Butters, I don't have the liberty of a protective fur coat on my soles."
    mc "Shine your lantern this way for a moment."
    show butters robehappy with dissolve
    butters "I got you."
    "The surface of the cave is natural and rocky, carelessness would make it easy to trip."
    "The two of us try to stay as silent as possible, the hollow caves cause even the lightest of sounds to reverberate across multiple passages."
    butters "We won't go too deep, slimes often congregate near water sources and there's one near here."
    mc "Slimes, plural?"
    butters "Hopefully we'll be able to single one out. Easier to deal with that way."
    "This is certainly a unique adventure, I have faith that Butters is experienced and knows what she's doing."
    "But there's still so much I don't know about this world. I hope Butters acknowledges the extent of my naivety."
    show bg cave2 with dissolve
    "Eventually walking through the stalactites and stalagmites of tight limestone caverns, we enter a more open area with metamorphic rocks that seems to have been carved out by people."
    butters "This is a long abandoned mine nature has overtaken, and now it's almost imperceptible to the traditionally formed caverns."
    hide butters with dissolve
    "I take a moment to look around and appreciate the vastness of this cave, it's as if the entire world were hollow from where I stand."
    "We carefully navigate around the perimeter of a dark chasm, weaving between halls and overhangs."
    show bg cavepool with dissolve
    "Eventually we enter a calming room with a pool."
    "But before we enter, Butters immediately hushes and pushes me behind a nearby rock where we both kneel and hide."
    "What is it, what has she seen?"
    "I daren’t ask, I don’t want to make any noise."
    label buttersandslime:
        pass
    show butters closerobeangry with dissolve:
        xpos -400
        ypos 50
    "Butters points up at the roof of the cavern. A few meters before the blue underground lake, there’s something writhing."
    play music danger fadein 3.0
    show basicslime with dissolve:
        xpos 700
        ypos 0
    "It’s a slime monster; curses, how could I have missed that?"
    "No doubt it hunts by falling on top of unwary creatures."
    "If it wasn't for Butters's experience I would have been easy prey."
    "How are we going to deal with this situation?"
    menu:
        "Perception Check.":
            "I squint my eyes at the slime thing, it really is just a gelatinous blob. Does it have a face? I can’t quite make it out."
            "How does it sense us? Can it hear us? I think it has eyes, but it probably can't hear us talking."
            "It’s about 8ft away from us, and the roof is about 7ft up, meaning I could barely reach it if I tried."
            "It doesn’t seem to be aware we’re here. It’s not moving."
            "I listen closely and I can’t hear anything from it, it’s quite a stealthy creature."
            mc "We need to lure it down and level the playing field."
        "Ask Butters.":
            mc "Psst, what are we going to do?"
            butters "We need to coax it down somehow, and then grab a glob of its slime."
            mc "Grab? Like rip off a piece?"
            butters "Yeah, hit and run. Both risky procedures, we can’t let it fall on us, and we can’t let it suck us in."
            butters "There's no point in taking any risks, we should try and catch her by surprise."
        "Intelligence Check.":
            "How would a slime work biologically?"
            "It must be able to detect temperature, perhaps even movement."
            "That's how it gets the drop on people, it reacts to movement below it, not sight or hearing."
            "We can outsmart it by standing still or moving very slowly."
            butters "I can’t reach it, I’m too small, what should we do?"
            mc "I think if we throw some rocks at it, it should cause the slime to fall down and we'll have an even playing field."
    "We need to get the slime down, but how?"
    menu:
        "Throw rocks":
            show butters closerobeneutral with dissolve
            butters "Ohh, great idea."
            "We scour the ground for a few small rocks; we get two each and then move out of cover."
            butters "I feel a little bit mean about this. I hope it's not animal abuse."
            mc "Isn’t stealing its gelatine animal abuse? Are we really going to draw the line here?"
            show butters closerobesad with dissolve
            butters "Oohh, I’m such a hypocrite."
            play sound knock
            "Butters tosses her first rock, she throws it overarm and it readily donks in the cave wall, missing the slime by a wide margin."
            "Her shot was so haphazard the slime doesn't even react."
            butters "Ah? I'm sorry [playername]... I have terrible coordination."
            menu:
                "Throw the rock underarm.":
                    "If I do this underarm it’ll have less power, but there’s a higher chance for me to hit it considering the slime’s position on the roof."
                    play sound knock
                    "I take a few seconds to line up my shot before tossing the rock."
                    "Direct hit!"
                    "To my surprise, it doesn’t bash the slime at all. The rock casually sinks into it, before it gets spat back out with disgust. The rock pathetically clacks on the ground below it."
                    mc "Ah, it didn’t work?"
                    show butters closerobesurprised with dissolve
                    butters "No wait, look!"
                    hide basicslime with easeoutbottom
                    "The slime starts to drop down, falling onto the ground. Perfect, that’s the first problem solved."
                    jump forestvisit1slimedropsuccess
                "Throw the rock overarm.":
                    play sound knock
                    "With as much power as I can, I toss the rock at the slime."
                    "However, the roof is too low, and with the slime being on the roof, I miss."
                    show butters closerobeneutral with dissolve
                    butters "Ohh bother, here let me try again."
                    "She starts to wind up another shot, this time she’s taking her time and throwing underarm."
                    "As she throws the rock, she narrowly misses, but she did much better than last time."
            menu:
                "Throw another rock underarm":
                    "If I do this underarm it’ll have less power, but there’s a higher chance for me to hit it considering the slime’s position on the roof."
                    play sound knock
                    "I take a few seconds to line up my shot before tossing the rock."
                    "Direct hit!"
                    "To my surprise, it doesn’t bash the slime at all. The rock casually sinks into it, before it gets spat back out with disgust. The rock pathetically clacks on the ground below it."
                    mc "Ah, it didn’t work?"
                    show butters closerobesurprised with dissolve
                    butters "No wait, look!"
                    hide basicslime with easeoutbottom
                    "The slime starts to drop down, falling onto the ground. Perfect, that’s the first problem solved."
                    jump forestvisit1slimedropsuccess
                "Throw another rock overarm":
                    play sound knock
                    "I line up another powerful shot and sling the rock towards the slime, it hits the roof adjacent to the slime with a clink, it misses but the slime reacts!"
                    "Wait, what is it doing?"
                    butters "Uwah, it’s crawling this way menacingly!"
                    "It crawls towards us from the roof and it’s surprisingly fast, there isn’t enough time to pick up some more stones."
                    jump forestvisit1slimedropfail
        "Use Butters as bait":
            show butters closerobeneutral with dissolve
            butters "Use me as bait? Could be worth trying."
            hide butters with dissolve
            show butters closerobeneutral with dissolve:
                xpos 0
                ypos 100
            "She pops down her knapsack next to me and meekly tiptoes her way near the slime."
            butters  "Excuse me slime! Get down here!"
            "I can’t tell if the slime has reacted to her or not yet."
            "Wait, it’s moving, it's about to drop!"
            mc "Get ready to dash out of the way."
            butters "Got it!"
            show butters closerobeangry with dissolve:
                xpos -100
                ypos 100
            "She did it, she dashed out of the way- but...!"
            jump forestvisit1slimedropfail
    label forestvisit1slimedropfail:
        play sound move
        hide basicslime with hpunch
        hide butters with easeoutbottom
        "To our shock, the slime displays a surprising amount of agility as it launches itself off the roof at an angle, managing to encapsulate Butters’ face in a slimy grip."
        "Butters falls to the ground desperately clinging at the slime on her head trying to toss it off, all to no avail."
        butters "Mmphhh mphhh- ish trying to mate with me!"
        "And then, something I absolutely couldn't have predicted happens."
        show slimegirl with dissolve
        "The slime fully forms into a female figure."
        slime "Keheh, I don't appreciate being woken up like that."
        show butters closerobeangry with dissolve:
            xpos -200
            ypos 400
        butters "G-Get off of me! I won't let you slime me."
        slime "But you look like a great place to lay some slime, kehehe."
        mc "Oh fuck, what do I do?"
        butters "Whatever you do, don't touch it!"
        "If I touch it, it’ll suck me in too. There may genuinely be nothing I can do right now to help Butters, except sit and watch it mate with her."
        jump forestvisit1slimesex
    label forestvisit1slimedropsuccess:
        show butters robeangry with dissolve:
            xpos -200
            ypos 50
        "The slime may have dropped, but now it’s very aware of us. It’s slowly crawling towards us, we have the advantage now that it’s grounded."
    "And then, something I absolutely couldn't have predicted happens."
    show slimegirl with dissolve:
        xpos 700
        ypos 250
    slime "Keheh, I don't appreciate being woken up like that."
    butters "Easy now miss slime, we just need to get some gelatine."
    slime "Mmm, I bet you're a great place to lay some slime, kehehe."
    hide slimegirl with None
    show slimegirl with dissolve:
        xpos 650
        ypos 250
    show butters robesurprised with dissolve
    butters "Uuh, no miss slime! Please stop."
    hide slimegirl with None
    show slimegirl with dissolve:
        xpos 600
        ypos 250
    slime "Come on little pony, I won't bite..."
    "It gradually closes the gap, specifically with her eyes on Butters."
    label forestvisit1choice3:
        $ time = 5
        $ timer_range = 5
        $ timer_jump = "forestvisit1slimepresex"
        show screen countdown
        menu:
            "Try and grab some gelatine quickly.":
                hide screen countdown
                "If I’m quick, it shouldn’t be able to react. The creature seems rather slow anyway."
                "I kneel over near it and get as still as possible, preparing myself to grab when it gets close."
                show slimegirl with dissolve:
                    xpos 550
                    ypos 250
                "Butters notices what I’m doing and tries to distract it, it works! It’s moving towards her now, I should have a chance."
                show slimegirl with dissolve:
                    xpos 500
                    ypos 250
                "Now!"
                "I shove my hand into the slimy creature and I clamp my hand into a fist to grab some gelatine, before trying to pull back."
                "What the? It’s thick. It’s sticky! My fist is stuck?"
                "Damnit, of course this slime is super sticky, how else was it able to stick on the roof?"
                slime "Uwaahh, a mating volunteer? Kehehe."
                "It's trying to suck me in, it feels so gross!"
                hide slimegirl with None
                show butters closerobeangry with dissolve
                butters "No! I won’t let my new friend get slimed!"
                hide butters with hpunch
                mc "Huh? Ahh!"
                play sound move
                "Butters tackles me, causing me to fall back, my hand released."
                "We did it, I have some gelatine in my fist, but as I regain my composure and look back…"
                "The tackle caused Butters to practically land in the slime and it quickly enveloped her."
                jump forestvisit1slimesex
            "Try to trap it in the knapsack.":
                hide screen countdown
                show butters robesurprised with dissolve
                butters "In my knapsack?"
                butters "There’s no way it’ll fit, that won’t work!"
                show butters robeangry with dissolve
                butters "Anyway, even if we do get it in the bag, then what?"
                "She has a point. The two of us back away as it approaches, what are we going to do?"
                jump forestvisit1choice3
            "Beat it up!":
                hide screen countdown
                mc "Butters, do you have anything we can whack it with?"
                show butters robesurprised with dissolve
                butters "Whack it? Are you kidding? That’s so mean!"
                mc "Now’s not the time to squabble about ethics, it wants to lay eggs in you!"
                butters "They don’t do that!"
                show slimegirl with dissolve:
                    xpos 550
                    ypos 250
                slime "Come 'ere sexy, let me fill those holes of yours."
                show butters robeangry with dissolve
                butters "Eugh, fine, I was going to use this to cut some leaves off."
                "From the knapsack she gets out a small box cutting knife."
                "What is she supposed to do with that tiny thing?"
                "She kneels down and prepares the tiny knife, I quickly get behind her."
                "As the slime approaches, she quickly launches a few rapid jabs. To my surprise she’s quite deft with the knife, slicing and dicing the poor slime."
                "The slime is initially damaged; it momentarily falls back."
                hide slimegirl with easeoutbottom
                mc "You did it!"
                butters "Miss slime, today my 'holes' stay intact, you got that?"
                show slimegirl with dissolve:
                    xpos 500
                    ypos 250
                "However, the cuts in the slime reform, it’s clear it took no actual damage. If anything it just pissed the slime off."
                slime "I was gonna be gentle, but... Now I'm totally gonna put it in your ass as well."
                show slimegirl with dissolve:
                    xpos 400
                    ypos 250
                butters "Uwah, my attacks have no effect, it’s invincible!"
                play sound move
                hide slimegirl with easeoutleft
                hide butters with hpunch
                "In our disbelief, the angry slime launches itself at Butters causing her to fall back, and hence knock me back as I’m behind her."
                "I quickly scurry to my feet, but it’s too late."
                jump forestvisit1slimesex
    label forestvisit1slimepresex:
        show slimegirl with dissolve:
            xpos 500
            ypos 250
        show slimegirl with dissolve:
            xpos 400
            ypos 250
        show slimegirl with dissolve:
            xpos 300
            ypos 250
        scene bg black with dissolve
        stop music fadeout 3.0
        butters "Aaah!"
        "Unable to come up with a plan, the slime catches Butters in a sticky grip."
    label forestvisit1slimesex:
        stop music fadeout 3.0
        scene bg black with dissolve
        "..."
    play music sex1 fadein 3.0
    show bg cavepool with dissolve
    show butters slimesex1 with dissolve
    butters "Kyaaa, my clothes! It’s pushing them apart!"
    butters "At least let me keep my decency while you molest me in front of my new friend!"
    slime "But your boobies are so cute, let them breathe! Kehe..."
    "The slime encapsulates Butters,  her head and extremities limply wiggling outside the slimy mass."
    mc "Uhm, what do I do?"
    butters "Ahhh, j-just keep watch for danger, I'll handle the slime!"
    "Uhh, okay, I'll keep watch?"
    "Her blouse gradually comes undone, revealing her plump breasts which the slime plays with using make-shift gelatinous hands."
    "Her skirt lifts too, as a coil of slime forms and prepares to mate with its victim."
    slime "What a perfect mate, you and me are going to have lots of fun."
    butters "Mmphh, maybe this won't be so bad, it's not my first time with a slime..."
    mc "You never told me that!"
    butters "You weren't supposed to know!"
    show butters slimesex2 with dissolve
    "A phallus shaped coil of slime applies pressure to her pussy; I can see her skin indenting as it slips inside like a viscous liquid."
    play ambience sex fadein 5.0
    butters "Ahh, it just went inside! Oh gosh, it's so thick, it's really filling me up... Mmphh, ahh!"
    "The slime writhes and wiggles as it starts to push itself inside while occasionally kissing Butters on the lips."
    slime "I told you I'd make it feel good, my delicious mate."
    butters "Mmmphhh, but mating with a slime in front of my new human friend... it's too embarrassing!"
    "She tries to hide her face, but her arms are held back inside the feminine slime creature."
    slime "Maybe you should ask him to join you, kehehe."
    mc "Should I run and go get help, Butters?"
    butters "Ahhh! J-Just wait for it to cum inside me, we can collect the gelatine in the jar I brought."
    mc "A jar? You’ve got to be kidding me."
    "Butters’s legs are pushed open by the slime, giving me a full-frontal view of the thick slime undulating into her."
    "It’s a similar motion to fucking and the movements inside her pussy result in lewd wet sounds."
    "This is actually the first time I've seen her pussy. Despite seeing a lot of mare pussy lately, finally getting to see Butters's feels extra erotic."
    butters "Uuurggghh, it’s so thick and filling… *Pant*. *Pant*."
    "Rather defeated, Butters relaxes in the slime, her breasts now fully spilled out of her clothes and her head leaning back into the slime as it starts to pound her."
    slime "There, there... Relax, and release... Relax, and release..."
    "The slime treats her well, massaging areas of her body while kissing her neck."
    butters "It feels so good, aahhh…"
    butters "Ahhh, aaahhh… aahhh… Even though it’s pumping slime into me…"
    slime "Mmm, baby your pussy feels just as good..."
    butters "Is my belly getting bigger? Oohh, don't fill me up too much miss slime."
    "With each thrust the slime does, both the girls rock back and forth, their squishy breasts jiggling erotically."
    "The bouncy slimy sex, and the fact Butters is enjoying it so much, is turning me on more than I’d like to admit."
    "This is basically watching lesbian sex, right? It's only natural that I'd get an erection while watching this."
    slime "Kehehe. Look mare, your friend's cock is hard."
    butters "Ahhh, ohhh gosh, you have an erection… Naughty human! Ahhh."
    mc "I couldn’t exactly help it, how am I the naughty one right now anyway? I’m not having consensual sex with a slime monster."
    "Against my best intentions, I start to masturbate while watching."
    slime "C'mon mare, let the poor boy join us, it'd be so rude to keep all the fun to yourself."
    butters "Ahhh, mmphh… M-Maybe... Do you enjoy this stuff too [playername]? I’ll let you join in if you really want..."
    mc "Join in? I'm not about to let a slime penetrate me."
    slime "No silly, give me your cock, I'll suck it off for you. Kehehe."
    mc "I’d rather have Butters suck it for me."
    butters "Eep? Me? I-I couldn’t! *Pant*."
    slime "Make your choice big boy, we're both horny and ready for you."
    slime "But even she can't beat a slime blowjob."
    butters "Y-Yeah, what she said, put it in the slime’s mouth!"
    "This could be risky, but if Butters is having such a good time, I’d feel bad if I didn’t get something out of it."
    menu:
        "Put your dick in Butters’s mouth.":
            "I move closer to her, and avoiding the slime I bring the tip of my cock towards her mouth."
            show butters slimesexangry with dissolve
            "She looks at my cock wearily and somewhat annoyed."
            "I press the tip of my cock against her lips and it looks like she’s just about to lick it, but then she turns her head away and suddenly her hand reaches for my cock instead, and starts to jack it off."
            show buttershand with dissolve:
                xpos 0
                ypos 0
            butters "Eugh, there's no way I'm sucking your cock you damn perv... Ahhh..."
            butters "This is all you’re getting, human."
            "She gives me a great hand job; her hand is fast! The technique is fantastic too!"
            "It feels just as good as jacking myself off."
            show butters slimesex2 with dissolve
            butters "Aahh, the slime is throbbing, ahhh!"
            "Meanwhile the slime watches Butters jack me off eagerly while continuing to pound away at Butters’s pussy."
            "Somehow throughout the entire intense fuck, Butters continues to give me this excellent handjob."
            "I think I’m going to cum after only a minute of this. I can feel a pressure in my loins and it’s building up extremely quickly."
            "She opens her mouth and her tongue splays outwards expectantly as she prepares to receive my cum."
            butters "Cum all over my dirty face!"
            slime "Mmm, give me your baby juice!"
            "Both the girls waggle their tongues in preparation for my load."
            show buttershand2 with cum:
                xpos 0
                ypos 0
            hide buttershand with dissolve
            show buttershand2 with cum
            "She milks my cock like a professional and before a minute of jacking is even up, I’m cumming loads all over them."
            butters "Ahh, ahh… Mmmm, tasty! Ahhhh! *Pant*."
            "She lets go of my cock after I finish giving her a facial, then licks all the cum up around her mouth and swallows it. The slime also makes sure not a single drop goes to waste as it absorbs any remnants it can."
            hide buttershand2 with dissolve
            "And seconds after I've cum all over their faces, it's been absorbed clean by the slime. I could use something like that at home."
            "I take a step back, the slime is starting to fuck her even faster right now, seemingly spurred on by my involvement. Is it about to finish?"
            $ forestvisithandjob = 1
        "Put your dick in the Slime’s mouth":
            "Am I really going to do this?"
            "The lengths a man will go to get some."
            butters "Ohh, you’re going to do it, what a brave lil’ human!"
            "The slime opens its mouth and waggles its tongue back and forth in a way I must assume is flirtatious, but it comes across as silly."
            show buttersslimeblow with dissolve:
                xpos 0
                ypos 0
            "I press the tip of my cock against it, it’s not exactly a real mouth, it’s more a fake mouth to give the illusion, only one inch inside there’s a thick barrier of slime that I have to push through."
            "Regardless, my cock sinks in deeper, and a makeshift tongue starts to coil and drool over my shaft."
            "Thankfully the inside of the slimy pseudo-mouth is warm, and due to the fact it's simply slime constricting around my shaft; it's very tight, although very different from a pussy."
            butters "Mmphhh, show him how it’s done, slime!"
            "She wasn’t wrong. From the slime's blowjob there are three overwhelmingly pleasureful sensations attacking my senses."
            "First, her lips wrap around my cock and slide up and down my shaft, then the warm slime inside squeezes tightly against my glans, and finally there is also a constant sucking sensation across my whole member."
            butters "It’s good, isn’t it?"
            "Surprisingly good, but I’m still remaining cautious. I don’t want this thing to overstep its boundaries."
            "Woah, it’s starting to speed up, it’s milking me just as fast as it’s fucking Butters! It’s inhumanly fast, but for a slime I bet this is no problem at all."
            "The technique is fantastic too! It feels just as good as sex."
            "It's like the slime has full control over every inch of her body, so she can expertly massage, and focus on my shaft with precision."
            butters "Aahh, the slime inside me is throbbing, ahhh!"
            "I think I’m throbbing too; I can see why she didn’t mind having sex with this thing."
            "The slime continues to pound away at her pussy while she continues to give me this excellent blowjob."
            "I think I’m going to cum, I can feel a pressure in my loins and it’s building up extremely quickly."
            "The slime also adapts unexpectedly, it responds to my body language and focuses its pleasure around the neck of my glans and other sensitive areas. It’s like having a blowjob and sex simultaneously."
            butters "Ohhh, I’m getting close!"
            "I’m also extremely close, my orgasm has managed to sneak up on me. This would definitely be a premature ejaculation if it was with anyone else, but this slime girl evolved to make people cum is pushing me to my limit."
            show buttersslimeblow2 with cum:
                xpos 0
                ypos 0
            hide buttersslimeblow with dissolve
            show buttersslimeblow2 with cum
            "The slime milks my cock like a pro, and before a minute of sucking is even up, I’m cumming loads into this amorphous sex blob."
            "It’s a strange sensation to see my cum drift through this see-through slime creature, I guess there’s no question on whether or not she swallows."
            hide buttersslimeblow2 with dissolve
            "After I cum, I’m fortunately able to pull out and back away as it continues to fuck Butters. I don’t know why she’s stuck and I get to go free."
            "Is she actually stuck or is she just being melodramatic?"
    show butters slimesex3 with dissolve
    butters "Mmphh, it’s so thick and fast, I-I’m gonna come!"
    "Her hips buckle as her body is overwhelmed with pleasure, she throws her head back, her loud moans echoing throughout the cavern."
    butters "Kyaahhh, cooomiinnnggg!!"
    show butters slimesex3 with cum
    show butters slimesex3 with cum
    show butters slimesex3 with cum
    stop ambience fadeout 3.0
    stop music fadeout 3.0
    scene bg black with dissolve
    if crystalballactivated == 1:
        $ crystalballactivated = 0
        jump cbmenu
    "…"
    play ambience ambiencecave fadein 3.0
    show bg cavepool with dissolve
    show butters robesad with dissolve
    mc "Wow your belly is so inflated…"
    butters "My womb is full of slimy cum…"
    butters "I’ve never seen a slime so excitable before, nor have I had one cum that much."
    show butters robesurprised with dissolve
    butters "Aahh! It’s because you’re here [playername], it got excited because there’s a male."
    butters "W-Wait! Your cum went into the slime! That means… You fertilised it!"
    mc "Wha?"
    show slimegirl with dissolve:
        xpos 800
        ypos 250
    slime "Hehehe."
    mc "Why are you even still here?"
    butters "That means I-I’m pregnant!"
    mc "PREGNANT?"
    slime "Totally pregnant! I put the man's cum in your womb, kehehe."
    mc "But how?"
    show butters robesad with dissolve
    butters "Yeah… The slime inside me will use the semen to develop into new slime…"
    butters "What a day... I need a shower."
    slime "You can bathe with me if you want."
    show butters robeangry with dissolve
    butters "Shut the hell up you dumb slime, we're leaving."
    "Woah, she has a temper. The genuine anger spitting from Butters caused my skin to shiver."
    slime "Awh... Fine. Here, take a free sample, least I could do."
    "The slime lets us take some of its gelatine, and kisses us both on the cheek before it slides away into the darkness."
    hide slimegirl with dissolve
    butters "On the bright side, one item down, two more to go, right?"
    mc "I don’t think it would be responsible for a pregnant mare to spelunk any further."
    butters "Yeah but, it's not like a proper pregnancy..."
    "Butters wipes some of her slimy hair out of her eyes, and adjusts her dishevelled clothing, I can still see her nipples though."
    butters "Let's go back home, I'm exhausted and I have post-orgasm jelly legs."
    hide butters with dissolve
    pause 0.5
    show bg cave2 with dissolve
    pause 0.5
    show bg cave with dissolve
    pause 0.5
    scene bg black with dissolve
    stop ambience fadeout 3.0
    "…"
    show bg buttershouse with dissolve
    play ambience ambienceday fadein 3.0
    play music butters fadein 3.0
    "Drearily we return to the cottage,and Butters hurriedly makes her way to the shower."
    show butters dresshappy with dissolve
    "I decide to stick around to make sure she’s okay. She pops out of the bathroom fully clothed and looking cheerful."
    butters "Ahhh, a hot shower is just what you need after being molested by slime monsters."
    mc "I've been wondering, are you really going to be pregnant for the next nine months?"
    show butters dresssurprised with dissolve
    butters "Nine months? Thank heavens not, the slime will be born by tomorrow morning."
    mc "Seriously, a day? That's an insane turnover. It's a relief though."
    mc "Are you going to be okay?"
    show butters dresshappy with dissolve
    butters "Of course, I’m looking forward to seeing what happens."
    show butters dresslaughing with dissolve
    butters "With any luck, I’ll have a constant supply of gelatine! Nature is so fascinating."
    show butters dresshappy with dissolve
    butters "Here’s your pay mister human. Sure you managed to completely screw everything up, but at least we got some gelatine."
    butters "Will you come back for more adventures? I might need someone as useless as you to act as bait when getting leaves."
    "I'm rendered somewhat speechless by her admonishment, but I laugh it off as a joke since she said it in such a positive tone."
    "And without skipping a beat, she gives me 35 monies. Sweet! Alchemy must pay well."
    mc "Sure, I'll be back for more adventures. Especially when you pay me this well."
    butters "Any time! I’ll see you soon. I can already feel it, my tummy's about to get really big, so I'm going to need to stay inside for the rest of the day."
    show butters dressneutral with dissolve
    butters "It’s too embarrassing to walk around and have everyone think I’m really, really pregnant, ehehe…"
    stop ambience fadeout 3.0
    stop music fadeout 3.0
    scene bg black with dissolve
    if crystalballdayactivated == 1:
        $ crystalballdayactivated = 0
        jump cbmenu
    "…"
    play ambience ambiencenight fadein 3.0
    show bg moxiewagonlamp with dissolve
    "I return to the wagon and spend the rest of the day relaxing, despite the ordeal, the mood was notably lightened by Butters's happy attitude."
    "Around 5:00pm Moxie returns."
    play music wagon
    show moxie2 althappy with dissolve
    moxie "Evening! I am zonked, had some great performances today, how about you?"
    mc "I can’t say I had great performances, but they sure were unique."
    mc "I went to work with Butters in the forest today."
    show moxie2 neutral with dissolve
    moxie "Oh dear, did she even talk to you?"
    mc "She sure did, she mistook me for a woodland animal at first."
    show moxie2 laughing with dissolve
    moxie "Oh yeah? Pfft, that completely hairless body, and your totally threatening features. A true wild animal at heart."
    "I think Butters’s point was that I wasn’t a pony; she’d probably treat a cow girl, or a wolf girl the same way she'd treat me."
    "She doesn’t seem to like ponies very much. I’ll keep that to myself though."
    mc "I don’t think she gets out much, she was very kind though."
    mc "Either way I had to collect ingredients so we could make potions together."
    show moxie2 neutral with dissolve
    moxie "Pfft, potions are only a myth, but that girl can do whatever she wants as long as she’s paying you."
    mc "Considering I recently found out magic is real, I’m not in a position where I can doubt the existence of potions."
    show moxie2 happyneutral with dissolve
    moxie "Well you see, alchemy is just throwing a bunch of ingredients together, boiling them, and hoping something interesting happens. The process just doesn’t have that magical oomph required."
    show moxie2 laughing with dissolve
    moxie "It's just like astrology, it isn't real!"
    moxie "The only potions I need are the apple ones Honeycrisp makes if you know what I mean, hahah."
    mc "Haha, yeah, yeah…"
    "Does she not know about unicorn dust?  Or am I the naïve one by believing potions exist?"
    "I'm compelled to trust Moxie over Butters, but I'm extremely tempted to test something."
    mc "Moxie, can you cast a spell for me?"
    show moxie2 smug with dissolve
    moxie "I’m not a spell slut, but for you? I can make an exception."
    mc "Hang on a second, I want to place my hands around your horn and feel what happens."
    show moxie2 althappy with dissolve
    moxie "Oh? Getting curious about magic? I can see why, go ahead."
    "I place my hands around her horn. This is the first time I’ve ever done it, it’s hard like you’d expect a mammal’s horn to be, yet it has a sheen to it, probably from showering."
    show moxie2 happy with dissolve
    moxie "Lemme think of a good spell… How about a perfume spell to make the wagon smell nice?"
    play sound magic2
    show moxie2 happy with cum
    "She starts to cast a spell and her horn lights up around my hands, there’s a very slight heat combined with a puff."
    "Oh, and there’s a pleasant aroma, lavender, I believe that’s her favourite flower."
    show moxie2 althappy with dissolve
    moxie "It’s nice having you holding my shaft, and this close proximity is turning me on."
    show moxie2 laughing with dissolve
    moxie "Maybe you could jack off my horn, ehehaha!"
    show moxie2 althappy with dissolve
    moxie "But I’m too hungry to have sex right now, how about I go start dinner?"
    mc "Sure, thanks for humouring me."
    hide moxie2 with dissolve
    "I back away and look at my hands, there is indeed miniscule amounts of pink granules on the palms of my hands, is this unicorn dust?"

    scene bg black with dissolve
    "…"
    jump evening
label forestvisit2:
    "Best check up on Butters and see how she’s doing after that slime 'incident'."
    stop music fadeout 3.0
    show bg foresthouseexterior with dissolve
    "I make my way to her cottage in the forest clearing and knock on the door."
    "This time I can definitely tell she’s peeking through the curtains before opening the door."
    "She likes me though, so she happily opens the door and welcomes me inside."
    show bg buttershouse with dissolve
    show butters dresslaughing with dissolve
    play music butters
    mc "You're looking good, Butters."
    butters "Thank you! I’m glad you came; I have a surprise for you."
    mc "A surprise? Other than what I’m already expecting?"
    show butters dresshappy with dissolve
    butters "What are you expecting?"
    show slimegirl with dissolve:
        xpos 900
        ypos 300
    "As I step inside, I immediately see a slime girl on the sofa watching cartoons on the TV. She doesn’t even react to me, but she does talk."
    slime "Sup."
    butters "She 'arrived' early this morning, turns out her name is Poyo."
    mc "Ohh, 'arrived'... That’s great…"
    show butters dressneutral with dissolve
    butters "She’s too young to reform her slime at the moment, so I’ve been feeding her lots of greens."
    "As much as the situation discomforts me, the slime girl is kinda adorable."
    show butters dresshappy with dissolve
    butters "Ohhh, and my belly is finally small again! A small price to pay for all the gelatine I could ever use."
    show butters dresslaughing with dissolve
    butters "Poyo and I are going to have a great symbiotic relationship!"
    mc "Is this thing technically my child? It’s pretty weird to think about."
    poyo "If I'm your child, that'd make me one ugly son-of-a-bitch."
    show butters dressangry with dissolve
    butters "Poyo, watch your language!"
    poyo "You're not my mom."
    show butters dresssad with dissolve
    butters "Eugh, don't mind her, she's going through her angsty teenage rebellion phase."
    mc "So what's the deal with her biology?"
    show butters dressneutral with dissolve
    butters "Well, slimes produce asexually, your cum didn’t fertilise the slime the same way as us mammals, it just provided enough nutrients for the separated slime to develop."
    mc "What? I have no idea what you just said."
    butters "When a slime breaks off a part of itself, it’s like a flower; if it gets enough nutrients it'll grow into a new flower, or it'll wilt."
    mc "Ooohhhh, right, I getcha."
    show butters dresshappy with dissolve
    butters "I think semen just happens to be particularly potent at it."
    butters "Poyo is more accurately the same slime girl we played with in the cave, with a lot less 'kehehe' thankfully."
    "'Played' is a friendly way to put it, molested perhaps."
    "It seems Butters's bunny, Devil, is terrified of the slime girl."
    mc "Hey Poyo, aren't you going back home?"
    poyo "No way man, that cave is a shit-hole. I dunno how my mom puts up with it."
    poyo "And Butters spoils me here, I got everything I need."
    show butters dressneutral with dissolve
    butters "Ehehe, maybe... I just do the best with what I have..."
    butters "But please watch your profanity..."
    poyo "Meh... I'm going to my room, don't bother me."
    hide slimegirl with dissolve
    butters "Anyway... [playername], it’s great for you to join me again, would you like any breakfast before we head out?"
    mc "No thanks; I’ve already eaten. Before we do head out though, I wanted to know a bit more about potions."
    show butters dresshappy with dissolve
    butters "Ask away, [playername]."
    mc "Tell me if this is too vague, but how does it work?"
    show butters dresslaughing with dissolve
    butters "Not vague at all, it's as easy as breathing for me."
    show butters dresshappy with dissolve
    butters "First, mix the ingredients in solvent, then overcome the energy barrier via heating."
    butters "Add unicorn dust to turn the liquid concoction into a magical brew. Wait for it to cool, then bottle it up!"
    butters "Like I said before, a lot of meticulous trial and error is required. Pour the potion onto something and see what happens; if you’re feeling brave, drink it!"
    mc "I'd love to hear some examples of potions. I'm always interested in magical things."
    show butters dresslaughing with dissolve
    butters "Oh goodie! I’m so happy that you’re interested in alchemy. It's always good to know what you're working towards too."
    show butters dresshappy with dissolve
    butters "But you absolutely can’t tell any of those pesky unicorns though!"
    mc "Understood, I’ll keep it to myself."
    "Woops I accidentally told Moxie about the potions, at least she didn’t believe me."
    butters "Well, here's my special trick. I have an ancient relic here, a crystal that collects unicorn dust from the area."
    "She lifts up a strange crystalline rock, cut like a gem. It was adjacent to a small, perpetually open window."
    mc "How does it do that?"
    show butters dressneutral with dissolve
    butters "It acts as a magnet for magic and dust."
    show butters dresshappy with dissolve
    butters "I adore magic imbued relics, the potential is limitless."
    show butters dressneutral with dissolve
    butters "I think Princess Selene collects them, they're probably safer in her hands."
    "Next to her cauldron is a shelf full of varying concoctions, each labelled, but the handwriting is too hard to read."
    mc "What are all these?"
    show butters dresslaughing with dissolve
    butters "That is a selection of my mastered potions, no touchies mister human!"
    show butters dresshappy with dissolve
    butters "This first one is a Dreamweaver potion, it lets me turn any dream I want into a lucid dream, it’s a ton of fun."
    butters "The next one is a Libido Suppressant. It’s far more powerful than any magic a pony could conjure and lasts over time unlike an instant-one-time spell."
    "The Libido Suppressant potion is notably half empty."
    mc "Interesting, I can think of a few ponies that need that, you could make a business out of it."
    show butters dressneutral with dissolve
    butters "My potions are too good for them. But if you'd like to buy a potion, I'd be more than happy to give you a discount rate."
    mc "Oohh, I just might take you up on that offer another time."
    show butters dresshappy with dissolve
    butters "Ohh, here’s one that’s similar to what I’m trying to make now."
    butters "This here is an anti-lycanthropy potion made using slime gelatine. I have no use for it personally, but isn’t that cool?"
    mc "Lycanthropy? That’s a thing in this world?"
    butters "Yeah, it's a really bad sexually transmitted curse, or STC for short. If a werewolf does the naughties with you, you’ll become one too!"
    mc "Sounds scary, next you’ll be telling me there are vampires."
    show butters dressangry with dissolve
    butters "Don’t be ridiculous! That’s utterly absurd folklore."
    "She snapped at me. She clearly takes this stuff seriously."
    mc "Oh, okay…"
    show butters dresssad with dissolve
    butters "*Sigh* Sorry. We need to find a folium polypus and a dewblossom, are you ready?"
    mc "I think we should gear up and be more prepared if we’re going into the same cave. We might run into some more slimes."
    mc "I'd rather not trade sex for alchemy ingredients again."
    show butters dressneutral with dissolve
    butters "Trading sex for alchemy ingredients isn’t so bad. Sometimes that's just the way of the wild."
    menu:
        "Have you seriously been fucking plants and monsters all day to get alchemy ingredients?":
            show butters dresshappy with dissolve
            butters "Not all the time! Gosh, what do you take me as, mister?"
            butters "The way I see it: You give a little, you get a little, that’s basic economics."
            mc "That’s not economics at all! That’s not even in the same ballpark!"
            butters "Ball… park?"
            mc "Nevermind…"
        "Seems fair, let’s go fuck a folium polypus, what could go wrong?":
            show butters dresshappy with dissolve
            butters "Mister plant deserves a reward for letting us have its leaves."
            butters "You give a little, and you get a little, such is the way of nature."
            mc "Do you actually enjoy doing it?"
            butters "Eheh, I don’t want to say. A girl has to keep her secrets."
            "That's a yes."
        "I think that’s a terrible idea.":
            show butters dresssad with dissolve
            butters "But why? There’s no risk associated with it."
            mc "How do you know? You just mentioned lycanthropy, what other mythical STDs could you catch by sleeping around with nature?"
            butters "Ohhh… Don’t judge me, it's always a last resort for me!"
            "She seems genuinely saddened, maybe I was too harsh."
            mc "Just try to be more careful in the future, alright?"
    "This girl is somewhat eager to do things with animals and plants but shows absolutely no interest in doing anything with me, ain’t that a kick in the head."
    menu:
        "I could ask her if it was bothering me this much."
        "Would you sleep with me?":
            show butters dressneutral with dissolve
            butters "No, I don’t think so..."
            show butters dresshappy with dissolve
            butters "Maybe if you help me make the potion super well, I can give you a little reward!"
            mc "Okay, I won’t pry, I was just curious."
        "(Ignore thought)":
            pass
    mc "I definitely think we need to gear up better, maybe a weapon? I’d rather not get into a weird situation again."
    show butters dresslaughing with dissolve
    butters "All we're doing is getting leaves from a plant... You’re silly for wanting weapons. What’s the worst a plant can do?"
    mc "Okay, I admit you're right. But what if we run into another slime?"
    show butters dressneutral with dissolve
    butters "Now that we have the gelatine we could just walk away from the miss slimeys."
    mc "Yeah they were pretty slow... What if there are any other monsters?"
    show butters dresshappy with dissolve
    butters "We'll be fine, [playername]. Do you really think there are dangerous monsters next to Arcadia city?"
    mc "Fine, fine... I concede, no weapons."
    show butters dresslaughing with dissolve
    butters "Pacifist route, let’s go!"
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene bg black with dissolve
    play ambience ambiencecave fadein 3.0
    show bg cave with dissolve
    show butters robeneutral with dissolve
    "We head off to the same cave as before, our route lit by a lantern."
    show bg cave2 with dissolve
    "We end up getting a fair bit deeper this time and we still don’t find anything."
    mc "No slimes this time..."
    butters "We’re close to the plants we need. Over here."
    "She walks to a tight crevice in the side of one of the walls and points inside."
    hide butters with dissolve
    show bg cavehole with dissolve
    butters "When I came here over a year ago, there was a small bloom of what we need on the other side of this hole."
    butters "You ready to crawl through?"
    mc "Seems uncomfortably claustrophobic, but if that's what we gotta do. Let's leave the lantern here."
    label buttersandalraune:
        pass
    "Butters goes first, laying on her belly and starting to crawl."
    show butters ass with dissolve
    "And yeah, I can see up her skirt, it’s hot."
    butters "Crawl with me human, let's go."
    "I’d be lying if I said I wasn’t staring; she has a great ass."
    butters "Wait... Can you see my butt?"
    "She says with a muffled voice."
    mc "Uhh, no don't worry, your skirt is covering it."
    butters "N-No it isn't! I can feel a breeze!"
    butters "Hmph. You can stare, but no touchies!"
    "Her ass would be easier to enjoy if it wasn't for the moist and mossy surroundings."
    "Crawling through this frankly gross and damp passage makes me definitely want to get a shower after this trip."
    "Eventually she slips through the other end and drops down into a new cavern, I shortly follow."
    hide butters ass with dissolve
    show bg caveovergrown with dissolve
    "The passage leads us to a completely overgrown cavern, only lit by a few stray beams of light radiating through gaps in the ceiling."
    "The gaps in the ceiling seem to have been created by vines slowly pushing through and eroding the stone."
    "Everything is covered in vines; the roof, walls and even the ground. Occasionally dotted around the vines are massive reddish pink bulbs which ooze pink mist."
    show butters robeneutral with dissolve
    butters "It may have been over a year since I’ve been in here, but I don’t remember it being this bad..."
    "The pink mist fogs and moistens the air making it damp and hazy. I almost want to go back into the damp crawlspace, this cave feels tainted."
    mc "Eugh, what’s with this pink mist?"
    show butters robesad with dissolve
    butters "I don’t even know... I feel kinda weird, [playername]..."
    "The strange pink mist is accompanied by an unfathomable smell; it’s not an unpleasant smell, but it’s so unfamiliar I don’t even know how to process it."
    "The claustrophobic nature of the cave and poor ventiliation due to lack of a draft only make it worse."
    butters "I don't like it here."
    mc "Let’s just get the leaf clippings and go."
    "Butters reaches into her knapsack and looks for her small knife that she brought to cut some leaves off."
    "For some bizarre reason I’m starting to become hot and slightly erect, but why?"
    mc "Is... is this thick mist turning me on?"
    "It's like my brain was just immediately stimulated with something erotic, and not just Butters's underskirt earlier."
    show butters robeneutral with dissolve
    butters "It’s not just you, my clit feels all tingly."
    butters "I-I'm getting wet, but I don't know why."
    "We may be getting horny, but we’re not braindead; something's wrong."
    menu:
        "Ask Butters what she thinks.":
            mc "What’s going on, Butters?"
            butters "I think the mist in this cavern is pheromones sprayed by those bulbs, and now we’re covered in it. It’s probably going to last a while."
            mc "Just pheromones? Could be worse, I can work with an erection."
            show butters robesad with dissolve
            butters "*Sigh*, I hope I can work while horny too..."
            butters "If I misbehave, just gimme a swift whack on the head please."
            mc "Will do."
        "Think about the situation yourself.":
            "Both me and Butters are suddenly rather horny, it must be because of this folium polypus."
            mc "If this plant collects nutrients from the juices of animals, then using pheromones to make them excrete fluid seems like a natural evolutionary progression."
            butters "Yeah... It's making me drip."
            "It probably tries to arouse creatures with pheromones, but what does it do then?"
            mc "I bet it has a collection method, we need to stay vigilant."
    "I definitely have an erection now as the two of us step over an obnoxious amount of vines in search of some specific leaves in the mist and darkness."
    "With each step, the vines writhe and react. I know it's just a plant, but I feel like it's aware of me."
    show butters robeangry with dissolve
    butters "Eugh, where is it? All I see are vines and no leaves."
    mc "Do we need leaves specifically?"
    butters "Yes! The potion needs to be perfect."
    "As Butters and I check the underside of a pink bud for the leaves we want, it suddenly sprays a thick load of pink mist in our faces causing us both to cough and splutter."
    show butters robesad with dissolve
    butters "Eck, *cough*! It went in my, *cough*, mouth!"
    mc "*Cough*! It's not just this bud that's spraying, they all are now!"
    play music danger fadein 3.0
    hide butters with dissolve
    show bg caveovergrown2 with dissolve
    "All throughout the room, the buds spew out more erotic pink mist."
    "What's worse is the writhing vines beneath us are starting to rise, slowly trying to coil around our feet and ankles."
    mc "Uhm, the plant is trying to hold me in place!"
    show butters robesad with dissolve
    butters "Mmmph, stupid plant! I don't wanna have sex with you! Break the vines, [playername]!"
    "She’s right, if I just lift my leg with a bit more force, the vines rip and tear."
    "The vines are concerning, however that's not what's on my mind right now..."
    "It's the pheromones... My cock is tight and throbbing, and Butters is starting to look sexier by the second."
    "This room isn’t very well ventilated and it’s clearly starting to go to our heads."
    show butters robehorny with dissolve
    butters "Ahh gosh... M-Maybe I do want to have sex... My pussy feels so empty right now..."
    "From behind, I can see Butters's hips sway back and forth, I can just imagine pushing her against the wall of this cave and sliding my cock deep inside her."
    "All I need to do is lift up her dress, I know she doesn't wear panties..."
    $ time = 4
    $ timer_range = 4
    $ timer_jump = "forestfuckbutters"
    show screen countdown
    menu:
        "Fuck Butters":
            hide screen countdown
            "I can’t help it; she just looks so sexy right now."
            "With my right hand I start to jack myself off, while using my left to lift up Butters’s dress, peeking at her dripping pussy."
            show butters robesad with dissolve
            butters "Eep! What are you doing?"
            mc "I’m going to fuck you."
            show butters robeangry with dissolve
            butters "N-No, you can’t! We need to get the leaves and run away!"
            "Eugh, fuck, she’s right. What’s wrong with my head right now?"
        "Just get the damn leaves, I’m not going to let a plant win over me.":
            hide screen countdown
            "Stop thinking lewd thoughts, I need to focus."
            "I push forward, trying to avoid letting the vines hold me back."
        "Fuck Butters, you know you want to":
            label forestfuckbutters:
                hide screen countdown
                pass
            "I can’t help it; she just looks so sexy right now."
            "With my right hand I start to jack myself off, while using my left to lift up Butters’s dress, peeking at her dripping pussy."
            show butters robesad with dissolve
            butters "Eep! What are you doing?"
            mc "I’m going to fuck you."
            show butters robeangry with dissolve
            butters "N-No, you can’t! We need to get the leaves and run away!"
            "Eugh, fuck, she’s right, what’s wrong with my head right now."
        "Just imagine your cock in her plump ass, I bet it feels amazing.":
            hide screen countdown
            "I can’t help it; she just looks so sexy right now."
            "With my right hand I start to jack myself off, while using my left to lift up Butters’s dress, peeking at her dripping pussy."
            show butters robesad with dissolve
            butters "Eep! What are you doing?"
            mc "I’m going to fuck you."
            show butters robeangry with dissolve
            butters "N-No, you can’t! We need to get the leaves and run away!"
            "Eugh, fuck, she’s right, what’s wrong with my head right now."
    "These aphrodisiacs are rotting my mind, we need to hurry."
    show butters robesurprised with dissolve
    butters "Aahhh, I finally found the leaves!"
    butters "Let's hurry before I drip any more than I already have."
    "She leans over and starts to take clippings from some vines on the wall."
    "While she takes the clippings, we’re left standing still, at our most vulnerable."
    "I try to desperately break the vines that are trying to coil around me, but the number is growing and they're beginning to overwhelm me."
    "Another dense spray of pink mist from a nearby bulb hits the both of us, continuing to overwhelm our senses."
    "All I can smell is a thick erotic aroma, all I can feel is the desperate need to get my cock touched."
    show butters robehorny with dissolve
    butters "Uuuhh... I... I really need to get fucked."
    "Butters seems to have honestly given up fighting, vines are coiling up to her knees and her thighs are quivering."
    "Her eyes are glazed over and her hand roams from the leaves to her thighs."
    show butters masturbating with dissolve
    "And just like that, she starts to rub her pussy, drunk with arousal."
    "Seeing her masturbate is enough to make my cock throb and drip with precum."
    mc "B-Butters, what about the leaves?"
    butters "The leaves can wait, I need cummies first…"
    "In my horny daze, I barely noticed the vines coiling up even higher on me too, the temptation to let my hand roam between my legs and start masturbating is unbearable."
    $ time = 5
    $ timer_range = 5
    $ timer_jump = "forestrelax"
    show screen countdown
    menu:
        "Fight the vines.":
            hide screen countdown
            "I struggle and fight the vines; the more I fight the more aggressively they try to wrap around and restrain me."
            "It's like the vines are fully sentient, they're intelligently trying to restrain me now as I frantically panic."
            "Eventually my struggle slows down as the vines overwhelm me and hold my feet completely in place."
            "I'm left pathetically wiggling about in place, unable to make any progress in escaping."
            "However, as I'm left stuck, the vines never rise above my knees."
        "Relax.":
            label forestrelax:
                pass
            hide screen countdown
            "Maybe these vines are reacting to my presence, they weren’t moving before I came in here."
            "They also started to attack more aggressively only after we started to panic."
            "I take a deep breath and clear my mind."
            "With no movement and no struggle, the vines do indeed completely stop rising."
            "I look over to Butters who stopped in place, and I can see the vines have also stopped rising on her too, she had the right idea, even if her method was wrong."
        "Skip the foreplay and start masturbating.":
            hide screen countdown
            "This vines just want my fluids, right? Fuck it, I’ll give it what it wants, then it can leave me alone."
            "I bring my hand to my sensitive cock and start to masturbate, as I do I feel an overwhelming rush of euphoria."
            "As soon as I start, I can't stop. It feels like nothing else in the world matters right now."
            "Butters watches me masturbate with glee, and in turn her fingers start to speed up."
    butters "Ahhh, ahh... These aphrodisiacs are making me just want to kneel down and become one with the tentacle vines."
    mc "Please don’t do that."
    butters "Mmphh, do you think these vines will calm down after we come?"
    mc "Why are you asking me? You’re supposed to be the expert."
    hide butters with dissolve
    mc "Uh oh."
    show butters robesurprised with dissolve
    butters "Uh oh?"
    "Two particularly thick vines slowly reach up Butters’s legs then thighs, I can only assume they’re about to fuck her in both holes at once."
    play sound cum
    show butters tentacles1 with dissolve
    butters "Kyyaah! The vines are pressing against my pussy and butt!"
    butters "Oohhh, oohh... One of them went inside…"
    play sound cum
    play ambience sex fadein 3.0
    "One of the vines immediately slips into her pussy, she’s so extremely wet that it readily pistons inside of her."
    play sound cum
    "The one at her butt is slightly slower though, it gently eases into her pucker before softly pushing itself inside."
    "Butters’s expression is of such immense satisfaction, it looks like she’s getting the best massage of her life."
    butters "Ahh, ahhh… Ahhh! I just wanna live here aahhh-and play with these tentacles all day."
    "The vine tentacles had made their move on Butters, yet I’m completely untouched."
    "I’m relieved since I don’t think I’d be as mentally prepared as Butters to get a tentacle up my butt."
    mc "Why aren’t the tentacles attacking me?"
    "The vines continue to penetrate Butters in both holes, fucking back and forth in intervals, she can barely form a sentence between her moans."
    butters "Ahh! T-The vines absorb, ahhh… fluids... There’s no point in doing this to males."
    mc "Oh, they just ignore men?"
    butters "Mmphh… Nope…"
    "She weakly points to something in the darkness of the cave."
    stop music
    show butters tentacles2 with dissolve
    alraune "Looking for leaves? You found 'em..."
    alraune "But what is the price you're willing to pay for such a commodity?"
    alraune "Now that the pony is occupied, how about we make a deal?"
    mc "Y-You and I?"
    butters "Aahh, ahh, fuck me harder! Aahaaaaah!"
    alraune "Let's shut her up shall we?"
    show butters tentacles3 with dissolve
    "A tentacle coming from the alraune herself pushes itself into Butters's mouth and fucks her face."
    "Her entire body is an orgasmic mess that can't stop quivering."
    alraune "You've got quite a dangerous friend there, hehe, but I'm dangerous too."
    mc "What do you want from us?"
    show butters tentacles4 with dissolve
    alraune "Us? No, just you."
    alraune "Let's talk business, I'll trade some of my leaves for two loads of your cum."
    mc "My cum? W-wha?"
    show butters tentacles3 with dissolve
    alraune "Cum is some fine gourmet shit, I ain't passing up this chance."
    alraune "The leaves? I'll be honest, I'm only giving you those because I feel nice today. I'm getting the cum regardless."
    mc "I see... So you want me to fuck you? You've got a deal."
    alraune "Ahaha, fuck you? No way, I'm not ready to get pregnant yet."
    show butters tentacles4 with dissolve
    alraune "I only want the nutrients..."
    "One of the reddish-pink bulbs, similar to those that were lining the walls comes closer to me on the tip of a tentacle."
    play sound cum
    show butters tentacles5 with dissolve
    "And it opens."
    "The inside is a moist, vaginal-like entrance that oozes and sprays pink misty aphrodisiac onto me as it writhes towards my phallus."
    alraune "This inside of this bulb will milk your semen, 'kay?"
    "Any other situation I'd be worried, I'd be concerned. But I'm beguiled with arousal, as my cock throbs, I nod."
    play music sex1
    play sound cum
    show butters tentacles6 with dissolve
    "The opening of the flower clumsily finds the tip of my cock before ungracefully pushing itself onto me and sliding back down my shaft."
    show butters tentacles6in with dissolve
    "The aphrodisiac it has sprayed acts as a thin layer of moisture which lubricates my shaft, while simultaneously making it feel strange and tingly."
    show butters tentacles6 with dissolve
    "The inside of the flower is warm and pleasant; it has an appealing texture that feels agonisingly pleasurable against my cock."
    show butters tentacles6in with dissolve
    "The catharsis of the tight sensation around me is immeasurable, I can barely contain my pent-up lust."
    show butters tentacles6 with dissolve
    butters "Mmphhh, mmmmphhh! Mmmmm..."
    show butters tentacles6in with dissolve
    "And neither can Butters, as the tentacles probably give her the best sex she’s ever had, although knowing her she’s probably done this before."
    show butters tentacles6 with dissolve
    show butters tentacles6in with dissolve
    "The tentacles speed up and throb within her, I love the cute way she twitches in response to the pleasure."
    show butters tentacles6 with dissolve
    show butters tentacles6in with dissolve
    "Meanwhile the flower bulb acts as a sex toy as it tightly slides up and down my shaft at a similar pace to the tentacles fucking Butters."
    show butters tentacles6 with dissolve
    show butters tentacles6in with dissolve
    "It squeezes in all the right places and with each thrust I can feel another wave of pleasure crash into my body."
    show butters tentacles6 with dissolve
    show butters tentacles6in with dissolve
    "With each wave of pleasure, my orgasm quickly rises, the pseudo-vagina flower feels just as good as the real thing."
    show butters tentacles6 with dissolve
    show butters tentacles6in with dissolve
    "The entire time I get the erotic show of watching Butters play with the tentacles. Along with the nude Alraune girl that watches me with a grin."
    show butters tentacles6 with dissolve
    show butters tentacles6in with dissolve
    alraune "Cum for me big boy..."
    play sound cum
    show butters tentacles7 with cum
    play sound cum
    show butters tentacles7in with cum
    "It hasn't even been a minute and my cock is boiling over with an immense orgasm rivalling none I've ever had before."
    play sound cum
    show butters tentacles7 with cum
    play sound cum
    show butters tentacles7in with cum
    show butters tentacles8 with dissolve
    alraune "Ohoho yesss... That's some fucking delicious semen."
    "The flower bulb graciously sucks and squeezes my shaft, swallowing as much semen as it can before it resumes fucking."
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    alraune "Ara ara, time for second breakfast."
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    "I'm so aroused that I barely feel my refractory period, after a short bout of sensitivity it fades away and the bulb continues to fuck me."
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    "Poor Butters's entire body buckles and gives out under the overwhelming pleasure, her clothes have been gradually loosening and falling off too."
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    butters "Mmphh, mmmphh, aahhh!"
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    "The aggressive fucking from the vines is causing her robes to rip and tear, by the time she's done she'll have nothing left."
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    "The flower starts to speed up again, the insides gooey and wet with a mixture of the pink aphrodisiac ooze and my cum."
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    "The sweet sensations are enough to push me to my limit a second time as I get closer to my orgasm."
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    alraune "Melt with this pleasure, give yourself wholly unto me."
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    "My cock feels tight and it’s throbbing again, I’m going to erupt any second."
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    "I’m going to cum, I can’t hold back much longer!"
    show butters tentacles7 with dissolve
    show butters tentacles7in with dissolve
    alraune "Yess, yes!"
    play sound cum
    show butters tentacles7 with cum
    play sound cum
    show butters tentacles7in with cum
    "My cock launches many loads of cum into the strange flower vagina, as the semen fills up the flower again, it starts acting strange, it writhes and wiggles intensely."
    play sound cum
    show butters tentacles8 with cum
    play sound cum
    show butters tentacles8 with cum
    alraune "Haahh, this semen is so good! So good! Haaahh... Mmm..."
    play sound cum
    show butters tentacles9 with cum
    play sound cum
    show butters tentacles9 with cum
    play sound cum
    show butters tentacles9 with cum
    "The tentacles inside Butters suddenly erupt into enormous amounts of sloppy thick cum concurrently with my orgasm, it's almost like the alraune herself had an orgasm."
    butters "Mmphh! Mmphh!"
    stop music fadeout 2.0
    stop ambience fadeout 2.0
    "The intensity in the room reaches its peak before quickly dying down."
    scene bg caveovergrown with dissolve
    "The once aggressive vines and flowers drop to the floor lifelessly, and the flower that had just been having sex with me recedes into its budded form and returns to the Alraune."
    "Both Butters and I are left panting and barely able to stand."
    if crystalballactivated == 1:
        $ crystalballactivated = 0
        jump cbmenu
    show butters cumsad with dissolve:
        xpos 700
        ypos 50
    show alraune happy with dissolve:
        xpos 100
        ypos 150
    butters "So much cum… In my belly, on my boobs... *Pant, pant*."
    mc "No time for hentai dialogue, we need to get the leaves and get out, come on."
    alraune "Here, I'll give you some. Nibble a little on the leaf to null the effects of the mist."
    play ambience ambiencecave fadein 5.0
    "Butters and I both nibble the leaf as fast as we can, and soon our clouded minds slowly begin to return to reality."
    show bg caveovergrown3  with dissolve
    "I haven't even realized how fucked up my vision, hearing and feeling in my body was until it all returned at once."
    "It's like that joke where the man's brain is in his dick, it really felt like I was just a host for my dick's whims for a while."
    show alraune horny with dissolve
    alraune "You two are fun, you can come back whenever you want."
    show butters cumneutral with dissolve
    butters "Only reason for me to come back is with a match and oil."
    show alraune happy with dissolve
    alraune "Hmph, I'd like to see you try! Ahaha, I'll have you squirting all over my floor again."
    mc "*Sigh*. Thanks for the leaves, come on Butters, let's leave."
    alraune "Buh-bye!"
    scene bg cavehole with dissolve
    "I take Butters by her hand and the two of us leave out the hole we used to enter the cursed room."
    show bg cave2 with dissolve
    mc "Phew, I’m so glad they stopped, I thought we might be trapped in there for a lot longer."
    show butters cumneutral with dissolve
    butters "I could have kept going, but... You’re right, I’m glad we got those leaves."
    butters "She gave every hole of mine a wild ride... As mind-breakingly good as it did feel, I'd rather not become an Alraune's love slave."
    mc "Did you know about her?"
    butters "I didn't, last time I was there it was just a small plant."
    butters "Alraunes are plant creatures that can mimic and symbiote with any nearby flora, so they can show up wherever."
    butters "Can we sit down a second? I need to catch my breath."
    hide butters with dissolve
    "I take a deep breath and the two of us sit down on the cave floor, it’s cold but that’s the least of our concerns right now."
    "Butters uses the remaining rags of her robe to wipe off the cum on her before tossing it."
    show butters closesad with dissolve
    "The two of us sheen slightly pink in the light due to those pheromones still lingering on us."
    butters "Icky, we’re naked, wet and still a bit horny because of that aphrodisiac."
    mc "Hopefully it dries off soon, nibbling on this leaf wasn't as effective as I had hoped. Speaking of naked, what’s that strange tattoo on your pelvis?"
    show butters neutral with dissolve
    "She was trying to hide it with her hand, but it was far too obvious."
    butters "Awh nuts, you were never supposed to see it. That plant really messed up my robe."
    mc "You were wearing clothing to hide this strange tattoo? Why?"
    show butters sad with dissolve
    butters "It’s no tattoo, it’s a permanent mark on my body because of a strange curse."
    mc "A curse? What kind of curse?"
    show butters neutral with dissolve
    butters "I believe it’s a succubus curse, it’s not a well-documented condition but from what I’ve read I have quite a lot of the symptoms."
    show butters closesad with dissolve
    butters "You know... Lust, death by sex. Maybe you haven’t heard of it before."
    "She’s a succubus? That explains why she doesn’t want anything to do with me sexually. Or does it?"
    butters "I’m surprised the tattoo is the first thing you pointed out; didn’t you notice my cool bat wings?"
    mc "Wha? I didn’t notice at all, were those always there? Damn!"
    menu:
        "What’s a succubus?":
            show butters closeneutral with dissolve
            butters "A succubus is a creature that feeds off sexual intercourse with creatures, I tend to get by with lust repression potions, and certain creatures resistant to my drain."
            butters "I don’t have the heart to actually hurt anyone."
            mc "So you get hungry for sex because of the succubus nature?"
            butters "Of course, that’s what the plants and slimes are for, they aren’t hurt by my draining."
        "Are you dangerous?":
            show butters closesad with dissolve
            butters "No, I could never hurt a mammal. I tend to get by with lust repression potions, and certain creatures resistant to my drain."
            show butters closeneutral with dissolve
            butters "I’m strictly on a vegetarian diet when it comes to sex."
            mc "That’s mildly amusing, do slimes count as vegetarian?"
            butters "No, but they kinda push themselves onto me, so I let that pass."
            mc "Don’t the plants and slimes get hurt when you have sex with them?"
            butters "Slimes and plants have the ability to regrow cells far more effectively than a mammal, meaning they recover."
    butters "If I slept with a mammal though, they might be okay the first time, but any damage is permanent."
    mc "Are you speaking from personal experience?"
    show butters closesad with dissolve
    butters "Mm... I’ve had one incident, as unfortunate as that one time is, I've otherwise always had good self-control."
    show butters closeneutral with dissolve
    butters "I may be a succubus, but that doesn’t mean I’m not grounded by morals and ethics. I'm not a monster."
    "How exactly did this innocuous forest girl end up with such a curse?"
    mc "How did this happen?"
    show butters closesad with dissolve
    butters "The curse stopped me from aging. I've actually been a witch for about fifty years now; always playing around with alchemy."
    butters "When I was young, in my twenties, I was the type of witch that sometimes got involved with bad crowds."
    butters "One particular bully I dealt with regularly was a unicorn named Umbra."
    show butters closeangry with dissolve
    butters "Umbra was a stallion that slept around. He'd use the same story of how he 'loved' the mare, only for him to dump her at a later point."
    butters "Well at some point he claimed to ‘love’ me but I denied his advances. This hurt his ego, he started to see me as a challenge."
    butters "The brute would bother me over and over, but I'd never give in."
    butters "One day he decided to curse me in an attempt to turn me into a sex slave."
    mc "A succubus sex slave? That sounds paradoxical, he’d die if he had sex with you."
    show butters closesad with dissolve
    butters "Well, he never meant to turn me into a succubus. He was trying to cast a strange mixture of a lust and sex slave spell."
    show butters closeangry with dissolve
    butters "He got more than he bargained for, I fucked him to death."
    butters "Only person I've ever killed. Thankfully I was picked up by good people and taken care of after that."
    mc "What a moron… Ruined two people’s lives with one spell."
    mc "I'm sorry to hear that, it must have been very traumatic for you."
    show butters closeneutral with dissolve
    butters "I don’t remember much... The curse is strange..."
    show butters closesad with dissolve
    butters "It's like the curse created a demonic alternate version of me, repressed inside."
    butters "Sometimes she talks to me in my head. It's scary."
    butters "Once it escapes, everything changes. That’s the version that had sex with him, I don’t consider that to be me."
    menu:
        "Do you like being a Succubus?":
            show butters closesad with dissolve
            butters "Not particularly... I often get cravings for sex, and I worry that my inner demon will escape."
            butters "I take lust repressing potions to quench that desire, it’s almost entirely a lust demon."
            butters "Oh, also the wings are a nice touch, but I just want to be myself again, this curse is wearisome."
        "Isn’t there a way to have sex without hurting someone?":
            show butters closesad with dissolve
            butters "Hmm… Let me think for a second…"
            butters "I’ve tried to be open-minded while developing a cure, which means I’ve thought outside of the box a few times while creating potions."
    show butters closeneutral with dissolve
    butters "Curing the actual curse may be impossible, repressing it is my number one priority."
    butters "There’s only one caveat, let’s say I hypothetically remove my succubus drain, the inner demonic personality will still exist and overpower me in almost every sexual experience."
    mc "That’d be bad, right?"
    show butters closeangry with dissolve
    butters "I think so. I think that personality is a little more... 'forceful'..."
    mc "How’s progress on the cure?"
    show butters closesad with dissolve
    butters "It has been many years now, and progress has been slow to say the least."
    butters "I’ve experimented with countless types of potions but the trial and error of mixing random untested ingredients is utterly exhausting, some days I just want to cry."
    mc "Haven’t you reached out and asked anyone for help? This sounds like far too much work for one person."
    if farmvisit1 == 1:
        "Her plight reminds me of what Honeycrisp is going through too."
    show butters closeneutral with dissolve
    butters "I had briefly considered doing such a thing when I befriended Lily and her magical friends…"
    mc "Ohh, Lily? I bet she’s been helpful."
    show butters closeangry with dissolve
    butters "Not particularly, I’ve distanced myself from the idea."
    show butters closesad with dissolve
    butters "It took me years and years to make progress, I just don’t see what use a unicorn would be."
    mc "Probably more helpful than you think, there’s another reason you’re not telling her, isn’t there?"
    show butters closeneutral with dissolve
    butters "A-Another reason?"
    mc "I can tell you have the pretty reason you don't mind admitting, and the ulterior reason you keep to yourself."
    mc "Be honest with me."
    show butters closesad with dissolve
    butters "... Fine..."
    butters "I can’t bring myself to admit that I'm a succubus... you can’t tell anyone, okay?"
    mc "Oh Butters... If you don't tell anyone, how will anyone help?"
    butters "I dunno..."
    mc "You mentioned you had a potion that cured lycanthropy, that’s rather substantial, how far removed is that from a succubus cure?"
    "Wait, how the heck does she know it cures lycanthropy? I don’t even want to ask."
    show butters closesurprised with dissolve
    butters "Yes! That was a huge milestone, the gelatine was a cornerstone of that potion."
    butters "Gelatine potions make you transform in unusual ways, and the lycanthropy potion specifically reverts you to your original species. From wolf back to pony."
    mc "Why doesn’t that cure your succubus curse too?"
    show butters closesad with dissolve
    butters "Unfortunately a succubus isn’t a species, it’s more of an add-on to any pre-existing species."
    show butters closeneutral with dissolve
    butters "But basically, I think I’m super close! I’ve been experimenting a lot with gelatine lately, I even turned into a frog for four hours last week!"
    mc "A frog? Damn, the possibilities of potions."
    mc "Uhm, so, what do these folium poly-whatever leaves we just got do?"
    butters "I think folium polypus is the key, as an ingredient it's an aphrodisiac."
    butters "But as a magic ingredient, it focuses the potion's magic towards lust, and erotica."
    mc "I see, so we have transformation and lust... It sounds like those two alone would turn you into a succubus, not remove the curse."
    show butters closehappy with dissolve
    butters "Exactly, those two combined could transform you into a nymph, just a theory, not tested! But it's the Dewblossom that changes everything."
    butters "The Dewblossom is an evil warding plant, add that to the potion and woosh! Suddenly it removes the nymph transformation instead of giving it…"
    mc "This sounds seriously promising."
    show butters closelaughing with dissolve
    butters "I’m betting everything on this one brew. It might not work, but I have to try."
    "She's finally smiling again, seeing it warms my heart."
    mc "What are we waiting for? Let’s go grab that dewblossom!"
    show butters closeneutral with dissolve
    butters "Aren’t you going to wait for your boner to go away?"
    "I look down, and indeed I am still erect due to that annoying pink mist."
    mc "Eh, it’s just for show, I can’t help it."
    show butters closehappy with dissolve
    butters "It’s okay, I’m also wet, and naked! We’re even."
    mc "That does make me feel a little better about the situation."
    show butters closelaughing with dissolve
    butters "If you’re embarrassed, you could always hide it."
    mc "It’s actually quite hard to cover a full erection with my hands."
    show butters closehorny with dissolve
    butters "That's because it's too big... Maybe you should try hiding it in me."
    mc "Come on, you know that’s a bad idea."
    show butters closehappy with dissolve
    butters "Hehe glad you were paying attention. Okay, let’s go get some more plants."
    mc "No more plant girls please."
    scene bg black with dissolve
    "Naked, wet and horny, the two of us manage to push on in this cave of molesting horrors until we get to a relatively safe looking mossy well with some blossoming flowers."
    show bg caveflower with dissolve
    "Butters runs past me to the flowers giddily."
    show butters happy with dissolve:
        xpos 000
        ypos 50
    butters "Ahh, perfect, the dewblossom!"
    mc "Now we have everything you need."
    play sound moxiespell2
    show butters surprised with hpunch
    "Butters goes to touch it but it stings her and she jolts as if receiving a potent electric shock."
    show butters surprised with dissolve
    butters "Owie, it still shocks me."
    show butters neutral with dissolve
    butters "Good thing I brought you along with me [playername], you have the special job of carrying the plant home."
    hide butters with dissolve
    mc "Sure thing, it won't sting me right?"
    "I say as I timidly poke the flower, and nothing happens."
    mc "Oh, it's fine."
    "I pluck the flower and turn back to Butters."
    show butters laughing with dissolve
    butters "I can’t believe how helpful you’ve been [playername], I’m so glad I met you."
    mc "Don’t mind me, just doing my job."
    butters "I don’t even know how I could reward you for this."
    mc "You could just pay me, maybe a fancy potion as a souvenir if you’re feeling especially generous."
    butters "What about something even better, hmm?"
    show butters horny with dissolve
    "She wiggles her butt inappropriately while she bends over."
    "Naturally, I’m still erect, I’d love to stick it inside her, but I also enjoy living."
    butters "If this potion works, I swear I'll have the most passionate and loving sex with you as a reward."
    butters "I wouldn't be against doing that now though, hehe."
    "I guess the aphrodisiac is still making her horny."
    mc "I won't have sex with you unless you're cured."
    show butters neutral with dissolve
    butters "Did I say that? All that blood must have rushed away from your brain and into your dick, hehe!"
    mc "If you say so..."
    butters "I’m teasing you!"
    show butters happy with dissolve
    butters "Hmm... Do you think condoms prevent succubus drain?"
    show butters horny with dissolve
    butters "Wanna find out?"
    mc "Not right now…"
    show butters neutral with dissolve
    butters "Awhh yeah, but one time might not hurt, you seem like a tough boy."
    mc "On the contrary, I’d like to think one time would hurt quite a lot."
    show butters horny with dissolve
    butters "Awhh… I bet your semen is yummy."
    show butters surprised with dissolve
    butters "Eugh, did I really just say that?"
    show butters angry with dissolve
    butters "I really need to shower off this aphrodisiac before you get a restraining order on me."
    mc "It’s okay, I’m used to taking a barrage of flirts from mares in heat."
    mc "By the way, the reason you’re not in heat is because you’re a succubus, right?"
    butters "Mhm, which means I can’t have any children, which is one of the reasons I want to cure myself soon…"
    mc "Ahh, I see."
    show butters sad with dissolve
    butters "I want to be able to settle down with a husband and have at least two children. *Sigh*"
    mc "In that case, what are we doing wasting time here, let’s go back to your cottage."
    show butters horny with dissolve
    butters "Ohhh my, you’re going to make me pregnant?"
    mc "Wha-? No! The potion!"
    show butters neutral with dissolve
    butters "Ohhh yeah, the potion! Let’s go!"
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene bg black with dissolve
    "…"
    play music butters fadein 3.0
    show bg buttershouse with dissolve
    show butters happy with dissolve
    show slimegirl with dissolve:
        xpos 1000
        ypos 500
    play ambience ambienceday fadein 3.0
    "We head back, and she starts brewing up the ingredients in her cauldron."
    "I take a quick shower to wash off the aphrodisiac, I suggested to Butters that she should as well but she’s too excited about this potion."
    "She hasn't even gotten dressed yet."
    "She’s definitely passionate about this, I just hope it works."
    "I dry up and as I leave the shower Butters looks positively perky."
    butters "[playername], come! Taste test it for me, hehe!"
    mc "Heh, that's a joke, right? Right? What would even happen if I tried it?"
    show butters laughing with dissolve
    butters "Oh my gosh, if this works, I’ll be able to live a normal life again. I’ve been on stand-still for so many years."
    show butters neutral with dissolve
    butters "I’m hope it works; I can feel the demon scratching in my head again, probably because of everything that has happened recently."
    mc "Has it finished?"
    show butters happy with dissolve
    butters "I’m just waiting for it to cool; it’s taking too long!"
    mc "Surely having a burnt tongue for a day is worth the opportunity of a lifetime!"
    show butters neutral with dissolve
    butters "Argh, I’m going to put some ice in it, it’ll water it down, so it might take longer to digest, but that should even it out, right?"
    mc "I dunno, why ya asking me?"
    show butters laughing with dissolve
    butters "Okay, ice it is, thanks for your input, human."
    hide butters with dissolve
    "I take a seat next to Poyo and watch with anticipation."
    "She gets a glass and drops in four- no, five ice cubes."
    "Before using a ladle to pour-"
    mc "Wait! What are you doing?"
    show butters surprised with dissolve
    butters "Uwah?"
    mc "You can’t just pour a boiling hot liquid into a glass with ice, the glass might crack!"
    show butters happy with dissolve
    butters "This is borosilicate glass, I've been doing this for years, I know my stuff."
    mc "Ah, b-borosillycate of course, my bad."
    "Using a ladle she pours in the hot steamy alchemical brew."
    "She gyrates the glass a few times causing the liquid inside to stir and the rapidly melting ice cubes to click."
    "For a moment, her positivity turns to scepticism."
    show butters neutral with dissolve
    butters "I could drink this, or I could be a succubus forever…"
    show butters laughing with dissolve
    butters "Hmm, forget being a succubus, it’s time to live a proper life."
    "She brings the tip of the ceramic mug to her lips and starts to gulp down the drink unceremoniously in one go."
    show butters sad with dissolve
    butters "*Gulp*. Ahhh… Disgusting, it had slimy blobs in it."
    mc "Yeah it didn’t look that appetising."
    butters "Eck, it's burning my throat, it's really sore now."
    mc "So... Is it working?"
    butters "*Cough, cough*. It'll take awhile to find out... I need to digest the potion first."
    butters "Ohh, my tummy hurts... That Dewblossom really doesn't agree with me..."
    butters "How about I pay you now, and you come back tomorrow? You definitely deserve it."
    mc "Sure thing, I'll be back in the morning."
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    "Butters pays me 35 monies and I return home."
    if crystalballdayactivated == 1:
        $ crystalballdayactivated = 0
        jump cbmenu
    scene bg black with dissolve
    "..."
    $ buttersthirdvisitsetup = 1
    play ambience ambiencenight fadein 3.0
    play music wagon fadein 13.0
    show bg moxiewagonlamp with dissolve
    "I sit down in the wagon and sigh. What an exhausting day."
    show moxie2 neutral with dissolve
    "Soon after Moxie arrives, still in her work uniform."
    show moxie2 happy with dissolve
    moxie "Oh hey! How's it going?"
    mc "Kinda weird, actually. I met an Alraune today."
    show moxie2 shocked with dissolve
    moxie "Ohh, those are pretty rare you know!"
    show moxie2 neutral with dissolve
    moxie "What happened? They're usually not dangerous but they're not one to turn down a man."
    mc "Precisely that, she didn't turn me down. But she didn't have sex with me either, just collected semen for nutrients."
    moxie "Interesting... I'm guessing you must have been doing extreme gardening in the forest with Butters."
    mc "Something like that, I wasn't expecting so many unusual anthropomorphic creatures in this world."
    show moxie2 althappy with dissolve
    moxie "Ohh there are countless, almost one for every creature you can imagine."
    mc "What's the strangest one you've met?"
    moxie "Hmm... Insect girls are strange, how did something like that even evolve?"
    mc "Insect girls... What do they look like?"
    show moxie2 happyneutral with dissolve
    moxie "A little like you actually, especially in the face. No fur, just skin and carapace."
    mc "That raises a good point, the Alraune earlier today had remarkably human features in her face, despite her long ears."
    mc "That has to come from somewhere, right?"
    show moxie2 neutral with dissolve
    moxie "Hmm, I dunno. As far as I know there's nothing quite like you around."
    mc "If there are all these creatures, including some that have human features, why are there no humans around?"
    mc "I don't think it's a question of 'why didn't they evolve', more a question of 'what happened to them'."
    show moxie2 althappy with dissolve
    moxie "You might be right, sounds like you should find an expert."
    moxie "The oldest denizens of Arcadia, you know who."
    mc "The Royal sisters... I can try asking them, maybe send a letter."
    show moxie2 laughing with dissolve
    moxie "You should! I'm gonna go cook dinner."
    scene bg black with dissolve
    "..."
    jump evening
label forestvisit3:
    show bg wagonoutside with dissolve
    $ forestvisit3 = 1
    "As soon as I step outside, a strange blue figure is quickly gliding towards me."
    show slimegirl sad with dissolve
    stop ambience fadeout 10.0
    play music hopelessness
    poyo "[playername]! Y-You've got to come to the forest, quick!"
    mc "What's wrong, Poyo?"
    poyo "It's Butters! I don't think the potion worked, she's turned crazy!"
    mc "Crazy? Come on, let's go."
    scene bg arcadiasuburbs with dissolve
    "The slime girl and I jog through the village despite stares of the townsfolk. It's not every day they see two alien creatures in such a panic."
    scene bg foresthouseexteriordark with dissolve
    "Eventually we reach the forest clearing of the cottage, the air feels sinister and there's an unnatural darkness as clouds and tall trees blotch out the rising sun."
    show slimegirl sad with dissolve
    poyo "U-Uhm I'm gonna wait here just in case."
    poyo "Go kick her ass, dad!"
    mc "Sure! W-wait, Dad?"
    poyo "Y-Yeah, you're like my father, y'know... That's why I came to you, I know you can stop Butters..."
    hide slimegirl with dissolve
    "I gulp and look towards the cottage having no idea what to expect, but the panic I saw in Poyo makes me shiver."
    stop music fadeout 3.0
    show bg buttershousedark with dissolve
    "I take a step into the cottage and look around."
    "For some reason, all the lights are turned off, and a hostile darkness blankets every corner."
    "There's an eerie silence, even the birds have stopped chirping."
    play music danger fadein 15.0
    play sound floorboards
    pause 2.0
    show bg buttershousered with Dissolve (5.0)
    "And that's when she walked in."
    pause 2.0
    show butters succubus with dissolve
    butters "HEEELLLLOOO [playername!u]! IT'S SO GREAT TO FINALLY MEET YOU!"
    butters "Ohoho, Butters has told me so much about you."
    mc "B-Butters?"
    butters "Oh, I am so much more than just Butters, babe."
    mc "Did the potion not work?"
    butters "Ahaha, is that what my 'innocent' side thought?"
    butters "Those things never work, she's so desperate that she'll try anything to cure herself."
    butters "Bwahaha, and I hired you to help me? And what did you do? Stand there and watch me get molested twice?"
    butters "You’re an utter failure, I shouldn’t even pay you."
    butters "Seriously, every choice you made was awful."
    butters "I can't even comprehend the fact you joined in when the Alraune and Slime were attacking me. You should have been helping me."
    show butters succsadistic with dissolve
    butters "Now my succubus side is flaring up because of all the sexual stimuli, and I want revenge."
    menu:
        "Snap out of it, Butters!":
            show butters succangry with dissolve
            butters "Snap out of it? Are you serious?"
            butters "Do you have any idea how stimulated I am right now?"
            show butters succhorny with dissolve
            butters "I’ve been so horny these past few days, you couldn’t snap me out of this one with the best orgasm in the world."
        "I’m really sorry, I fucked up.":
            show butters succsurprised with dissolve
            butters "Mmm, apology accepted… I guess…"
            "Her softer side is still in there somewhere, I need to appeal to it."
            show butters succfufufu with dissolve
            butters "But I'm not done with you! You owe me big, hehe..."
    show butters succubus with dissolve
    "Butters flares up completely, a dominating aura surrounding her, I feel myself pushed back from sheer intimidation."
    butters "Indeed, you’ll finally get what you want, I’m going to fuck you."
    menu:
        "Finally, that’s exactly what I want!":
            show butters succsurprised with dissolve
            butters "Eh? You’re enjoying this?"
            mc "It’s kinda hot, yeah."
            show butters succangry with dissolve
            butters "Alright... Don't you realize you're going to die?"
            mc "Ah, I don’t think I want to die, can you do it without the death part?"
            show butters succsurprised with dissolve
            butters "You're serious..? I can try..."
        "On the contrary, I don’t want that at all!":
            butters "Really? You don’t think I’m cute? I think you're so very cute, hehe, I want to ravage you, baby."
            mc "If you want me to be honest, I think you’re very cute."
            mc "I'd be happy to have sex with you, I just don’t want you to suck me to death."
            show butters succangry with dissolve
            butters "Hmph, you know, I've thought about this."
            butters "Succubi are addicted to sex, right? But when we do it, we kill the man!"
            show butters succsad with dissolve
            butters "Wouldn’t it be far more efficient to not kill the man, so we can repeatedly fuck them?"
            show butters succangry with dissolve
            butters "I bet that bastard Umbra messed up the spell, he got what he deserved by making me a lethal succubus instead of one that makes you sleepy."
            "I’m speechless, is she going on a rant in-between trying to intimidate me?"
    "Her softer side is leaking through, I need to keep her talking."
    "My choices might literally be life and death this time."
    show butters succubus with dissolve
    butters "I’ll fuck you softly, 'kay?"
    mc "Softly?"
    butters "I’d get into serious trouble if you died, so I’m going to fuck you gently, got it?"
    show butters succfufufu with dissolve
    butters "Oh and don’t worry, this won’t be painful, it’ll be the best thing you’ve ever felt, just lay back and allow my succubus charms to do their work."
    show butters succubus with dissolve
    "I don’t lay back, I’m actually rather tense, but that doesn’t stop her from seductively walking towards me, her curse mark flaring brightly."
    "Her hands gracefully gliding down her body as one hand finds its way between her legs."
    butters "Ohhh, I’m so wet, even a good girl like me can’t help but drip over you."
    mc "You’re not behaving like a good girl..."
    butters "Not anymore, you’ve awoken the very, very naughty girl."
    butters "Did you know, when I was younger, I’d masturbate every evening? Hehehe, I’ve always been a bad girl."
    "That’s… not naughty at all, even as a succubus she’s painfully naïve"
    "I guess I can’t expect too much of a personality change, she’s still as lovable as ever."
    "The fact she’s trying so hard to tempt me instead of forcing me is actually endearing."
    "It almost makes up for the fact she’s trying to rape me to death... almost."
    show butters succangry with dissolve
    butters "Hmph, you don’t even have a boner, what is going on with you?"
    mc "You haven’t done anything but threaten me with sex and death…"
    show butters succsurprised with dissolve
    butters "Y-Yeah but, my succubus charm!"
    mc "You can't be serious, even your evil side is a pushover? You haven't even touched me."
    show butters succsad with dissolve
    butters "Ohh, that was an option?"
    "Wha? Of course it’s an option, was she planning on fucking me or just awkwardly staring at me?"
    "Her hand reaches for my flaccid penis; I can feel danger signals spiking in my body and I flinch away."
    mc "Wait, I’ve changed my mind!"
    show butters succsurprised with dissolve
    butters "Oh, okay…"
    show butters succsad with dissolve
    mc "Uh…"
    mc "You’re too shy to do anything, aren’t you?"
    butters "M-M-Maybe…"
    butters "I-I'm fighting for you [playername], I'm trying to stop her."
    butters "I-I don't want to hurt you! *Sniff*"
    mc "You can do this Butters! Is there any way I can help?"
    butters "Y-You need to... Need to..."
    show butters succhorny with dissolve
    "She takes a deep breath and grins."
    butters "You need to fuck me, babe."
    show butters succubus with dissolve
    "Butters continues to loom over me, looking at me sharply with her intimidating, glowing red eyes."
    show butters succhorny with dissolve
    butters "I-I’m getting hornier…"
    mc "Huh?"
    show butters succangry with dissolve
    butters "Ahhh, what is this feeling?! Ahh-ahh, am I... in heat?"
    "Her curse mark is glowing a hot red whilst Butters cradles her tummy and grits her teeth."
    mc "Are you okay?"
    butters "I-I need to fuck; I really need to fuck."
    show butters succhorny with dissolve
    "She peers at me with haunting red eyes and a zombie-like lustful look."
    butters "Need to fuck, need to fuck, need to fuck..."
    mc "Not okay!"
    show butters succubus with dissolve
    "Her wings burst outwards and she starts to limp towards me, her dominant hand rubbing between her legs lecherously while she whispers sweet saccharine words."
    label succubuttersmeet:
        pass
    butters "I’m not going to listen to anything you say anymore, we’re going to do it right here, right now."
    "Is this it? Is no one going to save me? Moxie? Poyo?"
    $ time = 3
    $ timer_range = 3
    $ timer_jump = "forestfreeze"
    show screen countdown
    menu:
        "Fight":
            hide screen countdown
            hide butters with hpunch
            "Enough of this bullshit, I charge and, using that momentum, try tackle Butters to the ground."
            "But as a pony she's insanely strong compared to my human frame! My attempt to tackle her is like trying to tackle a boulder."
            "By the time my body connected with hers, she had already reacted and assumed a well-balanced footing. She doesn’t budge at all."
            show butters closesucchorny with dissolve
            butters "My, my, isn’t our little human friend eager for his death?"
            mc "D-Death?"
        "Flight":
            hide screen countdown
            "She’s finally lost it to her succubus side, she has gone insane."
            hide butters with dissolve
            "I try to accelerate into the fastest sprint of my life towards the door."
            "My hands wrap around the door handle as I desperately try to wiggle it open."
            "It’s locked!"
            "She locked the door in secret when I first stepped in, I’m screwed!"
            show butters closesucchorny with dissolve
            butters "Don't try to escape me. I only want to love you, baby."
            "I turn around and as I do, Butters places one hand adjacent to my head against the door in a opposing fashion."
        "Freeze":
            hide screen countdown
            label forestfreeze:
                pass
            show butters closesucchorny with dissolve
            "Butters approaches and leans over me, her breasts swaying, and her tongue lulling."
            butters "Mmm, finally some good fucking food to wash down that awful potion."
            show butters closesuccsatisfied with dissolve
            "She forces me into a kiss, her tongue slithering into my mouth, it’s hot and erotic."
            "The kiss is brief, yet I can already feel blood rapidly flows to my nether."
            "The feeling is similar to the pink aphrodisiacs yesterday."
    show buttershandalt with dissolve:
        xpos 0
        ypos 0
    "Her hand reaches for my cock and starts to jack it back and forth."
    "For some reason her fingers feel tingly, smooth and soft, like a pleasant hug. I can already feel my resistance slipping away."
    "These tingles are like electric sparks of pleasure throughout my body, simultaneously arousing and numbing me."
    "After mere seconds I am painfully erect."
    show butters closesucchorny with dissolve
    butters "No more games [playername], it’s inevitable."
    mc "Can’t we talk about this?"
    butters "No, I won’t let you walk all over me just because you think I’m a shy pushover."
    butters "This time I’m going to push you down and walk all over you."
    hide buttershandalt with dissolve
    show butters succubus with dissolve
    "She pushes me straight down and presses her foot against my erection. I’m not into this at all, but there’s something intoxicating about the touch of her skin."
    "Every time her skin grazes mine it’s exciting and fulfilling. Whenever she doesn’t touch me, I crave more intimacy, I'm completely beguiled by the succubus."
    show butters succubussex1 with dissolve
    "She straddles me and starts to glide her folds against my shaft. I can do nothing but lay there and take it."
    butters "Would you look at that, your delicious cock got so hard for me."
    "Not only am I erect and physically aroused, but even my thoughts are becoming increasingly corrupted by the succubus."
    "Her pussy continues to grind against my shaft, applying more pressure whilst her crimson gaze is fixated on me. It’s incredibly teasing, I want more than this."
    menu:
        butters "Don’t you wish it was inside right now?"
        "Yes!":
            butters "Kehehe, you’re either beguiled or a complete pervert."
        "No!":
            butters "Kehe, your mind may be saying no, but your body can’t resist my charms."
    "Behind my cock I can see her gorgeous pussy, I can’t help but bite my lip, it's so gorgeous and puffy."
    "She’s impeccably thick, I love her thighs and cute tummy, I can’t wait to sink my cock into her."
    butters "Look how wet I am for you, I can’t hold back any longer, my libido is going crazier than ever right now!"
    "My shaft twitches, my libido is going crazy too, even against my will, I can’t help but want more."
    butters "I’m going to put it in, last chance to stop me."
    "I don’t even attempt to stop her, I couldn’t even if I wanted to try, I can’t think of anything but sliding deep inside of her."
    butters "Kehehe, you keep staring at my pussy."
    "She giggles and raises herself causing my cock to pop upwards in the middle of her thighs."
    butters "Ooohh, I love it! I need it!"
    "Butters coos as she goes to lower herself, pressing the tip of my shaft against her entrance, teasingly applying pressure but not allowing the tip to push inwards."
    butters "Mmphh, it’s so difficult resisting sex when you’re a succubus, it was only a matter of time."
    "*Poke*. *Prod*."
    "Precum starts to leak from my tip, just touching her pussy feels immensely pleasurable, causing shivers to run through my entire body."
    "There’s something strange about her juices, it feels like the aphrodisiac from earlier, but exponentially more potent, I can’t think of anything but sex right now."
    butters "I’m going to put it in."
    butters "You can cum prematurely, or you can resist as long as you can, I’ll love it anyway."
    play sound cum
    show butters succubussex2 with dissolve
    "She lowers herself with a schlick, her thighs pressing against my body and her pussy sucking me in."
    "That tingling sensation is heightened greatly as her insides squeeze against my shaft even without a trace of movement. I can feel waves of pleasure crash throughout my body causing me to throb and tense."
    butters "Oohh, it feels so hot inside me, I can feel it pulsate too."
    play ambience sex fadein 2.0
    "She starts to bounce up and down against me, finally! She stalled for so long, but now she’s finally giving it to me, her tight pussy is fucking me, and it feels amazing."
    "Every time she pulls herself up, her small hole tightens up around my penis, then she sinks straight back. This feels fucking good."
    butters "Ahhh, ahh! I never realized how badly I needed this until this very moment."
    "She fucks me with wanton abandon, with each overwhelmingly powerful thrust I can feel my orgasm rush closer, and she has only just started!"
    show butters succubussex3 with dissolve
    butters "Hyaahhh! Ahhhh… This is so good; this is too good! Ahhh!"
    butters "I have no idea how I managed to resist so long; this feeling is worth living for! Ahhh!"
    "My cock is tight and throbbing, I try to hold back, if I let go even for a brief second I’ll explode inside her."
    show butters succubussex2 with dissolve
    butters "Hehe, that’s right. I’ll play with you all day, until you’re worn out!"
    play sound cum
    show butters succubussex4 with cum
    play sound cum
    show butters succubussex4 with cum
    "It’s too much! I release the tension in my cock only briefly and my orgasm erupts, my vision goes white and I start to unload deep into Butters’s pussy."
    butters "Oh heck! Ahhh, you’re cumming already! Such a naughty boy! Aahh!"
    play sound cum
    show butters succubussex4 with cum
    play sound cum
    show butters succubussex4 with cum
    "*Splurt*… *Splurt*… *Splurt*!"
    "My powerful orgasm lasts a long time, completely filling her pussy and leaking outwards, all whilst her pussy sucks and squeezes, adding to the heightened pleasure I’m feeling."
    butters "Aaahh! Yesss! You came so easily! Hehe."
    show butters succubussex5 with dissolve
    "As my orgasm dies down, I usually expect the girl to slow down and stop, but Butters speeds up, fucking me even faster!"
    "My cock would usually start to get sensitive, but it remains rock hard as she pounds away on top of me."
    butters "Kehehe, your confused face is cute, I did say we’re going to play all day."
    "I should have known; her succubus abilities are keeping me hard. I am completely at her whim."
    butters "I could never be satisfied with only one load of cum, even though yours was amazing."
    "She continues to slide up and down, slippery fluids drip down the length of my shaft, a mixture of her wetness and my cum which freely drips out of her pussy."
    butters "Now give me more of that thick human cum! I will absorb it all!"
    "Lewd wet sounds continue to spill uncontrollably from our point of contact, mixing in with the uncontrolled mess of moans from Butters."
    "*Schlick, schlick*… *Thrust*… *Grind*…"
    butters "Aaahhhh, ahhhh! Haahh, haah… My pussy is starting to feel better and better… Mmmm, haahh…"
    "I love the way her breasts bounce up and down with each thrust, I really want to touch them."
    "I had assumed my body may be too weak to move, but my arms move easily. I find myself fondling her breasts, and teasing her nipples. Butters reacts to each sensation with absolute admiration."
    butters "Ohhh yes, please play with my sensitive nipples, I love that!"
    "She arches her back with pleasure, resulting in her beautiful breasts pushing outwards."
    show butters succubussex4 with dissolve
    butters "Aahhh, ahhh, I… I’m gonna come!"
    play sound cum
    "Her pussy starts to contract as she orgasms, going so far as to squirt on me."
    "The contractions cause her insides to tighten around my shaft, forming another set of overwhelming sensations."
    "Even though the numbness in my body seems to be gone, all I can feel is the overpowering pleasure trying to milk me, and force me to cum."
    "I can feel the waves of pleasure crashing up against my body again as another orgasm rapidly builds."
    butters "Mmphh, you’re throbbing again, I want your cum now!"
    "Even she seems somewhat fatigued at this point, her riding started to slow down after her orgasm but it’s still enough to push me over the edge."
    play sound cum
    show butters succubussex4 with cum
    play sound cum
    show butters succubussex4 with cum
    "I don’t even try to hold back this time, I cum inside her, squirting more loads of my thick cum deep into her womb."
    play sound cum
    show butters succubussex4 with cum
    play sound cum
    show butters succubussex4 with cum
    "*Squirt, squirt, squirt*!"
    butters "Kyaaahhhh, ahhhhhh! You’re cumming again! Aahhh, yes!"
    "Her entire body begins to quiver as I cum inside her, her already tight pussy clinging to my shaft."
    stop ambience fadeout 3.0
    show butters succubussex1 with dissolve
    "As I finish pouring my hot, thick semen into her trembling insides, she lifts up and pulls me out."
    hide butters with dissolve
    "Unlike before, my cock goes limp and my body is weary. She’s tired too."
    stop music fadeout 3.0
    if crystalballactivated == 1:
        $ crystalballactivated = 0
        jump cbmenu
    show butters succangry with dissolve
    butters "Haahh, haaahh... W-Why am I so tired?"
    butters "I'm supposed to drain energy, not lose it..."
    show butters succsadistic with dissolve
    butters "Seems like Mister human is still kicking too..."
    butters "Do you feel any pain?"
    mc "I feel fine... Great, actually... The sex was nice..."
    show butters succangry with dissolve
    butters "Hmph, it was a good fuck, I'll give you that..."
    show butters succsatisfied with dissolve
    butters "I guess the potion worked after all, good job innocent me."
    mc "I figured it did, what did the potion do?"
    show butters succfufufu with dissolve
    butters "Seems like it removed my ability to drain life force."
    butters "I gotta hand it to myself, that was a damn smart potion."
    butters "Now I'll be able to freely have sex without killing anyone."
    mc "So... You're normal now?"
    show butters succsadistic with dissolve
    butters "I'm not sure, how about you talk to the smart-ass that's trying to remove me."
    butters "Oh, and if you can, convince her to keep me. Fufufu."
    mc "I dunno about that..."
    mc "Tell me exactly, what are you?"
    show butters succangry with dissolve
    butters "I'd love to talk right now, but I can feel myself drifting away... Come see me again sometime, I'll tell you..."
    play music butters fadein 3.0
    play ambience ambienceday fadein 3.0
    show bg buttershouse with dissolve
    show butters sad with dissolve
    "For a while now her horns have slowly been retracting and a milky white tint has been swirling in her eyes. She's slowly reverting back to her usual form."
    butters "I am so sorry! I'm sorry! Sorry, sorry, sorry!"
    mc "It felt like you wanted me to die at some point during that."
    butters "That was the meanie succubus side! I'm really sorry."
    butters "I-I didn't know she was still there!"
    mc "Could you explain to me what the heck just happened?"
    butters "Well… Give me a few seconds to think about it."
    show butters closesad with dissolve
    "She gets up off me and we both sit down on the sofa."
    butters "I made a huge misjudgement, and it put you in danger, I’m really sorry!"
    mc "What was the misjudgement? The potion worked."
    butters "Yeah, but it caused my succubus side to erupt. I should have been more careful because it was already looming up after the cave incidents."
    mc "Admittedly it was quite a surprise."
    show butters closeneutral with dissolve
    butters "The potion took a while to digest, so the effects occurred slowly over  time."
    butters "The potion seems to have removed my immortality, and my life drain. I regained some of my natural marehood back..."
    show butters closesurprised with dissolve
    butters "But then I immediately went into my first heat in fifty years!"
    butters "Being in heat pushed me over the edge and caused my Succubus side to go crazy."
    mc "That would explain why you didn’t absorb any of my cum, despite saying that’s what you wanted to do."
    "The cum is still dripping out of her pussy as we speak."
    mc "It's wonderful news that you're in heat though, that means you can have a family."
    show butters closehappy with dissolve
    butters "Uuuu, I could get pregnant again!"
    mc "Unfortunately, you won’t get pregnant from a human."
    butters "Maybe I could change that with a potion... But first..."
    show butters closesad with dissolve
    butters "I-I have to get rid of that evil succubus before she tries to hurt anyone else."
    mc "I wouldn't worry much about her, she may seem threatening, but she's as dangerous as your bunny rabbit."
    mc "She's just, well, horny. Now the life drain is gone, she's safe."
    show butters closesurprised with dissolve
    butters "But imagine if the life drain didn't go! I am so, so, so sorry that I put you in danger like that! I-I’ll do anything to make it up for you!"
    show butters closeneutral with dissolve
    butters "A-And you helped me make the potion, you removed my life drain and made me mortal again, I basically owe you my life!"
    mc "It’s okay, I didn’t do a lot if you think about it."
    butters "I’m serious, I’ll dedicate my life to you as a maid or servant if you’d like, I’ll let you live with me!"
    menu:
        "I’ll consider it.":
            show butters closehappy with dissolve
            butters "Ohh, how delightful!"
            butters "I could use a ‘close friend’ now that I have a heat; heat is even worse than the natural succubus hunger! I had no idea."
            mc "Really? It’s that bad?"
            butters "If I was at the peak of my heat, and there was a male with an erection in my proximity, I wouldn’t be able to help myself."
            butters "My mind goes all fuzzy, and before I know it… I’m penetrated!"
            mc "Maybe you really are as naughty as you said."
            butters "Hehe, why do you think I wanted to cure my succubus curse so much?"
            mc "You told me it was so you could settle down and have a family!"
            butters "Exactly, that takes a lot of naughty time!"
        "I don't think so.":
            show butters closesad with dissolve
            butters "Aww... But you’ll visit, right?"
            mc "Yeah of course, once I get over my trauma of Succubus-Butters."
    show butters closehappy with dissolve
    butters "I’ll make it up to you, next time we sleep together I’ll be really sweet and innocent."
    mc "Next time? You want to do it again?"
    show butters closelaughing with dissolve
    butters "I’m like a forest nymph, I wanna do it to everyone all the time."
    butters "And now, I actually can!"
    "We both laugh at her uncharacteristically brash comments. After we've been through so much, it feels like we can say anything to each other."
    mc "So... You still have the wings and curse mark. And the alternate personality, I guess."
    show butters closeneutral with dissolve
    butters "I think the mark could pass as a cool tattoo... and I think I’ll keep the wings, they’re rather useful."
    show butters closeangry with dissolve
    butters "And the other personality... Gosh, that could be another fifty years to cure, I might not have that time."
    butters "Could I ask you a big favour?"
    mc "What's that?"
    show butters closeneutral with dissolve
    butters "If you ever see her again, please talk to her, try and find out more about her."
    butters "I can't because while I occasionally hear her voice, I can't communicate with her at all."
    mc "I'll do my best."
    mc "Are you still going to do alchemy now that you’re cured?"
    show butters closehappy with dissolve
    butters "I did before, and I will continue in the future. I don’t think I’ll go back to the black market though."
    butters "I make quite a bit of monies selling some potions to contacts in Arcadia, but that’s secret!"
    show butters laughing with dissolve
    butters "Ah, and here’s your fair share of monies, consider it a bonus for all the problems I caused for you."
    "Another 35 monies! And I barely did anything except almost die!"
    $ monies += 35
    mc "Thank you Butters, I really appreciate that."
    show butters happy with dissolve
    show slimegirl with dissolve:
        xpos 800
        ypos 250
    poyo "Y-You did it! Butt-head is back to normal."
    show butters neutral with dissolve
    butters "Oh Poyo, can you not?"
    mc "Where were you five minutes ago when I was getting attacked?"
    poyo "She asked me to form a dick; I'm telling ya, she tried to seduce me!"
    butters "How embarrassing..."
    mc "Everything is okay now Poyo, I've had a word with Butters about it."
    poyo "Phew, you're my hero!"
    hide slimegirl with dissolve
    "Poyo slithers into another room leaving me and Butters alone again."
    mc "Mm, so what do you wanna do for the rest of the day?"
    show butters horny with dissolve
    butters "Well... Now I'm in heat... Wanna fuck a bit more?"
    mc "Hmm... Considering I'm still somewhat beguiled..."
    mc "Sure."
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene bg black with dissolve
    play ambience sex fadein 5.0
    butters "Ohhh yes, fuck me harder, [playername]!"
    butters "Mphh, ahh, ahhhh, aaaaahhhhhhhhhhhhh, c-coming!"
    "I fuck that squishy, pillowy, thick ass all day before calling it quits."
    stop ambience fadeout 2.0
    if crystalballdayactivated == 1:
        $ crystalballdayactivated = 0
        jump cbmenu
    "…"
    show bg moxiewagonlamp with dissolve
    show bg moxiebedday with dissolve
    "After the long fuck session, I go back to the wagon and nap until Moxie returns home. The nap helps me forget the scary situation."
    show bg black with dissolve
    "Butters has revealed such a strange, dangerous and alien aspect of the world to me."
    "But what I didn't expect was her to be the most dangerous part of all."
    "But I wasn't in any danger, I don't think so anyway. If the potion didn’t work, she wouldn’t have gone into heat and turned succubus. If the potion did work, I would be safe because the curse would be cured."
    "In theory."
    "Anyway... Why are the flora and fauna of this world such sexual deviants?"
    "Do the tables wanna fuck me too?"
    play ambience ambiencenight fadein 3.0
    show bg moxiebednight with dissolve
    moxie "Honey, I’m home!"
    show bg moxiewagonlamp with dissolve
    play music wagon fadein 3.0
    show moxie2 laughing with dissolve
    mc "Hello! I didn’t hear you come in, one hell of a day."
    show moxie2 happy with dissolve
    moxie "Look at you lazing in bed! You either had one hell of a day at work, or did none at all!"
    mc "Oh uh, just collecting more ingredients for silly potions."
    show moxie2 althappy with dissolve
    moxie "Ahaha, I hope they were tasty ingredients at least, because no magic is ever going to happen."
    "I humour her and cover up the Butters succubus situation, although I do want to ask one thing."
    mc "Is the outside world dangerous? I’ve encountered slimes that wanna suck my dick, and flowers that want to suck it too."
    if farmvisit2 == 1:
        mc "Not to mention I heard about minotaurs in the mountains."
    show moxie2 laughing with dissolve
    moxie "You’re such a wimp! Slimes and the flora that suck your juices are harmless, in fact, everything in this country is harmless."
    show moxie2 althappy with dissolve
    if farmvisit2 == 1:
        moxie "Although... Minotaurs, I wouldn’t mess with, but they don’t mess with us either! If either of us walked past one they’d ignore us, they’re only interested in cows."
    mc "That’s actually very relieving."
    show moxie2 smug with dissolve
    moxie "Keheh, if you wanna hear about dangerous stuff, let me tell you, there are some increasingly inhospitable areas in the world."
    moxie "There are some plants that tire you out with sleeping powder, keep you unconscious until your body rots and becomes nutrients for it."
    mc "That’s awful, and terrifying!"
    show moxie2 happy with dissolve
    moxie "There’s more!"
    mc "No!"
    show moxie2 happyneutral with dissolve
    moxie "There are some creatures called werewolves, if they have sex with you, you’ll turn into one too!"
    mc "Ah yeah, I heard of those. This world is crazy."
    moxie "This is a world of extremes. Dragons bathe in lava, there’s bound to be lots of absurdity out there."
    menu:
        "Tell me more about dangerous stuff!":
            show moxie2 laughing with dissolve
            moxie "You’re interested in this too? I don’t blame you."
            show moxie2 smug with dissolve
            moxie "I told you about insect people earlier, but how about spider people? They’re domestic anthropomorphs just like you and me, but they genuinely eat other anthropomorphs, isn’t that awful?"
            mc "It sounds like there’s an anthro species for every single creature."
            show moxie2 happyneutral with dissolve
            moxie "There are a few anthropomorphs like that, due to their general incompatibility with society they’re rejected, outside of exceptional cases."
            show moxie2 neutral with dissolve
            moxie "You mentioned slimes earlier, the ones here are harmless, but it’s possible to get lava slimes and corrosive slimes too."
            mc "Don’t put your dick in that."
            show moxie2 neutral with dissolve
            moxie "Deep underwater is a dangerous and territorial location for creatures."
            moxie "The conditions are extreme and competitive, so evolution has been aggressive."
            show moxie2 laughing with dissolve
            moxie "I don’t know many details, but I’d stay out of deep waters if I were you. A siren would sooner drown and eat you than suck your dick."
            mc "Duly noted."
        "How can we ensure we’re safe?":
            show moxie2 happyneutral with dissolve
            moxie "Most dangerous creatures don’t live on this continent, and even then, they don’t live close to society."
            moxie "They live in untamed wilderness, caves, deep ocean, deep jungles and deep underground."
            menu:
                "Very deep":
                    moxie "Yup, nothing to worry about."
                "Was that subliminal messaging?":
                    show moxie2 laughing with dissolve
                    moxie "Hehe, all three ‘deep’ locations make for a good innuendo, I don’t know which one to pick."
    show moxie2 happy with dissolve
    moxie "Is your world really that boring?"
    mc "My species has tamed almost the entirety of the planet; I’m never worried about flowers trying to seduce me while walking a dog."
    show moxie2 laughing with dissolve
    moxie "Ohh, your world sounds boring, what if you got horny while walking?"
    mc "I think I could wait, rather than finding a curvy looking tree with a hole."
    show moxie2 happyneutral with dissolve
    moxie "Hahaha same, I’d never want to have sex with any of the flora or fauna, I don’t understand mares that do."
    mc "Is having sex with the wildlife common?"
    show moxie2 happy with dissolve
    moxie "Nah, it’s a niche fetish, I only know about it because of porn categories."
    "I want to browse the pony net and watch extreme pony porn now."
    scene bg black with dissolve
    "…"
    jump evening
label buttersmenu:
    stop music fadeout 3.0
    if butterspregnanteasteregg >= 60:
        jump butterspregnanteasteregg
    if butterspregnant == 2:
        scene bg buttershouse with dissolve
        play ambience ambienceday
        $ butterspregnant = 3
        jump buttersimpregpaizuri
    $ rand = renpy.random.randint(1,2)
    if buttersforestvisit4 == 0:
        jump buttersnormal
    if rand == 1:
        stop ambience fadeout 3.0
        jump butterssucc
    else:
        play music butters fadein 3.0
        jump buttersnormal
label buttersnormal:
    if buttersimpregintro == 0 and buttersgifts > 1:
        show bg buttershouse with dissolve
        $ buttersimpregintro = 1
        jump buttersimpregintro
    if livingwithbutters == 1:
        show bg buttershouse with dissolve
        show butters dresshappy with dissolve
        butters "You didn't get far, did you want to work with me today?"
    else:
        show bg foresthouseexterior with dissolve
        "It's a bright and sunny day as I walk to Butters's cottage."
        show bg buttershouse with dissolve
        show butters dresshappy with dissolve
        if buttersforestvisit4 == 0:
            $ buttersforestvisit4 = 1
            butters "Hey [playername], you're just the human I've been looking for."
            mc "There are others?"
            butters "Aha, unfortunately not, which makes you even better!"
            mc "What's up, want me to jump into more dangerous caves?"
            butters "Well, that's precisely it. These last two incidents with the slime and the alraune weren't dangerous, but they had me thinking..."
            butters "It was inefficient and exhausting to trade sex for ingredients, it would be better if we had some equipment to be more... 'forceful'?"
            mc "Hmm... Equipment?"
            butters "If you could go to the market and buy some spelunking equipment, armor, and perhaps weapons, we would get a better yield for our potions."
            butters "Better yield, equals more pay, right?"
            mc "That sounds great."
            butters "Right now I can pay you [forestmonies] monies per spelunk, but with some proper equipment we could adventure into deeper caves and get rarer ingredients."
            mc "I'll start by buying ropes and basic gear to protect ourselves then."
            butters "Perfect, this'll pay off, I guarantee it."
            "Next time I'm at the market, I'll have to see what's available."
            butters "Oh, and one more thing."
            butters "You're welcome to live here if you'd like."
            mc "Really?"
            butters "Really, it's the least I can do for you after the jeopardy I put you through, in the face of everything you've done for me."
            jump buttersnormalmenu
        butters "Ohh, hey! It's great to see you [playername]. Would you like some breakfast?"
        mc "Ohh no, no thanks."
        butters "Ahh, what's on your mind then?"
    menu buttersnormalmenu:
        "Shop":
            butters "Ohh? What would you like to buy?"
            butters "I don't really have a shop setup, so... Just browse a few items and tell me if anything catches your eye."
            butters "Then maybe we can haggle a good price for you."
            menu buttersshopmenu:
                "Crystal Ball" if crystalball == 0:
                    mc "What's this?"
                    butters "The crystal ball caught your eye? It's an orb that shows you previous memories in vivid detail."
                    mc "So I could like... Watch myself having sex with a girl?"
                    butters "Yup, in first person too. It's quite spectacular to re-experience events again."
                    mc "You sure you want to sell this?"
                    butters "I owe you remember? And, anyway, I have another in my bedroom."
                    mc "How much?"
                    butters "Let's say 200 monies?"
                    mc "That sounds like a good price."
                    menu:
                        "I have [monies] monies."
                        "Yes" if monies >= 200:
                            butters "Perfect! I'll wrap it up for you."
                            $ crystalball = 1
                            $ monies -= 200
                            "From now on you'll be able to access 'memories' during the day at Moxie's wagon."
                            jump buttersshopmenu
                        "I'll pass.":
                            jump buttersshopmenu
                "Lust-Enhancing Potion.":
                    "I really have no reason to buy this. Mares are horny enough anyway."
                    "Butters notices me looking at it and comments."
                    butters "You won't need that to win me over."
                    "See? I don't need it."
                    jump buttersshopmenu
                "Werewolf Cure Potion" if zoe == 0:
                    mc "Hey Butters, why do you have this?"
                    show butters dresssurprised with dissolve
                    butters "Hmm? Why are you looking at me like that? You don't think I turned into a werewolf do you?"
                    mc "Uhh, I couldn't possibly say."
                    show butters dressneutral with dissolve
                    butters "I was a succubus, I wouldn't want to hurt any Mr. Wolfies out there."
                    show butters dresshappy with dissolve
                    butters "This is one of my commissioned potions, it was a lot easier to make compared to the succubus potion."
                    butters "I keep one available, just in case that same female friend feels like having another werewolf gangbang and needs me again."
                    mc "Huh..."
                    jump buttersshopmenu
                "Corruption Potion":
                    mc "What's this ambiguous red fluid?"
                    butters "One of my early attempts at a succubus cure."
                    butters "Remember when we talked about a potion that would turn you into a nymph without a dewblossom to reverse the effects? This is similar."
                    butters "While this potion doesn't turn you into a succubus or nymph, it exhibits a corrupting influence, making you more evil and lustful."
                    butters "I was only keeping this around as a control for tests, but I guess I don't need it anymore."
                    butters "I could even turn this into a purity potion with a touch of dewblossom."
                    jump buttersshopmenu
                "Bunny Potion":
                    mc "What’s this potion here?"
                    show butters dresssurprised with dissolve
                    butters "Ohh, that’s one I made while experimenting with gelatine."
                    butters "While attempting to cure my curse, I tried to make a potion that would revert me to my original ‘anthropomorphic’ form."
                    butters "But it turns out, it doesn’t do anything to me at all."
                    butters "So, I decided to give it to Devil as a small test, and it turns out the potion does work! It’s an anthropomorphising potion."
                    butters "For an entire day she was an intelligent humanoid just like you and I. A little clueless because she had no knowledge of the world, but it was a lot of fun."
                    mc "Is that so… Can we try it?"
                    show butters dresshappy with dissolve
                    butters "Sure, but the ingredients are quite expensive. You’ll have to pay me if you want to use some."
                    mc "How much?"
                    show butters dressneutral with dissolve
                    butters "Probably 100 monies, sorry [playername], that’s the best price I can do."
                    show butters dresshappy with dissolve
                    butters "But… On the bright side, the last time I used one of these potions Devil mentioned that she wanted to try sex while anthropomorphised…"
                    menu:
                        "Bang the Bunny?" if monies >= 100:
                            $ monies -= 100
                            butters "Pleasure doing business for you!"
                            mc "You realize you’re pimping out your pet, right?"
                            butters "N’aww, you’re silly."
                            butters "Now, here’s the potion, and here’s the bunny. You can use my bedroom, have fun now!"
                            jump devilsex
                        "Too pricy!":
                            mc "Hm… On second thought, that’s quite a lot of money just to turn your pet rabbit humanoid for the day."
                            butters "Sorrryyy. I think you should try it sometime though."
                            jump buttersshopmenu

                "Nevermind":
                    jump buttersnormalmenu
        "Sex" if butterssexfta == 0:
            $ butterssexfta = 1
            butters "No sex until we've finished work, mister! Ehehe."
            "Looks like Butters will only have sex with me after work."
            "But what about her succubus side? That's always worth a try."
            jump buttersnormalmenu
        "Work":
            butters "Perfect, you're just the man for the ingredients I'd like to get today."
            butters "Let's see here... With the equipment you have, we should be able to get enough ingredients to make [forestmonies] monies."
            mc "Sounds good to me, let's go!"
            stop ambience fadeout 3.0
            scene bg cave2 with dissolve
            if forestmonies == 25:
                "Butters and I spleunk all day, occasionally struggling when we run into a creature or dead end."
            elif forestmonies == 35:
                "Butters and I spleunk like a team, gathering more ingredients than usual."
            elif forestmonies == 45:
                "Butters and I spleunk with experienced intent, going deeper and getting better ingredients than before."
            elif forestmonies == 55:
                "Butters and I spleunk like pros all day without incident."
            play ambience ambiencenight fadein 3.0
            scene bg buttershouse with dissolve
            "When we return, Butters and I spend a few hours creating batches of potions."
            scene bg buttershousenight with dissolve
            show butters dresshappy with dissolve
            butters "Great job out there today."
            $ rand = renpy.random.randint(1,3)
            if rand == 3:
                butters "You really showed that slime that tried chasing us!"
                mc "She wouldn't leave us alone! I didn't think she'd cry from just an insult."
            elif rand == 2:
                butters "I can't believe we ran into a fairy, did you even know they native to this region?"
            else:
                butters "Even though we spent a while having sex after lunch, we got a pretty good yield."
                mc "It re-energised us, I'm telling ya."
            butters "Anyway, here's your pay! [forestmonies] monies."
            if forestmonies == 25:
                $ monies += 25
            elif forestmonies == 35:
                $ monies += 35
            elif forestmonies == 45:
                $ monies += 45
            elif forestmonies == 55:
                $ monies += 55
            else:
                pass
            jump eveningbuttersmenu
        "Leave":
            butters "Going out to work? Have fun!"
            pass
        "You mentioned I could live here?" if livingwithbutters == 0:
            show butters dresslaughing with dissolve
            butters "If you'd like to stay, of course you'd be welcome."
            show butters dresshappy with dissolve
            butters "Would you like to live here? Rent free, naturally."
            menu:
                "Sure thing.":
                    $ livingwithbutters = 1
                    $ livingwithmoxie = 0
                    butters "This is going to be so much fun!"
                    show butters dresslaughing with dissolve
                    butters "You're going to love it here!"
                    if livingwithbuttersfirsttime == 0:
                        $ livingwithbuttersfirsttime = 1
                        "Guess I need to break the news to Moxie."
                        scene bg black with dissolve
                        "..."
                        stop music fadeout 3.0
                        play ambience ambiencenight fadein 3.0
                        show bg moxiewagonlamp with dissolve
                        if fr == 1:
                            show moxie whappyneutral with dissolve
                        else:
                            show moxie happyneutral with dissolve
                        play music wagon fadein 3.0
                        moxie "You're going to stay with Butters? Of course, I'm happy for you."
                        moxie "She's a bit of an oddball, but if she isn't charging rent, I'd say go for it."
                        moxie "You're only a walk away after all, you can visit me any time you want, and hey, maybe I'll visit you too!"
                        mc "Are you sure? I feel a bit guilty about this."
                        if fr == 1:
                            show moxie wlaughing with dissolve
                        else:
                            show moxie laughing with dissolve
                        moxie "Oh please, you're a grown man, and I don't even feel a tiny bit jealous, or sad."
                        mc "Really?"
                        if fr == 1:
                            show moxie whappyneutral with dissolve
                        else:
                            show moxie happyneutral with dissolve
                        moxie "Really, really! I always wanted you to outgrow this tiny place."
                        if fr == 1:
                            show moxie wlaughing with dissolve
                        else:
                            show moxie laughing with dissolve
                        moxie "But do visit, you are special to me aaannnddd, I wanna fuck you at least once a week."
                        mc "Deal!"
                        if fr == 1:
                            show moxie whorny with dissolve
                        else:
                            show moxie horny with dissolve
                        moxie "Actually, uhm..."
                        stop music fadeout 3.0
                        scene bg black with dissolve
                        pause 1.5
                        show bg moxiebednight with dissolve
                        pause 0.75
                        play music sex1
                        if fr == 1:
                            show moxie wdoggystyle4 with dissolve
                        else:
                            show moxie doggystyle4 with dissolve
                        play ambience sex
                        moxie "Oh yeah, yeah, yeah! I'll always be your number one bad bitch, aahh haaah!"
                        play sound cum
                        if fr == 1:
                            show moxie wdoggystyle6 with dissolve
                        else:
                            show moxie doggystyle6 with dissolve
                        moxie "Aaahhh fuck yeah! Fill me up! Mmmphhh..."
                        stop ambience fadeout 2.0
                        scene bg black with dissolve
                        "..."
                        "Moxie and I aggressively and energetically rut long into the night, until we doze off together."
                        stop music fadeout 3.0
                        show bg moxiebedday with dissolve
                        "In the morning I kiss Moxie goodbye and make my way to my new home."
                        show bg moxiewagonday with dissolve
                        scene bg black with dissolve
                        "..."
                        jump altmorning
                    else:
                        jump buttersnormalmenu


                "I'll pass, but thanks for your offer.":
                    jump buttersnormalmenu
    if fr == 1:
        jump prefinalworldmap
    jump preworldmap
label butterssucc:
    show bg foresthouseexterior with dissolve
    stop music fadeout 2.0
    stop ambience fadeout 2.0
    "It's quiet and eerie as I walk to Butters's cottage."
    show bg buttershousered with dissolve
    play music danger fadein 2.0
    show butters succubus with dissolve
    butters "Ohoh, breakfast has arrived! Perfect..."
    menu butterssuccmenu:
        "Shop":
            butters "You want to buy something? From me?"
            butters "If I were you I'd wait until I was 'sober', but whatever. Just browse a few items and tell me if anything catches your eye."
            menu butterssuccshopmenu:
                "Crystal Ball" if crystalball == 0:
                    mc "What's this?"
                    butters "That ol' ball lets you look at previous memories in vivid detail, Butters used that quite a lot when working to remember and document things."
                    butters "She always had a poor memory."
                    mc "So I could like... Watch myself having sex with a girl?"
                    butters "Your mind is almost as one-track as mine. You can watch all the VR sex you want with this, minus the cuckoldry!"
                    mc "You sure you want to sell this?"
                    butters "Yeah I'm not bothered, I'm sure Butters ain't either, there's another in the bedroom."
                    mc "How much?"
                    butters "Let's say 200 monies?"
                    mc "That sounds like a good price."
                    menu:
                        "Yes" if monies >= 200:
                            butters "Awesome, I dunno why you couldn't have just shared mine, but whatever."
                            $ crystalball = 1
                            $ monies -= 200
                            "From now on you'll be able to access 'memories' during the day at Moxie's wagon."
                            jump butterssuccshopmenu
                        "I'll pass.":
                            jump butterssuccshopmenu
                "Lust-Enhancing Potion.":
                    "I really have no reason to buy this. Mares are horny enough anyway."
                    "Butters notices me looking at it and comments."
                    butters "This is the potion I spike your drinks with."
                    "What the fuck."
                    jump butterssuccshopmenu
                "Werewolf Cure Potion" if zoe == 0:
                    mc "Hey Butters, why do you have this?"
                    show butters succsurprised with dissolve
                    butters "What? You think I fucked a werewolf at some point?"
                    mc "Uhh, I couldn't possibly say."
                    show butters succneutral with dissolve
                    butters "You should know, I never fucked a single other person after the trauma of killing Umbra."
                    mc "Until me..."
                    butters "... Anyway, this potion was commissioned from a slutty friend that enjoyed getting knotted by werewolves but didn't enjoy the consequences."
                    butters "I don't see why she can't just fuck regular wolves like the rest of us, right [playername]?"
                    mc "Right...? No, not right, what the hell?"
                    show butters succubus with dissolve
                    butters "That's a joke, no need to be so gullible."
                    jump butterssuccshopmenu
                "Corruption Potion":
                    mc "What's this ambiguous red fluid?"
                    butters "Another failed attempt at a succubus cure."
                    butters "You'd be surprised just how many attempts actually made it fuckin' worse! LMAO!"
                    mc "How does it work?"
                    butters "Well, you know the difference between my regular form and normal form?"
                    butters "Black eyes, wings flare out, horns magically appear and my eyes get all glowy and shit?"
                    butters "This potion aids transformations like that, it makes you more 'evil'-like."
                    butters "With enough of this, even regular ol' pure Butters would look just like me. And fuck, maybe even act like me too!"
                    butters "Want me to try downing it and testing that theory?"
                    mc "I'd rather not subject her to that."
                    jump butterssuccshopmenu
                "Bunny Potion":
                    mc "What’s this potion here?"
                    butters "That’s one of the failed potions I made to try and cure the curse."
                    butters "For some strange reason my other self-thought she could reverse engineer the effects of the curse using a potion that turns creatures into an anthropomorphic version of themselves."
                    butters "Of course, that was a complete failure. Hahah. It did nothing at all!"
                    butters "Though, I did have a lot of fun with the bunny rabbit, turns out it works perfectly on her."
                    butters "For an entire day Bunny was an intelligent humanoid just like me, and maybe even smarter than you. When my other self wasn’t looking, we had a lot of fun."
                    mc "Is that so… Can we try it?"
                    butters "Hell yeah, I’d be happy to pimp out my pet for you. How about 50 monies?"
                    mc "You’re charging me?"
                    butters "Well, this is a shop. I don’t want to get in trouble with the boss."
                    menu:
                        "Bang the Bunny?" if monies >= 50:
                            $ monies -= 50
                            butters "Sweet. Now, you’d probably expect me to join you, but I think I’d scare her off based on what happened last time…"
                            mc "What happened last time?"
                            butters "Here’s the potion, and here’s the bunny. Have fun now!"
                            jump devilsex
                        "Too pricy!":
                            mc "Hm… On second thought, that’s quite a lot of money just to turn your pet rabbit humanoid for the day."
                            butters "Okay. I think you should totally try it sometime. She's very tight."
                            jump butterssuccshopmenu

                "Nevermind":
                    jump butterssuccmenu
        "Sex":
            menu morningbutterssuccsexmenu:
                "Cowgirl":
                    stop music fadeout 3.0
                    scene bg buttersbedday with dissolve
                    show butters succhappy with dissolve
                    "The two of us saunter over to the bedroom and I lay down on the bed, prepared to get the ride of a life-time."
                    show butters closesucchorny with dissolve
                    "She seductively wiggles her hips as she approaches and mounts me."
                    show butters succubussex1 with dissolve
                    play music sex1 fadein 3.0
                    butters "I'm not like my other side, I like to get down to business, got it?"
                    mc "Of course, let's rut like sex-crazed maniacs."
                    "My body grows hot at the display and my cock grows to point upwards against her belly, her feminine lubricant dripping down my shaft as she lustfully grinds against it."
                    show butters succubussex2 with dissolve
                    "Butters doesn't waste any time with foreplay, she arches her back while sliding her plush ass onto my cock."
                    "She sinks down onto my cock with a deliberate slowness, not once breaking eye contact."
                    "Her insides squeeze as her pussy spreads until she's finally at the hilt, fully impaled by every inch of my length."
                    butters "Oohh, I love how your cock squeezes every inch of my pussy... We're gonna have some fun..."
                    play ambience sex fadein 3.0
                    "She coos and rubs her clit for a few seconds while her hips begin to grind back and forth."
                    "Her tight, wet pussy squeezes and sucks around my cock in rhythmic motions as if her pussy is trying to drain me dry."
                    "Her powerful succubus sex qualities tingle through my body and deliver immense pleasure, beyond the standards of any other mare."
                    "She bites her lip when she notices my hips rocking to match her own pace, bouncing her up and down and making her large pillowy tits jiggle as the intensity increases."
                    butters "Haahh, this feels really good. I think it's time you let me have a taste of your cum, right darling?"
                    "Her movements are adept as she takes my entire cock from glans to hilt in her rapid assault of thrusts."
                    "In no time at all, my cock is feeling tight and full, almost ready to burst into Butters's dribbling cunt."
                    play sound cum
                    show butters succubussex4 with cum
                    play sound cum
                    show butters succubussex4 with cum
                    "My cock swells and suddenly releases a torrent of seed deep into her pussy and womb, sending the riding succubus into a fit of ecstasyand almost immediately making her come too."
                    play sound cum
                    show butters succubussex4 with cum
                    play sound cum
                    show butters succubussex4 with cum
                    butters "Ohh fuck yeah! Mmmphh, ahhh, aaahhh!"
                    "She continues to ride my cock eagerly, never satisfied with just one load of cum."
                    "After a few minutes of more rapid thrusts, this time bubbling and squelching with cum I feel close to a second orgasm."
                    show butters succubussex5 with dissolve
                    butters "Are you ready baby? My womb is waiting..."
                    play sound cum
                    show butters succubussex4 with cum
                    play sound cum
                    show butters succubussex4 with cum
                    "My body tenses and my mind is overwhelmed with euphoria as my orgasm is unleashed; a second torrent of hot cum erupts deep into Butters's eager pussy."
                    play sound cum
                    show butters succubussex4 with cum
                    play sound cum
                    show butters succubussex4 with cum
                    butters "Ahhh, ahhh, yes! Don't hold back, [playername]!"
                    "She quivers, riding with increased passion as her womb is filled up. Her eyes rolling back as she has another powerful orgasm."
                    "Butters's tongue hangs lewdly from her mouth as she's pumped with multiple loads of my cum, far more than I should ever let out in a regular orgasm, let alone my second in a row."
                    stop ambience fadeout 3.0
                    hide butters with dissolve
                    "We're both left panting as she flops off me, grinning blissfully and rubbing her curse mark satisfied."
                    show butters closesuccsatisfied with dissolve
                    butters "Mmm... Proper sex feels far too good, so glad I don't have to just masturbate and fuck the occasional plant."
                    scene bg black with dissolve
                    "Having sex with Butters reverted her back into her normal form."
                    show bg buttershouse with dissolve
                    show butters dresshappy with dissolve
                    butters "Phew, now that's over, I can get to work!"
                    jump buttersnormalmenu
                "Reverse-Cowgirl" if butterschocolates == 1:
                    scene bg buttersbedday with dissolve
                    play music sex1 fadein 3.0
                    "The two of us saunter over to the bedroom and she pushes me down onto the bed."
                    show butters closesucchorny with dissolve
                    butters "Oh yeah, I'm gonna fuck you real good."
                    "Butters turns around and wiggles her butt with a lecherous grin, while she begins to stroke my cock."
                    butters "Ohh, you got erect so quickly, I didn't even need to use any succubus trickery to get you rock hard..."
                    mc "Hey, you're hot, no trickery needed."
                    butters "Heh, you flatter me... And I flatten you..."
                    show butters succreversecowgirl1 with dissolve
                    "She coos and kisses the tip of my cock to give it a little bit of succubus magic, before straddling me and lustfully lowering herself, sliding down my cock in one smooth motion."
                    "With my cock fully buried inside of her, I spread her pillowy cheeks with my hands and get a good view of her dripping wet pussy."
                    butters "Ooo, getting touchy are we? I wouldn't be able to resist either if I were you, tehehe."
                    "She begins to grind her hips back and forth, occasionally thrusting up and down as she energetically rides me."
                    butters "Ahhh, ahhh... I'm glad you're my partner [playername], I bet there's no cock quite like yours..."
                    mc "It's true!"
                    "In response, I rock my hips into her movements causing her ass to thwap against me with the force of us both in our rut."
                    "Butters giggles and moans with glee as she lecherously gyrates and bounces against me for long salacious minutes that leave us both in euphoria."
                    "Her succubus pussy is even more pleasureful than her regular form, forcing my cock to cum far sooner."
                    play sound cum
                    show butters succreversecowgirl2 with cum
                    play sound cum
                    show butters succreversecowgirl2 with cum
                    butters "Ohh, ohhh! That came outta nowhere! Mmmphh..."
                    "She doesn't stop riding for a second, and thanks to her succubus magic my cock stays rock hard in her pussy."
                    "With my cum dripping inside of her, she orgasms too, her pussy constricting around my cock with purpose."
                    "She continues to ride for a further few minutes, basking in the glory of yet anonther orgasm while denying me mine."
                    "Eventually she takes mercy and her slick, wet pussy rides me fast enough to push me over the edge."
                    play sound cum
                    show butters succreversecowgirl2 with cum
                    play sound cum
                    show butters succreversecowgirl2 with cum
                    "I finally climax in unison with her as a torrent of my semen unloads into her waiting womb."
                    play sound cum
                    show butters succreversecowgirl2 with cum
                    play sound cum
                    show butters succreversecowgirl2 with cum
                    butters "Mmmm, mmphhh, fill my impure womb! Ahhh, aahhhh!"
                    hide butters with dissolve
                    "After the peak, she collapses backwards and cuddles into my chest. Her horn almost bashing me in the head with her carelessness."
                    scene bg black with dissolve
                    "Having sex with Butters reverted her back into her normal form."
                    show bg buttershouse with dissolve
                    show butters dresshappy with dissolve
                    butters "Phew, now that's over, I can get to work!"
                    jump buttersnormalmenu
                "Leg-Up Doggystyle" if buttersroses == 1:
                    scene bg buttersbedday with dissolve
                    play music sex1 fadein 3.0
                    butters "You wanna be in control? Think you can handle being on-top with a succubus? Ahaha."
                    hide butters with dissolve
                    "She hovers to the bedroom with her wings before seductively kneeling down onto the bed, face first into a pillow."
                    show butters succlegupdoggy1 with dissolve
                    "In an incredibly erotic display, her rump raises, followed by one of her legs."
                    "Her soaking wet and ready pussy drips down onto the bed sheets, and the tip of her succubus tail flicks back and forth."
                    butters "Mmm, I'm all yours baby..."
                    "I bring one hand under her raised leg, and another to her hip as I brush the tip of my cock against the lips of her vulva."
                    butters "No teasing, fuck me hard!"
                    show butters succlegupdoggy2 with dissolve
                    "Her rump pushes back into me slightly and I respond by pushing into her even harder. Pushing my cock all the way into her warm, inviting pussy in one smooth motion."
                    show butters succlegupdoggy2deep with dissolve
                    "Immediately it constricts around me, squeezing and tightening around my shaft."
                    butters "Aahh! Mmmphhh, w-wow, it feels weird not being on top... Ahhh..."
                    show butters succlegupdoggy2 with dissolve
                    show butters succlegupdoggy2deep with dissolve
                    "I grip her hips and leg and begin thrusting into her soft pillowy ass, pulling out as far as I can before slamming myself back into her needy pussy."
                    show butters succlegupdoggy2 with dissolve
                    show butters succlegupdoggy2deep with dissolve
                    "Her eyes roll back as I slam into her, each thrust elicits a moan of pleasure from my horny lover."
                    show butters succlegupdoggy2 with dissolve
                    show butters succlegupdoggy2deep with dissolve
                    "She squirms and groans under my assault, her pussy contracting as her easily earned orgasms start to overwhelm her body with pleasure."
                    show butters succlegupdoggy3 with dissolve
                    show butters succlegupdoggy4 with dissolve
                    "As she climaxes, her insides squeeze down around my shaft and she cries with pleasure."
                    show butters succlegupdoggy3 with dissolve
                    show butters succlegupdoggy4 with dissolve
                    "Her back arches, and her tits mash against the bed sheets below as her body quivers in response to the overpowering sensations."
                    show butters succlegupdoggy3 with dissolve
                    show butters succlegupdoggy4 with dissolve
                    "My cock erupt inside of her and we both cum in unison, both losing our minds in the primal heat of the moment."
                    play sound cum
                    show butters succlegupdoggy5 with cum
                    show butters succlegupdoggy5deep with dissolve
                    butters "Aahh, ahhh... Y-You're really good at this... I should have expected it from the alpha that fucks all the local mares..."
                    show butters succlegupdoggy6 with dissolve
                    butters "Mmphh... Don't think I'm satisfied with just one load... Keep going lady-killer."
                    "I continue to fuck her cum filled pussy for a few minutes, and she comes a few times turning this once dominant succubus into a slutty submissive mess."
                    show butters succlegupdoggy5 with dissolve
                    show butters succlegupdoggy5deep with dissolve
                    "My cock throbs and my orgasm teeters on the edge, her pussy just feels too good."
                    butters "Fill her up again! So much delicious cum!"
                    play sound cum
                    show butters succlegupdoggy5 with cum
                    show butters succlegupdoggy5deep with dissolve
                    play sound cum
                    show butters succlegupdoggy5 with cum
                    show butters succlegupdoggy5deep with dissolve
                    "I grit my teeth and with one last, mighty thrust, my cock swells and begins to launch several blasts of thick cum into her."
                    play sound cum
                    show butters succlegupdoggy5 with cum
                    show butters succlegupdoggy5deep with dissolve
                    play sound cum
                    show butters succlegupdoggy5 with cum
                    show butters succlegupdoggy5deep with dissolve
                    butters "Aahh, so much... Oooo..."
                    show butters succlegupdoggy6 with dissolve
                    "Exhausted, I pull out my cock, along with a glop of sex fluids."
                    "She grins behind the pillow and enjoys the feeling of my hot cum dripping out of her pussy before we snuggle together."
                    scene bg black with dissolve
                    "Having sex with Butters reverted her back into her normal form."
                    show bg buttershouse with dissolve
                    show butters dresshappy with dissolve
                    butters "Phew, now that's over, I can get to work!"
                    jump buttersnormalmenu
                "Back":
                    jump butterssuccmenu
        "Work":
            label butterssuccwork:
                pass
            show butters succangry with dissolve
            butters "Really? You're going to make me work?"
            mc "Well yeah, you're not living in that body rent free."
            butters "But I don't want to!"
            mc "If you don't help us out, Butters will get rid of you."
            show butters succsurprised with dissolve
            butters "Wha? I'll help, I promise! Let's go!"
            stop ambience fadeout 3.0
            stop music fadeout 3.0
            play ambience ambiencecave
            scene bg cave2 with dissolve
            $ rand = renpy.random.randint(1,2)
            if rand == 1 and succworksex == 0:
                $ succworksex = 1
                $ secretsunlocked += 1
                "You've unlocked a secret scene! Requirements met: Work with Butters while she's a succubus. 50%% chance."
                jump succworksex
            "Butters and I spleunk all day, her succubus form is brutally efficient."
            play ambience ambiencenight fadein 3.0
            scene bg buttershousenight with dissolve
            show butters succneutral with dissolve
            butters "Thank god that's over."
            $ rand = renpy.random.randint(1,3)
            if rand == 3:
                butters "Are we gonna have sex yet?"
            elif rand == 2:
                butters "Sorry for trying to rape you half-way through."
            else:
                butters "Oh, and thanks again for the quick blowjob, I was parched."
            butters "Let's see... I think you're supposed to get [forestmonies] monies."
            show butters succhappy with dissolve
            butters "Uhm, what now? Can we bang yet?"
            if forestmonies == 25:
                $ monies += 25
            elif forestmonies == 35:
                $ monies += 35
            elif forestmonies == 45:
                $ monies += 45
            elif forestmonies == 55:
                $ monies += 55
            else:
                pass
            jump eveningbutterssuccmenu
        "Talk" if succbutterstalks == 0:
            jump butterssucctalk
        "Leave":
            if fr == 1:
                jump prefinalworldmap
            jump preworldmap
    label butterssucctalk:
        menu:
            "Who are you exactly?":
                mc "Who are you exactly?"
                show butters succsadistic with dissolve
                butters "Hard to say. I've asked myself that question a few times too."
                butters "Am I the spirit of another? Am I merely a dark alterative personality of Butters?"
                butters "I killed the only person that could answer that in a fit of lust."
                mc "You do act a lot like Butters sometimes, don't you think?"
                show butters succangry with dissolve
                butters "I've been stuck here for a very long time [playername], she rubs off on me."
                show butters succneutral with dissolve
                butters "But I actually agree with you, my theory is that I'm simply a succubus version of Butters."
                butters "Whatever I am, I'm a part of her now, she can't get rid of me."
                mc "Don't worry, you're not exactly a priority."
                mc "As long as you're not a nuisance."
                show butters succsatisfied with dissolve
                butters "I know my place, if I act too wild Butters would be thrown in jail and I'd be stuck too."
                show butters succfufufu with dissolve
                butters "So you ain't gotta worry about little ol' me."
                mc "Sure, don't think I forgot that you tried to kill me once though."
                show butters succangry with dissolve
                butters "But I told you I'd try to avoid killing you!"
                mc "That you did, but it doesn't change the fact."
                butters "Well... I'm not apologising, that's just who I am."
                mc "Guess we're at a stand-still then."
            "What do you want out of life?":
                mc "So... What's your end-goal here? How are you trying to live a fulfilling life?"
                show butters succangry with dissolve
                butters "Don't say that existential crap, it's bad enough living as an alternate personality."
                mc "What do you want out of life though?"
                show butters succneutral with dissolve
                butters "Whatever makes Butters happy, makes me happy, vice versa."
                mc "Oh really?"
                show butters succhappy with dissolve
                butters "Yep, so I guess the meaning of my life is simply to make Butters happy."
                mc "That's quite sweet."
                butters "Not a lot else I can do, you're the only person I can talk to, and have sex with."
                mc "Is that why you've started appearing when I'm around?"
                show butters succneutral with dissolve
                butters "Guess so, I appreciate the company."
                butters "Keep giving it to me, and we can make Butters double happy."
                mc "I don't think it works like that. But I don't mind spending time with you to make {i}you{/i} happy."
                show butters succlaughing with dissolve
                butters "Well damn, you're gonna make this black heart swoon."
            "Ever catch Butters doing anything weird?":
                mc "You're always observing Butters' actions, right?"
                butters "More or less, we share a memory."
                mc "That means she's observing your actions too?"
                butters "Yep, once I turn back after a good nap, sex or a whack to the head, she'll remember everything."
                mc "Huh, interesting... Ever catch Butters doing something weird?"
                show butters succlaughing with dissolve
                butters "Ahaha, she'd hate me if I told you, but when she masturbates she says your name."
                mc "Really? How long has she been doing that?"
                show butters succhappy with dissolve
                butters "It's a recent thing, guess we know what she's imagining."
                butters "I'll let you in on another secret, I imagine the same thing too."
                mc "Why me? You two have a crush or something?"
                butters "I guess we do, but we're not exactly subtle about it."
                show butters succneutral with dissolve
                butters "I mean she offered to dedicate her life to you, you could practically ask her to marry you and she'd say yes."
                butters "Don't you dare break her heart though, I know you have other 'business' with mares."
                mc "Yeah, I'm not ready to settle quite yet."
                show butters succlaughing with dissolve
                butters "Well, when you are ready, why settle for one personality when you can have two? Right?"
                mc "One personality and one nuisance that begs for sex."
                show butters succneutral with dissolve
                butters "But it's great sex, you can't deny that."
                mc "That I can't..."
            "Back":
                jump butterssuccmenu
        $ succbutterstalks = 1
        jump butterssuccmenu
if fr == 1:
    jump prefinalworldmap
jump preworldmap

label devilsex:
    stop music fadeout 3.0
    scene bg black with dissolve
    show bg buttersbedday
    with d
    "Shrugging, I scoop up the receptive bunny and walk into Butters' bedroom."
    "I place the white bunny down on the bed, where she skitters around curiously on the duvet."
    "She really is cute; I wonder what she’s like as a humanoid."
    play sound cork
    "I uncork the potion, pour some into a bowl and place it on the bed. Devil hops over and drinks up eagerly. It's almost as if she knows precisely what’s happening."
    "A couple of seconds later, the fluffy bunny undergoes a dramatic transformation before me."
    play music woosh
    show devil sil with s:
        xalign 0.5
        ypos 700
        linear 5.0 ypos 100
    stop music
    "With a small 'fuck you' to the law of equivalent exchange, she magically expands outward from a tiny bunny into an entirely anthropomorphic form."
    "Speechless, I merely observe as the bunny slowly comes to her senses."
    play music farm fadein 3.0
    show devil happy with d:
        linear 0.5 ypos 5
    "Pure white, and with distinct red eyes. She could be no taller than 5ft, making her the smallest anthro girl I’ve met apart from the Alraune."
    devil "Oh fun! I’ve been made humanoid again. Thank you, [playername]!"
    mc "Ohh, so you know my name!"
    show devil horny with d
    devil "Mhm, I’ve hear you and Butters talking lots! That’s why I can speak such good words."
    "No, those aren’t typos, she really can’t speak English well. But her attempt at speaking the language through osmosis is admirable."
    mc "This is pretty strange for me. What’s it like for you?"
    show devil happy with d
    devil "I’m not really sure, but I think I like being very smart. It gives me a very opportunity to express my love to those that care for me!"
    show devil horny with d
    devil "Ohh, sex is a good way to show, yes? I want to have sex with you."
    "The naughty bunny crawls over me more like a cougar than a docile rabbit, pressing one of her fluffy fingers on my chest as she playfully pushes me onto my back."
    devil "I’m always horny, but I never have any play partners, is it okay if I take that out on you?"
    mc "By all means, I’d say we’re both in for quite the unusual experience."
    show devil happy with d
    devil "Mm, that’s yes!"
    devil "I want to try a fun position, I’ve watched you and Butters do lots of fun position, can we do one?"
    mc "Sure, did you have something in mind based on what you’ve watched?"
    show devil horny with d
    devil "Uhhmm… Lying down and paws up, like tummy rubs but with sex!"
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
    devil "When can you go again? I think I’m totally ready for a second round!"
    play music challenge
    mc "Oh… Oh no…"
    scene bg black with dissolve
    if devilsex == 0:
        $ secretsunlocked += 1
    else:
        pass
    $ devilsex = 1
    "And with that, my entire day disappeared."
    "I felt like I was somewhat obligated to have sex with Devil. Especially considering that she technically doesn’t exist in that capacity for long."
    "But I managed to distract her with some other musings about the world as we went on a walk around Arcadia."
    "Eventually Devil returns to her usual form, vowing that one day she’d like to be ‘like you and Butters forever’."
    "Later in the evening..."
    play ambience ambiencenight fadein 3.0
    play music butters fadein 3.0
    show bg buttershousenight
    show butters dressneutral with d
    butters "I’ll do it one day. I’ll make a potion that turns her into an anthropomorph permanently."
    mc "Why doesn’t the current one work?"
    show butters dressangry with d
    butters "I’m not entirely sure… I’m still yet to fully understand the full intricacies of potion effect permanence."
    butters "It seems that the larger in magical magnitude the 'effect', the harder it is to be made permanent."
    butters "But one day, I’ll definitely make Devil’s dream come true."
    mc "You let me know when you do. She said she wants to have more sex to celebrate, and... I guess I kinda offered myself."
    show butters dresshappy with d
    butters "You can’t just spoil her and give her everything she asks for, silly!"
    mc "But she’s so darn cute…"
    show butters dressneutral with d
    butters "You know how Devil operates; she’ll always ask for more treats if you give her one. But you have to say no, otherwise she’ll get too greedy!"
    mc "I feel like that shouldn’t apply to her anthropomorphic form, but I see the logic."
    show butters dresshappy with d
    butters "Hehe, I will have a lot to teach that girl."
    jump eveningbuttersmenu
label succworksex:
    scene bg black with d
    "Sometime during work…"
    scene bg caveovergrown with d
    "Hmm... It's this cave again."
    "Not too bad without the Alraune though."
    "Unfortunately, my companion seems a little distracted."
    mc "Is everything okay?"
    show butters closesuccsad with d
    butters "Mmphh… As a succubus, it’s not easy working with a man."
    butters "I have needs too, you know?"
    mc "I told you that I’d have sex after work."
    show butters closesuccsurprised with d
    butters "Yeah, I know but…"
    butters "For a Succubus, that’s like telling a starving worker that you’ll feed them after they’ve slaved away for the next eight hours."
    "Hmm, she does seem a little more lethargic and submissive than usual."
    mc "Hm… Alright, do you want a blowjob as a quick fuel stop?"
    show butters closesuccneutral with d
    butters "I was thinking… Could you have sex with me?"
    mc "I suppose we have time. You do tend to be rather efficient after all."
    show butters closesucchappy with d
    butters "Ah, you noticed my effort. I put in that effort to make you happy, so you’ll have sex with me, you know?"
    mc "You really are one track minded. But I suppose you’re rather cute in that aspect."
    scene buttersb legsup
    show butters legsup1
    with d
    "The succubus lays down on the rocky ground and raises her legs, presenting both her plump pussy and bubble butt."
    butters "We can be quick, if you want."
    mc "It’s not every day you put yourself in a submissive position. So, I think I’ll take my time."
    butters "Mmphh…"
    "I’m sure she’d pout if she wasn’t so eagerly anticipating sex."
    "As shy and occasionally timid as both of Butters’ personalities can be, it is rare for her succubus side to not be on top."
    "To present herself submissively like this… She must be quite serious."
    "It’s pretty dark in here, but with her legs lifted up I have quite a clear view of her beautiful pussy."
    butters "Like what you see? Come on, don’t keep a girl waiting!"
    mc "Easy up, I’m not even erect yet."
    "I begin to fondle my cock into an erection... When I'm ready, I grab the succubus’s hips and pull her towards me."
    butters "Eep! Easy on the goods!"
    "I tap my cock on her bubble butt; enjoying the soft feeling as Butters keenly awaits my next move. However, I choose to tease her a little longer, playing with her pussy and engaging in extra foreplay."
    "As I expected, she’s extremely wet already. She might be ready, but the cold of the cave has somewhat diminished my own sexual appetite, so I’ll take my time building it back up."
    "She slowly grows impatient as I tease and massage her cute butt, her attempts at grinding against me do not go unnoticed."
    butters "Come on! Butters will get mad if we slack off!"
    "Oh yeah, I did tell her that, didn’t I? In reality, Butters probably doesn’t mind."
    play sound cum
    show butters legsup2 with d
    "I giggle and give her ass a playful slap as I position my cock at the lips of her hot pussy, and with one thrust I plunge my cock into the warmth and wetness."
    "Immediately my body is attacked with sharp succubus beguilement. I’m pretty used to this by now. I know I won’t be able to stop fucking her for a while, even if I wanted to."
    butters "Haaahh, finally! Now I want you to go wild, don’t hold back!"
    play music sex fadein 2.0
    "I roughly pound the Succubutters’ pussy. While I maintain a firm grip on her thighs, she keeps her legs raised for the duration making it feel even tighter."
    "The sound of our sexes slapping against each other mix and echo through the cave with her moans of delight. It truly is an erotic symphony to the ears."
    "We’re not exactly being subtle, and I’m sure any cave dwelling denizens within 100 meters can hear us loud and clear. However, I know that no one here would dare approach someone with the appearance of a succubus."
    butters "Mmphh, mmm… Keep going. I’m going to need at least one load of cum to last the rest of the nine to five."
    "Under her beguilement I find it hard to resist her orders, so I continue to pound her fluffy butt as aggressively as I can. My cock twitching and swelling as an orgasm builds within me, albeit very slowly."
    "I keep up for a minute, fucking her while occasionally slapping her ass and playing with her tits. I can feel her orgasm starting to come."
    butters "Mmpmhh… That’s it, I-I’m gonna come soon! Haahh, ahhh…"
    "She climaxes, her pussy clenches around my member as she squeals with pleasure. I can feel myself getting closer too as strange succubus energies sharpen my nerves."
    "I grit my teeth and continue to pulverize her pussy, driving my cock deeper and faster than before, causing Butters’ pillowy body to jiggle back and forth along the floor."
    butters "Haaaahhh, yesss, this is exactly what I needed! *Squish, squelch!*"
    "Still in an orgasmic daze, her quivering thighs struggle to remain upright."
    "I can feel my orgasm finally begin to boil up, and no doubt my companion has already been racked to the core by a second orgasm; judging by her hysteric movements and moans."
    play sound cum
    show butters legsup3 with cum
    play sound cum
    show butters legsup3 with cum
    "My orgasm finally arrives and overwhelms me with its glory. My vision briefly turns white as a torrent of thick jism spews into Butters's pussy and womb."
    play sound cum
    show butters legsup3 with cum
    play sound cum
    show butters legsup3 with cum
    stop music fadeout 3.0
    "Three loads, six, then nine. The pony’s pussy is filled to the brim, so much that it readily oozes and spills out."
    "She doesn’t absorb it because she no longer has the ability to drain, but she’s still tremendously satisfied."
    show butters legsup4 with d
    "The beguilement seems to steadily wear off, bringing me to my senses and enabling me to pull out. Lucky I did, otherwise I’d be stuck for another orgasm or two."
    stop music fadeout 3.0
    butters "Haahh, that was perfect, [playername]..."
    mc "Hey… you let me go after a single orgasm. You told me that the beguilement lasts at least thirty minutes after penetration!"
    butters "Ohh, I did? I must have lied. Hehehe."
    scene bg black with d
    if crystalballactivated == 1:
        jump cbmenu

    "…"
    play ambience ambiencenight fadeout 5.0
    scene bg buttershouse with dissolve
    "When we return, Butters and I spend a few hours creating batches of potions."
    scene bg buttershousenight with dissolve
    show butters dresshappy with dissolve
    "And due to the sexual intercourse I had with her succubus side, she gradually shifted back to normal."
    butters "Great job out there today."
    $ rand = renpy.random.randint(1,3)
    if rand == 3:
        butters "You really showed that slime that tried chasing us!"
        mc "She wouldn't leave us alone! I didn't think she'd cry from just an insult."
    elif rand == 2:
        butters "I can't believe we ran into a fairy, did you even know they native to this region?"
    else:
        butters "Even though we spent a while having sex after lunch, we got a pretty good yield."
        mc "It re-energised us, I'm telling ya."
    butters "Anyway, here's your pay! [forestmonies] monies."
    if forestmonies == 25:
        $ monies += 25
    elif forestmonies == 35:
        $ monies += 35
    elif forestmonies == 45:
        $ monies += 45
    elif forestmonies == 55:
        $ monies += 55
    else:
        pass
    jump eveningbuttersmenu
