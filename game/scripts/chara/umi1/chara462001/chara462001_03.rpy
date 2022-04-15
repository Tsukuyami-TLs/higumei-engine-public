label chara462001_03:
 show black_background onlayer black
 $ event_store.current_event='chara462001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara462001_03'
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
 show expression 'images/bg/AdvBg_262.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_501_crow.wav'
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_782.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST5_COLLAB2.ogg"
 call wipein_routine
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I'm so... tired..."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_161.png' as bg
 camera at sepia_shader
 pause 0.0
 show rika_v002 fuan at mei_right
 show satoko_v002 sinken at mei_left
 with Dissolve(0.5)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v002 sinken at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...I've told you, I'm Rika Furude. I am not your master at all."
 show satoko_v002 sinken at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I don't know you at all."
 show rika_v002 fuan at inactive
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I don't know how much she looks like her, but Rika and your master are completely different people! Different! People!"
 hide satoko_v002
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'From what you say, this master person is a little, as far as I can tell, um...'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...does she know the word "kindness"?'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_782.png' as bg
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 camera at reset_shader
 pause 0.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 show erika_v001 sinken_close at chara_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Uu, if only I had realized it before I made the shrine sparkle, I wouldn't have had to go through such an excess of work...!"
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'And yet, to make matters worse! Now that I say it, that little girl with the unkempt hair!'
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'And her bluntly saying, "Why hadn\'t you realized until it was over?" ...with those pitying eyes!!!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 sinken at active
 show erika_v001 sinken at jump_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It couldn't have been helped! Even if it was one in ten thousand worlds, or a hundred million, no, even a trillion, ten quadrillion, one hundred quintillion!!!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Just like the pebbles in a sandstorm are small, there was a possibility that Rika Furude is my master!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "As if I wouldn't have cleaned that shriiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiine!!!!!!!!!!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 sinken_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Haah, haah, haaah...'
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Hooo...'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'However, as a result of me getting carried away, I accidentally forgot to investigate where my main target is located.'
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'No matter where I go, the mountains, the forest, the paddies, all of this is why I really HATE the countryside!'
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "...*sigh*. I mean really, whose permission did that little girl get to resemble my master so much? The next time I see her, I'm going to interrogate her on it without fail. "
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Hm? The one walking over there is...'
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Hold on, Rika Furude!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") '............?'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'What is that strange and foolish look? You, over there.'
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I forgot to say this earlier, but I am searching for someone.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "She's a super audacious child, and her name is... hm?"
 stop music fadeout 0.5
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") '*giggle*... *giggle*giggle*.'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "What's so funny, Rika Furude?"
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB2.ogg"
 show erika_v001 sinken_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Hm?... Rika Furude? Furude, Rika...\nFu-ru-de, Frede-... hm? Hmm?'
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") "*giggle*giggle*... It's obvious what's so funny."
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") "I couldn't find you, so I went out of my way to take this form and see what you were up to."
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") "Returning evil for good, hm? Isn't that a nice hobby."
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") 'That sort of thing is pretty amusing for you, hm? \nNot bad, yeah, not bad at all... *giggle*giggle*giggle*...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Eh, ah... huh? N-No, it couldn't be...?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") "Do you know the kind of idiot that goes for a picnic in a place with bears? You're exactly the same... *giggle*giggle*."
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") "But isn't it hopeless for you here? You're my piece. Shouldn't you have picked a better opponent to strike at...?"
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show erika_v001 odoroki at chara_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Y-You... n-no... thou...!\nThine highest is...!'
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") "No matter how long I stood there, you wouldn't come back. I wondered what you were doing, killing time just like you happened to be, so I went out of my way to come see you..."
 Character('Furude Rika?',ctc="ctcArrow", ctc_position="fixed") "I saw you doing something strange, so I was enjoying myself at first, but it really was too much. I really don't need something like you... *giggle*giggle*giggle*!!!"
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Ah, aaah, ah... thine highness is my... master...?'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Correct...... *giggle*. \nWell, isn't it game over for you?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Ah, aaah... ah, aaaaAAAAAAAH?!?!!?!??!'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 play music "<loop 0>audio/bgm/BGM_QUEST11_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Mmmm, this is pretty flashy, isn't it?"
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Nonetheless, Erika's thinking power has deteriorated from exhaustion, and she does not have the power to resist on hand."
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'All things considered, she was saved by you... Dlanor.'
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile_close at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'No, it was not anything CONSIDERABLE.'
 show dlanor_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'How modest. If it wasn\'t for you, her "target" would not have been able to escape to our domain to be protected.'
 show dlanor_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'That character will have already forgotten around now, but we had a very fun tea party together.'
 show beatrice_v001 smile at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "When forced into a battle out of the blue, whether it's a position I'm in or a friend's, I am not given permission to do ANYTHING."
 show beatrice_v001 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Thank you for the TEA. The conversation about mysteries was also terribly WORTHWHILE.'
 show dlanor_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Mhm. What's most important is that you are satisfied with spending your time with me."
 show dlanor_v001 normal at inactive
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Either way, is Erika going to be okay? She seems to be taking a great beating.'
 show beatrice_v001 fuan at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "It is ALRIGHT. Although I am unsure, I don't think Erika will be abandoned like THAT."
 show dlanor_v001 normal_close at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*... So you think so too, Dlanor?'
 show beatrice_v001 futeki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'YES. She will surely RETURN.'
 show beatrice_v001 futeki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'And the rematch with "her" as well... there should be rules that are more precisely put into PLACE.'
 show beatrice_v001 futeki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Where that being came from I have no idea, but she has an honest and open-minded approach in regards to mystery, which has given me a good impression of HER.'
 show dlanor_v001 normal at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*, exactly...!'
 show dlanor_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'That being said, what is your reason for being friends with Erika? Do opposites really attract?'
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...However it may turn out does not matter to ME. Now, I believe I will be taking my LEAVE.'
 show dlanor_v001 normal_close at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Are you going out to meet her?'
 show beatrice_v001 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'YES. We will return to this board, one way or ANOTHER.'
 show beatrice_v001 smile at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '............'
 show dlanor_v001 normal_close at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Dlanor? How was your time here?'
 show beatrice_v001 normal at inactive
 show dlanor_v001 smile at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...The cookies were DELICIOUS. May I come AGAIN?'
 show dlanor_v001 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Of course. Next time, it will be nice if we invite Erika.'
 show dlanor_v001 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I will always welcome you two here.'
 show beatrice_v001 smile at inactive
 show dlanor_v001 smile_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...I am thankful, BEATRICE.'
 hide dlanor_v001
 with Dissolve(0.6)
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Hm, I cannot really say that Erika is blessed, but...'
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Either way, it seems she was blessed with a friend.'
 call chapter_end
 
 $ persistent.chara462001_done = True
 return