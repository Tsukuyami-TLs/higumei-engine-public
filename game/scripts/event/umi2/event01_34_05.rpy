label event01_34_05:
 show black_background onlayer black
 $ event_store.current_event='umi2'
 $ event_store.current_progress=1
 $ event_store.current_chapter='event01_34_05'
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
 show expression 'images/bg/AdvBg_993.png' as bg
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB3.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_5055_bath.wav'
 narrator 'As we came back to the inn and headed towards the spring area, we were greeted with white steam and the scent of the hot spring.'
 show miyuki_v002 smile_close at mei_left
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show miyuki_v002 smile_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Haaah... The hot water is seeping into my exhausted muscles...'
 show miyuki_v002 smile_close at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "I wonder if we're the only customers here, customers here?"
 hide miyuki_v002
 show satoko_v002 smile at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'For us to have this huge bath all to ourselves is quite the luxury.'
 hide rena_v002
 show nao_v002 smile_blush at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show nao_v002 smile_blush at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Definitely... aaah, it feels so nice...'
 hide satoko_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator 'As Nao-chan sunk shoulder-deep into the hot water, she put on a relaxed expression.'
 show mion_v002 smile at mei_right
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Mmm, hot springs really are it, huh~?'
 show mion_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, it's like my exhaustion is melting away..."
 hide mion_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Even Hanyuu's face looks like it's melting.\n...By the way, Miyuki, what were you talking about with Akasaka earlier?"
 hide hanyuu_v002
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'My da-... Akasaka-san took a call from Tokyo before coming to the spring.'
 show rika_v002 smile at inactive
 show miyuki_v002 smile_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'He promised me that we would talk about work after I got out of the spring... but he told me to give him some time.'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile_close at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Was the call because of work?\nComing all the way to this place must have been rough.'
 show satoko_v002 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Nah, I think it was just a call from home.'
 hide satoko_v002
 show kazuho_v002 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'I... I see.'
 hide miyuki_v002
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "Around now... I wonder if he's chatting with his wife and his daughter, the 5-year-old Miyuki-chan?"
 narrator 'I was leisurely soaking in the hot water imagining that pleasant scenario when...'
 camera at screenshake_transform
 pause 0.0
 Character('????',ctc="ctcArrow", ctc_position="fixed") "It's all useless!"
 show hanyuu_v002 odoroki at mei_left
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show hanyuu_v002 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au? Was that... from the men's side of the spring?"
 show hanyuu_v002 odoroki at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "...Is that maybe Battler-san's voice, Battler-san's voice?"
 hide rena_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "If we're talking about boobies, aren't massive bazoingas better than mosquito bites?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rena_v002 odoroki_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show rena_v002 odoroki_blush at active
 show rena_v002 odoroki_blush at jump_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hauuu...?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rena_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "I'm definitely not gonna deny that! No, not a single man is capable of denying it! Every single man on earth {i}loves{/i} boobies!"
 show satoko_v002 normal at mei_center
 with Dissolve(0.5)
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...That's Keiichi-san's voice."
 hide satoko_v002
 with Dissolve(0.2)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "It's only natural that big boobs are splendiferous! \nIt's the truth our world accepts! It's the foundation behind all foundations!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "...But still, there's value in having small breasts too!"
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "From the chest, down to the waist, and even all the way down to the legs, it perfectly goes down in a straight line...! I believe that's a beauty that you can only behold with the unendowed!"
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Gotcha. You're focusing on the big picture, not just a small bit of it. Not bad at all...!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Exactly! And plus, you can't overlook the future either! \nIt's good to cherish their current form too, but watching them gradually form up over time will get you even more attached!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "If boobs were a wine and you were a wine connoisseur, wouldn't you be fastidious over how your Boobjolais Nouveau ages, and not just your Caboobnet Sauvignon?!?!"
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Ihihihi! Atta boy, Keiichi! That’s the prodigy I've been counting on!"
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'So, really... it all comes down to this.\nFrom here on out, not only should we check boobies out as they are now, but we should continue observing them grow as time goes on...!'
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "You got it! So for example, if we're talkin' itty bitty titties--..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_206_water_shot.wav'
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Aaahh?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'I heard something shifting towards me in the water.\nI looked over... and saw Miyuki-chan moved over behind me with a blank expression.'
 show miyuki_v002 fuan_close at mei_right
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show miyuki_v002 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "It's better if you don't listen in, Kazuho. The conversation's kinda getting extreme."
 show miyuki_v002 fuan_close at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Eh... uh, um...?'
 hide kazuho_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator "I have no idea what she meant, but I feel going against that mysterious tone of voice might be bad, so I'll just listen to her for now."
 narrator "Because of that, I started to hear Maebara-kun and Battler-san's voices less... and was able to make out the girls' voices instead."
 show mion_v002 fuan_blush at mei_right
 show rena_v002 fuan_blush at mei_left
 with Dissolve(0.5)
 show rena_v002 fuan_blush at inactive
 show mion_v002 fuan_blush at active
 show mion_v002 fuan_blush at chara_shake_transform
 show mion_v002 fuan_blush at chara_shake_transform:
  yanchor 1.0
  linear 0.5 pos (1440,1250)
 pause 0.5
 show mion_v002 fuan_blush:
  yanchor 1.0
  pos (1440,1250)
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'K-Kei-chan...'
 show mion_v002 fuan_blush at inactive
 show rena_v002 fuan_blush at active
 show rena_v002 fuan_blush at chara_shake_transform
 show rena_v002 fuan_blush at chara_shake_transform:
  yanchor 1.0
  linear 0.5 pos (480,1250)
 pause 0.5
 show rena_v002 fuan_blush:
  yanchor 1.0
  pos (480,1250)
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'H-Hauu...'
 hide rena_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator "Mion-san and Rena-san's faces turned bright red right away."
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'W-What kind of conversation are they having...?'
 hide kazuho_v002
 with Dissolve(0.2)
 show satoko_v002 fuan_close at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show satoko_v002 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...It'd be better if you didn't know."
 show satoko_v002 fuan_close at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. It would be too stimulating for Kazuho.'
 hide satoko_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Th-they should keep their voices down at least... au au...'
 hide rika_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show nao_v002 sinken at mei_right
 show miyuki_v002 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Are all men this dumb?'
 show nao_v002 sinken at inactive
 show miyuki_v002 normal_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Mmm, I see, I see... Maebara-kun and Battler-san were looking at us with those eyes of theirs~... Interesting...'
 show nao_v002 sinken at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...They want to take a peek, but what do you think we should do about that?'
 hide nao_v002
 show satoko_v002 sinken at mei_right
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I know what you want to say.\nI'm also in the mood to fill my bathing bucket as high as possible and toss it into the mens' side this very moment."
 hide miyuki_v002
 show hanyuu_v002 odoroki at mei_left
 with Dissolve(0.5)
 show satoko_v002 sinken at inactive
 show hanyuu_v002 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'I-If other customers tried doing that, it would be really dangerous!'
 show hanyuu_v002 odoroki at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'So do we just try to endure it then?'
 hide satoko_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show mion_v002 normal_close at mei_right
 show miyuki_v002 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show mion_v002 normal_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...In any event, let's just pretend we didn't hear that locker room talk."
 show mion_v002 normal_close at inactive
 show miyuki_v002 normal at active
 show miyuki_v002 normal at nod_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yeah...\nIf Maebara-kun knew that we could hear everything from our spot, he'd lose all desire to make eye contact with us without a doubt."
 hide mion_v002
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... what could we possibly do if he was making it so we could hear them on purpose, on purpose?'
 hide miyuki_v002
 show hanyuu_v002 sinken at mei_left
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show hanyuu_v002 sinken at active
 show hanyuu_v002 sinken at chara_shake_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Th-that would be way too vicious...!'
 hide rena_v002
 show nao_v002 sinken at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 sinken at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Electric chair.'
 hide hanyuu_v002
 show satoko_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "We'd drag them up and down town as punishment."
 hide nao_v002
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show satoko_v002 sinken at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Mr. Horsie goes clippity clap and they go slippity slide!'
 hide satoko_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Was that a Western movie reference...?'
 hide rika_v002
 show nao_v002 sinken at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'We should meet their gross, idiotic masculine talk with our righteous feminine justice.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide nao_v002
 hide fade onlayer curtain
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...I say this for everyone here.\nIf either of those two start trying to grope at your chest, you drive your fist right into their face. A few times, if you like.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 Character('Everyone',ctc="ctcArrow", ctc_position="fixed") 'Yeaaaahhh!!!'
 narrator "The womens' side uniting together in reaction to the feelings of the mens' side is... taking an aggressive turn."
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(I-I'm not too sure about this...\nBut I'm getting the feeling that Maebara-kun won't be able to participate in club activities for a while...)"
 hide kazuho_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "A-Anyways...\nYou aren't getting any other customers here, huh?"
 show kazuho_v002 fuan at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "We're still in the pre-opening phase, so we don't have enough guests staying here for that to happen in the first place. Day trippers only come when it's bright out, y'know?"
 show mion_v002 smile at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Oh, okay... Huh?\nIf that's true, then where's Battler-san's cousin?"
 hide mion_v002
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "There's a lodging facility here too apart from the hot spring, so shouldn't there be personal bathing area?"
 hide miyuki_v002
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 normal at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Well, the lodging facility itself is basically complete... but the outhouse where the bathing area would be is still under construction.'
 show mion_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Then I wonder if we'd be able to meet her here at the hot spring if we wait a bit longer...?"
 show kazuho_v002 fuan at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Who knows... she could have went in earlier today, or she could even go in tomorrow morning.'
 show mion_v002 normal at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I see... By the way, we still haven't met this Jessica-san, but I wonder what kind of person she is?"
 show kazuho_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I heard from Battler-san that she's a rich girl who doesn't act like a rich girl... but she's the daughter of a super rich family that privately owns an entire island."
 show mion_v002 smile at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(The Sonozaki family is super rich in its own right, though...)'
 show kazuho_v002 fuan at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Well, if it's the daughter of our business partner, I would at least want to greet her."
 show mion_v002 smile at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...Yeah.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 hide mion_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2463.png' as bg
 stop music fadeout 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator "...By the time we left the hot spring facility, everyone's faces gave off the impression that our fatigue had been completely washed away."
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Mmm, what a great bath! Your body really will feel like you've been reborn after coming here~!"
 hide mion_v002
 with Dissolve(0.2)
 show rena_v002 smile_blush at mei_center
 show rika_v002 fuan
 show rika_v002 fuan:
  yanchor 1.0
  pos (1160, 1200)
 show hanyuu_v002 fuan
 show hanyuu_v002 fuan:
  yanchor 1.0
  pos (760, 1200)
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_374_ls_question.wav'
 show hanyuu_v002 fuan at inactive
 show rika_v002 fuan at inactive
 show rena_v002 smile_blush at active
 show rena_v002 smile_blush at chara_shake_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau~, our skin is so smooth~!'
 show hanyuu_v002 fuan at inactive
 show rena_v002 smile_blush at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Meep, Rena. Please don't rub the hot spring's beautifying effects on our skin into oblivion."
 show rika_v002 fuan at inactive
 show rena_v002 smile_blush at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'A-Auauau! If we turned any more doughy, our cheeks would slide off~!'
 show hanyuu_v002 fuan at inactive
 show rena_v002 smile_blush at inactive
 show rika_v002 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'The stimulation from getting massaged is way too powerful, meep.'
 hide hanyuu_v002
 hide rika_v002
 hide rena_v002
 with Dissolve(0.2)
 show miyuki_v002 fuan at mei_left
 show nao_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...I feel like it's a smidge fast to be worrying about skin at that age, though."
 show miyuki_v002 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "But there's nothing better than taking care of your skin from a young age... Do you want me to teach you how?"
 show nao_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Mmm, nope!\nSatoko and the others look pretty interested in it, though, so go for them instead.'
 hide nao_v002
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "My, I'd love to hear about it. Next time we come here, I would very much like to be instructed by Nao-san~♪"
 hide miyuki_v002
 hide satoko_v002
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Yeah, I wanna come again.\n...Just with the girls next time.'
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(If not, they may seriously drag Maebara-kun around town as punishment...)'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'As soon as I had the determination to think, "I have to prevent that future from happening...!", the curtain over on the mens\' side moved lightly. And then--'
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show battler_v001 smile at mei_right
 show keiichi_v002 smile at mei_left
 with Dissolve(0.5)
 show keiichi_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Haha~, that was a sweet bath!'
 show battler_v001 smile at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Man, you said it! We gotta talk about nudity again sometime!'
 hide keiichi_v002
 hide battler_v001
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Those two have a refreshed look on their faces as if that meant something else.'
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'H-Hauu... Mii-chan, was there maybe an edge to your wording... your wording?'
 hide mion_v002
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Keiichi needs to watch his step for a bit.'
 hide rena_v002
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh...? W-Why?'
 hide rika_v002
 show nao_v002 fuan_close at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yeah, better not get involved.'
 hide kazuho_v002
 hide nao_v002
 with Dissolve(0.2)
 show keiichi_v002 smile at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Oh, the girls already got out of their bath. So, Mion, what are we doing now?'
 show keiichi_v002 smile at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Dinner at the inn. Afterwards we can properly relax... I guess?'
 hide mion_v002
 show battler_v001 smile at mei_right
 with Dissolve(0.5)
 show keiichi_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Aight, nice!'
 show battler_v001 smile at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "A traditional Japanese inn-style meal, huh? I'm psyched!"
 hide battler_v001
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show keiichi_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'And after that, we have our customary pillow fight?'
 hide keiichi_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Physical activity right after eating is... kind of...'
 hide satoko_v002
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Then we'll pillow fight after a short rest."
 hide nao_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, I'm looking forward to it~!"
 show hanyuu_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah, that's right. Battler-san, before we relax at the inn, your cousin, right? If you'd like, we could go greet her before--"
 stop music fadeout 0.5
 hide mion_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...Ah, Ushiromiya-kun!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show battler_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator "In that moment, a person making a face as if he was at wit's end appeared while running towards us, saying--"
 show akasaka_v001 sinken at mei_left
 with Dissolve(0.5)
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Everyone's here together... perfect timing!\nWas Jessica Ushiromiya-san in the womens' side of the spring?!"
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show akasaka_v001 sinken at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Huh? No, it was just us...'
 show miyuki_v002 fuan at inactive
 show akasaka_v001 sinken_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Really... If so, then where is she...?'
 hide miyuki_v002
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show akasaka_v001 sinken_close at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Uh, Akasaka-san, what's going on?"
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB3.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show battler_v001 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "...Ushiromiya-kun, listen carefully and calmly.\nYour cousin Jessica-san hasn't returned to her room all this time."
 camera at screenshake_transform
 pause 0.0
 show akasaka_v001 normal at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Wha-...?!'
 show battler_v001 odoroki at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'The inn people tried calling her repeatedly to inform her about dinner, but no one answered, so we believe something might be up.'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide battler_v001
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show akasaka_v001 normal at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... What if she's just out on a walk?"
 show rena_v002 fuan at inactive
 show akasaka_v001 normal_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'That would be nice if true...'
 hide akasaka_v001
 hide rena_v002
 with Dissolve(0.2)
 narrator 'After saying that, Akasaka-san hesitated.\n...Seeing that expression, Rika-chan turned towards him with a mysterious look.'
 show rika_v002 normal at mei_right
 show akasaka_v001 normal_close at mei_left
 with Dissolve(0.5)
 show akasaka_v001 normal_close at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Akasaka, are you perhaps considering the possibility that Jessica has come into contact with "them"?'
 show rika_v002 normal at inactive
 show akasaka_v001 normal at active
 show akasaka_v001 normal at nod_transform
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yeah. Of course, I'm hoping that that isn't what we're dealing with, though..."
 hide rika_v002
 show keiichi_v002 fuan at mei_right
 with Dissolve(0.5)
 show akasaka_v001 normal at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "But, Akasaka-san, we've picked off the majority of them around this area, so maybe you're a little overworried?"
 hide akasaka_v001
 show mion_v002 normal at mei_left
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...No, he's right. We still don't know where they might pop up at any point."
 hide keiichi_v002
 hide mion_v002
 with Dissolve(0.2)
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "A-Anyways... let's split up and search for her!"
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_263.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'We split up around the not-too-huge hot spring district, looking around for her.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2073.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator "But... even after we'd all regrouped at our designated meeting space at the entrance to the hot spring district, no one was able to bring Jessica-san back with them..."
 show satoko_v002 fuan at mei_left
 show battler_v001 sinken at mei_right
 with Dissolve(0.5)
 show battler_v001 sinken at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...*sigh*, she does have to be somewhere.'
 show satoko_v002 fuan at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Don't tell me Jessica... left the hot spring district?"
 hide satoko_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 sinken at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...She might have. But if so, where would she have gone?'
 hide battler_v001
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... If she went on a walk, I feel like she wouldn't be very far..."
 hide nao_v002
 show hanyuu_v002 normal at mei_left
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show hanyuu_v002 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'This road leads directly to the heart of the village, so the possibility of her going there could also be considered.'
 hide rena_v002
 show keiichi_v002 fuan at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 normal at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "But no matter how small the village is, isn't it too big to look for a single person?"
 hide hanyuu_v002
 show nao_v002 normal_close at mei_left
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "And plus, it's nighttime too, so it'll be hard to see..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide keiichi_v002
 hide nao_v002
 hide fade onlayer curtain
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "B-But that's all the more reason to find her as soon as possible!\nIt would be terrible if she ended up a missing person...!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v002 normal at mei_left
 show akasaka_v001 fuan at mei_right
 with Dissolve(0.5)
 show akasaka_v001 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Calm down, Kazuho. We're considering the fastest way to find her."
 show rika_v002 normal at inactive
 show akasaka_v001 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Mmm... I wonder what we should do.'
 hide akasaka_v001
 hide rika_v002
 with Dissolve(0.2)
 show mion_v002 fuan at mei_right
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'How about you, Satoko? Anything come to mind?'
 show mion_v002 fuan at inactive
 show satoko_v002 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I deeply apologize, but since I'm not familiar with this Jessica-san, I won't be able to read her behavioral patterns."
 hide satoko_v002
 hide mion_v002
 with Dissolve(0.2)
 show keiichi_v002 normal at mei_left
 show battler_v001 normal at mei_right
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "So then, even if it's not efficient, isn't throwing people at the problem the best way...?"
 show keiichi_v002 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But hasn't everyone here been giving it their all to no avail?"
 hide battler_v001
 hide keiichi_v002
 with Dissolve(0.2)
 show mion_v002 normal at mei_center
 with Dissolve(0.5)
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ah, please leave that part to me. If I can pick up a phone somewhere, I can get the village people to...'
 stop music fadeout 0.5
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Wait, huh?'
 hide mion_v002
 with Dissolve(0.2)
 window hide None
 play audio 'audio/sfx/SE_343_ls_engine1.wav'
 pause 2.0
 play audio 'audio/sfx/SE_514_car_engine.wav'
 narrator 'Over beyond, the headlights of a car shine on us. The car slowly comes up the hill and stops next to us, and as the driver window rolls down...'
 narrator 'It revealed a gentle-faced person sitting in the car... Doctor Irie.'
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 show irie_v001 smile at mei_center
 with Dissolve(0.5)
 show irie_v001 smile at active
 Character('Kyousuke Irie',ctc="ctcArrow", ctc_position="fixed") 'Oh, hello, everyone. What a coincidence to meet in these parts, huh?'
 hide irie_v001
 with Dissolve(0.2)
 show battler_v001 smile at mei_right
 with Dissolve(0.5)
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Ah! Are you the doctor that drove us here?'
 show rika_v002 odoroki at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Are you familiar with Irie?'
 show rika_v002 odoroki at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'We were in a rut since there was no way of getting here from Okinomiya Station, so he gave us a ride.'
 hide rika_v002
 show irie_v001 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show irie_v001 normal at active
 Character('Kyousuke Irie',ctc="ctcArrow", ctc_position="fixed") 'Speaking of that, has something happened? Everyone has such grave-looking expressions.'
 hide battler_v001
 show akasaka_v001 normal at mei_right
 with Dissolve(0.5)
 show irie_v001 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Uh, Doctor Irie, on the way here, could you have caught sight of the girl that you drove here with Ushiromiya-kun? Jessica-san?'
 show akasaka_v001 normal at inactive
 show irie_v001 odoroki at active
 Character('Kyousuke Irie',ctc="ctcArrow", ctc_position="fixed") 'Jessica-san, is it...? Around now, she should be getting shown around the Furude shrine grounds by Shion-san.'
 hide akasaka_v001
 show battler_v001 normal at mei_right
 with Dissolve(0.5)
 show irie_v001 odoroki at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Shion... the long-haired girl that was in the car with us when you picked us up, right?'
 hide irie_v001
 show mion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Huh...?\nBattler-san, you know Shion?'
 show mion_v002 odoroki at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ah, yeah. I never had the time to mention it, but she looks just like Mion-chan...'
 hide mion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Well, they {i}are{/i} twins.'
 show nao_v002 normal at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ah... that reminds me. While I was talking to Doctor Irie in the front seat, those two were talking about something in the back...'
 hide nao_v002
 show irie_v001 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 normal_close at inactive
 show irie_v001 normal at active
 Character('Kyousuke Irie',ctc="ctcArrow", ctc_position="fixed") 'That was when Shion-san was giving the recommendation... "Looking down on Hinamizawa from the high ground is a wonderful sight!", right?'
 hide battler_v001
 show satoko_v002 normal at mei_right
 with Dissolve(0.5)
 show irie_v001 normal at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'So then, Jessica-san is with Shion-san at the shrine grounds...?'
 hide irie_v001
 hide satoko_v002
 with Dissolve(0.2)
 narrator "Everyone's blood ran cold, even after all that time in the hot spring."
 show keiichi_v002 normal at mei_center
 with Dissolve(0.5)
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "...Hey. The area around the shrine wasn't in the range of our extermination rounds today... was it?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide keiichi_v002
 hide fade onlayer curtain
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 sinken at active
 show mion_v002 sinken at chara_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Th-... that dumbass Shion!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rena_v002 sinken at mei_left
 show rika_v002 sinken at mei_right
 with Dissolve(0.5)
 show rika_v002 sinken at inactive
 show rena_v002 sinken at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "A-Anyways, let's hurry before Jessica-san comes into contact with {b}Tsukuyami{/b}!"
 show rena_v002 sinken at inactive
 show rika_v002 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep, let's hurry to the Furude shrine!"
 hide rena_v002
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 show rika_v002 sinken at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'O-Okay!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_263.png' as bg
 hide rika_v002
 hide kazuho_v002
 with Dissolve(0.2)
 stop music fadeout 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_343_ls_engine1.wav'
 narrator "We hurried towards the Furude shrine, going separately in the Coach's car and a taxi from the hot spring district."
 narrator "Be that as it may, we can't take a car into the shrine."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_613.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator 'We breathlessly sped up the steps...'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_253.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Once we reached the high grounds, we spotted two girls... there with Kasai-san.'
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB3.ogg"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show battler_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Jessica! You were over here?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "The girl next to Shion-san, who didn't look much older than me, turned her head back in response."
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yo! You're late, Battler!"
 hide jessica_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show kasai_v001 normal at mei_right
 with Dissolve(0.5)
 show kasai_v001 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If it isn't Sis and friends. Why are you all out of breath?"
 show shion_v002 smile at inactive
 show kasai_v001 normal at active
 Character('Tatsuyoshi Kasai',ctc="ctcArrow", ctc_position="fixed") 'Are you all alright?'
 hide kasai_v001
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 fuan at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Wait, did you all come here in a group?'
 show jessica_v001 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah, n-nice to meet you...\nWe're from Hinamizawa..."
 hide kazuho_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'As I introduce myself while my head is still rushing from the lack of oxygen, I survey my surroundings.'
 narrator 'Before I realized it... the atmosphere gave off a laid-back feel.\nI felt kind of disappointed.'
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I kinda don't get the situation... but I'm Jessica Ushiromiya! Pleased to meet!"
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Greet them earlier, damn it...\nIf you're gonna disappear from the inn, at the very least let someone know where you're heading off to."
 show jessica_v001 smile at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Thanks to you, everyone was in a mad rush, y'know? Sometimes with you...!"
 show battler_v001 sinken at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Huuuh??? What are you even saying?'
 show battler_v001 sinken at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'While we were being brought to the hot spring district from the station, didn\'t she tell us, "Looking down on Hinamizawa from the Furude shrine high ground is a wonderful sight!"?'
 show battler_v001 sinken at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I\'m guessing you forgot our conversation where we said, "Let\'s go see it.", and I took your word for it when you said, "I\'ll come over when night hits."?'
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show akasaka_v001 odoroki at mei_center
 with Dissolve(0.5)
 show akasaka_v001 odoroki at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '...That conversation happened?'
 hide akasaka_v001
 with Dissolve(0.2)
 show battler_v001 odoroki at mei_right
 show jessica_v001 sinken at mei_left
 with Dissolve(0.5)
 show jessica_v001 sinken at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Oh, yeah... that conversation...!'
 show battler_v001 odoroki at inactive
 show jessica_v001 sinken at active
 show jessica_v001 sinken at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yes, that one! The one who didn't make it in time is you, Battler!!"
 show battler_v001 odoroki at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'And it would have been a burden to make Shion-san and Kasai-san wait after coming all the way over to get me, so I went without you!'
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show kasai_v001 normal at mei_right
 with Dissolve(0.5)
 show kasai_v001 normal at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Though I did mention that Kasai wouldn't mind much."
 show shion_v002 normal at inactive
 show kasai_v001 normal at active
 Character('Tatsuyoshi Kasai',ctc="ctcArrow", ctc_position="fixed") "...Shion-san, it'd be nice if you had a little more consideration for me."
 hide kasai_v001
 hide shion_v002
 with Dissolve(0.2)
 narrator "We could hear Shion-san and Kasai-san's joke, but it went over our heads."
 narrator 'So, we all focused our gazes and attention on Battler-san...'
 show rena_v002 fuan at mei_left
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Battler-san...?'
 show rena_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "No... It's just, I swear I've never heard that conversation before...?"
 hide rena_v002
 show jessica_v001 sinken at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Shut up! You said, "Let\'s go see it.", too, didn\'t you?!'
 show jessica_v001 sinken at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 narrator '{i}Boop{/i}, Battler-san closed his mouth.'
 show mion_v002 fuan at mei_center
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'So maybe you were lazily nodding your head along with the conversation and letting what was being said completely slip by...?'
 hide mion_v002
 with Dissolve(0.2)
 show miyuki_v002 odoroki at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...Oof. This guy'd rank high in the mens' battle against women back at police housing."
 show miyuki_v002 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "The man that lazily ignores what's being said, pitted against the girl that thought he was listening..."
 hide nao_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show battler_v001 fuan at mei_right
 show satoko_v002 normal at mei_left
 with Dissolve(0.5)
 show satoko_v002 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I-I said my bad! The panic at the hot spring district ejected any memory I had of that out of my head!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show battler_v001 fuan at inactive
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Battler-saan?'
 hide satoko_v002
 hide battler_v001
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 narrator 'The atmosphere turned menacing as everyone fixed their cold gazes on Battler-san.'
 show akasaka_v001 smile at mei_center
 with Dissolve(0.5)
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'So, this was essentially all caused by a simple slip of the mind, and nothing was actually wrong... Thank goodness.'
 hide akasaka_v001
 with Dissolve(0.2)
 narrator "...But because of Akasaka-san's one comment, {i}poof{/i}, you could feel the atmosphere chill down again."
 show battler_v001 fuan at mei_right
 show akasaka_v001 smile at mei_left
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show battler_v001 fuan at active
 show battler_v001 fuan at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'A-Akasaka-saaan!'
 show battler_v001 fuan at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "It really is a relief that no one's hurt.\nI clearly got a bit freaked out back there, but thankfully that was all baseless worry."
 hide battler_v001
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Y-... yeah, true.'
 hide akasaka_v001
 show keiichi_v002 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Y-Yeah... I didn't know what was gonna happen for a minute, but it's awesome that it turned out to be nothing after all!"
 hide miyuki_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show keiichi_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "All's well that ends well. Nipah~."
 hide keiichi_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, I'm glad it was nothing major."
 hide rika_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show jessica_v001 fuan at mei_left
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Huh? What were you so worried about?'
 show jessica_v001 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Well, you see...'
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'Battler-san was beating around the bush, hesitating from bringing up the fact he was attacked by {b}Tsukuyami{/b}.'
 narrator "Seeing those two, Shion-san couldn't help but let out a giggle."
 show shion_v002 smile at mei_left
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*... Battler-san seems pretty airheaded.'
 show battler_v001 fuan at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Let's tread carefully. Our precious friend that carelessly breaks his promises might get sad if we keep that up."
 show shion_v002 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I-It's not thaaat bad... probably..."
 hide shion_v002
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. His eyes are darting around.'
 show rika_v002 smile at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I-It's probably because no matter how my eyes move, it's too dark to see!"
 hide rika_v002
 show mion_v002 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 odoroki at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...What a painful excuse.'
 hide battler_v001
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Alright, alright, nothing happened, so...'
 stop music fadeout 0.5
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator '...We were getting ready to head back at this point of the conversation.\nIt was then that it happened.'
 play music "<loop 0>audio/bgm/BGM_BOSS1_COLLAB3.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Look out! They're coming!\nBrace yourselves!"
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 camera at screenshake_transform
 pause 0.0
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Giiiiiiiiiiiiiiiiiiiiii!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Paired with that screaming voice, {b}Tsukuyami{/b} came bursting out from the grassy area in front of us... instantly turning my mind blank.'
 show nao_v002 sinken at mei_left
 show jessica_v001 odoroki at mei_right
 with Dissolve(0.5)
 show jessica_v001 odoroki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Wha-...?! Why now?!'
 show nao_v002 sinken at inactive
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'H-... huh?'
 hide nao_v002
 show miyuki_v002 sinken at mei_left
 with Dissolve(0.5)
 show jessica_v001 odoroki at inactive
 show miyuki_v002 sinken at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Aah... this is bad!'
 hide jessica_v001
 show rena_v002 sinken at mei_right
 with Dissolve(0.5)
 show miyuki_v002 sinken at inactive
 show rena_v002 sinken at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Everyone, defend Jessica-san!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide miyuki_v002
 hide rena_v002
 hide fade onlayer curtain
 show battler_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Shit! Jessica, don't move from that spot, alright?!"
 hide battler_v001
 with Dissolve(0.2)
 camera at screenshake_transform
 pause 0.0
 Character('Tsukuyami',ctc="ctcArrow", ctc_position="fixed") 'Giiiiiiiiiiiiiiiiiiiiii!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show jessica_v001 fuan at mei_center
 with Dissolve(0.5)
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Wh-... ah, hey...?!'
 window hide None
 call wipeout_routine
 hide jessica_v001
 with Dissolve(0.2)
 pause 1.0
 call wipein_routine
 show ange_v001 sinken at mei_center
 with Dissolve(0.5)
 show ange_v001 sinken at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Gh... I was just planning on hiding and watching over them, but to think those monsters would come to the spot I was at...!'
 show ange_v001 sinken at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "What should I do? Just like those kids said, you probably can't go against them barehanded... Wait, huh?"
 show ange_v001 odoroki at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Is this a {b}Role Card{/b}...?\nHow did this end up in my hands...?!'
 hide ange_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_572_ls_bark.wav'
 camera at screenshake_transform
 pause 0.0
 Character('Tsukuyami',ctc="ctcArrow", ctc_position="fixed") 'GROOOOOOOOOHHHHHHHHH!!!'
 show ange_v001 sinken_close at mei_center
 with Dissolve(0.5)
 show ange_v001 sinken_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Apparently I'm not gonna have much room to think either.\nIf these ones make it over there as reinforcements, it'd be a load of trouble for Onii-chan and his friends...!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show ange_v001 sinken at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Fine... I'll tango for a bit.\nI'll burn the strength and pride of the sole survivor of the Ushiromiya family right into your eyes!!!"
 call chapter_end
 jump event01_34_99