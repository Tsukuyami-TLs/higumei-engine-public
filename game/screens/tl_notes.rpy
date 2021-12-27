init python in tlnote_store:
    current_event = ""
    current_progress = 0
    notes = {}
    


screen tl_notes(title="", contents=""):
    tag menu
    use game_menu(_("TL Notes")):
        style_prefix "about"
        has hbox

        vpgrid:
            area (0,0,500,1.0)
            cols 1
            spacing 5

            draggable True
            mousewheel True
            scrollbars "vertical"

            side_xalign 0.5
            
            for ntitle, ncontents in tlnote_store.notes[tlnote_store.current_event][:tlnote_store.current_progress]:
                textbutton _(ntitle):
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
 
