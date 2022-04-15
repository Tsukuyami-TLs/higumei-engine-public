## Event Story Select screen ############################################################

screen events():
    tag menu

    add "images/menu/EventStoryBg.png" at center

    textbutton "Back" style "button_back" action ShowMenu("story_select")
        

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10

        textbutton "The Witch's Bloodstained Birthday Banquet" style "button_story" action Start("event_umi1")
        textbutton "1983, The Bewilderment of Ange Ushiromiya" style "button_story" action Start("event_umi2")
        textbutton "The Fifth Year of Innocence" style "button_story" action Start("event_christmas")
        textbutton "Super Dimension Academy Z" style "button_story" action Start("event_space")