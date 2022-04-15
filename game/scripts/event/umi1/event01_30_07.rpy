label event01_30_07:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=4
 $ event_store.current_chapter='event01_30_07'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2331.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST2_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'We returned to the guesthouse, where lunch was being served in the hall.'
 narrator 'Shion-san was going on about how high-quality the silverware was.'
 narrator 'Once you get used to the cuisine on this island, you might never want to go back... maybe.'
 show shion_v008 fuan at mei_left
 show mion_v015 smile at mei_right
 with Dissolve(0.5)
 show mion_v015 smile at inactive
 show shion_v008 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Let's get changed quickly. I don't want to be eating lunch like this."
 show shion_v008 fuan at inactive
 show mion_v015 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Reaaally? This ol' man doesn't mind at all, though."
 show mion_v015 smile at inactive
 show shion_v008 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Sis, you might be okay with it, but I'd prefer to be modest. Anyways, I'm going upstairs to change."
 hide mion_v015
 hide shion_v008
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I would also like to return to my room for a bit to wash my hands.'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I can't bring myself to embroider at all, so I'll have to set it aside for now."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 narrator 'After folding my clothes neatly, I glanced around with a carefree look, where the sounds of clothes being shed resounded.'
 narrator "It's amazing that they're not afraid to put their nakedness on display even if they have a sisterly bond..."
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'This is the last Angel Mort request, right?'
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Yup! This afternoon, we\'re doing the "Heartbroken Rabbits Murder Case" photo set~!'
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Hey, Nao-san, you wanna join?'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Um... thanks, but getting embarrassed like that is gross.'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "It's fiiine, it's {i}fiiine{/i}, there's no need to be embarrassed! After all, you can be the star!"
 play audio 'audio/sfx/SE_604_Is_status.wav'
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ta-da! It's a Wanyan costume~!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator "...I see. Surely I wouldn't be embarrassed wearing a giant slug costume... maybe?"
 narrator 'Wait, wait, wait, do I even want to be photographed in the first place?'
 narrator "...No, I will NOT be fooling around. I'm on Team Kaneda after all..."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_526_door_open.wav'
 narrator 'Just as we left the room and locked our door, Erika-san came out of hers and did the same.'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "This time, I won't leave the door unlocked."
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Are you okay? Did a thief break in?'
 show shion_v002 smile at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Nope. You can rest assured.'
 hide shion_v002
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show erika_v001 normal_close at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "<Good>. That's nice to hear."
 hide erika_v001
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Then let's go. This wonderful smell is making my stomach rumble."
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5007_keyroll.wav'
 narrator 'Erika-san carefully tried the door to ensure it was locked.'
 show erika_v001 normal at mei_right
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'With this, my room is definitely a locked room. My mind is at ease.'
 show erika_v001 normal at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Is the window locked?'
 show mion_v002 smile at inactive
 show erika_v001 normal at active
 show erika_v001 normal at nod_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Indeed it is. Why wouldn't it be?"
 hide mion_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "*giggle*. Erika-san's an interesting person, huh?"
 hide erika_v001
 hide shion_v002
 with Dissolve(0.2)
 narrator "I think I would've preferred an uninteresting roommate who would let me relax and embroider instead."
 stop music fadeout 2.0
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2351.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 2.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2350.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST4_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_right
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "{b}What you brought as a souvenir{/b} is very intriguing, isn't it?"
 show beatrice_v001 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It's mere child's play compared to the difficulty you had while flirting with Battler-san, though."
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "...You really are a great DETECTIVE. You've used your surroundings and adapted to the situation to produce a great MYSTERY."
 show dlanor_v001 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It's only natural that those who are able to solve mysteries have the ability to create them as well."
 hide dlanor_v001
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'The mystery of the {b}first{/b} magic circle is unfolding... but Shannon I have yet to understand.'
 show erika_v001 normal_close at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'To look at a repulsive magic circle drawn on a bedsheet with such a calm demeanor...'
 show erika_v001 normal_close at inactive
 show beatrice_v001 sinken at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Hmmmm... there's not enough sugar in my head... Dlanor, I request another box..."
 hide erika_v001
 show dlanor_v001 fuan at mei_left
 with Dissolve(0.5)
 show beatrice_v001 sinken at inactive
 show dlanor_v001 fuan at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'I never thought you would be opening all of your Heaven-Speciality Angel Manjuu boxes that I brought as GIFTS.'
 show dlanor_v001 fuan at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "That's a testament to just how good they are. Angel manjuu really puts a smile on a witch's face! In fact, that should be the catchphrase!"
 hide dlanor_v001
 show erika_v001 normal_close at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Looks to me like a cruel witch eating a little angel's head in the form of a bun."
 play audio 'audio/sfx/SE_374_ls_question.wav'
 show beatrice_v001 futeki at inactive
 show erika_v001 smile at active
 show erika_v001 smile at jump_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '..."Oh, I\'m an angel manjuu☆ Am I going to... get eaten like all my friends were? Are you going to eat me...?"'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at inactive
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Gaaahhhh!! Don't say it like thaaaattt!!!! I won't be able to eat them if they have a soooouulll...!!"
 hide erika_v001
 show dlanor_v001 fuan_close at mei_left
 with Dissolve(0.5)
 show beatrice_v001 fuan at inactive
 show dlanor_v001 fuan_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'In the past, witches embodied cruelty, but now they have become quite CHARMING...'
 show dlanor_v001 fuan_close at inactive
 show beatrice_v001 fuan at active
 show beatrice_v001 fuan at chara_shake_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Erikaaaa! Give me another hiiinttt.'
 hide dlanor_v001
 show erika_v001 fuan at mei_left
 with Dissolve(0.5)
 show beatrice_v001 fuan at inactive
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'When Battler-san was begging you for mercy, what was it that you said that tormented him, again?'
 show beatrice_v001 fuan at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It really is a great feeling, controlling the red truth like it's life or death, even though the witch's side must lose in the end."
 hide beatrice_v001
 show dlanor_v001 fuan at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at inactive
 show dlanor_v001 fuan at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Even Lady Beatrice mellowed out with TIME. ...Erika, you could stand to do the SAME.'
 show dlanor_v001 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "...Yeah, yeah. I'm {i}so{/i} despicable that I'll give you the red truth you desire."
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show dlanor_v001 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "{umi_red}It was I, Erika Furudo, who performed the magic circle prank on Nao's bed.{/umi_red}"
 hide dlanor_v001
 show beatrice_v001 sinken at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show beatrice_v001 sinken at active
 show beatrice_v001 sinken at jump_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I knew that since the beginning! One more, one more!'
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show beatrice_v001 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "{umi_red}After Nao and everyone went to dinner, Erika crawled in through the window and replaced Nao's bedsheets with another that had the magic circle drawn on it in advance.{/umi_red}"
 show erika_v001 normal at inactive
 show beatrice_v001 sinken at active
 show beatrice_v001 sinken at nod_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "That was obvious too! Even Nao would've figured that out long ago!"
 hide erika_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 sinken at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Then, Shannon entered the ROOM. Why did she look at the sheet and not think anything was WRONG...?'
 show dlanor_v001 normal at inactive
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "THAT! THAT! That's one detail I still don't understand...!!"
 show dlanor_v001 normal at inactive
 show beatrice_v001 fuan_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "It's freaky how incredibly dedicated that Shannon is! I wonder if she activated some kind of hidden power?"
 hide dlanor_v001
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 fuan_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Now then, this is your last big hint, okay? Make sure you listen veeery well.'
 show erika_v001 normal at inactive
 show beatrice_v001 fuan at active
 show beatrice_v001 fuan at chara_shake_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Oh yes, please! My God, my Buddha, my lady Erikaaaaa!!'
 hide beatrice_v001
 hide erika_v001
 with Dissolve(0.2)
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_5036_glass_break.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 narrator '{umi_red}On this island, there exist people other than Shannon who would look at the situation in that room and determine there is nothing wrong.{/umi_red}'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show beatrice_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show beatrice_v001 odoroki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Whaaaaaaaaat!?! Shannon isn't the only crazy person? There are more?!"
 show beatrice_v001 sinken at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Kanon? Genji? Even Nanjoooo?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show dlanor_v001 fuan_close at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5005_grab.wav'
 show dlanor_v001 fuan_close at active
 show dlanor_v001 fuan_close at chara_shake_transform
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Th-This is DIFFICULT... This hint has only served to restrain ME...'
 hide dlanor_v001
 with Dissolve(0.2)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '*giggle*giggle*. It really is a treat to dangle riddles in front of Beatrice like this♪'
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Keep doing your best, won't you? Hadn't {b}they{/b} seen through everything on their first look...?"
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 pause 2.0
 stop sound
 show expression 'images/bg/AdvBg_2361.png' as bg
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 2.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_2271.png' as bg
 call wipein_routine
 pause 2.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_2221.png' as bg
 call wipein_routine
 narrator 'After lunch, Erika-san said she wanted to be alone and went on a walk somewhere.'
 narrator "Finally, I had the chance to embroider to my heart's content, surrounded by the wonderful roses in the arbor."
 narrator 'The Sonozaki sisters seemed to enjoy their Detective Wanyan cosplay photo shoot that afternoon.'
 narrator '...There were many ridiculous costumes appearing one after another. Just what kind of mystery {i}was{/i} this...?'
 narrator 'I have no idea why the creator decided to make the protagonist Wanyan a giant slug. Maybe that was the real mystery...'
 show shion_v012 smile at mei_left
 show mion_v004 smile at mei_right
 with Dissolve(0.5)
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "We took a lot a pictures, huh? I'm excited to develop all of them."
 show shion_v012 smile at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "We'd better finish up soon. Tonight is our last dinner together, and I think it'd taste amazing after a hardworking day!"
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Nao-saan~. We're heading back, but what will you do?"
 hide mion_v004
 hide shion_v012
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I think I'll leave too then. The wind was beginning to get cold anyway."
 hide nao_v002
 with Dissolve(0.2)
 narrator "At any rate, I don't know how the Sonozakis can take pictures outside in such revealing costumes when it's almost winter."
 narrator "...I wonder if it's true that cosplayers can withstand winter events naked if they reach max level..."
 show nao_v002 smile at mei_left
 show mion_v004 smile at mei_right
 with Dissolve(0.5)
 show mion_v004 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Are your costumes handmade?'
 show nao_v002 smile at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I wouldn't go so far as to say they're handmaaade~. But well, we did it in a bit of a rush~."
 play audio 'audio/sfx/SE_5037_getup.wav'
 show mion_v004 smile at inactive
 show nao_v002 sinken at active
 show nao_v002 sinken:
  yanchor 1.0
  linear 0.5 pos (1110,1200)
 pause 0.5
 show nao_v002 sinken:
  yanchor 1.0
  pos (1110,1200)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Let me see. ...This fabric is... hmm... mm-hmm... very shoddy. ...And how was the inner lining sewed?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v004
 hide nao_v002
 hide fade onlayer curtain
 show shion_v012 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show shion_v012 odoroki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "What are you, the costume police!? Don't look at the insideeee!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide shion_v012
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v004 fuan at mei_right
 show nao_v002 smile
 show nao_v002 smile:
  yanchor 1.0
  pos (1110, 1200)
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show mion_v004 fuan at active
 show mion_v004 fuan at chara_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Even if we don't get fazed wearing something revealing, we couldn't bear looking at the inner lining...! Spare me, Officer Good Looks!"
 show mion_v004 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Well... I happen to know a bit about clothing, so feel free to ask me for help the next time you want to make something.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide mion_v004
 hide fade onlayer curtain
 show shion_v012 fuan at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show shion_v012 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "B-But if you start helping, you'll see iiiiiittttttt!!! Ewwwww, it's sooo embarrassiiiiiiiinggggg!!!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide shion_v012
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "I seriously don't know how you can be embarrassed by people looking at the inner lining of your outfit when you've been doing sexy cosplay photo shoots outdoors..."
 narrator 'We chatted on as we returned to the guesthouse.'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Three days and two nights went by in the blink of an eye, huh?'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v004 smile at mei_right
 show shion_v012 smile at mei_left
 with Dissolve(0.5)
 show shion_v012 smile at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Yup, and we only have less than a day left before it ends.'
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "We'll be leaving tomorrow before noon. We'll be flying back by plane from Niijima Airport, I think it was."
 hide shion_v012
 hide mion_v004
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...This will be the last time I see this wonderful rose garden.'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v004 smile at mei_right
 show shion_v012 smile at mei_left
 with Dissolve(0.5)
 show shion_v012 smile at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'If this place takes our advice and opens as a magnificent resort, we can always come back.'
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Cosplay-friendly resorts are hard to find, so I definitely think this one will get really popular!'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide shion_v012
 hide mion_v004
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_536_up_stairs.wav'
 narrator 'We went up to the second floor.'
 narrator 'While Mion-san opened the door with her key... I braced myself. I was expecting to see another magic circle sitting there.'
 stop music fadeout 2.0
 show mion_v004 smile at mei_right
 show shion_v012 smile at mei_left
 with Dissolve(0.5)
 show shion_v012 smile at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Don't worry, everything was locked up tight! If there really was another magic circle, I think we'd have a closed-room mystery on our hands."
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Just relax. You won't have anything to be afraid of anymore, Nao-san."
 hide shion_v012
 hide mion_v004
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Th-that's reassuring..."
 hide nao_v002
 with Dissolve(0.2)
 show mion_v004 smile at mei_center
 with Dissolve(0.5)
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'See this?'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 hide mion_v004
 with Dissolve(0.2)
 narrator "Mion-san pointed at the keyhole, but I didn't see what she meant."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 play music "<loop 0>audio/bgm/BGM_QUEST5_COLLAB2.ogg"
 show mion_v004 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If you don't get it, you don't need to know the details... but there's actually a tiny device I set here."
 show mion_v004 smile at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh? What do you mean?'
 hide nao_v002
 show shion_v012 smile at mei_left
 with Dissolve(0.5)
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I can't go into specifics, but if you insert a key while it's inside, the cylinder will jam and break."
 show shion_v012 smile at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "An onlooker wouldn't realize it's there. Basically, until the person who created the device takes it out, the door will absolutely not open."
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Supposing someone {i}did{/i} notice the device, even if they tried to remove it, it would change shape, and there would be evidence that they got in.'
 hide mion_v004
 hide shion_v012
 with Dissolve(0.2)
 narrator "I don't know what the Sonozakis were talking about at all, but this was the gist:"
 narrator 'When she left the room this morning and locked the door, she made a strange modification to the keyhole. If someone tries to open the door by inserting the key without realizing it, the keyhole will jam and be unable to open.'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Although, a servant with a master key trying to open it for cleaning would be in a lot of trouble.'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v012 smile at mei_left
 show mion_v004 smile at mei_right
 with Dissolve(0.5)
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That's why you left this hanging, right?"
 show shion_v012 smile at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'A "Bedmaking Not Necessary" tag. If a servant sees that, there\'d be no reason for them to enter.'
 hide mion_v004
 hide shion_v012
 with Dissolve(0.2)
 narrator "Of course, the probability of the culprit noticing this device and trying to remove it isn't zero."
 narrator 'However, what the sisters are saying is that, if that {i}does{/i} happen, it will absolutely leave behind evidence.'
 narrator 'Even if the culprit knew what this device was, continuing to go at it with a master key or even a lockpick would of course bear no fruit.'
 show mion_v004 fuan at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show mion_v004 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "This trick is a secret, alright? If any amateurs try doing it, we're gonna have to batten the hatches."
 show mion_v004 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I can't come up with something like that and I don't intend to, so don't worry..."
 show mion_v004 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'That said... this trick works, right? Any signs of entry?'
 show nao_v002 normal at inactive
 show mion_v004 normal at active
 show mion_v004 normal at nod_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Nope. This proves that from when I locked it earlier to unlocking it just now, nobody else opened it.'
 hide nao_v002
 hide mion_v004
 with Dissolve(0.2)
 narrator 'But if a magic circle was there... it would actually be the work of a witch.'
 show shion_v012 smile at mei_left
 show mion_v004 smile at mei_right
 with Dissolve(0.5)
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Sis, let's open it on the count of three."
 show shion_v012 smile at inactive
 show mion_v004 smile at active
 show mion_v004 smile at jump_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Okay! Three, two, one!'
 hide shion_v012
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v004 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "P-Please don't announce it like that, just open the door quietly..."
 hide mion_v004
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "...Oh my, what's going on here? Don't tell me you {i}put some garbage in the keyhole{/i} and broke it?"
 hide erika_v001
 with Dissolve(0.2)
 show mion_v004 smile at mei_right
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Eh? We did nothing of the sort.'
 show mion_v004 smile at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I was certain that you had broken the lock on your door this time after breaking the window lock yesterday.'
 show mion_v004 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "You had me thinking that people from thatched-roof villages really weren't used to handling Western doors."
 hide mion_v004
 show shion_v012 smile at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Don't worry about us. Welcome back, Erika-san."
 hide erika_v001
 hide shion_v012
 with Dissolve(0.2)
 narrator 'I feel like throughout this entire vacation, even while I {i}meant{/i} to spend my free time in the rose garden, Erika-san has constantly been starting fights with me.'
 narrator "Erika-san's provocative attitude combined with the Sonozaki sisters' fighting over their paid visit..."
 narrator "I think I'll write in the questionnaire that this island would be better off reserved..."
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Erika-san, did you also inspect the lock to your room?'
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I do find it funny. I carelessly left my door unlocked until noon, and now I'm being cautious about yours."
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_526_door_open.wav'
 narrator 'Leaving behind that terribly cautious Erika-san, the rest of us entered our room.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v004 smile at mei_right
 show shion_v012 smile at mei_left
 with Dissolve(0.5)
 show shion_v012 smile at inactive
 show mion_v004 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Haaaah! Finally, I can take this off!'
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Aaahhh, I'm so tired! That does it for our photography trip!"
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show mion_v004 smile at inactive
 show shion_v012 smile at active
 show shion_v012 smile at jump_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hope you don't mind if I shower first♪"
 camera at screenshake_transform
 pause 0.0
 show shion_v012 smile at inactive
 show mion_v004 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Huhhhh?! I should go first since I was the one working hard and sweating my ass off!!'
 show mion_v004 odoroki at inactive
 show shion_v012 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'First come, first served♪ You can sweat there and listen to the running water in my shower.'
 play audio 'audio/sfx/SE_332_ls_fall.wav'
 show shion_v012 smile
 show shion_v012 smile:
  yanchor 1.0
  linear 0.16666666666666666 pos (-480,1200)
 pause 0.16666666666666666
 show shion_v012 smile:
  yanchor 1.0
  pos (-480,1200)
 pause 0.5
 play audio 'audio/sfx/SE_332_ls_fall.wav'
 show mion_v004 odoroki
 show mion_v004 odoroki:
  yanchor 1.0
  linear 0.16666666666666666 pos (-480,1200)
 pause 0.16666666666666666
 show mion_v004 odoroki:
  yanchor 1.0
  pos (-480,1200)
 hide shion_v012
 hide mion_v004
 with Dissolve(0.2)
 narrator 'Once again, the Sonozakis bicker like little children, throw off their clothes and enter the bathroom at the same time, completely naked...'
 narrator '...They say you forget about your sex when in the absence of the other.'
 narrator "I think I'll be a bit more careful, even when nobody is watching..."
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...That's a relief. There's nothing on my bed."
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 narrator 'I carefully turned over my pillow and looked under my bed. No sign of any ridiculous pranks.'
 show nao_v002 smile_close at mei_center
 with Dissolve(0.5)
 show nao_v002 smile_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I think I can sleep in peace... on this final night...'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 show black_cover as bg
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'KYAAAAAAAAAAAAAAA...!!!'
 play music "<loop 0>audio/bgm/BGM_QUEST7_COLLAB2.ogg"
 narrator "That was undoubtedly Erika's voice coming from the next room. The walls aren't very thick, so it was easy to realize... that it was a scream."
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'M-M-Mion-san, Shion-san! That scream came from next door...!!'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v008 sinken at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at inactive
 show mion_v008 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Huh? What's wrong...?"
 show mion_v008 sinken at inactive
 show shion_v007 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'A scream from next door... could that be Erika-san?'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide shion_v007
 hide mion_v008
 with Dissolve(0.2)
 show black_cover as bg
 play audio 'audio/sfx/SE_408_run.wav'
 narrator 'The concerned Sonozaki sisters acted fast, putting on bath towels and running into the hallway.'
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'There, Erika-san was sunken down on the floor and pointing towards the inside of her wide-open room.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Ahhhh... uwaaaaaa...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v008 sinken at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show mion_v008 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Are you alright?! What happened?!'
 show mion_v008 sinken at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'For that Erika-san to get... frightened as much as this...'
 hide nao_v002
 hide mion_v008
 with Dissolve(0.2)
 show shion_v007 sinken at mei_center
 with Dissolve(0.5)
 show shion_v007 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Is there something wrong inside your room?! I'm coming in!"
 hide shion_v007
 with Dissolve(0.2)
 narrator 'Shion-san gripped her stun gun tightly and leapt into the room.'
 narrator 'Wait a minute, she just ran out of the bathroom with a towel! Why does she have a stun gun...?! I give up...'
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2320.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 2.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show erika_v001 odoroki at chara_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...M-My bed... my bed has...'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v008 futeki at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show mion_v008 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle* ...Well, well, well... did they get ya?'
 show mion_v008 futeki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'This is... the same magic circle I saw on mine...'
 hide nao_v002
 hide mion_v008
 with Dissolve(0.2)
 show shion_v007 normal at mei_center
 with Dissolve(0.5)
 show shion_v007 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "There's no one in here or in the bathroom."
 hide shion_v007
 with Dissolve(0.2)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show erika_v001 odoroki at chara_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'This is... this is... hic... hic......'
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Erika-san was visibly upset.'
 narrator "No, thinking about it, this was a reasonable reaction... Erika-san must be on the culprit's side. And yet, a magic circle has mysteriously appeared inside her room."
 show erika_v001 odoroki at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Impossible, this couldn't really be... a witch's curse?"
 show erika_v001 odoroki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'E-Erika-san, calm down...'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator 'The provocative Erika-san now looked so frail and weak...'
 narrator 'The sight of her like this... was far more terrifying. Even I was frozen with fear...'
 show mion_v008 normal at mei_left
 show erika_v001 sinken at mei_right
 with Dissolve(0.5)
 show erika_v001 sinken at inactive
 show mion_v008 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Um... this morning, you said you didn't lock your door... right?"
 show mion_v008 normal at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Y-Yes, that's right... But after that, I made very sure to lock my door... nnh."
 hide mion_v008
 show shion_v007 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken at inactive
 show shion_v007 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "And at that time, you entered your room, right? You didn't find anything weird inside?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide shion_v007
 hide fade onlayer curtain
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Nothing at all! That would be impossible!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v008 normal at mei_right
 show shion_v007 normal at mei_left
 with Dissolve(0.5)
 show shion_v007 normal at inactive
 show mion_v008 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If that's the case, Erika-san, then when you left your door unlocked, there were no pranks left there at all."
 show mion_v008 normal at inactive
 show shion_v007 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'The crime was committed between the time the door was locked and the time it was opened, right?'
 hide shion_v007
 hide mion_v008
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...It looks just like the magic circle that was on my sheets, and it uses the same paint.'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v008 normal at mei_right
 show shion_v007 normal at mei_left
 with Dissolve(0.5)
 show shion_v007 normal at inactive
 show mion_v008 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yeah. It's just ordinary watercolor paint, if I'm right..."
 show mion_v008 normal at inactive
 show shion_v007 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...It's a trick where it's transparent at first, but as time passes, the stain starts to show up more and more."
 show shion_v007 normal at inactive
 show mion_v008 normal_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'As far as this crime goes... it could only have been committed immediately after opening the door.'
 hide shion_v007
 hide mion_v008
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Huh......?'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v007 normal at mei_left
 show erika_v001 odoroki at mei_right
 with Dissolve(0.5)
 show erika_v001 odoroki at inactive
 show shion_v007 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Erika-san. Please give us an honest answer, okay?'
 show shion_v007 normal at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "What? I'll tell you. Anything you want!"
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 narrator "As if we couldn't suspect that clever Erika-san... Even I could guess that right away..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show shion_v007 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show shion_v007 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...You're faking this, aren't you?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide shion_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "I had never seen such a look on Erika-san's face. Her eyes widened, and her expression was one of both shock and dumbfoundedness."
 call chapter_end
 jump event01_30_08