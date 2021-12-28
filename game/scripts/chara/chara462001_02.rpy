label chara462001_02:
 show black_background onlayer black
 $ event_store.current_event='chara462001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara462001_02'
 stop sound
 scene #000
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_204.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "The fact that I've arrived is nice... but there really is nooothing here, huh?"
 show erika_v001 normal at active
 erika 'A desolate and run-down village with nearly no one here. Without the scenery, it would have no redeeming qualities...'
 show erika_v001 normal_close at active
 erika 'It makes me feel like a long time ago a detective with dandruff falling from his head would come here, but as I thought, the times seem to have changed.'
 show erika_v001 normal at active
 erika "There aren't any locked-room murders or mysterious incidents around here that would stimulate my withering brain cells, huh... *siiigh*."
 show erika_v001 normal at active
 erika 'But then... I do wonder where in the world Nao-san is?'
 show erika_v001 normal at active
 erika "Let's try to reason this out... We'll restrict it to a place where kids would be gathering in a desolate countryside like this."
 show erika_v001 normal_close at active
 erika "School... considering the time, it would be afterschool hours. A park... I don't think this village has one, right? I do suppose it would be difficult even to manage playground equipment without having a budget."
 show erika_v001 normal at active
 erika 'With that in mind, the place with the highest possibility would be the substitute for a playground... the shrine.'
 show erika_v001 normal at active
 erika "And if they aren't there, this village is deserted. I don't anticipate the number of kids here to be huge anyway."
 show erika_v001 normal at active
 erika "If it comes to that, getting information about where that girl lives and her current location won't be that difficult either--."
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 smile at active
 erika 'Just from one peek at this village, this level of reasoning is possible for Erika Furudo. What do you think, everyone?'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 normal_close at active
 erika "......If there's no audience, the response really will be just as lacking. I guess it would have been nice if I forced Dlanor to come with me."
 show erika_v001 normal at active
 erika 'Well, whatever. For now, I will find that girl quickly and drag her away.'
 show erika_v001 normal at active
 erika 'The shrine also serves as a shelter for when disasters happen, so it must be at a high altitude... Now, shall I go and confirm the result of my reasoning?'
 window hide None
 show black_cover as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_161.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Ah, I can hear the voices of children. It seems somehow my reasoning hit the nail on the head... Well, but of course it would.'
 show erika_v001 normal at active
 erika "Now, let us find out where that girl's location is."
 stop music fadeout 0.5
 window hide None
 show black_cover as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene black_cover
 play music 'audio/bgm/BGM_HOME_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_1101.png' as bg
 with Dissolve(1.0)
 show kazuho_v002 smile at mei_left
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at active
 show kazuho_v002 smile at inactive
 rika "Okay, Kazuho, Satoko, here's your tea."
 show kazuho_v002 smile at active
 show rika_v002 smile at inactive
 kazuho "Thank you, Rika-chan. ...Wah, it's delicious."
 show rika_v002 smile at active
 show kazuho_v002 smile at inactive
 rika '"Thank you" is my line here. Instead of me going, Kazuho went out and bought these tea leaves for us, saving the day.'
 show kazuho_v002 smile at active
 show rika_v002 smile at inactive
 kazuho 'This kind of errand was easy for me... but the contractor they asked to clean the shrine is pretty slow, huh?'
 show rika_v002 fuan at active
 show kazuho_v002 smile at inactive
 rika 'Meep. He should already be here, so I thought his absence would be bad, and then I had Kazuho run that errand, but...'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show kazuho_v002 smile at inactive
 satoko 'If it comes to it, I could finish that task plus go shopping and I would still completely make it on time.'
 show kazuho_v002 fuan at active
 show satoko_v002 fuan at inactive
 kazuho 'Yeahh, I think the former job is being dragged out.'
 show satoko_v002 fuan_close at active
 show kazuho_v002 fuan at inactive
 satoko "It might be like that, but in that case, even if we call and complain once, I don't think scolding would do much..."
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show satoko_v002 normal at mei_left
 with Dissolve(0.5)
 show satoko_v002 normal at active
 show rika_v002 fuan at inactive
 satoko 'But Rika, why did you entrust Kazuho with that task?'
 show rika_v002 smile at active
 show satoko_v002 normal at inactive
 rika 'Meep. Whenever I run into trouble with having no tea, I occasionally call Kazuho, like I did this time.'
 hide satoko_v002
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 show rika_v002 smile at inactive
 kazuho 'Yep. Earlier, Rika gave me an apple and Miyuki made me a compote, or some snack like that, so I thought it would be nice to share all of this stuff with everyone.'
 show kazuho_v002 smile at active
 show rika_v002 smile at inactive
 kazuho 'With all of this stuff in hand, I took that opportunity to get tea leaves.'
 show rika_v002 smile at active
 show kazuho_v002 smile at inactive
 rika "Compotes are so delicious when they're chilled. Let's enjoy it for dessert tonight!"
 hide rika_v002
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at active
 show kazuho_v002 smile at inactive
 satoko 'My, that would be fun. ...But where is Miyuki-san?'
 show kazuho_v002 fuan_close at active
 show satoko_v002 smile at inactive
 kazuho "Even now, she's attentively sitting in front of the pan making the compote. The whole inside of her house is full of sweet scents..."
 show satoko_v002 fuan at active
 show kazuho_v002 fuan_close at inactive
 satoko "Hanyuu-san is taking a nap at home right now, isn't she? If she were to hear this conversation, she would be breaking into a sprint running to Miyuki's house~."
 show kazuho_v002 fuan at active
 show satoko_v002 fuan at inactive
 kazuho "Y-yep. If it was Hanyuu-chan, I think she would love those smells... but for me, it's so sickeningly sweet it gives me a headache."
 hide satoko_v002
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at active
 show kazuho_v002 fuan at inactive
 rika 'Meep. You tend to be picky with smells.'
 hide kazuho_v002
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 kazuho 'It seems like Nao-chan is okay with it, though. Napping soundly right in the midst of that smell... huh?'
 show kazuho_v002 normal at active
 kazuho "That person there under the torii... isn't that the contractor?"
 hide kazuho_v002
 with Dissolve(0.2)
 show rika_v002 normal at mei_right
 show satoko_v002 odoroki at mei_left
 with Dissolve(0.5)
 show satoko_v002 odoroki at active
 show rika_v002 normal at inactive
 satoko "Huh? But I can't see someone cleaning in those clothes though..."
 show rika_v002 normal at active
 show satoko_v002 odoroki at inactive
 rika 'Meep... She has on like a dress or something.'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide satoko_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'Ah, ah, ah, aaaaaaaahhhhhhhhhhhhhhhhh...!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show rika_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 rika 'What?!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'AAAHHHHHHH---!'
 play audio 'audio/sfx/SE_408_run.wav'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at chara_shake_transform,active
 kazuho "S-She's dashing over here at full force?!"
 hide kazuho_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show satoko_v002 odoroki at mei_left
 with Dissolve(0.5)
 show satoko_v002 odoroki at jump_transform,active
 show rika_v002 fuan at inactive
 satoko "Ri, Rikaa! Isn't she someone you know?!"
 show rika_v002 fuan at active
 show satoko_v002 odoroki at inactive
 rika "I-I don't know her!"
 hide satoko_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show rika_v002 fuan at inactive
 kazuho 'But that person is sprinting over here like a missile...?!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide kazuho_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_224_sliding.wav'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'MYYYYY MAAASTERRRRRRRRRRRRRRRRRRR!!!!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show rika_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v002 odoroki at jump_transform,active
 rika 'Me...ep?!'
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_left
 show satoko_v002 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v002 odoroki at chara_shake_transform,active
 show kazuho_v002 fuan at inactive
 satoko "Whaaaaaaaaa? This stranger just dropped down by Rika's feet and slid into a kneeling position?!"
 show kazuho_v002 fuan at active
 show satoko_v002 odoroki at inactive
 kazuho 'Wow, such an artistic form...!'
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show erika_v001 odoroki at mei_left
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show rika_v002 fuan at inactive
 erika 'W-w-w-w-why would my master ever be in a run-down place like this?!'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 sinken at active
 show rika_v002 fuan at inactive
 erika 'Ah...!? Had you perhaps went out of your way to investigate what I had been doing here...?!'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show erika_v001 smile at active
 show rika_v002 fuan at inactive
 erika 'Th-thank you so much! For not having reasoned out an expectation of your arrival, I so deeply apologize!!'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show rika_v002 fuan at active
 show erika_v001 smile at inactive
 rika 'U-um...'
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show erika_v001 smile at jump_transform,active
 show rika_v002 fuan at inactive
 erika 'Yes, what is it?!'
 show rika_v002 fuan at active
 show erika_v001 smile at inactive
 rika 'Wh-who are you?'
 show erika_v001 odoroki at active
 show rika_v002 fuan at inactive
 erika 'What? ...You are my master, right?'
 show rika_v002 normal at active
 show erika_v001 odoroki at inactive
 rika 'Not at all.'
 show erika_v001 odoroki at chara_shake_transform,active
 show rika_v002 normal at inactive
 erika 'Huh?! N-no, that sort of joke is...'
 hide rika_v002
 hide erika_v001
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_right
 show kazuho_v002 normal at mei_left
 with Dissolve(0.5)
 show kazuho_v002 normal at active
 show satoko_v002 fuan at inactive
 kazuho "Hey, Rika-chan. Maybe this person... isn't... the cleaner guy?"
 show satoko_v002 fuan at active
 show kazuho_v002 normal at inactive
 satoko 'She\'s saying "my master" and stuff too?'
 show kazuho_v002 fuan at active
 show satoko_v002 fuan at inactive
 kazuho "Uhh... it's, it's that kind of service?"
 show kazuho_v002 sinken at active
 show satoko_v002 fuan at inactive
 kazuho "Lo-look! Doesn't she look like a waitress from Angel Mort wearing that cute uniform, dealing with customers by calling them master? ...She does, right?!"
 show satoko_v002 fuan at active
 show kazuho_v002 sinken at inactive
 satoko 'Kazuho-san... are you seriously saying that?'
 show kazuho_v002 fuan_close at active
 show kazuho_v002 fuan_close:
  linear 0.5 pos (480,1250)
 show satoko_v002 fuan at inactive
 pause 0.5
 kazuho "... I'm sorry. I was talking to myself, but I didn't have that much confidence in that... Uuu."
 show kazuho_v002 fuan_close
 show kazuho_v002 fuan_close:
  linear 0.5 pos (480,1200)
 pause 0.5
 show kazuho_v002 sinken at active
 show satoko_v002 fuan at inactive
 kazuho 'Bu-but, I think it would be a good idea to properly check again!'
 hide satoko_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at active
 show erika_v001 smile at inactive
 rika "Meep. I also think it's a little different, but Kazuho was right in saying that..."
 show rika_v002 normal at active
 show erika_v001 smile at inactive
 rika 'Um... are you maybe the cleaner person that Kiichirou requested for?'
 show erika_v001 sinken at active
 show rika_v002 normal at inactive
 erika 'Cleaner person?'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide rika_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 erika '...Huh?!'
 show erika_v001 smile at active
 erika "I see, it's like that? This is also one of my master's time killing games. No, this is mercy!"
 show erika_v001 smile at active
 erika 'This is basically revenge for me displeasing her, so if I clean up this timeworn shrine, my master will change her perception of me out of thoughtfulness!!'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 erika "So basically! In this meaning, it's a bonus stage?!?!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show kazuho_v002 fuan at mei_left
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show kazuho_v002 fuan at inactive
 satoko "...Whatever you're talking about, I don't get it at all."
 show kazuho_v002 fuan at active
 show satoko_v002 fuan at inactive
 kazuho "I-I don't get it either..."
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at active
 show erika_v001 smile at inactive
 rika 'Meep...'
 show erika_v001 smile at active
 show rika_v002 fuan at inactive
 erika 'I do humbly apologize for the trouble! So, from here on out, Erika Furudo shall demonstrate to you her magnificent cleaning powers!'
 show erika_v001 smile at jump_transform,active
 show rika_v002 fuan at inactive
 erika 'Now, where are the cleaning tools?'
 show rika_v002 fuan_close at active
 show erika_v001 smile at inactive
 rika 'Meep. I certainly thought the contractor guy would have specialized cleaning tools with him...'
 hide erika_v001
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show rika_v002 fuan_close at inactive
 satoko 'And especially not nothing...'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide satoko_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at active
 erika '...Hah! *giggle*, *giggle*giggle*, I see. I get it now.'
 show erika_v001 smile at active
 erika "So, what you're saying is you literally want me to clean it all up with my tongue! I shall get to it expeditiously, my master!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show rika_v002 fuan at mei_right
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show kazuho_v002 sinken at active
 show rika_v002 fuan at inactive
 kazuho "That's... I don't think that's right."
 show rika_v002 fuan at active
 show kazuho_v002 sinken at inactive
 rika "...I think that's actually more dirty."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide kazuho_v002
 hide fade with Dissolve(0.08333333333333333)
 show satoko_v002 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v002 fuan at chara_shake_transform,active
 satoko "I-I'll bring out some cleaning tools right now! Please do not be so hasty! PLEASEEEE!"
 call chapter_end
 jump chara462001_03