label chara482001_03:
 show black_background onlayer black
 $ event_store.current_event='chara482001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara482001_03'
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
 show expression 'images/bg/AdvBg_331.png' as bg
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB3.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show battler_v001 smile at mei_left
 show keiichi_v002 smile at mei_right
 with Dissolve(0.5)
 show keiichi_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Wahahahahaha!!!'
 show battler_v001 smile at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Hahahahahaha!!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show hanyuu_v002 fuan at mei_left
 show jessica_v001 sinken at mei_right
 with Dissolve(0.5)
 show jessica_v001 sinken at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...Regardless, those two seem to be getting along.'
 show hanyuu_v002 fuan at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Battler sure is a lively guy. We had so many people with us that we had to sit at separate tables, but still, doesn't it seem like he forgot he came here with a bunch of girls?"
 hide jessica_v001
 hide hanyuu_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_515_tableware.wav'
 Character('Waitress',ctc="ctcArrow", ctc_position="fixed") 'Your order is ready, sorry to keep you waiting. Enjoy~'
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Th-thank you very much...'
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...But yeah, that seriously is a sick uniform. Are things like that actually in fashion now? The place has a ton of customers, and it seems like it's doing well..."
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'd get kinda skeptical if my dad said he wanted to invest in a place like this."
 hide jessica_v001
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show jessica_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show jessica_v001 fuan_close at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Is that so...? Well, one of my relatives runs this place.'
 show shion_v002 normal at inactive
 show jessica_v001 odoroki at active
 show jessica_v001 odoroki at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Eh?! R-Really?!'
 show jessica_v001 odoroki at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Huh, didn't I mention that earlier?"
 show shion_v002 smile at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'S-Sorry... that outfit hit me like a brick, so it went in one ear and out the other.'
 hide shion_v002
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 fuan at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah, no worries. I think that reaction's normal."
 hide jessica_v001
 hide mion_v002
 with Dissolve(0.2)
 show rena_v002 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau~, but maybe Rena wouldn't be opposed if a bunch more of these family restaurants with kyute uniforms sprang up, sprang up?"
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 show nao_v002 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yeah. I have the same opinion as Rena-chan.'
 hide rena_v002
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "When have you ever objected to Rena-chan's opinion?"
 show miyuki_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Never. No way I would. If Rena-chan said something was white, and it was really black, I would also insist it was white. '
 show nao_v002 normal at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Such terrifying dedication...'
 hide nao_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-Ahahaha.'
 hide kazuho_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ah... but wow, the food is delicious. The way they plated it is intricate too, making it even more attractive.'
 show jessica_v001 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Of course; they put a ton of effort into preparing the food. Attractiveness is essential in getting repeat customers, y'know?"
 show mion_v002 smile at inactive
 show jessica_v001 smile_blush at active
 show jessica_v001 smile_blush at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I see, so there's more to the restaurant than just the uniforms.\n...Mmm, and the taste!"
 hide mion_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile_blush at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Their sweet food is really tasty too! We're gonna have some afterwards, au au!"
 hide jessica_v001
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Only Hanyuu wants to eat that stuff.'
 hide hanyuu_v002
 hide rika_v002
 with Dissolve(0.2)
 call wipeout_routine
 call wipein_routine
 show battler_v001 smile at mei_left
 show keiichi_v002 smile at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_577_ls_sanriokirakira.wav'
 show keiichi_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Now that's a precious sight..."
 show battler_v001 smile at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Just by looking at it... I feel my chest swelling up.'
 hide keiichi_v002
 hide battler_v001
 with Dissolve(0.2)
 call wipeout_routine
 call wipein_routine
 show miyuki_v002 odoroki at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Woah, so the guys can even get their fill of food just from the sight of the uniforms.'
 show miyuki_v002 odoroki at inactive
 show mion_v002 normal_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...They really are taking it way too far, huh? Wonder if we're gonna have to rake over the coals."
 show miyuki_v002 odoroki at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Shion, we\'re preparing "that thing". ...You know what I\'m talking about, right?'
 hide miyuki_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Yes, of course. Shall we give them a taste of how terrifying this restaurant can really be...? *cackle*cackle*!'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(W-What exactly are Mion-san and Shion-san planning.....?)'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v002 smile at mei_right
 show rena_v002 smile at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Oh... it\'s here, it\'s here! Our long-awaited "thing"~!'
 show mion_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'I wonder why this thing... is a small plate of chocolate, of chocolate?'
 show rena_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I asked them for one of the sweets they're making next season. This is... Russian Roulette Chocolate! "
 show rena_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'One of the chocolates here is the "bullet" that will gush out hot sauce when bitten into. So, whoever bites the bullet loses!'
 hide rena_v002
 hide mion_v002
 with Dissolve(0.2)
 show hanyuu_v002 fuan at mei_left
 show miyuki_v002 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, I just wanted normal, tasty chocolate...'
 show hanyuu_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, and you can't tell from a glance which one the bullet is either."
 hide hanyuu_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Of course. There wouldn't be any point in doing it if it was that simple to figure out. ...Now, are you two ready?"
 hide miyuki_v002
 hide shion_v002
 with Dissolve(0.2)
 show battler_v001 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I see, so this is what a club activity is...\nSounds fun. I'm in!"
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Heheh, right?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide jessica_v001
 hide battler_v001
 hide fade onlayer curtain
 show mion_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 play audio 'audio/sfx/SE_5050_gong.wav'
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'The one rule is that once you pick up a chocolate, you absolutely must eat it! Now, fiery hot chocolate battleeee, begin!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide mion_v002
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
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Alright, I'm safe! Isn't Battler-san up next~?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide fade onlayer curtain
 show battler_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...O-Oooooh! Got it! Next round, I'm definitely shooting a blank...!"
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide battler_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/card/Card_482001.png' as bg
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Alright, let's go! My pick is... this chocolate in the middle!"
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Oh my... *giggle*, is that really your choice? I think you still have time to look at it a little more closely, though~. *cackle*cackle*!'
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Heh... stay out of this! You misled me once with that bluff earlier, but you won't get me again!"
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "When in doubt, choose the one in the middle! I'm choosing this red chocolate! Uoooooooooooohhhhhhhh!!!!"
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_331.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show battler_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'AAAAAAAAAHHHHH!!! Hot, hot, uoooooohhhh!!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rena_v002 odoroki at mei_left
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau?! Battler chose the bullet again?!'
 show rena_v002 odoroki at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'How many times has Battler-san lost now?'
 hide rena_v002
 show rika_v002 normal at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. He's had three battles and lost three times."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide satoko_v002
 hide rika_v002
 hide fade onlayer curtain
 show battler_v001 fuan_close at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 fuan_close at active
 show battler_v001 fuan_close at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hiiiihh, hot, hooot!! What's up with this gouging, piercing pain?!"
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Isaythatbutit'slikemyentiremouthisgettingshockednoit'smorethanthat {i}it'ssearingwhatisthisITBURNSITBURNSOOHMYMOUTHBUR-{/i}... AHHHWHATISTHISHORRIBLEFEELIIIIIINGGGG??!!"
 camera at screenshake_transform
 pause 0.0
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hiiiiiiiiiiiiiiiiiiiihhhhhhiiiiiiiiiiiiiiiiiiiiiihhh!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5012_icerock.wav'
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "H-... here! Here's some water, Battler-san!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide fade onlayer curtain
 show battler_v001 fuan_close at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Thank----guh?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show miyuki_v002 normal at mei_right
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 show kazuho_v002 sinken at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "By the way, one of the guys in police housing that really loves spicy stuff told me... that drinking water when you're suffering from the effects of spicy food will only make the pain worse."
 show miyuki_v002 normal at inactive
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jump_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh....?!'
 hide miyuki_v002
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... so the spicy stuff will mix with the water and spread everywhere in your mouth...?'
 hide kazuho_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So essentially by drinking water, what you're doing is the same as dusting the entire inside of your mouth with spicy stuff?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rena_v002
 hide nao_v002
 hide fade onlayer curtain
 show battler_v001 fuan_close at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'GUUUUOOOOOOOOOOHHHHHHHHHHH!!!!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Aaaaahhhhh!! Sorrysorrysorry!!'
 hide kazuho_v002
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_center
 with Dissolve(0.5)
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'H-Hey, hey, hey, are you okay, Battler?'
 hide jessica_v001
 with Dissolve(0.2)
 show hanyuu_v002 fuan at mei_left
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "A-Au au au, scary...! I'm glad I didn't pick the spicy chocolate...!"
 show hanyuu_v002 fuan at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. I wanted Hanyuu to pick one of the spicy chocolates, but Battler drew all of them instead.'
 hide rika_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show keiichi_v002 odoroki at mei_center
 with Dissolve(0.5)
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Huh?! Does that mean Battler deliberately took the bullets in order to protect us...?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide keiichi_v002
 hide fade onlayer curtain
 show battler_v001 fuan_close at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hiiiiiiiiiiiiihhhh!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show shion_v002 fuan at mei_left
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Nope, that definitely wasn't why he drew them."
 show shion_v002 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Excuse me, but can I please get a glass of milk? Make it iiiice cold if you can.'
 hide miyuki_v002
 hide shion_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_right
 show battler_v001 fuan_close at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Sorry, Battler-san! I-I had no idea that water would make it worse...!'
 show kazuho_v002 fuan at inactive
 show battler_v001 fuan_close at active
 show battler_v001 fuan_close at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "N-No... it's okay. You didn't think of doing it to screw me over, right...?"
 show kazuho_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So... so this is what it's like to have the satisfaction of... being taken care of by thick-breasted babes in your last moments..."
 show kazuho_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "It's... that... \nLong ago, something like this... must... have..."
 show battler_v001 fuan
 show battler_v001 fuan:
  yanchor 1.0
  linear 0.5 pos (480,1280)
 pause 0.5
 show battler_v001 fuan:
  yanchor 1.0
  pos (480,1280)
 play audio 'audio/sfx/SE_5001_sitdown2.wav'
 show kazuho_v002 fuan at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '......happ...ened...'
 camera at screenshake_transform
 pause 0.0
 show battler_v001 fuan_close at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh?! H-his head just jerked! It jerked!'
 hide battler_v001
 hide kazuho_v002
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_right
 show keiichi_v002 odoroki at mei_left
 with Dissolve(0.5)
 show keiichi_v002 odoroki at inactive
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hey, Battler?! Battler--?!'
 show jessica_v001 odoroki at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Stay with us, Battleeeeeer!!'
 hide keiichi_v002
 hide jessica_v001
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...His face is completely drained of color.'
 show rika_v002 fuan at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "It feels like we're about to see angels come grab his soul."
 hide shion_v002
 hide rika_v002
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_left
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'What is up with this person? It seems his hidden ability is being unlucky...?'
 show satoko_v002 fuan at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "On top of that it seems like, how do I say this... like he's the type to be terrible at doubting what people say?"
 hide satoko_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Who would force a bullet onto someone in Russian Roulette...? Maybe he's not really one for that kind of psychological warfare."
 hide mion_v002
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... His luck could be bad, but maybe he's even worse at observation, at observation?"
 hide nao_v002
 hide rena_v002
 with Dissolve(0.2)
 show mion_v002 fuan at mei_center
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I think he's an honest guy, but if he can't learn how to doubt people in our games, he probably won't ever win."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 show mion_v002 fuan at inactive
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Uuuu, I've had enough of this game..."
 call chapter_end
 
 $ persistent.chara482001_done = True
 return