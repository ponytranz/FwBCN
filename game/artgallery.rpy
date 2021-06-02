
label artgallery:
    stop ambience fadeout  3.0
    scene bg artgallery with dissolve
    if galleryypass == 1 or gallerydpass == 1:
        jump artgallerypostpass
    elif artgallery == 0 and dlc == 1:
        "It's just a regular art gallery. There are certainly a lot of beautiful works, but I have more important things to do right now."
        menu:
            "Leave":
                if worldmap == 2:
                    jump nightcity
                elif worldmap == 4:
                    jump nightcity
                jump city
    elif artgallery == 1 and dlc == 1 and gallerydpass == 0 and galleryypass == 0:
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        scene bg artgallery with dissolve
        "Alright, where's that room Augusta was talking about..."
        "Oh, hold on... I may have a key, but that doesn't give me free entry... Damnit Augusta."
        "Entry Fee - 15 monies for the day."
        "150 for a year pass."
        mc "Well, I guess it can't be helped."
        menu:
            "I should probably only pay if there's something worth seeing. (Best to complete some routes first!)"
            "Pay for the day (-15 monies)" if monies >= 15:
                $ monies -= 15
                $ gallerydpass = 1
                "The pass works all day, and in the evening too."
                pass
            "Pay for the year (-150 monies)" if monies >= 150:
                $ monies -= 150
                $ galleryypass = 1
                $ galleryyear = 0
                "This will expire after 365 days. I'm serious."
                pass
            "Nah!":
                if worldmap == 2:
                    jump nightcity
                elif worldmap == 4:
                    jump nightcity
                jump city
        "Alright, with that done... Where does this key fit?"
        "Let's try the door with a giant loveheart around it, that's exceedingly unsubtle."
        scene bg artgallery2 with dissolve
        "Okay perfect. Let's find a canvas and see what happens."
        pass
    elif gallerydpass == 0 or galleryypass == 0:
        "Entry Fee - 15 monies for the day."
        "150 for a year pass."
        mc "Well, I guess it can't be helped."
        menu:
            "I should probably only pay if there's something worth seeing. (Best to complete some routes first!)"
            "Pay for the day (-15 monies)":
                $ monies -= 15
                $ gallerydpass = 1
                "The pass works all day, and in the evening too."
                scene bg artgallery2 with dissolve
            "Pay for the year (-150 monies)":
                $ monies -= 150
                $ galleryypass = 1
                $ galleryyear = 0
                "This will expire after 365 days. I'm serious."
                scene bg artgallery2 with dissolve
            "Nah!":
                if worldmap == 2:
                    jump nightcity
                elif worldmap == 4:
                    jump nightcity
                jump city
    else:
        label artgallerypostpass:
            pass
        scene bg artgallery2 with dissolve
    "I'll only be able to view art from girls I've spent a lot of time with..."
    play music sex1 fadein 3.0
    menu g1:
        "Moxie" if moxieroses == 1 and moxiechocolates == 1 and fr == 1:
            menu moxieg:
                "Blowjob and 69":
                    show moxieb blowjob
                    show moxie blowjob1
                    with dissolve
                    ""
                    show moxie blowjob2 with dissolve
                    ""
                    show moxie blowjob3 with dissolve
                    ""
                    show moxie blowjob4 with dissolve
                    ""
                    show moxie blowjob5 with dissolve
                    ""
                    show moxieb sixtynine
                    show moxie sixtynine1
                    with dissolve
                    ""
                    show moxie sixtynine2 with dissolve
                    ""
                    show moxie sixtynine3 with dissolve
                    ""
                    show moxie sixtynine4 with dissolve
                    ""
                    show moxie sixtynine5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump moxieg
                "Missionary" if fr == 1:
                    show moxie bmissionary1 with dissolve
                    ""
                    show moxie bmissionary2 with dissolve
                    ""
                    show moxie bmissionary3 with dissolve
                    ""
                    show moxie bmissionary4 with dissolve
                    ""
                    show moxie bmissionary5 with dissolve
                    ""
                    show moxie bmissionary6 with dissolve
                    ""
                    show moxie bmissionary7 with dissolve
                    ""
                    show moxie bmissionary8 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump moxieg
                "Butt":
                    show moxie butt with dissolve
                    ""
                    show moxie buttclitrub with dissolve
                    ""
                    show moxie buttfinger with dissolve
                    ""
                    show moxie butttongue with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump moxieg
                "Cowgirl":
                    show moxie wcowgirl1 with dissolve
                    ""
                    show moxie wcowgirl2 with dissolve
                    ""
                    show moxie wcowgirl3 with dissolve
                    ""
                    show moxie wcowgirl4 with dissolve
                    ""
                    show moxie wcowgirl5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump moxieg
                "Doggystyle Vaginal":
                    show moxie doggystyle1 with dissolve
                    ""
                    show moxie doggystyle2 with dissolve
                    ""
                    show moxie doggystyle3 with dissolve
                    ""
                    show moxie doggystyle4 with dissolve
                    ""
                    show moxie doggystyle5 with dissolve
                    ""
                    show moxie doggystyle6 with dissolve
                    ""
                    show moxie doggystyle7 with dissolve
                    ""
                    show moxie doggystyle8 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump moxieg
                "Doggystyle Anal":
                    show moxie anal1 with dissolve
                    ""
                    show moxie anal2 with dissolve
                    ""
                    show moxie anal3 with dissolve
                    ""
                    show moxie anal4 with dissolve
                    ""
                    show moxie anal5 with dissolve
                    ""
                    show moxie anal6 with dissolve
                    ""
                    show moxie anal7 with dissolve
                    ""
                    show moxie anal8 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump moxieg
                "Back":
                    jump g1
        "Penelope" if sdps == 1:
            menu penelopeg:
                "Cunnilingus":
                    show penelope cunnilingus with dissolve
                    ""
                    show penelope mcunnilingus with d
                    ""
                    scene bg artgallery2 with dissolve
                    jump penelopeg
                "Masturbating":
                    show penelope rubbing with dissolve
                    ""
                    show penelope mrubbing with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump penelopeg
                "Facesitting":
                    show penelope facesitting with dissolve
                    ""
                    show penelope mfacesitting with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump penelopeg
                "Tribbing":
                    show penelope tribbing with dissolve
                    ""
                    show penelope mtribbing with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump penelopeg
                "Vaginal" if fr == 1:
                    show penelopeb sex
                    show penelope sex1
                    with dissolve
                    ""
                    show penelope sex2 with dissolve
                    ""
                    show penelope sex3 with dissolve
                    ""
                    show penelope sex4 with dissolve
                    ""
                    show penelope sex5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump penelopeg
                "Penelope x Moxie":
                    show penelopexmoxiegs with dissolve:
                        xalign 0.5
                        yalign 0
                    ""
                    show penelopexmoxiegs with dissolve:
                        xalign 0.5
                        yalign 0.8
                    ""
                    scene bg artgallery2 with dissolve
                    jump penelopeg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g1
        "Lily" if libraryvisit3 == 1 and fr == 1:
            menu lilyg:
                "Standing Sex":
                    show lily ssex1 with dissolve
                    ""
                    show lily ssex2  with dissolve
                    ""
                    show lily ssex3 with dissolve
                    ""
                    show lily ssex4 with dissolve
                    ""
                    show lily ssex5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump lilyg
                "Missionary":
                    show lily missionary1 with dissolve
                    ""
                    hide lily
                    show lilyb missionary
                    show lily missionary3
                    with dissolve
                    ""
                    show lily missionary4
                    with dissolve
                    ""
                    show lily missionary5 with dissolve
                    ""
                    show lily missionary6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump lilyg
                "From Behind":
                    show lilyb wsex
                    with dissolve
                    ""
                    show lily sex2 with dissolve
                    ""
                    show lily sex3 with dissolve
                    ""
                    show lily sex4 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump lilyg
                "Butt":
                    show lily butt with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump lilyg
                "Thigh Job":
                    show lilytj with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump lilyg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g1
        "Honeycrisp" if honeyrubythreesome == 1:
            menu honeycrispg:
                "Cowgirl":
                    show honeycrispb cowgirl1
                    show honeycrisp cowgirl2
                    with dissolve
                    ""
                    show honeycrisp cowgirl3 with dissolve
                    ""
                    show honeycrisp cowgirl4 with dissolve
                    ""
                    show honeycrisp cowgirl5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump honeycrispg
                "Anna threesome":
                    show honeycrispannab threesome
                    show honeycrispanna threesome1
                    with d
                    ""
                    show honeycrispanna threesome2
                    with d
                    ""
                    show honeycrispanna threesome3
                    with d
                    ""
                    show honeycrispanna threesome4
                    with d
                    ""
                    show honeycrispanna threesome5
                    with d
                    ""
                    show honeycrispanna threesome6
                    with d
                    ""
                    show honeycrispanna threesome7
                    with d
                    ""
                    show honeycrispanna threesome8
                    with d
                    ""
                    show honeycrispanna threesome9
                    with d
                    ""
                    scene bg artgallery2 with dissolve
                    jump honeycrispg
                "Blossom threesome" if fr == 1:
                    show honeyblossomb threesome
                    show honeyblossom threesome1
                    with dissolve
                    ""
                    show honeyblossom threesome2 with dissolve
                    ""
                    show honeyblossom threesome3 with dissolve
                    ""
                    show honeyblossom threesome4 with dissolve
                    ""
                    show honeyblossom threesome5 with dissolve
                    ""
                    show honeyblossom threesome6 with dissolve
                    ""
                    show honeyblossom threesome7 with dissolve
                    ""
                    show honeyblossom threesome8 with dissolve
                    ""
                    show honeyblossom threesome9 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump honeycrispg
                "Ruby threesome (Vaginal then Anal)":
                    show honeyrubyb spanking
                    show honeyruby spanking1
                    with dissolve
                    ""
                    show honeyruby spanking2 with dissolve
                    ""
                    show honeyruby spankingv1 with dissolve
                    ""
                    show honeyruby spankingv2 with dissolve
                    ""
                    show honeyruby spankingv3 with dissolve
                    ""
                    show honeyruby spankinga1 with dissolve
                    ""
                    show honeyruby spankinga2 with dissolve
                    ""
                    show honeyruby spankinga3 with dissolve
                    ""
                    show honeyruby spankingcum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump honeycrispg
                "Masturbation":
                    show honeycrisp ncmasturbating with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump honeycrispg
                "Ass":
                    show honeycrisp ass with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump honeycrispg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g1
        "Ruby" if honeyrubythreesome == 1:
            menu rubyg:
                "Camming Alone":
                    show ruby camming with dissolve
                    ""
                    show ruby camming2 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rubyg
                "Photoshoot":
                    show ruby photoshoot1 with dissolve
                    ""
                    show ruby photoshoot2 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rubyg
                "Cowgirl":
                    show ruby sexlipbite with dissolve
                    ""
                    show ruby sexoface with dissolve
                    ""
                    show ruby sexahegaocumdeep with dissolve
                    ""
                    show ruby sexofacemorecum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rubyg
                "Melody Threesome" if fr == 1:
                    show rubymelody threesome1 with dissolve
                    ""
                    show rubymelody threesome2 with dissolve
                    ""
                    show rubymelody threesome3 with dissolve
                    ""
                    show rubymelody threesome4 with dissolve
                    ""
                    show rubymelody threesome5 with dissolve
                    ""
                    show rubymelody threesome6 with dissolve
                    ""
                    show rubymelody threesome7 with dissolve
                    ""
                    show rubymelody threesome8 with dissolve
                    ""
                    show rubymelody threesome9 with dissolve
                    ""
                    show rubymelody threesome10 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rubyg
                "Honey Threesome (Vaginal then Anal)":
                    show honeyrubyb spanking
                    show honeyruby spanking1
                    with dissolve
                    ""
                    show honeyruby spanking2 with dissolve
                    ""
                    show honeyruby spankingv1 with dissolve
                    ""
                    show honeyruby spankingv2 with dissolve
                    ""
                    show honeyruby spankingv3 with dissolve
                    ""
                    show honeyruby spankinga1 with dissolve
                    ""
                    show honeyruby spankinga2 with dissolve
                    ""
                    show honeyruby spankinga3 with dissolve
                    ""
                    show honeyruby spankingcum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rubyg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g1
        "Cream" if bakeryvisit2 == 1:
            menu creamg:
                "Doggystyle (Quickie)":
                    show cream ass1 with dissolve
                    ""
                    show cream ass2 with dissolve
                    ""
                    show cream ass3 with dissolve
                    ""
                    show cream ass4 with dissolve
                    ""
                    show cream ass5 with dissolve
                    ""
                    show cream ass6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump creamg
                "Missionary":
                    show cream missionary1 with dissolve
                    ""
                    show cream missionary2 with dissolve
                    ""
                    show cream missionary3 with dissolve
                    ""
                    show cream missionary4 with dissolve
                    ""
                    show cream missionary5 with dissolve
                    ""
                    show cream missionary6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump creamg
                "Against the Counter" if fr == 1:
                    show cream ssex1 with dissolve
                    ""
                    show cream ssex2 with dissolve
                    ""
                    show cream ssex3 with dissolve
                    ""
                    show cream ssex4 with dissolve
                    ""
                    show cream ssex5 with dissolve
                    ""
                    show cream ssex6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump creamg
                "Foursome Blowjob":
                    show cream foursomebj1 with dissolve
                    ""
                    show cream foursomebj2 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump creamg
                "Foursome from Behind":
                    show cream foursome1 with dissolve
                    ""
                    show cream foursome2 with dissolve
                    ""
                    show cream foursome3 with dissolve
                    ""
                    show cream foursome4 with dissolve
                    ""
                    show cream foursome5 with dissolve
                    ""
                    show cream foursome6 with dissolve
                    ""
                    show cream foursome7 with dissolve
                    ""
                    show cream foursome8 with dissolve
                    ""
                    show cream foursome9 with dissolve
                    ""
                    show cream foursome10 with dissolve
                    ""
                    show cream foursome11 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump creamg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g1
        "Next Page ->":
            jump g2
        "Leave":
            if worldmap == 2:
                jump nightcity
            elif worldmap == 4:
                jump nightcity
            jump city
    menu g2:
        "Riku" if barvisit2 == 1:
            menu rikug:
                "Blowjob (Maid and Without)":
                    show rikub maidblowjob
                    show riku blowjob1
                    with dissolve
                    ""
                    show riku blowjob2 with dissolve
                    ""
                    show riku blowjob3 with dissolve
                    ""
                    show riku blowjob4 with dissolve
                    ""
                    show riku blowjob5 with dissolve
                    ""
                    show riku blowjob6 with dissolve
                    ""
                    show rikub blowjob
                    show riku blowjob1
                    with dissolve
                    ""
                    show riku blowjob2 with dissolve
                    ""
                    show riku blowjob3 with dissolve
                    ""
                    show riku blowjob4 with dissolve
                    ""
                    show riku blowjob5 with dissolve
                    ""
                    show riku blowjob6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rikug
                "Riding Anal" if fr == 1:
                    show rikub anal
                    show riku ranal1
                    with dissolve
                    ""
                    show riku ranal2 with dissolve
                    ""
                    show riku ranal3 with dissolve
                    ""
                    show riku ranal5 with dissolve
                    ""
                    show riku ranal6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rikug
                "Sofa Sex":
                    show rikub sofasex
                    show riku sofasex1
                    with dissolve
                    ""
                    show riku sofasex2 with dissolve
                    ""
                    show riku sofasex3 with dissolve
                    ""
                    show riku sofasex4 with dissolve
                    ""
                    show riku sofasex5 with dissolve
                    ""
                    show riku sofasex6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rikug
                "Moxie Threesome":
                    show rikub threesome
                    show riku threesome1
                    with dissolve
                    ""
                    show riku threesome2 with dissolve
                    ""
                    show riku threesome3 with dissolve
                    ""
                    show riku threesome4 with dissolve
                    ""
                    show riku threesome5 with dissolve
                    ""
                    show rikub maidthreesome
                    show riku threesome1
                    with dissolve
                    ""
                    show riku threesome2 with dissolve
                    ""
                    show riku threesome3 with dissolve
                    ""
                    show riku threesome4 with dissolve
                    ""
                    show riku threesome5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rikug
                "Butters Threesome":
                    show riku buttersthreesome1 with dissolve
                    ""
                    show riku buttersthreesome2 with dissolve
                    ""
                    show riku buttersthreesome3 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rikug
                "Butts (Three Different Butts)":
                    show riku assdere with dissolve
                    ""
                    show riku asstsun with dissolve
                    ""
                    show riku altass with dissolve
                    ""
                    show riku altass2 with dissolve
                    ""
                    show riku facesitting2 with dissolve
                    ""
                    show riku facesitting with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rikug
                "Feet":
                    show riku feet1 with dissolve
                    ""
                    show riku feet2 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump rikug
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g2
        "Butters" if buttersroses == 1 and butterschocolates == 1:
            menu buttersg:
                "Slime'd":
                    show butters slimesex1 with dissolve
                    ""
                    show butters slimesex2 with dissolve
                    ""
                    show butters slimesex3 with dissolve
                    ""
                    show butters slimesexangry with dissolve
                    ""
                    scene artgallery2 with dissolve
                    jump buttersg
                "Plant'd":
                    show butters tentacles1 with dissolve
                    ""
                    show butters tentacles2 with dissolve
                    ""
                    show butters tentacles3 with dissolve
                    ""
                    show butters tentacles4 with dissolve
                    ""
                    show butters tentacles5 with dissolve
                    ""
                    show butters tentacles6 with dissolve
                    ""
                    show butters tentacles7 with dissolve
                    ""
                    show butters tentacles8 with dissolve
                    ""
                    show butters tentacles9 with dissolve
                    ""
                    scene artgallery2 with dissolve
                    jump buttersg
                "Cowgirl (Normal/Succubus)":
                    show butters cowgirl1 with dissolve
                    ""
                    show butters cowgirl2 with dissolve
                    ""
                    show butters cowgirl3 with dissolve
                    ""
                    show butters cowgirl4 with dissolve
                    ""
                    show butters cowgirl5 with dissolve
                    ""
                    show butters succubussex1 with dissolve
                    ""
                    show butters succubussex2 with dissolve
                    ""
                    show butters succubussex3 with dissolve
                    ""
                    show butters succubussex4 with dissolve
                    ""
                    show butters succubussex5 with dissolve
                    ""
                    scene artgallery2 with dissolve
                    jump buttersg
                "Legup Doggy (Normal/Succubus)":
                    show butters legupdoggy1 with dissolve
                    ""
                    show butters legupdoggy2 with dissolve
                    ""
                    show butters legupdoggy3 with dissolve
                    ""
                    show butters legupdoggy4 with dissolve
                    ""
                    show butters legupdoggy5 with dissolve
                    ""
                    show butters legupdoggy6 with dissolve
                    ""
                    show butters succlegupdoggy1 with dissolve
                    ""
                    show butters succlegupdoggy2 with dissolve
                    ""
                    show butters succlegupdoggy3 with dissolve
                    ""
                    show butters succlegupdoggy4 with dissolve
                    ""
                    show butters succlegupdoggy5 with dissolve
                    ""
                    show butters succlegupdoggy6 with dissolve
                    ""
                    scene artgallery2 with dissolve
                    jump buttersg
                "Reverse Cowgirl (Normal/Succubus)":
                    show butters reversecowgirl1 with dissolve
                    ""
                    show butters reversecowgirl2 with dissolve
                    ""
                    show butters succreversecowgirl1 with dissolve
                    ""
                    show butters succreversecowgirl2 with dissolve
                    ""
                    scene artgallery2 with dissolve
                    jump buttersg
                "Missionary":
                    show butters missionary1 with dissolve
                    ""
                    show butters missionary2 with dissolve
                    ""
                    show butters missionary3 with dissolve
                    ""
                    show butters missionary4 with dissolve
                    ""
                    show butters missionary5 with dissolve
                    ""
                    show butters missionary6b with dissolve
                    ""
                    show butters missionary6a with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump buttersg
                "Milky Paizuri":
                    show butters paizuri1 with dissolve
                    ""
                    show butters paizuri2 with dissolve
                    ""
                    show butters paizuri3 with dissolve
                    ""
                    show butters paizuri4 with dissolve
                    ""
                    show butters paizuri5 with dissolve
                    ""
                    show butters paizuri6 with dissolve
                    ""
                    show butters paizuri7 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump buttersg
                "Poyo":
                    show buttersslimeblow with dissolve:
                        xalign 0.5
                    ""
                    show buttersslimeblow2 with dissolve:
                        xalign 0.5
                    ""
                    scene bg artgallery2 with dissolve
                    jump buttersg
                "Misc (Ass and Masturbating)":
                    show butters ass with dissolve
                    ""
                    show butters masturbating with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump buttersg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g2
        "Blossom" if farmvisit3 == 1:
            menu blossomg:
                "Blossom Cowgirl":
                    show blossomb1 sex
                    show blossom sex1
                    with dissolve
                    ""
                    show blossom sex2 with dissolve
                    ""
                    show blossom sex3 with dissolve
                    ""
                    show blossom sex4 with dissolve
                    ""
                    show blossom sex5 with dissolve
                    ""
                    show blossom sex6 with dissolve
                    ""
                    show blossom sex7 with dissolve
                    ""
                    show blossom sex8 with dissolve
                    ""
                    show blossom sex9 with dissolve
                    ""
                    hide blossom
                    hide blossomb1 sex
                    show blossomb2 sex
                    show blossom sex1
                    with dissolve
                    ""
                    show blossom sex2 with dissolve
                    ""
                    show blossom sex3 with dissolve
                    ""
                    show blossom sex4 with dissolve
                    ""
                    show blossom sex5 with dissolve
                    ""
                    scene artgallery2 with dissolve
                    jump blossomg
                "Blossom Thighs":
                    show blossom lewd with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump blossomg
                "Blossom Masturbating":
                    show blossom masturbating with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump blossomg
                "Honeycrisp threesome" if fr == 1:
                    show honeyblossomb threesome
                    show honeyblossom threesome1
                    with dissolve
                    ""
                    show honeyblossom threesome2 with dissolve
                    ""
                    show honeyblossom threesome3 with dissolve
                    ""
                    show honeyblossom threesome4 with dissolve
                    ""
                    show honeyblossom threesome5 with dissolve
                    ""
                    show honeyblossom threesome6 with dissolve
                    ""
                    show honeyblossom threesome7 with dissolve
                    ""
                    show honeyblossom threesome8 with dissolve
                    ""
                    show honeyblossom threesome9 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump blossomg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g2
        "Melody" if melodylaptop == 1:
            play music melodytheme
            menu melodyg:
                "Handjob":
                    show melodyb handjob
                    show melody handjob1
                    with dissolve
                    ""
                    show melody handjob2 with dissolve
                    ""
                    show melody handjob3 with dissolve
                    ""
                    show melody handjob4 with dissolve
                    ""
                    show melody handjob5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump melodyg
                "Blowjob":
                    show melodyb blowjob
                    show melody blowjob1 with dissolve
                    ""
                    show melody blowjob2 with dissolve
                    ""
                    show melody blowjob3 with dissolve
                    ""
                    show melody blowjob4 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump melodyg
                "Cowgirl":
                    show melodyb sex
                    show melody sex1
                    with dissolve
                    ""
                    show melody sex2 with dissolve
                    ""
                    show melody sex3 with dissolve
                    ""
                    show melody sex4 with dissolve
                    ""
                    show melody sex5 with dissolve
                    ""
                    show melody sex6 with dissolve
                    ""
                    show melody sex7 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump melodyg
                "Music Studio":
                    show melodyb studiosex
                    show melody studiosex1
                    with dissolve
                    ""
                    show melody studiosex2 with dissolve
                    ""
                    show melody studiosex3 with dissolve
                    ""
                    show melody studiosex4 with dissolve
                    ""
                    show melody studiosex5 with dissolve
                    ""
                    show melody studiosex6 with dissolve
                    ""
                    show melody studiosex7 with dissolve
                    ""
                    scene artgallery2 with dissolve
                    jump melodyg
                "Ruby Threesome" if fr == 1:
                    show rubymelody threesome1 with dissolve
                    ""
                    show rubymelody threesome2 with dissolve
                    ""
                    show rubymelody threesome3 with dissolve
                    ""
                    show rubymelody threesome4 with dissolve
                    ""
                    show rubymelody threesome5 with dissolve
                    ""
                    show rubymelody threesome6 with dissolve
                    ""
                    show rubymelody threesome7 with dissolve
                    ""
                    show rubymelody threesome8 with dissolve
                    ""
                    show rubymelody threesome9 with dissolve
                    ""
                    show rubymelody threesome10 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump melodyg
                "Butt":
                    show melody butt with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump melodyg
                "Back":
                    scene bg artgallery2 with dissolve
                    play music sex1 fadeout 2.0
                    jump g2
        "Anna" if farmvisit3 == 1:
            menu annag:
                "Blowjob":
                    show anna blowjob with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump annag
                "Milking":
                    show anna milking1 with dissolve
                    ""
                    show anna milking2 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump annag
                "Paizuri":
                    show anna paizuri with dissolve
                    ""
                    show anna paizuricum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump annag
                "Pussy":
                    show annapussycloseup with dissolve:
                        xalign 0.5
                    ""
                    scene bg artgallery2 with dissolve
                    jump annag
                "Handjob":
                    show annahandjob with dissolve:
                        xalign 0.5
                    ""
                    scene bg artgallery2 with dissolve
                    jump annag
                "Honey Threesome":
                    show honeycrispannab threesome
                    show honeycrispanna threesome1
                    with d
                    ""
                    show honeycrispanna threesome2
                    with d
                    ""
                    show honeycrispanna threesome3
                    with d
                    ""
                    show honeycrispanna threesome4
                    with d
                    ""
                    show honeycrispanna threesome5
                    with d
                    ""
                    show honeycrispanna threesome6
                    with d
                    ""
                    show honeycrispanna threesome7
                    with d
                    ""
                    show honeycrispanna threesome8
                    with d
                    ""
                    show honeycrispanna threesome9
                    with d
                    ""
                    scene bg artgallery2 with dissolve
                    jump annag
                "Doggystyle":
                    show anna doggystyle1 with d
                    ""
                    show anna doggystyle2 with d
                    ""
                    scene bg artgallery2 with d
                    jump annag
                "Random Cow Girls Threesome":
                    show cow threesome with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump annag
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g2
        "Next Page ->":
            jump g3
        "<- Previous Page":
            jump g1
        "Leave":
            if worldmap == 2:
                jump nightcity
            elif worldmap == 4:
                jump nightcity
            jump city
    menu g3:
        "Ari, Sonia and Agatha" if arisex == 1:
            menu dazzlingsg:
                "Sonia and Agatha":
                    show agathasoniab sex
                    show agathasonia sex1
                    with dissolve
                    ""
                    show agathasonia sex2 with dissolve
                    ""
                    show agathasonia sex3 with dissolve
                    ""
                    show agathasonia sex4 with dissolve
                    ""
                    show agathasonia sex5 with dissolve
                    ""
                    show agathasonia sex6 with dissolve
                    ""
                    show agathasonia sex7 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump dazzlingsg
                "Ari":
                    show arib sex
                    show ari sex1
                    with dissolve
                    ""
                    show ari sex2 with dissolve
                    ""
                    show ari sex3 with dissolve
                    ""
                    show ari sex4 with dissolve
                    ""
                    show ari sex5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump dazzlingsg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g3
        "Bar + Nightclub Girls" if doggirl1 == 1 and wolfgirl1 == 1 and midnasexd == 1 and sofiasex == 1:
            menu barg:
                "Rosa (Vaginal then Anal)":
                    show rosa sex1 with dissolve
                    ""
                    show rosa sexv1 with dissolve
                    ""
                    show rosa sexv2 with dissolve
                    ""
                    show rosa sexv3 with dissolve
                    ""
                    show rosa sexa1 with dissolve
                    ""
                    show rosa sexa2 with dissolve
                    ""
                    show rosa sexa3 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump barg
                "Hilda Character Model":
                    show hilda char with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump barg
                "Hilda (Vaginal then Anal)":
                    show hilda sex1 with dissolve
                    ""
                    show hilda sex2 with dissolve
                    ""
                    show hilda sex3 with dissolve
                    ""
                    show hilda sexv1 with dissolve
                    ""
                    show hilda sexv2 with dissolve
                    ""
                    show hilda sexa1 with dissolve
                    ""
                    show hilda sexa2 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump barg
                "Midna":
                    show midna pet1 with dissolve
                    ""
                    show midna pet2 with dissolve
                    ""
                    show midna pet3 with dissolve
                    ""
                    show midna pet4 with dissolve
                    ""
                    show midna pet5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump barg
                "Sofia (Panties then Stockings)":
                    show sofia panties1 with dissolve
                    ""
                    show sofia panties2 with dissolve
                    ""
                    show sofia panties3 with dissolve
                    ""
                    show sofia panties4 with dissolve
                    ""
                    show sofia panties5 with dissolve
                    ""
                    show sofia stockings1 with dissolve
                    ""
                    show sofia stockings2 with dissolve
                    ""
                    show sofia stockings3 with dissolve
                    ""
                    show sofia stockings4 with dissolve
                    ""
                    show sofia stockings5 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump barg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g3
        "Spa Girls" if spatodo > 2 and musicstudio == 1:
            menu spag:
                "Back Massage":
                    show spa1 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump spag
                "Tribbing":
                    show spa11 with dissolve
                    ""
                    show spa11cum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump spag
                "Blowjob":
                    show spa blowjob1 with dissolve
                    ""
                    show spa blowjob2 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump spag
                "Threesome":
                    show spa threesome1 with dissolve
                    ""
                    show spa threesome2 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump spag
                "Tavi Reverse Cowgirl":
                    show tavi ride1 with dissolve
                    ""
                    show tavi ride2 with dissolve
                    ""
                    show tavi ride3 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump spag
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g3
        "Dawn" if dawnvisit > 4:
            menu dawng:
                "Blowjob":
                    show dawnb blowjob
                    show dawn blowjob1
                    with dissolve
                    ""
                    show dawn blowjob2 with dissolve
                    ""
                    show dawn blowjob3 with dissolve
                    ""
                    show dawn blowjob4 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump dawng
                "Reverse Cowgirl":
                    show dawnb sex
                    show dawn sex1
                    with dissolve
                    ""
                    show dawn sex2 with dissolve
                    ""
                    show dawn sex3 with dissolve
                    ""
                    show dawn sex4 with dissolve
                    ""
                    show dawn sex5 with dissolve
                    ""
                    show dawn sex6 with dissolve
                    ""
                    show dawn sex7 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump dawng
                "Doggystyle":
                    show dawnb doggystyle
                    show dawn doggystyle1
                    with dissolve
                    ""
                    show dawn doggystyle2 with dissolve
                    ""
                    show dawn doggystyle3 with dissolve
                    ""
                    show dawn doggystyle4 with dissolve
                    ""
                    show dawn doggystyle5 with dissolve
                    ""
                    show dawn doggystyle6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump dawng
                "The Entire Dawn Lily Mega-Fuck":
                    show dawnlily sauna1 with dissolve:
                        xalign 0.5
                        yalign 0.0
                    ""
                    show dawnlily sauna2 with dissolve:
                        xalign 0.5
                        yalign 1.0
                    ""
                    show dawnlily facesitting1 with dissolve:
                        xalign 0.5
                        yalign 0.0
                    ""
                    show dawnlily facesitting2 with dissolve:
                        xalign 0.5
                        yalign 1.0
                    ""
                    scene dawnlilyb vaginal
                    show dawnlily vaginal1
                    with dissolve
                    ""
                    show dawnlily vaginal2 with dissolve
                    ""
                    show dawnlily vaginal3 with dissolve
                    ""
                    show dawnlily vaginal4 with dissolve
                    ""
                    show dawnlily vaginal5 with dissolve
                    ""
                    show dawnlily vaginal6 with dissolve
                    ""
                    show dawnlily vaginal7 with dissolve
                    ""
                    scene dawnlilyb anal
                    show dawnlily anal1
                    with dissolve
                    ""
                    show dawnlily anal2 with dissolve
                    ""
                    show dawnlily anal3 with dissolve
                    ""
                    show dawnlily anal4 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump dawng
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g3
        "Cindy" if cindylum == 1:
            menu cindyg:
                "Cindy Reverse Cowgirl":
                    show cindy rcg1 with d
                    ""
                    show cindy rcg2 with d
                    ""
                    show cindy rcg3 with d
                    ""
                    show cindy rcg4 with d
                    ""
                    scene bg artgallery2 with dissolve
                    jump cindyg
                "Cindy Legs-Up Missionary (Vaginal then Anal)":
                    show cindy legsup1 with d
                    ""
                    show cindy legsupv1 with d
                    ""
                    show cindy legsupv2 with d
                    ""
                    show cindy legsupv3 with d
                    ""
                    show cindy legsupa1 with d
                    ""
                    show cindy legsupa2 with d
                    ""
                    show cindy legsupa3 with d
                    ""
                    show cindy legsupcum with d
                    scene bg artgallery2 with dissolve
                    jump cindyg
                "Back":
                    jump g3
        "Next Page ->":
            jump g4
        "<- Previous Page":
            jump g2
        "Leave":
            if worldmap == 2:
                jump nightcity
            elif worldmap == 4:
                jump nightcity
            jump city
    menu g4:
        "Zoe" if zoe == 2:
            menu zoeg:
                "Doggystyle (Vaginal and unused Anal variant)":
                    show zoeb doggystyle
                    show zoe doggystyle1
                    with d
                    ""
                    show zoe doggystyle2 with d
                    ""
                    show zoe doggystylev1 with d
                    ""
                    show zoe doggystylev2 with d
                    ""
                    show zoe doggystylev3 with d
                    ""
                    show zoe doggystylea1 with d
                    ""
                    show zoe doggystylea2 with d
                    ""
                    show zoe doggystylea3 with d
                    ""
                    show zoe doggystylecum with d
                    ""
                    scene bg artgallery2 with d
                    jump zoeg
                "Leg-Up Sideways":
                    show zoeb lum
                    show zoe lum1 with d
                    ""
                    show zoe lum2 with d
                    ""
                    show zoe lum3 with d
                    ""
                    show zoe lum4 with d
                    ""
                    show zoe lum5 with d
                    ""
                    show zoe lum6 with d
                    ""
                    show zoe lum7 with d
                    ""
                    scene bg artgallery2 with d
                    jump zoeg
                "Alraune Standing(?) Sex":
                    show alrauneb sex
                    show alraune sex1
                    with d
                    ""
                    show alraune sex2 with d
                    ""
                    show alraune sex3 with d
                    ""
                    show alraune sex4 with d
                    ""
                    show alraune sex5 with d
                    ""
                    show alraune sex6 with d
                    ""
                    scene bg artgallery2 with d
                    jump zoeg
                "Back":
                    jump g4
        "Augusta":
            menu augustag:
                "Hole - Augusta":
                    show holeb augusta with dissolve
                    ""
                    show hole vaginal1 with dissolve
                    ""
                    show hole vaginal2 with dissolve
                    ""
                    show hole cum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump augustag
                "Hole - Suspicously Recognizable Orange Pony":
                    show holeb scoots with dissolve
                    ""
                    show hole augusta1 with dissolve
                    ""
                    show hole augusta2 with dissolve
                    ""
                    show hole augusta3 with dissolve
                    ""
                    show hole train1 with dissolve
                    ""
                    show hole train2 with dissolve
                    ""
                    show hole dp1 with dissolve
                    ""
                    show hole dp2 with dissolve
                    ""
                    show hole vaginal1 with dissolve
                    ""
                    show hole vaginal2 with dissolve
                    ""
                    show hole cum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump augustag
                "Hole - Yellow Pony":
                    show holeb yellow  with dissolve
                    ""
                    show hole augusta1 with dissolve
                    ""
                    show hole augusta2 with dissolve
                    ""
                    show hole augusta3 with dissolve
                    ""
                    show hole train1 with dissolve
                    ""
                    show hole train2 with dissolve
                    ""
                    show hole dp1 with dissolve
                    ""
                    show hole dp2 with dissolve
                    ""
                    show hole vaginal1 with dissolve
                    ""
                    show hole vaginal2 with dissolve
                    ""
                    show hole cum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump augustag
                "Hole - Black/White Pony":
                    show holeb grey with dissolve
                    ""
                    show hole augusta1 with dissolve
                    ""
                    show hole augusta2 with dissolve
                    ""
                    show hole augusta3 with dissolve
                    ""
                    show hole train1 with dissolve
                    ""
                    show hole train2 with dissolve
                    ""
                    show hole dp1 with dissolve
                    ""
                    show hole dp2 with dissolve
                    ""
                    show hole vaginal1 with dissolve
                    ""
                    show hole vaginal2 with dissolve
                    ""
                    show hole cum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump augustag
                "Hole - Red Pony":
                    show holeb red with dissolve
                    ""
                    show hole augusta1 with dissolve
                    ""
                    show hole augusta2 with dissolve
                    ""
                    show hole augusta3 with dissolve
                    ""
                    show hole train1 with dissolve
                    ""
                    show hole train2 with dissolve
                    ""
                    show hole dp1 with dissolve
                    ""
                    show hole dp2 with dissolve
                    ""
                    show hole vaginal1 with dissolve
                    ""
                    show hole vaginal2 with dissolve
                    ""
                    show hole cum with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump augustag
                "Reverse Cowgirl":
                    show augusta cowgirl1 with dissolve
                    ""
                    show augusta cowgirl2 with dissolve
                    ""
                    show augusta cowgirl3 with dissolve
                    ""
                    show augusta cowgirl4 with dissolve
                    ""
                    show augusta cowgirl5 with dissolve
                    ""
                    show augusta cowgirl6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump augustag
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g4
        "Selene" if selenevisit1 == 1:
            menu seleneg:
                "Blowjob":
                    show seleneb blowjob
                    show selene blowjob1
                    with dissolve
                    ""
                    show selene blowjob2 with dissolve
                    ""
                    show selene blowjob3 with dissolve
                    ""
                    show selene blowjob4 with dissolve
                    ""
                    show selene blowjob5 with dissolve
                    ""
                    show selene blowjob6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump seleneg
                "Cowgirl":
                    show seleneb cowgirl
                    show selene cowgirl1
                    with dissolve
                    ""
                    show selene cowgirl2 with dissolve
                    ""
                    show selene cowgirl3 with dissolve
                    ""
                    show selene cowgirl4 with dissolve
                    ""
                    show selene cowgirl5 with dissolve
                    ""
                    show selene cowgirl6 with dissolve
                    ""
                    show selene cowgirl7 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump seleneg
                "Aurora Threesome" if fr == 1:
                    show auroraseleneb threesome
                    show auroraselene threesome1
                    with dissolve
                    ""
                    show auroraselene threesome2 with dissolve
                    ""
                    show auroraselene threesome3 with dissolve
                    ""
                    show auroraselene threesome4 with dissolve
                    ""
                    show auroraselene threesome5 with dissolve
                    ""
                    show auroraselene threesome6 with dissolve
                    ""
                    show auroraselene threesome7 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump seleneg
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g4
        "Aurora" if auroravisit1 == 1:
            menu aurorag:
                "Missionary":
                    show aurorab missionary
                    show aurora missionary1
                    with d
                    ""
                    show aurora missionary2 with d
                    ""
                    show aurora missionary3 with d
                    ""
                    show aurora missionary4 with d
                    ""
                    show aurora missionary5 with d
                    ""
                    show aurora missionary6 with d
                    ""
                    show aurora missionary7 with d
                    ""
                    show aurora missionary8 with d
                    ""
                    show aurora missionary9 with d
                    ""
                    show aurora missionary10 with d
                    ""
                    scene bg artgallery2 with dissolve
                    jump aurorag
                "Principal Aurora" if dawnvisit > 2:
                    show principalaurorab sex
                    show principalaurora sex1
                    with dissolve
                    ""
                    show principalaurora sex2 with dissolve
                    ""
                    show principalaurora sex3 with dissolve
                    ""
                    show principalaurora sex4 with dissolve
                    ""
                    show principalaurora sex5 with dissolve
                    ""
                    show principalaurora sex6 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump aurorag
                "Selene Threesome" if fr == 1:
                    show auroraseleneb threesome
                    show auroraselene threesome1
                    with dissolve
                    ""
                    show auroraselene threesome2 with dissolve
                    ""
                    show auroraselene threesome3 with dissolve
                    ""
                    show auroraselene threesome4 with dissolve
                    ""
                    show auroraselene threesome5 with dissolve
                    ""
                    show auroraselene threesome6 with dissolve
                    ""
                    show auroraselene threesome7 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump aurorag
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g4
        "Morrigan" if fr == 1:
            menu morrigang:
                "Game Over Scenes":
                    show morrigan groupcun1 with dissolve
                    ""
                    show morrigan groupcun2 with s
                    ""
                    show morrigan harem1 with dissolve
                    ""
                    show morrigan harem2 with s
                    ""
                    scene bg artgallery2 with dissolve
                    jump morrigang
                "Missionary":
                    show morrigan sex1 with dissolve
                    ""
                    show morrigan sex2 with dissolve
                    ""
                    show morrigan sex3 with dissolve
                    ""
                    show morrigan sex4 with dissolve
                    ""
                    show morrigan sex5 with dissolve
                    ""
                    show morrigan sex6 with dissolve
                    ""
                    show morrigan sex7 with dissolve
                    ""
                    show morrigan sex8 with dissolve
                    ""
                    scene bg artgallery2 with dissolve
                    jump morrigang
                "Back":
                    scene bg artgallery2 with dissolve
                    jump g4
        "Last Page ->":
            jump g5
        "<- Previous Page":
            jump g3
        "Leave":
            if worldmap == 2:
                jump nightcity
            elif worldmap == 4:
                jump nightcity
            jump city
    menu g5:
        "Secret Scenes":
            jump sg1
        "<- Previous Page":
            jump g3
        "Leave":
            if worldmap == 2:
                jump nightcity
            elif worldmap == 4:
                jump nightcity
            jump city
    menu sg1:
        "Werewolf" if werewolfsex == 1:
            show werewolf with dissolve
            ""
            scene werewolfb sex
            show werewolf sex1
            with d
            ""
            show werewolf sex2 with d
            ""
            show werewolf sex3 with d
            ""
            show werewolf sex4 with d
            ""
            scene bg artgallery2 with dissolve
            jump sg1
        "Devil Sex" if devilsex == 1:
            show devilb sex
            show devil sex1
            with d
            ""
            show devil sex2 with d
            ""
            show devil sex3 with d
            ""
            show devil sex4 with d
            ""
            scene bg artgallery2 with dissolve
            jump sg1
        "Sandy Threesome" if sandysex == 1:
            show sandyb sex
            show sandy sex1
            with d
            ""
            show sandy sex2 with d
            ""
            show sandy sex3 with d
            ""
            show sandy sex4 with d
            ""
            show sandy sex5 with d
            ""
            scene bg artgallery2 with dissolve
            jump sg1

        "Double Doggos" if doubledog == 1:
            show doubleb doggo
            show double doggo1
            with d
            ""
            show double doggo2 with d
            ""
            show double doggo3 with d
            ""
            show double doggo4 with d
            ""
            show double doggo5 with d
            ""
            show double doggo6 with d
            ""
            show double doggo7 with d
            ""
            show double doggo8 with d
            ""
            show double doggo9 with d
            ""

            scene bg artgallery2 with dissolve
            jump sg1
        "Honeycrisp Outside" if honeycrispoutsidesex == 1:
            show honeycrispb outside
            show honeycrisp outside1
            with d
            ""
            show honeycrisp outside2 with d
            ""
            show honeycrisp outside3 with d
            ""
            show honeycrisp outside4 with d
            ""

            scene bg artgallery2 with dissolve
            jump sg1

        "Cream Lingerie" if creamlingeriesex == 1:
            show creamb lingerie
            show cream lingerie1
            with d
            ""
            show cream lingerie2
            with d
            ""
            show cream lingerie3
            with d
            ""
            show cream lingerie4
            with d
            ""

            scene bg artgallery2 with dissolve
            jump sg1

        "Next Page ->":
            jump sg2
        "Back":
            jump g5
    menu sg2:
        "Ruby Lingerie Doggystyle" if rubylingeriesex == 1:
            show rubyb doggystyle
            show ruby doggystyle1
            with d
            ""
            show ruby doggystyle2
            with d
            ""
            show ruby doggystyle3
            with d
            ""
            show ruby doggystyle4
            with d
            ""


            scene bg artgallery2 with dissolve
            jump sg2

        "Riku Climbing Sex" if rikuclimbingsex == 1:
            show rikub climbing1
            show riku climbing1
            with d
            ""
            show rikub climbing2 with d
            ""
            show riku climbing2
            with d
            ""
            show riku climbing3
            with d
            ""
            show riku climbing4
            with d
            ""
            show riku climbing5
            with d
            ""
            show riku climbing6
            with d
            ""
            show riku climbing7
            with d
            ""

            scene bg artgallery2 with dissolve
            jump sg2
        "Lily Splits Sex" if lilysplitsex == 1:
            show lilyb splits
            show lily splits1
            with d
            ""
            show lily splits2
            with d
            ""
            show lily splits3
            with d
            ""
            show lily splits4
            with d
            ""
            scene bg artgallery2 with dissolve
            jump sg2
        "Dawn Shower Sex" if dawnshowersex == 1:
            show dawnb shower
            show dawn shower1
            with d
            ""
            show dawn shower2
            with d
            ""
            show dawn shower3
            with d
            ""
            show dawn shower5
            with d
            ""
            show dawn shower4
            with d
            ""
            scene bg artgallery2 with dissolve
            jump sg2
        "Melody Cunnilingus" if melodycunnilingus == 1:
            show melodyb cunnilingus
            show melody cunnilingus1
            with d
            ""
            show melody cunnilingus2
            with d
            ""
            show melody cunnilingus3
            with d
            ""
            show melody cunnilingus4
            with d
            ""
            show melody cunnilingus5
            with d
            ""
            scene bg artgallery2 with dissolve
            jump sg2
        "Succubutters Work Sex" if succworksex == 1:
            show buttersb legsup
            show butters legsup1
            with d
            ""
            show butters legsup2
            with d
            ""
            show butters legsup3
            with d
            ""
            show butters legsup4
            with d
            ""
            scene bg artgallery2 with dissolve
            jump sg2

        "<- Previous Page":
            jump sg1
        "Back":
            jump g5
