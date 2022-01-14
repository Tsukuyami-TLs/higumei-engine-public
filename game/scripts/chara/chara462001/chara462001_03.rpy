label chara462001_03:
 show black_background onlayer black
 $ event_store.current_event='chara462001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara462001_03'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_262.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_501_crow.wav'
 pause 1.0
 call wipeout_routine from _call_wipeout_routine_6
 stop sound
 show expression 'images/bg/AdvBg_782.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST5_COLLAB2.ogg"
 call wipein_routine from _call_wipein_routine_6
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 erika "I'm so... tired..."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_161.png' as bg
 camera at sepia_shader
 pause 0.0
 show satoko_v002 sinken at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v002 fuan at active
 show satoko_v002 sinken at inactive
 rika "...I've told you, I'm Rika Furude. I am not your master at all."
 show rika_v002 fuan at active
 show satoko_v002 sinken at inactive
 rika "I don't know you at all."
 show satoko_v002 sinken at active
 show rika_v002 fuan at inactive
 satoko "I don't know how much she looks like her, but Rika and your master are completely different people! Different! People!"
 hide satoko_v002
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 kazuho 'From what you say, this master person is a little, as far as I can tell, um...'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show kazuho_v002 fuan at active
 kazuho '...does she know the word "kindness"?'
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
 show erika_v001 sinken_close at chara_shake_transform,active
 erika "Uu, if only I had realized it before I made the shrine sparkle, I wouldn't have had to go through such an excess of work...!"
 show erika_v001 sinken at active
 erika 'And yet, to make matters worse! Now that I say it, that little girl with the unkempt hair!'
 show erika_v001 sinken at active
 erika 'And her bluntly saying, "Why hadn\'t you realized until it was over?" ...with those pitying eyes!!!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 sinken at jump_transform,active
 erika "It couldn't have been helped! Even if it was one in ten thousand worlds, or a hundred million, no, even a trillion, ten quadrillion, one hundred quintillion!!!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show erika_v001 sinken at active
 erika 'Just like the pebbles in a sandstorm are small, there was a possibility that Rika Furude is my master!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 sinken at active
 erika "As if I wouldn't have cleaned that shriiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiine!!!!!!!!!!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 sinken_close at active
 erika 'Haah, haah, haaah...'
 show erika_v001 normal_close at active
 erika 'Hooo...'
 show erika_v001 normal at active
 erika 'However, as a result of me getting carried away, I accidentally forgot to investigate where my main target is located.'
 show erika_v001 sinken at active
 erika 'No matter where I go, the mountains, the forest, the paddies, all of this is why I really HATE the countryside!'
 show erika_v001 normal_close at active
 erika "...*sigh*. I mean really, whose permission did that little girl get to resemble my master so much? The next time I see her, I'm going to interrogate her on it without fail. "
 show erika_v001 normal at active
 erika 'Hm? The one walking over there is...'
 hide erika_v001
 with Dissolve(0.2)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
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
 erika 'Hold on, Rika Furude!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............?'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 erika 'What is that strange and foolish look? You, over there.'
 show erika_v001 normal_close at active
 erika 'I forgot to say this earlier, but I am searching for someone.'
 show erika_v001 normal at active
 erika "She's a super audacious child, and her name is... hm?"
 stop music fadeout 0.5
 hide erika_v001
 with Dissolve(0.2)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '*giggle*... *giggle*giggle*.'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 erika "What's so funny, Rika Furude?"
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB2.ogg"
 show erika_v001 sinken_close at active
 erika 'Hm?... Rika Furude? Fu-ru-de... hm? Hmm?'
 hide erika_v001
 with Dissolve(0.2)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "*giggle*giggle*... It's obvious what's so funny."
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I couldn't find you, so I went out of my way to take this form and see what you were up to."
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Returning evil for good, hm? Isn't that a nice hobby."
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'That sort of thing is pretty amusing for you, hm? Not bad, yeah, not bad at all... *giggle*giggle*giggle*...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 erika "Eh, ah... huh? N-No, it couldn't be...?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Do you know the kind of idiot that goes for a picnic in a place with bears? You're exactly the same... *giggle*giggle*."
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But isn't it hopeless for you here? You're my piece. Shouldn't you have picked a better opponent to strike at...?"
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at chara_shake_transform,active
 erika 'Y-You... n-no... thou, thine highest is...!'
 hide erika_v001
 with Dissolve(0.2)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "No matter how long I stood there, you wouldn't come back. I wondered what you were doing, killing time just like you happened to be, so I went out of my way to come see you..."
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I saw you doing something strange, so I was enjoying myself at first, but it really was too much. I really don't need something like you... *giggle*giggle*giggle*!!!"
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 odoroki at active
 erika 'Ah, aaah, ah... thine highness is my... master...?'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Correct...... *giggle*. Well, isn't it game over for you?"
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
 erika 'Ah, aaah... ah, aaaaAAAAAAAH?!?!!?!??!'
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
 beatrice "Mmmm, this is pretty flashy, isn't it?"
 show beatrice_v001 smile at active
 beatrice "Nonetheless, Erika's thinking power has deteriorated from exhaustion, and she does not have the power to resist on hand."
 show beatrice_v001 smile_close at active
 beatrice 'All things considered, she was saved by you... Dlanor.'
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show beatrice_v001 smile_close at inactive
 dlanor 'No, it was not anything CONSIDERABLE.'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'How modest. If it weren\'t for you, her "target" would not have been able to escape to our domain to be protected.'
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice 'That character will have already forgotten around now, but we had a very fun tea party together.'
 show dlanor_v001 normal_close at active
 show beatrice_v001 smile at inactive
 dlanor "When forced into a battle out of the blue, whether it's a position I'm in or a friend's, I am not given permission to do ANYTHING."
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor '...Thank you for the TEA. The conversation about mysteries was also terribly WORTHWHILE.'
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice "Mhm. What's most important is that you are satisfied with spending your time with me."
 show beatrice_v001 fuan at active
 show dlanor_v001 normal at inactive
 beatrice 'Either way, is Erika going to be okay? She seems to be taking a great beating.'
 show dlanor_v001 normal_close at active
 show beatrice_v001 fuan at inactive
 dlanor "It is ALRIGHT. Although I am unsure, I don't think Erika will be abandoned like THAT."
 show beatrice_v001 futeki at active
 show dlanor_v001 normal_close at inactive
 beatrice '*cackle*cackle*... So you think so too, Dlanor?'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'YES. She will surely RETURN.'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'And the rematch with "her" as well... there should be rules that are more precisely put into PLACE.'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'Where that being came from I have no idea, but she has an honest and open-minded approach in regards to mystery, which has given me a good impression of HER.'
 show beatrice_v001 futeki at active
 show dlanor_v001 normal at inactive
 beatrice '*cackle*cackle*, exactly...!'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'That being said, what is your reason for being friends with Erika? Do opposites really attract?'
 show dlanor_v001 normal_close at active
 show beatrice_v001 normal at inactive
 dlanor '...However it may turn out does not matter to ME. Now, I believe I will be taking my LEAVE.'
 show beatrice_v001 smile at active
 show dlanor_v001 normal_close at inactive
 beatrice 'Are you going out to meet her?'
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'YES. We will return to this board, one way or ANOTHER.'
 show dlanor_v001 normal_close at active
 show beatrice_v001 smile at inactive
 dlanor '............'
 show beatrice_v001 normal at active
 show dlanor_v001 normal_close at inactive
 beatrice 'Dlanor? How was your time here?'
 show dlanor_v001 smile at active
 show beatrice_v001 normal at inactive
 dlanor '...The cookies were DELICIOUS. May I come AGAIN?'
 show beatrice_v001 smile at active
 show dlanor_v001 smile at inactive
 beatrice 'Of course. Next time, it will be nice if we invite Erika.'
 show beatrice_v001 smile at active
 show dlanor_v001 smile at inactive
 beatrice 'I will always welcome you two here.'
 show dlanor_v001 smile_close at active
 show beatrice_v001 smile at inactive
 dlanor '...I am thankful, BEATRICE.'
 hide dlanor_v001
 with Dissolve(0.6)
 show beatrice_v001 smile_close at active
 beatrice 'Hm, I cannot really say that Erika is blessed, but...'
 show beatrice_v001 smile at active
 beatrice 'Either way, it seems she was blessed with a friend.'
 call chapter_end from _call_chapter_end_11
 return