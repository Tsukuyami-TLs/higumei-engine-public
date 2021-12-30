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

transform sepia_shader:
    matrixcolor SepiaMatrix()

transform inverse_shader:
    matrixcolor InvertMatrix(1.0)

transform reset_shader:
    matrixcolor IdentityMatrix()

transform inactive:
    matrixcolor Matrix([
        0.5, 0, 0, 0,
        0, 0.5, 0, 0,
        0, 0, 0.5, 0,
        0, 0, 0, 1
    ])

transform active:
    matrixcolor IdentityMatrix(0.0)

image crack_effect = Movie(play="video/crack_video.mp4", mask="video/crack_mask.mp4", loop=False)

init python:
    config.layers = ['black', 'master', 'curtain', 'transient', 'screens', 'overlay']

image black_background = Solid(Color('#000'), xalign=0.5, yalign=0.5, xzoom=2.0, yzoom=2.0)
image black_cover = Solid(Color('#000'), xalign=0.5, yalign=0.5, xzoom=2.0, yzoom=2.0)
image white_cover = Solid(Color('#fff'), xalign=0.5, yalign=0.5, xzoom=2.0, yzoom=2.0)
image red_cover = Solid(Color('#e11'), xalign=0.5, yalign=0.5, xzoom=2.0, yzoom=2.0)
