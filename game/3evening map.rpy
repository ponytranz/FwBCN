screen worldmapnight():
    imagemap:
        ground "bg worldmapnightui.png"
        hover "bg worldmapnightuihover.png"

        #hotspot (0, 300, 290, 210) clicked Jump("maplibrary")
        hotspot (895, 305, 140, 140) clicked Jump ("mapnightwagon")
        #hotspot (380, 210, 107, 90) clicked Jump ("mapfarm")
        #hotspot (480, 260, 75, 50) clicked Jump ("mapbakery")
        hotspot (575, 360, 75, 75) clicked Jump ("mapnightbar")
        #hotspot (556, 310, 75, 50) clicked Jump ("mapspa")
        #hotspot (490, 310, 60, 60) clicked Jump ("mapmarket")
        hotspot (200, 225, 90, 90) clicked Jump ("mapnightforest")
        hotspot (1130, 270, 150, 175) clicked Jump ("mapnightboutique")
        hotspot (830, 180, 175, 140) clicked Jump ("mapnightcastle")
        hotspot (18, 180, 120, 200) clicked Jump ("deepforest")


        hotspot (920, 0, 108, 125)  action Show("todolist", dissolve)
        hotspot (1025, 0, 138, 125) clicked Jump ("inventorymenuday")
        hotspot (1165, 0, 108, 125)  action ShowMenu("preferences")

    ## Ensure this appears on top of other screens.
    text "{b}[monies]{/b}":
        xalign 0.22
        yalign 0.0225
    text "{b}Day [days]{/b}":
        xalign 0.065
        yalign 0.0225



## This code ensures that the quick_menu screen is displayed in-game,
label preworldmapnight:
    scene bg worldmapnight with dissolve
    play ambience ambiencenight
label worldmapnight:
    $ worldmap = 2
    scene bg worldmapnightui
    if wmnu1 == 0:
        $ wmnu1 = 1
        "Maybe I should check out the bar or nightclub?"
    call screen worldmapnight
    label mapnightwagon:
        jump eveningmoxie1
    label mapnightforest:
        if fr == 1:
            show bg pgworldmapnightnoui with dissolve
        else:
            show bg worldmapnightdialogue with dissolve
        if forestvisits > 2:
            jump eveningbutters1
        else:
            "Visiting Butters in the evening is just a little too far of a walk, especially since I'm not yet familiar with the layout of the dark forest."
            jump worldmapnight
    label mapnightboutique:
        if fr == 1:
            show bg pgworldmapnightnoui with dissolve
        else:
            show bg worldmapnightdialogue with dissolve
        menu:
            "Ruby's boutique"
            "Visit the boutique":
                if boutiquevisit3 == 1:
                    jump melodyevening
                else:
                    "I knock on the boutique door and there's no response. This building is massive, so the girls probably can't hear my knocking from their bedrooms at all."
            "Go back":
                if fr == 1:
                    jump finalworldmapnight
                else:
                    jump worldmapnight
        jump worldmapnight
    label mapnightbar:
        if fr == 1:
            show bg pgworldmapnightnoui with dissolve
        else:
            show bg worldmapnightdialogue with dissolve
        menu:
            "The Riding Mare bar"
            "Visit the bar":
                jump barvisitevening
            "Go back":
                if fr == 1:
                    jump finalworldmapnight
                else:
                    jump worldmapnight
    label mapnightcastle:
        jump nightcity
