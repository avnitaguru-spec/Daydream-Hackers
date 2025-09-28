# Characters
define m = Character("Meowknight", color="#66ccff")
define h = Character("Holy Mage", color="#ff99ff")
define d = Character("Evil Blob", color="#ff3333")
# Images (based on your actual files)
image bg cliff = "meowknightintro"
image bg dungeon = "meowknightlibrary1"
image bg mage_room = "meowknightinlibrary.jpeg"
image bg library = "meowknightinlibrary.jpeg"
image bg library_battle = "meowknightgetsthecure.jpeg"
image bg cliff_day = "mk good ending.jpeg"

image meowknight = "Dead MK.jpeg"
image mage = "Dead Hm.jpeg"
image blob = "Dead MK.jpeg"  # Placeholder image

# Creator photos
image creator1 = "avnita-pfp.png"
image creator2 = "juana-pfp.png"
image creator3 = "thy-pfp.png"

label start:

    ### Scene 1 ###
    play sound "fiji-meow-01.mp3"
    play music "sad-meow-song.mp3"

    scene bg cliff with fade
    show meowknight at center

    m "I…must do something. This place is my home."
    m "The Holy Mage shall return under my direction with her cure."
    m "Time to start the journey…"

    ### Scene 2 ###
    scene bg dungeon with fade
    "Meowknight spawns in a dungeon. Poison drips everywhere, bodies piled around..."
    "He slips and falls into an ancient well."

    "What should Meowknight do?"

    menu:

            "Scream for help":
                jump bad_end
            "Swim up":
                jump scene4

label bad_end:
    show blob at center
    "An evil mage appears and kills Meowknight."
    centered "THE END"
    return

label scene4:
    ### Scene 4 ###
    play music "dying-sound.mp3"
    play sound "heartbeat.mp3"

    "Meowknight’s vision blurs as he dies..."
    "Suddenly, the Holy Mage appears, saving him with the cure."

    m "This level is impossible!!!"
    m "I’m….dying…my kingdom…"
    m "Is that you…Holy Mage…?"

    ### Scene 5 ###
    scene bg mage_room
    show meowknight at left
    show mage at right

    m "Holy Mage…please return to the kingdom! I know you’ve been hiding from publicity…but we really, really need you, now more than ever."
    h "I…cannot, I’m afraid."
    m "Please, Mage, you’re the only person with the cure!"
    h "....Fine. Though, we must first find the formula from my library. I need someone to go with me."

    ### Scene 6 ###
    scene bg library
    show meowknight at left
    show mage at right

    h "It’s quite messy….my apologies. I wasn’t expecting a visitor after all these years."
    h "Do mind the broken glass. They hurt very, VERY bad."

    ### Scene 7 ###
    scene bg library_battle
    show blob at center

    h "WHAT?!"
    m "It’s an Evil Blob…He’ll attack us!"
    d "All those PESTS. They will die out under MY watch. You cannot take the cure from me. I am a mighty Evil Blob, the superior species."

    "What should Meowknight do?"

    menu:
 
            "Sacrifice Holy Mage":
                jump cutscene8a
            "Trust Holy Mage":
                jump cutscene8b

label cutscene8a:
    ### Cutscene 8A – Mage Sacrifice ###
    d "You’ll never get past me!"
    h "Knight. Listen to what I say carefu-"
    m "...Sacrifices must be made..."
    h "...No. I’ve been alive for so long..."
    d "You both will die!"
    h "Go, knight, take the recipe and run towards the exit."
    d "Yelp! It’s blinding!"
    m "I got the recipe! The fight is over."
    m "Rest in peace….Mage."

    jump scene9

label cutscene8b:
    ### Cutscene 8B – Knight Sacrifice (Betrayal) ###
    d "You’ll never get past me!"
    h "Knight. Listen to what I say carefu-"
    m "My friends…my family…they’ll understand. I’ll do it."
    d "You slow twats, hurry up and run towards your death."
    m "As long as the kingdom is saved…I’ll gladly give my life…"
    h "Spare me! O great Evil Blob! I won’t try to save the kingdom!"
    m "Did she…lie? Oh no….my family…."
    d "Heh…I knew all of you cats are spineless wimps!"
    m "Damn it all…"

    centered "THE END"
    return

label scene9:
    ### Scene 9 – Ending ###
    scene bg cliff_day with fade
    show meowknight at center

    "Five months later…"
    m "The world is a much better place now. Thank you, Holy Mage, you’ve given your life to a beautiful cause."

    centered "THE END"

    jump credits_choice

label credits_choice:

    "How would you like to view the credits?"

    menu:

            "Slideshow (one by one)":
                jump about_me_slideshow
            "Side-by-side (all at once)":
                jump about_me_sidebyside

label about_me_slideshow:
    scene black with fade
    with Pause(1.0)

    centered "✨ ABOUT THE CREATORS ✨"
    with Pause(2.0)

    scene black
    show creator1 at center
    with dissolve
    centered "Name: Thy L.\nRole: Visuals/Audio & Storyboarding"
    with Pause(4.0)

    scene black
    show creator2 at center
    with dissolve
    centered "Name: Juana B.\nRole: Coder & Designer"
    with Pause(4.0)

    scene black
    show creator3 at center
    with dissolve
    centered "Name: Avnita G.\nRole: Artist & Emotional Support"
    with Pause(4.0)

    scene black
    centered "💖 Thank you for playing Meowknight’s Quest 💖"
    with Pause(3.0)

    return

label about_me_sidebyside:
    scene black with fade
    with Pause(1.0)

    centered "✨ ABOUT THE CREATORS ✨"
    with Pause(2.0)

    show creator1 at left
    show creator2 at center
    show creator3 at right
    with dissolve

    show text "Thy L.\nVisuals/Audio & Storyboarding" at Position(xalign=0.2, yalign=0.9)
    show text "Juana B.\nCoder & Designer" at Position(xalign=0.5, yalign=0.9)
    show text "Avnita G.\nArtist & Emotional Support" at Position(xalign=0.8, yalign=0.9)

    with Pause(6.0)

    scene black with fade
    centered "💖 Thank you for playing Meowknight’s Quest 💖"
    with Pause(3.0)

    return
