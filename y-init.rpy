#characters#
init:
    define gui.dialogue_text_outlines = [ (0, "#00000080", 2, 2) ]
    define gui.characters_text_outlines = [ (0, "#00000080", 2, 2) ]
    define gui.name_text_outlines = [ (0, "#00000080", 2, 2) ]
    define gui.menu_text_outlines = [ (0, "#00000080", 2, 2) ]
    define unnamedmc = Character(_("Male Familiar?"), color="a4f8ff", what_color="a4f8ff")

    define mc = Character(_("[playername]"), color="a4f8ff", what_color="a4f8ff")
    define moxie = Character(_("Moxie"), color="#7df5ff", what_color="a4f8ff")

    define penelope = Character(_("Penelope"), color="d703fc", what_color="a4f8ff")
    define lily = Character(_("Lily"), color="9803fc", what_color="a4f8ff")
    define honeycrisp = Character(_("Honeycrisp"), color="fc9d03", what_color="a4f8ff")
    define blossom = Character(_("Blossom"), color="fce303", what_color="a4f8ff")
    define anna = Character(_ ("Anna"), color="03fc84", what_color="a4f8ff")
    define ruby = Character(_("Ruby"), color="fc034a",what_color="a4f8ff")
    define melody = Character(_("Melody"), color="fc03c6",what_color="a4f8ff")
    define butters = Character(_("Butters"), color="fcca03",what_color="a4f8ff")

    define cream = Character(_("Cream"), color="fcca03",what_color="a4f8ff")
    define carrot = Character(_("Carrot"), color="fc9d03",what_color="a4f8ff")
    define blue = Character(_("Blueberry"), color="a4f8ff",what_color="a4f8ff")
    define purple  = Character(_("Blackcurrant"), color="9803fc",what_color="a4f8ff")

    define morrigan = Character(_("Morrigan"), color="00a5a1",what_color="a4f8ff")
    define guard1 = Character(_("Guard 1"), color="ffffff", what_color="a4f8ff")
    define guard2 = Character(_("Guard 2"), color="ffffff", what_color="a4f8ff")
    define guard3 = Character(_("Guard 3"), color="ffffff", what_color="a4f8ff")
    define guard4 = Character(_("Guard 4"), color="ffffff", what_color="a4f8ff")

    define dawn = Character(_("Dawn"), color="7df5ff", what_color="#ffccfe")
    define dressdawn = Character(_("Dress Dawn"), color="7df5ff", what_color="#ffccfe")
    define dawn2 = Character(_("Anthro Dawn"), color="fce303", what_color="#a4f8ff")
    define dawnunknown = Character(_("???"), color="7df5ff", what_color="#ffccfe")

    define amora = Character(_("Amora"), color="d703fc", what_color="#a4f8ff")
    define augusta = Character(_("Augusta"), color="d703fc", what_color="#ffccfe")

    define devil = Character(_("Devil"), color="ff7573",what_color="a4f8ff")
    define riku = Character(_("Riku"), color="ff7573",what_color="a4f8ff")
    define selene = Character(_("Princess Selene"), color="263d91", what_color="a4f8ff")
    define aurora = Character(_("Queen Aurora"), color="ffea70",what_color="a4f8ff")
    define paurora = Character(_("Principal Aurora"), color="ffea70",what_color="a4f8ff")

    define unknown = Character(_("???"), color="808080", what_color="a4f8ff")
    define camshowaudience = Character(_("Camshow Audience"), color="808080", what_color="a4f8ff")

    define merchant = Character(_("Merchant"), color="808080", what_color="a4f8ff")
    define ari = Character(_("Ari"), color ="ff9654", what_color="a4f8ff")
    define agatha = Character(_("Agatha"), color ="ff8ae4", what_color="a4f8ff")
    define sonia = Character(_("Sonia"), color ="ffef85", what_color="a4f8ff")
    define sofia = Character(_("Sofia"), color="ffb0ff",what_color="a4f8ff")
    define greymare = Character(_("[greymare]"), color="9B9B9B", what_color="a4f8ff")
    $ greymare = "Grey Mare"
    define whitemare = Character(_("[WhiteMare]"), color="ffffff", what_color="a4f8ff")
    $ whitemare = "White Mare"

    define ci = Character(_("Cindy"), color="c56eff", what_color="a4f8ff")
    define sa = Character(_("Sandy"), color ="ff8ae4", what_color="a4f8ff")
    define zo = Character(_("Zoe"), color="8a8a8a", what_color="a4f8ff")


    define everyone = Character(_("Everyone"), color="ffffff", what_color="a4f8ff")
    define slime = Character(_("Slime Girl"), color="00ddff",what_color="a4f8ff")
    define poyo = Character(_("Poyo"), color="00ddff",what_color="a4f8ff")
    define alraune = Character(_("Alraune"), color="fc9d03", what_color="a4f8ff")
    define midna = Character(_("Midna"), color="9B9B9B", what_color="a4f8ff")
    define claire = Character(_("Claire"), color="9B9B9B", what_color="a4f8ff")
    define doggirl = Character(_("[doggirl]"), color="ffea70", what_color="a4f8ff")
    $ doggirl = "Dog Girl"
    define wolfgirl = Character(_("[wolfgirl]"), color="d703fc", what_color="a4f8ff")
    $ wolfgirl = "Wolf Girl"

    #effects#
    define flash = Fade(.25, 0.0, .75, color="#fff")
    define cum = Fade(.25, 0.0, .75, color="#fff")
    define fcum = Fade(.9, 0.0, .37, color="#fff")
    define moxiespell = Fade(.25, 0.0, .75, color="#cd05e5")
    define morriganspell = Fade(.25, 0.0, .75, color="#00a5a1")
    define qd = Dissolve(0.2)
    define s = Dissolve(3.0)
    define ss = { "master" : Dissolve(10.0)}
    define d = Dissolve (0.3)

    define audio.suspense = "music/Suspense.mp3"
    define audio.wagon = "music/Wagon.mp3"
    define audio.wagon2 = "music/Wagon2.mp3"
    define audio.sex1 = "music/sex1.mp3"
    define audio.emotional = "music/ConqueredEmotions.mp3"
    define audio.day = "music/daytheme.mp3"
    define audio.daytheme = "music/daytheme.mp3"
    define audio.day2 = "music/daytheme2.mp3"
    define audio.farm = "music/farm.mp3"
    define audio.boutique = "music/boutique.mp3"
    define audio.library = "music/library.mp3"
    define audio.uhoh = "music/uhoh.mp3"
    define audio.castle = "music/castle.mp3"
    define audio.hopelessness = "music/hopelessness.mp3"
    define audio.ambientinterlude = "music/ambientinterlude.mp3"
    define audio.melodytheme = "music/lorncloud.mp3"
    define audio.challenge = "music/challenge.mp3"
    define audio.sad = "music/SoftPianoandCello.mp3"
    define audio.sad2 = "music/DanseMorialta.mp3"
    define audio.bar = "music/Bar.mp3"
    define audio.yanderecomplex = "music/YandereComplex.mp3"
    define audio.inpeace = "music/inpeace.mp3"
    define audio.inlove = "music/inlove.mp3"
    define audio.lily = "music/lily.mp3"
    define audio.epic = "music/epic.mp3"
    define audio.intense = "music/Intense.mp3"
    define audio.PeaceSerenity = "music/Peace&Serenity.mp3"
    define audio.butters = "music/butters.mp3"
    define audio.danger = "music/danger.mp3"
    define audio.anotherperspective = "music/anotherperspective.mp3"
    define audio.triads = "music/triads.mp3"
    define audio.artofsilence = "music/artofsilence.mp3"
    define audio.dissociation = "music/dissociation.mp3"
    define audio.spookybreathing = "music/spookybreathing.mp3"
    define audio.eyesofthewind = "music/eyesofthewind.mp3"
    define audio.sadpiano = "music/sadpiano.mp3"
    define audio.cream1 = "music/cream1.mp3"
    define audio.mky = "music/mrkillyourself.mp3"
    define audio.minikillyourself = "music/minikillyourself.mp3"
    define audio.aurora = "music/aurora.mp3"
    define audio.lips = "music/lips.mp3"
    define audio.morrigan = "music/oni.mp3"
    define audio.morriganbattle = "music/morriganbattle.mp3"
    define audio.nightclub = "music/cyberialyr3.mp3"
    define audio.nightclub2 = "music/cyberialyr32.mp3"
    define audio.dawn = "music/dawn.mp3"
    define audio.church = "music/church.mp3"
    define audio.augusta = "music/augusta.mp3"
    define audio.toewizard = "music/ToeWizard.mp3"


    #ambience#

    define audio.ambienceday = "sounds/ambienceday.mp3"
    define audio.ambiencenight = "sounds/ambiencenight.mp3"
    define audio.ambienceotherworldly = "sounds/ambienceotherworldly.mp3"
    define audio.ambiencecave = "sounds/ambiencecave.mp3"
    define audio.ambiencewind = "sounds/ambiencewind2.mp3"
    define audio.ambiencerain = "music/ambiencerain.mp3"
    define audio.ambiencecity = "sounds/ambiencecity.mp3"
    define audio.waves = "sounds/waves.mp3"
    define audio.raindistantthunder = "sounds/raindistantthunder.mp3"
    define audio.thunderstorm = "sounds/thunderstorm.mp3"

    #sounds#

    define audio.cork = "sounds/cork.mp3"
    define audio.dudududumeme = "sounds/dududududumeme.mp3"
    define audio.blowjob = "sounds/blowjob.mp3"
    define audio.explosion = "sounds/explosion.mp3"
    define audio.explosion2 = "sounds/bomb4.mp3"
    define audio.cum = "sounds/cum.mp3"
    define audio.sex = "sounds/sex.mp3"
    define audio.sex2 = "sounds/sex2.mp3"
    define audio.magic1 = "sounds/magic1.mp3"
    define audio.magic2 = "sounds/magic2.mp3"
    define audio.magic3 = "sounds/magic3.mp3"
    define audio.open = "sounds/open4.mp3"
    define audio.door = "sounds/door5.mp3"
    define audio.knock = "sounds/knock.mp3"
    define audio.move = "sounds/knock.mp3"
    define audio.strings = "sounds/strings.mp3"
    define audio.spank = "sounds/spank.mp3"
    define audio.floorboards = "sounds/floorboards.mp3"
    define audio.thunder = "sounds/thunder.mp3"
    define audio.cartoonimpact = "sounds/cartoonimpact.mp3"
    define audio.prismaserenade = "sounds/prismaserenade.mp3"
    define audio.movie = "sounds/movie.wav"
    define audio.dressing = "sounds/dressing.mp3"
    define audio.ping = "sounds/ping.mp3"
    define audio.doorbell = "sounds/doorbell.mp3"
    define audio.transition1 = "sounds/transition1.mp3"
    define audio.movement = "sounds/movement.mp3"
    define audio.thunder1 = "sounds/thunder1.mp3"
    define audio.thunder2 = "sounds/thunder2.mp3"
    define audio.distantbang = "sounds/distantbang.mp3"
    define audio.morriganattack1 = "sounds/morriganspell1.mp3"
    define audio.morriganattack2 = "sounds/morriganspell2.mp3"
    define audio.morriganattack3 = "sounds/morriganspell3.mp3"
    define audio.sharpmagicimpact = "sounds/sharpmagicimpact.mp3"
    define audio.gameendblast = "sounds/gameendblast.mp3"
    define audio.moxiespell1 = "sounds/moxiespell1.mp3"
    define audio.moxiespell2 = "sounds/moxiespell2.mp3"
    define audio.moxiespell3 = "sounds/moxiespell3.mp3"
    define audio.towerspell = "sounds/towerspell.mp3"
    define audio.smash = "sounds/smash.mp3"
    define audio.thundercharge = "sounds/thundercharge.mp3"
    define audio.genericmagic = "sounds/genericmagic.mp3"
    define audio.genericspell = "sounds/genericmagic.mp3"
    define audio.rainoffire = "sounds/rainoffire.mp3"
    define audio.woosh = "sounds/woosh.mp3"

    # Images
    $ mainmenu = "gui/main_menu.png"


