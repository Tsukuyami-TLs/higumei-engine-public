label chara462001_03:
 show black_background onlayer black
 $ event_store.current_event='chara462001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara462001_03'
 stop sound
 scene #000
 show expression 'images/bg/AdvBg_262.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_501_crow.wav'
 pause 1.0
 call wipeout_routine
 stop sound
 scene #000
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_782.png' as bg
 call wipein_routine
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 erika "I'm so... tired..."
 window hide None
 show black_cover as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene black_cover
 camera at sepia_shader
 pause 0.0
 show expression 'images/bg/AdvBg_161.png' as bg
 show satoko_v002 sinken at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(1.0)
 show rika_v002 fuan at active
 show satoko_v002 sinken at inactive
 rika "...I've told you, I'm Rika Furude. I am not your master at all."
 show rika_v002 fuan at active
 show satoko_v002 sinken at inactive
 rika 'I do not know you at all.'
 show satoko_v002 sinken at active
 show rika_v002 fuan at inactive
 satoko "I don't know to what extent she looks similar to her, but Rika and your master are completely different people! Different! People!"
 hide satoko_v002
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 kazuho 'Unlike how you say, this master person is a little, as far as I can tell, um...'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show kazuho_v002 fuan at active
 kazuho '...does she know the word "kindness"?'
 window hide None
 show black_cover as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 stop sound
 scene black_cover
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 camera at reset_shader
 pause 0.0
 show expression 'images/bg/AdvBg_782.png' as bg
 with Dissolve(1.0)
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken_close at chara_shake_transform,active
 erika 'Uu, until she recognizes that this shrine is shining, this excess of work will never have been worth it, though...!'
 show erika_v001 sinken at active
 erika 'And yet, to make matters worse! Now that you say it, that little girl with the unkempt hair!'
 show erika_v001 sinken at active
 erika 'And her spitting out, "Why hadn\'t you realized until it was over?" ...with those pitying eyes!!!'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 sinken at jump_transform,active
 erika "Because it couldn't have been helped! Not even in ten thousand worlds, nor a hundred million, no, even a trillion, ten quadrillion, one hundred quintillion!!!"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show erika_v001 sinken at active
 erika 'Just like the pebbles in a sandstorm are small, there is a possibility that Rika Furude is my master!'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 sinken at active
 erika "As if I couldn't be cleaning this shrine right nooooooooooooowwwwww!!!!!!!!!!"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 sinken_close at active
 erika 'Hah, hah, hah...'
 show erika_v001 normal_close at active
 erika 'Hooo...'
 show erika_v001 normal at active
 erika 'However, as a result of me getting carried away, I accidentally forgot to hear about where my main target is located.'
 show erika_v001 sinken at active
 erika 'No matter where I go, the mountains, the forest, the paddies, all of this is why I really HATE the countryside!'
 show erika_v001 normal_close at active
 erika "...*sigh*. I mean really, whose permission did that little girl get to resemble my master so much? The next time I see her, I'm going to interrogate her on it without fail. "
 show erika_v001 normal at active
 erika 'Hm? The one walking over there is...'
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") '............'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 sinken at active
 erika 'Hold on, Rika Furude!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") '............?'
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
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") '*giggle*... *giggle*giggle*.'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 erika "What's so funny, Rika Furude?"
 play music 'audio/bgm/BGM_QUEST1_COLLAB2.ogg'
 show erika_v001 sinken_close at active
 erika 'Hm? ... Rika Furude? Fu-ru-de... hm? Hmm?'
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") "*giggle*giggle*... It's obvious what's so funny."
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") "I couldn't find you, so I went out of my way to take this form and see what you were up to."
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") "Repaying evil for good, hm? Isn't that a nice hobby."
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") 'That sort of thing is pretty amusing for you, hm? Not bad, yeah, not bad at all... *giggle*giggle*giggle*...'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 erika "Eh, ah... huh? No, it couldn't be...?!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") "Do you know the type of idiot that would picnic out at a place where bears could come out? You're exactly the same... *giggle*giggle*."
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") "But isn't it hopeless for you here? You're my piece. Shouldn't you have picked a better opponent to strike at...?"
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at chara_shake_transform,active
 erika 'Y-you... n-no... thou, thine highest is...!'
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") "No matter how long I stood there, you wouldn't come back. I wondered what you were doing, killing time just like you happened to be, so I went out of my way to come see you..."
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") "I saw you doing something strange, so I was enjoying myself at first, but it really was too much. I really don't need something like you... *giggle*giggle*giggle*!!!"
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 odoroki at active
 erika 'Ah, aaah, ah... thine highness is my... master...?'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Correct......... *giggle*. Well, isn't it game over for you?"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show erika_v001 odoroki at active
 erika 'Ah, aaah... ah, aaaaAAAAAAAH?!?!!?!??!'
 stop music fadeout 0.5
 window hide None
 show black_cover as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene black_cover
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 play music 'audio/bgm/BGM_QUEST11_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 beatrice "Mhm, this is pretty flashy, isn't it?"
 show beatrice_v001 smile at active
 beatrice "Nonetheless, Erika's thinking power has deteriorated from exhaustion, and does not have the power to resist on hand."
 show beatrice_v001 smile_close at active
 beatrice 'All things considered, she was saved by you... Dlanor.'
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show beatrice_v001 smile_close at inactive
 dlanor 'No, it was not anything CONSIDERABLE.'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'How modest. If you hadn\'t gotten involved, her "goal" would have been forestalled as she escaped to my domain, and she wouldn\'t have been able to be protected.'
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice "I've been forgetting who that character is lately, but we had a very fun tea party together."
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
 beatrice 'Either way, is Erika going to be okay? She seems to be taking a great beating though.'
 show dlanor_v001 normal_close at active
 show beatrice_v001 fuan at inactive
 dlanor 'It is ALRIGHT. I dare say in that scenario, Erika could not be ABANDONED.'
 show beatrice_v001 futeki at active
 show dlanor_v001 normal_close at inactive
 beatrice '*cackle*cackle*... So you think so too, Dlanor?'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'YES. She will surely RETURN.'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'And the rematch with "her" as well... there should be rules that are more precisely put in to PLACE.'
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
 dlanor '...What becomes of it does not matter to ME. Now, I believe I will be taking my LEAVE.'
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
 dlanor '...The cookies were DELICIOUS. Can I come AGAIN?'
 show beatrice_v001 smile at active
 show dlanor_v001 smile at inactive
 beatrice 'Of course. Next time, it will be nice if we invite Erika.'
 show beatrice_v001 smile at active
 show dlanor_v001 smile at inactive
 beatrice 'I will always welcome you here.'
 show dlanor_v001 smile_close at active
 show beatrice_v001 smile at inactive
 dlanor '...I am thankful, BEATRICE.'
 hide dlanor_v001
 with Dissolve(0.6)
 show beatrice_v001 smile_close at active
 beatrice 'Hm, I cannot really say that Erika is blessed, but...'
 show beatrice_v001 smile at active
 beatrice 'Either way, it seems she was blessed with a friend.'
 call chapter_end
 return