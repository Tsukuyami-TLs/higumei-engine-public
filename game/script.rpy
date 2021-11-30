# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.gl2 = True

define rika = Character("Rika")

init:
    transform mei_left:
        xanchor 0.0
        xpos 0.0
        xoffset 100

        yanchor 1.0
        ypos 1.0
        yoffset 100

    transform mei_right:
        xanchor 1.0
        xpos 1.0
        xoffset -100

        yanchor 1.0
        ypos 1.0
        yoffset 100
    
    transform mei_center:
        xanchor 0.5
        xpos 0.5

        yanchor 1.0
        ypos 1.0
        yoffset 100
    


# The game starts here.
label start:
    jump event01_30_01
    return


label rika_test:
    show rika_v001 smile
    rika "Nipaah. I am blinking frequently for demonstration purposes"
    
    show rika_v001 futeki_close
    rika "Now I will close my eyes and be smug!"

    show rika_v001 odoroki_blush
    rika "Surprised blush"

    hide rika_v001 with dissolve
    rika "Poof"

    return
