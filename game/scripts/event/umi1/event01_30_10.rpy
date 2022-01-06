label event01_30_10:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=3
 $ event_store.current_chapter='event01_30_10'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.ogg'
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '...has been in something like an anime or a manga before.'
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice 'Huh? C-Can you repeat that once more...?'
 show nao_v002 normal at active
 show beatrice_v001 fuan at inactive
 nao 'I think... that this magic circle appeared in some manga or anime before, probably.'
 camera at screenshake_transform
 pause 0.0
 show beatrice_v001 odoroki at active
 show nao_v002 normal at inactive
 beatrice "What'd you say?! Manga...?!?!"
 hide nao_v002
 show erika_v001 sinken_close at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 show beatrice_v001 odoroki at inactive
 erika "Beatrice, haven't you seen it...? Detective Wanyan."
 show beatrice_v001 futeki at updown_shake_transform,active
 show erika_v001 sinken_close at inactive
 beatrice "Huh?! Ahahahaha, I'm more Team Kaneda Case Files, remember?"
 show beatrice_v001 futeki at active
 show erika_v001 sinken_close at inactive
 beatrice "Detective Wanyan is too childish, so I don't watch it. That said, I remember Shannon saying it was interesting and recommending it to me."
 show erika_v001 odoroki at active
 show beatrice_v001 futeki at inactive
 erika '...It seriously is {i}incredibly{/i} interesting, so do please watch it.'
 show erika_v001 odoroki_close at chara_shake_transform,active
 show beatrice_v001 futeki at inactive
 erika "Even though I had recommended it so much to my master as well, she didn't even so much as glaaaaaanceee..."
 hide beatrice_v001
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "For people who don't know much about it... it'll look like a really grotesque magic circle."
 show nao_v002 normal at active
 nao 'But... for people who know, it might actually make them smile.'
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'Did this magic circle... appear in Detective WANYAN...?'
 show erika_v001 odoroki at mei_right
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika "If you haven't watched it yet, please do sooo... It's really popular and the screening period has extendeddd..."
 hide dlanor_v001
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao '...The movie, Detective Wanyan\'s "Mid-Autumn\'s Lament: The Heartbroken Rabbits Murder Case"...'
 show erika_v001 sinken at active
 show nao_v002 normal at inactive
 erika 'The serial killer in this movie leaves magic circles on the crime sceneeeee...'
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao '...Is that serial killer...... popular?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide nao_v002
 hide fade onlayer curtain
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 $ event_store.current_progress = 4
 show erika_v001 sinken at active
 erika "Um, YEEEEEEEEEEESSSSSSSSS?! They're saying Bright-sama has like 10 billion men after him in real liiiiifeeeeeee!!!!"
 show erika_v001 smile at active
 erika "It's just so mysterious, just so beautiful the way that he pierces through the melancholy of love by eternally tying someone to him through death...!! Aaaahhhhhnn, Bright-samaaaaaaaa...!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 fuan at mei_center
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 beatrice 'S-... So, this means in the movie, a handsome killer leaves a "sign" at the crime scene...?'
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 fuan at mei_center
 with Dissolve(0.5)
 show erika_v001 fuan at active
 erika 'Looking at it as a witch and thinking that the magic circles are silly is part of its chaaaaaaarrrmm!!! The author, Mr. Go Daikanyama, is an expert on mystery, not on magic circleeeeeess!!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 smile at active
 erika 'And you know what else? You know what elsee?! The magic circle that Shion brought has the details all wroooooonggg!!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika "There wasn't enough love, no, there wasn't any love in it at all, so they couldn't see it! In any event, I absolutely HAVE to attend the 3 time screening at the theaters a month from nooooowwwww!!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 futeki at active
 erika "The way that I drew it was perfect! Even Mr. Go Daikanyama's Chief Ash character was able to learn it himself in just three days while in confinement!!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 fuan at mei_left
 show beatrice_v001 fuan at mei_right
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 show dlanor_v001 fuan at inactive
 beatrice 'No hesitation coming out about doing the crime now, huh?'
 show dlanor_v001 fuan at active
 show beatrice_v001 fuan at inactive
 dlanor 'Essentially... having only seen the Wanyan movie once, Shannon, Mion, and Shion were able to see the meaning behind the circle with EASE...'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "Shannon-san should have also been aware that Mion-san's group was doing a cosplay photo shoot."
 show nao_v002 normal at active
 nao "And so, as she entered the room to fix the window lock... just as she saw in the movie, the sheets with the handsome criminal's magic circle were sitting there."
 hide nao_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show beatrice_v001 fuan at mei_right
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice '...Haaaaahh... So, in place of being afraid of it, she saw it as a fellow fan of the series and began to smile, huh...'
 show nao_v002 normal_close at active
 show beatrice_v001 fuan at inactive
 nao "And Erika-san put a suggestive smile on her face after hearing that the room wasn't broken into..."
 hide beatrice_v001
 show dlanor_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show dlanor_v001 fuan_close at active
 show nao_v002 normal_close at inactive
 dlanor '...I understand the sentiment behind why Shannon naturally said, "No, please be at ease.", a little bit more NOW.'
 show nao_v002 normal at active
 show dlanor_v001 fuan_close at inactive
 nao "I haven't watched the movie, but I suppose even the way the bed was laid waste to was likely based on the movie. "
 show nao_v002 normal at active
 show dlanor_v001 fuan_close at inactive
 nao "Now that I think about it, Erika-san's blanket and pillows on her bed were arranged... in a pattern, exactly the same as my bed was back then."
 hide dlanor_v001
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v002 normal at inactive
 beatrice "...Guess I'm... gonna have to read Detective Wanyan, huh..."
 show nao_v002 smile at active
 show beatrice_v001 futeki at inactive
 nao "I also have some interest in this recent case. ...I'll search for the specific volume in the bookstore."
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao "For that reason, the first magic circle accident was done by Erika-san's hands, aaand, um..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade onlayer curtain
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken_close at chara_shake_transform,active
 erika 'Yeah, yeah. I resiiiiiignnnnn... It was my faaaaulltttt...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken_close at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show erika_v001 sinken_close at inactive
 dlanor 'Are you okay with RESIGNING?'
 show erika_v001 sinken_close at active
 show dlanor_v001 normal at inactive
 erika "I'm finiiished... defeeeated. I'll behave and go back home to read through the whole Wanyan manga series agaaaiiinnn..."
 hide erika_v001
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show beatrice_v001 smile at jumping_transform,active
 beatrice 'Why not even lend some volumes to me? For you to go that far in punishing yourself is dreadfully fascinating!'
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor "In that case, through Erika's resign, the winners are Beatrice and NAO. I congratulate the both of YOU."
 hide dlanor_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5040_handclap.wav'
 pause 1.3333333333333333
 play audio 'audio/sfx/SE_5040_handclap.wav'
 narrator 'Dlanor-san started a round of applause, so Beatrice and I joined in.'
 narrator 'As if she had transformed into a sea mollusc wriggling around its tendrils, Erika-san begrudgingly joined in on the applause for us...'
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 beatrice "Yeah!! I'm very satisfied! I truly had a fun birthday!"
 show beatrice_v001 futeki at jump_transform,active
 beatrice 'Nao, Erika!! You two have successfully cured me of my boredom.'
 show beatrice_v001 smile at active
 beatrice 'As a reward to Erika for sending me this delightful present, allow me to give you this handwritten letter I put together stating what a wonderful messenger you were, addressed to Lady Bernkastel.'
 show beatrice_v001 smile at active
 beatrice "What's more, in the postscript, I recommended Detective Wanyan to her as well, stating how amusing I find it!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide fade onlayer curtain
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at chara_shake_transform,active
 erika 'M-Miss Beatrice...!! Thank you for your wordsss!! Ha-, haaaaaahhh!!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show dlanor_v001 normal_close at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show nao_v002 normal at inactive
 dlanor 'Nao, please do not misunderstand ERIKA. ...Erika plays her part both as an outstanding detective and a pitiable criminal, and does a fine job as an ACTRESS. '
 show nao_v002 smile at active
 show dlanor_v001 normal_close at inactive
 nao "...I realize that. She's only pretending to be the villain, but normally, she actually isn't like that."
 show dlanor_v001 smile at active
 show nao_v002 smile at inactive
 dlanor '......Nao, you really are an extraordinary person, even coming up to par with voyager WITCHES.'
 hide dlanor_v001
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice 'And Nao! You came to {i}my{/i} Rokkenjima and spent lots of time playing games with me until the very end!'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao '...My intention was to embroider while relaxing in the rose garden, though. It became the {i}worst{/i} possible vacation ever.'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao 'But... I might have also enjoyed it a little bit... maybe.'
 show beatrice_v001 normal_close at active
 show nao_v002 smile at inactive
 beatrice 'Dawn will arrive soon. We will part then.'
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice "I'll present you with a small token of my thanks. Do look forward to it upon waking up."
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao "Thanks. ...If I can play with you again... maybe coming back to Rokkenjima wouldn't be so bad."
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice "I'll be waiting! Come whenever you like!"
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika "If you fell off of a boat closeby to the island, you'd drift here on your own anyway."
 show dlanor_v001 normal_close at active
 show erika_v001 normal at inactive
 dlanor '...Nao, while I was peaking through your Fragments... I caught glimpse of a hapless fate to COME.'
 show dlanor_v001 normal at active
 show erika_v001 normal at inactive
 dlanor "Be strong, and please live ON. If it's you, you should be able to acquire any Fragment POSSIBLE. "
 hide dlanor_v001
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "I'm just a little girl who loves her sister. ...Whatever happens, happens. I don't have any fears or expectations."
 hide nao_v002
 with Dissolve(0.2)
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator '...Ah. I can feel my vision... slowly darkening.'
 narrator "Morning will come, and I'll probably rise out of bed."
 narrator "...It was fun, here at Rokkenjima. Next time I come... I'll definitely be able to relax and embroider..."
 stop music fadeout 2.0
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(3.0)
 play music 'audio/bgm/BGM_GACHA_COLLAB2.ogg'
 show white_cover onlayer curtain as fade with Dissolve(2.0)
 stop sound
 show expression 'images/bg/AdvBg_2221.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_2271.png' as bg
 call wipein_routine
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 call wipein_routine
 play audio 'audio/sfx/SE_543_bird.wav'
 narrator "...I started to hear the sparrows chirping. If I slowly open my eyes... I'll be able to see the ceiling of my room being warmed up by the morning sun......"
 narrator "Today, I'm parting ways with Rokkenjima, huh...?"
 narrator "Now that I've said that, I believe Beatrice told me she had a present for me."
 narrator '"Do look forward to it upon waking up.", is what she told me, I think...'
 stop music fadeout 0.5
 show black_cover as bg
 narrator 'I should have never come to this island.'
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.ogg'
 nao 'N... n......'
 nao 'Nooooooooooooooooo!!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1270.png' as bg
 play audio 'audio/sfx/SE_346_ls_blood.wav'
 hide fade onlayer curtain
 with Dissolve(1.0)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 narrator 'The poor victims... were on the bed covered in blood.'
 narrator "Mion-san's negligee used to be very lovely."
 narrator 'But... it had been relentlessly cut by a blade or something of the sort, and torn to shreds.'
 narrator 'The blood that must have poured out from that spot had dyed the negligee and the sheets to the point where I could no longer remember what color they were originally.'
 narrator 'Shion-san was in a gown. ...Of course, she was also stained with fresh, bright red blood.'
 narrator 'Just like the other one, it had been torn to shreds... and was clearly in a pitiful state.'
 narrator 'Out of three beds, two were covered in blood... But one bed was still as clean as it was last night. That was... my bed.'
 narrator "And I was the only one... who wasn't covered in a single drop of blood... while having slept soundly in the same room as them..."
 narrator 'I wanted to ask "A-Are you okay...?". But the only thing that came out of my mouth was a faint, unsteady groan that was too weak to be called a scream.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 play audio 'audio/sfx/SE_527_door_close.wav'
 narrator 'I dashed out to the next room over, frantically knocking on the door while trying at the doorknob.'
 nao 'Erika-san, Erika-san!! S-Something awful happened! H-H-Help...!!'
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 play audio 'audio/sfx/SE_526_door_open.wav'
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'Huh...? It opened...?'
 hide nao_v002
 with Dissolve(0.2)
 narrator "Even if you turn a doorknob, when it's locked, there's no way it would open."
 narrator 'Rattling the doorknob like that was just my unconscious way of informing her of my confusion and the abnormality of the situation.'
 narrator "...That's why I didn't actually expect the door to open."
 narrator 'It was so unexpected... that it made my heart stop for a second... sharpening my senses like a knife.'
 narrator "Extreme fear can numb our emotions and sharpen our senses to the limit. But... it's a blade of ice in the end. ...No matter how sharp it is, it's fragile and easily shattered......"
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'Erika...san...?'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_1270.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 narrator 'It was stained... Erika-san was also on the bed... red and bloody......'
 camera at screenshake_transform
 pause 0.0
 nao 'Noooooooooooooooooooooooooooooooo!!!!!!!!!!!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(2.0)
 show black_cover as bg
 pause 2.0
 stop music
 nao '......Erika-san, good morning.'
 narrator "Of course, corpses don't speak."
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.ogg'
 narrator "So, corpses don't need to breathe either."
 play audio 'audio/sfx/SE_5005_grab.wav'
 erika 'Gh......'
 erika '.......................................'
 erika '............................................................nn--'
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 normal at mei_left
 show erika_v001 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show nao_v002 normal at inactive
 erika 'Guh--!!! A-Are you trying to kill me?! Haah, haah, *cough*cough*!!!'
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao 'Good morning, Erika-san.'
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao "This is another reenactment of a scene you saw in the Wanyan movie, isn't it?"
 show erika_v001 futeki at active
 show nao_v002 normal at inactive
 erika "*giggle*giggle*giggle*! Wasn't it perfect?! I thought my death face in particular was the ultimate expression of one's leftover traces of regret and yearning!!"
 show erika_v001 smile at active
 show nao_v002 normal at inactive
 erika 'Just through my love for Detective Wanyan, this level of cosplay is possible for Erika Furudo! What do you think, Mion-san and Shion-san?!'
 show nao_v002 fuan_close at active
 show erika_v001 smile at inactive
 nao '...Dead bodies over there too. I wish there were grades on these to see who did it better...'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator 'With an intrepid laugh, Erika-san burst into our room looking like a zombie out of a horror movie.'
 call wipeout_routine
 call wipein_routine
 pause 2.0
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 erika "Oooohhh!!! ...What a splendid recreation! This must be... if I'm correct... the movie scene at 32 minutes and 18 seconds......"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 nao "Is this... did you guys sneak a picture at the theaters...? That's a crime. Movie thieves. Popcorn is gonna shoot out of your heads now."
 hide nao_v002
 with Dissolve(0.2)
 narrator 'From who knows where, Erika-san grabbed out a secret detective gadget with a little screen... which depicted a scene that matched perfectly with what was in this room...'
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 $ event_store.current_progress = 5
 show erika_v001 smile at active
 erika 'Firstly, Shion-san, powerful portrayal of Slugger-kun!'
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show erika_v001 smile at jumping_transform,active
 erika "Yeah, that's it, the clothes being perfectly in the right form, just like that! This couldn't be done unless you allowed the character to envelop your soul!"
 show erika_v001 smile at chara_shake_transform,active
 erika 'But what ties it all together is that reactionary death face!! Truly an amazing facial expression! Just let me give you an A+!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide fade onlayer curtain
 show shion_v002 smile_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show shion_v002 smile_blush at jump_transform,active
 shion "Haaaah! That's a Wanyanner if I see one!! You judged it down to every last detail, huh?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide shion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'Incredible. ...She just sprang up from out of her death position like it was nothing...'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 $ event_store.current_progress = 6
 show erika_v001 smile at active
 erika "Now I'll judge Mion-san. This one is a depiction of Matilda-san; very nicely done as well!"
 show erika_v001 smile at active
 erika 'I had already called the other one perfect... but this one really has me feeling like this is a <double perfect!!>'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at active
 show nao_v002 fuan at inactive
 shion "Nao-san, do you get why she's so hung up on the details?"
 show nao_v002 fuan_close at active
 show shion_v002 smile at inactive
 nao '......Yeah, not at all.'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 smile at active
 erika "The bottom edge of this negligee! See how it puffs out a little bit? Right here! There's a ring case hidden here!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show erika_v001 fuan at active
 erika "Since you can't see it at all, lots of cosplayers might lazily gloss over that fact... but with Mion-san...?!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_5037_getup.wav'
 pause 2.0
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 erika "She has iiiit!! Absolutely artful remastering of the original work!! It's perfect, even down to the scar she got from when she was thrown back!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao "...I just don't know what's happening anymore."
 show mion_v002 futeki at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 show nao_v002 fuan at inactive
 mion '*cackle*cackle*cackle*! God is in the details! Being fastidious even over aspects that go unseen is to be a true Wanyanner!'
 show nao_v002 fuan_close at active
 show mion_v002 futeki at inactive
 nao "...I'm so sorry. Once I get back I'll absolutely go to the movie theaters."
 hide nao_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 $ event_store.current_progress = 7
 show shion_v002 smile at jump_transform,active
 show mion_v002 futeki at inactive
 shion "Even looking at Erika-san's clothes, I can somehow tell she recreated Mirai-san's death scene!"
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show mion_v002 smile at jumping_transform,active
 show shion_v002 smile at inactive
 mion "Let's go check out Erika-san's room! Erika-san, we wanna see, so just die one more time, one more time!!"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao '...Really, everyone, just die once......'
 hide nao_v002
 with Dissolve(0.2)
 narrator "These Wanyanners are having a blast because they're so incredibly compatible."
 narrator 'I feel like some pretty edgy words were being exchanged yesterday, but that was also likely... another Wanyan recital they started doing.'
 narrator 'Mion-san, Shion-san, and Erika-san all have common interests, so they were able to get onstage together and hit it off fast...'
 narrator 'So with that, they engaged in an edgy Western mystery roleplay conversation that only people who were in the know could enjoy...?'
 show erika_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 smile at inactive
 nao 'Stop. ...Thereupon, we arrive at a very obvious question.'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'A question? And what could that be?'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'Ah-, maybe enjoying the movie is actually impossible without finishing the manga first, is that what you mean?'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Finishing the whole series is as brutal as one would expect! Shouldn't she start off on volume 68?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide shion_v002
 hide fade onlayer curtain
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_341_ls_WhistleShort.wav'
 pause 0.16666666666666666
 play audio 'audio/sfx/SE_341_ls_WhistleLong.wav'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika 'Eeeeeee~! Never that, never that! Without knowing the depth surrounding the character relationships in the Wanyan universe, the entertainment level would dramatically decrease!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show shion_v002 smile at mei_center
 with Dissolve(0.5)
 show shion_v002 smile at updown_shake_transform,active
 shion 'Riiight?! Nao-san definitely needs to read through the entire thing!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide shion_v002
 hide fade onlayer curtain
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at active
 nao "Please cut that out. I'm gonna chop you guys up."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'The Wanyanners were taken aback, shrieking with a little "Hee?!"'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 pause 1.0
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.ogg'
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v002 fuan at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 fuan at inactive
 nao 'I will now set up an inquiry for everyone.'
 show nao_v002 normal at active
 show mion_v002 fuan at inactive
 nao 'Depending on your answer, it will literally become a murder case, so please reply with caution.'
 show mion_v002 fuan at chara_shake_transform,active
 show nao_v002 normal at inactive
 mion "Wha-whaaat~...? If you're gonna threaten me, Nao-chan, don't ruin it with having such a cuuuute little face. Okay?"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v002 sinken at active
 show mion_v002 fuan at inactive
 nao "I'm glad that you taught me that, you know?"
 hide mion_v002
 show shion_v002 fuan at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show nao_v002 sinken at inactive
 shion 'Taught you... what...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide shion_v002
 hide fade onlayer curtain
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao "When that magic circle appeared on my bed, I'm really glad that you taught me that, you know?!"
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao 'This was an actual scene from the Wanyan movie! In teaching me that, it stopped being scary to me.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v002 fuan at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 fuan at inactive
 shion "That's... yeah...?"
 show mion_v002 fuan_close at active
 show shion_v002 normal at inactive
 mion 'Nao-chan getting surprised was... excessively cute... though unintentional...'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '{i}Yeah{/i}... "Excessively cute, though unintentional.". 34 letters, right?'
 show nao_v002 normal_close at active
 nao "I'm going to chop you and Shion-san into 34 bits."
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal_close at inactive
 nao "Let's continue, Erika-san. ...Did you really see it?"
 show erika_v001 smile at active
 show nao_v002 normal at inactive
 erika "Eh? See what? Of course I saw all of Wanyan's broadcast...."
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 show erika_v001 smile at inactive
 nao "The magic circle in your room! Shion-san's prank had already been done before noon!"
 show nao_v002 normal at active
 show erika_v001 smile at inactive
 nao "You checked inside before you locked your room, but you said you found nothing out of the ordinary. ...That was a lie, wasn't it?"
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika "...You were so confused over the case with Shannon-san not batting an eye at the magic circle prank that I thought I'd maybe mess around with you for a little bit...♪"
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao "Your statement in total had 49 vowels... right? I'll do you a favor and make it 50."
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '50 pieces would definitely be painstaking to get to, though, so tossing Erika-san in a food processor would be much more fun.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 camera at screenshake_transform
 pause 0.0
 narrator '"Eeeekkk, how grotesque!!" The three shrieked.'
 narrator 'No, from my point of view, the image of three massacred bodies banding together in front of me has been {i}far more{/i} grotesque.'
 show nao_v002 normal_close at mei_center
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 nao "Well, since you three already apologized earnestly, I'll save mincing you up for another day."
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at chara_shake_transform,active
 show shion_v002 smile at inactive
 mion 'Haaaahh. Thank goodnesss! Nao-chan, if you watched Wanyan too it would be awesome!'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "If you see the movie, you'll AB-SO-lutely sink deep into the Wanyan swamp."
 hide mion_v002
 show erika_v001 smile at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show erika_v001 smile at jumping_transform,active
 show shion_v002 smile at inactive
 erika "Wanyan swamp, cool term. There's apparently a cafe collabing with them that opened recentlyyy! Let's go togetheeerrrr!!"
 hide shion_v002
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '...The last mystery has just emerged.'
 show nao_v002 normal at active
 nao "I've finally grasped that each of you are wildly enthusiastic about Detective Wanyan."
 show nao_v002 normal_close at active
 nao "But with that said... it's a bit hard to understand why you guys are so chummy."
 show nao_v002 fuan at active
 nao 'At what point did you guys start getting along so well?'
 hide nao_v002
 with Dissolve(0.2)
 narrator "Aah... it's getting more and more clear. For me, my stay on Rokkenjima has been a very mysterious three days and two nights, involving witches, magic circles, and puzzles to solve."
 narrator 'But...'
 narrator 'As I was fearing magic circles and concerned with baffling mysteries... a "{i}preposterous{/i}" secret feud between the girls began to ensue.'
 call chapter_end
 call event01_30_99