define config.gl2 = True

define config.default_transform = truecenter

# Custom sprite positions

transform mei_center:
    xanchor 0.5
    xpos 0.5

    yalign 1.0
    yoffset 120

transform mei_left:
    xanchor 0.5
    xpos 0.25

    yalign 1.0
    yoffset 120

transform mei_right:
    xanchor 0.5
    xpos 0.74

    yalign 1.0
    yoffset 120

# Declare music files.

define event7 = "audio/bgm/BGM_EVENT7.wav"

# Declare backgrounds

# Color transforms

transform grayscale:
    matrixcolor SaturationMatrix(0.0)

transform sepia:
    matrixcolor SepiaMatrix()

transform inverse:
    matrixcolor InvertMatrix(1.0)

transform inactive:
    matrixcolor BrightnessMatrix(-0.5)

transform active:
    matrixcolor BrightnessMatrix(0.0)

# Click to continue

image Arrow1 = "gui/adv_Arrow1.png"
image Arrow2 = "gui/adv_Arrow2.png"

image ctcArrow:
    contains:
        xpos 1630 ypos 992 xanchor 0.5
        "Arrow1"
        parallel:
            0.1
            ease 0.1 xzoom 0.0
            ease 0.1 xzoom 1.0
        parallel:
            ease 0.4 yoffset 20
        0.1
        ease 0.4 yoffset 0
        repeat
    contains:
        xpos 1630 ypos 984 xanchor 0.5
        "Arrow2"
        parallel:
            ease 0.1 xzoom 0.0
            ease 0.1 xzoom 1.0
        parallel:
            0.1
            ease 0.4 yoffset 20
        ease 0.4 yoffset 0
        repeat

# Declare characters

define narrator = Character(None, ctc="ctcArrow", ctc_position="fixed")


# The game starts here.

label start:

    #jump main_prologue

    return
