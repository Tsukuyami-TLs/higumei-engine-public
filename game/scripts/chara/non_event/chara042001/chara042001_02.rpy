label chara042001_02:
 show black_background onlayer black
 $ event_store.current_event='chara042001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara042001_02'
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
 show expression 'images/bg/AdvBg_343.png' as bg
 show black_cover onlayer curtain as fade with Dissolve(0.0)
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...I said we would be careful, but how did this happen...?'
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kazuho_v002 fuan at inactive
 Character(' Delinquent A',ctc="ctcArrow", ctc_position="fixed") 'Whadjya say, bitch?!'
 show kazuho_v002 fuan at inactive
 Character(' Delinquent B',ctc="ctcArrow", ctc_position="fixed") 'Ya knock over a guy, then ya got an attitude?!'
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah, um...'
 hide kazuho_v002
 with Dissolve(0.2)
 show nao_v002 sinken at active
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'You guys tried to bump into me on purpose, and while I avoided it, you still made a show of falling over. You should quit with the false accusations.'
 show nao_v002 sinken at inactive
 Character(' Delinquent C',ctc="ctcArrow", ctc_position="fixed") 'Wuzzat, pipsqeak?!'
 hide nao_v002
 with Dissolve(0.2)
 show miyuki_v002 fuan at active
 show miyuki_v002 fuan at mei_left
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Um, well... you see...'
 show miyuki_v002 fuan at inactive
 show nao_v002 normal at active
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "What, you're not afraid, are you?"
 show nao_v002 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "No, it's the opposite. I'm a little impressed.\nThis kind of Showa-esque scenario is really playing out, huh~?"
 show miyuki_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's not Showa-{i}esque{/i}, this IS Showa."
 show nao_v002 normal at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Oh, I guess you're right. Mmm, but now what do we do?\nWe can't use {b}Role Cards{/b} against regular people."
 show nao_v002 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ah, I know: you two go head on home.'
 hide nao_v002
 show miyuki_v002 smile at inactive
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Eh...? What are you going to do alone, Miyuki-chan?'
 show kazuho_v002 odoroki at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Oh, don't worry.\nI'll go easy on 'em with just one per guy."
 show miyuki_v002 smile at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wh-what do you mean by "just one"? Just one judo throw?'
 show kazuho_v002 odoroki at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'One bone☆'
 show miyuki_v002 smile at inactive
 show kazuho_v002 sinken at active
 show kazuho_v002 sinken at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "D-Don't! You can't break their bones!"
 show kazuho_v002 sinken at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Whaat, why not?\nWe're not gonna get away from this many people unless I break at least one bone, y'know?"
 hide miyuki_v002
 hide kazuho_v002
 with Dissolve(0.2)
 Character(' Delinquent A',ctc="ctcArrow", ctc_position="fixed") "Whaa? Shuddup'n listen'a me! The fuck ya bitches think ya are?!"
 show miyuki_v002 normal at active
 show miyuki_v002 normal at mei_center
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Mmm, well, could you let us go home?'
 hide miyuki_v002
 with Dissolve(0.2)
 Character(' Delinquent B',ctc="ctcArrow", ctc_position="fixed") "Iyain lettin' ya go noplace!"
 Character(' Delinquent C',ctc="ctcArrow", ctc_position="fixed") 'Pay up!'
 show nao_v002 fuan at active
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '*sigh*... what for?'
 show nao_v002 fuan at inactive
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Umm, that's... \nWe haven't done anything that's worth paying for, so I'll just make my way-..."
 hide nao_v002
 hide kazuho_v002
 with Dissolve(0.2)
 Character(' Delinquent A',ctc="ctcArrow", ctc_position="fixed") "Ya been fuckin' wit us up til now, so make my way my ass!"
 stop music fadeout 1.0
 play audio 'audio/sfx/SE_408_run.wav'
 show kazuho_v002 fuan at inactive
 show kazuho_v002 fuan at mei_right
 show miyuki_v002 sinken at active
 show miyuki_v002 sinken at mei_center
 show miyuki_v002 sinken:
  yanchor 1.0
  linear 0.5 pos (1140,1200)
 with Dissolve(0.5)
 show miyuki_v002 sinken:
  yanchor 1.0
  pos (1140,1200)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Kazuho, watch out!'
 show miyuki_v002 sinken at inactive
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...*gasp*...!'
 call wipeout_routine
 stop sound
 show expression 'images/card/Card_042001.png' as bg
 hide miyuki_v002
 hide kazuho_v002
 with Dissolve(0.2)
 play music "<loop 3.53>audio/bgm/BGM_EVENT7.ogg"
 show black_cover onlayer curtain as fade with Dissolve(0.016666666666666666)
 call wipein_routine
 show white_cover onlayer curtain as fade with Dissolve(0.25)
 Character(' Masked Hero',ctc="ctcArrow", ctc_position="fixed") 'Doryaah!!'
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_101_hit_strike1.wav'
 Character(' Delinquent A',ctc="ctcArrow", ctc_position="fixed") 'Guhoh!'
 Character(' Delinquent B',ctc="ctcArrow", ctc_position="fixed") 'Wh-wha?! What just happened?!'
 Character(' Delinquent A',ctc="ctcArrow", ctc_position="fixed") "S-Some shithead in a mask jus' hit me...!"
 Character(' Masked Hero',ctc="ctcArrow", ctc_position="fixed") "Shithead in a mask, huh... that's the first thing you come up with?\nHonestly, you need to come up with some better descriptions."
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh, ah, is that...?'
 Character(' Masked Hero',ctc="ctcArrow", ctc_position="fixed") "It's alright now, so run ahead and leave this to me!"
 Character(' Masked Hero',ctc="ctcArrow", ctc_position="fixed") 'Heheh, I always wanted to say that at least once~!'
 Character(' Delinquent B',ctc="ctcArrow", ctc_position="fixed") "Ya got some nerve ta fuck wit' us!"
 Character(' Delinquent C',ctc="ctcArrow", ctc_position="fixed") "Get 'em!"
 Character(' Masked Hero',ctc="ctcArrow", ctc_position="fixed") 'Thanks for the cliché catchphrases, lowlives!\nThis is gonna be fun!'
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_343.png' as bg
 call wipein_routine
 show miyuki_v002 odoroki at active
 show miyuki_v002 odoroki at mei_left
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...Ah! This isn't the time to be getting distracted!"
 show miyuki_v002 odoroki at inactive
 show nao_v002 sinken at active
 show nao_v002 sinken at mei_right
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Let's go...!\nHero! We'll be waiting for you in the spot where we first met!"
 call wipeout_routine
 hide miyuki_v002
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/card/Card_042001.png' as bg
 call wipein_routine
 Character(' Masked Hero',ctc="ctcArrow", ctc_position="fixed") "Yeah, I'll catch up with you later!"
 pause 1.6666666666666667
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_343.png' as bg
 call wipein_routine
 show kazuho_v002 odoroki at inactive
 show kazuho_v002 odoroki at mei_right
 show miyuki_v002 sinken at active
 show miyuki_v002 sinken at mei_center
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Let's go, Kazuho!"
 show miyuki_v002 sinken at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'O-Okay!'
 play audio 'audio/sfx/SE_511_sand_run.wav'
 hide kazuho_v002
 hide miyuki_v002
 call chapter_end
 jump chara042001_03