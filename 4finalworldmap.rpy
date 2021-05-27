screen finalworldmap():
    imagemap:
        ground "bg pgworldmapday"
        hover "bg worldmaphover"

        hotspot (0, 300, 290, 210) clicked Jump("maplibrary")
        hotspot (895, 305, 140, 140) clicked Jump ("mapwagon")
        hotspot (380, 210, 107, 90) clicked Jump ("mapfarm")
        hotspot (480, 250, 90, 90) clicked Jump ("mapbakery")
        hotspot (575, 360, 75, 75) clicked Jump ("mapbar")
        hotspot (556, 280, 85, 80) clicked Jump ("mapspa")
        hotspot (470, 320, 80, 65) clicked Jump ("mapmarket")
        hotspot (200, 225, 90, 90) clicked Jump ("mapforest")
        hotspot (1130, 270, 150, 175) clicked Jump ("mapboutique")
        hotspot (830, 180, 175, 140) clicked Jump ("mapcity")

        hotspot (920, 0, 108, 125)  action (Show("todolist", dissolve), Hide("finalworldmap", dissolve))
        hotspot (1025, 0, 138, 125)  clicked Jump ("inventorymenuday")
        hotspot (1165, 0, 108, 125)  action ShowMenu("preferences")
    text "{b}[monies]{/b}":
        xalign 0.22
        yalign 0.0225
    text "{b}Day [days]{/b}":
        xalign 0.065
        yalign 0.0225


label prefinalworldmap:
    play music day fadein 3.0
    play ambience ambienceday fadein 5.0
label finalworldmap:
    $ worldmap = 3
    hide screen todolist
    scene bg pgworldmapday
    call screen finalworldmap
    with qd
