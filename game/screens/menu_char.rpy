## Character Story Select screen ############################################################

screen characters():
    tag menu
    add "images/menu/CharaStoryBg.png" at center
    textbutton "Back" style "button_back" action ShowMenu("story_select")
    textbutton "Sort by Character" style "button_sort" action ShowMenu("characters_event")


    vpgrid:
        cols 1
        xalign 0.5
        yalign 0.5
        spacing 10
        ymaximum 800

        draggable True
        mousewheel True
        if renpy.variant("android"):
            scrollbars "vertical"
            
        $ lines = ["Nao", "Keiichi", "Satoko", "Rika", "Akasaka", "Others"]
        for i in lines:
            textbutton i style "button_story" action ShowMenu("stories", i, "char")
            
screen characters_event():
    tag menu
    add "images/menu/CharaStoryBg.png" at center
    textbutton "Back" style "button_back" action ShowMenu("story_select")
    textbutton "Sort by Event" style "button_sort" action ShowMenu("characters")

    vpgrid:
        cols 1
        xalign 0.5
        yalign 0.5
        spacing 10
        ymaximum 800


        draggable True
        mousewheel True
        if renpy.variant("android"):
            scrollbars "vertical"

        python:
            lines = [["The Witch's Bloodstained Birthday Banquet", "witch", "umi1_done"],
                     ["1983, The Bewilderment of Ange Ushiromiya", "ange", "umi2_done"],
                     ["The Fifth Year of Innocence", "christmas", "christmas_done"],
                     ["Super Dimension Academy Z", "space", "space_done"],
                     ["Eventless", "no_event", ""]]
        
        for i in lines:
                if getattr(persistent,i[2],False) or i[2] == "":
                    textbutton i[0] style "button_story" action ShowMenu("stories", i[1], "event")
                else:
                    textbutton i[0] style "button_story_locked" at grayscale action ShowMenu("locked_screen", i[1], i[2])
            

