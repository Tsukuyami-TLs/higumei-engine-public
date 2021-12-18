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
