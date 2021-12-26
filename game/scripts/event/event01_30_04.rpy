label event01_30_04:
 show black_background onlayer black
 stop sound
 scene #000
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_2320.png' as bg
 with Dissolve(1.0)
 pause 2.0
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator 'The blankets in my bed had been stripped... and a blood-red magic circle could be seen painted on the sheets underneath.'
 narrator "Beatrice... an existence I don't believe in... drew this in my bed."
 show black_cover as fade with Dissolve(1.0)
 scene black_cover
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 narrator "Ah, in the end, Rokkenjima was indeed a witch's island.\nCursed... by its human inhabitants's lack of respect towards the being they dreaded."
 narrator 'Why does it have to be like this...? Why...?'
 narrator '...........................'
 stop music fadeout 2.0
 narrator "...Calm down. Think this over.\nC'mon... we talked about that, right?"
 narrator '...Was it the topic regarding Beatrice?\nNo... it was the talk about mystery and the occult.'
 stop sound
 scene black_cover
 camera at sepia_shader
 pause 0.0
 show expression 'images/bg/AdvBg_2291.png' as bg
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(1.0)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "You do have a point there, huh? While it may be a mystery if it can be explained, this might turn into something occult if it can't."
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'Since ancient times, things once assumed to be divine miracles have been successfully explained through science.'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Divine miracles cannot be explained. Meaning, if you can't figure them out, you may, fittingly, just call them as such."
 show black_cover as fade with Dissolve(1.0)
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator '...That\'s right. Isn\'t it just like what Mion-san and Shion-san said?\nIf something cannot be explained, "it" becomes a miracle... or in this case, a witch.'
 play music 'audio/bgm/BGM_TITLE_COLLAB2.ogg'
 narrator 'However, if it can be explained, there is no witch. Nor the occult. Nor fantasy.'
 narrator 'Didn\'t I also say it myself? "It\'s the battle between science and the occult, right?" ... and......'
 narrator 'Ah, then Erika-san said...'
 hide fade with Dissolve(1.0)
 show nao_v002 normal at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(1.0)
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika "More gracefully put, it's <Mystery versus Fantasy>."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '...Honestly, all of them, always with that "Detective Wanyan" nonsense!'
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 camera at reset_shader
 pause 0.0
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show expression 'images/bg/AdvBg_2190.png' as bg
 show nao_v002 sinken at mei_center
 with Dissolve(1.0)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao 'I\'m Team "Kaneda Case Files", all the way! In the name of my granny, I won\'t acknowledge any witches!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_5040_handclap.wav'
 pause 1.3333333333333333
 play audio 'audio/sfx/SE_5040_handclap.wav'
 narrator "At that moment, the mental fog inside of my head had finally been cleared.\nThat's when I hear the sound of hands clapping... paired with a laughing voice..."
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '...Thanks for the lovely scribble on my bedsheets.'
 show nao_v002 normal at active
 nao 'Perhaps an ordinary person would freak out seeing something like that? Well, too bad for you.'
 show nao_v002 normal_close at active
 nao "I may look like I'm still just a kid, but I'll have you know, I'm right in the middle of my rebellious phase!"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show nao_v002 sinken at active
 nao 'Since my room was locked, this creepy prank could only have been done by a witch!!'
 show nao_v002 sinken at active
 nao 'What a pretentious locked-room trick! All you did was make me more skeptical!! '
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v002 sinken at active
 nao 'If you are going to claim that you "exist", I\'m going to claim the opposite without fail!!'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao 'As if things like you "exist", Beatrice!!!\n'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 hide nao_v002
 with Dissolve(0.2)
 pause 1.0
 show beatrice_v001 futeki at mei_center
 with Dissolve(2.0)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice 'Hahahahaha, kkhhhahahhahaha!! My, my!'
 show beatrice_v001 futeki_close at active
 beatrice 'Quite the troublesome guest has come to bring me a present for my birthday this year!'
 show beatrice_v001 futeki at active
 beatrice "First and most importantly, you get to enjoy my greetings! And then, I'll have you subdued, kneeling before me and kissing my shoes!"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show beatrice_v001 futeki at active
 beatrice "Let us introduce ourselves once again! I am this island's master, the Golden Witch, Beatrice!!"
 camera at screenshake_transform
 pause 0.0
 show beatrice_v001 futeki at active
 beatrice 'And tomorrow is my birthday! <Happy Birthday>!! <Tooooo meeeeee>!!!'
 hide beatrice_v001
 with Dissolve(0.2)
 narrator 'The witch from the portrait was in a tremendously enthusiastic good mood.\nNevertheless, matching up to said high spirits would be just what my opponent wishes for.'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "I'm Nao Houtani. I'm going to spend my time gracefully admiring the roses while doing embroidery, and then I'll go back home the day after tomorrow."
 show nao_v002 sinken at active
 nao 'Neither you, nor your birthday have absolutely any chance of remaining in the memories of this lovely vacation!'
 hide nao_v002
 with Dissolve(0.2)
 narrator '...Where am I? When did I even end up in a place like this?'
 narrator "And then, there's the witch from the portrait mocking me like this. Not a chance. Inconceivable."
 narrator 'Whether she\'s there or not is something for me to settle from here on out. Does Beatrice "exist, or does she not?'
 narrator 'I pointed at the witch as if I was piercing her, and yelled with all of my strength.'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_5029_slap_back.wav'
 show nao_v002 sinken at active
 nao 'The deciding factors are not your tricks nor your magic!!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator 'Then, in declaration of war with the witch, I pointed my finger at my temple.'
 show beatrice_v001 futeki at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show beatrice_v001 futeki at inactive
 nao "The one who decides is me!! I'll take your mystery and unravel it with my very own mind!!"
 show beatrice_v001 futeki at active
 show nao_v002 sinken at inactive
 beatrice '*cackle*cackle*cackle*! This feeling is truly spectacular! This gets my blood {i}rushing{/i}!! Oh, what excitement! What pleasure! What an upsurge of emotion!!!'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "The questions of where I am and why I'm faced up against the witch right now... are trivial matters to me."
 narrator "I'm on the offensive side, and she's on the defensive. If we ended up this way, it's whatever."
 show beatrice_v001 futeki at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show beatrice_v001 futeki at inactive
 nao "I'm going to put an end to the mystery of your worthless pranks!! In the name of my granny!!!"
 show beatrice_v001 futeki at active
 show nao_v002 sinken at inactive
 beatrice "Hyaaahhhahahahaha!!! Spatter as much as you like! I'll make you surrender!! In the name of my granny!!!"
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Oh. Was she also... Team "Kaneda Case Files"?'
 show nao_v002 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice "Ooh, you're Team Kaneda too?! This island has far too many people on Team Wanyan!"
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao "...Comrade of mine. Let's fight fair and square."
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Mhm! Now, sit where you please, Nao! Shall we have fun again after all of this time?!'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_230_charge.wav'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 460)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 narrator 'In between the witch and I, a table and chairs appeared.'
 narrator "On top of the table, pieces seemed to have been lined up on a chessboard, but in a way that wasn't like the usual chess setup..."
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 stop music fadeout 0.5
 pause 1.0
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.ogg'
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "For my first move, I'll draw a magic circle on your bedsheets."
 show beatrice_v001 futeki at active
 show nao_v002 normal at inactive
 beatrice "It would have been a locked room? Then, the magic circle could only have been drawn with a witch's magic...!"
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao 'Oh, really? Next time, drawing the circle with goat blood would make it a bit more convincing.'
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao 'This magic circle prank has already been seen through, thanks to Mion-san.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Hoh? Why is it that just through the sheets, you can deny my existence as a witch?'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'Mion-san realized instantly how it was drawn with watercolor paint.'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao 'Actually, I wonder if you drew the magic circle with red paint {i}because{/i} your magic is too cheap to be able to draw in blood?'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 narrator "What's more, the paint hadn't even seeped past the sheets onto the bed."
 show beatrice_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao "You're pretty nice to the people in the mansion. You pulled this prank knowing the sheets could just be washed and re-set, didn't you?"
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'Which means that the culprit painted a magic circle onto some sheets beforehand, pulled off the sheets from my bed, then laid out the fake sheets in its place.'
 show beatrice_v001 futeki at updown_shake_transform,active
 show nao_v002 normal at inactive
 beatrice '*cackle*cackle*cackle*!! I see, I see. This prank has human spelled all over it, huh?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Allow me to say this outright, then. My magic paint circle was drawn with my faithful servants in mind.'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao "...I see? You didn't want to burden Shannon-san and the rest of the servants who believe in you."
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "And just like that, it's just a magic circle that can wash off easily?"
 show beatrice_v001 smile at mei_right
 show nao_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 show beatrice_v001 smile at inactive
 nao 'What a kind witch you are.'
 show beatrice_v001 futeki at active
 show nao_v002 normal_close at inactive
 beatrice 'Even with it drawn with paint, however, can you still deny that I drew it with magic?'
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice 'How would a Human be able to accomplish that? Only with you beginning to launch hypotheses as blue truths into my body will you be able to deny me.'
 show nao_v002 fuan at active
 show beatrice_v001 normal at inactive
 nao '.........?? Blue? What?'
 show beatrice_v001 fuan at active
 show nao_v002 fuan at inactive
 beatrice '...Uugggghhhhhh. ...I had to take the time to explain this to Battler around this point too...'
 show beatrice_v001 fuan_close at active
 show nao_v002 fuan at inactive
 beatrice 'If I get too carried away bullying her, would she get all depressed just like Battler did when I bullied him...?'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 play music 'audio/bgm/BGM_QUEST4_COLLAB2.ogg'
 pause 1.0
 show dlanor_v001 normal at mei_center
 with Dissolve(2.0)
 show dlanor_v001 normal at active
 dlanor 'If Lady Beatrice would like, I can take up that ROLE.'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice 'My, my... long time no see, Dlanor! I suppose you got tired of all of that stamping and fled here. *cackle*cackle*cackle*.'
 show nao_v002 fuan at active
 show beatrice_v001 futeki at inactive
 nao "Wh-, who's that?"
 show nao_v002 normal_close at active
 show beatrice_v001 futeki at inactive
 nao "Well, I {i}am{/i} facing off with {i}Beatrice{/i} right now. Whoever else appears shouldn't be a surprise."
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal_close at inactive
 dlanor 'Nao, I am your ALLY. Dlanor is my NAME.'
 show dlanor_v001 normal at active
 show nao_v002 normal_close at inactive
 dlanor "What you are looking over right now is the witch's GAME. According to the rules, winning is IMPOSSIBLE."
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "Rules? First it was club tabletops with punishment games, and now it's a witch's game. This won't be too boring."
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor "Nao, you should remember Erika's WORDS."
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '...<Mystery versus Fantasy>, right?'
 show dlanor_v001 normal_close at active
 show nao_v002 normal at inactive
 dlanor "EXACTLY. The witch's claim is that it would be impossible for a Human to perform the prank on your BED."
 show nao_v002 normal at active
 show dlanor_v001 normal_close at inactive
 nao "I see... And since it's impossible for a Human, it's magic. She's trying to say it was done by a witch."
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 beatrice "*cackle*cackle*cackle*. If you don't acknowledge me as a witch, nor acknowledge magic, I'll just have to show it to you myself."
 show beatrice_v001 futeki at active
 beatrice 'Do tell how could a Human could have drawn that magic circle!'
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'Nao, you may set up a HYPOTHESIS. This should demonstrate how a Human could have executed this in a concrete WAY.'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'It doesn\'t matter how far-fetched the argument is. And if your hypothesis is valid, it will become a "blue truth".'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '...Blue... truth......'
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'As the blue truth drills through the witch, she must disprove it or face DEFEAT.'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'So, this means I can say whatever nonsense I want about how a human could have performed this magic circle prank?'
 show dlanor_v001 normal_close at active
 show nao_v002 normal at inactive
 dlanor "That is CORRECT. Nonsense is FINE. Even if it's untrue, it does not MATTER."
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor "In the witch's game, the objective is to deny the existence of the WITCH."
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'Even if it is nonsense, if you hypothesize a crime that is possible with human hands, that will end in your WIN.'
 show nao_v002 smile at active
 show dlanor_v001 normal at inactive
 nao 'Understood. ...Okay. Since any kind of argument is fine, it is possible that a human did it, somehow.'
 hide dlanor_v001
 show beatrice_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 fuan_close at active
 show nao_v002 smile at inactive
 beatrice "You catch on quite fast... Will you let me dig out the dirt from under your nails afterwards? I'll mix it in with Battler's tea leaves!"
 show nao_v002 normal at active
 show beatrice_v001 fuan_close at inactive
 nao 'The magic circle prank can be performed by a human. While we were absent, someone sneakily entered the room and was able to do the prank. Like that?'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'That is not a valid argument. Have you forgotten, Nao? That the room was locked?'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'As you had went out to have dinner, the room should have been locked.'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'From the point you came back to the room to retire for the night up until you found the magic circle, the room should have been locked.'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "...Then, how's this?"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao '{umi_blue}Although it is a locked room, it is possible for a human with a master key to enter and perform the prank.{/umi_blue}'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show beatrice_v001 normal at inactive
 nao 'Did that work?!'
 show beatrice_v001 normal_close at active
 show nao_v002 sinken at inactive
 beatrice 'I would appreciate it if you were a bit more specific.'
 show beatrice_v001 normal at active
 show nao_v002 sinken at inactive
 beatrice 'For instance, {i}who{/i} could have possibly had the master key?'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "Then I'll say something more daring."
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 sinken at active
 show beatrice_v001 normal at inactive
 nao '{umi_blue}The servant Shannon-san has a master key. Through that, she used the key to unlock the door, enter the room, and perform the prank!{/umi_blue}'
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_5036_glass_break.wav'
 show crack_effect
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.ogg'
 show beatrice_v001 futeki at active
 show nao_v002 sinken at inactive
 beatrice '{umi_red}Shannon was not involved in performing the act of drawing the magic circle!{/umi_red}'
 show nao_v002 odoroki at active
 show beatrice_v001 futeki at inactive
 nao 'But how...?! On what grounds?!'
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 odoroki at inactive
 dlanor 'Nao, this is the red TRUTH.'
 show dlanor_v001 normal at active
 show nao_v002 odoroki at inactive
 dlanor 'The red truth speaks of nothing but the undeniable TRUTH. The basis behind it has no need to be EXPLAINED.'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 beatrice "*cackle*cackle*cackle*! It's just as she says. The red truth is simply the truth!"
 show beatrice_v001 futeki at active
 beatrice 'Why and how is it so? Looking past all of that, it simply shows the truth.'
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show dlanor_v001 normal at inactive
 nao "...That's... so unreasonable..."
 show dlanor_v001 normal at active
 show nao_v002 fuan at inactive
 dlanor 'Please calm yourself, NAO. ...The red truth may be a merciless counter attack, but it simultaneously gives clues as WELL.'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "Like how I was at least given out the hint that Shannon-san didn't draw the magic circle, right...?"
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'Just as you SAY. As you send out more blue truths, the witch will retaliate with red TRUTHS.'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'Letting that pile up... the truth behind this magic circle locked-room incident will jut out further and further.'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 fuan at mei_center
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 beatrice "Naooo, please do let me dig out the dirt from your naaaillss! Battler's going to love drinking iiiit!"
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'Okay, NAO. This is your game NOW. Please challenge it to your LIKING.'
 show nao_v002 smile at active
 show dlanor_v001 normal at inactive
 nao '...Got it. Thanks.'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "First, let's try to get the conditions in order."
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator "Between me being called out to have dinner and me leaving my room, I hadn't left once until then. Of course, by that time, nothing was wrong with my bed."
 narrator 'And when we left the room, we locked it.'
 narrator 'After dinner, Jessica-san joined in, and we played a board game.'
 narrator "Then, when we went back to go to sleep, we unlocked the room. ...That's when we saw the magic circle."
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'Thinking about it normally, the crime could have been done while we were having dinner.'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'The only person who could have entered at that time... was Shannon-san.'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'When you requested her to check out the window lock, Shannon-san went up to the second floor and unlocked your room with the master key.'
 show nao_v002 normal_close at active
 show dlanor_v001 normal at inactive
 nao "That's when Shannon-san gained the opportunity to perform the magic circle prank."
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'As a matter of fact, Beatrice had said this in the red truth just earlier.'
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '{umi_red}Shannon was not involved in performing the act of drawing the magic circle.{/umi_red}'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '...is what she said, right?'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'What a roundabout way of saying it. Then, another way of saying this is that someone {i}did perform{/i} the crime of drawing the magic circle...?'
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "{umi_blue}Shannon-san didn't draw the magic circle, but she could have laid the sheets with the magic circle on my bed.{/umi_blue}"
 show dlanor_v001 normal_close at active
 show nao_v002 normal at inactive
 dlanor 'This is VALID. It is possible that someone else could have prepared the magic circle sheets in hiding beforehand, while Shannon could have entered with THEM.'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 normal at mei_center
 with Dissolve(0.5)
 show red_cover as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show beatrice_v001 normal at active
 beatrice "{umi_red}Shannon was not involved in any way, directly or indirectly, in the act of laying the sheet with a magic circle on Nao's bed.{/umi_red}"
 hide beatrice_v001
 with Dissolve(0.2)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Too indirect?'
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice "This isn't just a matter of directly laying the magic circle sheets on the bed. This means it includes {i}any{/i} act that led to this result, even without knowing it."
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "So, this means... Shannon-san hasn't even cooperated with the culprit even without knowing."
 narrator 'For example, though, the culprit could have prepared those sheets in particular beforehand.'
 narrator 'By the time the paint was on, it was transparent, though, so this magic circle could have been drawn with paint that fades over time. In that sense, these sheets are just any old sheets.'
 narrator "Shannon-san could have been intending to lay on some normal white sheets, but afterwards, the color set in, and they became the magic circle sheets. In this case, a third party could have done this in good faith, and she wouldn't have been involved at all."
 show dlanor_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'But Shannon likely did not go to your room to change the sheets in the first place, though? She should have simply went to check on the window lock.'
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor 'The timeframe that Shannon went up to the second floor and came back down was as fast as can BE.'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal_close at mei_center
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 nao "...That's right. Thinking about it normally, no matter how much of an expert she is at bedmaking, it's unthinkable how it could be done in such a short timeframe."
 show nao_v002 normal at active
 nao 'Moreover, she even came back from the room as soon as we had broached the topic of the window lock.'
 show nao_v002 normal at active
 nao "It just so happened that she gained that chance from going upstairs. But even in that chance, Shannon-san having those magic circle sheets hidden on her at all isn't realistic."
 show nao_v002 normal at active
 nao "...Beatrice. Wouldn't this be too boring if this argument was just about Shannon-san straying from us? Make this clear for me."
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'At times like this, you can have her repeat what you SAY. Allow me to try IT.'
 show dlanor_v001 normal at active
 dlanor 'Repeat it in RED. "From the point the girls left the room to eat dinner to the point they returned, not once did Shannon touch the SHEETS."'
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show dlanor_v001 normal at inactive
 beatrice "Very well. I'll repeat it."
 show red_cover as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice '{umi_red}From the point the girls left the room to eat dinner to the point they returned, not once did Shannon touch the sheets.{/umi_red}'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao 'Thanks. Now I can approach this from a different direction.'
 show nao_v002 normal_close at active
 nao "...I can't just put the blame on Shannon-san. ...I need to think about it differently."
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 normal at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor '...Lady Beatrice has also changed quite a LOT.'
 show beatrice_v001 normal_close at active
 show dlanor_v001 normal at inactive
 beatrice "Oh, hush. Battler's game in particular was an exception."
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice 'Tonight is nothing in comparison to the endless torture between him and I back then. I just wanted to have a little fun.'
 show dlanor_v001 smile_close at active
 show beatrice_v001 smile at inactive
 dlanor 'When I return to heaven, I must report that you have also been turned into a peaceful LADY.'
 show beatrice_v001 smile at active
 show dlanor_v001 smile_close at inactive
 beatrice '*cackle*cackle*cackle*. Doesn\'t my name mean Eternal Lady? ...Well, "Eternity" is unpleasant, though.'
 show beatrice_v001 futeki at active
 show dlanor_v001 smile_close at inactive
 beatrice 'If I get tired of "Lady" too... would it give rise to another hideously behaving person...?'
 hide dlanor_v001
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao 'Umm, repeat this in red.'
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao '"To get to the second floor of the guesthouse, you must absolutely pass through the front area of the first floor."'
 show beatrice_v001 futeki at updown_shake_transform,active
 show nao_v002 normal at inactive
 beatrice "*cackle*cackle*cackle*. I know what you're trying to say. Instead, I'll say something more specific."
 show red_cover as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show beatrice_v001 futeki at active
 show nao_v002 normal at inactive
 beatrice '{umi_red}No one visited the second floor of the guesthouse from the time you locked the door until you opened it again, except for Shannon.{/umi_red}'
 show nao_v002 normal_close at active
 show beatrice_v001 futeki at inactive
 nao "...Thanks. ...I'm starting to think a human can do this less and less, but there is an important hint there."
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Shannon-san is not the only one to have a master key. All servants have a master key.'
 narrator 'After Shannon-san went to fix the window lock, we had been there on the first floor playing a board game the whole time.'
 narrator 'In that timeframe, there is a possibility that someone other than Shannon-san who had a master key could have sneakily went up to the second floor and committed the crime.'
 show beatrice_v001 futeki at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao 'But thanks to your red truth, all of those possibilities have been snuffed out.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'The night is short. Allow me to tack on some more red truths for you out of generosity.'
 stop music fadeout 2.0
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '{umi_red}No one visited the second floor of the guesthouse from the time you locked the door until you opened it again, except for Shannon.{/umi_red}'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show red_cover as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_5036_glass_break.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '{umi_red}Going upstairs any other way than using the stairs, such as sawing through the walls or gliding in from the sky, is unforgivable. Any other means of reaching the second floor can therefore be denied.{/umi_red}'
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.ogg'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show nao_v002 fuan at active
 show beatrice_v001 normal at inactive
 nao 'Wha-... Then, that means going in from the window is...'
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice '*cackle*cackle*cackle*cackle*! Until Shannon fixed it, the window was unlocked. I suppose you thought someone broke into the guesthouse through there?'
 show nao_v002 fuan_close at active
 show beatrice_v001 futeki at inactive
 nao 'Bullseye... I thought the culprit climbed the wall and came in through the window...'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'At first, when they said nonsense was fine, I thought just saying any crime that was possible for a human would result in me winning.'
 narrator 'But despite that... of course, the witch is used to this game.'
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'I see... it really is like Erika-san said.'
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'What is IT...?'
 show nao_v002 normal_close at active
 show dlanor_v001 normal at inactive
 nao 'Mysteries have offensive and defensive components.'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "In this witch's game... I have a winning condition, but the fact witch's side doesn't is strange."
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'If I demonstrate that the crime is possible for a human, I win.'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "However, the witch's side has no winning condition. Until I win, my opponent can only..."
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'Basically, this is a game of back and forth wits, where we just compete until the witch loses.'
 narrator 'But with back and forth wits... there are drawbacks.'
 show beatrice_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao "Amidst the chaos of throwing logic back and forth at each other... I'll get tired and start feeling like I don't care about the end result... This is a drawback for me."
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice "That's right, Nao. ...You really do understand fast."
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'The outcome of this witch game offers nothing for my side.'
 show beatrice_v001 futeki at active
 show nao_v002 normal at inactive
 beatrice 'Win or lose, the human side has an upper hand. ...*cackle*cackle*cackle*cackle*!'
 show nao_v002 normal_close at active
 show beatrice_v001 futeki at inactive
 nao "...This is bad. Shannon-san wasn't involved when she entered, and on top of that, absolutely no one else even went up to the second floor."
 show nao_v002 fuan at active
 show beatrice_v001 futeki at inactive
 nao "At a glimpse, it feels like a crime impossible for a human. When I get tired out, I'll start wanting to acknowledge the witch."
 show nao_v002 sinken at active
 show beatrice_v001 futeki at inactive
 nao "But I hate losing! I haven't been cornered at all!"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 show beatrice_v001 futeki at inactive
 nao "Your red truths won't shoot through me. I'll launch over this precipice and wedge into the heart of fantasy!!"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "I absolutely won't lose until I admit my defeat! This means I'm absolutely {i}going{/i} to win!"
 show dlanor_v001 odoroki at mei_center
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 dlanor 'How SURPRISING. ...You are insanely GIFTED.'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_center
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 beatrice "Now, this night isn't meant to be eternal torture, it's meant to be fun. Again, the night is short."
 show beatrice_v001 normal at active
 beatrice 'Originally, I would have wanted to force you to play against me eternally until you got bored, however...'
 show beatrice_v001 normal at active
 beatrice "Let's cut it off here for now."
 show beatrice_v001 normal at active
 beatrice "Your stay is only two nights and three days long, isn't it? Until then, let's see if you can expose my pranks!"
 hide beatrice_v001
 with Dissolve(0.2)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "...If I lose, is there a punishment game? You're a witch, so you can be extraordinarily gruesome with it."
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'I am enjoying myself with a rare visitor. There will be no punishment games.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice "Rather, if you can defeat me, why don't I bestow a gift upon you?"
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao 'I like that idea. ...That makes me wanna go at it more.'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 show black_cover as fade with Dissolve(1.0)
 hide fade with Dissolve(1.0)
 with Dissolve(1.0)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao "...Eh? ...What? It's gotten dark already."
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'Goodbye, NAO. We shall meet in the next TWILIGHT.'
 show beatrice_v001 futeki at active
 show dlanor_v001 normal at inactive
 beatrice "I'm also looking forward to this. *cackle*cackle*cackle*..."
 show white_cover as fade with Dissolve(3.0)
 return