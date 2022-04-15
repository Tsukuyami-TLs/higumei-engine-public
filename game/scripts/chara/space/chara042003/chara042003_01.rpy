label chara042003_01:
 show black_background onlayer black
 $ event_store.current_event='chara042003'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara042003_01'
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
 show expression 'images/bg/AdvBg_591.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 show miyuki_v002 odoroki_close at mei_outerleft
 show miyuki_v002 odoroki_close at walk_transform:
  yanchor 1.0
  linear 0.6666666666666666 pos (480,1200)
 with Dissolve(0.5)
 pause 0.16666666666666663
 show miyuki_v002 odoroki_close:
  yanchor 1.0
  pos (480,1200)
 show miyuki_v002 odoroki_close at active
 show miyuki_v002 odoroki_close at deepbreath_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '*yaaawn*... Guu mawniih, Wehna.\nYou seem lively this... morniiing...'
 show rena_v002 odoroki at mei_right
 with Dissolve(0.5)
 show miyuki_v002 odoroki_close at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Good morning! Miyuki-chan...?\nHau, you seem very sleepy. I wonder if you got any sleep at all last night, at all last night?'
 hide rena_v002
 show nao_v002 sinken_close at mei_right
 with Dissolve(0.5)
 show miyuki_v002 odoroki_close at inactive
 show nao_v002 sinken_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "You don't have to worry about her, Rena-chan.\nMiyuki's like this because she lazed around watching movies all night... ugh."
 show nao_v002 sinken_close at inactive
 show miyuki_v002 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "I wasn't laaaziiinnn'... I thought I'd peruse them as references for play practice todaaay-... *yaawn*..."
 show miyuki_v002 fuan_close at nod_transform
 show miyuki_v002 fuan_close at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'And like I told you, you didn\'t have to watch until sunrise.\nAre you even aware of the phrase "getting your priorities backwards"?'
 hide miyuki_v002
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "A-Ahahaha... by the way, Rena-san, are those wrapped-up boxes you're carrying possibly lunch bentos?"
 hide nao_v002
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 smile at inactive
 show rena_v002 smile at active
 show rena_v002 smile at nod_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Yes. I thought everyone would get hungry after all that moving around, so I put my all into it~! Hau hau♪'
 hide kazuho_v002
 show nao_v002 smile_blush at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show nao_v002 smile_blush at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Thank you~! Just thinking about Rena-chan's delicious lunch makes it all the more worthwhileee♪"
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Same for you, right, Miyuki? You didn't even drink milk this morning, so you'll need to hold out until lunch... Miyuki?"
 hide rena_v002
 hide nao_v002
 with Dissolve(0.2)
 show miyuki_v002 normal_close at mei_center
 with Dissolve(0.5)
 show miyuki_v002 normal_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Zzz~...'
 hide miyuki_v002
 with Dissolve(0.2)
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Did... did she fall asleep standing up?\nWake up, Miyuki-chan! Won't it be dangerous if you fall down sleeping like that?!"
 show satoko_v002 odoroki at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Miyuki-san must be an awfully dextrous type to fall asleep like that.'
 hide kazuho_v002
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 odoroki at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. This special skill will help her if she ever gets told to go to stand in the hallway. Nipah~'
 hide satoko_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'A-Au au... I think it\'s more about making sure you don\'t do the "dumb" things that get you told to go stand in the hallway...'
 hide rika_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show nao_v002 fuan at active
 show nao_v002 fuan at deepbreath_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "*sigh*... Anyway, we're going to act out all of the scenes from top to bottom until dusk to make sure we're set. Let's do this cleanly and carefully so that no one gets hurt."
 hide hanyuu_v002
 show satoko_v002 futeki at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show satoko_v002 futeki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ohohohohoho, do leave it to me! As a future famous actress and contender for the Aodemy Award, a mere play will be a cinch!'
 hide nao_v002
 show miyuki_v002 normal_close at mei_left
 with Dissolve(0.5)
 show satoko_v002 futeki at inactive
 show miyuki_v002 normal_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Awfully long time since I heard someone say something being a cinch...zzz...'
 hide satoko_v002
 show kazuho_v002 odoroki at mei_right
 with Dissolve(0.5)
 show miyuki_v002 normal_close at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Sh-she doesn't miss punch lines even in a half-asleep state, huh...?"
 hide miyuki_v002
 show rena_v002 smile at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Ahahahaha. But for sure, I think the best scene is going to be the final battle between Keiichi-kun as the protagonist and Mii-chan as the Demon Queen. Hau, I'm really looking forward to it~♪"
 hide kazuho_v002
 show nao_v002 smile at mei_right
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "No matter how rigorous the practicing gets, those two make a perfect team, so there's probably no need for worry. Let's take great care not to overadmire them and get hurt doing-... what was that?"
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide rena_v002
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_541.png' as bg
 camera:
  pos (960, 510)
  zoom 1.3
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v002 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 play audio 'audio/sfx/SE_518_drum.wav'
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "LIKE! I! SAID! You don't get it, Kei-chan!\nYou don't get what makes sci-fi heroes charming, not at ALL!"
 hide mion_v002
 show keiichi_v002 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 play audio 'audio/sfx/SE_518_drum.wav'
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "{i}You're{/i} the one who doesn't get it, Mion!\nI'm {i}really{/i} getting tired of disagreeing with you!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v002 odoroki at mei_right
 with Dissolve(0.5)
 show mion_v002 odoroki at active
 show mion_v002 odoroki at jumping_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Wha-...? Y-You say that to me even though I've been stepping around glass shards for you...?!"
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Aah, now I'm mad! This means war!"
 show keiichi_v002 sinken at mei_left
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Fine by me; you'd better prepare yourself!"
 hide mion_v002
 hide keiichi_v002
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Wait... what's this all about? Why are Maebara-kun and Mion-san arguing so vehemently?!"
 show miyuki_v002 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v002 odoroki at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Stop it, Mion! You too, Maebara-kun!\nWhy the hell are they fighting when they just made up a minute ago?!'
 hide nao_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show shion_v002 normal at mei_center
 with Dissolve(0.5)
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah, it's okay, everyone. You don't need to worry...or rather, it's a waste of time to worry about it, so please don't."
 show rena_v002 odoroki at mei_left
 show shion_v002 normal
 show shion_v002 normal:
  yanchor 1.0
  linear 0.5 pos (1440,1200)
 with Dissolve(0.5)
 show shion_v002 normal:
  yanchor 1.0
  pos (1440,1200)
 show shion_v002 normal at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Sh-Shii-chan...? Why might Keiichi-kun and Mii-chan be fighting, be fighting?'
 show rena_v002 odoroki at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Well, to tell the truth...The protagonist and the Demon Queen have conflicting opinions over their weapons.'
 hide rena_v002
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "The protagonist's and Demon Queen's weapons...? \nUm, I don't get what you're saying here... could you explain?"
 show kazuho_v002 odoroki at inactive
 show shion_v002 normal_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Basically they're talking about whether to use swords or firearms.\nIncidentally, Kei-chan claims swords are better, while Sis..."
 hide shion_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show mion_v002 sinken at mei_right
 with Dissolve(0.5)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Swords are strong? Maybe just in a historical drama?\nIn a sci-fi world where weapons firing lasers and beams are the norm, guns are absolutely the way to go!'
 show keiichi_v002 sinken at mei_left
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "You just don't get it, Mion! It's not about being strong or weak; it's about looking epic!"
 show mion_v002 sinken at inactive
 show keiichi_v002 futeki_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "You saw that movie last night too, right? The coolness of that space knight fighting with a laser sword! If you didn't get chills from that, then you can't call yourself a man!"
 show keiichi_v002 futeki_close at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hahah, let that old-fashioned remark of male chauvinism jump out!\nYou know, you're the only boy in the club right now, Kei-chan.\nMaybe we should give you that 9-vs-1 octopus smack?"
 show mion_v002 futeki at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Uh... nah, my bad but that sounded wrong. \nThat expression was definitely not appropriate.'
 show mion_v002 futeki at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "A-...and besides, your favorite space sheriff's weapon he uses for his finishing blows is a light sword, isn't it?! Guns are just a sidearm. A sidearm! And they're obviously not as cool in stage plays either!"
 show keiichi_v002 sinken at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I told you we'd make do with stage lighting and sound effects!\nHow would you even make a laser sword look cool to the kids?\nBy using a lamp?"
 show mion_v002 sinken at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "We'd use the {b}Role Cards{/b} at times like that!\nDone right, it's totally possible to make a light sword that way!"
 show keiichi_v002 sinken at inactive
 show mion_v002 sinken at active
 show mion_v002 sinken at jumping_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "We can't do a dangerous performance like that in a play for kiiiids!!\nI didn't think you were such a blockhead, Kei-chan! Hmph!"
 show mion_v002 sinken at inactive
 show keiichi_v002 sinken_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Heh, same here! You're just as stubborn as always!"
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 show keiichi_v002 sinken_close at active
 show mion_v002 sinken at active
 Character('Keiichi and Mion',ctc="ctcArrow", ctc_position="fixed") 'Bleeeeeeeeeeehh!!'
 hide mion_v002
 hide keiichi_v002
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show shion_v002 normal at mei_center
 with Dissolve(0.5)
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...And that's what's going on. Does that help you understand the situation now?"
 hide shion_v002
 with Dissolve(0.2)
 show miyuki_v002 odoroki at mei_left
 with Dissolve(0.5)
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Uh... what? Are those two really getting worked up over something as {i}stupid{/i} as that...?'
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v002 odoroki at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Meep. It really is an unproductive, extremely low-level discussion.'
 hide miyuki_v002
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I wholeheartedly approved of them making up earlier... but it feels like their immaturity has skyrocketed since then.'
 hide rika_v002
 show kazuho_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-Ahahaha...'
 hide satoko_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show mion_v002 sinken at mei_right
 with Dissolve(0.5)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Since it's come to this, let's prove our arguments in real time. \nWhy don't we clash our ideas together in battle and decide whose side is right and whose side is wrong?"
 show keiichi_v002 futeki at mei_left
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show keiichi_v002 futeki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Heh... I see. It's like that fable we learned with the unstoppable force versus the immovable object. Hell yeah; let's go for it...!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide keiichi_v002
 hide fade onlayer curtain
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Now that that's settled... is everybody ready?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Eh... wh-what?'
 show keiichi_v002 sinken at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "This is a path we can't miss if we wanna make this play a hit... I'm counting on you guys!"
 show keiichi_v002 sinken at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'But... what exactly is that...?!'
 call chapter_end
 jump chara042003_02