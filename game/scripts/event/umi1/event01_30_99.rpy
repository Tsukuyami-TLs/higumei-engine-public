label event01_30_99:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=9
 $ event_store.current_chapter='event01_30_99'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop sound
 show expression 'images/bg/AdvBg_2320.png' as bg
 hide fade onlayer curtain
 with Dissolve(2.0)
 pause 1.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'H-............'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 odoroki at mei_left
 show mion_v002 sinken at mei_right
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show shion_v002 odoroki at active
 show shion_v002 odoroki at jump_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'What happened? .........Heee?!?! S-Sis...!!'
 show shion_v002 odoroki at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...They've... done it..."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator 'The story goes back to when I first found the magic circle on my bed sheet.'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'W-... what is this...'
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 narrator "Mion-san and Shion-san's beds had... nothing on top of them, but my bed alone was {i}murdered{/i}..."
 narrator 'The blanket was torn off disastrously... exposing the sheets underneath as if they were skin... skin that was... dyed red with blood...'
 narrator "No. It's not just dyed red. There is... something drawn on... with a red, blood-like substance..."
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'A.........  magic circle.........'
 play music "<loop 0>audio/bgm/BGM_EVENT_TOP_COLLAB2.ogg"
 hide nao_v002
 with Dissolve(0.2)
 narrator 'I was enraptured by that horrible magic circle. That was when the Sonozakis spoke.'
 narrator "Heee?!?! S-Sis...!! \n...They've... done it..."
 narrator "The following is an exchange that only the Sonozaki sisters can hear. I was so terrified that I couldn't even hear it."
 show shion_v002 sinken at mei_left
 show mion_v002 futeki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 futeki at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...That's... Bright-sama's magic circle?!?!"
 show shion_v002 sinken at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "They... They're not half bad... This is a magnificent reproduction..."
 show mion_v002 futeki at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Sis... did you notice...?'
 show shion_v002 sinken at inactive
 show mion_v002 sinken at active
 show mion_v002 sinken at jump_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Of course... The way that the pillows and blankets are messed up... it perfectly recreates the scene from the movie!'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator "For a long time, I was confused as to why Shannon-san wasn't bothered by the magic circle."
 narrator 'But... Mion-san instantly understood. She knew that Shannon-san was also deep into the Wanyan swamp.'
 narrator 'Mion-san remembered the question Erika-san had asked Shannon-san after she returned from fixing the lock on the window upstairs.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2331.png' as bg
 camera at sepia_shader
 pause 0.0
 show erika_v001 normal at mei_right
 show shannon_v001 smile at mei_left
 with Dissolve(0.5)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show shannon_v001 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Excellent work, Shannon-san. Has a robber broken into the window or anything?'
 show erika_v001 normal at inactive
 show shannon_v001 smile_close at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'No. Please be at ease.'
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Mion-san thought that felt out of place.'
 narrator "It sounded like a sarcastic remark from Erika-san... but it only sounded that way if you weren't in the know."
 narrator 'Why did she ask if something happened in the room?'
 narrator 'Mion-san instantly understood. Erika-san knew that Shannon-san was a Wanyanner.'
 narrator 'I heard about it myself after dinner that night when she came out to me as a Wanyanner.'
 narrator 'So, I wanted to confirm with her that it was indeed the magic circle from the film.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 camera at reset_shader
 pause 0.0
 show black_cover as bg
 narrator 'Now, Shannon-san had originally not planned to go to the room upstairs.'
 narrator 'She only had to go upstairs because I suddenly mentioned the lock on the window.'
 narrator "So, at that point, I'm sure Erika-san was panicking internally."
 narrator "That's because it was {i}me{/i} who was supposed to be the first to discover the magic circle prank and be surprised."
 narrator 'And at the same time, it would have been a fun joke to share with her fellow Wanyanners, Mion-san and Shion-san.'
 narrator 'However, since Shannon-san is also a hardcore Wanyanner, she immediately understood the meaning of the magic circle, so she just smiled and ignored it.'
 narrator 'This fact was confirmed by Erika-san when she asked Shannon-san after coming down the stairs.'
 narrator 'Mion-san understood it instantly.\nBoth why Shannon-san could ignore it and that the culprit was Erika-san were answers that could be derived in seconds.'
 narrator 'In other words, the moment the magic circle was discovered, the Sonozaki sisters knew everything, from the meaning of the magic circle, to the culprit being Erika-san.'
 narrator 'While I was cowering in fear at the magic circle... the Wanyan-adoring Sonozaki sisters must have been laughing at me with disgusting smiles.'
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 play music "<loop 0>audio/bgm/BGM_BATTLE1_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator "...And... from here on it's a world beyond my understanding.\nIt's said that monsters are drawn to each other, but who would've thought that'd turn out to be true..."
 narrator 'Mion-san and Shion-san instantly got a grasp on the situation.\nWhat could Erika-san, who had drawn this perfect recreation of the circle from the movie, possibly want?'
 narrator 'A compliment? Or a shocked scream? ...No, it was an {i}audience{/i}.'
 narrator "That's right. In that moment, across the wall in Erika-san's room... one more Wanyanner was listening intently, letting out a disgusting laugh."
 camera at screenshake_transform,reset_shader
 pause 0.0
 narrator 'Erika-san... who wanted to hear the admiration of her magic circle by comrades, was listening... with a cup pressed against the wall... She was listening the whole time!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "*giggle*... What do you think? Isn't my magic circle a masterpiece...?\nIsn't it a perfect recreation of Bright-sama's magic circle...?"
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Now, do allow me to hear your praise, Mion-san and Shion-san!!\nI've already satisfied myself with the screams of Nao-san, who refuses to watch Detective Wanyan."
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Nwext, I want to hear your cries of admirationnNNIHIHIHI!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "Erika-san strains her ears more and more. She wants to know Mion-san and Shion-san's reactions, so she focuses all of her attention into her hearing...!!"
 play audio 'audio/sfx/SE_5046_scratch.wav'
 narrator '...Ssskk......'
 narrator 'It was a small, strange sound.\nIt was almost inaudible... but it was {i}as if it was pressed right up against her ear{/i}.'
 narrator "...No way. ......No, it can't be..."
 narrator "A bead of cold sweat appeared on Erika-san's face.\n...As it slowly ran down Erika-san's forehead... her expression... was colored with... an eerie joy."
 camera at screenshake_transform,reset_shader
 pause 0.0
 narrator "These... these people...... they couldn't have......!?!"
 narrator "That's right. As Erika-san listened to the voices in the next room over with the cup pressed against the wall..."
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 narrator '...there was {i}a creepy pair of laughs mimicking the exact way Erika-san had just laughed{/i}.'
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Ha...... haha............ ah.'
 hide erika_v001
 with Dissolve(0.2)
 narrator "Those two... {i}they're listening to me{/i}!!!"
 narrator "I've drawn a perfect magic circle, and am now listening through the wall for voices of admiration... but at the same time they're listening to me!!!"
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 narrator 'On either side of the wall separating the two rooms... was one giant slug and two giant slugs... listening to each other through the wall with cups.'
 camera at screenshake_transform,reset_shader
 pause 0.0
 narrator '<G-Good>, <Gooderrrrrr>... <Goodeeeeeeeesssssstttt!!!>'
 narrator 'The next day, as if to say, "Now it\'s your turn.", Erika-san purposely forgot to lock the door.'
 narrator 'Even though they knew it was a trap, the Sonozaki sisters decided to take advantage of this... so Shion-san returned to the guesthouse under the guise of retrieving some luggage.'
 narrator "And then, she went into Erika-san's room to set up the prank with the magic circle."
 narrator 'Furthermore, the sheet with the magic circle was prepared in advance. ...The Sonozaki sisters worked all night on it after I had used the sleeping pills to fall asleep!'
 narrator 'Then, Shion-san falls for the trap with the fluorescent paint on the doorknob.'
 narrator 'Shion-san exercised a certain amount of caution, but as expected, she was unaware of the substance Erika had prepared herself.'
 narrator "So, there should certainly have been fluorescent paint on Shion-san's hands. Erika-san should have been able to checkmate her with that!"
 narrator "But... the Sonozaki sisters were not so naive after all.\nThat's right. After we returned, the two fought and ran into the shower together."
 narrator 'I was just smiling at how close the two were, fighting over who would go first in the shower.'
 narrator '...But the two of them, were doing this deliberately.'
 narrator "They switched at that time. When they heard Erika-san's scream and ran out of the shower, they had switched places."
 narrator "The two of them didn't underestimate Erika-san... They had suspected something had been attached to them that they couldn't percieve! "
 narrator 'The purpose of the shower was to wash that away, and more importantly, switch the sisters.'
 narrator 'But, Erika-san is crazy enough to call herself a great detective.'
 narrator 'When nothing came up after shining on Shion-san\'s hand with the blacklight, and she started crying out, "That\'s impossible!"... it wasn\'t frenzied scream of despair, but rather, of great delight.'
 narrator 'In Erika-san\'s words... "Knox\'s 10th: It is forbidden to disguise yourself as another person without any clues."'
 narrator 'However, Erika-san had met the sisters, introduced herself, and knew that they were identical twins.'
 narrator '"Identical twin sisters.", Erika-san had said herself on the boat to Rokkenjima.'
 narrator 'Therefore, "It is EFFECTIVE.".\nA disguise that does not violate Knox\'s 10th. No, a swap...!'
 narrator "At that moment, Erika-san could have immediately illuminated Mion's hand with her blacklight."
 narrator "If she did that, I would've seen Mion-san's hands illuminated with fluorescent paint."
 narrator "But she didn't... why? Isn't she supposed to be tougher than that?"
 camera at screenshake_transform,reset_shader
 pause 0.0
 narrator 'No. It was respect... awe... reverence...!'
 narrator 'Erika-san had great admiration for the Sonozaki sisters, who had responded not only with their love as Wanyanners, but also with all their might in a battle of wits.'
 narrator 'Dlanor-san told me. Erika-san is a great actor, who can play both the detective and the culprit.'
 narrator "That's why she responded to the Sonozaki sisters with such a shameful and outwitted display of dismay."
 narrator 'No, perhaps it was even a reenactment of a particularly ill-tempered culprit in Detective Wanyan.'
 narrator 'These three days and two nights on Rokkenjima, for me alone, have been a horror and a mystery.'
 narrator 'As for the other three... it was a fan meetup for those who love Wanyan the giant slug...'
 stop music fadeout 2.0
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2271.png' as bg
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_2221.png' as bg
 call wipein_routine
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_2251.png' as bg
 call wipein_routine
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Of course! Feel free to come over and play again!! Next time, we'll pull an all-nighter having a board game showdown! Right?"
 hide jessica_v001
 with Dissolve(0.2)
 Character('Krauss Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'The servants say that they have learned a great deal from your stay. You have our thanks.'
 Character('Natsuhi Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Thank you for completing the questionnaire as well. We will read it carefully and make good use of it in the future.'
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I've put my all into it! Please definitely read it to the end!"
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "We'll take responsibility for it! Because we're the consultants for the new resort on Rokkenjima!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator 'When it was time to leave, even the Ushiromiya family members came to see us off.'
 narrator "If I come here again... I'd like to take it easier. Otherwise... I may as well try cosplay too... maybe."
 show kanon_v001 normal_close at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show kanon_v001 normal_close at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") 'Shannon would like to express her apologies for not being able to see you off.'
 show kanon_v001 normal_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Today's her day off. It can't be helped. Do give her my regards, for we are comrades under the giant slug!"
 $ event_store.current_progress = 10
 show erika_v001 normal at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '...Um, I think that quote was... "{note_green}There are always two truths.{/note_green}"'
 play audio 'audio/sfx/SE_226_shine.wav'
 show kanon_v001 normal at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'There are always two truths! Do you read it too?'
 hide erika_v001
 hide kanon_v001
 with Dissolve(0.2)
 show jessica_v001 fuan_blush at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show jessica_v001 fuan_blush at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I... uh, might also like to do a cosplay photo shoot next time.'
 show nao_v002 smile at inactive
 show jessica_v001 smile_blush at active
 show jessica_v001 smile_blush at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "You know, when that time comes, why don't we do it together, \nNao-chan? I'm sure it won't be as embarrassing if we're in it together."
 show jessica_v001 smile_blush at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "*giggle*... You're right. ...Let's make our cosplay debut together."
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'Among the people who see us off, the witch is mixed in with the crowd.\nOf course, no one can see her though.'
 show beatrice_v001 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'It was a pleasure to spend my birthday with you, Nao.'
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Thank you. But, I'd like to ask something... how old exactly are you?"
 show nao_v002 smile at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*! I have forgotten over the course of a thousand years!'
 show nao_v002 smile at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "You are always welcome to come play again. Next time, I'll show you the golden rose garden of the Golden Land!"
 show beatrice_v001 futeki at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'll bring a game console too. I'll show you just how good I am."
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'I pray for your good FORTUNE. Wishing you the BEST.'
 show dlanor_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Thank you. I would have liked to spend more time speaking with you. See you again.'
 hide dlanor_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Since I'm a detective, wherever an incident may occur, you'll find me. So, I don't think I will ever see you again."
 show erika_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's okay. There's the Detective Wanyan collab cafe. I'll probably be there, so we'll see each other again then."
 show nao_v002 smile at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") ".........*giggle*giggle*. <Good> When you do, let's talk about our favorite characters to the fullest. "
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Come visit us in Hinamizawa some time, Erika-san! We definitely won't let you get bored!"
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'I want to see you face off with Kei-chan. \nThe Magician of Words vs The Great Detective. I wonder who will win?'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Oh? A Magician of Words? A magician, just like the alias of that culprit in The Kaneda Case Files! Wonderful!'
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Whenever anyone has a case, I, Erika Furudo, shall promise to come to your aid!'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Alternatively, we can go to Angel Mort and have a long casual talk over all-you-can-eat dessert.☆'
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'd love to invite someone fun and tough like you to the Hinamizawa Branch School."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Definitely. ...Erika-san's energy and reasoning skills are like a combination of Mion-san and Rena-chan."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade onlayer curtain
 show erika_v001 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'One day, absolutely.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '*giggle*...Just with the presence of a few friends that are reluctant to depart, this level of farewell is possible for Erika Furudo. What do you think, everyone?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 futeki at mei_center
 with Dissolve(0.5)
 show nao_v002 futeki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '<Good!>'
 show white_cover onlayer curtain as fade with Dissolve(2.5)
 window hide None
 hide nao_v002
 with Dissolve(0.2)
 pause 3.0
 play sound ['audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav'] fadeout 1.0
 stop sound
 show expression 'images/bg/AdvBg_2101.png' as bg
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...What's with the letter that you received, Erika-san?"
 show nao_v002 smile at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Do ignore it. I am only the messenger. I have merely been entrusted with this message to give to my master.'
 show nao_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It seems that Beatrice has written a lot about me. I look forward to seeing what's inside."
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Speaking of which... Beatrice said she had a present for me too...'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 odoroki at mei_right
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show shion_v002 fuan at inactive
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ehh? What?! Did you get a present on Rokkenjima?!'
 show mion_v002 odoroki at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That's nice. We didn't get anything at all."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Actually, I think the witch's present for Nao-san was intended for all three of you."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Why don't you have a look in your luggage?"
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'After she says that, I take a look through my luggage.\nSitting inside, was a small present box that I had never seen before.'
 narrator "There's a message card attached... As I thought, it's from Beatrice."
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator '"In honor of your visit to Rokkenjima. -From The Golden Witch"'
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah-, it's that portrait! Could it be the 20 billion yen's worth of gold bars?"
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "There's something like an inscription in front of the portrait. They say it's a riddle, and solving it leads to the location of the gold bars."
 camera at screenshake_transform,reset_shader
 pause 0.0
 show shion_v002 smile at inactive
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Eeeeeh?! You should've told me that during the stay! I would have tried solving the riddle!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "*giggle*. Well, I've solved it before, though."
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's an easy thing to say. Was there really gold...?"
 show nao_v002 fuan at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Of course! ...Although, I had no interest in it, so I left it to the Ushiromiya family.'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Come on, Nao-chan. Let's open up the present!"
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'What if it contains a solid gold figurine?'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Even 1 gram of gold is a few thousand yen. If it was 100 grams of gold, that'd be quite the pretty penny."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "But, I don't think that Beatrice would give us gold for no reason."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide fade onlayer curtain
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's very light, so it's probably not gold... It's almost as if it was empty."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "Anyways, let's open it..."
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 show white_cover onlayer curtain as fade with Dissolve(1.0)
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Wh-... What?! ...What is this?!'
 stop sound
 show expression 'images/bg/AdvBg_2101.png' as bg
 play music "<loop 0>audio/bgm/BGM_EVENT_TOP_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v013 fuan at mei_right
 show shion_v011 fuan at mei_left
 with Dissolve(0.5)
 show shion_v011 fuan at inactive
 show mion_v013 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Wow, that sure was some lightning...! That was amazing for such a sunny day...'
 camera at screenshake_transform,reset_shader
 pause 0.0
 show mion_v013 fuan at inactive
 show shion_v011 odoroki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "S-Sis?! Wh-what's that outfit...?!"
 hide shion_v011
 hide mion_v013
 with Dissolve(0.2)
 show nao_v014 odoroki at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v014 odoroki at active
 show nao_v014 odoroki at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Y-You should talk, Shion-san. What was that? A magic trick? A quick change of clothes?'
 show nao_v014 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Nao-san also has a lovely outfit.'
 show nao_v014 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'That is... if I remember correctly, the Chiester Sisters Guard Corps.'
 show erika_v001 normal at inactive
 show nao_v014 odoroki_blush at active
 show nao_v014 odoroki_blush at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Wh-... wh-wh-what's with these clothes? Hey, wait, this skirt's way too short! I mean, you can see the whole front?!"
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 show shion_v011 fuan at mei_left
 show mion_v013 smile at mei_right
 with Dissolve(0.5)
 show mion_v013 smile at inactive
 show shion_v011 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Sis, these clothes of ours...'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show shion_v011 fuan at inactive
 show mion_v013 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'They\'re the costumes of the moon rabbits from\n"Mid-Autumn\'s Lament: The Heartbroken Rabbits Murder Caaseee"!!'
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show mion_v013 smile at inactive
 show shion_v011 smile at active
 show shion_v011 smile at jump_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Isn't this great?! Now Sis and I can do the moon rabbit dance together?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v013
 hide shion_v011
 hide fade onlayer curtain
 show nao_v014 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v014 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Mion-san and Shion-san seem to be having fun, but I don't understand what's going on!"
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Is this also a costume from Detective Wanyan?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Not at all. It's the uniform of the Chiester Sisters Guard Corps."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Among the maniacs of the Magical World, it's sold at an incredibly high price. In a way, a new one of those is priceless."
 hide erika_v001
 with Dissolve(0.2)
 show mion_v013 smile at mei_center
 with Dissolve(0.5)
 show mion_v013 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Well, there are industries where a used one is worth more than a new one you know~.'
 hide mion_v013
 with Dissolve(0.2)
 show nao_v014 sinken_blush at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v014 sinken_blush at active
 show nao_v014 sinken_blush at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I don't care what it's worth. I'm cold... {i}and{/i} I'm embarrassed!!"
 show nao_v014 sinken_blush at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Oh? The text on the message card from earlier has changed.'
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator "I wonder if you've been enjoying yourself?\nIt instantly changes your clothes when you open it, as it's a Clothes Change Pandora Box!"
 narrator "In fact, I thought I'd give the three of you the costumes you wanted the most while giving you all a glimpse at a fragment of yourself."
 narrator "For Mion and Shion, I had a clear image of what they wanted, but I couldn't figure anything out for Nao."
 show nao_v014 fuan at mei_center
 with Dissolve(0.5)
 show nao_v014 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...For clothing, my preferences change all the time. I don't usually have an image of one outfit I want the most."
 hide nao_v014
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator 'So, I thought about it.\nMion and Shion have the moon rabbit costumes from The Heartbroken Rabbits Murder Case, right?'
 narrator 'I thought that if you were a rabbit too, the three of you could be good friends!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show nao_v014 fuan_blush at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 fuan_blush at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I don't think soooooooo!!! Give it back! The front part of the skiiiirtt!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Front-open skirts are popular in the magic world for some reason.'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v011 smile at mei_left
 show mion_v013 smile at mei_right
 with Dissolve(0.5)
 show mion_v013 smile at inactive
 show shion_v011 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Wait, it's kind of like an Angel Mort outfit!"
 show shion_v011 smile at inactive
 show mion_v013 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Nao-chan, why won't you try out some part-time at Angel Mort in that outfit?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v013
 hide shion_v011
 hide fade onlayer curtain
 show nao_v014 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '{i}Hinamizawa--{/i}?!?! I re-fu-seeeeeee!!!'
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Wait, where are the clothes I was wearing just now?! Where are they?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Ah, there are more words on the message card. ...I do wonder what it says?'
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator 'P.S.'
 narrator "The clothes you were wearing will be delivered to your house tomorrow by Magic World Cleaning's express service, where they will be as good as new."
 narrator "The cleaning is on the house! No need to thank me.\nI'll see you soon! <See you again. Have a nice day!>"
 show nao_v014 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v014 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'What do you mean?! Am I supposed to dress like this until we get home?!'
 hide nao_v014
 with Dissolve(0.2)
 show mion_v013 smile at mei_right
 show shion_v011 smile at mei_left
 with Dissolve(0.5)
 show shion_v011 smile at inactive
 show mion_v013 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "This ol' man has cosplay outfits if you want to change~."
 show mion_v013 smile at inactive
 show shion_v011 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But Sis? Aren't these outfits a bit revealing for walking in public?"
 hide mion_v013
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show shion_v011 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Why don't you wear that bloody one from the murder scene reenactment?"
 show erika_v001 normal at inactive
 show shion_v011 fuan_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But I think it'd be hard to avoid getting questioned if we did that..."
 hide erika_v001
 show mion_v013 smile at mei_right
 with Dissolve(0.5)
 show shion_v011 fuan_close at inactive
 show mion_v013 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Well, I think that if I stopped a taxi while wearing a wedding dress and crying, I might get a bit of a discount♪'
 hide shion_v011
 hide mion_v013
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'You two are tireless. *giggle*.'
 show nao_v014 sinken_blush at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v014 sinken_blush at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "This... shameplay! I've never heard of something like this!! How could you taint me!?"
 show erika_v001 normal at inactive
 show nao_v014 sinken_blush at active
 show nao_v014 sinken_blush at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Going home dressed like this is worse than the club's cosplay punishment games!!"
 show nao_v014 sinken_blush at inactive
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '*giggle*giggle*giggle*. <May I help you?>'
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 show nao_v014 sinken at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show nao_v014 sinken at active
 show nao_v014 sinken at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '<Yes!! I need>, ummm.... <Skirt no front!!>'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v014 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Give me back the front part of this skirt! At least let me cover the abdomen area!!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.4
 pause 0.5
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "What's with this outfit!! It's tasteless!! It's pervy! It's the worstttttttt!!!"
 show black_cover onlayer curtain as fade with Dissolve(3.0)
 pause 1.5
 call chapter_end
 
 $ persistent.umi1_done = True
 return