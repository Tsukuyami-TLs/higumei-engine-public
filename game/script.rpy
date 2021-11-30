# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.gl2 = True

define rika = Character("Rika")


# The game starts here.

label start:
    
    $ Engine.run_file('scripts/event01_30_01.bytes', 'tl/tl/event_01_30_01.csv')

    return

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show rika_v001 smile

    rika "Nipaah. I am blinking frequently for demonstration purposes"
    
    show rika_v001 futeki_close

    rika "Now I will close my eyes and be smug!"

    show rika_v001 odoroki_blush

    rika "Surprised blush"

    hide rika_v001 with dissolve

    rika "Poof"

    return
