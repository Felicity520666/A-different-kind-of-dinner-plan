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
    pause 5
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
    play music "emotional-sad-guitar-music-349888 6.29.52 PM.mp3"
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
    play music "mad-145260.mp3"
    a "Oh hey Lucy!"
    a "Are you ready!"
    l "Oh yeah Abby..."
    l "I AM SO READY..."
    l "TO CUT TIES WITH YOU!"
    play sound "crying-411857.mp3"
    a "Lucy...? Boohoo... What are you even talking about...?"
    a "You're mean..."
    play sound "grunting-228447.mp3"
    l "Me? Mean?"
    l "YOU are mean!"
    l "You never listened to me!"
    l "Every conversation is you talking about your ideas."
    l "And when I try to say something, it's like shouting into a tunnel."
    l "I don't enjoy our friendship anymore!"
    play sound "girl-oh-no-150550.mp3"
    a "Oh, no!"
    a "Lucy, please..."
    a "I didn't know you felt this way."
    a "You could've just told me."
    l "I tried. Dozens of times."
    l "You brushed it off."
    a "Well, I'm sorry..."
    a "So, you don't like adventures...?"
    l "Abby!!!"
    a "Okay, okay, I get it now..."
    a "How was I suppose to know?"
    l "Abby, what frustrates me isn't that you didn't know. It's that you didn't try to know."
    l "I shouldnt have to fight you just to be heard."
    l "Friendship isn't supposed to feel like competing for attention."
    play sound "sigh_1_female-83927"
    a "Wow Lucy, I didn't realize you thought I was that terrible of a friend."
    l "I don't think you're terrible. I think you're self-absorbed and not willing to admit it!"
    l "Bye Abby. I hope you find a new bestie who don't get annoyed with you!"
    play sound "im-sorry-what-83636.mp3" volume 5.0
    a "I'm sorry what?!"
    a "Lucy... You... You're joking right?"
    l "I'm not. I can't keep giving and giving while you take and take and call it friendship."
    play sound "girl-sighs-80765.mp3"
    l "I'm tired. I'm hurt. And I don't trust that anything will change, because every time I've brought something up, you made me feel like I was overreacting."
    l "For once, Abby, maybe just listen. Goodbye."
    a "..."
    return