label chara072005_01:
 show black_background onlayer black
 $ event_store.current_event='chara072005'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072005_01'
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
 show expression 'images/bg/AdvBg_82.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 camera:
  pos (960, 510)
  zoom 1.3
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v001 smile at mei_center
 with Dissolve(0.5)
 show mion_v001 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Okaay, that does it for today's practice!\nThanks for the hard work, everyone!"
 hide mion_v001
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show miyuki_v001 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v001 smile at active
 show miyuki_v001 smile at deepbreath_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Aaah... we're finally done.\nThis part of the play had a lot of really flashy scenes, so there was a lot more moving around than I thought."
 show rena_v001 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v001 smile at inactive
 show rena_v001 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Ahahaha. But I think we've all gotten better since we started practicing, no?"
 show miyuki_v001 smile at inactive
 show rena_v001 smile_close at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Keiichi-kun and Mii-chan's showdown at the end in particular was super cool... hau hau~♪"
 show rena_v001 smile_close at leftright_shake_transform
 hide miyuki_v001
 show shion_v001 smile at mei_left
 with Dissolve(0.5)
 show rena_v001 smile_close at inactive
 show shion_v001 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'It sure was. Their performance was so breathtaking that I felt like I was going to get sucked in, even while acting together with them.'
 hide rena_v001
 show keiichi_v001 smile at mei_right
 with Dissolve(0.5)
 show shion_v001 smile at inactive
 show keiichi_v001 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Oh, really?\nHeheh... then I'm glad I joined the play!"
 hide shion_v001
 show rika_v001 smile at mei_left
 with Dissolve(0.5)
 show keiichi_v001 smile at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. I was worried we wouldn't make it in time since we rewrote it from a dark-themed play to a light-hearted one midway through..."
 show keiichi_v001 smile at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But I'm glad we pulled it off.\nI think the kids are going to be pleased with it if we do it this way. Nipah~☆"
 hide keiichi_v001
 show satoko_v001 futeki at mei_right
 with Dissolve(0.5)
 show rika_v001 smile at inactive
 show satoko_v001 futeki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ohohohoho! This is definitely a classic example of that one saying, "Blood hardens after the pain"~!'
 hide rika_v001
 show hanyuu_v001 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v001 futeki at inactive
 show hanyuu_v001 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'A-Au au... Satoko, what hardens after {i}the rain{/i} in that saying is "dirt", not "blood".'
 hide hanyuu_v001
 show nao_v001 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v001 futeki at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...That wording was particularly unsettling even if you misspoke.\nCould you have said this on purpose?'
 show nao_v001 fuan at inactive
 show satoko_v001 sinken at active
 show satoko_v001 sinken at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "H-How rude! I was trying to praise Keiichi-san and Mion-san's great work in my own way!"
 hide satoko_v001
 hide nao_v001
 with Dissolve(0.2)
 show mion_v001 smile at mei_center
 with Dissolve(0.5)
 show mion_v001 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Alright, alright, I think you guys sold the punch line already.\n...Hey, who's hungry? We can drop by my place and get some ohagi if you guys like."
 hide mion_v001
 with Dissolve(0.2)
 show rena_v001 smile at mei_right
 with Dissolve(0.5)
 show rena_v001 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hauu~, yeah, yeah!\nNao-chan, would you maybe want to come with me, come with me?'
 show nao_v001 smile_blush at mei_left
 with Dissolve(0.5)
 show rena_v001 smile at inactive
 show nao_v001 smile_blush at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "O-Of course I'd love to go with you if you're going, Rena...!\nDo you guys want to come too?"
 hide rena_v001
 show miyuki_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v001 smile_blush at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, I wonder. That probably won't hold me over for dinner... I might have to decline."
 hide nao_v001
 hide miyuki_v001
 with Dissolve(0.2)
 show shion_v001 fuan at mei_center
 with Dissolve(0.5)
 show shion_v001 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Ah, I'll pass. I'm pretty sure the hag was at home all day, so me being there with everyone is... kinda..."
 show mion_v001 odoroki at mei_right
 show shion_v001 fuan
 show shion_v001 fuan:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 with Dissolve(0.5)
 show shion_v001 fuan:
  yanchor 1.0
  pos (480,1200)
 show shion_v001 fuan at inactive
 show mion_v001 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Huh? Shion, what are you passing on it for at this point?\nShe never says it out loud, but Granny doesn't think badly about having you near the main house anymore."
 show shion_v001 fuan at inactive
 show mion_v001 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "As proof of that, she doesn't complain that its loud to me or Mom when you come over to pick up your stuff from time to time. So it's fine, absolutely no problem!"
 show mion_v001 smile at inactive
 show shion_v001 odoroki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "R-Really now...? I don't know what happened to that stubborn old hag to make her have a change of heart..."
 show mion_v001 smile at inactive
 show shion_v001 smile_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Mmm, but yeah, still, I'm good with that for today.\nI don't have long until my part-time job starts, and I have {i}important{/i} things to do with Satoko~."
 hide mion_v001
 show satoko_v001 fuan at mei_right
 with Dissolve(0.5)
 show shion_v001 smile_close at inactive
 show satoko_v001 fuan at active
 show satoko_v001 fuan at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Eek? Wh-what do you mean, Shion-san...?\nI didn't do anything particularly reprehensible today, did I?"
 show satoko_v001 fuan at inactive
 show shion_v001 futeki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hoh, so you're saying you aren't aware...?\n...I heard from Coach that it seems you've been seeing a {i}dentist{/i} recently...?"
 show shion_v001 futeki at inactive
 show satoko_v001 fuan at active
 show satoko_v001 fuan at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '*gulp*?! Wh-what do you mean by that...?\nO-Ohohoho...'
 hide shion_v001
 show rika_v001 smile at mei_left
 with Dissolve(0.5)
 show satoko_v001 fuan at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Playing dumb is pointless, Satoko.\nWe already know very well that the dentist in Okinomiya contacted Irie. Nipah~.'
 show rika_v001 smile at inactive
 show satoko_v001 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Wh-...whaaaaaaat?\nIt's not very doctorly to betray the privacy of your patieeeents!"
 hide rika_v001
 show hanyuu_v001 normal at mei_left
 with Dissolve(0.5)
 show satoko_v001 sinken at inactive
 show hanyuu_v001 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...Au au, Satoko. Doctors regularly keep in contact with each other to check the compatibility of the medicines they prescribe~.'
 hide hanyuu_v001
 show rika_v001 normal_close at mei_left
 with Dissolve(0.5)
 show satoko_v001 sinken at inactive
 show rika_v001 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Plus, recently you've been drinking water weirdly.\nIt's like you timidly turn your face away so we can't see..."
 show rika_v001 normal_close at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'm-... I'm not actually suffering from a cavity, you know?\nBut there this teensy, tiny sting-like sensation whenever I have something cold..."
 hide rika_v001
 show shion_v001 smile at mei_left
 with Dissolve(0.5)
 show satoko_v001 fuan at inactive
 show shion_v001 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That sounds like a cavity. ...Well, in any event, I'm taking you to see the dentist. Oh, and as for everyone else, do please have fun without worrying about it~!"
 hide satoko_v001
 show mion_v001 normal at mei_right
 with Dissolve(0.5)
 show shion_v001 smile at inactive
 show mion_v001 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Mmm, can't be helped in that case.\nWell then, Satoko, until your dental work is finished, you'll have to lay off the candy for a while~."
 hide shion_v001
 show rena_v001 smile at mei_left
 with Dissolve(0.5)
 show mion_v001 normal at inactive
 show rena_v001 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Get well soon, Satoko-chan.\nOnce you can eat again, Rena and everyone will make all sorts of sweet things for you, okay?'
 hide mion_v001
 show satoko_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show rena_v001 smile at inactive
 show satoko_v001 fuan_close at active
 show satoko_v001 fuan_close:
  yanchor 1.0
  linear 0.3333333333333333 pos (1440,1250)
 pause 0.3333333333333333
 show satoko_v001 fuan_close:
  yanchor 1.0
  pos (1440,1250)
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ghh... u-understood...'
 hide rena_v001
 hide satoko_v001
 with Dissolve(0.2)
 show miyuki_v001 odoroki at mei_center
 with Dissolve(0.5)
 show miyuki_v001 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Okay, so aside from Shion and Satoko, who else is... oh, what's wrong, Kazuho? You're raising your hand."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide miyuki_v001
 hide fade onlayer curtain
 show kazuho_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v001 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah, um... is it maybe alright if I also... excuse myself today...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v001 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v001 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Eh? ...What for? You didn't get a cavity too, did you?"
 show kazuho_v001 fuan at mei_right
 with Dissolve(0.5)
 show nao_v001 odoroki at inactive
 show kazuho_v001 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I-It's not that...\nI just feel a little tired today and wanted to rest until dinner, so..."
 hide nao_v001
 show mion_v001 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v001 fuan at inactive
 show mion_v001 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ah, I see. Not a problem then, but...'
 hide mion_v001
 show nao_v001 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v001 fuan at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Are you alright, Kazuho?\nIf you're not feeling well, we can go home with you..."
 show nao_v001 fuan at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Mm-mm. I don't mind if I'm a little late, so you and Miyuki-chan go and can enjoy yourselves. ...See you."
 play audio 'audio/sfx/SE_5019_doorclose.wav'
 hide kazuho_v001
 hide nao_v001
 with Dissolve(0.2)
 show rika_v001 fuan at mei_center
 with Dissolve(0.5)
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 call chapter_end
 jump chara072005_02