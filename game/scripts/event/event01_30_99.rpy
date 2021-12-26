label event01_30_99:
 show black_background onlayer black
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop sound
 scene #000
 show expression 'images/bg/AdvBg_2320.png' as bg
 with Dissolve(2.0)
 pause 1.0
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao '...........................'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 sinken at mei_right
 show shion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show shion_v002 odoroki at jump_transform,active
 show mion_v002 sinken at inactive
 shion "What's wrong? ...Wha?!?! S-sis...!!"
 show mion_v002 futeki at active
 show shion_v002 odoroki at inactive
 mion "...They've... done it..."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator 'The story goes back to when I first found the magic circle on my bed sheet.'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'W-... what is this...'
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 narrator "Mion-san and Shion-san's beds had... nothing on top of them, but my bed alone was k i l l e d..."
 narrator 'The blanket was torn off disastrously... almost like the sheets were skin hanging off of it... and dyed with fresh blood.'
 narrator "No. It's not just dyed red. This is... something drawn on with a blood-like substance..."
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'A.........  magic circle.........'
 play music 'audio/bgm/BGM_EVENT_TOP_COLLAB2.ogg'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'I was enraptured by that horrible magic circle. That was when the Sonozakis spoke.'
 narrator "Wha?!? S-sis...!! ...They've... done it..."
 narrator "The following is an exchange that only the Sonozaki sisters can hear. I was so terrified that I couldn't even hear it."
 show mion_v002 futeki at mei_right
 show shion_v002 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show shion_v002 sinken at active
 show mion_v002 futeki at inactive
 shion "...That's... Bright-sama's magic circle?!?!"
 show mion_v002 futeki at active
 show shion_v002 sinken at inactive
 mion "They... They're not half bad... This is a magnificent reproduction..."
 show shion_v002 sinken at active
 show mion_v002 futeki at inactive
 shion 'Sis... did you notice...?'
 show mion_v002 sinken at jump_transform,active
 show shion_v002 sinken at inactive
 mion 'Of course... The way that the pillows and blankets are messed up... it perfectly recreates the scene from the movie!'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator "For a long time, I was confused as to why Shannon-san wasn't bothered by the magic circle."
 narrator 'But... Mion-san instantly understood. She knew that Shannon was also a deeply engrossed fan of Detective Wanyan.'
 narrator 'Mion remembered the question Erika had asked Shannon after she returned from fixing the lock on the window upstairs.'
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 camera at sepia_shader
 pause 0.0
 show expression 'images/bg/AdvBg_2331.png' as bg
 show shannon_v001 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(1.0)
 show erika_v001 normal at active
 show shannon_v001 smile at inactive
 erika 'Excellent work, Shannon-san. Has a robber broken into the window or anything?'
 show shannon_v001 smile_close at active
 show erika_v001 normal at inactive
 shannon 'No. Please be at ease.'
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Mion thought that felt out of place.'
 narrator "It sounded like a sarcastic remark from Erika-san... but if it was meant to be that way, she's saying that to the wrong person."
 narrator 'Why did she ask if something happened in the room?'
 narrator 'Mion-san instantly understood. Erika-san knew that Shannon-san was a Wanyanner.'
 narrator 'I heard about it myself after dinner that night when she confessed to me that she was a Wanyanner.'
 narrator 'So, I wanted to confirm with her that it was indeed the magic circle from the film.'
 show black_cover as fade with Dissolve(1.0)
 camera at reset_shader
 pause 0.0
 scene black_cover
 narrator 'Now, Shannon-san had originally not planned to go to the room upstairs.'
 narrator 'She only had to upstairs because I suddenly mentioned the lock on the window.'
 narrator "So, at that point, I'm sure Erika-san was panicking internally."
 narrator "That's because it was {i}me{/i} who was supposed to be the first to discover the magic circle prank and be surprised."
 narrator 'And at the same time, it would have been a fun joke to share with her fellow Wanyanners, Mion-san and Shion-san.'
 narrator 'However, since Shannon-san is also a hardcore Wanyanner, she immediately understood the meaning of the magic circle, so she just smiled and ignored it.'
 narrator 'This fact was confirmed by Erika-san when she asked Shannon-san after coming down the stairs.'
 narrator 'Mion-san understood it instantly.\nBoth why Shannon-san could ignore it and that the culprit was Erika were answers that could be derived in seconds.'
 narrator 'In other words, the moment the magic circle was discovered, the Sonozaki sisters knew everything, from the meaning of the magic circle, to the culprit being Erika-san.'
 narrator 'While I was cowering in fear at the magic circle... the Wanyan adoring Sonozaki sisters must have been laughing at me with disgusting smiles.'
 stop sound
 scene black_cover
 play music 'audio/bgm/BGM_BATTLE1_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator "...And... from here on it's a world beyond my understanding.\nIt's said that monsters are drawn to each other, but who would've thought that'd turn out to be true..."
 narrator 'Mion-san and Shion-san instantly got a grasp on the situation.\nWhat could Erika, who had drawn this perfect recreation of the circle from the movie, possibly want?'
 narrator 'A compliment? Or a shocked scream? ...Yes, it was an {i}audience{/i}.'
 narrator "That's right. In that moment, across the wall in Erika-san's room... one more Wanyanner was listening intently, letting out a disgusting laugh."
 camera at screenshake_transform,reset_shader
 pause 0.0
 narrator 'Erika-san... who wanted to hear the admiration of her magic circle by comrades, was listening... with a cup pressed against the wall... she was listening the whole time!!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at active
 erika "...*giggle*... What do you think? Isn't my magic circle a masterpiece...?\nIsn't it a perfect recreation of Bright-sama's magic circle...?"
 show erika_v001 smile at active
 erika "Now, do allow me to hear your praise, Mion-san, Shion-san!!\nI've already satisfied myself with the screams of Nao-san, who refuses to watch Detective Wanyan."
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 fuan at active
 erika 'Nwext, I want to hear your cries of admirationnNNIHIHIHI!!!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator "Erika strains her ears more and more. She wants to know Mion-san and Shion-san's reactions, so she focuses all of her attention into her hearing...!!"
 play audio 'audio/sfx/SE_5046_scratch.wav'
 narrator '...Ssskk......'
 narrator 'It was a small, strange sound.\nA quiet sound, but... as if it was pressed right up next to ear.'
 narrator "...No way. ......No, it can't be..."
 narrator "A bead of cold sweat appeared on Erika's face.\n...As it slowly ran down Erika's forehead... her expression... was colored with... an eerie joy."
 camera at screenshake_transform,reset_shader
 pause 0.0
 narrator 'Th-these people...... really......!?!'
 narrator "That's right. Erika-san, with the cup pressed against the wall, listens to the voice in the next room over, and hears through the wall..."
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 narrator "Two sets of creepy laughs, just like Erika's."
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 show erika_v001 futeki at active
 erika 'Ha...... haha............ nnn.'
 hide erika_v001
 with Dissolve(0.2)
 narrator "Those two... {i}they're listening to me{/i}!!!"
 narrator "I've drawn a perfect magic circle, and am now listening through the wall for voices of admiration... but they're listening to me!!!"
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 narrator 'On either side of the wall separating the two rooms... was one giant slug and two giant slugs... listening to each other through the wall with cups.'
 camera at screenshake_transform,reset_shader
 pause 0.0
 narrator '<G-Good>, <Gooderrrrrr>... <Goodeeeeeeeesssssstttt!!!>'
 narrator 'The next day, as if to say "Now it\'s your turn", Erika-san purposely forgot to lock the door.'
 narrator 'Even though they knew it was a trap, the Sonozaki sisters decided to take advantage of this... so Shion-san returned to the guesthouse under the guise of retrieving some luggage.'
 narrator "And then, she went into Erika-san's room to set up the prank with the magic circle."
 narrator 'Furthermore, the sheet with the magic circle was prepared in advance. ...The Sonozaki sisters worked all night on it after I had gone to sleep with the sleeping pills!'
 narrator 'Then, Shion-san falls for the trap with the fluorescent paint on the doorknob.'
 narrator 'Shion-san exercised a certain amount of caution, but as expected, she was unaware of the substance Erika had prepared herself.'
 narrator "So, there should certainly have been fluorescent paint on Shion's hands. So Erika-san should have checkmated her!"
 narrator "But... the Sonozaki sisters were not so naive after all.\nThat's right. After we returned, the two fought and ran into the shower together."
 narrator 'I was just smiling at how close the two were, fighting over who would go first in the shower.'
 narrator '...But the two of them, were doing this deliberately.'
 narrator "They switched at that time. When they heard Erika-san's scream and ran out of the shower, they had switched places."
 narrator "The two of them didn't underestimate Erika-san... They had suspected something had been attached to them that they couldn't percieve! "
 narrator 'The purpose of the shower was to wash that away, and more importantly, switch the sisters.'
 narrator 'But, Erika-san is crazy enough to call herself a great detective.'
 narrator 'When nothing came up after shining on Shion-san\'s hand with the black light, and she started crying out, "That\'s impossible!"... it wasn\'t frenzied scream of despair, but rather, of great delight.'
 narrator 'Erika-san says... Knox\'s 10th: "it is forbidden to disguise yourself as another person without any clues."'
 narrator 'However, Erika-san had met the sisters, introduced herself, and knew that they were identical twins.'
 narrator '"Identical twin sisters", Erika-san had said herself on the boat to Rokkenjima.'
 narrator "Therefore, EFFECTIVE.\nA disguise that does not violate Knox's 10th. No, a swap...!"
 narrator "At that moment, Erika-san could have immediately illuminated Mion's hand with her black light."
 narrator "If she did that, I would've seen Mion's hands illuminated with fluorescent paint."
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
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 play music 'audio/bgm/BGM_GACHA_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_2271.png' as bg
 with Dissolve(1.0)
 pause 1.0
 call wipeout_routine
 stop sound
 scene #000
 show expression 'images/bg/AdvBg_2221.png' as bg
 call wipein_routine
 pause 1.0
 call wipeout_routine
 stop sound
 scene #000
 show expression 'images/bg/AdvBg_2251.png' as bg
 call wipein_routine
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 jessica "Of course! Feel free to come over and play again!! Next time, we'll pull an all-nighter having a board game showdown! Right?"
 hide jessica_v001
 with Dissolve(0.2)
 Character('Krauss Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'The servants say that they have learned a great deal from your stay. You have our thanks.'
 Character('Natsuhi Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Thank you for completing the questionnaire as well. We will read it carefully and make good use of it in the future.'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "I've put my all into it! Please definitely read it to the end!"
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "We'll take responsibility for it! Because we're the consultants for the new resort on Rokkenjima!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator 'When it was time to leave, even the Ushiromiya family members came to see us off.'
 narrator "If I come here again... I'd like to take it easier. Otherwise... I might as well try cosplay... I think... maybe."
 show erika_v001 normal at mei_right
 show kanon_v001 normal_close at mei_left
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 show erika_v001 normal at inactive
 kanon 'Shannon would like to express her apologies for not being able to see you off.'
 show erika_v001 normal at active
 show kanon_v001 normal_close at inactive
 erika "Today's her day off. It can't be helped. Do give her my regards, for we are comrades under the giant slug!"
 show kanon_v001 normal at active
 show erika_v001 normal at inactive
 kanon '...Um, of course. ...As always, there are two truths.'
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 smile at active
 show kanon_v001 normal at inactive
 erika 'As always, there are two truths! Do you read it too?'
 hide erika_v001
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show jessica_v001 fuan_blush at mei_right
 with Dissolve(0.5)
 show jessica_v001 fuan_blush at active
 show nao_v002 smile at inactive
 jessica 'I... uh, might also like to do a cosplay photoshoot next time.'
 show jessica_v001 smile_blush at jump_transform,active
 show nao_v002 smile at inactive
 jessica "You know, when that time comes, why don't we do it together, Nao-chan? I'm sure it won't be as embarrassing if we go together."
 show nao_v002 smile at active
 show jessica_v001 smile_blush at inactive
 nao "*giggle*... That's right... let's make our cosplay debut together."
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'Among the people who see us off, the witch is mixed in with the crowd.\nOf course, no one can see her though.'
 show nao_v002 smile at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice 'It was a pleasure to spend my birthday with you, Nao.'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao "Thank you. But, I'd like to ask something... how old exactly are you?"
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice '*cackle*cackle*! I have forgotten over the course of a thousand years!'
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice "You are always welcome to come play again. Next time, I'll show you the golden rose garden of the Golden Land!"
 show nao_v002 smile at active
 show beatrice_v001 futeki at inactive
 nao "I'll bring a game console too. I'll show you just how good I am."
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 smile at inactive
 dlanor 'I pray for your good FORTUNE. Wishing you the BEST.'
 show nao_v002 smile at active
 show dlanor_v001 normal at inactive
 nao 'Thank you. I would have liked to spend more time speaking with you. See you again.'
 hide dlanor_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika "Since I'm a detective, whereever an incident might occur, you'll find me. So, I don't think I will ever see you again."
 show nao_v002 smile at active
 show erika_v001 normal at inactive
 nao "That's okay. There's the Detective Wanyan collab cafe. I'll probably be there, so we'll see each other again then."
 show erika_v001 smile at active
 show nao_v002 smile at inactive
 erika ".........*giggle*giggle*. <Good> When you do, let's talk about our favorite characters to the fullest. "
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Come visit us in Hinamizawa some time, Erika-san! We definitely won't let you get bored!"
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'I want to see you face off with Kei-chan. The Magician of Words vs The Great Detective. I wonder who will win?'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Oh? A Magician of Words? A magician, just like the alias of that culprit in The Kaneda Case Files! Wonderful!'
 show erika_v001 futeki at active
 erika 'Whenever anyone has a case, I, Erika Furudo, shall promise to come to your aid!'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'Alternatively, we can go to Angel Mort and have a long casual talk over all-you-can-eat dessert.☆'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "I'd love to invite someone fun and tough like you to the Hinamizawa Branch School."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "Definitely. ...Erika's energy and reasoning skills are like a combination of Mion-san and Rena-chan."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at active
 erika 'One day, absolutely.'
 show erika_v001 normal at active
 erika '*giggle*...Just with the presence of a few friends that are reluctant to depart, this level of farewell is possible for Erika Furudo. What do you think, everyone?'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 futeki at mei_center
 with Dissolve(0.5)
 show nao_v002 futeki at active
 nao '<Good!>'
 show white_cover as fade with Dissolve(2.5)
 window hide None
 hide nao_v002
 with Dissolve(0.2)
 pause 3.0
 play sound ['audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav'] fadeout 1.0
 stop sound
 scene white_cover
 play music 'audio/bgm/BGM_HOME_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_2101.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show erika_v001 normal at inactive
 nao "...What's with the letter that Erika received?"
 show erika_v001 normal_close at active
 show nao_v002 smile at inactive
 erika "Don't worry. I am only a messenger. I have merely been entrusted with this message to give to my master."
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika "It seems that Beatrice has written a lot about me. I look forward to seeing what's inside."
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '...Speaking of which... Beatrice said she had a present for me too...'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 show mion_v002 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show mion_v002 odoroki at active
 show shion_v002 fuan at inactive
 mion 'Ehh? What?! Did you get a present on Rokkenjima?!'
 show shion_v002 fuan at active
 show mion_v002 odoroki at inactive
 shion "That's nice. We didn't get anything at all."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "Actually, I think the witch's present for Nao was intended for all three of you."
 show erika_v001 normal at active
 erika "Why don't you have a look in your luggage?"
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'After she says that, I take a look through my luggage.\nSitting inside, was a small present box that I had never seen before.'
 narrator "There's a message card attached... As I thought, it's from Beatrice."
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator '"In honor of your visit to Rokkenjima. -From The Golden Witch"'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "I-It's that portrait! Could it be the 20 billion yen's worth of gold bars?"
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "There's something like an inscription in front of the portrait. They say it's a riddle, and solving it leads to the location of the gold bars."
 camera at screenshake_transform,reset_shader
 pause 0.0
 show mion_v002 odoroki at active
 show shion_v002 smile at inactive
 mion "Eeeeeh!? You should've told me that during the stay! I would have tried solving the riddle!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika "*giggle*. Well, I've solved it before, though."
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao "That's an easy thing to say. Was there really gold...?"
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'Of course! ...Although, I had no interest in it, so I left it to the Ushiromiya family.'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Come on, Nao-chan. Let's open up the present!"
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'What if it contains a solid gold figurine?'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "Even 1 gram of gold is a few thousand yen. If it was 100 grams of gold that'd be quite the pretty penny."
 show erika_v001 normal at active
 erika "But, I don't think that Beatrice would give us gold for no reason."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao "It's very light, so it's probably not gold... It's almost as if it was empty."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator "Anyways, let's open it..."
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 show white_cover as fade with Dissolve(1.0)
 erika 'Wh... What?! ...What is this?!'
 stop sound
 scene white_cover
 play music 'audio/bgm/BGM_EVENT_TOP_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_2101.png' as bg
 with Dissolve(1.0)
 show shion_v011 fuan at mei_left
 show mion_v013 fuan at mei_right
 with Dissolve(0.5)
 show mion_v013 fuan at active
 show shion_v011 fuan at inactive
 mion 'Wow, that sure was some lightning...! That was amazing for such a sunny day...'
 camera at screenshake_transform,reset_shader
 pause 0.0
 show shion_v011 odoroki at active
 show mion_v013 fuan at inactive
 shion "S-Sis?! Wh-what's that outfit...?!"
 hide shion_v011
 hide mion_v013
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v014 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v014 odoroki at jump_transform,active
 show erika_v001 normal at inactive
 nao 'Y-you should talk, Shion-san. What was that? A magic trick? A quick change of clothes?'
 show erika_v001 normal at active
 show nao_v014 odoroki at inactive
 erika '...Nao-san also has a lovely outfit.'
 show erika_v001 normal at active
 show nao_v014 odoroki at inactive
 erika 'That is... if I remember correctly, the Chiester Sisters Guard Corps.'
 show nao_v014 odoroki_blush at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao "Wh... wh-wh-what's with these clothes? Hey, wait, the skirt's too short! I mean, you can see the whole front?!"
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 show mion_v013 smile at mei_right
 show shion_v011 fuan at mei_left
 with Dissolve(0.5)
 show shion_v011 fuan at active
 show mion_v013 smile at inactive
 shion 'Sis, these clothes of ours...'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show mion_v013 smile at active
 show shion_v011 fuan at inactive
 mion "It's the costumes of the moon rabbits from Mid-Autumn's Lament: The Heartbroken Rabbits Murder Caasseee!!"
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show shion_v011 smile at jump_transform,active
 show mion_v013 smile at inactive
 shion "Isn't this great! Me and my sister, we can do the moon rabbit dance together!!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide mion_v013
 hide shion_v011
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v014 sinken at active
 nao "Mion-san and Shion-san seem to be having fun, but I don't understand what's going on!"
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 fuan at active
 nao 'Is this also a costume from Detective Wanyan?!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "Not at all. It's the uniform of the Chiester Sisters Guard Corps."
 show erika_v001 normal at active
 erika "Among the maniacs of the Magical World, it's sold at an incredibly high price. In a way, a new one of those is priceless."
 hide erika_v001
 with Dissolve(0.2)
 show mion_v013 smile at mei_center
 with Dissolve(0.5)
 show mion_v013 smile at active
 mion 'Well, there are industries where a used one is worth more than a new one you know~.'
 hide mion_v013
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v014 sinken_blush at mei_left
 with Dissolve(0.5)
 show nao_v014 sinken_blush at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao "I don't care what it's worth. I'm cold, {i}and{/i} I'm embarassed!!"
 show erika_v001 normal at active
 show nao_v014 sinken_blush at inactive
 erika 'Oh? The text on the message card from earlier has changed.'
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator "I wonder if you've been enjoying yourself?\nIt instantly changes your clothes when you open it, as it's a Clothes Change Pandora Box!"
 narrator "The truth is, I thought I'd give the three of you the costumes you wanted the most while giving you all a glimpse at a fragment of yourselves."
 narrator "For Mion and Shion, I had a clear image of what they wanted, but I couldn't figure anything out for Nao."
 show nao_v014 fuan at mei_center
 with Dissolve(0.5)
 show nao_v014 fuan at active
 nao "...For clothing, my needs change from time to time. I don't usually have an image of one outfit I want the most."
 hide nao_v014
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator 'So, I thought about it.\nMion and Shion have the moon rabbit costumes from The Heartbroken Rabbits Murder Case, right?'
 narrator 'So, I thought that if you were a rabbit too, the three of you could be good friends!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 fuan_blush at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 fuan_blush at active
 nao "I don't think soooooooo!!! Give it back! The front part of the skiiiirtt!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika '...Front-open skirts are popular in the magic world for some reason.'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v013 smile at mei_right
 show shion_v011 smile at mei_left
 with Dissolve(0.5)
 show shion_v011 smile at active
 show mion_v013 smile at inactive
 shion "Wait, these are a bit like Angel Mort's outfits!"
 show mion_v013 smile at active
 show shion_v011 smile at inactive
 mion "Nao-chan, why won't you try out some part-time at Angel Mort in that outfit?!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide mion_v013
 hide shion_v011
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 sinken at active
 nao 'Hinamizawa--!! I re-fu-seeeeeee!!!'
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 sinken at active
 nao 'Wait, where are the clothes I was wearing just now?! Where are they?!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Ah, there are more words on the message card... I do wonder what it says? ...Hm?'
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator 'P.S.'
 narrator "The clothes you were wearing will be delivered to your house tomorrow, by Magic World Cleaning's express service, where they will be as good as new."
 narrator "The cleaning is on the house! No need to thank me.\nI'll see you soon! <See you again. Have a nice day!>"
 show nao_v014 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v014 odoroki at active
 nao 'What do you mean?! Am I supposed to dress like this until we get home?!'
 hide nao_v014
 with Dissolve(0.2)
 show shion_v011 smile at mei_left
 show mion_v013 smile at mei_right
 with Dissolve(0.5)
 show mion_v013 smile at active
 show shion_v011 smile at inactive
 mion "This ol' man has cosplay outfits if you want to change~."
 show shion_v011 fuan at active
 show mion_v013 smile at inactive
 shion "But Sis? Aren't these outfits a bit revealing for walking in public?"
 hide mion_v013
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v011 fuan at inactive
 erika "Why don't you wear that bloody one from the murder scene reenactment?"
 show shion_v011 fuan_close at active
 show erika_v001 normal at inactive
 shion "But, I think it'd be hard to avoid getting questioned if we did that..."
 hide erika_v001
 show mion_v013 smile at mei_right
 with Dissolve(0.5)
 show mion_v013 smile at active
 show shion_v011 fuan_close at inactive
 mion 'Well, I think that if I stopped a taxi while wearing a wedding dress and crying, I might get a bit of a discount♪'
 hide shion_v011
 hide mion_v013
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'You two are tireless. *giggle*'
 show nao_v014 sinken_blush at mei_left
 with Dissolve(0.5)
 show nao_v014 sinken_blush at active
 show erika_v001 normal at inactive
 nao "This shameplay! I've never heard of something like this!! How could you taint me like this!?"
 show nao_v014 sinken_blush at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao "Going home dressed like this is worse than the club's cosplay punishment games!!"
 show erika_v001 futeki at active
 show nao_v014 sinken_blush at inactive
 erika '*giggle*giggle*giggle*. <May I help you?>'
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 show nao_v014 sinken at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show nao_v014 sinken at jump_transform,active
 nao '<Yes!! I need>, ummm.... <Skirt no front!!>'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v014 sinken at active
 nao 'Give me back the front part of this skirt! At least let me cover the abdomen area!!'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.4
 pause 0.5
 camera at screenshake_transform,reset_shader
 pause 0.0
 show nao_v014 sinken at active
 nao "What's with this outfit!! It's tasteless!! It's pervy! It's the worstttttttt!!!"
 show black_cover as fade with Dissolve(3.0)
 pause 1.5
 return