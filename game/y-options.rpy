## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Friendship with Benefits")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.20"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _("""Art, Coding and Writing:
TwistedScarlett60
Spelling and Grammar Checking: Jinjo Bytes

All music is royalty free and used with permission.
However, considering the subject of my game, please don't hesistate to message me if I'm using your content and you're not comfortable associating with it.

Music:
Bread - {a=https://soundcloud.com/lukrembo}Lukrembo{/a}
Dissociation - {a=https://soundcloud.com/naoya-sakamata}Naoya Sakamata{/a}
Another Perspective - {a=https://soundcloud.com/idealismus}Idealism{/a}
Before you Fall Asleep - {a=https://soundcloud.com/jhovebeats}Jhove{/a}
Art of Silence - {a=https://soundcloud.com/uniqofficial/art-of-silence}Uniq{/a}
Fire and Thunder - {a=https://soundcloud.com/cjbeards}Cjbeards{/a}
inlove - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Mr Kill Yourself - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Lips - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Oni - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Euphoric Filth - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
inpeace - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
inlove - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Yandere Complex - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
lorncloud - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Hopelessness - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Slow Death - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Cyberia lyr3 - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
The Maw - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Toe Wizard - {a=https://www.patreon.com/sewerslvt}Sewerslvt{/a}
Blue Boi - {a=https://soundcloud.com/lakeyinspired}Lakey Inspired{/a}
Untitled - {a=https://soundcloud.com/lakeyinspired}Lakey Inspired{/a}
Conquered Emotions - {a=https://soundcloud.com/user-811451507}Yakuzee Beatz{/a}
Soul Aches - {a=https://soundcloud.com/user-811451507}Yakuzee Beatz{/a}
That's One Sly Cat - {a=https://soundcloud.com/artificial-music}Artificial Music{/a}
Abstract Foilage - {a=https://soundcloud.com/artificial-music}Artificial Music{/a}
Secrets - {a=https://soundcloud.com/user-602857531}Michael Hildreth{/a}
Good Day - {a=https://www.youtube.com/LowFrequencyMusic}Low Frequency Music{/a}
Sad Piano - Mark Clark
Pina Colada - {a=https://soundcloud.com/silentpartnermusic}Silent Partner{/a}
Tranquil - {a=https://soundcloud.com/martynaslau}Whitesand{/a}
Been Here Before - {a=https://soundcloud.com/no_mic}NO MIC{/a}
Stuck in the Machine - {a=https://soundcloud.com/no_mic}NO MIC{/a}
Danse Morialta - {a=https://incompetech.com/}Kevin MacLeod{/a}
Hip Jazz - {a=www.bensound.com}Benjamin Tissot{/a}
Basic Metal 6 - {a=http://teknoaxe.com/Home.php}TeknoAXE{/a}
Jazz Organ Trio Cool Blue - Doug Maxwell
La Fille aux Cheveux de lin - Claude Debussy


Sound Effects from https://www.zapsplat.com""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "FriendshipwithBenefits"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

init:
    define config.has_sound = True
    define config.has_music = True
    define config.default_music_volume = 0.5
    define config.default_sfx_volume = 1.0
init python:
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True)
init python:
    renpy.music.register_channel("sound2", mixer="sfx", loop=False, stop_on_mute=True, tight=False, buffer_queue=True)



## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = None


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = dissolve


## Used when entering the main menu after the game has ended.

define config.end_game_transition = dissolve


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 55


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "FriendshipwithBenefits"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 排除翻译文件

    build.classify('paratranz/*', None)
    build.classify('README.md', None)
    build.classify('*.js', None)

    ## 排除源码

    build.classify('game/**.rpy', None)

    ## To archive files, classify them as 'archive'.

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.rpt', 'archive')
    build.classify('game/**.rpyc', 'archive')
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')
    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

### Text Box
define gui.text_size = 18
define gui.textbox_height = 150

## Rollbacks
define config.rollback_length = 6

## Timer
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.
