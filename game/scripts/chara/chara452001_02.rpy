label chara452001_02:
 show black_background onlayer black
 $ event_store.current_event='chara452001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara452001_02'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 stop sound
 scene #000
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show nao_v002 normal at mei_right
 show beatrice_v001 normal_close at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'It seems like our time is up. ...We will meet again, lost child.'
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 normal_close at inactive
 nao 'Eh... ah, wait...?!!'
 play audio 'audio/sfx/SE_230_charge.wav'
 show black_cover as fade with Dissolve(1.0)
 hide beatrice_v001
 with Dissolve(0.3)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_287.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 play music 'audio/bgm/BGM_QUEST2_COLLAB2.ogg'
 nao '...This is... Okinomiya?'
 nao 'Huh, what have I been doing? Or rather... why did I go to Okinomiya?'
 show rena_v002 odoroki at mei_left
 with Dissolve(0.5)
 show rena_v002 odoroki at active
 rena '...Huh, Nao-chan?'
 show rena_v002 odoroki at inactive
 nao 'Ah, Rena-chan!'
 show rena_v002 smile at active
 rena 'Ahaha, hello. ...Are you in the middle of shopping?'
 show rena_v002 smile at inactive
 nao 'Eh? Ah, y-yeah!'
 show rena_v002 smile at inactive
 nao '(I see, I was on my way to go shopping.)'
 show rena_v002 smile at active
 rena 'Hau... that looks like a lot for one person to carry. Do you want me to hold some of it?'
 show rena_v002 smile at inactive
 nao "No, I'm fine. ...Right, I was buying things for dinner."
 show rena_v002 fuan at active
 rena "Speaking of which... I wonder why you're not with Kazuho and her friends today... today?"
 show rena_v002 fuan at inactive
 nao 'Kazuho is home cleaning, and Miyuki is out walking by herself.'
 show rena_v002 fuan at inactive
 nao '(...Yeah, I finally remember. So that should be right... I think.)'
 show rena_v002 fuan at active
 rena 'Nao-chan...?'
 show rena_v002 fuan at inactive
 nao 'Ah, sorry. Rena-chan, did you come to Okonomiya to do shopping?'
 show rena_v002 smile at nod_transform,active
 rena "Yup. I just finished, so now I'm on my way back. Do you want to walk back together, Nao-chan?"
 show rena_v002 smile at inactive
 nao 'Yes. Thank you, Rena-chan.'
 stop music fadeout 0.5
 window hide None
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 pause 1.0
 show expression 'images/bg/AdvBg_1352.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_501_crow.wav'
 play music 'audio/bgm/BGM_GACHA_COLLAB2.ogg'
 rena "The sun is setting soon...roads can be dangerous when it's dark, so I think it's better to go together with someone else."
 nao "Yeah, let's do that."
 rena '...? Did something happen, Nao-chan?'
 nao '"Wh-... what, what do you mean?"'
 rena "Somehow, you're being more reserved than usual... I wonder if something is bothering you, bothering you?"
 nao "No, it's not really like that..."
 nao '...Hey, Rena-chan.'
 rena 'What is it, Nao-chan?'
 nao "Rena-chan, when you get depressed because you're reminded of something you'll never be able to do no matter how hard you try, what could somebody say to cheer you up?"
 rena "Hau, umm... I wonder, does that mean that there's somebody close to Nao-chan that has that problem, that problem?"
 nao '...Yes.'
 nao "(I don't remember the name or the face, but... yes. I feel... I know somebody like that.)"
 rena "And it's not Miyuki-chan or Kazuho-chan..."
 nao "Yes. I would know what to do if it were those two, so if that was the case, I suppose I wouldn't have been as worried."
 rena 'But this is an important person to you.'
 nao "Important... person. That's probably true."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide rena_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao "This person is extremely prideful and it's not easy to figure out what they're really feeling..."
 show nao_v002 normal at active
 nao 'I get the impression that they are a very sensitive, delicate person.'
 show nao_v002 fuan at active
 nao "So, because I don't know her circumstances, I'm afraid I might hurt her if I don't word things correctly, so I don't know what to say."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show rena_v002 normal_close at mei_left
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show rena_v002 normal_close at active
 show nao_v002 fuan at inactive
 rena '............'
 show nao_v002 fuan at active
 show rena_v002 normal_close at inactive
 nao "Sorry, Rena-chan. I'm dragging you into my weird problems."
 show rena_v002 smile at active
 show nao_v002 fuan at inactive
 rena "No, that's not the case. ...I've got it. Would you like to hear Rena's opinion?"
 show nao_v002 smile at nod_transform,active
 show rena_v002 smile at inactive
 nao "O-of course! I'm listening!"
 show rena_v002 smile_close at active
 show nao_v002 smile at inactive
 rena 'Ahaha, thanks. Umm, right...'
 show rena_v002 smile at active
 show nao_v002 smile at inactive
 rena "While there are times where I'm happy when somebody comforts and encourages me..."
 show rena_v002 smile at active
 show nao_v002 smile at inactive
 rena "Sometimes, when you're trying your best to recover and keep at it, that support may feel like a hindrance depending on your current feelings. "
 show nao_v002 fuan at active
 show rena_v002 smile at inactive
 nao "It's sort of like... when you're trying to study, and then somebody tells you to go study, so you feel like trying to do the opposite... I think?"
 show rena_v002 smile at nod_transform,active
 show nao_v002 fuan at inactive
 rena 'Yeah, in that ballpark.'
 show nao_v002 fuan at active
 show rena_v002 smile at inactive
 nao "If that's the case, I wonder what I can do..."
 show rena_v002 smile_close at active
 show nao_v002 fuan at inactive
 rena "...I don't think you need to think about getting them fully recovered."
 show nao_v002 odoroki at active
 show rena_v002 smile_close at inactive
 nao '...What do you mean?'
 show rena_v002 smile at active
 show nao_v002 odoroki at inactive
 rena 'Whether or not you have the ability to stand up on your own, putting on a bright and fun aura can help...'
 show rena_v002 smile at active
 show nao_v002 odoroki at inactive
 rena 'What do you think, you think?'
 show nao_v002 fuan at active
 show rena_v002 smile at inactive
 nao "I'm sorry Rena-chan, but I'm having trouble picturing what you're saying... could you give me an example?"
 show rena_v002 smile at active
 show nao_v002 fuan at inactive
 rena 'Okay, right... Say there was someone who seemed like they were really into their studies, and you brought them sweets as refreshments. How about that, about that?'
 show nao_v002 normal at active
 show rena_v002 smile at inactive
 nao '...Bringing refreshments.'
 show rena_v002 smile at active
 show nao_v002 normal at inactive
 rena 'Do you know what this person likes?'
 show nao_v002 smile at nod_transform,active
 show rena_v002 smile at inactive
 nao 'Ah, I understand. I see, bringing her refreshments...'
 show nao_v002 smile at active
 show rena_v002 smile at inactive
 nao "Thanks, Rena-chan. I don't know what they'll think of it, but... I'll give it a try."
 show rena_v002 smile at nod_transform,active
 show nao_v002 smile at inactive
 rena 'Yup, do your best. Rena will be rooting for you to do well, Nao-chan...!'
 call chapter_end
 jump chara452001_03