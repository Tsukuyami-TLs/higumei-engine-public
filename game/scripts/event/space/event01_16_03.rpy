label event01_16_03:
 show black_background onlayer black
 $ event_store.current_event='space'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_16_03'
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
 show expression 'images/bg/AdvBg_162.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator '...When we arrived at the foot of the stone steps leading up to the Furude Shrine, the sun was already starting to set, and the area around us was becoming dyed with a warm shade of vermillion.'
 play audio 'audio/sfx/SE_530_walk_one.wav'
 show mion_v002 smile at mei_center
 show mion_v002 smile at walk_transform:
  yanchor 1.0
  linear 0.6666666666666666 pos (1440,1200)
 with Dissolve(0.5)
 pause 0.16666666666666663
 show mion_v002 smile:
  yanchor 1.0
  pos (1440,1200)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Woah, this place looks just like how it was before too, huh?\nEveryone, you all still behind me?'
 play audio 'audio/sfx/SE_530_walk_one.wav'
 show kazuho_v002 smile at mei_outerleft
 show kazuho_v002 smile at walk_transform:
  yanchor 1.0
  linear 0.6666666666666666 pos (480,1200)
 with Dissolve(0.5)
 pause 0.16666666666666663
 show kazuho_v002 smile:
  yanchor 1.0
  pos (480,1200)
 show mion_v002 smile at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Y-Yeah...!'
 hide mion_v002
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'I nod back with as much spirit as I could muster to Mion-san, who turned back to us with a bright expression.'
 narrator 'And so we followed behind as she quickly ran up the stairs...'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_512.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'We walked under the incredibly familiar torii gate and stepped out onto the grounds, where the main shrine could be seen.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1102.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Wow, they surprisingly made the shrine look like the original.\nThis level of attention to detail is a huge technological feat, isn't it?"
 show miyuki_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show miyuki_v002 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Nah, I actually think it's pretty bad taste. It's like they focused on the wrong details or something."
 show miyuki_v002 fuan_close at inactive
 show shion_v002 smile_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '*giggle*... for sure.\nThey have a hard time reading the room just like Sis does, huh?'
 hide miyuki_v002
 show mion_v002 sinken at mei_left
 with Dissolve(0.5)
 show shion_v002 smile_close at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Alright, alright, Shion. I'm not gonna let you take advantage of the situation to badmouth me. Seriously..."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator 'While conversing like this, we passed the front of the main shrine and through the gravel patch, continuing towards the grassy area spread out around the back of the grounds.'
 narrator 'And shortly thereafter, we finally arrived at the lookout, where we could see all of Hinamizawa.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_172.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 show satoko_v002 smile at mei_center
 show satoko_v002 smile at walk_transform:
  yanchor 1.0
  linear 0.6666666666666666 pos (1440,1200)
 with Dissolve(0.5)
 pause 0.16666666666666663
 show satoko_v002 smile:
  yanchor 1.0
  pos (1440,1200)
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Uwaa...! Looking down on Hinamizawa's scenery from up here really feels nice, doesn't it...?"
 show rena_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Ahahaha, you're right. The refreshing evening breeze, the good weather... these really are ideal conditions for stargazing~, hauu♪"
 hide satoko_v002
 show shion_v002 smile_close at mei_right
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show shion_v002 smile_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yeah... a thousand years did go by, but I wouldn't complain if we could see a meteor shower just like we did back then."
 hide rena_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile_close at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Agreed. Even if we didn't get to see one, I feel that the ability to in and of itself would be charming and intriguing."
 hide shion_v002
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, yeah, definitely. ...By the way, I heard that the North Star changes every few thousand years or so, so I wonder if it's different now?"
 hide nao_v002
 show mion_v002 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Well, who knows. I don't know that much about constellations. ...Hup."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide miyuki_v002
 hide mion_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_142.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 narrator 'As she says that, Mion-san puts the knapsack-like bag she got from K-1 down on the ground. Then she takes its contents and lays them out on the ground.'
 narrator 'There were weapons like knives, which we were told to use "for self-defense just in case". Besides that...'
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Woah, they gave us fake candies?\nAnd they got a variety of flavors from sweet to salty, huh~?'
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "*giggle*giggle*... those people of the future do make super clever recreations for us, don't they? When they mentioned food, I thought it'd be something like space food."
 hide mion_v002
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Hey, they even got cup ramen. ...Wait a minute, there's no hot water? No way I'm I supposed to eat it like this, right?"
 hide shion_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's okay, we have candy too.\nYou like cup ramen, don't you?"
 show nao_v002 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "I mean... I don't dislike it. But... jeez, those guys really aren't thoughtful..."
 hide miyuki_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator 'With that sentiment, Miyuki-chan groans and complains as she breaks open the cup ramen and sticks it in her mouth, starting to bite and gnaw at it.'
 narrator '...To tell the truth, we all felt hungry, so we all picked up something we liked and started eating it.'
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hauu~...I wonder why candy tastes so good when I'm hungry~♪"
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'But... is it really okay to be eating this? We got the bag from those two, so I get a strange feeling that this stuff is suspicious...'
 hide rena_v002
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Well, we don't gotta be so on guard about it.\nYou can't fight on an empty stomach now, can you?"
 show mion_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I certainly can't argue with that, Mion-san.\nWe're like a koi on a cutting board in that case; it's in for a penny, in for a pound~."
 hide mion_v002
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau~, Nao-chan, let's split the candy in two and eat aaaaaall sorts of flavors♪"
 hide satoko_v002
 show nao_v002 smile_blush at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show nao_v002 smile_blush at active
 show nao_v002 smile_blush at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Yeah, Rena-chan, let's do it!"
 hide rena_v002
 hide nao_v002
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'I breathe a sigh of relief and grin at the sight of seeing everyone brightly mingling and stuffing their cheeks with candy.'
 narrator 'This "World" that K-1 and Lady Meep created may be temporary... or rather, "a fake".'
 narrator "But... the people I love so much are all there in front of me, and they're all enjoying this moment as much as they can..."
 narrator 'Their strength and kindness were undoubtedly real.\nFrom the bottom of my heart, I could feel that this alone was true, and that it was okay to feel that it was too...'
 show kazuho_v002 smile_close at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(We're leaving this place tomorrow...\nI have no idea if I can continue to have fun with everyone like this if we do go to another planet... but...)"
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "Right now, I'm going to cherish this time spent with everyone, and it will be something I'll never, ever want to forget."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_172.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'While I was ruminating on that, I casually turned towards the far-off sky, which was reddening in the distance.'
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_402_higurashi1.wav'
 narrator '...And out of nowhere, I could hear the cries of the higurashi.'
 narrator 'I feel like I heard someone say that the moment when sunset and night merge to create twilight is called {b}Omagatoki{/b}, the "Time of Great Calamity".'
 narrator '...I laughed bitterly at my backwards thought of something so ominous―...'
 narrator 'It was then that it happened.'
 show black_cover as bg
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...*cackle*, *cackle*cackle*.\nKuheheheheheh, kekekekeke...!!'
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahahahahaha...\nAAAAHHAHAHAHAHAHAHA!!'
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...ah-...?!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_142.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'I heard strange, eerie laughter mixed in with unintelligible sounds, so I turn my head... and while remaining in that position, I gasp and grow stiff.'
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wha-...ah-...aaah...?!'
 play music "<loop 5.836>audio/bgm/BGM_EVENT5.ogg"
 camera at screenshake_transform
 pause 0.0
 show kazuho_v002 odoroki at inactive
 show kazuho_v002 odoroki at chara_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ahahahahahahaha...\nAHAHAHAHAHAHAHAHA..!!'
 camera at screenshake_transform
 pause 0.0
 show kazuho_v002 odoroki at inactive
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*...!! Hehehehehe... HYAAGAGAGAGAGAGAGAAAHHH!!'
 camera at screenshake_transform
 pause 0.0
 show kazuho_v002 odoroki at inactive
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*... AAAAHAHAHAHAHAAAH...!!!'
 camera at screenshake_transform
 pause 0.0
 show kazuho_v002 odoroki at inactive
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Kehheheheheheheh, kkhehehehehhh...!!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_1400.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Everyone except me is breaking down laughing... all while showing expressions of madness.'
 narrator 'A chill runs up my spine and throughout my entire body.\nWhat on earth... was this...?!'
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Wh-...what's wrong, everyone? Why is... what's going on...?!"
 camera at screenshake_transform
 pause 0.0
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Kuhehehehehe... kekekekekekeke!!'
 camera at screenshake_transform
 pause 0.0
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ahahahahahahaha...\nAHHHAHAHAHAHAHAHA!!'
 narrator 'Mion-san and Miyuki-chan, Rena-san and Nao-chan, Satoko-chan and Shion-san...'
 narrator 'With both the candies and the weapons we were given in hand, they all begin to attack each other brutally.'
 stop sound
 show expression 'images/bg/AdvBg_1271.png' as bg
 narrator 'Sounds of blades being swung were followed by fresh blood spurting out as flesh was torn open. The sickening crunch of their bones breaking from their bodies taking dull strikes is...!'
 camera at screenshake_transform
 pause 0.0
 camera at reset_shader
 pause 0.0
 play audio 'audio/sfx/SE_105_hit_pierce.wav'
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'GUHEH...! HEE, HYAHAHAHAHA... UHFG!'
 camera at screenshake_transform,reset_shader
 pause 0.0
 play audio 'audio/sfx/SE_125_hit_slash2.wav'
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'GAHH... HA... GEHGHE, GEGEGEGEGEEHHHHHH!!'
 call wipeout_routine
 camera at reset_shader
 pause 0.0
 stop sound
 show expression 'images/bg/AdvBg_1270.png' as bg
 call wipein_routine
 narrator "I didn't think about protecting myself... all I did was watch as they tore each other apart right in front of me."
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...H-Hih... hiiiieeee..?!'
 narrator 'An all-too-terrible, unimaginable tragedy unfolds before my very eyes... and {i}plop{/i}, I fall back onto the ground right in that spot.'
 narrator "...I didn't think about running away. Not even being able to rush over to stop them, all I did was sit there and watch them break and destroy each other... is there really nothing I can-...?!"
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_142.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_022_WaveStart.wav'
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahahahahahaha, ahahahahahaha..!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '—*gasp*...?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Suddenly, Rena-san turns her head toward me as she straddles Nao-chan... her sharp glare makes me gasp as she was clearly fixating on an enemy.'
 narrator 'The grass behind the shrine was coated with a massive pool of blood darker than the red hues of the evening sun, and it was filling the air with a horrible stench...'
 narrator "Aside from Rena-san and I, everyone's tragic figures were laid there like a swamp of blood and flesh..."
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahahahahaha, AAAAHHAHAHAHAHAHAHAAAHH!!!'
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah-, aaaaaaahhhh...!'
 hide kazuho_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 narrator 'With her weapon dripping blood and her entire body stained bright red, Rena-san wears a crazed expression while creeping towards me slowly.'
 narrator "...Is the blood that's coating her knife... Nao-chan's?\nWhen that obscure thought arose in the back of my mind, my whole body shivered with fright."
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'S-...stop, Rena-san...!\nJust what is... why... is this happening?!'
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 show kazuho_v002 fuan at inactive
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahahahahahaha... AHAHAHAHAHAHAAAHH!!'
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-...anyways, calm down...!\nPlease, PLEASE...!'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'As if mocking my desperate attempts at persuasion... Rena-san raises her weapon high above her head.'
 play audio 'audio/sfx/SE_405_swing_high.wav'
 narrator 'Then as she swings downward in attempt to slice my head open—'
 stop music fadeout 0.5
 camera at screenshake_transform,reset_shader
 pause 0.0
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") '....GAAHH...?!'
 narrator 'I suddenly hear Rena-san groan or something... and her body remains frozen in that same position.'
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '....R-Re-...Rena...san...... ah-?'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Her eyes were open wide and crossed...\nJust as I thought that her face seemed contorted in surprise, she fell onto her back.'
 play audio 'audio/sfx/SE_218_down.wav'
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Rena-san...?\nWh-what is going-...?!'
 hide kazuho_v002
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 show rika_v012 smile at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep. We got here just in time.'
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Heheh... good work. If she died, then all of this would've been for nothing."
 hide rika_v012
 hide keiichi_v007
 with Dissolve(0.2)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Eh... y-you guys are...?!'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'From behind the fallen Rena-san appeared two people.'
 narrator 'It was those people of the future with the faces of my friends... K-1 and Lady Meep.'
 call chapter_end
 jump event01_16_04