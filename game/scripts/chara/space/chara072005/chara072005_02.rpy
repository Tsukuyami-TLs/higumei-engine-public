label chara072005_02:
 show black_background onlayer black
 $ event_store.current_event='chara072005'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072005_02'
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
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rena_v001 fuan at mei_left
 with Dissolve(0.5)
 show rena_v001 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Kazuho-chan... wasn't very lively today.\nShe didn't finish her bento, so I wonder if she's not feeling well... not feeling well?"
 show rika_v001 fuan at mei_right
 with Dissolve(0.5)
 show rena_v001 fuan at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. It wasn't just today either.\nFor a while now, Kazuho has been talking very little and acting strange."
 hide rena_v001
 show keiichi_v001 fuan at mei_left
 with Dissolve(0.5)
 show rika_v001 fuan at inactive
 show keiichi_v001 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "...Rika-chan's probably right.\nTo be honest, I kept quiet about it because I thought I was overworrying, but..."
 show rika_v001 fuan at inactive
 show keiichi_v001 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Kazuho-chan... won't even make eye contact with me these days, not during practice, and not during breaks. ...Did I do something bad?"
 hide rika_v001
 show miyuki_v001 odoroki at mei_right
 with Dissolve(0.5)
 show keiichi_v001 fuan at inactive
 show miyuki_v001 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Woah... really?\nI feel her and I have been just as we usually are, though...'
 hide keiichi_v001
 show satoko_v001 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v001 odoroki at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Are you sure you're not mistaken, Keiichi-san? I don't think Kazuho-san has appeared angry at all, at least as far as we can see."
 hide miyuki_v001
 hide satoko_v001
 with Dissolve(0.2)
 show rika_v001 fuan at mei_center
 with Dissolve(0.5)
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Meep. It might not be a misunderstanding.'
 show satoko_v001 odoroki at mei_left
 show rika_v001 fuan
 show rika_v001 fuan:
  yanchor 1.0
  linear 0.5 pos (1440,1200)
 with Dissolve(0.5)
 show rika_v001 fuan:
  yanchor 1.0
  pos (1440,1200)
 show rika_v001 fuan at inactive
 show satoko_v001 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh...? What do you mean, Rika?'
 show satoko_v001 odoroki at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I had an experience similar to Keiichi's. After the end of practice earlier, I tried to start a conversation with Kazuho, but..."
 show satoko_v001 odoroki at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'As soon as she saw my face, she got scared like she saw a ghost.\nHer reaction was so intense that it surprised {i}me{/i}.'
 hide satoko_v001
 show miyuki_v001 normal at mei_left
 with Dissolve(0.5)
 show rika_v001 fuan at inactive
 show miyuki_v001 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yeah... maybe the first script wasn't all too great after all. It was a shocking ending with Maebara-kun and Rika-chan turning evil."
 hide rika_v001
 show nao_v001 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v001 normal at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It was a pretty hard-hitting twist, wasn't it?\nAnd it was for sure much too serious for something intended for kids, and that's why we started talking about making it more palatable..."
 show miyuki_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But it is also true that Kazuho had some cruel lines spoken to her, but that was just part of the play in the end. Did she really take it so seriously despite that?'
 hide miyuki_v001
 hide nao_v001
 with Dissolve(0.2)
 show hanyuu_v001 normal at mei_center
 with Dissolve(0.5)
 show hanyuu_v001 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...That may not exactly be the situation with Kazuho right now.'
 show nao_v001 odoroki at mei_right
 show hanyuu_v001 normal
 show hanyuu_v001 normal:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 with Dissolve(0.5)
 show hanyuu_v001 normal:
  yanchor 1.0
  pos (480,1200)
 show hanyuu_v001 normal at inactive
 show nao_v001 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '......What could you mean by that, Hanyuu?'
 show nao_v001 odoroki at inactive
 show hanyuu_v001 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "A-Au au... I'm so sorry. I'm just thinking aloud... um..."
 hide hanyuu_v001
 hide nao_v001
 with Dissolve(0.2)
 show rika_v001 fuan at mei_center
 with Dissolve(0.5)
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...........'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop music fadeout 0.5
 hide rika_v001
 with Dissolve(0.2)
 pause 1.0
 stop sound
 show expression 'images/bg/AdvBg_142.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kazuho_v001 fuan_close at mei_center
 with Dissolve(0.5)
 show kazuho_v001 fuan_close at active
 show kazuho_v001 fuan_close at deepbreath_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '*sigh*... I did something terrible to them.'
 show kazuho_v001 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I know it was just a dream all in my head... but I can't stop thinking about that conversation back then..."
 play audio 'audio/sfx/SE_530_walk_one.wav'
 show rika_v001 smile at mei_outerright
 show rika_v001 smile at walk_transform:
  yanchor 1.0
  linear 0.6666666666666666 pos (1440,1200)
 show kazuho_v001 fuan
 show kazuho_v001 fuan:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 with Dissolve(0.5)
 pause 0.16666666666666663
 show rika_v001 smile:
  yanchor 1.0
  pos (1440,1200)
 show kazuho_v001 fuan:
  yanchor 1.0
  pos (480,1200)
 show kazuho_v001 fuan at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Kazuho.'
 show rika_v001 smile at inactive
 show kazuho_v001 odoroki at active
 show kazuho_v001 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Mm? R-Rika-chan... why are you here?'
 show kazuho_v001 odoroki at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Just by chance. ...The way things were, it made me feel that you wouldn't go straight home."
 show rika_v001 smile at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "A-Ahahaha... I see. I'm sorry."
 show kazuho_v001 smile at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I brought some ohagi from Mion's house. If you like, we can eat together?"
 show rika_v001 smile at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...Thanks. But right now, I'm a little..."
 show kazuho_v001 smile at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Everyone is worried about you.\nDo you maybe have something causing you trouble?'
 show rika_v001 fuan at inactive
 show kazuho_v001 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v001
 hide rika_v001
 hide fade onlayer curtain
 show rika_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Kazuho, we're your friends. If you don't want to talk, then of course I won't force you to. But..."
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Maybe speaking to us will help you feel better... and we can lend you our support in response, you know?'
 hide rika_v001
 show kazuho_v001 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Rika-chan...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v001 smile_close at mei_left
 with Dissolve(0.5)
 show kazuho_v001 smile_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...When I tell you this story, you might find it funny or feel disgusted.\nOr maybe you'll get mad at me and think I'm pulling your leg...?"
 show rika_v001 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v001 smile_close at inactive
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v001 normal at inactive
 show kazuho_v001 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I... had a dream.\nNo, maybe it wasn't a dream... it felt like I was in a different world that really existed..."
 call chapter_end
 jump chara072005_03