## TIPS Select screen ############################################################

screen tips():

    tag menu

    add "images/menu/TipsStoryBg.png" at center

    textbutton "Back" style "button_back" action ShowMenu("story_select")
        

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10

        textbutton "TIPS" style "button_story" action NullAction()