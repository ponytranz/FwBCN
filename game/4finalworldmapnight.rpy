screen fworldmapnight():
    imagemap:
        ground "bg pgworldmapnightui.png"
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
        hotspot (830, 180, 175, 140) clicked Jump ("nightcity")
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


label prefinalworldmapnight:
    stop music fadeout 3.0
    play ambience ambiencenight
    scene bg pgworldmapnight with dissolve
label finalworldmapnight:
    $ worldmap = 4
    stop music fadeout 3.0
    scene bg pgworldmapnightui
    call screen fworldmapnight
    with qd
