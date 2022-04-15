label chara062008_03:
 show black_background onlayer black
 $ event_store.current_event='chara062008'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara062008_03'
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
 show expression 'images/card/Card_062008.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_5031_write_paper.wav'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '~♪ *humming*, this is this... and next is this...'
 Character('Homeroom Teacher ',ctc="ctcArrow", ctc_position="fixed") '...Houjou-san. Are you listening, Houjou-san?'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ah... y-yes, of course.\nHow I'm going to spend my time during summer break... right?"
 Character('Homeroom Teacher ',ctc="ctcArrow", ctc_position="fixed") 'Yes, exactly. It is an extended break, so please do not let yourself go too much and do please spend your time responsibly.'
 Character('Homeroom Teacher ',ctc="ctcArrow", ctc_position="fixed") 'Now, that ends homeroom.\nWill the student on duty please do the class call?'
 play audio 'audio/sfx/SE_537_move_desk.wav'
 Character('Day Duty',ctc="ctcArrow", ctc_position="fixed") '...Stand, bow.\nThank you so much for today.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_261.png' as bg
 stop music fadeout 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Homeroom Teacher ',ctc="ctcArrow", ctc_position="fixed") 'Ah, Houjou-san.\nI would like a word with you about the pop quiz from a few days ago, so might you come to the staff room with me after this?'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Y-Yes. Got it... I mean, I understand.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1751.png' as bg
 pause 1.0
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rika_v017 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v017 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah... Satoko!\nHow did, um... the conversation with the teacher go?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v017
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show satoko_v016 smile at mei_left
 show rika_v017 fuan at mei_right
 with Dissolve(0.5)
 show rika_v017 fuan at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ohohohoho!\nDon't make such a gloomy face!"
 show rika_v017 fuan at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's alright; there's nothing you have to worry about, Rika."
 show satoko_v016 smile at inactive
 show rika_v017 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Th-then...!'
 show rika_v017 smile at inactive
 show satoko_v016 smile at active
 show satoko_v016 smile at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Yes. My grades have gone up, so I've received a rare compliment."
 show rika_v017 smile at inactive
 show satoko_v016 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Well, she did end it with, "Now, let\'s hope this persists", though.'
 show satoko_v016 fuan at inactive
 show rika_v017 smile_close at active
 show rika_v017 smile_close at deepbreath_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Wow... I'm happy for you, really, I am..."
 show rika_v017 smile_close at inactive
 show satoko_v016 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Thank you, Rika. I can set goals and study with ease now that I've learned good habits and strategies from you"
 show rika_v017 smile_close at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Fully memorizing the answer and the steps to the solution, working hard on the problem by repeating it over and over... I originally thought applying this method would be unbearable.'
 show rika_v017 smile_close at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'But it blew me out of the water realizing the opposite. I came up with a solution that I had never thought of before, and it made me feel more capable than ever!'
 show satoko_v016 smile at inactive
 show rika_v017 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Really? ...You know, I guess I did always think about how you have a pretty good memory, so maybe this style will work in your favor more.'
 show rika_v017 odoroki at inactive
 show satoko_v016 smile_close at active
 show satoko_v016 smile_close at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yeah. Studies and games are both beaten in similar ways.\nAnd the feelings of exhilaration and accomplishment you get from them are basically the same too...'
 play audio 'audio/sfx/SE_054_gacha_Flash.wav'
 show rika_v017 odoroki at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'For me it was almost like the awakening Christopher Columbus received when he made that egg-like discovery~♪'
 show satoko_v016 smile at inactive
 show rika_v017 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "*giggle*giggle*... I'm so glad it led to a great result.\nLet's keep this attitude for our next test."
 show rika_v017 smile at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Oh, now even Rika's talking like that teacher...\nWell, I'm in an amazing mood today, so I'll let it slide this once~.\nOhohohoho!"
 show satoko_v016 smile at inactive
 show rika_v017 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '*chuckle*... Ah, by the way, returning to the topic of founding a club, I was actually informed of a good way to go about that.'
 show satoko_v016 smile at inactive
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's going to be impossible to have anything that feels like we're playing... but if we try to persuade them with something educational, we might be able to make them consider it."
 show satoko_v016 smile at inactive
 show rika_v017 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Like for example, Home Ec... but they already have a cooking club, so we'll have to think of something else."
 show rika_v017 normal_close at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "In that case, how about desserts... like a sweets research group?\nAnd it doesn't just have to be sweet stuff; we can figure out how to make healthy stuff too!"
 show satoko_v016 smile at inactive
 show rika_v017 smile at active
 show rika_v017 smile at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Yeah... I like that a lot!\nLet's get that idea down on a written application and try sending this request to a teacher then."
 show rika_v017 smile at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Okay! If it'll make studying more entertaining, I'll welcome it warmly~!"
 hide rika_v017
 hide satoko_v016
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop music fadeout 0.5
 narrator '............'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(Those three that came from Tokyo...\nIf I'm being honest, I had completely forgotten about them until Satoko had brought them back up.)"
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(They left a huge impression on Satoko, which laid the groundwork for a turning point later on in her life. So we ended up indebted to them...)'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(How could I have ended up "forgetting" about those three...?)'
 play audio 'audio/sfx/SE_530_walk_one.wav'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(Concealing these thoughts within the depths of my heart, I walked together with Satoko back to her dorm...)'
 call chapter_end
 
 $ persistent.chara062008_done = True
 return