label chara072008_03:
 show black_background onlayer black
 $ event_store.current_event='chara072008'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072008_03'
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
 show expression 'images/bg/AdvBg_262.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_501_crow.wav'
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_172.png' as bg
 play music "<loop 1.5>audio/bgm/BGM_EVENT4.ogg"
 call wipein_routine
 show hanyuu_v001 fuan at mei_right
 show rika_v001 fuan_close at mei_left
 with Dissolve(0.5)
 show hanyuu_v001 fuan at inactive
 show rika_v001 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v001 fuan_close at inactive
 show hanyuu_v001 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Um... Rika. The day is almost over. Shouldn't we head home?"
 show hanyuu_v001 fuan at inactive
 show rika_v001 fuan_close at active
 show rika_v001 fuan_close at chara_shake_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...ngh...'
 show rika_v001 fuan_close at inactive
 show hanyuu_v001 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "...If you need me, please call me whenever.\nI'll come rushing over to you right away..."
 play audio 'audio/sfx/SE_530_walk_one.wav'
 show hanyuu_v001 fuan at walk_transform
 show hanyuu_v001 fuan at walk_transform:
  yanchor 1.0
  linear 0.5 pos (2400,1200)
 pause 0.5
 show hanyuu_v001 fuan:
  yanchor 1.0
  pos (2400,1200)
 hide hanyuu_v001
 with Dissolve(0.2)
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v001
 hide fade onlayer curtain
 show rika_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...I should have explained properly. I really wasn't planning on doing anything mean..."
 show rika_v001 fuan at active
 show rika_v001 fuan at chara_shake_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Satoko's an idiot...\nBut I'm the bigger one... gh..."
 stop music fadeout 0.5
 show rika_v001 fuan at inactive
 Character('????',ctc="ctcArrow", ctc_position="fixed") "...True.\nIt's obvious that someone would get down in the dumps after messing up a big surprise like that."
 show rika_v001 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Eh...?'
 call wipeout_routine
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 stop sound
 show expression 'images/bg/AdvBg_142.png' as bg
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 call wipein_routine
 show rika_v001 odoroki at mei_left
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show rika_v001 odoroki at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I grabbed this leaflet they had set up at the storefront.\nRika... so this was your goal when you bought the Anfeya soy sauce?'
 show nao_v001 normal at inactive
 show rika_v001 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah-, Nao...?!'
 hide nao_v001
 show rena_v001 smile_blush at mei_right
 with Dissolve(0.5)
 show rika_v001 odoroki at inactive
 show rena_v001 smile_blush at active
 show rena_v001 smile_blush at chara_shake_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Chopsticks, bowls and plates... a full matching dinner set.\nAnd plus... hau~, this Mr. Beary print is soo kyuute~♪'
 hide rena_v001
 show kazuho_v001 smile at mei_right
 with Dissolve(0.5)
 show rika_v001 odoroki at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "The special prize during their promotions.\nYou were thinking to enter the raffle with this, weren't you, Rika-chan?"
 show kazuho_v001 smile at inactive
 show rika_v001 fuan at active
 show rika_v001 fuan at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Yes, I was.\nI thought Satoko would have been happy if I won.'
 hide kazuho_v001
 show miyuki_v001 normal at mei_right
 with Dissolve(0.5)
 show rika_v001 fuan at inactive
 show miyuki_v001 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "You should have been upfront then.\nActing all weird and making people suspicious doesn't make it worth it."
 show miyuki_v001 normal at inactive
 show rika_v001 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Since it was a raffle, I thought Satoko would be disappointed if I got her hopes up and I ended up losing, but...'
 show miyuki_v001 normal at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'During that heated exchange, I started thinking, "Why can\'t she understand me even though we\'ve lived together for so long?"...'
 show miyuki_v001 normal at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'And I accidentally got really angry because of it, so it turned into a fight...'
 hide miyuki_v001
 show rena_v001 normal at mei_right
 with Dissolve(0.5)
 show rika_v001 fuan at inactive
 show rena_v001 normal at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'But... you regret it now, right, Rika-chan?'
 show rena_v001 normal at inactive
 show rika_v001 fuan_close at active
 show rika_v001 fuan_close at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Yes, I do. ...But since it's been so long since I've made Satoko that mad..."
 show rena_v001 normal at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I didn't know how to apologize to her, and then it ended up like this..."
 hide rena_v001
 show kazuho_v001 smile at mei_right
 with Dissolve(0.5)
 show rika_v001 fuan at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I don't think you have to worry, Rika-chan.\nThe fact that you're so close to each other might have made you overthink, so it became difficult to apologize..."
 show rika_v001 fuan at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "But when you feel sorry for what you did, you should convey that to each other properly... so isn't that about enough for you two?"
 show rika_v001 fuan at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Don't you agree, Satoko-chan?"
 hide kazuho_v001
 show satoko_v001 normal at mei_right
 with Dissolve(0.5)
 show rika_v001 fuan at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 show satoko_v001 normal at inactive
 show rika_v001 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'M-Meep? S-Satoko...?'
 show rika_v001 odoroki at inactive
 show satoko_v001 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I'm so sorry, Rika.\nI never realized last night how much thought you put in for me..."
 show rika_v001 odoroki at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If you really, really think about it, there's no way Rika could have bought a different soy sauce for no reason. It's embarrassing for me not to have come to that realization..."
 show satoko_v001 fuan at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. That's not true at all. I thought too hard about wanting to surprise you and ended up acting weird and secretive."
 show satoko_v001 fuan at inactive
 show rika_v001 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "What's more, I got angry and said some things that shouldn't have been said... so the one who should apologize here is me."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show rika_v001 fuan_close at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "No, I'm more sorry. It goes without saying that the way I spoke... was..."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show satoko_v001 normal at inactive
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep, even mine was...'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show rika_v001 normal at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.4
 pause 0.5
 show satoko_v001 normal at inactive
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v001 normal at inactive
 show satoko_v001 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '......*chuckle*.'
 show satoko_v001 smile at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ahaha...'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 hide rika_v001
 hide satoko_v001
 with Dissolve(0.2)
 show mion_v001 smile at mei_center
 with Dissolve(0.5)
 show mion_v001 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yep, yep, now this settles it.\nSo, Satoko, why don't you and Rika make today's dinner together?"
 hide mion_v001
 with Dissolve(0.2)
 show rika_v001 smile at mei_left
 show satoko_v001 smile at mei_right
 with Dissolve(0.5)
 show rika_v001 smile at inactive
 show satoko_v001 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yes, of course. May I ask the same of you, Rika?'
 show satoko_v001 smile at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Yes, I would like to. I'll put all of my effort in to make us a super delicious meal. Nipah★"
 hide satoko_v001
 hide rika_v001
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1752.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v016 smile at mei_right
 show rika_v017 normal at mei_left
 with Dissolve(0.5)
 show rika_v017 normal at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...We never got that prize in the end. But I didn't think of it as a complete loss."
 show rika_v017 normal at inactive
 show satoko_v016 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Because the feelings that you shared with me then... made me incredibly happy.'
 show satoko_v016 smile_close at inactive
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Satoko...'
 show rika_v017 normal at inactive
 show satoko_v016 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Uh... huh? What made me bring this topic up again?'
 show rika_v017 normal at inactive
 show satoko_v016 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'If I remember correctly, I was... blaming you for hiding stuff from me at times, but... huhhh...?'
 show satoko_v016 fuan at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...I'm sorry, Satoko.\nIt's a bad habit of mine to assume things are already clear, so I don't feel the need to convey them."
 show satoko_v016 fuan at inactive
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I'll be more open now. And I'll continue trusting in you too.\nNow and... forever more."
 show rika_v017 normal at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "......Let's head back, Rika. We'll miss the dorm curfew if we stay too late."
 show satoko_v016 smile at inactive
 show rika_v017 smile at active
 show rika_v017 smile at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Yeah, you're right. Let's go, together."
 hide rika_v017
 hide satoko_v016
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/card/Card_072008.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Okay... my hair is set, my textbooks and notebooks have been ready since last night, and now...'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah, look at the time.\nI planned to get up extra early today, but it ended up being pretty nice timing before I realized it.'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "By the way, Satoko did say that she was dangerously close to being late yesterday... I'll go check on her."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1761.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Just as I thought, she's still asleep.\nSatoko, if you don’t get up, we'll be late."
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Hmmnhhnn... Rika, just a bit longer...\n1 minute... no, 3 minutes... 30...'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Oh, c'moonn, you just keep adding on more tiiime...\nIf you stay asleep like that, you'll be late. Do you want to get stuck in supplementary class again after school?"
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'O-Okay, I got it... hnmmnn...'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Wait, Rika? Why are you in my dorm?'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '*giggle*... good morning, Satoko.\n I was worried about you, so I came to wake you up.'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Hurry up and wash your face. I'll help fix your hair for you."
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "U-... uh-huh... I'm alright with that. Please wait for a few minutes."
 narrator '............'
 show satoko_v016 normal_close at mei_center
 with Dissolve(0.5)
 show satoko_v016 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "(...I feel like I was having a weird dream, but I've forgotten most of it. It's just...)"
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "(I want to try putting more trust in Rika now...\nThat's how I feel...)"
 call chapter_end
 
 $ persistent.chara072008_done = True
 return