label event01_30_03:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST2_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator 'I thought I could just close my eyes for 10 minutes, and sure enough, I fell asleep.'
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'Mion-san and Shion-san are asleep too, but I woke up from feeling like I was tossing and turning.'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '...Oh gosh. As expected, I probably overslept... I guess.'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan_close at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at deepbreath_transform,active
 show shion_v002 fuan_close at inactive
 mion "Ha~aah! I slept goood! This ol' man's charged up 120%!"
 show shion_v002 odoroki at active
 show mion_v002 smile at inactive
 shion "What time is it right now? Huh, it's already after 6:00?"
 show mion_v002 smile at active
 show shion_v002 odoroki at inactive
 mion "That rain is coming down too. Tomorrow's gonna be big picturesque!"
 hide shion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao '... The window lock. Is it fixed?'
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion 'Hm? Ehehe~...'
 hide nao_v002
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion 'It was impossible. Please apologize to the servant later.'
 show mion_v002 fuan_close at active
 show mion_v002 fuan_close:
  linear 0.5 pos (1440,1250)
 show shion_v002 fuan at inactive
 pause 0.5
 mion 'Okayy...'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator 'At that time, the house phone in the room rang.'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_521_phone_pickup.wav'
 show nao_v002 normal at active
 nao 'Ah, umm, yes, hello?'
 hide nao_v002
 with Dissolve(0.2)
 Character('Phone',ctc="ctcArrow", ctc_position="fixed") '"I am sorry to intrude on your relaxation time. The preparations for dinner are complete. If you would please come over to the reception room."'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao "Okay. I'll be there soon."
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "I'm going too, Sis. Please be a bit sophisticated at dinner, yeah?"
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Yeah, yeah. If I don't, the witch is gonna curse mee~."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '...'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2371.png' as bg
 with Dissolve(1.0)
 narrator 'Even though I tried so hard to forget... I remembered the ghost story of the witch again. But since I had that nap, my face relaxed a bit.'
 narrator "If I have a boastful dinner, I'll get charged up to 120% too, and from tomorrow, my mood might even get replaced with an even better one on its own."
 play audio 'audio/sfx/SE_5034_knock.wav'
 narrator "Before I go down, I'll knock on the door to Erika's room as well."
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'Erika-san. It seems that dinner is ready, so would you like to go down there together?'
 hide nao_v002
 with Dissolve(0.2)
 erika "... Please go without me. My hair isn't set..."
 narrator 'Through the door, I could hear a grunting voice grappling with those long twintails.'
 narrator "I've been kind of longing for hair as long as that, but it really is a big handful..."
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'Waahh, I already smell the deliciousness from here~!'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "This is definitely a smell you wouldn't get in Hinamizawa, huh?"
 hide shion_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show mion_v002 smile at inactive
 nao "Lunch earlier was the absolute best it could have been, so I'm super looking forward to dinner!"
 show mion_v002 smile at jump_transform,active
 show nao_v002 smile at inactive
 mion 'As expected, meals decide everything, huh?!'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2331.png' as bg
 with Dissolve(1.0)
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon 'I apologize for the wait, everyone. I will gladly guide you to your seats.'
 hide shannon_v001
 with Dissolve(0.2)
 narrator 'Upon the snow white tablecloth, there was a beautiful arrangement of French cuisine that could probably satisfy your appetite just by looking.'
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon 'Our family head chef, Gohda, has brought to you today his rendition of Spanish cuisine.'
 hide shannon_v001
 with Dissolve(0.2)
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao '...Spanish is close to French. ...Safe, safe...'
 hide nao_v002
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'Dear me. ... I do wonder if Erika-sama is still in her room?'
 narrator 'Gohda-san had appeared at the best possible moment to introduce his own cooking.'
 narrator 'In that moment, everyone wanted to sit and listen. But he had only come out of worry that Erika was still missing.'
 narrator 'However, if we were to wait for Erika-san, we would miss our chance to eat while the food was still at its most ideal.'
 narrator "With a cough to clear his throat, Gohda-san had begun his explanation on tonight's cuisine."
 narrator 'By the time we had finished a subtle appetizer and even gotten through a deliciously light-flavored soup, Erika had finally gone down the stairs.'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'I deeply apologize for the wait.'
 hide erika_v001
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'No, no, it was no problem! Now, please, have your seat!'
 show shannon_v001 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shannon_v001 smile at inactive
 erika 'Ah, for me, if I would have my own chopsticks. Using silver to eat would be quite fine.'
 show shannon_v001 fuan at active
 show erika_v001 normal at inactive
 shannon 'B-, but... eating soup with chopsticks is...'
 show erika_v001 smile at active
 show shannon_v001 fuan at inactive
 erika "You're underrating Erika's skill in using chopsticks, aren't you? Allow me to demonstrate my soup eating chopstick technique!"
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Whaaat, I wanna see this hardcore.'
 narrator 'For unrelated people looking in from a distance, Erika-san might seem like a really amusing person.'
 window hide None
 stop music fadeout 2.0
 pause 3.0
 play music 'audio/bgm/BGM_GACHA_COLLAB2.wav'
 narrator 'After dinner, we were all sat in front of the TV, relaxing on the sofa.'
 narrator "While being pleasantly full from all that food, even though I shouldn't have been doing that much these days, I started getting the strange feeling that I had done my best today."
 narrator 'Of course, "Detective Wanyan" was on TV. The cast on the show has multiplied since the last time I watched it.'
 narrator 'Speaking of which, why are the police in this show just letting an elementary schooler and that big slug stand there on the scene of a murder incident??'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 sinken at active
 mion 'Nonononono! They should have held back saying thaat! They revealed the culprit too faaast!'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Sometimes mysteries have intellectual puzzles, but others will be entirely about hand-to-hand combat.'
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion "Definitely. In the end, the bunches of evidence are just like punches. Like no matter how many they throw at you, it's possible to put up with all of it."
 hide erika_v001
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Shion, you've never learned to give up since back in the day, huh?"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika "*giggle*. Well, seeing a killer that doesn't know when to give up in a mystery is quite pleasant, though."
 show erika_v001 normal at active
 erika "If it were me... I would be a pretty tough character; I daresay I'd put my all into it. *giggle*giggle*"
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Sheesh. ...Everyone wants to see "The Kaneda Case Files". It\'s suuper interesting, but...'
 narrator "I'm not sure if this is a feeling of alienation or this is me being a contrarian. ...I feel left out of the circle."
 narrator 'I stand up on the sofa. Over near the bar table, Shannon was there cleaning up.'
 play audio 'audio/sfx/SE_515_tableware.wav'
 show nao_v002 smile at mei_left
 show shannon_v001 smile at mei_right
 with Dissolve(0.5)
 show shannon_v001 smile at active
 show nao_v002 smile at inactive
 shannon 'I wonder if you would like me to make a drink for you...?'
 show nao_v002 smile at active
 show shannon_v001 smile at inactive
 nao 'Ah, no. I have had more than enough.'
 show shannon_v001 smile at active
 show nao_v002 smile at inactive
 shannon 'Detective Wanyan sure is interesting, huh?'
 show shannon_v001 fuan at active
 show nao_v002 smile at inactive
 shannon "I've also recommended it to the other servants, but nobody has started reading it..."
 show nao_v002 fuan at active
 show shannon_v001 fuan at inactive
 nao "... You're also a Wanyan fan? ... Have you seen the movie?"
 show shannon_v001 smile at active
 show nao_v002 fuan at inactive
 shannon 'Of course! I watched it in a huge theater in Tokyo♪'
 show nao_v002 normal at active
 show shannon_v001 smile at inactive
 nao '... Have you read The Kaneda Case Files?'
 show shannon_v001 smile at nod_transform,active
 show nao_v002 normal at inactive
 shannon "Yeah, I love that one too. It's a pretty difficult choice, but I liked it better."
 hide nao_v002
 hide shannon_v001
 with Dissolve(0.2)
 narrator 'Then, Shannon-san...'
 show shannon_v001 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show shannon_v001 smile at inactive
 nao '... I believe I would like a glass to drink. A red cola, carbonated, extra sugar, and shaken, please.'
 show shannon_v001 smile_close at active
 show nao_v002 smile at inactive
 shannon '*giggle*. As you wish.'
 show nao_v002 normal at active
 show shannon_v001 smile_close at inactive
 nao '...'
 show nao_v002 normal at active
 show shannon_v001 smile_close at inactive
 nao '...Um... Shannon-san. This is just between you and I, okay?'
 show shannon_v001 smile at active
 show nao_v002 normal at inactive
 shannon 'Okay...?'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 2.0
 show nao_v002 fuan at active
 show shannon_v001 smile at inactive
 nao "...Jessica-san and them have been terrified of this island's ghost story about a witch."
 show shannon_v001 normal at active
 show nao_v002 fuan at inactive
 shannon "Ghost story... about a witch... you're saying...?"
 hide shannon_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'A bewildered expression. ...Yeah, that reaction is good.'
 narrator 'Everyone has been getting in on saying that the witch Beatrice "exists".'
 narrator "In a normal situation, even I'd be able to read the mood, like how you don't want to indiscriminately deny the existence of Santa Claus."
 narrator '...But I\'m a bit more of the contrary type. As they join in and say Beatrice "exists", I more so get the feeling of wanting to be shown proof.'
 narrator '...Proof? ...This is no joke. I just wanted to relax on this island, so why does it have to come to this?'
 show shannon_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show shannon_v001 smile at inactive
 nao 'As I thought, Shannon-san... believes in her too? In Beatrice.'
 show shannon_v001 smile_close at active
 show nao_v002 normal at inactive
 shannon 'Yes. She "exists", Beatrice-sama.'
 show nao_v002 normal at active
 show shannon_v001 smile_close at inactive
 nao 'When you say exists, where could that be?'
 show shannon_v001 smile at active
 show nao_v002 normal at inactive
 shannon 'Right here, right now, she surely "exists".'
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.wav'
 hide shannon_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "Shannon-san is sweetly laughing with a smile on her face... but I get the feeling that I've soured her mood instead."
 show shannon_v001 smile at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show shannon_v001 smile at inactive
 nao 'If she does exist, I would like for her to impress with her appearance.'
 show nao_v002 normal at active
 show shannon_v001 smile at inactive
 nao "If she shows her form begrudgingly and while putting on airs, she'll make the experience rather uncanny."
 show shannon_v001 normal_close at active
 show nao_v002 normal at inactive
 shannon '... It seems like you are quite poisoned with anti-magic toxin.'
 show nao_v002 odoroki at active
 show shannon_v001 normal_close at inactive
 nao 'Anti-magic... toxin...?'
 show shannon_v001 normal at active
 show nao_v002 odoroki at inactive
 shannon "They say that Humans who don't believe in magic... emit a poisonous gas that is harmful to witches."
 show nao_v002 normal at active
 show shannon_v001 normal at inactive
 nao "So, basically... humans who don't believe in Beatrice will repel her, is what you're saying?"
 show nao_v002 smile at active
 show shannon_v001 normal at inactive
 nao "That's relieving then. She can't appear to people who don't believe in her in the first place."
 hide shannon_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "If she only appears to those who believe, she's no different than Santa Claus. People who don't want to meet her will go on without meeting her..."
 show nao_v002 smile at mei_left
 show shannon_v001 fuan at mei_right
 with Dissolve(0.5)
 show shannon_v001 fuan at active
 show nao_v002 smile at inactive
 shannon "It's... actually the other way around."
 show nao_v002 fuan at active
 show shannon_v001 fuan at inactive
 nao 'Huh...?'
 show shannon_v001 normal_close at active
 show nao_v002 fuan at inactive
 shannon "Beatrice-sama holds grudges towards people who don't believe in her existence."
 show shannon_v001 normal at active
 show nao_v002 fuan at inactive
 shannon "She'll come to you to demonstrate that she really exists, play strange pranks on you, even frighten you..."
 show nao_v002 normal at active
 show shannon_v001 normal at inactive
 nao 'I heard that from Kanon-san. Like how in rooms that no one should be entering, creepy magic circles were found?'
 hide nao_v002
 hide shannon_v001
 with Dissolve(0.2)
 narrator "Shannon-san's face clouded over for a split second. She had this look like I had surprised her by suddenly saying something foolish... and was criticizing me for it."
 show shannon_v001 fuan at mei_center
 with Dissolve(0.5)
 show shannon_v001 fuan at active
 shannon 'Nao-sama... Saying things like that can be very-...'
 play audio 'audio/sfx/SE_5029_slap_back.wav'
 pause 0.5
 play music 'audio/bgm/BGM_HOME_COLLAB2.wav'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide shannon_v001
 hide fade with Dissolve(0.08333333333333333)
 show jessica_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show jessica_v001 smile at active
 jessica 'Good eveniing~~!! Guess who came to mess around~~!!'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide jessica_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator 'In good spirits, Jessica had appeared holding something.'
 narrator 'To Jessica, us coming here to vacation is probably more like friends coming to sleep over.'
 show jessica_v001 smile at mei_right
 show mion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show mion_v002 odoroki at active
 show jessica_v001 smile at inactive
 mion "Whaaat?! Could that little board game you're carrying really be?!"
 show jessica_v001 futeki at active
 show mion_v002 odoroki at inactive
 jessica "I always knew this day would come! After buying this all those years back, it's finally time to play...!"
 hide mion_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show jessica_v001 futeki at inactive
 shion 'Ah, jeez. Bringing a board game in front of Sis like that is a huge deal, you know?'
 hide jessica_v001
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at updown_shake_transform,active
 show erika_v001 normal at inactive
 mion "Let's go! Let's go! Everyone, let's go!! You wanna play with us too, Erika-san?"
 show erika_v001 normal_close at active
 show mion_v002 smile at inactive
 erika 'I do think I will be spending time leisurely in my room.'
 show mion_v002 futeki at active
 show erika_v001 normal_close at inactive
 mion "Whaaat? You're gonna run oooff? Board games are a head-to-head clashing experience!"
 show mion_v002 futeki_close at active
 show erika_v001 normal_close at inactive
 mion "Well, this head of mine isn't too good at winning. You still gonna run off~?"
 show erika_v001 normal at active
 show mion_v002 futeki_close at inactive
 erika '...Hnn. Cheap provocation method. But if you say that much, I must have to take your offer.'
 hide mion_v002
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show erika_v001 normal at inactive
 shion "Are you sure? Sis doesn't take any excuses when she plays games with people, okay?"
 hide erika_v001
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show nao_v002 normal at inactive
 jessica 'Mion-san, you know a lot about board games?'
 show nao_v002 fuan at active
 show jessica_v001 smile at inactive
 nao '...Not even just board games. Mion and competition is to fish and water.'
 play audio 'audio/sfx/SE_226_shine.wav'
 show jessica_v001 futeki at jump_transform,active
 show nao_v002 fuan at inactive
 jessica "Sweet! I'm the grandkid of Kinzo Ushiromiya, so competition is first nature to me!"
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 mion "Let's get everyone to play! Me, Shion, Erika-san and Jessica-san. Nao-chan and Shannon-san can jump in too!"
 show shannon_v001 smile at mei_left
 with Dissolve(0.5)
 show shannon_v001 smile at active
 show mion_v002 smile at inactive
 shannon 'The feeling alone is enough for me. I have yet to do all my chores in the mansion...'
 show shannon_v001 smile_close at active
 show mion_v002 smile at inactive
 shannon "I'll take my leave for today..."
 hide mion_v002
 hide shannon_v001
 with Dissolve(0.2)
 narrator 'Shannon-san went off with a slight bow out of consideration.'
 show mion_v002 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao 'Mion-san. Did you have the conversation with her... about the window lock?'
 show mion_v002 fuan at chara_shake_transform,active
 show nao_v002 normal at inactive
 mion '*gulp*'
 hide nao_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 fuan at inactive
 shion 'Sis. It would be best to apologize outright for something like this, yeah?'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show shannon_v001 normal at mei_left
 with Dissolve(0.5)
 show shannon_v001 normal at active
 shannon 'What conversation did you want to have...?'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shannon_v001 normal at inactive
 erika 'Ah, ... about the window, *giggle*.'
 show erika_v001 normal at active
 show shannon_v001 normal at inactive
 erika 'Though we are on an island separated from the outside world, it is quite unpleasant for a girl to have her room left unlocked, even by window.'
 hide shannon_v001
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show erika_v001 normal at inactive
 jessica "Aah, so you're talking about the window locks? Those are old, so there's a bit of a trick to using them."
 hide erika_v001
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at active
 show jessica_v001 smile at inactive
 mion 'Nahh... I was psyched that we got a really nice room, and while I was opening the window... I kind of used all my force on the lock...'
 hide jessica_v001
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 fuan_close at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan_close at active
 show nao_v002 fuan at inactive
 shion "I'm sorry my sister is such a hick."
 show nao_v002 fuan at active
 show shion_v002 fuan_close at inactive
 nao "I'm really sorry about Mion-san being a hick. ...I do wonder if we can have you look at it?"
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show shannon_v001 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show shannon_v001 smile at inactive
 jessica 'Shannon, go check it out.'
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon 'Certainly...'
 hide shannon_v001
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 mion "Alriiiiight, let's go let's go let's go!! Okay, so this is the type of game where whoever survives 'til the end wins!!"
 hide mion_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show jessica_v001 smile at inactive
 nao 'When Mion-san is playing a game, she has to make sure she has a punishment game set.'
 show jessica_v001 smile at active
 show nao_v002 smile at inactive
 jessica "Wait, what?!?! We're running this with punishment games?! Whenever there's risk involved, the Ushiromiya blood inside me gets fired up!"
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v002 smile at inactive
 erika "I'll be the winner, in any case. At most, do allow me to choose a serious punishment game myself."
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion "Erika-san, you'd best not underestimate Sis, yeah? She'll do anything to win."
 hide shion_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao "...For starters, I'll be glad if we won't be doing ones with explosions, traps, or bodily harm."
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'My, my. In the face of these punishment games, this is going to become quite the thrilling one. *cackle*cackle*cackle*!!'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_center
 with Dissolve(0.5)
 show jessica_v001 odoroki at active
 jessica 'W-, weird. I had no idea this was gonna be a dangerous kind of game...'
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'When Mion-san comes into the picture, anytime playing is involved, it transforms into a much darker game...'
 narrator 'No one wanted to get their pillow wet with tears of humiliation on their first night here. Everyone diligently looked over the rules.'
 play audio 'audio/sfx/SE_526_door_open.wav'
 pause 0.5
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon "I've fixed the lock!"
 hide shannon_v001
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_left
 show mion_v002 odoroki at mei_right
 with Dissolve(0.5)
 show mion_v002 odoroki at active
 show nao_v002 odoroki at inactive
 mion 'Woah! That was real fast! To think you had gone up just now, jeez!'
 show nao_v002 smile at active
 show mion_v002 odoroki at inactive
 nao "Right? But anyways, this is a relief. You've fixed it in quite a flash."
 hide nao_v002
 hide mion_v002
 with Dissolve(0.2)
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon "There's a trick in using it. From tomorrow forward, we would appreciate if you handled it with care."
 hide shannon_v001
 with Dissolve(0.2)
 show mion_v002 fuan at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 fuan at inactive
 shion 'Did you hear that, Sis? Now reflect on your actions.'
 show mion_v002 fuan at chara_shake_transform,active
 show shion_v002 normal at inactive
 mion "Th-, this ol' man wanted to be the strong visitor, so he was surveying it that way! Really!!"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show shannon_v001 smile at mei_left
 with Dissolve(0.5)
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon "Hehe. Okay, now I'll take my leave."
 show jessica_v001 smile at active
 show shannon_v001 smile at inactive
 jessica "Thanks, Shannon! Don't let the adults know that I'm playing over here...!"
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon '*giggle*. I will act under this instruction.'
 hide jessica_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shannon_v001 smile at inactive
 erika 'Nice work, Shannon-san. Has a robber broken into the window or anything?'
 show shannon_v001 smile_close at active
 show erika_v001 normal at inactive
 shannon 'No. Please be at ease.'
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Shannon-san bowed very deeply and returned to the mansion.'
 show mion_v002 smile at mei_right
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at jump_transform,active
 show mion_v002 smile at inactive
 jessica "Alright!! Let's go!!"
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 show jessica_v001 smile at inactive
 mion "Yeah, that's the spirit!! Here are Jessica and I's business trip club activities on Rokkenjimaaaa!!!"
 stop music fadeout 2.0
 window hide None
 hide mion_v002
 hide jessica_v001
 with Dissolve(0.2)
 pause 2.0
 play music 'audio/bgm/BGM_QUEST2_COLLAB2.wav'
 narrator "When you play a board game for the first time, it's often accompanied with taking a while to look over all of the rules."
 show jessica_v001 fuan at mei_center
 with Dissolve(0.5)
 show jessica_v001 fuan at chara_shake_transform,active
 jessica 'Haaaaaaaah... aaaah...'
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'Jessica-san yawned, so it caught Shion-san and I into the yawn chain too.'
 show mion_v002 normal at mei_right
 show erika_v001 sinken at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken at active
 show mion_v002 normal at inactive
 erika 'Wait a second. This one is saying "it\'s okay to do this", right? Isn\'t it also saying "it\'s not okay to do this"?'
 show mion_v002 normal at active
 show erika_v001 sinken at inactive
 mion "Umm, wait, wait. First, we settled we'd go in clockwise to collect taxes, and then processing income was..."
 hide erika_v001
 show shion_v002 sinken at mei_left
 with Dissolve(0.5)
 show shion_v002 sinken at active
 show mion_v002 normal at inactive
 shion 'Sis, before, I was going to be the first to have my income processed, and then we would collect from there, right?'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 fuan at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show jessica_v001 fuan at inactive
 nao '...Yeah, hold on. The game is absolutely falling through.'
 show jessica_v001 fuan_close at active
 show nao_v002 fuan at inactive
 jessica 'Ahhh... hahahh... I wish I brought over a game that we could play quickly... '
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v002 fuan at inactive
 erika 'Oh my. Nao-chama let out a massive yawn.'
 show erika_v001 normal at active
 show shion_v002 fuan at inactive
 erika "It has clearly already reached the point in the night where children shouldn't be up."
 show shion_v002 fuan at active
 show erika_v001 normal at inactive
 shion "The game hasn't reached a result, and we haven't even gotten to enjoy the process. Won't we end it here for today?"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide shion_v002
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 sinken at active
 mion "Aaaah-, come on, come on!! Just as this ol' man charged up all this power, we decide to end it?"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show jessica_v001 smile at mei_right
 show nao_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 show jessica_v001 smile at inactive
 nao "I'm already getting sleepy. ... I want to take a shower and stuff."
 show jessica_v001 smile at active
 show nao_v002 fuan_close at inactive
 jessica 'Welp, I guess that settles it.'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Since Mion-san would have destroyed all of us ingame had it continued past that point, we called it here and went on our ways.'
 narrator 'Besides, having a punishment game enforced on everyone second place and below was too much... Even for a kid from Hinamizawa... that... is a little...'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2371.png' as bg
 with Dissolve(1.0)
 narrator 'Jessica-san returns to the mansion. The rest of us dragged ourselves up to the second floor.'
 show erika_v001 normal at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion "What's the verdict? Did we enjoy ourselves a little with the club activity?"
 show erika_v001 normal_close at active
 show shion_v002 smile at inactive
 erika 'As expected, dice-throwing games relying on luck are not my thing.'
 show erika_v001 normal at active
 show shion_v002 smile at inactive
 erika 'Unlike my master, eternally rolling over and over until you get the number desired is something I can never do.'
 hide erika_v001
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show nao_v002 fuan at inactive
 mion 'Did Nao-chan have fun too?'
 show nao_v002 fuan at active
 show mion_v002 smile at inactive
 nao 'By the time it felt fun, I feel like we could have been laughing carelessly playing Russian roulette with live bullets.'
 show mion_v002 futeki at active
 show nao_v002 fuan at inactive
 mion 'Jessica-san said it herself, I guess, how there is a huge prize hidden underneath the insanity of risk.'
 show mion_v002 smile at updown_shake_transform,active
 show nao_v002 fuan at inactive
 mion "I feel like the head of this place, Kinzo-san, would have enjoyed the madness of this ol' man's club activities."
 hide nao_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 smile at inactive
 shion 'Umm, who has the key?'
 show mion_v002 smile at active
 show shion_v002 normal at inactive
 mion 'I have iiit~. Opening it now~.'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika 'Okay, everyone. Good night.'
 show nao_v002 smile at active
 show erika_v001 normal at inactive
 nao 'Good night, Erika-san.'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika 'Oh, yeah. Nao-chama.'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao "That 'Nao-chama', would you stop calling me that...?"
 stop music fadeout 2.0
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika 'I heard. ...I suppose you had spoken with Shannon-san earlier?'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika "How Beatrice loves playing pranks on people who don't believe, and such... "
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika 'And how you denounced the Golden Witch outright, even with her having that level of magnificence.'
 show erika_v001 fuan at active
 show nao_v002 fuan at inactive
 erika "...I do hope that she doesn't some sort of creepy prank on you because of that...?"
 show nao_v002 normal_close at active
 show erika_v001 fuan at inactive
 nao 'You really are poorly mannered, Erika-san. ... Treating people like children.'
 show nao_v002 normal at active
 show erika_v001 fuan at inactive
 nao "I'm not afraid or anything of that ghost story."
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika '<Good>.'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'Do please keep that determination up for me. *giggle*giggle*giggle*...'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_526_door_open.wav'
 narrator 'Erika-san aimed out a sarcastic laugh at me while disappearing into her room.'
 narrator 'Mion-san, finally remembering which pocket she had left the key in, picked it out and opened the door.'
 show expression "#000" as fade with Dissolve(1.0)
 mion "Who's gonna shower after me?"
 shion 'Nao-san can go after, right?'
 nao "I'd be happy to, but I want to give myself a proper bath."
 play audio 'audio/sfx/SE_5004_lightoff.wav'
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator "There's a light switch inside. Without breaking the Western-style house feel, what illuminated inside was some disorenting proof."
 window hide None
 scene expression "#000" as bg
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2320.png' as bg
 with Dissolve(2.0)
 pause 1.0
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao 'H-......'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 sinken at mei_right
 show shion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show shion_v002 odoroki at jump_transform,active
 show mion_v002 sinken at inactive
 shion 'What happened? .... Heee?!?! S-, Sis...!!'
 show mion_v002 futeki at active
 show shion_v002 odoroki at inactive
 mion "...They've... done it..."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator "This is... a prank... geared towards people who don't acknowledge the witch's existence."
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'W-... what in the hell...'
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 narrator "Mion-san and Shion-san's beds had... nothing on top of them, but just my bed was k i l l e d..."
 narrator 'The blanket was torn off disastrously... almost like the sheets were skin hanging off of it... dyed it with fresh blood.'
 narrator "No. It's not just dyed red. This is... something drawn on with a blood-like substance..."
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'A........  magic circle.........'
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 pause 2.0