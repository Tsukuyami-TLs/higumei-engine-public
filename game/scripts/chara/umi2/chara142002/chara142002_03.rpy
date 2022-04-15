label chara142002_03:
 show black_background onlayer black
 $ event_store.current_event='chara142002'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara142002_03'
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
 show expression 'images/bg/AdvBg_141.png' as bg
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show akasaka_v001 normal at mei_left
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '...We intended for this to be brief, but this ended up dragging on awfully long, huh? Are you tired, Rika-chan?'
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. I'm okay. It's just..."
 show akasaka_v001 normal at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...after learning about so many new things at once, I'm going to need some time to wrap my head around all of it."
 show rika_v002 fuan at inactive
 show akasaka_v001 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "I feel like it's seriously inexcusable of me to be sharing such highly classified information with a young child. But..."
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Rika-chan, you are an intelligent girl. Moreover, I can deeply understand why you have the earnest wish to save all of the people in this village.'
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "So, that is frankly the reason why I shared all this to you. ...But I'm also aware of the fact that this may make you suffer as well."
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...It's okay, Akasaka. I myself thought it was a good idea to speak to you. I wanted you to tell me everything just the same."
 show akasaka_v001 normal at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Actually, the fact that you treated me as your equal and brought the issue up earnestly makes me really happy! Nipah♪'
 show rika_v002 smile at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Thank you, Rika-chan. You saying that makes me glad too.'
 show rika_v002 smile at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "But alright, it's about time for me to leave. If any new developments come up, let me know... Seeya."
 show akasaka_v001 normal at inactive
 show rika_v002 odoroki at active
 show rika_v002 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'A-... Akasaka!'
 show rika_v002 odoroki at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mm...? What's up, Rika-chan? Is there something else you want to ask me?"
 stop music fadeout 0.5
 show akasaka_v001 normal at inactive
 show rika_v002 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...I understand that this upcoming question will be incredibly difficult for you to answer.'
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show akasaka_v001 normal at inactive
 show rika_v002 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But please hear me out. ...It's about the girl you met in this village, Miyuki."
 show rika_v002 sinken at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "...What's the matter with Miyuki-san?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide akasaka_v001
 hide fade onlayer curtain
 show rika_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v002 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Have you actually not realized yet? ...The fact that she might be your daughter?'
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Your daughter\'s name is "Miyuki"... and that girl\'s last name is "Akasaka". Something like that being a coincidence is unthinkable.'
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "And plus, the face Miyuki made as she stared at you...\nKnowing you with your advanced skill in observation, I wouldn't think it strange if you had already felt it by now."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show akasaka_v001 normal_close at mei_left
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show akasaka_v001 normal_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '............'
 show akasaka_v001 normal_close at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Why won't you ask her? Will you keep pretending like you don't know, continuing to treat her like she's someone else?"
 show akasaka_v001 normal_close at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I completely understand how important your family was to you in that situation 5 years ago. But then... why this?'
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "...It might be because... she's kept silent... all this time."
 show akasaka_v001 normal at inactive
 show rika_v002 odoroki at active
 show rika_v002 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide rika_v002
 hide akasaka_v001
 with Dissolve(0.2)
 show akasaka_v001 normal at mei_center
 with Dissolve(0.5)
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Of course I knew just as much. Whenever Miyuki-san looks at me, she always seems so delighted... but simultaneously looks like she's going to cry."
 show akasaka_v001 smile_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '...As someone who knows I can be laughed at for being a helicopter dad, of course I can say I remember my own daughter.'
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Even when that girl gets lonely and feels like crying, she puts up with it by thinking of us and putting on a smile. She's so tender and loving..."
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "And wow... doesn't she look just like her? If that really is my girl 10 years down the line, that would make me so proud... and just so happy."
 hide akasaka_v001
 with Dissolve(0.2)
 show rika_v002 sinken at mei_right
 show akasaka_v001 smile at mei_left
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show rika_v002 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'So, so then...!'
 show rika_v002 sinken at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "That spoiled girl is desperately holding in the truth. I'm sure she has reasons that prevent her from saying anything."
 show rika_v002 sinken at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "So, in that case, I have to hold back for her too. If I don't, I wouldn't be qualified to be her parent... right?"
 show akasaka_v001 normal at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Akasaka...'
 show rika_v002 fuan at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Rika-chan. What we talked about now stays between us. And of course, that goes for Miyuki-san, no, "Miyuki" as well.'
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "When the time comes, she'll definitely speak. No, even in the scenario that it doesn't happen, I would definitely take measures to reach out to her."
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "That is... the least I could do for my daughter who's always trying her best."
 stop music fadeout 1.0
 show akasaka_v001 normal at inactive
 show rika_v002 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide akasaka_v001
 hide rika_v002
 with Dissolve(0.2)
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show satoko_v002 smile at mei_center
 with Dissolve(0.5)
 show satoko_v002 smile at active
 show satoko_v002 smile at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ah, there she iiis! So you were over {i}here{/i}, Rika... and... Akasaka-san?'
 hide satoko_v002
 with Dissolve(0.2)
 show akasaka_v001 smile at mei_left
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Hey, Satoko-chan. Were you looking for Rika-chan?'
 show akasaka_v001 smile at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yes... The truth is, I received news about "them" appearing again in the mountains behind the lodging facility.'
 show satoko_v002 normal at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "That's some serious news. If you'd like, I wouldn't mind helping out like I did before... but what do you think?"
 show akasaka_v001 sinken at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Eh? Well, of course, taking in another person would be a massive help for us... but would that be okay, Rika?'
 hide satoko_v002
 hide akasaka_v001
 with Dissolve(0.2)
 show rika_v002 normal at mei_center
 with Dissolve(0.5)
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Of course it would. Akasaka wants to know a lot more about them just like we do.'
 hide rika_v002
 with Dissolve(0.2)
 show akasaka_v001 smile at mei_center
 with Dissolve(0.5)
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Thank you, Rika-chan. Let's head to the scene right away then."
 stop music fadeout 1.0
 hide akasaka_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_408_run.wav'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1501.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 play music "<loop 0>audio/bgm/BGM_BATTLE1_hiru.ogg"
 show keiichi_v002 futeki at mei_center
 with Dissolve(0.5)
 show keiichi_v002 futeki at active
 show keiichi_v002 futeki at jumping_transform
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Ooooh, they're over here! Battler-san and Jessica-san, I'm leaving the rest up to you!"
 hide keiichi_v002
 with Dissolve(0.2)
 show battler_v001 futeki at mei_left
 show jessica_v001 normal at mei_right
 with Dissolve(0.5)
 show jessica_v001 normal at inactive
 show battler_v001 futeki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Yup, leave it to us! Jessica, you ready?'
 show battler_v001 futeki at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I... um, well, I was the one who was asking to see monsters get destroyed, but...'
 show battler_v001 futeki at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Don't tell me you were thinking of counting me in on your fight?! ...Haah, I don't feel like I'd be good enough..."
 hide battler_v001
 with Dissolve(0.2)
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "It's all good, Jessica-san! Us women have the brawn and men have the brains!"
 show jessica_v001 fuan at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Ah, or was it the other way around? Oh well!'
 hide jessica_v001
 hide miyuki_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_left
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Mi-Miyuki-chan, you're pretty enthusiastic..."
 show kazuho_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Well, the reason for that is clearer than anything else here.'
 hide nao_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show akasaka_v003 normal at mei_left
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show akasaka_v003 normal at inactive
 show miyuki_v002 smile at active
 show miyuki_v002 smile at jump_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Akasaka-san, this is the final push! The rest is up to you!'
 show miyuki_v002 smile at inactive
 show akasaka_v003 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Alright... not sure how this'll go, but let me at em!"
 hide miyuki_v002
 hide akasaka_v003
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/card/Card_142002.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_016_SpecialStart.wav'
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Take this, you monster freaks!!! Uoooooooohhhh!!!!'
 play audio 'audio/sfx/SE_310_ls_stageexplosion.wav'
 camera at screenshake_transform
 pause 0.0
 pause 0.5
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Wo-... woaaah?! I-I don't know how, but he just blew out a bunch of those guys with one clean sweep...!"
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yeah, jeez...! But still, attack as crazy as it was, Akasaka-san's outfit has a powerful, kind of flashy look to it, huh?"
 stop music fadeout 1.0
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1501.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show battler_v001 fuan at mei_right
 show akasaka_v003 normal at mei_left
 with Dissolve(0.5)
 show akasaka_v003 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Isn't that my suit underneath? Just by putting that cloak on, it makes it all flashy looking... But why are you in that outfit all of a sudden?"
 show battler_v001 fuan at inactive
 show akasaka_v003 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Well... you're asking me. Might have turned out like this because I used this {b}Role Card{/b} I was given."
 hide akasaka_v003
 hide battler_v001
 with Dissolve(0.2)
 show miyuki_v002 sinken at mei_center
 with Dissolve(0.5)
 show miyuki_v002 sinken at active
 show miyuki_v002 sinken at jumping_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "I like it! It's so cool and you look so reliable! And if you have anything bad to say about it, I'll fight you on it!"
 hide miyuki_v002
 with Dissolve(0.2)
 show battler_v001 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Nah, I don't really have anything bad to say. It definitely does suit him well."
 hide battler_v001
 with Dissolve(0.2)
 show nao_v002 fuan_close at mei_left
 show miyuki_v002 sinken at mei_right
 with Dissolve(0.5)
 show miyuki_v002 sinken at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "If someone picks a fight with Akasaka-san, you seriously degenerate into a super fan... You're one step away from being certified as a hooligan."
 show nao_v002 fuan_close at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Lalalalala, I can't hear you, lalalala. By the way, Akasaka-san, let's finish up over there next!"
 hide nao_v002
 with Dissolve(0.2)
 show akasaka_v003 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show akasaka_v003 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Alright, lead the way, Miyuki-san.'
 show akasaka_v003 smile at inactive
 show miyuki_v002 smile at active
 show miyuki_v002 smile at updown_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Yessir! Leave it to me! Here we goooo!! Oriiiiiyaaaahhhhh!!!'
 play audio 'audio/sfx/SE_304_ls_run.wav'
 hide miyuki_v002
 with Dissolve(0.6)
 pause 0.5
 hide akasaka_v003
 with Dissolve(0.2)
 show satoko_v002 smile at mei_left
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show satoko_v002 smile at active
 show satoko_v002 smile at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ohohohoho!! Not bad at all! We can't let them show us up, Rika!"
 show satoko_v002 smile at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v002 normal at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Rika? Whatever could be wrong?'
 show satoko_v002 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. It's nothing. All day today, let's fight oooon!"
 hide rika_v002
 hide satoko_v002
 with Dissolve(0.2)
 narrator '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rika_v002 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v002 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(They continue living in that lie, but they can be happy solely through thinking of each other... huh?)'
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(Seriously... what a close parent-child relationship those two have.)'
 call chapter_end
 
 $ persistent.chara142002_done = True
 return