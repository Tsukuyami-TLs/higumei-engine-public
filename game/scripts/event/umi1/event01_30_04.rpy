label event01_30_04:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=4
 $ event_store.current_chapter='event01_30_04'
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
 show expression 'images/bg/AdvBg_2320.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST7_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 2.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'The blankets on my bed had been stripped off... and a blood-red magic circle could be seen painted on the sheets underneath.'
 narrator "Beatrice... an existence I don't believe in... drew this on my bed."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 narrator "Ah, in the end, Rokkenjima was indeed a witch's island.\nCursed... by its human inhabitants' lack of respect towards the being they dreaded."
 narrator 'Why did it have to be like this...? Why...?'
 narrator '...........................'
 stop music fadeout 2.0
 narrator "...Calm down. Think this over.\nC'mon... we talked about that, right?"
 narrator '...Was it the topic regarding Beatrice?\nNo... it was the talk about mystery and the occult.'
 stop sound
 show expression 'images/bg/AdvBg_2291.png' as bg
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 camera at sepia_shader
 pause 0.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That's true. When you're able to solve it, it's considered a mystery, but unresolved ones often become part of the occult."
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Since ancient times, things once assumed to be divine miracles have successfully been explained through science.'
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Divine miracles cannot be explained. The idea here being, whatever you can't explain gets written off as a divine miracle."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator '...That\'s right. Isn\'t it just like what Mion-san and Shion-san said?\nIf something cannot be explained, "it" becomes a miracle... or in this case, a witch.'
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB2.ogg"
 narrator 'However...\nIf it can be explained, then there is no witch. No occult. No fantasy.'
 narrator 'Didn\'t I also say it myself? \n"It\'s the battle between science and the occult, right?"'
 narrator 'Ah, then Erika-san said...'
 show erika_v001 normal_close at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "More gracefully put, it's <Mystery versus Fantasy>."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '...Honestly, all of them, always with that "Detective Wanyan" nonsense!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 camera at reset_shader
 pause 0.0
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 hide fade onlayer curtain
 with Dissolve(1.0)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I\'m Team "Kaneda Case Files", all the way! In the name of my granny, I won\'t acknowledge any witches!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_5040_handclap.wav'
 pause 1.3333333333333333
 play audio 'audio/sfx/SE_5040_handclap.wav'
 narrator "At that moment, the mental fog inside my head finally cleared.\nThat's when I heard the sound of hands clapping, paired with a laughing voice..."
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Thanks for the lovely scribble on my bedsheets.'
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Perhaps an ordinary person would freak out seeing something like that? Well, too bad for you.'
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I may look like I'm still just a kid, but I'll have you know, I'm right in the middle of my rebellious phase!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Since my room was locked, this creepy prank could only have been done by a witch?!'
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'What a pretentious locked-room trick! All you did was make me more skeptical!! '
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'If you are going to claim that you "exist", I\'m going to claim the opposite without fail!!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'As if things like you "exist", Beatrice!!!\n'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 hide nao_v002
 with Dissolve(0.2)
 pause 1.0
 show beatrice_v001 futeki at mei_center
 with Dissolve(2.0)
 show beatrice_v001 futeki at active
 show beatrice_v001 futeki at updown_shake_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Hahahahaha, kkhhhahahhahaha!! My, my!'
 show beatrice_v001 futeki_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Quite the troublesome guest has come to bring me a present for my birthday this year!'
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "First and most importantly, you'll get to enjoy a greeting from me! Afterwards, I'll have you subdued, kneeling before me and kissing my shoes!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Let us formally introduce ourselves! I am this island's master, the Golden Witch, Beatrice!!"
 camera at screenshake_transform,reset_shader
 pause 0.0
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'And tomorrow is my birthday! \n<Happy Birthday!!> <Tooooo meeeeee!!!>'
 hide beatrice_v001
 with Dissolve(0.2)
 narrator 'The witch from the portrait was in a tremendously enthusiastic mood.\nNevertheless, matching up to said high spirits would be just what my opponent wished for.'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm Nao Houtani. I'm going to spend my time gracefully admiring the roses while doing embroidery, and then I'll go back home the day after tomorrow."
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Neither you, nor your birthday have absolutely any chance of remaining in my memories of this lovely vacation!'
 hide nao_v002
 with Dissolve(0.2)
 narrator '...Where am I? When did I even end up in this place?'
 narrator 'To make matters worse, the witch from the portrait is mocking me like this. Not a chance. Inconceivable.'
 narrator 'Whether she\'s there or not is something for me to settle from here on out. Does Beatrice "exist", or does she not?'
 narrator 'I pointed at the witch as if I was piercing her, and yelled with all of my strength.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_5029_slap_back.wav'
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The deciding factors are neither your tricks nor your magic!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Then, in a declaration of war with the witch, I pointed my finger at my temple.'
 show nao_v002 sinken at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "The one who decides is me!! I'll take your mystery and unravel it with my very own mind!!"
 show nao_v002 sinken at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*! This feeling is truly spectacular! This gets my blood {i}rushing{/i}!! Oh, what excitement! What pleasure! What an upsurge of emotion!!!'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "The questions of where I am and why I'm faced up against the witch right now... are trivial matters to me."
 narrator "I'm the claimant, and she's the defendant. If we ended up this way, it is what it is."
 show nao_v002 sinken at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm going to put an end to the mystery of your worthless pranks!! \nIn the name of my granny!!!"
 show nao_v002 sinken at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Hyaaahhhahahahaha!!! Spatter as much as you like! I'll make you surrender!! In the name of my granny!!!"
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Oh. Was she also... Team "Kaneda Case Files"?'
 show beatrice_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Ooh, you're Team Kaneda too?! This island has far too many people on Team Wanyan!"
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Comrade of mine. Let's fight fair and square."
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Mhm! Now, sit where you please, Nao! It's been a long time since I've had this much fun!"
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_230_charge.wav'
 camera:
  parallel:
   linear 0.5 pos (960, 460)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 narrator 'In between the witch and I, a table and chairs appeared.'
 narrator "On top of the table, pieces seemed to have been lined up on a chessboard, but in a way that wasn't like the usual chess setup..."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 stop music fadeout 0.5
 pause 1.0
 play music "<loop 0>audio/bgm/BGM_QUEST3_COLLAB2.ogg"
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "For my first move, I've drawn a magic circle on your bedsheets."
 show nao_v002 normal at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "It would have been a locked room, wouldn't it? Then, the magic circle could only have been drawn with a witch's magic...!"
 show beatrice_v001 futeki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Oh, really? Next time, drawing the circle with goat blood would make it a bit more convincing.'
 show beatrice_v001 futeki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'This magic circle prank has already been seen through, thanks to Mion-san.'
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Hoh? Why is it that just through the sheets, you can deny my existence as a witch?'
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Mion-san realized instantly that it was drawn with watercolor paint.'
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Actually, I wonder if you drew the magic circle with red paint {i}because{/i} your magic is too cheap to be able to draw in blood?'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 narrator "What's more, the paint hadn't even seeped past the sheets onto the bed."
 show nao_v002 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "You're pretty nice to the people in the mansion. You pulled this prank knowing the sheets could just be washed and re-set, didn't you?"
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Which means that the culprit painted a magic circle onto some sheets beforehand, pulled off the sheets from my bed, then laid out the fake sheets in its place.'
 show nao_v002 normal at inactive
 show beatrice_v001 futeki at active
 show beatrice_v001 futeki at updown_shake_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*!! I see, I see. This prank has human spelled all over it, huh?'
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Allow me to say this upfront, then. My magic paint circle was drawn with my faithful servants in mind.'
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I see? You didn't want to burden Shannon-san and the rest of the servants who believe in you."
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "And just like that, it's just a magic circle that can wash off easily?"
 show nao_v002 normal_close at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'What a kind witch you are.'
 show nao_v002 normal_close at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Even with it having been drawn with paint, can you deny that I drew it with magic?'
 show nao_v002 normal_close at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'How would a Human be able to accomplish that? Only by beginning to launch hypotheses as blue truths into my body will you be able to deny me.'
 show beatrice_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '.........?? Blue? What?'
 show nao_v002 fuan at inactive
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...Uugggghhhhhh. ...I had to take the time to explain this to Battler around this point too...'
 show nao_v002 fuan at inactive
 show beatrice_v001 fuan_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'If I get too carried away bullying her, would she get all depressed just like Battler did when I bullied him...?'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 play music "<loop 0>audio/bgm/BGM_QUEST4_COLLAB2.ogg"
 pause 1.0
 show dlanor_v001 normal at mei_center
 with Dissolve(2.0)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'If Lady Beatrice would like, I can take up that ROLE.'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 futeki at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'My, my... long time no see, Dlanor! I suppose you got tired of all of that stamping and fled here. *cackle*cackle*cackle*.'
 show beatrice_v001 futeki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Wh-who's that?"
 show beatrice_v001 futeki at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Well, I {i}am{/i} facing off with {i}Beatrice{/i} right now. Whoever else appears shouldn't be a surprise."
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal_close at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Nao, I am your ALLY. Dlanor is my NAME.'
 show nao_v002 normal_close at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "What you are confronted with right now is the witch's GAME. If you don't follow the rules, winning will be IMPOSSIBLE."
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Rules? First it was club tabletops with punishment games, and now it's a witch's game. I hope this won't be too boring."
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "Nao, you should remember Erika's WORDS."
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...<Mystery versus Fantasy>, right?'
 show nao_v002 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "EXACTLY. The witch's claim is that it would be impossible for a Human to perform the prank on your BED."
 show dlanor_v001 normal_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I see... And since it's impossible for a Human, it's magic. She's trying to say it was done by a witch."
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "*cackle*cackle*cackle*. If you don't acknowledge me as a witch, nor acknowledge magic, you'll just have to show me yourself."
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Do tell how could a Human could have drawn that magic circle!'
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Nao, you may set up a HYPOTHESIS. This should demonstrate how a Human could have executed this in a concrete WAY.'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'It doesn\'t matter how far-fetched the argument is. And if your hypothesis is valid, it will become a "blue truth".'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Blue... truth......'
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'As the blue truth drills through the witch, she must disprove it or face DEFEAT.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'So, this means I can say whatever nonsense I want about how a human could have performed this magic circle prank?'
 show nao_v002 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "That is CORRECT. Nonsense is FINE. Even if it's untrue, it does not MATTER."
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "In the witch's game, the objective is to deny the existence of the WITCH."
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Even if it is nonsense, if you hypothesize a crime that is possible with human hands, that will end in your VICTORY.'
 show dlanor_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Understood. ...Okay. Since any kind of argument is fine, it is possible that a human did it, somehow.'
 hide dlanor_v001
 show beatrice_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show beatrice_v001 fuan_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "You catch on quite fast... Will you let me dig out the dirt from under your nails afterwards? I'll mix it in with Battler's tea leaves!"
 show beatrice_v001 fuan_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The magic circle prank could have been performed by a human. While we were absent, someone sneakily entered the room and was able to do the prank. Like that?'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'That is not a valid argument. Have you forgotten, Nao? That the room was locked?'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'As you went out to have dinner, you locked the room.'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Until you retired to your room and found the magic circle, the room should have been locked.'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...How's this, then?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade onlayer curtain
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '{umi_blue}Although it is a locked room, it is possible for a human with a master key to enter and perform the prank.{/umi_blue}'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Did that work?!'
 show nao_v002 sinken at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I would appreciate it if you were a bit more specific.'
 show nao_v002 sinken at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'For instance, {i}who{/i} could have possibly had the master key?'
 show beatrice_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Then I'll say something more daring."
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show beatrice_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '{umi_blue}The servant Shannon-san has a master key. Through that, she used the key to unlock the door, enter the room, and perform the prank!{/umi_blue}'
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_5036_glass_break.wav'
 show crack_effect
 play music "<loop 0>audio/bgm/BGM_QUEST3_COLLAB2.ogg"
 show nao_v002 sinken at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '{umi_red}Shannon was not involved in performing the act of drawing the magic circle!{/umi_red}'
 show beatrice_v001 futeki at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But how...?! On what grounds?!'
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 odoroki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Nao, this is the red TRUTH.'
 show nao_v002 odoroki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'The red truth speaks of nothing but the undeniable TRUTH. The basis behind it has no need to be EXPLAINED.'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "*cackle*cackle*cackle*! It's just as she says. The red truth is simply the truth!"
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Why and how is it so? Looking past all of that, it simply shows the truth.'
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...That's... so unreasonable..."
 show nao_v002 fuan at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Please calm yourself, NAO. ...The red truth may be a merciless counter attack, but it simultaneously gives clues as WELL.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Like how I was at least given the hint that Shannon-san didn't draw the magic circle, right...?"
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Just as you SAY. As you send out more blue truths, the witch will retaliate with red TRUTHS.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Letting those pile up... the truth behind this magic circle locked-room incident will jut out further and further.'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 fuan at mei_center
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Naooo, please do let me dig out the dirt from your naaaillss! Battler's going to love drinking iiiit!"
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Okay, NAO. This is your game NOW. Please challenge it to your LIKING.'
 show dlanor_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Got it. Thanks.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "First, let's try to get the conditions in order."
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'We did not leave our room at all until we were called out for dinner. \nOf course, by that time, nothing was wrong with my bed.'
 narrator 'And when we did leave the room, we locked it.'
 narrator 'After dinner, Jessica-san joined in, and we played a board game.'
 narrator "Then, when we went back to go to sleep, we unlocked the room. ...That's when we saw the magic circle."
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Thinking about it normally, the crime could have been done while we were having dinner.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The only person who could have entered at that time... was Shannon-san.'
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'When you requested her to check out the window lock, Shannon-san went up to the second floor and unlocked your room with the master KEY.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's when Shannon-san gained the opportunity to perform the magic circle prank."
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But as a matter of fact, Beatrice had said this in the red truth just earlier.'
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '{umi_red}Shannon-san was not involved in performing the act of drawing the magic circle.{/umi_red}'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Right?'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'What a roundabout way of saying it. Another way of saying this, then, is that someone can perform the crime without drawing the magic circle...?'
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "{umi_blue}Shannon-san didn't draw the magic circle, but she could have laid the sheets with the magic circle on my bed.{/umi_blue}"
 show nao_v002 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'This is VALID. It is possible that someone else could have prepared the magic circle sheets in hiding beforehand, while Shannon could have entered with THEM.'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 normal at mei_center
 with Dissolve(0.5)
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "{umi_red}Shannon was not involved in any way, directly or indirectly, in the act of laying the magic circle sheets on Nao's bed.{/umi_red}"
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Indirectly?'
 show nao_v002 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "This isn't just a matter of directly laying the magic circle sheets on the bed. This means it includes {i}any{/i} act that led to this result, even without knowing it."
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "So, this means... Shannon-san hasn't even cooperated with the culprit unknowingly."
 narrator 'For example, though, the culprit could have prepared some unique sheets beforehand.'
 narrator 'But by the time the paint was on, it was transparent, so this magic circle could have been drawn with paint that fades in over time. In that sense, these sheets are just any old sheets.'
 narrator "Suppose Shannon-san entered in order to lay on some normal white sheets, but afterwards, the color set in, and they became the magic circle sheets. In this case, she as a third party could have done this in good faith, and she wouldn't have been involved at all."
 show beatrice_v001 normal at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Shannon probably didn't go to your room to change the sheets in the first place, though? She simply should have went in to check on the window lock."
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'The timeframe that Shannon went up to the second floor and came back down was as short as can BE.'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal_close at mei_center
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...That's right. Thinking about it regularly, no matter how much of an expert she is at bedmaking, it's unthinkable that it could have been done in such a short timeframe."
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Moreover, she even came back from the room as soon as we had broached the topic of the window lock.'
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It just so happened that going upstairs gave her that chance. It's unrealistic for Shannon-san to have had the magic circle sheets on her the entire time, just for that possibility."
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Beatrice. Wouldn't this be too boring if this argument was just about Shannon-san straying from us? Make this clear for me."
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'At times like this, you can have her repeat what you SAY. Allow me to try IT.'
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Repeat it in RED. "From the point the girls left the room to eat dinner to the point they returned, not once did Shannon touch the SHEETS."'
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Very well. I'll repeat it."
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '{umi_red}From the point the girls left the room to eat dinner to the point they returned, not once did Shannon touch the sheets.{/umi_red}'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Thanks. Now I can approach this from a different direction.'
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I can't just put the blame on Shannon-san. ...I need to think about it differently."
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Lady Beatrice has also changed quite a LOT.'
 show dlanor_v001 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Oh, hush. Battler's game in particular was an exception."
 show dlanor_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Tonight is nothing in comparison to the endless torture between him and I back then. I just wanted to have a little fun.'
 show beatrice_v001 smile at inactive
 show dlanor_v001 smile_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'When I return to Heaven, I must report that you have also been turned into a peaceful LADY.'
 show dlanor_v001 smile_close at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*. Doesn\'t my name mean Eternal Lady? ...Well, "Eternity" is unpleasant, though.'
 show dlanor_v001 smile_close at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'If I get tired of "Lady" too... would it give rise to another hideously behaving person...?'
 hide dlanor_v001
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Umm, repeat this in red.'
 show beatrice_v001 futeki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '"To get to the second floor of the guesthouse, you must absolutely pass through the front area of the first floor."'
 show nao_v002 normal at inactive
 show beatrice_v001 futeki at active
 show beatrice_v001 futeki at updown_shake_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "*cackle*cackle*cackle*. I know what you're trying to say. Instead, I'll say something more specific."
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show nao_v002 normal at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '{umi_red}No one visited the second floor of the guesthouse from the time you locked the door until you opened it again, except for Shannon.{/umi_red}'
 show beatrice_v001 futeki at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Thanks. ...I'm starting to think a human could do this less and less, but there is an important hint there."
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Shannon-san is not the only one to have a master key. All servants have a master key.'
 narrator 'After Shannon-san went to fix the window lock, we had been there on the first floor playing a board game the whole time.'
 narrator 'In that timeframe, there is a possibility that someone other than Shannon-san who had a master key could have sneakily went up to the second floor and committed the crime.'
 show nao_v002 normal at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But thanks to your red truth, all of those possibilities have been snuffed out.'
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'The night is short. Allow me to tack on some more red truths for you out of generosity.'
 stop music fadeout 2.0
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '{umi_red}No one visited the second floor of the guesthouse from the time you locked the door until you opened it again, except for Shannon.{/umi_red}'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_5036_glass_break.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '{umi_red}Going upstairs through any other way than using the stairs, such as sawing through the walls or gliding in from the sky, is not permitted. Any other means of reaching the second floor can therefore be denied.{/umi_red}'
 play music "<loop 0>audio/bgm/BGM_QUEST3_COLLAB2.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show beatrice_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Wha-... Then, that means going in from the window is...'
 show nao_v002 fuan at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*cackle*! Until Shannon fixed it, the window was unlocked. I suppose you thought someone broke into the guesthouse through there?'
 show beatrice_v001 futeki at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Bullseye... I thought the culprit climbed the wall and came in through the window...'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'At first, when they said nonsense was fine, I thought just saying any crime that was possible for a human would result in me winning.'
 narrator 'But despite that... of course, this game is something the witch is {i}accustomed to{/i}.'
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I see. ...It actually is like Erika-san said.'
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'What IS...?'
 show dlanor_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Mysteries have offensive and defensive components.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "In this witch's game... I have a winning condition, but the fact that the witch's side doesn't is strange."
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'If I demonstrate that the crime is possible for a human, I win.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "However, the witch's side has no winning condition. Until I win, my opponent can only..."
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'Basically, this is a game of back and forth wits, where we just compete until the witch loses.'
 narrator 'But with back and forth wits... there are drawbacks.'
 show nao_v002 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Amidst the chaos of throwing logic back and forth at each other... I might get tired and start feeling like I don't care about the end result... This is a drawback for me."
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "That's right, Nao. ...You really do understand fast."
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'The outcome of this witch game offers nothing for my side.'
 show nao_v002 normal at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Win or lose, the human side has the upper hand. ...*cackle*cackle*!'
 show beatrice_v001 futeki at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...This is bad. Shannon-san wasn't involved when she entered, and on top of that, absolutely no one else even went up to the second floor."
 show beatrice_v001 futeki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "At a glimpse, it feels like a crime impossible for a human. When I get tired out, I'll start wanting to acknowledge the witch."
 show beatrice_v001 futeki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "But I hate losing! I haven't been cornered at all!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform,reset_shader
 pause 0.0
 show beatrice_v001 futeki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Your red truths won't shoot through me. I'll launch over this precipice and wedge into the heart of fantasy!!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "I certainly can't lose until I admit my defeat! This means I'm {i}certainly{/i} going to win!"
 show dlanor_v001 odoroki at mei_center
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'How SURPRISING. ...You are incredibly GIFTED.'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_center
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Now, this night isn't meant to be eternal torture, it's meant to be fun. Again, the night is short."
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Originally, I would have wanted to force you to play against me eternally until you got bored; however...'
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Let's cut it off here for now."
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Your stay is only two nights and three days long, isn't it? Until then, let's see if you can expose my pranks."
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...If I lose, is there a punishment game? You're a witch, so you could be extraordinarily gruesome with it."
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I am enjoying myself with a rare visitor. There will be no punishment games.'
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Rather, if you can defeat me, why don't I bestow a gift upon you?"
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I like that idea. ...That makes me wanna go at it more.'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Huh? It's fading to black?"
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Goodbye, NAO. We shall meet in the next TWILIGHT.'
 show dlanor_v001 normal at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "I'm also looking forward to this. *cackle*cackle*cackle*..."
 show white_cover onlayer curtain as fade with Dissolve(3.0)
 call chapter_end
 jump event01_30_05