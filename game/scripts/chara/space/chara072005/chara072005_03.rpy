label chara072005_03:
 show black_background onlayer black
 $ event_store.current_event='chara072005'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072005_03'
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
 show expression 'images/bg/AdvBg_142.png' as bg
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v001 normal at mei_right
 with Dissolve(0.5)
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...I see.\nSo that explains why you were so afraid whenever you saw Keiichi and I.'
 show kazuho_v001 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v001 normal at inactive
 show kazuho_v001 odoroki at active
 show kazuho_v001 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Oh... you noticed?'
 show kazuho_v001 odoroki at inactive
 show rika_v001 smile_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. It was almost like you were a big meow meow cowering before a big woof woof.'
 show rika_v001 smile_close at inactive
 show kazuho_v001 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'O-...oh, wow...'
 show kazuho_v001 fuan at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "You didn't do anything bad, Kazuho.\nOn the contrary, I'm sorry for not realizing how much I scared you."
 show kazuho_v001 fuan at inactive
 show rika_v001 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'We were very excited since it was a sci-fi play... but we kept tossing a lot of harsh words and mean faces at you, even if it was just meant to be scripted.'
 show rika_v001 fuan_close at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "No, it's okay since you were just doing your best. But..."
 show kazuho_v001 smile at inactive
 show rika_v001 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'But... what?'
 show rika_v001 odoroki at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Play or not, seeing you and Maebara-kun becoming evil and attacking us... was definitely frightening. And even then...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v001
 hide kazuho_v001
 hide fade onlayer curtain
 show kazuho_v001 fuan_close at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v001 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'The most frightening thing to me was... that I abandoned that "world that could have existed" for my own convenience...'
 show kazuho_v001 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'If I was there, I may have been able to save countless lives... but it seems I chose to return to my original world. It was scary... and shameful...'
 show kazuho_v001 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'I got so angry... scared... at how terrible a person I must be to do such a thing.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v001 normal at mei_right
 with Dissolve(0.5)
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show kazuho_v001 fuan at mei_left
 with Dissolve(0.5)
 show rika_v001 normal at inactive
 show kazuho_v001 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I know... it's just a dream, a product of my imagination that my feelings are trapped in."
 show rika_v001 normal at inactive
 show kazuho_v001 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'But... if by some fraction of a chance... I really did bear witness to a "world that could have existed"... then I did nothing as countless people died...'
 show kazuho_v001 fuan_close at inactive
 show kazuho_v001 fuan_close at chara_shake_transform
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Kazuho. \nRegardless of the choice you made, I want to ask you something.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v001
 hide kazuho_v001
 hide fade onlayer curtain
 show rika_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Which do you want to hear more? \nThe harsh truth? Or perhaps a gentle lie?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v001 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v001 odoroki at active
 show kazuho_v001 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show rika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show kazuho_v001 odoroki at inactive
 show rika_v001 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'No... you already know the answer to this question. If you chose the gentle lie, then you would\'ve decided that it was all just a "Dream".'
 show kazuho_v001 odoroki at inactive
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "So, I'm going to tell you the harsh reality."
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show kazuho_v001 odoroki at inactive
 show rika_v001 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "—How dare you be so conceited, even though you aren't a god?\nWho do you think you are?!"
 show rika_v001 sinken at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '....ah-...?'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show kazuho_v001 odoroki at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I'm sorry for speaking brashly. \n...However, please allow me to stress this for you. I've anguished over similar doubts and regrets... as your predecessor."
 show rika_v001 fuan at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Pre...decessor...?'
 show kazuho_v001 odoroki at inactive
 show rika_v001 smile_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...That was me talking to myself. Please don't worry about it."
 show rika_v001 smile_close at inactive
 show kazuho_v001 normal at active
 show kazuho_v001 normal at nod_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'O-Okay...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v001
 hide rika_v001
 hide fade onlayer curtain
 show rika_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "There are a plethora of calculations involved when you make a choice.\nAnd from that arises one's self-interest, but it's nearly impossible for there to be a case where everyone benefits from that... no, the possibility of that is zero."
 show rika_v001 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "As we move into the future, some people will be there laughing, and some will be crying. Or maybe some so angry and spiteful that they'd wish for anybody other than themselves to die or disappear..."
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'That is the logic behind everything. That is exactly why justice and evil continue to exist. Like with fictional heroes, the final boss can never truly be destroyed.'
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'On the other hand, the remaining corruption can give rise to a new battle. There is no rest for the heart and soul, so it becomes disheartening and even desperate...'
 show rika_v001 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "So... that's why everyone holds wishes.\nIn this very moment now, there are people longing for their wishes where the most wonderful thing in their eyes occurs right before them..."
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Is thinking that way troubling for you...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v001 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'R-Rika-chan...?'
 show rika_v001 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v001 odoroki at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's just like this ohagi. It's sweet and delicious.\nOnce you've savored its taste, it ceases to exist..."
 show kazuho_v001 odoroki at inactive
 show rika_v001 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But while you could just leave it there forever, it will eventually start to go bad. And if you put it in the refrigerator, it's only good for at most another week..."
 show kazuho_v001 odoroki at inactive
 show rika_v001 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'So, you have no choice but to make a decision.\nEven if someone besides you cries and is resentful because of it...'
 show kazuho_v001 odoroki at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I personally only want to think about living out my days, where I and the people close to me can laugh together... and where I can truly feel happiness from the bottom of my heart.'
 show rika_v001 smile at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 show kazuho_v001 odoroki at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'So, Kazuho.\nForget about the ohagi that no longer exists.'
 show kazuho_v001 odoroki at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "And... just eat. Eat this delicious ohagi that actually does exist in front of you, the one that I'm presenting to you right now..."
 show rika_v001 smile at inactive
 show kazuho_v001 fuan_blush at active
 show kazuho_v001 fuan_blush at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...gh...'
 show rika_v001 smile at inactive
 show kazuho_v001 smile_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Thank you, Rika-chan. *munch*'
 show kazuho_v001 smile_close at nod_transform
 show kazuho_v001 smile_close at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Does it taste good, Kazuho?'
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show rika_v001 smile at inactive
 show kazuho_v001 smile_blush at active
 show kazuho_v001 smile_blush at nod_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Yes... it's delicious. It tastes very sweet..."
 show kazuho_v001 smile_blush at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "That's great to hear.\nFace towards the future and fight on, Kazuho! Nipah~"
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v001
 hide rika_v001
 with Dissolve(0.2)
 camera:
  pos (960, 540)
  zoom 1.0
 stop music fadeout 0.5
 pause 1.0
 show black_cover as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_408_run.wav'
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Quickly, K-1!\nWe need to get past the gate, where Lady Meep is-...!'
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Aight... leave it to me!\nGalaxy Bazooka, FIREEEEEE!!'
 play audio 'audio/sfx/SE_310_ls_stageexplosion.wav'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/card/Card_072005.png' as bg
 play music "<loop 3.53>audio/bgm/BGM_EVENT7.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "M-Meep!\nK-1 and Ka-zuho, you've come to save me?"
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yeah, of course!\nYou can rest assured now that I'm here!"
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "*cackle*... You're in high spirits, aren't you, Space Sheriff K-1?\nBut unfortunately for you... this will be your graveyard!"
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Heh... right back 'atcha!\nHere I come, Demon Queen of Darkness, Miyon!!"
 Character('Boy',ctc="ctcArrow", ctc_position="fixed") 'Go, Space Sheriff K-1!\nDefeat the Demon Queen of Darkness!!'
 Character('Girl',ctc="ctcArrow", ctc_position="fixed") "Be careful, Space Warrior Ka-zuho!\nDon't lose to the bad guys!"
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_341.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Boy, seems like it's going pretty nicely. At some point I wondered what was going to happen... but seems I didn't need to worry in the end."
 show nao_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show nao_v002 smile at active
 show nao_v002 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Indeed. The kids in the audience look like they're receiving it well... so it's fair to say this was a huge success."
 hide miyuki_v002
 hide nao_v002
 with Dissolve(0.2)
 show hanyuu_v002 smile at mei_center
 with Dissolve(0.5)
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show hanyuu_v002 smile_close at active
 show hanyuu_v002 smile_close at nod_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "You've overcome this hurdle, Kazuho.\nRika's also seemed to have grown stronger than before, and I'm very happy about that~. Au au♪"
 call chapter_end
 
 $ persistent.chara072005_done = True
 return