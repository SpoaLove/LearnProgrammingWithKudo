# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kudo = Character("kudo")
define slowdissolve = Dissolve(1.0)

label start:

    scene bg bushitsu
    show kudo working
    "Kudo is working with her laptop"
    "Let's go and check out"

    kudo "..."
    show kudo working realized
    kudo "almost there..."
    show kudo working happy
    kudo "Done!"
    show kudo surprised
    kudo "Riki?"
    show kudo smile hand
    kudo "I am working on an online programming lesson"
    show kudo laugh handin
    kudo "Do you want to have a try?"


menu:

    "Yes, I do.":
        jump choice1_yes

    "No, I don't.":
        jump choice1_no

label choice1_yes:

    $ menu_flag = True
    show kudo wafu hand
    kudo "Wafu!"
    show kudo working happy
    kudo "Wait a second, I will open up the tutorial lesson for you"
    jump choice1_done

label choice1_no:
    show kudo sad handin
    "she look very dissapointed..."
    $ menu_flag = False
    "lets try it anyways!"
    jump choice1_yes

label choice1_done:
    jump start
