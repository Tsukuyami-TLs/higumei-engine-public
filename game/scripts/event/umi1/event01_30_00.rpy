label event01_30_00:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_30_00'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 narrator 'I should have never come to this island.'
 play music "<loop 0>audio/bgm/BGM_QUEST7_COLLAB2.ogg"
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'N-... n-......'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Nooooooooooooooooo!!'
 stop sound
 show expression 'images/bg/AdvBg_1270.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_346_ls_blood.wav'
 narrator 'The poor victims... were on the bed covered in blood.'
 narrator "The girl's negligee probably used to be very lovely."
 narrator 'But... it had been relentlessly cut by a blade or something, and torn to shreds.'
 narrator 'The blood that must have poured out from that spot had dyed the negligee and the sheets to the point where I could no longer remember what color they were originally.'
 narrator 'The other one was in a gown. ...Of course, it was also stained with fresh, bright red blood.'
 narrator 'Just like the other one, it had been torn to shreds... and was clearly in a pitiful state.'
 narrator 'Out of three beds, two were covered in blood... But one bed was still as clean as it was last night. That was... my bed.'
 narrator "And I was the only one... who wasn't covered in a single drop of blood... while having slept soundly in the same room as them..."
 narrator '"A-Are you okay...?", was what I wanted to say, but the only thing that came out of my mouth was a faint, unsteady groan that was too weak to be called a scream.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 play audio 'audio/sfx/SE_527_door_close.wav'
 narrator 'I dashed out to the next room over, frantically knocking on the door while trying at the doorknob.'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Erika-san, Erika-san!! S-Something awful happened! H-H-Help...!!'
 play audio 'audio/sfx/SE_526_door_open.wav'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh...? It opened...?'
 narrator "Even if you turn a doorknob, there's no way it would open if the door was locked."
 narrator 'Rattling the doorknob like that was just my unconscious way of informing her of my confusion and the abnormality of the situation.'
 narrator "...That's why I didn't actually expect the door to open."
 narrator 'It was so unexpected... that it made my heart stop for a second... sharpening my senses like a knife.'
 narrator "Extreme fear can numb our emotions and sharpen our senses to the limit. But... it's a blade of ice in the end. ...No matter how sharp it is, it's fragile and easily shattered......"
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Erika...san...?'
 stop sound
 show expression 'images/bg/AdvBg_1270.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 narrator 'It was stained... Erika-san was also on the bed... red and bloody......'
 camera at screenshake_transform
 pause 0.0
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Noooooooooooooooooooooooooooooooo!!!!!!!!!!!'
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 pause 3.0
 show black_cover as bg
 narrator 'I should have never come to this island... \nThinking about it now, the invitation to Rokkenjima was very sudden.'
 window hide None
 stop sound
 show expression 'images/bg/AdvBg_541.png' as bg
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, yes, I heard about it from Rena-chan...'
 show nao_v002 normal at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That's good to hear! Wouldn't want these precious tickets to be wasted!"
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator 'The conversation came suddenly. Rena-chan asked me if I wanted to go on a short two night trip during the weekend.'
 narrator 'Originally, it was Rena-chan, Mion-san, and Shion-san who were supposed to go on this trip.'
 narrator "But at just the last minute, a relative had some errands, and Rena-chan wasn't able to participate anymore."
 show nao_v002 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Rokkenjima... It's a small, privately owned island, right?"
 show nao_v002 normal at inactive
 show mion_v002 smile at active
 show mion_v002 smile at nod_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yeah that's right! It's owned by the super rich Udaikan family!"
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_center
 with Dissolve(0.5)
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Sis, it's the {i}Ushiromiya{/i} family. "
 hide shion_v002
 with Dissolve(0.2)
 narrator 'Rokkenjima is a small island with a total circumference of about 10 km, located in the Izu Archipelago. The island is the private property of the wealthy Ushiromiya family, so normally travellers and such are not allowed to go there.'
 show mion_v002 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Or so it used to be! Looks like they're thinking about turning it into a resort in the future."
 show mion_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...So we were invited as reviewers?'
 hide mion_v002
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "All we have to do is to answer a simple questionnaire at the end. It's a two night trip with free meals, so it'll be great!"
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator 'They say the Ushiromiya family chef was good enough to have competed for the head chef position at a famous hotel, so his cooking is rumored to be excellent.'
 narrator 'Moreover, they have a well-kept rose garden and a perfectly picturesque beach with white sand.'
 narrator 'And of course, the Western-style buildings, which were built right after the war, are also said to be wonderfully elegant.'
 show shion_v002 fuan at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Still, the place isn't meant for tourists, though, so there aren't any stores or things to do."
 show shion_v002 fuan at inactive
 show nao_v002 smile at active
 show nao_v002 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I understand. After all, traveling isn't just about playing and shopping."
 hide shion_v002
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Japanese people just don't get what vacations are, y'know? It's not just about shopping or sightseeing on bus tours."
 show mion_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "We aren't going there to travel anyways; this is a vacation."
 show nao_v002 normal at inactive
 show mion_v002 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'In those wonderful Western-style houses, we can spend time resting our minds while watching the roses, not a soul there to bother us.'
 hide nao_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator '...Hearing her say that, I started to get in the mood to go a little more. Doing some embroidery as I watch the roses... my heart might finally know some peace... maybe.'
 narrator "The payments were all done ahead of time. Now we'll be able to relax ourselves in a wonderful Western-style house, and follow it up with even more wonderful meals. "
 narrator "We'll rest up for three days and two nights, then we'll return home Sunday night. The schedule is kind of tight, but the conditions will be well worth it."
 narrator 'That golden ticket was a special raffle prize at some shopping district, so for Mion-san to be the one to have pulled it was...'
 narrator 'At first, I thought I would be asked to help Rena-chan with her things.'
 narrator "But the Sonozaki sisters had no such intentions. The three were invited to go, but Rena-chan couldn't make it. And since having that leftover space would be wasteful, I was asked to go in her place."
 narrator 'I was also given the option to turn down the offer if it was a bother. In that case, the sisters told me they would just go on their own.'
 narrator "Rena-chan kindly gave her invitation up to me, so I won't let it go to waste. I'll make sure I have a blast, so I can bring back a bunch of stories of my time there."
 stop music fadeout 2.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 narrator 'So, just like that, I accepted the trip to Rokkenjima for three days and two nights. ...We were absolutely going to have lots of fun this time.'
 narrator 'But I might have... gotten jinxed at some point...'
 play audio 'audio/sfx/SE_5053_wind.wav'
 narrator 'It was probably because of {i}that{/i}. When we were heading to Niijima by ferry... the sky started looking weird.'
 narrator "It has to be that unpleasant woman's... Erika Furudo's fault."
 stop sound
 show expression 'images/bg/AdvBg_2111.png' as bg
 play sound ['audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav'] fadeout 1.0
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v002 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 $ event_store.current_progress = 1
 show nao_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Nao-chan! Are you watching "{note_green}Detective Wanyan{/note_green}"?!'
 $ event_store.current_progress = 2
 show mion_v002 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I\'m more of a "{note_green}Kaneda Case Files{/note_green}" person.'
 hide mion_v002
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That doesn't matter!! It's really good, okay?!"
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 show mion_v002 smile at jump_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If you don't want to watch the show or read the manga, I totally get it!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'But please! I thought you were just messing with this ol\' man, but the Detective Wanyan movie "Mid-Autumn\'s Lament: The Heartbroken Rabbits Murder Case" is something you absolutely must waaatch!!!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide mion_v002
 with Dissolve(0.2)
 narrator '"Detective Wanyan" is a very popular mystery anime.'
 narrator "The movie in particular is really high quality, so much that it's regarded as a masterpiece among their most recent works... or at least that's what Mion-san was stressing to me."
 show mion_v002 smile_close at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Western-style houses are really romantic! This ol’ man finally gets why Rika-chan has been yearning to go to St. Lucia so much.'
 show mion_v002 smile_close at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'In any case, our stay in question has a beautifully mysterious aura to it~!'
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show mion_v002 smile_close at inactive
 show shion_v002 smile_blush at active
 show shion_v002 smile_blush at jumping_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'If Satoshi-kun whispered, "I love you, so die for me.", to me in that house, I\'d just {i}have{/i} to hand my life over to him~! Unnnnfff~☆'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I see. So, now you're saying the Western-style house craze is coming between you two, huh?"
 hide nao_v002
 with Dissolve(0.2)
 narrator "The traditional Japanese architecture of the houses in Hinamizawa paired with its scenic land makes for a splendid living area, but I suppose that's the same reason we also have a taste for Western things. "
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I think the beauty of Hinamizawa is much more impressive, but...'
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I guess the grass is always greener on the other side.'
 hide nao_v002
 with Dissolve(0.2)
 narrator "I don't have a taste for Western-styled houses or big mansions, though. They look like it'd be difficult to get some peace and quiet without someone or something interfering."
 narrator 'The Sonozaki sisters were having a rousing discussion about Detective Wanyan.'
 narrator "If that's the case, then they can have their fun over there, and I'll have mine over here."
 narrator "Although you wouldn't call this a cruise, our view of the horizon from the ferry was quite nice."
 play audio 'audio/sfx/SE_611_ls_wind.wav'
 pause 0.5
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...The wind's pretty strong."
 stop music fadeout 2.0
 hide nao_v002
 with Dissolve(0.2)
 narrator "The deck didn't have too many people on it. At first, the atmosphere was bright and fun, but the winds got too chilling, so everyone went inside."
 narrator 'So, sadly, the little children, who would otherwise be bustling around in excitement, are now submerged in a reclusive and depressing atmosphere.  '
 play music "<loop 0>audio/bgm/BGM_QUEST3_COLLAB2.ogg"
 narrator 'Oh, look. Fitting with that thought, there was a melancholic looking girl hanging onto the railing, looking out into the horizon.'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '.....................'
 hide erika_v001
 with Dissolve(0.2)
 narrator 'The girl appeared sweet and cute. ...But that was only my first impression.'
 narrator "Once again, the frolicking voice of a child approaches. He's excited for some reason, running around the deck in bunches of laps. "
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Ah.'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'At that moment, I saw it clearly. As the child ran past, the girl stuck out her foot and tripped him.'
 play audio 'audio/sfx/SE_5013_down.wav'
 narrator "The child's momentum... made him fall face-first onto the deck with a bang."
 narrator 'Rather than from the pain, the surprise from the fall made him start bawling a bit after...'
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...A-Are you okay?! You aren't hurt, are you? Please calm down."
 hide nao_v002
 with Dissolve(0.2)
 narrator "Thankfully, he fell gracefully and gently. He wasn't hurt."
 play audio 'audio/sfx/SE_408_run.wav'
 narrator 'The child eventually ran off, still crying. The only ones left afterwards were... just the girl and I.'
 show nao_v002 sinken at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...You're awful, tripping someone on purpose like this."
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "On purpose? Please don't say such bad things about people."
 camera at screenshake_transform
 pause 0.0
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'How bold of you to do something so disgraceful! And right in front of me, too!'
 stop music fadeout 0.5
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Do you have conclusive evidence that I tripped someone on purpose?'
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB2.ogg"
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Conclusive... evidence??'
 show nao_v002 fuan at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'The fact that the child has fallen is not an issue as we have both witnessed this.'
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Similarly, me sticking out my leg and causing the child to fall isn't an issue as we both have witnessed this."
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...So, is the issue whether or not it was done {i}on purpose{/i}...?'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "<Good>. This level of the topic does exist, but I'm glad we got the rest out of the way quickly."
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "What is this person... even saying...? Ugh, it's already so obvious with how boldly she did it. Is she seriously saying that sticking her leg out in front of a kid who seems like he's having fun {i}isn't{/i} on purpose?!"
 show erika_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I was simply feeling a bit fickle, so I stuck my leg out like this.'
 show nao_v002 sinken at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "People aren't made out of stone. You can move your legs, change your position. Nothing is strange about that."
 show erika_v001 normal_close at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'How good can your intent be when you watched the child run up to you? Can you make that clear to me?'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 normal_close at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Don't make me out to be stupid. I'm not blind!"
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Splendid. These two claims are in direct conflict with each other. That is the point at issue.'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "A child was running, tripped on my leg, and fell. And then, there's whether or not it was {i}on purpose{/i}..."
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'You claim that I tripped that child on purpose, while I claim that the child tripping on my leg was a coincidence. '
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'These two conflicting claims are shut inside the catbox...'
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '....Catbox? What are you saying?'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'These two conflicting claims are mutually exclusive, meaning they cannot exist simultaneously.'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Both are possible. However, without opening the catbox, we cannot ascertain which has happened.'
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'To arrive at the truth within the catbox... in your words, you would need solid evidence.'
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") " <Good>. That's exactly it. So, then, allow me to inquire again."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show nao_v002 normal at inactive
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'When you say I stuck out my leg on {i}purpose{/i}, do you happen to have proof for that?'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 futeki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Me seeing it clearly with my own eyes is proof alone!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I maintain the possibility that you are using false evidence against me.'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'In other words, there is a possibility that there could be something wrong with your sight, so it impedes your ability to properly witness events. I also declare that there is a possibility something is wrong with your brain, so you make up everything that you say.'
 show erika_v001 normal at inactive
 show nao_v002 odoroki at active
 show nao_v002 odoroki at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh?! You... you think you can excuse yourself like this?!'
 show nao_v002 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Allow me to rephrase. As a witness, do you think you can prove whether it was {i}on purpose{/i} or not?'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator 'That puts me on the spot. ...On purpose or not, the problem is the fact her intentions are invisible.'
 narrator "No matter how evil her face looked, or how much I measure the timing of when she stuck out her leg in front of the kid... it ultimately wouldn't be proof enough for whether it was {i}on purpose{/i} or not."
 narrator "No, it's just that. Even though she stuck out her leg in front of the kid, me witnessing that isn't proof enough."
 show nao_v002 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Are witnesses... this powerless? Meaningless?! That's just stupid!"
 show nao_v002 sinken at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Knox's 9th, it is permitted for observers to let their own conclusions and explanations be heard."
 show erika_v001 normal_close at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show nao_v002 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'You observed me kicking my leg out in front of the child and watched him fall.'
 show nao_v002 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'From that observation, you interpreted it this way, claiming: "This intellectual girl purposefully made this child fall over."'
 show nao_v002 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Since the claim itself is permitted as an act, there is no issue.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "In essence, this is what the girl wants to say. Since I felt as though she {i}purposefully{/i} made him fall, it's an act of selfishness on my part."
 narrator "And so, that alone isn't proof enough..."
 show nao_v002 fuan at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Witnesses are... really this weak...?!'
 show nao_v002 fuan at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "How unfortunate for you. In the real world, a witness' ability in proving the credibility of their testimony will be put to the test."
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'It is as I have stated to you before. ...Do you or do you not have issues with your eyesight? Do you or do you not have issues with your perception? These various things will be put to the test.'
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'The result. According to the work of competent lawyers, although there may have been eyewitnesses to a crime, their ability to prove that fact may be rejected as well.'
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...That's just... insane..."
 show nao_v002 fuan at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Yes, I concur. It's completely insane. <It's nonsense>!"
 show erika_v001 normal_close at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '......Huh...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide nao_v002
 hide fade onlayer curtain
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Even if there is clear evidence or an eyewitness, just with the negotiations between the lawyer and attorney alone, it is possible for them to rule evidence as rejectable or as a misobservation!'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "When this ridiculous court farce contaminates such beautiful reasoning, doesn't just thinking about it make you sick?!"
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "That's why I want to respect it! The fact that you say you clearly witnessed it in your testimony!"
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "No, no, it's not just that! It's the fact that I, in the period of me being lost in my own intelligent thoughts, was disturbed by this loud, annoying, bumbling snot-nosed BRAT running amok, so you believe that I kicked out my leg in the crime scene!!!"
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Aah, if this was a proper mystery world, your witness report would be respected above all else, and it ought to beautifully put an end to me in a checkmate!'
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "But I'm stuck in this hideous Human world where irrational lines of thinking go unpunished!"
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "YES, I did it on purpose! AND YES, you clearly saw it happen! But you can't even PROVE IT!!!! AAAAAAAAAAAHHH, IT'S SOOOO RIDICULOOOOOUUSSS!!!!"
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "...Isn't it? ......Reflecting on my time living in this world, as we approach the horizon, I seriously feel as though all I want to do is to flap my wings into that beautifully intellectual world up ahead. "
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Oh my, do excuse me. That was too advanced for you. It seems I got a little carried away. We're already done here. Please do go stand someplace else."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '........................'
 hide nao_v002
 with Dissolve(0.2)
 narrator "What's... with that woman?"
 narrator 'Right in front of my eyes, she boldly kicks out her leg and makes that child fall over. I then get grilled on that fact, and on top of that, she herself admits that she kicked out her leg on purpose, but... I have no proof...?'
 narrator "And as if that wasn't enough, she mocks me... going off about how she's in a ridiculous world where things go unpunished? I just don't get it...!"
 play sound ['audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav'] fadeout 1.0
 stop music fadeout 2.0
 narrator "I feel like I'm going to puke... but above all else, even hanging out with that unpleasant woman was just so unnecessary."
 narrator "She's telling me to go over there, so I'll gladly go over there for her. I won't ever meet her again anyway."
 show nao_v002 normal_close at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Bye now.'
 show nao_v002 normal_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Goodbye. I won't even remember you, you irrelevant random."
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's my line..."
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator 'With a blatant expression of displeasure, Nao turns her heel and walks off.'
 narrator 'Without even so much as glancing at her back, Erika once again returns her gaze to the horizon.'
 play music "<loop 0>audio/bgm/BGM_QUEST4_COLLAB2.ogg"
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 pause 2.0
 show dlanor_v001 fuan_close at mei_left
 with Dissolve(1.0)
 show erika_v001 normal at inactive
 show dlanor_v001 fuan_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'As usual... you do not behave MATURELY.'
 show dlanor_v001 fuan_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "My, if it isn't my friend. I thought my behavior was adult enough, though."
 show erika_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'If the noisy children were bothering you in the first place, you should have taken the time to move to another LOCATION.'
 show dlanor_v001 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I had wanted to chat with you while watching the horizon.'
 show dlanor_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I'm a bit annoyed since I was interrupted. ...Isn't the motive for the crime enough?"
 show erika_v001 normal at inactive
 show dlanor_v001 fuan at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Moreover, being defiant about being seen sticking your leg out WAS...'
 show erika_v001 normal at inactive
 show dlanor_v001 fuan_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "For me to even call a character like that a friend of mine doesn't sit well in my HEART."
 show dlanor_v001 fuan_close at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Hmph. Says the killer doll without a heart.'
 show erika_v001 normal_close at inactive
 show dlanor_v001 smile at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...You are TALKATIVE. It seems you are in a good MOOD.'
 show erika_v001 normal_close at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "However, I do recommend for the future that you more openly present yourself with this good mood you're IN."
 show dlanor_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Me? In a good mood?'
 show dlanor_v001 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Hmph.'
 show dlanor_v001 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "You really are doll-like. You just don't understand my delicate heart."
 show erika_v001 normal_close at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "I understand it loud and CLEAR. ...I was thinking that I might have disappointed with this method of delivering a celebration present for Beatrice's BIRTHDAY."
 show dlanor_v001 normal at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It obviously is a disappointment. If it weren't for my master's orders, no one would go out of their way to Beatrice's party all the way on that island."
 show dlanor_v001 normal at inactive
 show erika_v001 sinken_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Yeah, it is a disappointment. It's boring. Originally, I was supposed to be the one welcomed as a guest by that witch."
 show erika_v001 sinken_close at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Do not worry, ERIKA.'
 show erika_v001 sinken_close at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'You are a DETECTIVE. Where a detective visits, an incident OCCURS.'
 show erika_v001 sinken_close at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Surely there is an incident stirring up on Rokkenjima that will not leave you BORED.'
 show dlanor_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Well, I guess you are right. I am the detective after all. Wherever I go, an incident will occur.'
 show dlanor_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '*giggle*giggle*giggle*...!!'
 show erika_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'If your mind has cleared up by now, I want to continue from EARLIER. You were still in the middle of explaining that closed room substitution TRICK.'
 show dlanor_v001 normal at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Aah, that's right! Uuuhh, where was I againn?! It's so ground-breaking, so wonderful!!"
 hide erika_v001
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'Like a little animal wagging its tail, Erika once again regained her fervorous attitude, returning to her mystery discussion with Dlanor.'
 show dlanor_v001 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...It is both a surprise and honor that you enjoy speaking to me so MUCH.'
 show dlanor_v001 normal_close at inactive
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Well, you {i}were{/i} my motive in putting my leg in front of that kid.'
 call chapter_end
 jump event01_30_01