label chara062016_01:
 show black_background onlayer black
 $ event_store.current_event='chara062016'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara062016_01'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_1751.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v015 fuan_close at mei_center
 with Dissolve(0.5)
 show satoko_v015 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '*sigh*... I somehow just {i}barely{/i} managed to escape from getting a failing grade on that proficiency test...'
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "But I mustn't be too careless. There's been a rumor going around lately that the head teacher is becoming terribly desperate in getting the school's average gradepoint to rise."
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "To get into the safety zone, it seems I'll need to tack about 5 points... no, 10 points more onto my average."
 show satoko_v015 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I've somehow been able to brute force my way this far thanks to me sticking to Rika and having her watch over me while I study... but to be honest, I've become quite exhausted."
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's almost like a marathon with no goal.\nHow long am I supposed to keep doing my best?"
 show satoko_v015 sinken_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'No... is there even any meaning in doing my best to begin with?'
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If I'll just be imposing a burden on Rika by continuing to try hard... then I'll..."
 hide satoko_v015
 with Dissolve(0.2)
 window hide None
 play audio 'audio/sfx/SE_410_runonglass.wav'
 pause 2.0
 show satoko_v015 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v015 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Oh my?'
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Had I just seen someone going into the woods...?'
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I've heard that there's nothing in there but a dead end, though..."
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Now I'm interested... \nCould it be an intruder has gotten into the academy?"
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Other people here aside, I simply cannot overlook anything looming by that may cause any harm to Rika. ...Alright.'
 hide satoko_v015
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_741.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v015 sinken at mei_center
 with Dissolve(0.5)
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...?\nThis should be the spot I saw them go in, but I don't see anyone..."
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Could what I have seen perhaps been a ghost...? Of course it wasn't. Maybe I was just tired and saw an illusion... Wha-?"
 show satoko_v015 odoroki at active
 show satoko_v015 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "This rope that was recently set up here... is it a trap?\nAnd what's hooked up onto the tip of it is..."
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I see. There are noisemakers set up here and there to alert when there's an intruder afoot."
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "And this ground that's swelled up a bit is... yep, it's a pitfall. It's not very deep, but its purpose is to frighten, I'm sure."
 show satoko_v015 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'But the existence of this trap alone is clear evidence of something... *chuckle*, how exhilarating this is getting.'
 hide satoko_v015
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v015 normal at mei_center
 with Dissolve(0.5)
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Oh my? There's this open patch of dirt...?\nAnd in the center of it, there's a lawnchair set out that--"
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 play audio 'audio/sfx/SE_201_shutter.wav'
 show satoko_v015 odoroki at active
 show satoko_v015 odoroki at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Fwwaaaahhhhh?!\nA light?! Something's shined over here?!"
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Hmm... and who would you be?'
 show satoko_v015 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v015 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'A voice from overhead...?! Wh-who could I have heard... well, more importantly, what was that light just now?'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Just as you saw, it was a camera flash.\nI do apologize, but I photographed you.'
 show satoko_v015 sinken at mei_center
 with Dissolve(0.5)
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Wha-? Taking a picture suddenly without someone's permission is up on the peak of rudeness, you know?!"
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Yes, exactly. ...However, I had to make sure to have you silenced before you shared this with anyone. I do beg for your understanding.'
 show satoko_v015 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'S-Silenced...?!'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Quite. Had you spoken of what you witnessed just now, I would present this photo to the teachers at the registrar's office."
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Thereupon, oh dear, how strange; the person who had been secretly eating snacks and reading manga here won't actually be me, but you."
 show satoko_v015 odoroki at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show satoko_v015 odoroki at active
 show satoko_v015 odoroki at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huuuuh?!'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'And so, all appeals for innocence will go unheard, and the culprit that the teachers will punish since they were fixed upon their original preconceptions will, for some reason, be you.'
 Character('????',ctc="ctcArrow", ctc_position="fixed") "And through this accusation, it would become possible for me to succeed in my escape. ...So, isn't that a nice plan?"
 show satoko_v015 sinken at mei_center
 with Dissolve(0.5)
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '......What an intricate and threatening mode of speech.\nWhat could you possibly want from me?'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Nothing. As long as you keep quiet about this place for the next year and a half or so, you will undergo no harm.'
 Character('????',ctc="ctcArrow", ctc_position="fixed") "I can swear on something if you like. Would you mind if I did it to the god in this academy's chapel?"
 show satoko_v015 normal at mei_center
 with Dissolve(0.5)
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Even if you swore to this academy's god, I can't fully trust you... but understood. I also wish to avoid being sent off to the reflection room."
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "How thoughtful of you to comply. I also don't wish to disturb the lives of my fellow students at the academy, so you spared me that pain."
 show satoko_v015 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "You're hysterical... Yyeoowch!!"
 play audio 'audio/sfx/SE_347_ls_fall.wav'
 camera at screenshake_transform
 pause 0.0
 show satoko_v015 odoroki
 pause 2.0
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Uuu, something fell from up there... wait, what is this?'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'A token of your complicity, and a portion of the profit.\nHow do you feel about a newly released chocolate candy as of this month?'
 show satoko_v015 normal at mei_center
 with Dissolve(0.5)
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I'll take it. \nBut still, aren't you up in that tree right now?"
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Yes, that's correct."
 show satoko_v015 normal at mei_center
 with Dissolve(0.5)
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Are you going to come down?'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "I'm comfortable up here."
 show satoko_v015 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ah, okay...\n(...What a strange person.)'
 call chapter_end
 jump chara062016_02