#variables#
    ## 1.2:
    init:
        $ secretsunlocked = 0
        $ devilsex = 0
        $ werewolfsex = 0
        $ clairewwc = 0
        $ sandysex = 0
        $ doubledog = 0
        $ honeycrispoutsidesex = 0
        $ creamlingeriesex = 0
        $ rubylingeriesex = 0
        $ rikuclimbingsex = 0
        $ lilysplitsex = 0
        $ dawnshowersex = 0
        $ melodycunnilingus = 0
        $ succworksex = 0

    ## misc 1.2
    init:
        $ melcunnilingustoday = 0

    #Various
    init:
        $ spaday = 0
        $ dlc = 1

        $ buttersrikuthreesome = 0
        $ alraunesex = 0
        $ alraunec = 0
        $ zoelum = 0
        $ zoedog = 0
        $ zoevisit1 = 0
        $ zoe = 0

        $ cindyanal1 = 0
        $ cindylum1 = 0
        $ cindyrcg1 = 0
        $ cindylum = 0
        $ cindyrcg = 0
        $ cindymet = 0
        $ bavcl = 0

        $ lilfulast = 0
        $ fleursex = 0
        $ spaday = 0
        $ muffinsmet = 0
        $ zoemet = 0
        $ galleryyear = 0
        $ gallerydpass = 0
        $ galleryypass = 0
        $ artgallery = 0
        $ aure = 3
        $ aurpa1 = 0
        $ augustasex = 0
        $ augustareview15 = 0
        $ augname = 0
        $ augustavisit = 0
        $ pauroraft = 0
        $ pauroras = 0
        $ dawnmilk = 0
        $ spatodo = 0
        $ dawntalk = 0
        $ dawnv2c1 = 0
        $ arisextoday = 0
        $ arisex = 0
        $ sofiasex = 0
        $ honeyrubythreesome = 0
        $ agathasoniathreesome = 0
        $ dawnvisit = 0
        $ dawnltr = 0
        $ musicstudionight = 0
        $ nightclubintro = 0
        $ nightclubmenuintro = 0
        $ milkypaizuriunlocked = 0
        $ butterspregnanteasteregg = 0
        $ buttersmissionaryunlock = 0
        $ butterspregnant = 0
        $ buttersimpregintro = 0
        $ citynightfirstvisit = 0
        $ sofiasex = 0
        $ honeyrubythreesome = 0
        $ sdps = 0
        $ nightclubday = 0
        $ worldmap = 1
        $ inv1sttime = 0
        $ todo1st = 0
        $ fr = 0
        $ finalroute = 0
        $ milk3 = 0
        $ passcorrect = 0
        $ timer_range = 0
        $ timer_jump = 0
        $ monies = 0
        $ days = 2
        $ debt = 0
        $ permit = 0
        $ debt = 0
        $ splashscreen = 0
        $ rand = 0
        $ rand2 = 0
        $ todturns = 0
        $ mctruths = 0
        $ mcdares = 0
        $ cityfirstvisit = 0
        $ musicstudio = 0
        $ musicstudiosex = 0
        $ lilysex = 0
        $ honeycrispsex = 0
        $ doggirl1 = 0
        $ wolfgirl1 = 0
        $ buttersprismathreesome = 0
        $ rubysex = 0

    #visits
    init:
        $ farmvisits = 0
        $ farmvisit1 = 0
        $ farmvisit2 = 0
        $ farmvisit3 = 0
        $ boutiquevisits = 0
        $ boutiquevisit1 = 0
        $ boutiquevisit2 = 0
        $ boutiquevisit3 = 0
        $ libraryvisits = 0
        $ libraryvisit1 = 0
        $ libraryvisit2 = 0
        $ libraryvisit3 = 0
        $ bakeryvisits = 0
        $ bakeryvisit1 = 0
        $ bakeryvisit2 = 0
        $ barvisits = 0
        $ barvisit1 = 0
        $ barvisit2 = 0
        $ forestvisits = 0
        $ forestvisit1 = 0
        $ forestvisit2 = 0
        $ selenevisits = 0
        $ selenevisit1 = 0
        $ selenevisitsetup = 0
        $ auroravisits = 0
        $ auroravisit1 = 0
        $ spavisit = 0
        $ spaspecial = 0
        $ alphabakeryvisits = 0
        $ alphalibraryvisit = 0
        $ alphabarvisit = 0
        $ marketfirstvisit = 0
        $ spavisited = 0
        $ annamilking = 0
        $ cowvillagevisit = 0
        $ boutiqueaftervisit1 = 0
        $ melodyeveningsex1 = 0
        $ melodyeveningvisit1 = 0
        $ buttersthirdvisitsetup = 0
        $ buttersforestvisit4 = 0
        $ marketequipmentvisit = 0
        $ blossomvisit = 0
        $ confessedsexwithblossom = 0
        $ forestvisit3 = 0
        $ honeycrispcomplete = 0
        $ aurorasex = 0
        $ midnasex = 0
        $ selenevisitready = 0
        $ ashoney = 0
        $ saruby = 0
        $ blossomsex = 0
        $ hildasex = 0
        $ rosasex = 0
        $ midnadiscount = 0
        $ midnayou = 0
        $ midnasexd = 0
        $ creamfuckedday1 = 0
        $ auroravisitsetup = 0
        $ soniaagathasex = 0
        $ arisex = 0
        $ dawnvisit1 = 0
        $ dawnvisit2 = 0
        $ dawnvisit3 = 0
        $ dawnvisit4 = 0

    #Inventory Related
    init:
        $ lingerie = 0
        $ lesbianknowledge = 0
        $ chocolates = 0
        $ moxiechocolates = 0
        $ butterschocolates = 0
        $ roses = 0
        $ buttersroses = 0
        $ moxieroses = 0
        $ moxiecowgirl = 0
        $ moxieanal = 0
        $ moxiesextoys = 0
        $ buttersdoggystyle = 0
        $ buttersreversecowgirl = 0
        $ crystalball = 0
        $ crystalballactivated = 0
        $ forestmonies = 25
        $ rope = 0
        $ leatherarmor = 0
        $ scimitar = 0
        $ crystalballdayactivated = 0
        $ crystalballactivated = 0
        $ maiddressbought = 0
        $ melodylaptop = 0
        $ lingeriebought = 0


    #Conversational
    init:
        $ ariflirtcounter = 0
        $ honeycrisptalks = 0
        $ blossomtalks = 0
        $ rubytalks = 0
        $ melodytalks = 0
        $ creamtalks = 0
        $ prismatalks = 0
        $ moxietalks = 0
        $ lilytalks = 0
        $ penelopetalks = 0
        $ butterstalks = 0
        $ succbutterstalks = 0
        $ poyotalks = 0
        $ auroratalks = 0
        $ auroratalk = 0
        $ selenetalks = 0
        $ selenetalk = 0
        $ blossommelodytalk = 0
        $ moxiefarmtalk = 0
        $ moxieboutiquetalk = 0
        $ moxiebakerytalk = 0
        $ moxieforesttalk = 0
        $ moxielibrarytalk = 0
        $ moxiebartalk = 0
        $ annatalks = 0
        $ boutiqueafteramv = 0
        $ melodysex = 0
        $ livingwithbutters = 0
        $ livingwithmoxie = 1
        $ livingwithbuttersfirsttime = 0
        $ midnabar = 0
        $ selenesex = 0
        $ cst = 0
        $ frs = 0
        $ wmnu1 = 0
        $ aurorahumanconversation = 0
        $ rubyhoneycrispbar = 0
        $ buttersbar = 0
        $ magictriobar = 0
        $ mingle = 0
        $ musicstudiotalk = 0
        $ butterssexfta = 0
        $ buttersgifts = 0
        $ moxiegifts = 0
        $ midnaflirt = 0
        $ prismasex = 0
        $ prismamoxiethreesome = 0
        $ creamsex2 = 0

    #Genuinely random
    init:
        $ turnedintogirl = 0
    #endgame
    init:
        $ clibvisit = 0
        $ cbakvisit = 0
        $ cforvisit = 0
        $ cbarvisit = 0
        $ cbouvisit = 0
        $ cfarvisit = 0
        $ clibcom = 0
        $ cbakcom = 0
        $ cbarcom = 0
        $ cboucom = 0
        $ cfarcom = 0
        $ moxieend = 0
        $ lilyend = 0
        $ honeycrispend = 0
        $ rubyend = 0
        $ blossomend = 0
        $ prismaend = 0
        $ melodyend = 0
        $ buttersend = 0
        $ creamend = 0
        $ seleneend = 0
        $ auroraend = 0
        $ nvm = 0


label start:
    #variable setup#
    stop music fadeout 1.0
    jump prologue
