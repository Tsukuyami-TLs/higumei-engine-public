define config.gl2 = True
define config.default_transform = truecenter

# Declare music files.

define event7 = "audio/bgm/BGM_EVENT7.wav"

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

# Position definitions

transform mei_center:
    xanchor 0.5
    xpos 960

    yanchor 1.0
    ypos 1200

transform mei_left:
    xanchor 0.5
    xpos 480

    yanchor 1.0
    ypos 1200

transform mei_right:
    xanchor 0.5
    xpos 1440

    yanchor 1.0
    ypos 1200

# Color transforms

transform grayscale:
    matrixcolor SaturationMatrix(0.0)

transform sepia:
    matrixcolor SepiaMatrix()

transform inverse:
    matrixcolor InvertMatrix(1.0)

transform inactive:
    matrixcolor SaturationMatrix(0.65) * BrightnessMatrix(-0.2) 

transform active:
    matrixcolor BrightnessMatrix(0.0)

