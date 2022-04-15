label chara482001_02:
 show black_background onlayer black
 $ event_store.current_event='chara482001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara482001_02'
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
 show expression 'images/bg/AdvBg_321.png' as bg
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB3.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show battler_v001 fuan at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'They brought us here, but...'
 show battler_v001 fuan at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Is this a... family restaurant? '
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show hanyuu_v002 smile at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_348_ls_suddunshow.wav'
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, this is Okinomiya's best family restaurant, Angel Mort~!"
 hide hanyuu_v002
 with Dissolve(0.2)
 show battler_v001 fuan_close at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 fuan_close at active
 show battler_v001 fuan_close:
  yanchor 1.0
  linear 0.5 pos (480,1250)
 pause 0.5
 show battler_v001 fuan_close:
  yanchor 1.0
  pos (480,1250)
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'A family restaurant, huh...?'
 show battler_v001 fuan_close at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Woo, a family restaurant!'
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show rika_v002 normal at mei_center
 with Dissolve(0.5)
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep, their responses are polar opposites.'
 hide rika_v002
 with Dissolve(0.2)
 show satoko_v002 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Jessica, do you enjoy family restaurants?'
 show satoko_v002 smile at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Yeah! I went to one during a school trip when I was younger! It was a different chain than this one, though.'
 hide satoko_v002
 show miyuki_v002 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...You went to a family restaurant on a field trip?'
 show miyuki_v002 fuan at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "My school was on a small island, so there weren't any family restaurants there."
 hide miyuki_v002
 show battler_v001 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Family restaurant...'
 show battler_v001 fuan at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hey, Battler, what's got you moping around?\nEverything's fine, so let's go♪"
 show jessica_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "No, it's just that you were really confident in this place, and I thought it would be something more like... regional food you could only get here, or something?"
 show jessica_v001 smile at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I was expecting something more like soba that used water from a famous local spring, or tempura...'
 hide jessica_v001
 with Dissolve(0.3)
 show rika_v002 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Battler is disappointed because his expectation was off the mark. ...Pet, pet.'
 show rika_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...How can you pet my head so naturally?'
 show satoko_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show battler_v001 fuan at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's Rika's hobby."
 show satoko_v002 normal at inactive
 show rika_v002 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Her hobby... huh? Hey, Rika. Have we ever met before?'
 show satoko_v002 normal at inactive
 show battler_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep? Are you flirting with me?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide battler_v001
 hide rika_v002
 hide satoko_v002
 hide fade onlayer curtain
 show mion_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Wha-! Flirting with this tiny kid?! '
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show battler_v001 odoroki at mei_center
 with Dissolve(0.5)
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Wh-, no...?!'
 hide battler_v001
 with Dissolve(0.2)
 show rena_v002 fuan at mei_left
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... I know Rika-chan is kyute, but flirting with her is...'
 show rena_v002 fuan at inactive
 show miyuki_v002 sinken at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "No, that guy loves boobies... so in other words, in anticipation of what she'll be like in the future, he's planning on grooming her to be his ideal woman?!"
 hide rena_v002
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show miyuki_v002 sinken at inactive
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jump_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Eh... ehhhhhhh?!'
 hide miyuki_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show satoko_v002 sinken at mei_right
 show rika_v002 fuan at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 show rika_v002 fuan at inactive
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Rika, do please come over this way. It's dangerous for you to be next to him."
 show satoko_v002 sinken at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep.'
 hide satoko_v002
 show shion_v002 sinken at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Rika-chama, please hide behind my back.'
 hide rika_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 sinken at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I think it would be a good idea to put some distance between us.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide shion_v002
 hide nao_v002
 hide fade onlayer curtain
 show battler_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Don't stand in a circle around me like that! You're gonna hurt my feelings bad!!"
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "It's not like that! I really do feel like we've met somewhere before...!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show jessica_v001 smile at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "C'mon, don't just stand there! Aren't you hungry?"
 play audio 'audio/sfx/SE_530_walk_one.wav'
 hide jessica_v001
 with Dissolve(0.6)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah... w-wait, Jessica-san!'
 hide kazuho_v002
 with Dissolve(0.2)
 show battler_v001 fuan_close at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Uoooh... I feel like I've been walked all over."
 show keiichi_v002 normal at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") '...Hey, Battler. Do you know what the phrase "your clothes make you look smaller" means?'
 show keiichi_v002 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "W-What's up, Keiichi...? What is it all of a sudden?"
 show battler_v001 fuan at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "It means a person will look slender while wearing clothes, but once they're off..."
 show keiichi_v002 normal at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I-It can't be...?!"
 play audio 'audio/sfx/SE_226_shine.wav'
 show battler_v001 sinken at inactive
 show keiichi_v002 futeki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "The true form of this restaurant cannot be seen from the exterior! Preconceptions are poison---no, in this case they're a grave sin! "
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide battler_v001
 hide keiichi_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_331.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_5037_getup.wav'
 Character('Waitress',ctc="ctcArrow", ctc_position="fixed") "Hello, I'll take your orders now~.\nHere is our menu."
 show battler_v001 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Wh-wh-wha...!!'
 show keiichi_v002 futeki_close at mei_right
 with Dissolve(0.5)
 show battler_v001 odoroki at inactive
 show keiichi_v002 futeki_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "What is it, Battler...? It's all good; you can lay those feelings on me!"
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show keiichi_v002 futeki_close at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'W-wh-wha... what was that waitress wearing?!'
 show keiichi_v002 futeki_close at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "This is the best... no, it's too good to be true! Is this place heaven, or perhaps paradise?"
 show keiichi_v002 futeki_close at inactive
 show battler_v001 smile_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Excellent... truly excellent...!!! To think I almost missed out on this Shangri-La...!'
 show battler_v001 smile_close at inactive
 show keiichi_v002 futeki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Whatcha think...? Understand why I recommended this place now?'
 show keiichi_v002 futeki at inactive
 show battler_v001 smile at active
 show battler_v001 smile at nod_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yeah... I'm sorry, Keiichi, my beloved friend! I'm ashamed! Pathetic! I want to dig a hole and jump insiiiiiiiiide!!!"
 play audio 'audio/sfx/SE_577_ls_sanriokirakira.wav'
 show keiichi_v002 futeki at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm going to sear this image into every cell of my retinas and carry it with me forevermore...! That image will be the crown jewel, the ultimate souvenir of my time in Hinamizawa!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show shion_v002 fuan at mei_left
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I-It's that good...?! Well, this store's selling point {i}is{/i} the outfits, so getting that sort of appraisal isn't that bad, but...?"
 show shion_v002 fuan at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Is it me, or does anyone else feel like Kei-chan's likability is falling as rapidly as the Niagaras...?"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show battler_v001 normal at mei_left
 show keiichi_v002 futeki at mei_right
 with Dissolve(0.5)
 show keiichi_v002 futeki at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...By the way, Keiichi. Between underboob or cleavage, which do you like more?'
 show battler_v001 normal at inactive
 show keiichi_v002 normal_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "I'd say I like both, but if I had to pick....."
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_369_ls_suddunshow2.wav'
 show battler_v001 normal at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "I'd go with cleavage!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show keiichi_v002 sinken at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hoh... let's hear the thought process behind that."
 show battler_v001 normal at inactive
 show keiichi_v002 normal_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "That's because underboob is erotic... but a little too erotic."
 show battler_v001 normal at inactive
 show keiichi_v002 normal_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'You only see underboob when somebody is wearing clothing designed to show it off...'
 show battler_v001 normal at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Or it's when they roll their shirt up just below their boobs."
 show keiichi_v002 normal at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But in the latter case... it's just a fleeting, concidential glimpse! "
 show battler_v001 sinken at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yeah, with one glimpse, it has the power to rule your world! It's a delicacy! Its true value is in its electrifying desirability!!"
 show keiichi_v002 sinken at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "However... if the underboob is constantly visible, you get desensitized... so you can't deny that it has the drawback of potentially becoming mundane!"
 camera:
  parallel:
   linear 0.5 pos (960, 550)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show battler_v001 sinken at inactive
 show keiichi_v002 sinken_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Going off that point, normal clothes will sometimes show off cleavage! Furthermore, when they do, somehow it still looks elegant!'
 camera:
  parallel:
   linear 0.5 pos (960, 570)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show battler_v001 sinken at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Low-cut shirts showing off a bit of the collarbone! The bravery in showing off your boob outline in a bikini!'
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show battler_v001 sinken at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Bunny suits expose a huge amount of skin, but do you know what ties its refined look together with its versatility?!'
 show keiichi_v002 sinken at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "That's right... the one thing that brings it all together... it's the cleavage...!!"
 show keiichi_v002 sinken at inactive
 show battler_v001 futeki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "It seems we're of the same opinion...!"
 show keiichi_v002 sinken
 show keiichi_v002 sinken:
  yanchor 1.0
  linear 0.5 pos (1160,1200)
 show battler_v001 futeki
 show battler_v001 futeki:
  yanchor 1.0
  linear 0.5 pos (760,1200)
 pause 0.5
 show keiichi_v002 sinken:
  yanchor 1.0
  pos (1160,1200)
 show battler_v001 futeki:
  yanchor 1.0
  pos (760,1200)
 play audio 'audio/sfx/SE_229_grap.wav'
 show keiichi_v002 sinken at active
 show battler_v001 futeki at active
 Character('Battler and Keiichi',ctc="ctcArrow", ctc_position="fixed") '............ (firm handshake)'
 show keiichi_v002 sinken at inactive
 show battler_v001 futeki_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Perhaps we were close friends in a previous life...'
 show battler_v001 futeki_close at inactive
 show keiichi_v002 futeki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Maybe even brothers!'
 show battler_v001 futeki
 show keiichi_v002 futeki at active
 show battler_v001 futeki at active
 show keiichi_v002 futeki at updown_shake_transform
 show battler_v001 futeki at updown_shake_transform
 Character('Battler and Keiichi',ctc="ctcArrow", ctc_position="fixed") 'Hahahahah...!!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide keiichi_v002
 hide battler_v001
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v002 fuan at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'W-... what on earth is this...?'
 show satoko_v002 fuan at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. The sweaty men sweatily sitting at the table next to us are talking sweatily while exchanging sweaty handshakes.'
 hide satoko_v002
 show miyuki_v002 smile_close at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show miyuki_v002 smile_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "You girls, you shouldn't pay attention to them! Here, take a look at this menu, okay~?"
 hide rika_v002
 show jessica_v001 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile_close at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So, to those two, Angel Mort outfits classify as prim and proper... is what I'm getting here?"
 hide miyuki_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'In what world are those uniforms prim and proper...?'
 hide jessica_v001
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It seems that right now, Keiichi-san and Battler-san can't see anything but that."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide satoko_v002
 hide fade onlayer curtain
 show nao_v002 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Without love, it cannot be seen.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v002 odoroki at mei_right
 show nao_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at inactive
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Eh?'
 show mion_v002 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Those words... came to mind just now. Maybe it was a phrase I picked up somewhere in a novel?'
 hide mion_v002
 show jessica_v001 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'You say "love"... So, they can see those outfits that way because they won\'t stop loving boobs?'
 hide nao_v002
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 fuan at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau, so that's how it is...?"
 hide jessica_v001
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...That's love?"
 hide rena_v002
 show rika_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show rika_v002 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. If the people in question think it's love, it's love... surely, maybe... probably."
 hide miyuki_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan_close at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, I'm not following this at all~."
 hide rika_v002
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Th-this got kinda philosophical somehow... It's all gibberish to me."
 hide hanyuu_v002
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'M-Me too...'
 hide satoko_v002
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... maybe I'll understand it one day."
 hide kazuho_v002
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, I don't think you'd get much meaning out of it even if you did understand what was going on."
 hide rena_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Well, anyways...'
 show miyuki_v002 fuan at inactive
 show shion_v002 normal_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'After making Satoko listen to that conversation... we should invite those two to the Sonozaki house.'
 hide miyuki_v002
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show shion_v002 normal_close at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Which part of it? The top side? Or the bottom side?'
 show mion_v002 normal at inactive
 show shion_v002 futeki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yeah, I wonder which side they'll prefer then... *cackle*cackle*cackle*."
 show shion_v002 futeki at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*......!'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "S-Shion-san and Mion-san are laughing, but their faces aren't funny looking at all...!"
 show satoko_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...The boys' upper vs lower conversation over there is just vulgar, but the one going on here is just disturbing."
 hide nao_v002
 hide satoko_v002
 with Dissolve(0.2)
 show jessica_v001 normal at mei_right
 show rika_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'What do you mean by... the top or bottom... of the Sonozaki house?'
 show jessica_v001 normal at inactive
 show rika_v002 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I think it's better if you didn't know, meep."
 call chapter_end
 jump chara482001_03