screen stories(key, type):
    tag menu
    add "images/menu/CharaStoryBg.png" at center

    if type == "event":
        textbutton "Back" style "button_back" action ShowMenu("characters_event")
    if type == "char":
        textbutton "Back" style "button_back" action ShowMenu("characters")

    vpgrid:
        cols 1
        xalign 0.5
        yalign 0.5
        spacing 10
        ymaximum 800

        draggable True
        mousewheel True
        if renpy.variant("android"):
            scrollbars "vertical"
            
        
        if(key == "witch"):
            textbutton "\"Chiester Sister Corps\" Nao Houtani" style "button_story" action Start('event_chara032009')
            textbutton "\"The Golden Witch\" Beatrice" style "button_story" action Start('event_chara452001')
            textbutton "\"Witch of Truth\" Erika Furudo" style "button_story" action Start('event_chara462001')
            textbutton "\"Inquisitor of Heresy\" Dlanor" style "button_story" action Start('event_chara472001')

        if(key == "ange"):
            textbutton "\"Chiester Sister Corps\" Furude Rika" style "button_story" action Start('event_chara072016')
            textbutton "\"Game Master\" Mamoru Akasaka" style "button_story" action Start('event_chara142002')
            textbutton "\"Endless Sorcerer\" Battler Ushiromiya" style "button_story" action Start('event_chara482001')
            textbutton "\"Witch of Resurrection\" Ange Ushiromiya" style "button_story" action Start('event_chara492001')

        if(key == "christmas"):
            textbutton "\"Lucia Christmas Eve\" Satoko Houjou" style "button_story" action Start('event_chara062016')
            textbutton "\"Lucia Christmas Eve\" Rika Furude" style "button_story" action Start('event_chara072017')

        if(key == "space"):
            textbutton "\"Borg Decker\" Keiichi" style "button_story" action Start('event_chara042003')
            textbutton "\"Galactic Patrol\" Rika" style "button_story" action Start('event_chara072005')

        if(key == "no_event"):
            textbutton "\"High School Student\" Satoko Houjou" style "button_story" action Start('event_chara062008')
            textbutton "\"High School Student\" Rika Furude" style "button_story" action Start('event_chara072008')
            textbutton "\"Theatregoer of the Torus\" Eua" style "button_story" action Start('event_chara442001')
            textbutton "\"Dark Hero\" Keiichi Maebara" style "button_story" action Start('event_chara042001')




        if(key == "Nao"):
            python:
                lines = [["\"Chiester Sister Corps\" Nao Houtani", "event_chara032009", "umi1_done"]]               
            for i in lines:
                if getattr(persistent,i[2],False) or i[2] == "":
                    textbutton i[0] style "button_story" action Start(i[1])
                else:
                    textbutton i[0] style "button_story_locked" at grayscale action ShowMenu("locked_screen", i[1], i[2])
                    
        if(key == "Keiichi"):
            python:
                lines = [["\"Borg Decker\" Keiichi Maebara", "event_chara042003", "space_done"],\
                        ["\"Dark Hero\" Keiichi Maebara", "event_chara042001", ""]]                       
            for i in lines:
                if getattr(persistent,i[2],False) or i[2] == "":
                    textbutton i[0] style "button_story" action Start(i[1])
                else:
                    textbutton i[0] style "button_story_locked" at grayscale action ShowMenu("locked_screen", i[1], i[2])
                    
        if(key == "Satoko"):
            python:
                lines = [["\"High School Student\" Satoko Houjou", "event_chara062008", ""],\
                        ["\"Lucia Christmas Eve\" Satoko Houjou", "event_chara062016", "christmas_done"]]                       
            for i in lines:
                if getattr(persistent,i[2],False) or i[2] == "":
                    textbutton i[0] style "button_story" action Start(i[1])
                else:
                    textbutton i[0] style "button_story_locked" at grayscale action ShowMenu("locked_screen", i[1], i[2])
                    
        if(key == "Rika"):
            python:
                lines = [["\"High School Student\" Rika Furude", "event_chara072008", ""],\
                        ["\"Lucia Christmas Eve\" Rika Furude", "event_chara072017", "christmas_done"],\
                        ["\"Chiester Sister Corps\" Rika Furude", "event_chara072016", "umi2_done"],\
                        ["\"Galactic Patrol\" Rika Furude", "event_chara072005", "space_done"]]                       
            for i in lines:
                if getattr(persistent,i[2],False) or i[2] == "":
                    textbutton i[0] style "button_story" action Start(i[1])
                else:
                    textbutton i[0] style "button_story_locked" at grayscale action ShowMenu("locked_screen", i[1], i[2])

        if(key == "Akasaka"):
            python:
                lines = [["\"Game Master\" Mamoru Akasaka", "event_chara142002", "umi2_done"]]               
            for i in lines:
                if getattr(persistent,i[2],False) or i[2] == "":
                    textbutton i[0] style "button_story" action Start(i[1])
                else:
                    textbutton i[0] style "button_story_locked" at grayscale action ShowMenu("locked_screen", i[1], i[2])

        if(key == "Others"):
            python:
                lines = [["\"The Golden Witch\" Beatrice", "event_chara452001", "umi1_done"],\
                        ["\"Witch of Truth\" Erika Furudo", "event_chara462001", "umi1_done"],\
                        ["\"Inquisitor of Heresy\" Dlanor", "event_chara472001", "umi1_done"],\
                        ["\"Endless Sorcerer\" Battler Ushiromiya", "event_chara482001", "umi2_done"],\
                        ["\"Witch of Resurrection\" Ange Ushiromiya", "event_chara492001", "umi2_done"],\
                        ["\"Theatregoer of the Torus\" Eua", "event_chara442001", ""]]                       
            for i in lines:
                if getattr(persistent,i[2],False) or i[2] == "":
                    textbutton i[0] style "button_story" action Start(i[1])
                else:
                    textbutton i[0] style "button_story_locked" at grayscale action ShowMenu("locked_screen", i[1], i[2])

                    

screen locked_screen(name, unlock):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("To unlock these character stories, read the corresponding event story first."):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Force Unlock"):
                    action [SetField(persistent, unlock, True), Hide("locked_screen")]
                textbutton _("Confirm "):
                    activate_sound "audio/sfx/SE_003_Cancel.wav"
                    action Hide("locked_screen")

    ## Right-click and escape answer "no".
    key "game_menu" action Hide("locked_screen")

