# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lucy", color="#9b3c11")
define a = Character("Abby", color="#118bd8")


# The game starts here.

label start:
    play music "just-relax-11157.mp3" fadein 1.0
    # A simple ATL transform that centers the background and applies a
    # small zoom so images that don't perfectly match the window aspect
    # ratio will cover the screen instead of leaving transparent bars.
    transform bg_cover:
        xalign 0.5
        yalign 0.5
        zoom 1.21

    scene res at bg_cover with fade
    pause 3
    #scene zoom at bg_cover with dissolve
    pause 1
    play sound "girl-laugh-6689.mp3"
    l "What a beautiful day!"
    a "Indeed it is, Lucy. Perfect for an adventure."
    play sound "girl-oh-no-150550.mp3"
    l "Oh no..."
    l "What...? An adventure?"
    l "Are you kidding me, Abby?!"
    l "You know how much I hate..."
    a "We could go to the forest, or the lake... Oh! What about the old castle on the hill?"
    l "Wait! Can't you let me finish? I don't want..."
    a "You know what! I have the perfect idea!!! We could go to the secret cave I once found!"
    a "It looks so creepy, but I bet it's full of treasures!"
    a "So get ready for an unforgettable day full of suprises!"
    l "Ugh! Abby! You..."
    a "It's settled then! Remember to bring a flashlight!"
    play sound "teenage-girl-says-woo-186594.mp3"
    a "Woo! We might get hungry!"
    a "So we can go have dinner together at seven o'clock and go exploring the cave in the dark!"
    a "Oh la la! That way it's way more fun!"
    a "So see you at seven o'clock, Lucy!"
    play sound "girl-sighs-80765.mp3"
    l "..."
    scene bedroom at bg_cover with fade
    pause 1.1
    scene cy at bg_cover with fade
    play sound "female-scream-short-251067.mp3"
    l "What the f*ck?!"
    l "Why is Abby so annoying!!!"
    l "She just does whatever she wants! She doesn't listen to me at all—it feels like I'm invisible."
    l "Ugh! I can't stand it!!!"
    l "Why are we even friends?!"
    l "That whole “adventure in a cave” idea — like what are we, broke explorers?!"
    play sound "sigh_1_female-83927.mp3"
    l "I just want to stay home and watch my freaking TV! I'm definitely not going..."
    l "…Or maybe I could go and give her A DIFFERENT KINF OF DINNER PLAN..."
    l "Yeah, let's do that..."
    l "She doesn't deserve to be my bestie anymore:("
    scene res at bg_cover with dissolve