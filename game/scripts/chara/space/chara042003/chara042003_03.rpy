label chara042003_03:
 show black_background onlayer black
 $ event_store.current_event='chara042003'
 $ event_store.current_progress=1
 $ event_store.current_chapter='chara042003_03'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 show black_cover as bg
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(And then, the game began—)'
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(It ended very easily, though I suppose everyone put up a surprisingly good fight, for what it was... it was all settled just within a few minutes.)'
 stop sound
 show expression 'images/bg/AdvBg_021.png' as bg
 play music "<loop 0>audio/bgm/BGM_ARENA.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_310_ls_stageexplosion.wav'
 show keiichi_v002 odoroki at mei_center
 with Dissolve(0.5)
 show keiichi_v002 odoroki at active
 show keiichi_v002 odoroki at jumping_transform
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "..U-Uwaaaaaah? Th-there's a trap here toooooooo?!"
 play audio 'audio/sfx/SE_310_ls_stageexplosion.wav'
 hide keiichi_v002
 show shion_v002 fuan at mei_center
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show shion_v002 fuan at jumping_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hol-... hyaaaaaah? Land mines aren't meant to be thrown, Satoko!"
 hide shion_v002
 with Dissolve(0.2)
 show satoko_v002 futeki at mei_left
 with Dissolve(0.5)
 show satoko_v002 futeki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ohohohohoho! There's a special kind of enjoyment in taking your opponents out with a long-range attack before they can even reach you~!"
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 futeki at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. Poor, poor Keiichi's group was overwhelmed by the difference in firepower. Nipah♪"
 hide satoko_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Th-this can't even be called a battle anymore...\nThis is a one-sided massacre, a war crime...!"
 show hanyuu_v002 fuan at inactive
 show rika_v002 futeki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Dear me... then why don't you go join them if you think that way?\nI won't stop you."
 show rika_v002 futeki at inactive
 show hanyuu_v002 fuan at active
 show hanyuu_v002 fuan at chara_shake_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Eeek? P-Please don't hate me for this, Keiichi...!\nI don't want to become a victim either...!"
 hide rika_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Tch...! Now that it's come to this, we're going to have to set our sights on General Mion and... wha-...?"
 show kazuho_v002 sinken at jumping_transform
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 show miyuki_v002 futeki at mei_right
 show kazuho_v002 sinken
 show kazuho_v002 sinken at jumping_transform:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 with Dissolve(0.5)
 show kazuho_v002 sinken:
  yanchor 1.0
  pos (480,1200)
 show kazuho_v002 sinken at inactive
 show miyuki_v002 futeki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Hey there...! I'm not letting you through, Kazuho!"
 hide miyuki_v002
 show nao_v002 sinken at mei_right
 with Dissolve(0.5)
 show kazuho_v002 sinken at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I also predicted you would come here.\nTwo of us isn't enough to beat you, but we can stall you.\nNow, Rena―!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide nao_v002
 hide fade onlayer curtain
 show rena_v002 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show rena_v002 futeki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahahahahahaha! I got you, Kazuho-chan!!'
 hide rena_v002
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Th-this can't be... kyaaaah?!"
 play audio 'audio/sfx/SE_102_hit_strike2.wav'
 hide kazuho_v002
 with Dissolve(0.2)
 show satoko_v002 smile at mei_center
 with Dissolve(0.5)
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Well done, Rena-san! I finished Shion-san off here as well!!!'
 play audio 'audio/sfx/SE_303_ls_destruction.wav'
 hide satoko_v002
 show shion_v002 fuan at mei_center
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show shion_v002 fuan at jumping_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hrrggyaaaaaahh?!\nY-You'll pay for this... Saaatookoooooooo!!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 show shion_v002 fuan
 show shion_v002 fuan:
  yanchor 1.0
  linear 0.5 pos (960,1300)
 pause 0.5
 show shion_v002 fuan:
  yanchor 1.0
  pos (960,1300)
 camera:
  pos (960, 540)
  zoom 1.0
 hide shion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show satoko_v002 futeki at mei_left
 with Dissolve(0.5)
 show satoko_v002 futeki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ohohohoho! I can feel some of my pent-up stress getting alleviated already~!'
 show rika_v002 smile_close at mei_right
 with Dissolve(0.5)
 show satoko_v002 futeki at inactive
 show rika_v002 smile_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Meep. Poor, poor Satoko is most definitely itching to vent her stress some more, but it seems that her joy will be short lived. Nipah~☆'
 hide satoko_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 smile_close at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "You won't break it to her even though you're aware...\nY-You're a demon, you know, au au..."
 hide rika_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show mion_v002 futeki at mei_left
 with Dissolve(0.5)
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "You're the only one left!\nGet ready for this, Kei-chan! ...Oryaaaaaaaaaahhhh!!"
 show keiichi_v002 sinken at mei_right
 with Dissolve(0.5)
 show mion_v002 futeki at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Tch... it's no use. If neither swords nor guns work here, this third option will...!"
 show keiichi_v002 sinken at inactive
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Huh? Kei-chan, whaddya talkin' abou-... WHAA-?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide keiichi_v002
 hide fade onlayer curtain
 show keiichi_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") '{i}ARMORIZE!!{/i}'
 play audio 'audio/sfx/SE_308_ls_eyeflash.wav'
 stop sound
 show expression 'images/bg/white.png' as bg
 hide keiichi_v002
 with Dissolve(0.2)
 pause 1.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 camera:
  pos (960, 540)
  zoom 1.0
 stop sound
 show expression 'images/bg/AdvBg_021.png' as bg
 play music "<loop 3.53>audio/bgm/BGM_EVENT7.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show keiichi_v007 futeki at mei_center
 with Dissolve(0.5)
 show keiichi_v007 futeki at inactive
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I-Is that... the combat suit for the play that I made with everyone the other day?!'
 $ event_store.current_progress = 2
 show keiichi_v007 futeki at inactive
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'M-Meep. He transformed in 0.05 seconds, just like {note_green}on that TV show{/note_green}...!'
 show keiichi_v007 futeki at inactive
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Did you link it with a {b}Role Card{/b} in secret or something?\nBut what kind of weapon will... you... huuuh?!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide keiichi_v007
 with Dissolve(0.2)
 stop sound
 show expression 'images/card/Card_042003.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "It's my trump card that I saved for you guys until the very last moment!\nEat this, suckeeeeers!!"
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'A-A bazooka cannoooooon?\nKei-chan, what happened to your obsession with swords?!'
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "We... we don't know! Not once have we heard that we'd use a weapon like this hereeee!!"
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "P-Please wait a minute, Kei-chan!\nYou don't actually want to fire off a high-powered weapon in a place like this?! This is a joke, right?!"
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "*cackle*cackle*... it's been a while since I felt like this.\nGiving it your all and beating your opponents is what club activities are aaaaaall about, am I right?!?!"
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...Ah, it's over. I see where this is going.\nHe's gonna keep up with this no matter what we tell him."
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'TRANSFORM INTO LIIIIIIIIGHT!!!'
 play audio 'audio/sfx/SE_375_ls_satellitelaser.wav'
 camera at screenshake_transform
 pause 0.0
 Character('Everyone',ctc="ctcArrow", ctc_position="fixed") 'Gyaaaaaaaa?!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop music fadeout 0.5
 pause 1.0
 stop sound
 show expression 'images/bg/AdvBg_021.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show miyuki_v002 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...Maaan, he got us.\nCan't believe Maebara-kun obsessed over swords so much only to sneak a bazooka cannon in as his trump card."
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I was completely taken by surprise.\nIt took everything we could muster just to avoid a direct hit.'
 hide miyuki_v002
 show rena_v002 smile_blush at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show rena_v002 smile_blush at active
 show rena_v002 smile_blush at leftright_shake_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau~, Keiichi-kun really is cool when he gets serious~.\nPulling out a secret weapon to turn the tables is just like him~♪'
 hide nao_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show rena_v002 smile_blush at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Um, Rena-san. Maybe it would be more accurate... {i}not{/i} to say that was cool, but rather, so wild that you'd have to have twenty screws in your head loose to be able to do it...?"
 hide rena_v002
 show rika_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show rika_v002 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. Keiichi's style of not holding back even when fighting against girls is ungentlemanly and brutish..."
 hide satoko_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan_close at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au... our rulebreaking tactics today were also pretty unladylike...'
 hide rika_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(And then they keep talking on and on about that stuff...)'
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at active
 show mion_v002 fuan at leftright_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'What the hell, Kei-chan?!\nNo one ever comes here, sure, but you made a big ass hole right up in the middle of this place!'
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "You know that if the town council members saw that, they'd be heated, right?! Granny might even grab a katana and slice you to pieces if she found out!!"
 show keiichi_v007 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show keiichi_v007 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "M-My bad...! I didn't realize how powerful that'd be, so I accidentally..."
 hide mion_v002
 show shion_v002 normal_close at mei_right
 with Dissolve(0.5)
 show keiichi_v007 fuan at inactive
 show shion_v002 normal_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...You'll need to take responsibility for the time being, Kei-chan, so your nails―..."
 show keiichi_v007 fuan at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'No, in this case, we\'ll have to go with "fingers".\nIf you give up and apologize, I think you\'ll be able to get off with just three... hopefully.'
 play audio 'audio/sfx/SE_202_armready.wav'
 show shion_v002 sinken at inactive
 show keiichi_v007 odoroki at active
 show mion_v002 sinken behind keiichi_v007
 show mion_v002 sinken at inactive: 
  yanchor 1.0
  pos (280, 1200)
 with Dissolve(0.5)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Wha-...? Fingers... wa-wait, Shion!\nWhere'd you get that knife?\nThat isn't the kind they use to sharpen pencils, is it?!"
 play audio 'audio/sfx/SE_229_grap.wav'
 show mion_v002 sinken at inactive behind keiichi_v007
 show shion_v002 sinken at inactive
 show keiichi_v007 sinken at active
 show keiichi_v007 sinken at chara_shake_transform
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") '...And what are {i}you{/i} doing, Mion?\nWhy are you restraining me from behind?!'
 show mion_v002 sinken at inactive
 show keiichi_v007 sinken at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Don't let him get away, Sis.\nWithout Kei-chan's fingers, it'll be our throats..."
 show shion_v002 sinken at inactive
 show keiichi_v007 sinken at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Yeah, true.\nY'know, I was wrong... Kei-chan.\nMaybe {i}sharp objects{/i} really were the better weapons, huh...?!"
 show mion_v002 futeki at inactive
 show shion_v002 sinken at inactive
 show keiichi_v007 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'H-...hey, Mion, Shion...?\nTh-this is a joke, right...?\nNo, you guys seriously look creepy right now...?!'
 hide keiichi_v007
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show shion_v002 sinken at mei_right
 show mion_v002 sinken at mei_left
 with Dissolve(0.5)
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 show mion_v002 sinken at active
 show shion_v002 sinken at active
 Character('Mion and Shion',ctc="ctcArrow", ctc_position="fixed") '"Ya better be ready, Kei-chan...!"\n"Please do be ready, Kei-chan...!"'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show keiichi_v007 fuan at mei_center
 with Dissolve(0.5)
 show keiichi_v007 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'G-...gyaaaaaaaah?!'
 show keiichi_v007 fuan at jumping_transform
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 show keiichi_v007 fuan at inactive
 narrator '............'
 show keiichi_v007 fuan at inactive
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(How we were all forgiven after that...)'
 show keiichi_v007 fuan at inactive
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(...I don't know the specifics. Yeah, let's keep it a mystery.)"
 call chapter_end
 
 $ persistent.chara042003_done = True
 return