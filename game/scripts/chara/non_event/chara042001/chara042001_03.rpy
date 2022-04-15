label chara042001_03:
 show black_background onlayer black
 $ event_store.current_event='chara042001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara042001_03'
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
 show expression 'images/bg/AdvBg_333.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_5052_bell.wav'
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show keiichi_v004 smile at active
 show keiichi_v004 smile at mei_left
 with Dissolve(0.5)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Yo. Looks like I was right about Angel Mort being our meeting place.'
 show keiichi_v004 smile at inactive
 show kazuho_v002 smile at active
 show kazuho_v002 smile at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Yeah. So, the guy from earlier {i}was{/i} you, Maebara-kun.'
 show kazuho_v002 smile at inactive
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yup. By the way, how'd you know it was me?"
 hide kazuho_v002
 show keiichi_v004 smile at inactive
 show miyuki_v002 smile at active
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'It was the sound of your voice... so what happened with those guys?'
 show miyuki_v002 smile at inactive
 show keiichi_v004 futeki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "They put up a good fight, so I taught them a lesson.\nLet's just say they'll never be able to find this place. Hahahahaha!"
 hide miyuki_v002
 show keiichi_v004 futeki at inactive
 show nao_v002 smile at active
 show nao_v002 smile at mei_right
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Thank you. We were able to get away thanks to you.'
 show keiichi_v004 futeki at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I don't often give compliments like this because I don't think it's tasteful... but you were a pretty cool hero."
 show nao_v002 smile at inactive
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Heheh, thanks. ...But, I'll have to turn down being called a hero.\nThe title of hero is a little too heavy for me."
 show nao_v002 smile at inactive
 show keiichi_v004 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "And honestly... I can't really call myself an ally to justice for a bunch of reasons either."
 show keiichi_v004 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I see. Even then, the fact remains that you saved us.'
 hide keiichi_v004
 hide nao_v002
 with Dissolve(0.2)
 show miyuki_v002 smile at active
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Mmm. Then maybe you could call yourself "Dark Hero" as an in between?'
 show miyuki_v002 smile at inactive
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '"Dark Hero"...?'
 show kazuho_v002 odoroki at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Basically, a villain who awakened to a heart of justice.\nThat's more something you can accept, right, Maebara-kun?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 610)
  zoom 1.4
 hide miyuki_v002
 hide kazuho_v002
 hide fade onlayer curtain
 show keiichi_v004 smile at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "I see... Dark Hero, huh?\nFor someone who can't call himself an ally to justice, that sounds perfect."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v004
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show miyuki_v002 smile at active
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "*chuckle*, I'm glad you like it."
 show keiichi_v004 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Thank you. But really, I got scared when you said you would break their bones earlier. You're pretty hot-blooded, Miyuki-chan."
 show keiichi_v004 smile at inactive
 show miyuki_v002 smile at active
 show miyuki_v002 smile at jumping_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ahahaha, I don't wanna hear it from you, Maebara-kun~.\nBut it got them riled up and kept their attention focused on us, right?"
 hide miyuki_v002
 show keiichi_v004 smile at inactive
 show nao_v002 normal at active
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...You're dark enough, Miyuki.\nYou give off the vibe you're trying to get used to fights."
 show nao_v002 normal at inactive
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Haha, I appreciate that energy... but is it really okay?\nThose guys are gonna be looking for you.'
 show keiichi_v004 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Well, we'll get there when we get there."
 hide nao_v002
 show keiichi_v004 smile at inactive
 show miyuki_v002 futeki at active
 show miyuki_v002 futeki at mei_right
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "We've got a trump card of our own for emergencies.\nThere's no need to worry."
 show miyuki_v002 futeki at inactive
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "...I see. At any rate, don't do anything unreasonable. If it gets down to it, just run for Hinamizawa. Those guys wouldn't go that far."
 hide miyuki_v002
 show keiichi_v004 smile at inactive
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'But Maebara-kun? You live in Okinomiya, so they might find you...'
 show kazuho_v002 fuan at inactive
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Haha, I'll be fine. I was wearing a mask."
 hide kazuho_v002
 show keiichi_v004 smile at inactive
 show nao_v002 normal at active
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'So that mask {i}was{/i} there to hide your face.\nIt looked like a stage production or like it was a hobby.'
 show nao_v002 normal at inactive
 show keiichi_v004 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'I actually wanted to fight them fair and square without hiding my face... but there was the risk of getting my family involved.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide keiichi_v004
 hide nao_v002
 hide fade onlayer curtain
 show keiichi_v004 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v004 normal_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "But, well, I'll let it be just this once."
 show keiichi_v004 smile at active
 show keiichi_v004 smile:
  yanchor 1.0
  linear 0.5 pos (960,1200)
 pause 0.5
 show keiichi_v004 smile:
  yanchor 1.0
  pos (960,1200)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "It's more my style to fight with everything exposed rather than fight while hiding something."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v004
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...? What kind of situation would you have to be in to fight with everything exposed?'
 show kazuho_v002 odoroki at inactive
 show keiichi_v004 normal at active
 show keiichi_v004 normal at mei_left
 with Dissolve(0.5)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Mm, good question...'
 show kazuho_v002 odoroki at inactive
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'For those really serious moments, I guess.'
 show keiichi_v004 smile at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...........'
 show kazuho_v002 normal at inactive
 show keiichi_v004 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "What's wrong, Kazuho-chan? You're just staring at my face."
 show keiichi_v004 odoroki at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Um, it's nothing important.\nIt's just... you looked like you felt nostalgic for a second, Maebara-kun."
 hide kazuho_v002
 show keiichi_v004 odoroki at inactive
 show miyuki_v002 smile at active
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Do you maybe have experience going all out fighting for someone really important?'
 show miyuki_v002 smile at inactive
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "I don't remember doing anything like that... but it would be encouraging if that did happen."
 show miyuki_v002 smile at inactive
 show keiichi_v004 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "After all, once you do something once, there's nothing stopping you from doing it again! Hahahaha!!"
 call chapter_end
 
 $ persistent.chara042001_done = True
 return