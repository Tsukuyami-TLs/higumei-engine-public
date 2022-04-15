label chara452001_02:
 show black_background onlayer black
 $ event_store.current_event='chara452001'
 $ event_store.current_progress=2
 $ event_store.current_chapter='chara452001_02'
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
 show expression 'images/bg/AdvBg_2190.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 normal_close at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'It seems like our time is up. ...We will meet again, lost child.'
 show beatrice_v001 normal_close at inactive
 show nao_v002 odoroki at active
 show nao_v002 odoroki at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Eh... ah, wait...?!'
 play audio 'audio/sfx/SE_230_charge.wav'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide beatrice_v001
 with Dissolve(0.3)
 stop sound
 show expression 'images/bg/AdvBg_287.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 play music "<loop 0>audio/bgm/BGM_QUEST2_COLLAB2.ogg"
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...This is... Okinomiya?'
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Wait, what have I been doing up until now...? Or rather... why did I go to Okinomiya...?'
 show rena_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") '...Wait, Nao-chan?'
 show rena_v002 odoroki at inactive
 show nao_v002 smile at active
 show nao_v002 smile at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, Rena-chan!'
 show nao_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahaha, hello. ...Are you in the middle of shopping?'
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 show nao_v002 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Eh? Ah, y-yeah!'
 show rena_v002 smile at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '(I see, I was on my way to go shopping.)'
 show nao_v002 normal_close at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... that looks like a lot for one person to carry. Do you want me to hold some of it?'
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "No, I'm fine. ...Right, I came here to buy the ingredients for dinner."
 show nao_v002 smile at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Speaking of which... I wonder why you're not with Kazuho-chan and Miyuki-chan today... today?"
 show rena_v002 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Kazuho is home cleaning, and Miyuki is out for a walk by herself.'
 show rena_v002 fuan at inactive
 show nao_v002 smile_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '(...Yeah, I finally remember. So that should be right... I think.)'
 show nao_v002 smile_close at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Nao-chan...?'
 show rena_v002 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, sorry. Rena-chan, did you come to Okinomiya to do shopping?'
 show nao_v002 smile at inactive
 show rena_v002 smile at active
 show rena_v002 smile at nod_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Yup. I just finished, so now I'm on my way back. Do you want to walk back together, Nao-chan?"
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yes. Thank you, Rena-chan.'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1352.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_501_crow.wav'
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 show nao_v002 smile at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "The sun is setting soon... The roads can be dangerous when it's dark, so I think it's better having someone with you when you shop."
 show rena_v002 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Okay, I'll do that from now on."
 show nao_v002 smile at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") '...? Did something happen, Nao-chan?'
 show rena_v002 fuan at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Wh-... what, what do you mean?'
 show nao_v002 odoroki at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Somehow you're being more reserved than usual... I wonder if something is bothering you, bothering you?"
 show rena_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "No, it's not really like that, but..."
 show rena_v002 fuan at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '......um, Rena-chan?'
 show nao_v002 fuan_close at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'What is it, Nao-chan?'
 show rena_v002 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Rena-chan, when you get depressed because you're reminded of something you'll never be able to do no matter how hard you try, what could somebody say to cheer you up?"
 show nao_v002 fuan at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau, umm... I wonder if that means that there's somebody close to Nao-chan that has that problem, that problem?"
 show rena_v002 fuan at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '......There is.'
 show rena_v002 fuan at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "(I don't remember the name or the face, but... yes. I feel like... I do know somebody like that.)"
 show nao_v002 normal_close at inactive
 show rena_v002 normal at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "And it's not Miyuki-chan or Kazuho-chan, right...?"
 show rena_v002 normal at inactive
 show nao_v002 fuan at active
 show nao_v002 fuan at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Right. I would know what to do if it were those two, so if that was the case, I suppose I wouldn't have been as worried."
 show nao_v002 fuan at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'But this is an important person to you.'
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Important... person. That's probably true."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide rena_v002
 hide fade onlayer curtain
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "This person is extremely prideful, and it's not easy to figure out what they're really feeling..."
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I get the impression that they're a very sensitive, delicate person."
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So, because I don't know their circumstances, I'm afraid I might hurt them if I don't word things correctly, so I don't know what to say."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_right
 show rena_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show rena_v002 normal_close at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") '............'
 show rena_v002 normal_close at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Sorry, Rena-chan. I'm dragging you into my silly issues."
 show nao_v002 fuan at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Noo, you aren't at all. \n...I've got it. Would you like to hear Rena's opinion?"
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 show nao_v002 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "O-Of course! I'm listening!"
 show nao_v002 smile at inactive
 show rena_v002 smile_close at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahaha, thanks. Umm, right...'
 show nao_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "While there are times where I'm happy when somebody comforts and encourages me..."
 show nao_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Sometimes, when you're trying your best to recover and keep at it, that support may feel like a hindrance depending on your current feelings. "
 show rena_v002 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So it's sort of like... when you're trying to study, and then somebody tells you to go study, so you feel like doing the opposite... I guess?"
 show nao_v002 fuan at inactive
 show rena_v002 smile at active
 show rena_v002 smile at nod_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Yeah, in that ballpark.'
 show rena_v002 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "If that's the case, I wonder what I can do..."
 show nao_v002 fuan at inactive
 show rena_v002 smile_close at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "...I don't think you need to think about getting them fully recovered."
 show rena_v002 smile_close at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...What do you mean?'
 show nao_v002 odoroki at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Whether or not one has the ability to stand up on their own, putting on a bright and fun aura can help...'
 show nao_v002 odoroki at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'What do you think, you think?'
 show rena_v002 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm sorry, Rena-chan, but I'm having trouble picturing what you're saying... could you give me an example?"
 show nao_v002 fuan at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Okay, right... Say there was someone who seemed like they were really into their studies, and you brought them sweets as refreshments. How about that, about that?'
 show rena_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Bringing refreshments.'
 show nao_v002 normal at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Do you know what this person likes?'
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 show nao_v002 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Yeah, I do. So it's bringing refreshments......"
 show rena_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Thanks, Rena-chan. I don't know what they'll think of it... but I'll give it a try."
 show nao_v002 smile at inactive
 show rena_v002 smile at active
 show rena_v002 smile at nod_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Yup, do your best. Rena will be rooting for you, Nao-chan...!'
 call chapter_end
 jump chara452001_03