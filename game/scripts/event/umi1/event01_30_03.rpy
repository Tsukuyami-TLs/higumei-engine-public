label event01_30_03:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=4
 $ event_store.current_chapter='event01_30_03'
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
 show expression 'images/bg/AdvBg_2281.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST2_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'I thought I could just close my eyes for 10 minutes, and sure enough, I fell asleep.'
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'Mion-san and Shion-san are asleep too, but I woke up from feeling like I was tossing and turning.'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Oh gosh. I might have... overslept after all... maybe.'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan_close at inactive
 show mion_v002 smile at active
 show mion_v002 smile at deepbreath_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ha~aah! I slept goood! This ol' man's charged up 120%%!"
 show mion_v002 smile at inactive
 show shion_v002 odoroki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "What time is it right now? Huh, it's already after 6:00?"
 show shion_v002 odoroki at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That rain is coming down too. Tomorrow's gonna be big picturesque!"
 hide shion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...The window lock. Did you manage to fix it?'
 show nao_v002 normal at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Hm? Ehehe~...'
 hide nao_v002
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'I guess not. Please apologize to a servant later.'
 show shion_v002 fuan at inactive
 show mion_v002 fuan_close at active
 show mion_v002 fuan_close:
  yanchor 1.0
  linear 0.5 pos (1440,1250)
 pause 0.5
 show mion_v002 fuan_close:
  yanchor 1.0
  pos (1440,1250)
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Okayy...'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator 'At that moment, the house phone in the room rang.'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_521_phone_pickup.wav'
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, umm, yes, hello?'
 hide nao_v002
 with Dissolve(0.2)
 Character('Phone',ctc="ctcArrow", ctc_position="fixed") '"I am sorry to intrude on your relaxation time. The preparations for dinner are complete. If you would please come over to the reception room."'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Okay. I'll be there soon."
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'm going too, Sis. Please be a bit more sophisticated at dinner, yeah?"
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yeah, yeah. If I don't, the witch is gonna curse mee~."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '.....................'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Even though I tried so hard to forget... I was reminded of the ghost story about the witch again. But since I just had that nap, my face eased up a bit.'
 narrator "Having a dinner I could boast about, I'll be charged up to 120%% too, and starting tomorrow, my mood might even improve on its own."
 play audio 'audio/sfx/SE_5034_knock.wav'
 narrator "Before I go down, I'll knock on the door to Erika-san's room as well."
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Erika-san. It seems that dinner is ready, so would you like to go down there together?'
 hide nao_v002
 with Dissolve(0.2)
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "...Please go on without me. My hair isn't set yet..."
 narrator 'Through the door, I could hear a grunting voice grappling with those long twintails.'
 narrator "I've been kind of longing for hair as long as that, but it really is a big handful..."
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Mmm, I already smell the deliciousness from here~!'
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "This is definitely a smell you wouldn't get in Hinamizawa, huh?"
 hide shion_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Lunch earlier was the absolute best it could have been, so I'm super looking forward to dinner!"
 show nao_v002 smile at inactive
 show mion_v002 smile at active
 show mion_v002 smile at jump_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Meals really do decide everything, huh?!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2331.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'I apologize for the wait, everyone. I will gladly guide you to your seats.'
 hide shannon_v001
 with Dissolve(0.2)
 narrator 'Upon the snow white tablecloth, there was a beautiful arrangement of French cuisine that could probably satisfy your appetite just by looking.'
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'Our family head chef, Gohda, has brought to you today his rendition of Spanish cuisine.'
 hide shannon_v001
 with Dissolve(0.2)
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Spanish is close to French. ...Phew, close enough...'
 hide nao_v002
 with Dissolve(0.2)
 Character('Toshiro Gohda',ctc="ctcArrow", ctc_position="fixed") 'Dear me. ... I do wonder if Erika-sama is still in her room?'
 narrator 'Gohda-san had appeared at the best possible moment to introduce his own cooking.'
 narrator 'In that moment, everyone wanted to sit and listen. But he seemed to be worried that Erika-san was still missing.'
 narrator 'However, if we were to wait for Erika-san, we would miss our chance to eat while the food was still at its most ideal.'
 narrator "With a cough to clear his throat, Gohda-san had begun his explanation on tonight's cuisine."
 narrator 'By the time we had finished a subtle appetizer and even gotten through a deliciously light-flavored soup, Erika-san had finally gone down the stairs.'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I deeply apologize for the wait.'
 hide erika_v001
 with Dissolve(0.2)
 Character('Toshiro Gohda',ctc="ctcArrow", ctc_position="fixed") 'No, no, it was no problem! Now, please, have your seat!'
 show erika_v001 normal at mei_right
 show shannon_v001 smile at mei_left
 with Dissolve(0.5)
 show shannon_v001 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Ah, I have my own chopsticks, so it would be splendid if you took away my silverware.'
 show erika_v001 normal at inactive
 show shannon_v001 fuan at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'B-But... eating soup with chopsticks is...'
 show shannon_v001 fuan at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "You're underestimating the refined art of Erika-Chopstick-Jutsu, aren't you? Allow me to demonstrate my soup eating chopstick technique!"
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Whaaat, I totally wanna see this.'
 narrator 'For someone unrelated looking in from a distance, Erika-san might actually seem like a really amusing person.'
 window hide None
 stop music fadeout 2.0
 pause 3.0
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 narrator 'After dinner, we all sat down in front of the TV, relaxing on the sofa.'
 narrator "After getting pleasantly stuffed from all that food, I got the strange feeling that I had done my best today, even though I haven't done much at all lately."
 narrator 'Of course, "Detective Wanyan" was on TV. The cast on the show has multiplied since the last time I watched it.'
 narrator 'Speaking of which, why are the police in this show just letting an elementary schooler and that big slug stand there on the scene of a murder incident??'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Nonononono! They should have held back on thaat! They revealed the culprit way too faaast!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'There are mysteries with intellectual puzzles, but sometimes others will entirely be about the competitive nature between the detective and culprit.'
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Definitely. In the end, the piles of evidence are just like punches. No matter how many they throw at you, it's possible to put up with all of it."
 hide erika_v001
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Shion, you've never learned when to give up since way back in the day, huh?"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "*giggle*. Well, watching a killer that doesn't know when to give up in a mystery can be quite pleasant, though."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "If it were me... I would be a pretty tough character. \nI daresay I'd put my all into it. *giggle*."
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Tch. ...I want everyone to watch "The Kaneda Case Files" too. It\'s suuper interesting, but...'
 narrator "I'm not sure if this is a feeling of alienation or if this is me being a contrarian. ...I just feel left out of the circle."
 narrator 'I got up from the sofa. Over near the bar table, Shannon-san was there cleaning up.'
 play audio 'audio/sfx/SE_515_tableware.wav'
 show shannon_v001 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "I'm wondering if you'd like me to make you a drink...?"
 show shannon_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Ah, no. I've had more than enough."
 show nao_v002 smile at inactive
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'Detective Wanyan sure is interesting, huh?'
 show nao_v002 smile at inactive
 show shannon_v001 fuan at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "I've also been recommended it to the other servants, but nobody has started reading it..."
 show shannon_v001 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...You're also a Wanyan fan? ...Have you seen the movie?"
 show nao_v002 fuan at inactive
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'Of course! I watched it in a huge theater in Tokyo♪'
 show shannon_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Have you read The Kaneda Case Files?'
 show nao_v002 normal at inactive
 show shannon_v001 smile at active
 show shannon_v001 smile at nod_transform
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "Yeah, I love that one too. It's a pretty difficult choice, but I liked it better."
 hide nao_v002
 hide shannon_v001
 with Dissolve(0.2)
 narrator 'Then, Shannon-san...'
 show nao_v002 smile at mei_left
 show shannon_v001 smile at mei_right
 with Dissolve(0.5)
 show shannon_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I believe I would like a glass to drink after all. A carbonated red cola with extra sugar mixed in, please.'
 show nao_v002 smile at inactive
 show shannon_v001 smile_close at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") '*giggle*. As you wish.'
 show shannon_v001 smile_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '........................'
 show shannon_v001 smile_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Um... Shannon-san. This is just between you and I... okay?'
 show nao_v002 normal at inactive
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'Okay...?'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 2.0
 show shannon_v001 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Jessica-san and them have been scaring me with this island's ghost story about a witch."
 show nao_v002 fuan at inactive
 show shannon_v001 normal at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'Ghost story... about a witch... you say...?'
 hide shannon_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'A bewildered expression. ...Yeah, that reaction is good.'
 narrator 'Everyone has been claiming that Beatrice, the witch, "exists".'
 narrator "Normally, even I'd be able to read the mood, like how you wouldn't want to indiscriminately deny the existence of Santa Claus."
 narrator '...But I\'m a bit more of the contrarian type. As they join in and declare that Beatrice "exists", I more so get the feeling of wanting to be shown proof.'
 narrator '...Proof? ...This is no joke. I just wanted to relax on this island, so why did it have to come to this?'
 show nao_v002 normal at mei_left
 show shannon_v001 smile at mei_right
 with Dissolve(0.5)
 show shannon_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'As I thought, Shannon-san... you believe in Beatrice too?'
 show nao_v002 normal at inactive
 show shannon_v001 smile_close at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'Yes. ...Beatrice-sama "exists".'
 show shannon_v001 smile_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'When you say exists, where would that be?'
 show nao_v002 normal at inactive
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'Right here, right now, she surely "exists".'
 play music "<loop 0>audio/bgm/BGM_QUEST7_COLLAB2.ogg"
 hide shannon_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "Shannon-san is laughing sweetly with a smile on her face... but I get the feeling that I've soured her mood instead."
 show nao_v002 sinken at mei_left
 show shannon_v001 smile at mei_right
 with Dissolve(0.5)
 show shannon_v001 smile at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "If she does exist, she'd better impress me with her appearance."
 show shannon_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "If she shows her form begrudgingly, acting like she owns the place, she'd ruin the experience."
 show nao_v002 normal at inactive
 show shannon_v001 normal_close at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") '...It seems like you are quite poisoned with anti-magic toxin.'
 show shannon_v001 normal_close at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Anti-magic... toxin...?'
 show nao_v002 odoroki at inactive
 show shannon_v001 normal at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "They say that Humans who don't believe in magic... emit a poisonous gas that is harmful to witches."
 show shannon_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So, basically... humans who don't believe in Beatrice will repel her, is what you're saying?"
 show shannon_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's relieving then. She can't appear to people who don't believe in her in the first place."
 hide shannon_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "If she only appears to those who believe, she's no different than Santa Claus. People who don't want to meet her will go on without meeting her..."
 show shannon_v001 fuan at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show shannon_v001 fuan at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "It's... actually the other way around."
 show shannon_v001 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show nao_v002 fuan at inactive
 show shannon_v001 normal_close at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "Beatrice-sama holds grudges towards people who don't believe in her existence."
 show nao_v002 fuan at inactive
 show shannon_v001 normal at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "She'll come to you to demonstrate that she really exists, play strange pranks on you, even frighten you..."
 show shannon_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I heard that from Kanon-san. Like how in rooms that no one should have been able to enter, creepy magic circles were found?'
 hide nao_v002
 hide shannon_v001
 with Dissolve(0.2)
 narrator "Shannon-san's face clouded over for a split second. She had this look like I had surprised her by suddenly saying something foolish... and was criticizing me for it."
 show shannon_v001 fuan at mei_center
 with Dissolve(0.5)
 show shannon_v001 fuan at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'Nao-sama... Saying things like that can be very--'
 play audio 'audio/sfx/SE_5029_slap_back.wav'
 pause 0.5
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide shannon_v001
 hide fade onlayer curtain
 show jessica_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Good eveniing~~!! Guess who came to mess around~~!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide jessica_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Jessica-san had appeared in good spirits, holding something.'
 narrator 'To Jessica-san, us coming here on vacation is probably more like friends coming to sleep over.'
 show mion_v002 odoroki at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Whaaat?! Could that little board game you're carrying really be?!"
 show mion_v002 odoroki at inactive
 show jessica_v001 futeki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I always knew this day would come! After buying this all those years back, it's finally time to play...!"
 hide mion_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 futeki at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ah, jeez. Bringing a board game in front of Sis like that is a huge deal, you know?'
 hide jessica_v001
 hide shion_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show mion_v002 smile at active
 show mion_v002 smile at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Let's go! Let's go! Everyone, let's go!! You wanna play with us too, Erika-san?"
 show mion_v002 smile at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I do think I will be spending time leisurely in my room.'
 show erika_v001 normal_close at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Whaaaat? You're gonna run oooff? Board games are a clash of brains!"
 show erika_v001 normal_close at inactive
 show mion_v002 futeki_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Well, this brain doesn't get me that many wins, though. You still gonna run off~?"
 show mion_v002 futeki_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Hm. Cheap provocation method on your part. But if you say that much, I guess I must accept your offer.'
 hide mion_v002
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Are you sure? Sis doesn't take any excuses when she plays games with people, okay?"
 hide erika_v001
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Mion-san, you know a lot about board games?'
 show jessica_v001 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Not even just board games. Mion-san and competition are like fish and water.'
 play audio 'audio/sfx/SE_226_shine.wav'
 show nao_v002 fuan at inactive
 show jessica_v001 futeki at active
 show jessica_v001 futeki at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Sweet! I'm the grandkid of Kinzo Ushiromiya, so competition is first nature to me too!"
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Let's get everyone to play! Me, Shion, Erika-san and Jessica-san. Nao-chan and Shannon-san can jump in too!"
 show shannon_v001 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'The sentiment alone is enough for me. I have yet to do all my chores in the mansion...'
 show mion_v002 smile at inactive
 show shannon_v001 smile_close at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "I'll take my leave for today..."
 hide mion_v002
 hide shannon_v001
 with Dissolve(0.2)
 narrator 'Shannon-san went off with a slight bow out of consideration.'
 show nao_v002 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Mion-san. Did you have the conversation with her... about the window lock?'
 show nao_v002 normal at inactive
 show mion_v002 fuan at active
 show mion_v002 fuan at chara_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '*gulp*.'
 hide nao_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Sis. Wouldn't it be best to apologize right away for something like this?"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show shannon_v001 normal at mei_left
 with Dissolve(0.5)
 show shannon_v001 normal at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'What conversation did you want to have...?'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show shannon_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Ah... about the window. *giggle*.'
 show shannon_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Though we are on an island separated from the outside world, it is quite unpleasant for a girl to have her room left unlocked, even by window.'
 hide shannon_v001
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Aah, so you're talking about the window locks? Those are old, so there's a bit of a trick to using them."
 hide erika_v001
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Nahh... I was so psyched that we got a really nice room, that while I was opening the window... I kind of used all my force on the lock...'
 hide jessica_v001
 hide mion_v002
 with Dissolve(0.2)
 show shion_v002 fuan_close at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show shion_v002 fuan_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'm sorry my sister is such a country bumpkin."
 show shion_v002 fuan_close at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm really sorry about Mion-san being a country bumpkin. ...I do wonder if we can have you take a look at it?"
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show shannon_v001 smile at mei_left
 with Dissolve(0.5)
 show shannon_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Shannon, go check it out.'
 show jessica_v001 smile at inactive
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'Certainly...'
 hide shannon_v001
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Alriiiiight, let's go let's go let's go!! Okay, so this is the type of game where whoever survives 'til the end wins!!"
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'When Mion-san is playing a game, she has to make sure she has a punishment game set.'
 show nao_v002 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Wait, what?!?! We're running this with punishment games?! Whenever there's risk involved, the Ushiromiya blood inside me gets fired up!"
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I'll be the winner, in any case. Do allow me to choose a punishment game that would work in my favor."
 show erika_v001 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Erika-san, you'd best not underestimate Sis, yeah? She'll do anything to win."
 hide shion_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...For starters, I'll be glad if we won't be dealing with explosions, traps, or bodily harm."
 show nao_v002 fuan at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'My, my. In the face of these punishment games, this is going to become quite the thrilling session. *cackle*cackle*cackle*!!'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_center
 with Dissolve(0.5)
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'W-Woah. I had no idea it was gonna be {i}that{/i} kind of dangerous...'
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'No matter what game it is, if Mion-san comes into the picture, it transforms into a much darker game...'
 narrator 'No one wanted to get their pillow wet with tears of humiliation on their first night here. Everyone diligently looked over the rules.'
 play audio 'audio/sfx/SE_526_door_open.wav'
 pause 0.5
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "I've fixed the lock!"
 hide shannon_v001
 with Dissolve(0.2)
 show mion_v002 odoroki at mei_right
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 odoroki at inactive
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Woah! That was real fast! To think you had gone up just now, jeez!'
 show mion_v002 odoroki at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Right? But anyway, this is a relief. You've fixed it in quite a flash."
 hide nao_v002
 hide mion_v002
 with Dissolve(0.2)
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "There's a trick in using it. From tomorrow forward, we would appreciate if you handled it with care."
 hide shannon_v001
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Hear that, Sis? Now go reflect on your actions.'
 show shion_v002 normal at inactive
 show mion_v002 fuan at active
 show mion_v002 fuan at chara_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Th-this ol' man only wanted to review it from the perspective of a heavy-handed guest! Really!!"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show shannon_v001 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") "*giggle*. Okay, I'll take my leave now."
 show shannon_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Thanks, Shannon! Don't let the adults know that I'm playing over here...!"
 show jessica_v001 smile at inactive
 show shannon_v001 smile at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") '*giggle*. I will act under this instruction.'
 hide jessica_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show shannon_v001 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Excellent work, Shannon-san. Has a robber broken in from the window or anything?'
 show erika_v001 normal at inactive
 show shannon_v001 smile_close at active
 Character('Shannon',ctc="ctcArrow", ctc_position="fixed") 'No. Please be at ease.'
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Shannon-san bowed very deeply and returned to the mansion.'
 show jessica_v001 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Alright!! Let's go!!"
 play audio 'audio/sfx/SE_226_shine.wav'
 show jessica_v001 smile at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Yeah, that\'s the spirit!! All right, Jessica-san, here\'s our\n "Rokkenjima Club Activity Business Trip Five-Demon Firefiiiiiiiight"!!!'
 stop music fadeout 2.0
 window hide None
 hide mion_v002
 hide jessica_v001
 with Dissolve(0.2)
 pause 2.0
 play music "<loop 0>audio/bgm/BGM_QUEST2_COLLAB2.ogg"
 narrator 'When you play a board game for the first time, you usually spend quite some time going over all of the rules.'
 show jessica_v001 fuan at mei_center
 with Dissolve(0.5)
 show jessica_v001 fuan at active
 show jessica_v001 fuan at chara_shake_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'HaaaAAaaaah... aaaah...'
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'When Jessica-san yawned, Shion-san and I were caught up in the yawn chain as well.'
 show erika_v001 sinken at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Wait a second. This one is saying "it\'s okay to do this", right? Does this mean "it\'s okay not to do this" as well?'
 show erika_v001 sinken at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Umm, wait, wait. First, we settled we'd go in clockwise to collect taxes, and then income processing was..."
 hide erika_v001
 show shion_v002 sinken at mei_left
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Sis, before, I was going to be the first to have my income processed, and then we would collect from there, right?'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show jessica_v001 fuan at mei_right
 with Dissolve(0.5)
 show jessica_v001 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Yeah, hold on. You guys, we absolutely cannot cut corners in a game.'
 show nao_v002 fuan at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ahhh... hahahh... I wish I brought over a game that was easier to play... '
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Oh my. Nao-chama let out a massive yawn.'
 show shion_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It has clearly already reached the point in the night where children shouldn't be up."
 show erika_v001 normal at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "The game hasn't reached a result, and we haven't even gotten to enjoy the process. Won't we end it here for today?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide shion_v002
 hide erika_v001
 hide fade onlayer curtain
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Aaaah-, come on, come on!! Just as this ol' man charged up all this power, we decide to end it?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan_close at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm already getting sleepy. ... I want to take a shower and stuff."
 show nao_v002 fuan_close at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Welp, I guess that settles it.'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Since Mion-san would have destroyed all of us ingame had it continued past that point, we called it here and went on our ways.'
 narrator 'Besides, having a punishment game enforced on everyone second place and below was too much... Even for a kid from Hinamizawa... {i}that{/i}... was a little...'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Jessica-san returned to the mansion. The rest of us went up to the second floor in a huddle.'
 show shion_v002 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "What's the verdict? Did we enjoy ourselves a little with that club activity?"
 show shion_v002 smile at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'As expected, dice-throwing games relying on luck are not my thing.'
 show shion_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Unlike my master, eternally rolling over and over until you get the number desired is something I could never do.'
 hide erika_v001
 hide shion_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Did you have fun too, Nao-chan?'
 show mion_v002 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...By the time it felt fun, I feel like we could have been laughing carelessly playing Russian roulette with live bullets.'
 show nao_v002 fuan at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Jessica-san said it herself, didn't she? About how there's a huge prize hidden within the insanity of risk."
 show nao_v002 fuan at inactive
 show mion_v002 smile at active
 show mion_v002 smile at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I feel like the head of this place, Kinzo-san, would enjoy the madness of this ol' man's club activities."
 hide nao_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Umm, who has the key?'
 show shion_v002 normal at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "This ol' man has iiit~. Opening it now~."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Okay, everyone. Good night.'
 show erika_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Good night, Erika-san.'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show nao_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Oh, yeah. Nao-chama.'
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That 'Nao-chama', would you stop calling me that...?"
 stop music fadeout 2.0
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I heard. ...I suppose you had spoken with Shannon-san earlier?'
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "About how Beatrice loves playing pranks on people who don't believe, et cetera... "
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'And how you denounced the Golden Witch outright, even with her having that level of magnificence.'
 show nao_v002 fuan at inactive
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "...I do hope that she doesn't play some sort of creepy prank on you because of that...?"
 show erika_v001 fuan at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'You really are poorly mannered, Erika-san... treating people like children.'
 show erika_v001 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm not afraid of that ghost story or anything."
 show nao_v002 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '<Good>.'
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Please do keep that determination up for me. *giggle*giggle*giggle*...'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_526_door_open.wav'
 narrator 'Erika-san directed a sarcastic laugh at me while disappearing into her room.'
 narrator 'Mion-san, finally remembering which pocket she had left the key in, picked it out and opened the door.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Who's gonna shower after me?"
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Nao-san can go after, right?'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'd be happy to, but I want to give myself a proper bath."
 play audio 'audio/sfx/SE_5004_lightoff.wav'
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'I hit the light switch. Without breaking the Western-style house feel, the lights revealed some disturbing evidence.'
 window hide None
 show black_cover as bg
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2320.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST7_COLLAB2.ogg"
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
 narrator "This is... a prank... geared towards people who don't acknowledge the witch's existence."
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
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 pause 2.0
 call chapter_end
 jump event01_30_04