init python:
    def red_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "color=#f00")] + contents + [(renpy.TEXT_TAG, "/color")]
    def blue_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "color=#4169e1")] + contents + [(renpy.TEXT_TAG, "/color")]
    def green_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "color=#00e00e")] + contents + [(renpy.TEXT_TAG, "/color")]

    config.custom_text_tags["umi_red"] = red_tag
    config.custom_text_tags["umi_blue"] = blue_tag
    config.custom_text_tags["note_green"] = green_tag
