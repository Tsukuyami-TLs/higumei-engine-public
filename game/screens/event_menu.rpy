init python in event_store:
    current_event = ""
    current_chapter = ""
    current_progress = 0
    notes = {}
    chapters = {}
    


screen tl_notes(title="", contents=""):
    tag menu
    use game_menu(_("TL Notes")):
        style_prefix "about"
        has hbox

        
        viewport:
            area (0,0,500,1.0)

            draggable True
            mousewheel True
            scrollbars "vertical"

            has vbox
            
            for ntitle, ncontents in event_store.notes[event_store.current_event][:event_store.current_progress]:
                textbutton _(ntitle):
                    activate_sound "audio/sfx/SE_004_Tap.wav"
                    action ShowMenu("tl_notes", ntitle, ncontents)
                    selected title == ntitle

        null width 50
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            
            has vbox
            label title
            text contents
 
screen chapter_jump():
    tag menu
    use game_menu(_("Chapter Jump")):
        style_prefix "about"
        has hbox

        vbox:
            for title, label in event_store.chapters[event_store.current_event]:
                textbutton _(title):
                    activate_sound "audio/sfx/SE_002_Decision.wav"
                    action Start(label)
                    selected label == event_store.current_chapter

