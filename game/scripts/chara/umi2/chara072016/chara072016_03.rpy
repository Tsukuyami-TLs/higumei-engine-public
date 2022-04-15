label chara072016_03:
 show black_background onlayer black
 $ event_store.current_event='chara072016'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072016_03'
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
 show expression 'images/bg/AdvBg_511.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") 'My... my......'
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") 'MY MAAASSTTEEEERRRRRRRRRR!!!!'
 window hide None
 play audio 'audio/sfx/SE_304_ls_run.wav'
 pause 0.5
 show erika_v001 smile
 show erika_v001 smile:
  yanchor 1.0
  linear 0.5 pos (-480,1200)
 pause 0.5
 show erika_v001 smile:
  yanchor 1.0
  pos (-480,1200)
 hide erika_v001
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show rika_v023 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v023 odoroki at active
 show rika_v023 odoroki at jumping_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'M-me-eep?!'
 hide rika_v023
 with Dissolve(0.2)
 show miyuki_v002 odoroki at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Woah, this weirdo just turns around and runs full blast at Rika-chan?!'
 show miyuki_v002 odoroki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ruuun, Rikaaa!'
 hide nao_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_outerright
 show rika_v023 odoroki at mei_left
 with Dissolve(0.5)
 show erika_v001 smile
 show erika_v001 smile:
  yanchor 1.0
  linear 0.16666666666666666 pos (1440,1200)
 pause 0.16666666666666666
 show erika_v001 smile:
  yanchor 1.0
  pos (1440,1200)
 show rika_v023 odoroki at inactive
 show erika_v001 smile at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") 'MAAAASSSTEEEERRRRRRRRRR!!!'
 play audio 'audio/sfx/SE_5037_getup.wav'
 pause 1.0
 show erika_v001 smile at chara_shake_transform
 show erika_v001 smile:
  yanchor 1.0
  linear 0.5 pos (1440,1320)
 pause 0.5
 show erika_v001 smile:
  yanchor 1.0
  pos (1440,1320)
 hide rika_v023
 hide erika_v001
 with Dissolve(0.2)
 show miyuki_v002 odoroki at mei_center
 with Dissolve(0.5)
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'W-, and then she slides into a kneeling positioooon?!'
 hide miyuki_v002
 with Dissolve(0.2)
 show rika_v023 fuan at mei_left
 show erika_v001 smile at mei_right
 with Dissolve(0.5)
 show erika_v001 smile at inactive
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'W-What...?'
 show rika_v023 fuan at inactive
 show erika_v001 odoroki at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") 'W-w-w-why ever would you be here...?\nN-No, it was tactless of me to have asked!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 show rika_v023 fuan at inactive
 show erika_v001 smile at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") 'My master, you have blessed me, Erika Furudo, with your humble visit to oversee my activities!!'
 show rika_v023 fuan at inactive
 show erika_v001 smile at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") "Aah, I'm so honored, so deeply emotional to be able to expect you to come here...! "
 hide erika_v001
 hide rika_v023
 with Dissolve(0.2)
 window hide None
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show miyuki_v002 fuan at mei_left
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Erika, Furudo-san...? Nao, is that familiar to you?'
 show miyuki_v002 fuan at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Not even close. I don't even think I want to be familiar with that weirdo."
 hide miyuki_v002
 with Dissolve(0.3)
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan_close at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "R-Right... But it looks like she's acquainted with Rika-chan too."
 hide nao_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show rika_v023 fuan at mei_center
 with Dissolve(0.5)
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Me-Meep...?'
 hide rika_v023
 with Dissolve(0.2)
 show miyuki_v002 normal at mei_center
 with Dissolve(0.5)
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Wait, but... \nDoesn't her baffled look say otherwise?"
 hide miyuki_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show rika_v023 fuan at mei_left
 with Dissolve(0.5)
 show rika_v023 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'At any rate, my master, do tell why you would be in this Chiester Sisters outfit as you are right now?'
 show rika_v023 fuan at inactive
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "...H-, could it be that you're cosplaying as someone? I have overheard that it's all the rage to arrange an outfit using the clothes of commoners!"
 camera:
  parallel:
   linear 0.16666666666666666 pos (960, 540)
  parallel:
   linear 0.16666666666666666 zoom 1.3
 show rika_v023 fuan at inactive
 show erika_v001 smile at active
 show erika_v001 smile at jump_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "That's my master! Your face and body are perfect! No matter what clothes you have on, you wear it ravishingly!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 smile at inactive
 show rika_v023 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Um, I've been telling you I'm Rika Furude..."
 show rika_v023 fuan_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Rika Furude... Furuderika... ah-, oh... I see! So that was the idea behind it!'
 show erika_v001 normal at inactive
 show rika_v023 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep?!'
 hide rika_v023
 hide erika_v001
 with Dissolve(0.2)
 show battler_v001 normal at mei_left
 show keiichi_v002 normal at mei_right
 with Dissolve(0.5)
 show keiichi_v002 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hey, what's up, what's up, what's all this ruckus?"
 show battler_v001 normal at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "What happened? ...Wait, who's this person kneeled up in front of Rika-chan?"
 hide keiichi_v002
 hide battler_v001
 with Dissolve(0.2)
 show kazuho_v002 normal at mei_center
 with Dissolve(0.5)
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah, Maebara-kun, Battler-san! Do either of you know an Erika Furudo?'
 hide kazuho_v002
 with Dissolve(0.2)
 show battler_v001 fuan_close at mei_left
 show keiichi_v002 fuan at mei_right
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Who?'
 show battler_v001 fuan_close at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Nah... but why is this Furudo-san kneeling in front of Rika-chan?'
 hide battler_v001
 with Dissolve(0.3)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "We have no idea, but it looks like she's mistaken Rika for someone else."
 hide keiichi_v002
 hide nao_v002
 with Dissolve(0.2)
 show rika_v023 sinken at mei_left
 show erika_v001 smile at mei_right
 with Dissolve(0.5)
 show erika_v001 smile at inactive
 show rika_v023 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "L-Like I said, I'm someone else...!"
 show rika_v023 sinken at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Do rest assured, my master. I, Erika Furudo, have properly grasped the situation at hand!'
 hide erika_v001
 hide rika_v023
 with Dissolve(0.2)
 show nao_v002 sinken at mei_left
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...That pervert hasn't grasped a single thing."
 show nao_v002 sinken at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "P-Pervert...? Nao-chan, isn't that a little too much...?"
 hide nao_v002
 with Dissolve(0.3)
 show miyuki_v002 normal_close at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show miyuki_v002 normal_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, we wanted her to go home right away with the Nao thing, but now it's looking like going home for her means something totally different."
 show miyuki_v002 normal_close at inactive
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'For Rika-chan to get overwhelmed like that...!\nWhat should we do? What {i}could{/i} we do...?!'
 hide kazuho_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show battler_v001 smile at mei_left
 show keiichi_v002 normal at mei_right
 with Dissolve(0.5)
 show keiichi_v002 normal at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Oh, right. I just remembered something good.'
 show keiichi_v002 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Keiichi, got a minute?'
 show battler_v001 normal at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide keiichi_v002
 hide battler_v001
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 smile at mei_right
 show rika_v023 fuan at mei_left
 with Dissolve(0.5)
 show rika_v023 fuan at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'My master, why would you be here? Could you have had an urgent order for me?'
 show rika_v023 fuan at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'In that case, I, Erika Furudo, will traverse lands, water, even hell...!!'
 show erika_v001 smile at inactive
 show rika_v023 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I'm, I'm telling you...!"
 hide erika_v001
 with Dissolve(0.3)
 show keiichi_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v023 sinken at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Ah, excuse me a sec. Rika-chan, can you lend me your ear for a bit?'
 show keiichi_v002 normal at inactive
 show rika_v023 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep?'
 window hide None
 show keiichi_v002 normal
 show keiichi_v002 normal:
  yanchor 1.0
  linear 0.5 pos (960,1200)
 pause 0.5
 show keiichi_v002 normal:
  yanchor 1.0
  pos (960,1200)
 hide rika_v023
 hide keiichi_v002
 with Dissolve(0.2)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "You, what are you doing?! My master's ears are, no, ah, AAAH! Y-Your breath is TOUCHING HER...!"
 hide erika_v001
 with Dissolve(0.2)
 show rika_v023 fuan at mei_left
 show keiichi_v002 smile at mei_center
 with Dissolve(0.5)
 show keiichi_v002 smile at inactive
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Is that really okay?'
 show rika_v023 fuan at inactive
 show keiichi_v002 normal_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Yeah.'
 hide keiichi_v002
 hide rika_v023
 with Dissolve(0.2)
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 show erika_v001 sinken at updown_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'You menial! Shut your mouth this instant...!'
 stop music fadeout 1.0
 hide erika_v001
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/card/Card_072016.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play music "<loop 3.53>audio/bgm/BGM_EVENT7.ogg"
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...E-Erika Furudo!'
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Yes, ma'am!"
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'You have done well to see through my lies. You are to be praised. I have come to give you an order.'
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Pr-prai... ah, aaaahh! W-What joy...!'
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Hm? An order?'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Yes... th-that's right. From here on out, you are to..."
 camera at screenshake_transform
 pause 0.0
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...work as a part time employee at an inn!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_511.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 odoroki at mei_right
 show rika_v023 sinken at mei_left
 with Dissolve(0.5)
 show rika_v023 sinken at inactive
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Wh-... what is that? Part time... employee?'
 show erika_v001 odoroki at inactive
 show rika_v023 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Is that undesireable for you? Will you not hear out my order?'
 show erika_v001 odoroki at inactive
 show rika_v023 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'If so, then you are to leave at once! *spits*'
 show rika_v023 sinken_close at inactive
 show erika_v001 odoroki at active
 show erika_v001 odoroki at jumping_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I-I would never intend to feel that way!'
 show erika_v001 odoroki at inactive
 show rika_v023 futeki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'So, that is your order. You will work as hard as you can!'
 show rika_v023 futeki at inactive
 show erika_v001 smile at active
 show erika_v001 smile at nod_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Yes, my master!!'
 stop music fadeout 1.0
 window hide None
 call wipeout_routine
 hide rika_v023
 hide erika_v001
 with Dissolve(0.2)
 pause 1.0
 stop sound
 show expression 'images/bg/AdvBg_2471.png' as bg
 call wipein_routine
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_304_ls_run.wav'
 show erika_v001 futeki at active
 show erika_v001 futeki:
  yanchor 1.0
  linear 0.5 pos (2400,1200)
 pause 0.5
 show erika_v001 futeki:
  yanchor 1.0
  pos (2400,1200)
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Uooooooohhh!!'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 odoroki at mei_left
 show rena_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rena_v002 odoroki at inactive
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Amazing. She's carrying away an uncountable amount of futons in one sitting?"
 show mion_v002 odoroki at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... five people might be able to carry all of that. And with that kyute outfit on too...'
 hide mion_v002
 with Dissolve(0.3)
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show rena_v002 odoroki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I wonder if it's hard to move in."
 hide rena_v002
 with Dissolve(0.3)
 show satoko_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "She hasn't changed clothes or anything?"
 hide nao_v002
 with Dissolve(0.3)
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 normal at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'We tried to get her to for the time being, but she kept insisting, "Wearing discourteous clothes in front of my master is unacceptable."...'
 hide satoko_v002
 hide shion_v002
 with Dissolve(0.2)
 show rika_v023 sinken at mei_center
 with Dissolve(0.5)
 show rika_v023 sinken at active
 show rika_v023 sinken at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Slack off and it's punishment for you!"
 hide rika_v023
 with Dissolve(0.2)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_304_ls_run.wav'
 show erika_v001 smile at active
 show erika_v001 smile:
  yanchor 1.0
  linear 0.25 pos (2400,1200)
 pause 0.25
 show erika_v001 smile:
  yanchor 1.0
  pos (2400,1200)
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Yes, ma'am, right away!!"
 hide erika_v001
 with Dissolve(0.2)
 show kazuho_v002 odoroki at mei_left
 show satoko_v002 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v002 odoroki at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah, she's speeding up again."
 show kazuho_v002 odoroki at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Rika, you're commanding that person quite well..."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide satoko_v002
 hide kazuho_v002
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show miyuki_v002 fuan at mei_right
 show rika_v023 fuan at mei_left
 with Dissolve(0.5)
 show rika_v023 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Rika-chan, are you okay?'
 show miyuki_v002 fuan at inactive
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Y-Yeah...'
 show miyuki_v002 fuan at inactive
 show rika_v023 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But I'm not doing anything, so I'm getting really tired."
 show rika_v023 fuan_close at inactive
 show miyuki_v002 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "That's boredom... thank you for your hard work. I'll give you a shoulder rub after, yeah?"
 hide rika_v023
 hide miyuki_v002
 with Dissolve(0.2)
 show akasaka_v001 smile at mei_center
 with Dissolve(0.5)
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Hey! It's pretty lively here, huh?"
 hide akasaka_v001
 with Dissolve(0.2)
 show rika_v023 odoroki at mei_left
 show miyuki_v002 odoroki at mei_right
 with Dissolve(0.5)
 show miyuki_v002 odoroki at inactive
 show rika_v023 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'A-Akasaka...?!'
 show rika_v023 odoroki at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Eh... w-why are you here?'
 hide miyuki_v002
 hide rika_v023
 with Dissolve(0.2)
 show akasaka_v001 smile_close at mei_center
 with Dissolve(0.5)
 show akasaka_v001 smile_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'I came to help a bit with the cleanup work for the debris. I heard that everyone was helping out here.'
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ah, Rika-chan, why are you in those clothes again?'
 hide akasaka_v001
 with Dissolve(0.2)
 show rika_v023 fuan at mei_center
 with Dissolve(0.5)
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep... it's embarrassing, so I don't want you to look at me too closely, okay?"
 hide rika_v023
 with Dissolve(0.2)
 show miyuki_v002 fuan at mei_left
 show akasaka_v001 smile at mei_right
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Da-... A-Akasaka-san?'
 show miyuki_v002 fuan at inactive
 show akasaka_v001 odoroki at active
 show akasaka_v001 odoroki at jump_transform
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "W-Woah, don't look at me like that! I was just... thinking how cute it was."
 show miyuki_v002 fuan at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'On top of that, it looks like clothes from a police group. I think it suits you a lot!'
 hide miyuki_v002
 with Dissolve(0.3)
 show rika_v023 smile at mei_left
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show rika_v023 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Th-thank you...'
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide akasaka_v001
 hide rika_v023
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play music "<loop 0>audio/bgm/BGM_BATTLE1_hiru.ogg"
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'N-NOOOOOOOOOOOOOOOOO?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show akasaka_v001 fuan at mei_center
 with Dissolve(0.5)
 show akasaka_v001 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Wh-what's up?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide akasaka_v001
 hide fade onlayer curtain
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'My master, who is this man?! Is he suspicious? A hoodlum?! AN ENEMY?!'
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Please do not fret, for I, as a comrade, can assure that my master will not have to use her hands once!'
 play audio 'audio/sfx/SE_326_ls_spacestop.wav'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I'LL GET AT HIS THROAT THIS INSTAAAANT!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show akasaka_v001 odoroki at mei_center
 with Dissolve(0.5)
 show akasaka_v001 odoroki at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Huh? Wha-?'
 hide akasaka_v001
 with Dissolve(0.2)
 show miyuki_v002 odoroki at mei_right
 show rika_v023 fuan at mei_left
 with Dissolve(0.5)
 show rika_v023 fuan at inactive
 show miyuki_v002 odoroki at active
 show miyuki_v002 odoroki at updown_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'W-Wait wait wait waaaait!!'
 show miyuki_v002 odoroki at inactive
 show rika_v023 fuan at active
 show rika_v023 fuan at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep! This person isn't like that!!"
 stop music fadeout 1.0
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide rika_v023
 hide miyuki_v002
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show hanyuu_v002 odoroki at mei_center
 with Dissolve(0.5)
 show hanyuu_v002 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'A-Au au au...'
 hide hanyuu_v002
 with Dissolve(0.2)
 show mion_v002 normal at mei_center
 with Dissolve(0.5)
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "She's an issue at times, but once she stops working... it's like ten people or more stop working, huh?"
 hide mion_v002
 with Dissolve(0.2)
 show keiichi_v002 smile at mei_left
 show battler_v001 smile at mei_right
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") '"Won\'t she start listening if she became her master and ordered her around?", was what Battler asked me. Turns out his strategy was crazy effective.'
 show keiichi_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Wasn't it you who thought of how to word it, though, Keiichi? I think you brought the wording to the next level."
 hide keiichi_v002
 with Dissolve(0.3)
 show rena_v002 odoroki at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... but what an incredible effect.'
 show rena_v002 odoroki at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I figured this would make an impact on her... but honestly, I'm not sure why."
 hide rena_v002
 with Dissolve(0.3)
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Well, it definitely did have quite the effect, but...'
 show battler_v001 normal at inactive
 show satoko_v002 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Wouldn't it be best to let the truth out? Rika isn't that person's master."
 hide battler_v001
 with Dissolve(0.3)
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Wouldn't it be more peaceful if we left it as is?"
 hide nao_v002
 with Dissolve(0.3)
 show shion_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan_close at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If we do that, though, don't you think that person will always be glued to Rika-chama?"
 show shion_v002 fuan at inactive
 show satoko_v002 fuan at active
 show satoko_v002 fuan at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Th-that suffering won't be tolerated one bit!"
 show shion_v002 fuan at inactive
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "We won't be able to have peace of mind being together with such a noisy person from morning all the way til night!!"
 hide shion_v002
 with Dissolve(0.3)
 show kazuho_v002 fuan_close at mei_right
 with Dissolve(0.5)
 show satoko_v002 sinken at inactive
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Yeah, that'd be terrible..."
 hide kazuho_v002
 with Dissolve(0.3)
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 sinken at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'I understand that feeling, Satoko-chan. But... hau...'
 hide satoko_v002
 hide rena_v002
 with Dissolve(0.2)
 show keiichi_v002 normal at mei_left
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'How are we gonna get her to go home?'
 show keiichi_v002 normal at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...What do we do?'
 hide battler_v001
 hide keiichi_v002
 with Dissolve(0.2)
 show hanyuu_v002 normal at mei_center
 with Dissolve(0.5)
 show hanyuu_v002 normal at active
 show hanyuu_v002 normal at jump_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'D-Do your best, Rikaa! You have my support!!'
 hide hanyuu_v002
 with Dissolve(0.2)
 show rika_v023 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show rika_v023 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Erika.'
 show rika_v023 normal at inactive
 show erika_v001 normal at active
 show erika_v001 normal at nod_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Yes, what ever could it be, my master?'
 camera:
  parallel:
   linear 0.3333333333333333 pos (960, 540)
  parallel:
   linear 0.3333333333333333 zoom 1.3
 pause 0.3333333333333333
 show erika_v001 normal at inactive
 show rika_v023 futeki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Tonight, I'm feeling like eating kimchi. Prepare it extra spicy!"
 show rika_v023 futeki at inactive
 show erika_v001 smile at active
 show erika_v001 smile at updown_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Yes, ma'am! I will positively present for you the spiciest kimchi you will ever lay your tastebuds on!!"
 window hide None
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide rika_v023
 hide fade onlayer curtain
 show hanyuu_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show hanyuu_v002 odoroki at active
 show hanyuu_v002 odoroki at chara_shake_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'H-How could this beee~~?!'
 call chapter_end
 
 $ persistent.chara072016_done = True
 return