## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

init -2 python:

    class Start(Action, DictEquality):
        """
         :doc: menu_action

         Causes Ren'Py to jump out of the menu context to the named
         label. The main use of this is to start a new game from the
         main menu. Common uses are:

         * Start() - Start at the start label.
         * Start("foo") - Start at the "foo" label.
         """

        def __init__(self, label="start"):
            self.label = label

        def __call__(self):
            renpy.transition(Dissolve(0.3))
            renpy.jump_out_of_context(self.label)

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background at truecenter

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    image "gui/higulogo_mei.png":
        xzoom 0.6
        yzoom 0.6
        xalign 0.9
        yalign -0.3

    if gui.show_name:

        vbox:
            
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")




## Story Select screen ############################################################

screen story_select():

    tag menu

    add "images/menu/PhotoStoryTop.png":
        xpos 67
        ypos 24
        xzoom 0.466
        yzoom 0.466
        rotate 10

    add "images/menu/BgStoryTop.png" at center

    textbutton "Title Screen" style "button_back" action ShowMenu("main_menu")
        

    vbox:
        xalign 0.9
        yalign 0.5
        spacing 18

        imagebutton idle "gui/button/BtnMainStory.png" at grayscale action NullAction()

        hbox:
            spacing 18

            imagebutton idle "gui/button/BtnCharaStory.png":
                activate_sound "audio/sfx/SE_002_Decision.wav"
                action ShowMenu("characters")


            imagebutton idle "gui/button/BtnTips.png" at grayscale action NullAction()

            imagebutton idle "gui/button/BtnEventStory.png":
                activate_sound "audio/sfx/SE_002_Decision.wav"
                action ShowMenu("events")


## Character Story Select screen ############################################################

screen characters():

    tag menu

    add "images/menu/CharaStoryBg.png" at center

    textbutton "Back" style "button_back" action ShowMenu("story_select")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10

        textbutton "\"Chiester Sister Corps\" Nao Houtani" style "button_story" action Start('chara032009')
        textbutton "\"The Golden Witch\" Beatrice" style "button_story" action Start('chara452001')
        textbutton "\"Witch of Truth\" Erika Furudo" style "button_story" action Start('chara462001')
        textbutton "\"Inquisitor of Heresy\" Dlanor" style "button_story" action Start('chara472001')


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

