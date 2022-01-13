label chara462001_01:
 show black_background onlayer black
 $ event_store.current_event='chara462001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara462001_01'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2220.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST6_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 show erika_v001 smile at chara_shake_transform,active
 erika 'Aah, I do offer my humblest welcome! For my master, with a loving spirit, I do---'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '............'
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 erika '... U-um... my master? I do see that your face is quite pale...'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'My... is that so? But I am in good health, and my heart is as clear as the darkness of the depths of the ocean.'
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 erika 'That... that is, I am highly honored to know that, but would it happen that you are, um...... angered? '
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "...Angered? Me? My my, how vexing. I can't think of any reason why I would be angered as if there was hot lava boiling in my chest. "
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Although... I wonder if it could be that you had something else in mind?'
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Aah... there is, isn't there? Like how my own piece is a shameful loser that has brought public humiliation upon me..."
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika "Hih... hiiiiiiiiiiiiiiiih??? You, you couldn't have heard of the other day, with that girl...?!"
 show erika_v001 odoroki_close at active
 erika 'N-... no, um, uh! I-I can assure you, that was only a minor playfight with an irrelevant brat...!'
 show erika_v001 sinken at jump_transform,active
 erika 'I-I never lost! If the game continued at that rate, my victory would have been absolutely certain! Not once was I shaken!'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Is that so? If that's the case, then perhaps it would have been better if you had waited it out instead... did you think of that?"
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'When you win against another piece, you get carried away. Your habit of being so conceited as a piece of mine is so pitiful, I have to laugh.'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 erika 'Huh? Um, what was that about another piece?'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...Were you not listening to what I said? Had you or had you not just heard about how conceited you are?'
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at chara_shake_transform,active
 erika 'Nn-noooo! I-I would never be anything close to conceited, absolutely not...!!'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...My, really? But isn\'t it indicative of conceit how you retaliated so poorly, left an opening for yourself out of negligence, and got eaten up? That "blue" couldn\'t even shoot down your opponent...'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika 'N-, AH?! W-WHO RATTED ME OU-... I mean! How could word of this nonsense have ever reached your greatness?!'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'There is no need for explanation. Even though you lost, I thought it was ever so entertaining to have seen, although...'
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...I never could have expected you to be a competent mirror of me anyway... *giggle*.'
 Character('????',ctc="ctcArrow", ctc_position="fixed") "In any case, I'll have to properly reward you for dragging your master's face through the mud, right...?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 erika 'P-p-ple-please wait, my master?! At least if you would hear me out this once! And then you can rethink i--?!'
 play audio 'audio/sfx/SE_335_ls_magmafire.wav'
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika '... ngyappabrigigeraan, gohaheegagagaaaaa?!!'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 play music "<loop 0>audio/bgm/BGM_QUEST5_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika "DDDLLLAAAAANNNNNOOORRRRRRRRR!! YOU'D BETTER RESPOND RIGHT NOW, DLAAAANOOOOORRRRRR!!!!!"
 show dlanor_v001 normal at mei_right
 with Dissolve(1.0)
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor '...You CALLED, Erika? Your face is all black, and your dress is SINGED, almost like a fire or something STARTED.'
 show erika_v001 sinken at active
 show dlanor_v001 normal at inactive
 erika 'It\'s not "almost like"; an actual fire started! It seriously turned everything to white ash, and I thought it was going to spread everywhere...!'
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor '...If you scatter it in the mountains, will beautiful flowers bloom in SPRING?'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show erika_v001 smile at active
 show dlanor_v001 normal at inactive
 erika 'Yes, absolutely. If I were to sip sake under those sakura trees, the beginning of my logic story would take off fr--'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 show dlanor_v001 normal at inactive
 erika 'LIKE HELLL IT WOUUUUUUUUUUUULDDDDDDD!!!!!!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show dlanor_v001 smile_close at active
 show erika_v001 fuan at inactive
 dlanor 'It was a JOKE.'
 show erika_v001 sinken at updown_shake_transform,active
 show dlanor_v001 smile_close at inactive
 erika "Hahh, hahh, hahh... wait, it's weird for you to be doing something like telling jokes. Has something good happened?"
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor "NO. Nothing in PARTICULAR... Hadn't Lady Bernkastel just punished YOU?"
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 futeki at active
 show dlanor_v001 normal at inactive
 erika 'Exactly that! For me to have been able to receive such punishment, of course it was done by none other than my master!'
 show dlanor_v001 fuan at active
 show erika_v001 futeki at inactive
 dlanor '...Why is Erika so boastful of this FACT?'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/card/Card_462001.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 erika 'ANYWAYS! In order to help rid my master of her displeasure, I must absolutely fight a second time!'
 erika "A few days ago was Beatrice's birthday, so I let them have their fun, but..."
 erika "Though I have regrettably departed from my friends, for my master's sake, I must once again show Nao-san my superiority over her!"
 erika "Beatrice has securing a route to Nao-san, and luckily, they're are still preparing for travel."
 erika "If I move now, I will also have no worries of someone getting in my way. In other words, Dlanor, you're coming with me!"
 erika '*cackle*cackle*... This time for sure will be a perfect game; with me as a detective and as a Wanyanner, I will thoroughly crush her!!!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show dlanor_v001 normal_close at mei_right
 show erika_v001 smile at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show erika_v001 smile at inactive
 dlanor '-- I will DECLINE.'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show dlanor_v001 normal_close at inactive
 erika 'Huuh? W-why is that?!?'
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor 'The Great Court does approve of private DUELS. Venting emotions is to be judged as the highest blasphemy against the mystery GENRE.'
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor 'Last time, the game board was brought about by a MIRACLE. I merely accompanied you to inspect its CONTENTS.'
 show dlanor_v001 fuan_close at active
 show erika_v001 odoroki at inactive
 dlanor '...Furthermore, I have a huge pile of work I should be FINISHING. I ask that the one going will be you and only YOU.'
 show erika_v001 sinken at chara_shake_transform,active
 show dlanor_v001 fuan_close at inactive
 erika 'H... Very well! I thought that you would understand my feelings as a friend, though...!'
 show erika_v001 sinken at active
 show dlanor_v001 fuan_close at inactive
 erika 'Now, as for the item here that I have been lent by my master, it will take me to where Nao-san is...'
 show erika_v001 odoroki at active
 show dlanor_v001 fuan_close at inactive
 erika "Huh? Even though it was supposed to return to my own game board a while ago, it's gone...? No, I can't find it...?"
 show erika_v001 sinken at active
 show dlanor_v001 fuan_close at inactive
 erika 'I wonder if this is also the fault of the "{i}lost child{/i}". Haah, this is so annoying... If it\'s like this, I suppose I\'ll have to go directly and summon it back to this space.'
 hide erika_v001
 with Dissolve(0.6)
 show dlanor_v001 fuan at active
 dlanor "...Is she GONE? If she didn't have those huge jumps in emotion, she would be quite the outstanding character, HOWEVER..."
 show dlanor_v001 fuan_close at active
 dlanor "...I guess it can't be HELPED."
 call chapter_end
 jump chara462001_02