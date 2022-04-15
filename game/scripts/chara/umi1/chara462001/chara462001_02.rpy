label chara462001_02:
 show black_background onlayer black
 $ event_store.current_event='chara462001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara462001_02'
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
 show expression 'images/bg/AdvBg_204.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST5_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "The fact that I've arrived is nice... but there really is nooothing here, huh?"
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'A desolate and run-down village with nearly no one here. Without the scenery, it would have no redeeming qualities...'
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'It makes me feel like a long time ago a detective with dandruff falling from his head would come here, but as I thought, the times seem to have changed.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "There aren't any locked-room murders or mysterious incidents around here that would stimulate my withering brain cells, huh... *siiigh*."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'But then... I do wonder where in the world Nao-san is?'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Let's try to reason this out... We'll restrict it to a place where kids would be gathering in a desolate countryside like this."
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "School... considering the time, it would be afterschool hours. A park... I don't think this village has one, right? I do suppose it would be difficult to even manage playground equipment without the budget for it."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'With that in mind, the place with the highest possibility to be the substitute for a playground would be... the shrine.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "And if they aren't there, this village is deserted. I don't anticipate the number of kids here to be huge anyway."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "If it comes to it, getting information about where that girl lives and her current location won't be that difficult either--."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Just from one peek at this village, this level of reasoning is possible for Erika Furudo. What do you think, everyone?'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "......If there's no audience, the response really will be just as lacking. I guess it would have been nice if I forced Dlanor to come with me."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Well, whatever. For now, I will find that girl quickly and drag her away.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'The shrine also serves as a shelter for when disasters happen, so it must be at a high altitude. ...Now, shall I go and confirm the result of my reasoning?'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_161.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Ah, I can hear the voices of children. It seems my reasoning hit the nail on the head. ...Well, but of course it would.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Now, let us find out where that girl's location is."
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_1101.png' as bg
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v002 smile at mei_right
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show kazuho_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Okay, Kazuho, Satoko, here's your tea."
 show rika_v002 smile at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Thank you, Rika-chan. ......Wow, it's delicious."
 show kazuho_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I should be the one thanking you. Kazuho went out in my place and saved the day by buying these tea leaves for us.'
 show rika_v002 smile at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'This kind of errand was easy for me... but the contractor they asked to clean the shrine is pretty slow, huh?'
 show kazuho_v002 smile at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. I thought it'd be bad if I wasn't here when he came, so I had Kazuho run that errand..."
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'It turns out that I could have finished that, {i}and{/i} went shopping, {i}and{/i} I still would have made it completely on time.'
 show satoko_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Yeahh, I think that first job you mentioned is being dragged out.'
 show kazuho_v002 fuan at inactive
 show satoko_v002 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It might be that way, but even if we call and complain, I don't think scolding would do much..."
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show satoko_v002 normal at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'But Rika, why did you entrust Kazuho-san with that errand?'
 show satoko_v002 normal at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Whenever I run into trouble with having no tea, I occasionally call Kazuho, like I did this time.'
 hide satoko_v002
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Yep. Earlier, Rika-chan gave me an apple and Miyuki-chan made me a compote, or some snack like that, so I thought it would be nice to share all of this stuff with everyone.'
 show rika_v002 smile at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'With all of this stuff in hand already, I took the opportunity to get some tea leaves as well.'
 show kazuho_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Compotes are so delicious when they're chilled. Let's enjoy it for dessert tonight!"
 hide rika_v002
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'My, that would be fun. ...But where is Miyuki-san?'
 show satoko_v002 smile at inactive
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Even now, she's attentively sitting in front of the pan making compote. The whole inside of our house is full of sweet scents..."
 show kazuho_v002 fuan_close at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Hanyuu-san is taking a nap at home right now, isn't she? If she were to hear this conversation, she would be breaking into a sprint running towards Miyuki-san's house~."
 show satoko_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Y-Yep. If it was Hanyuu-chan, I think she would love those smells... but for me, it's so sickeningly sweet it gives me a headache."
 hide satoko_v002
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. You tend to be picky with smells.'
 hide kazuho_v002
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'It seems like Nao-chan is okay with it, though. Napping soundly right in the midst of all those smells... huh?'
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'That person there under the shrine gate... \nIs that the contractor?'
 hide kazuho_v002
 with Dissolve(0.2)
 show satoko_v002 odoroki at mei_left
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Huh? But I can't see someone cleaning in those clothes..."
 show satoko_v002 odoroki at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep... She's wearing something like a dress."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide satoko_v002
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Ah, ah, ah, aaaaaaaahhhhhhhhhhhhhhhhh...!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'What?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'AAAHHHHHHH---!'
 play audio 'audio/sfx/SE_408_run.wav'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "S-She's dashing over here at full force?!"
 hide kazuho_v002
 with Dissolve(0.2)
 show satoko_v002 odoroki at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show satoko_v002 odoroki at active
 show satoko_v002 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ri-Rikaa! Is she someone you know?!'
 show satoko_v002 odoroki at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I-I don't know her!"
 hide satoko_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'But that person is sprinting over here like a missile...?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide kazuho_v002
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_224_sliding.wav'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'MYYYYY MAAASTERRRRRRRRRRRRRRRRRRR!!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 show rika_v002 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Me...ep?!'
 hide rika_v002
 with Dissolve(0.2)
 show satoko_v002 odoroki at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show satoko_v002 odoroki at active
 show satoko_v002 odoroki at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Whaaaaaaaaa? This stranger just dropped down by Rika's feet and slid into a kneeling position?!"
 show satoko_v002 odoroki at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wow, such an artistic form...!'
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show erika_v001 odoroki at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'W-w-w-w-why would my master ever be in a run-down place like this?!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show rika_v002 fuan at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Ah...!? Have you perhaps gone out of your way to investigate what I've been doing here...?!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show rika_v002 fuan at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Th-thank you so much! For not having reasoned out an expectation of your arrival, I so deeply apologize!!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 smile at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'U-Um...'
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show rika_v002 fuan at inactive
 show erika_v001 smile at active
 show erika_v001 smile at jump_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Yes, what is it?!'
 show erika_v001 smile at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Wh-who are you?'
 show rika_v002 fuan at inactive
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'What? ...You are my master, right?'
 show erika_v001 odoroki at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Not at all.'
 show rika_v002 normal at inactive
 show erika_v001 odoroki at active
 show erika_v001 odoroki at chara_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Huh?! N-No, that sort of joke is...'
 hide rika_v002
 hide erika_v001
 with Dissolve(0.2)
 show kazuho_v002 normal at mei_left
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Hey, Rika-chan. Maybe this... isn't... the cleaner they hired?"
 show kazuho_v002 normal at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'She\'s saying "my master" and stuff too?'
 show satoko_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Uhh... so, is it like that kind of service?'
 show satoko_v002 fuan at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "L-Look! Doesn't she look just like a waitress from Angel Mort wearing that cute uniform, dealing with customers by calling them master? ...She does, right?!"
 show kazuho_v002 sinken at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Kazuho-san... are you seriously saying that?'
 show satoko_v002 fuan at inactive
 show kazuho_v002 fuan_close at active
 show kazuho_v002 fuan_close:
  yanchor 1.0
  linear 0.5 pos (480,1250)
 pause 0.5
 show kazuho_v002 fuan_close:
  yanchor 1.0
  pos (480,1250)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...I'm sorry. I said it myself, but I didn't really believe it all too much... Uuu."
 show kazuho_v002 fuan_close
 show kazuho_v002 fuan_close:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 pause 0.5
 show kazuho_v002 fuan_close:
  yanchor 1.0
  pos (480,1200)
 show satoko_v002 fuan at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'B-But I think we should check it out again to make sure!'
 hide satoko_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show erika_v001 smile at mei_left
 with Dissolve(0.5)
 show erika_v001 smile at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. I also think it's a little different, but Kazuho was right in saying that..."
 show erika_v001 smile at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Um... are you maybe the cleaner that Kiichirou requested?'
 show rika_v002 normal at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Cleaner?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide rika_v002
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '......AH?!'
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I see, so it's like that? This is also one of my master's time killing games. No, this is mercy!"
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'This is basically revenge for me displeasing her, so if I clean up this timeworn shrine, my master will change her perception of me out of thoughtfulness!!'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "So basically! This means it's a bonus stage?!?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show satoko_v002 fuan at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Whatever you're talking about, I don't get it at all."
 show satoko_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I-I don't get it either..."
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show erika_v001 smile at mei_left
 with Dissolve(0.5)
 show erika_v001 smile at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep...'
 show rika_v002 fuan at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I do humbly apologize for the trouble! So, from here on out, Erika Furudo shall demonstrate to you her magnificent cleaning powers!'
 show rika_v002 fuan at inactive
 show erika_v001 smile at active
 show erika_v001 smile at jump_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Now, where are the cleaning tools?'
 show erika_v001 smile at inactive
 show rika_v002 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. I certainly thought the contractor guy would have specialized cleaning tools with him...'
 hide erika_v001
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan_close at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Or at least, something...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide satoko_v002
 hide fade onlayer curtain
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Ah! *giggle*... *giggle*giggle*, I see. I get it now.'
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "So, what you're saying is you want me to clean it all up with my tongue! \nI shall get to it expeditiously, my master!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 sinken at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show rika_v002 fuan at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "That's... I don't think that's right!"
 show kazuho_v002 sinken at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...I think that's actually dirtier."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide kazuho_v002
 hide fade onlayer curtain
 show satoko_v002 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v002 fuan at active
 show satoko_v002 fuan at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I-I'll bring out some cleaning tools right now! Please do not be so hasty! PLEASEEEE!"
 call chapter_end
 jump chara462001_03