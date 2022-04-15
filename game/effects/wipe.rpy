image wipeout1 = Image("images/effects/wipeout.png", yanchor=0.0, ypos=0, yzoom=0.8)
image wipeout2 = Image("images/effects/wipeout.png", yanchor=0.0, ypos=200, yzoom=0.5)
image wipeout3 = Image("images/effects/wipeout.png", yanchor=0.0, ypos=325, yzoom=1.0)
image wipeout4 = Image("images/effects/wipeout.png", yanchor=0.0, ypos=575, yzoom=0.4)
image wipeout5 = Image("images/effects/wipeout.png", yanchor=0.0, ypos=675, yzoom=0.8)
image wipeout6 = Image("images/effects/wipeout.png", yanchor=0.0, ypos=879, yzoom=0.3)
image wipeout7 = Image("images/effects/wipeout.png", yanchor=0.0, ypos=955, yzoom=0.6)

image wipein1 = Image("images/effects/wipein.png", yanchor=0.0, ypos=0, yzoom=0.8)
image wipein2 = Image("images/effects/wipein.png", yanchor=0.0, ypos=200, yzoom=0.5)
image wipein3 = Image("images/effects/wipein.png", yanchor=0.0, ypos=325, yzoom=1.0)
image wipein4 = Image("images/effects/wipein.png", yanchor=0.0, ypos=575, yzoom=0.4)
image wipein5 = Image("images/effects/wipein.png", yanchor=0.0, ypos=675, yzoom=0.8)
image wipein6 = Image("images/effects/wipein.png", yanchor=0.0, ypos=879, yzoom=0.3)
image wipein7 = Image("images/effects/wipein.png", yanchor=0.0, ypos=955, yzoom=0.6)

transform wipeout_transform:
    xanchor 0.0
    xpos 2000
    linear 0.1 xpos -500

transform wipein_transform:
    xanchor 1.0
    xpos 2420
    linear 0.1 xpos -80

label wipeout_routine:
    show wipeout4 at wipeout_transform
    pause 0.03
    show wipeout3 at wipeout_transform
    pause 0.03
    show wipeout5 at wipeout_transform
    pause 0.03
    show wipeout7 at wipeout_transform
    pause 0.03
    show wipeout1 at wipeout_transform
    pause 0.03
    show wipeout6 at wipeout_transform
    pause 0.03
    show wipeout2 at wipeout_transform
    pause 0.11

    show expression "#000" as fade onlayer curtain

    hide wipeout1
    hide wipeout2
    hide wipeout3
    hide wipeout4
    hide wipeout5
    hide wipeout6
    hide wipeout7

    return


label wipein_routine:
    show wipein1:
        xanchor 1.0
        xpos 2420
    show wipein2:
        xanchor 1.0
        xpos 2420
    show wipein3:
        xanchor 1.0
        xpos 2420
    show wipein4:
        xanchor 1.0
        xpos 2420
    show wipein5:
        xanchor 1.0
        xpos 2420
    show wipein6:
        xanchor 1.0
        xpos 2420
    show wipein7:
        xanchor 1.0
        xpos 2420

    hide fade onlayer curtain
    show wipein4 at wipein_transform
    pause 0.03
    show wipein3 at wipein_transform
    pause 0.03
    show wipein5 at wipein_transform
    pause 0.03
    show wipein7 at wipein_transform
    pause 0.03
    show wipein1 at wipein_transform
    pause 0.03
    show wipein6 at wipein_transform
    pause 0.03
    show wipein2 at wipein_transform
    pause 0.1


    hide wipein1
    hide wipein2
    hide wipein3
    hide wipein4
    hide wipein5
    hide wipein6
    hide wipein7

    return

image chend_cover = Solid(Color('#000'), xalign=0.5, yalign=0.5, xzoom=2.0, yzoom=2.0)
label chapter_end:
    window hide None 
    $ timeout = 2.0
    $ timepause = 1.0
    $ timein = 1.0
    show chend_cover:
        align (0.5, 0.5)
        zoom 2.0
        alpha 0.0
        linear timeout alpha 1.0
    show expression "gui/higulogo_mei.png" as logo onlayer curtain:
        alpha 0.0
        zoom 0.4
        align (1.0, 1.0)
        offset (0, 70)
        linear timeout alpha 1.0

    $ renpy.pause(timeout, hard=True)
    scene
    stop music fadeout 1.0
    $ renpy.pause(timepause, hard=True)
    show expression "gui/higulogo_mei.png" as logo onlayer curtain:
        linear timein alpha 0.0
    $ renpy.pause(timein)
    hide chend_cover
