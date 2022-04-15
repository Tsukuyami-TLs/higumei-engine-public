label chara492001_03:
 show black_background onlayer black
 $ event_store.current_event='chara492001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara492001_03'
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
 show expression 'images/bg/AdvBg_2481.png' as bg
 play music "<loop 0>audio/bgm/BGM_EVENT_TOP_COLLAB3.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show ange_v001 fuan_close at mei_center
 with Dissolve(0.5)
 show ange_v001 fuan_close at active
 show ange_v001 fuan_close at chara_shake_transform
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...hic...... uu...'
 hide ange_v001
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_right
 show ange_v001 fuan_close at mei_left
 with Dissolve(0.5)
 show ange_v001 fuan_close at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'U-Uh... um...'
 show kazuho_v002 fuan at inactive
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "......Nn. I'm sorry I just flew out of the room all of a sudden."
 show kazuho_v002 fuan at inactive
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...I was just a bit surprised. You don't have to worry about me, so would you mind leaving me alone...?"
 show ange_v001 fuan at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...I apologize if I'm mistaken. Do you and Battler Ushiromiya-san have some sort of connection?"
 show kazuho_v002 normal at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Why would you think that?'
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Just... a feeling. The moment Battler-san entered the room and you saw his face, you got really surprised...'
 show ange_v001 normal at inactive
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'After that, I thought your face seemed happy for a split second... but then it clouded over with tension, your face drooping as if your feelings themselves were weighing it down...'
 show kazuho_v002 fuan_close at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Excuse me. Don't just randomly assume someone else's circumstances through speculation. ...In all honesty, it's unpleasant."
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at jump_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I... I'm sorry! B-But..."
 show ange_v001 normal at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "That look of delight turning straight into a depressed and solemn expression... is something I've even witnessed in my very own friends before."
 show ange_v001 normal at inactive
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Those two meet the person that they've been dying to see... but then, they can't convey what they want to that person..."
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "As I watch it happen... there's nothing I can do except pretend that I don't notice..."
 show kazuho_v002 fuan at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'But... I have been able to notice it. That those thoughts are filled with pain and agony...'
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I've lost my family in a similar way... and while my experience may not cover everything, I feel as though I can sympathize just a bit..."
 show kazuho_v002 fuan at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...By the way, we never told each other our names. What's yours?"
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh? Um... Kazuho Kimiyoshi.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide ange_v001
 hide kazuho_v002
 hide fade onlayer curtain
 show ange_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Kazuho... huh? I'm Ange Ushiromiya. Just as my name implies, I'm in the same Ushiromiya family as those two."
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'And so... that man, Battler, is my Onii-chan.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide ange_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at mei_right
 show ange_v001 normal_close at mei_left
 with Dissolve(0.5)
 show ange_v001 normal_close at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Th-then...?!'
 show kazuho_v002 odoroki at inactive
 show ange_v001 normal at active
 show ange_v001 normal at nod_transform
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Yes. Those people are from my "World", but 12 years back in 1986, they lost their lives on some island in an accident... no, in an "incident".'
 show kazuho_v002 odoroki at inactive
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'And so, I followed their tracks to investigate the truth of that day... and in that process, I got sucked into this village.'
 show ange_v001 normal_close at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'I-Is that how it went... then...?'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show ange_v001 normal_close at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'This "World" is set in 1983... so those two are destined to die in 3 years?!'
 show ange_v001 normal_close at inactive
 show kazuho_v002 sinken at active
 show kazuho_v002 sinken at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Th-then, we need to tell Battler-san and Jessica-san about what's gonna happen--!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show kazuho_v002 sinken at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "We can't. I can't let Onii-chan know about my name either. This is the one rule I had imposed on me that will serve to save him..."
 show kazuho_v002 sinken at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I couldn't have imagined that I would be able to meet them here, but even just seeing Onii-chan and Jessica Onee-chan in good health is... a miracle to me."
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'B-... But! If you have the chance to save their lives right now, doing nothing would forever--!'
 show kazuho_v002 fuan at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Let me ask you something instead. What do you plan on gaining from this strange experience in a past world?'
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show kazuho_v002 fuan at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Do you want to save someone important? \nDo you want to pin down the truth?\nIf this resulted in you feeling "ambivalence", which one would you intend on picking...?'
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Th-that... I......'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide ange_v001
 hide kazuho_v002
 hide fade onlayer curtain
 show ange_v001 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'At the very least, I want to pin down the truth of what happened on Rokkenjima. What happened on that island in October 1986...?'
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I cannot accept a reality where I remain ignorant about this.\n...That's why I will be resolute in following this rule."
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "This is the biggest chance I've been given on a whim to save Onii-chan, even if it makes it my first and last."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide ange_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 normal at mei_right
 show ange_v001 normal at mei_left
 with Dissolve(0.5)
 show ange_v001 normal at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...Ange-san, are you okay with that...?'
 show kazuho_v002 normal at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Yes, since it's a Fragment that even the Witch of Miracles has been unable to find."
 show ange_v001 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wi-witch...?'
 show kazuho_v002 fuan at inactive
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Pay no mind, just talking to myself. ...But, thank you. I feel like you\'ve helped me understand my reason in coming to this "World" more.'
 show kazuho_v002 fuan at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "The reason I've arrived here... is that--"
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide ange_v001
 hide kazuho_v002
 hide fade onlayer curtain
 show miyuki_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ah... you were over here! Man, we were wondering where you were, but you've been surprisingly close, huh?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide miyuki_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB3.ogg"
 show kazuho_v002 normal at mei_center
 with Dissolve(0.5)
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Mi-Miyuki-chan... Nao-chan...?'
 hide kazuho_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Please forgive Battler-san. He looks like he feels really sorry for it.'
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 sinken at mei_left
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5029_slap_back.wav'
 show battler_v001 fuan at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hey, get over here, Battler! You better apologize wholeheartedly for talking rudely to that girl!'
 show jessica_v001 sinken at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I-I get iiiittt... I didn't mean to say that, so it's my bad."
 show jessica_v001 sinken at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Can we make up? Ah-... in the meantime, please let me hear your name. '
 hide jessica_v001
 show ange_v001 normal_close at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '..........................................'
 show battler_v001 fuan at inactive
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'An-... I mean, "Gretel".'
 show ange_v001 normal_close at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Girdle? Like the thing you wear on your waist?'
 show battler_v001 normal at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'No, like the name. Call me "Gretel".'
 show ange_v001 normal at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'In that case, would you call me "Hansel"? ...Ihihihi, just kidding! I\'m Battler Ushiromiya! You can call me Battler. Nice to meet you.'
 show ange_v001 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Sorry about earlier. This village is extremely comfortable, so I kinda got carried away... Forgive me. I didn't mean it any other way."
 show battler_v001 fuan
 show battler_v001 fuan:
  yanchor 1.0
  linear 0.5 pos (1440,1250)
 pause 0.5
 show battler_v001 fuan:
  yanchor 1.0
  pos (1440,1250)
 show battler_v001 fuan at inactive
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...It's fine. I just got a bit surprised is all. It's over and done with."
 show ange_v001 normal_close at inactive
 show battler_v001 smile at active
 show battler_v001 smile:
  yanchor 1.0
  linear 0.5 pos (1440,1200)
 pause 0.5
 show battler_v001 smile:
  yanchor 1.0
  pos (1440,1200)
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Y-...yeah? Haah, that's relieving..."
 show ange_v001 normal_close at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So, now that that's out of the way, how's eating together sound? Looks like the doc's buying us some breakfast... but we can do lunch or even dinner. I'll treat you to anything!"
 hide ange_v001
 show jessica_v001 sinken at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "C-C'mooon Battler! You just apologized and you're already back to picking her up?! You're mad unprincipled!!"
 show jessica_v001 sinken at inactive
 show battler_v001 fuan at active
 show battler_v001 fuan at jump_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I told you it's not like that! ...Aah, in that case."
 play audio 'audio/sfx/SE_226_shine.wav'
 show jessica_v001 sinken at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Kazuho-chan, Miyuki-chan, Nao-chan. Do you know a nice restaurant around here? If you take me someplace, it's all on me!"
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 show miyuki_v002 fuan at mei_left
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'No. That would be a lifesaver for us, though...'
 show miyuki_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'U-Um... what are we going to do?'
 hide kazuho_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show ange_v001 smile at mei_left
 show battler_v001 smile at mei_right
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show ange_v001 smile at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "......Yes, gladly. I'm looking forward to your hospitality."
 show ange_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Alright, leave it to me! With all the food you're gonna get off of my treat, your stomach will get so full you'll inflate!"
 hide ange_v001
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Battler-san, putting it that way is...'
 hide battler_v001
 hide nao_v002
 with Dissolve(0.2)
 show kazuho_v002 normal at mei_center
 with Dissolve(0.5)
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 show kazuho_v002 smile_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(Right... Ange-san's reason in coming here...)"
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(Surely, she was thinking about meeting with her brother and talking with him...)'
 call chapter_end
 
 $ persistent.chara492001_done = True
 return