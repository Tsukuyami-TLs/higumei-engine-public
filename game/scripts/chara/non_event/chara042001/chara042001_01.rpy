label chara042001_01:
 show black_background onlayer black
 $ event_store.current_event='chara042001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara042001_01'
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
 show expression 'images/bg/AdvBg_341.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 2.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_351.png' as bg
 call wipein_routine
 show nao_v001 normal at active
 show nao_v001 normal at mei_left
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Kazuho, have you found any new documents on Hinamizawa?'
 show nao_v001 normal at inactive
 show kazuho_v001 normal at active
 show kazuho_v001 normal at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Yeah. For now, there's a book called Regional Studies... but taking a quick look, I don't know if it'd make a good reference."
 show kazuho_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Let's check it out in the meantime.\nWe can just examine it and decide if it'll be useful or not."
 show kazuho_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Right now, we don't know which documents will be helpful to us at all."
 show nao_v001 normal at inactive
 show kazuho_v001 normal at active
 show kazuho_v001 normal at nod_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I agree. ...By the way, where's Miyuki-chan?"
 hide nao_v001
 hide kazuho_v001
 with Dissolve(0.2)
 show miyuki_v001 smile at active
 show miyuki_v001 smile at mei_center
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ah, over here! Heeeeey!'
 show nao_v001 sinken at active
 show nao_v001 sinken at mei_outerright
 show nao_v001 sinken at walk_transform:
  yanchor 1.0
  linear 1.0 pos (1440,1200)
 show miyuki_v001 smile at inactive
 show miyuki_v001 smile:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 with Dissolve(0.5)
 pause 0.5
 show nao_v001 sinken:
  yanchor 1.0
  pos (1440,1200)
 show miyuki_v001 smile:
  yanchor 1.0
  pos (480,1200)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Pipe down when you're in the library.\n...Anyway, what did you find?"
 show nao_v001 sinken at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Right! Look at these leaflets!'
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 hide nao_v001
 show miyuki_v001 smile at inactive
 show kazuho_v001 odoroki at active
 show kazuho_v001 odoroki at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'An announcement for the "Children\'s Fair to be held in front of Okinomiya Library"?'
 show kazuho_v001 odoroki at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "The librarian told me about it just now.\nEvery weekend, there's a fair held for Okinomiya children in the library parking lot."
 show kazuho_v001 odoroki at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Of course, it's on a smaller scale than the Watanagashi, but I hear it attracts a lot of people... We should try going."
 show miyuki_v001 smile at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Um... so we're taking a break?"
 hide kazuho_v001
 show miyuki_v001 smile at inactive
 show nao_v001 normal at active
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "This is different. It's more like... we're collecting information?"
 show nao_v001 normal at inactive
 show miyuki_v001 smile at active
 show miyuki_v001 smile at nod_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Yeah, yeah! Shion and Maebara-kun are the only people we know in Okinomiya, right?'
 show nao_v001 normal at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Where people gather, information follows... \nAnd plus, if it's a small-scale festival, unfamiliar people like us won't stand out."
 hide nao_v001
 show miyuki_v001 smile at inactive
 show kazuho_v001 smile at active
 show kazuho_v001 smile at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...True. I feel like we've hit a dead end when it comes to gathering info at the library..."
 hide miyuki_v001
 hide kazuho_v001
 with Dissolve(0.2)
 show keiichi_v001 smile at active
 show keiichi_v001 smile at mei_center
 with Dissolve(0.5)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Oh...? So, you guys going to the fair?'
 hide keiichi_v001
 with Dissolve(0.2)
 show kazuho_v001 smile at active
 show kazuho_v001 smile at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Oh, hello.\nI didn't know you also came to this library, Maebara-kun."
 show kazuho_v001 smile at inactive
 show keiichi_v001 smile at active
 show keiichi_v001 smile at mei_left
 with Dissolve(0.5)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yeah. I'm doing a little cram school prep and reviewing some of the stuff they taught today. What are you gonna do at the fair?"
 show keiichi_v001 smile at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'U-Um...'
 hide kazuho_v001
 show keiichi_v001 smile at inactive
 show nao_v001 normal at active
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "We're doing homework too. It's an independent research project."
 hide nao_v001
 show keiichi_v001 smile at inactive
 show kazuho_v001 smile at active
 show kazuho_v001 smile at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Y-Yeah.\n...By the way, Maebara-kun, would you like to go with us?'
 show kazuho_v001 smile at inactive
 show keiichi_v001 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Me? Well... maybe if I have time after cram school.\n...Just be careful if you go to the fair.'
 hide kazuho_v001
 show keiichi_v001 normal at inactive
 show miyuki_v001 normal at active
 show miyuki_v001 normal at mei_right
 with Dissolve(0.5)
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'What, are we gonna get pickpocketed or extorted from or something? I heard Okinomiya was safe, but I guess that kind of thing does happen.'
 show miyuki_v001 normal at inactive
 show keiichi_v001 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Well, anything happens when a bunch of people get together.'
 show miyuki_v001 normal at inactive
 show keiichi_v001 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Some people who don't even go to the library regularly might try to go for the fairgoers."
 hide miyuki_v001
 show keiichi_v001 normal at inactive
 show kazuho_v001 smile at active
 show kazuho_v001 smile at mei_right
 with Dissolve(0.5)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Okay, thanks for the heads up. We'll be sure to be careful."
 call chapter_end
 jump chara042001_02