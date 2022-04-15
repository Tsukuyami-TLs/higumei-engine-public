label chara142002_02:
 show black_background onlayer black
 $ event_store.current_event='chara142002'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara142002_02'
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
 show expression 'images/bg/AdvBg_141.png' as bg
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show akasaka_v001 normal at mei_center
 with Dissolve(0.5)
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Hey, sorry, Rika-chan. We made plans ahead of time, but I made it here a little late.'
 hide akasaka_v001
 with Dissolve(0.2)
 show rika_v002 normal at mei_right
 show akasaka_v001 normal at mei_left
 with Dissolve(0.5)
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. It's okay. I was the one who came earlier than we promised."
 show rika_v002 normal at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Haha, is that right? ...Also, I can't stay for too long, so let's try to make this brief."
 play audio 'audio/sfx/SE_5037_getup.wav'
 show rika_v002 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Firstly, Rika-chan, look at this.'
 show akasaka_v001 normal at inactive
 show rika_v002 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'This is...\nCould this be a {b}Role Card{/b}?'
 show rika_v002 sinken at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Hm... So, you kids have been calling them "Cards". Who gave it that name?'
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Miyuki did. Also, she was the first one to try shouting the phrase, "{b}Role Card Escalation!{/b}".'
 show rika_v002 normal at inactive
 show akasaka_v001 normal_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "...I see. Seems like I'm also going to have to hear what she has to say afterwards."
 show akasaka_v001 normal_close at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Anyway, Akasaka, where and when did you get your hands on this "Card"?'
 show rika_v002 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Far off from Hinamizawa, on the prefectural border in the mountains. I discovered it about 4 years ago.'
 show rika_v002 normal at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'This was directly after the dam site foreman was killed and dismembered in the {b}first year of the curse{/b}.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide akasaka_v001
 hide rika_v002
 hide fade onlayer curtain
 show rika_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v002 odoroki at active
 show rika_v002 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Ah...?! Akasaka, you've been involved with the {b}Oyashiro-sama's curse{/b} incidents?"
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "B-But... you're definitely a detective from Tokyo, and...?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show akasaka_v001 normal at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yeah. Normally, working in public safety versus out in the field are two separate worlds. So, for my part, I thought I shouldn't intrude on Ooishi-san's group's duty at first."
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'But over these past few months, the situation has changed.\n...Can you look at this "Card" one more time?'
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 pause 0.5
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...It's blackening a lot. It's almost like it's been scorched in a fire."
 show rika_v002 normal at inactive
 show akasaka_v001 normal at active
 show akasaka_v001 normal at nod_transform
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Exactly. What's more, I sent it in to be appraised by a forensic research team, and the result confirmed that, through means unknown, it was made from a material that cannot be found in this world."
 show rika_v002 normal at inactive
 show akasaka_v001 normal_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Of course, if that is the case, then the police have their hands tied. Even more of a reason for me as public safety to poke my nose in it.'
 show rika_v002 normal at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "But... if the same recent events happened in the capital, or worse, if it led to there being a crime scene, that would be a different story. I assume there's a high possibility some sort of conspiracy is in the works."
 camera at screenshake_transform
 pause 0.0
 show akasaka_v001 sinken at inactive
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'So even Tokyo has {b}Role Cards{/b}...? How could that possibly be?'
 show rika_v002 odoroki at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Well, before I explain that... Rika-chan, my family owes you their lives. At the very least, I believe that you saved us.'
 show akasaka_v001 normal at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep...?'
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '5 years ago, you told me to, "Go back to Tokyo.". At the time, I couldn\'t understand the meaning behind it, but...'
 show rika_v002 fuan at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "For some reason, I got uneasy, and decided to abandon my duties the next day so that I could return to my wife admitted in a hospital in Tokyo... That's when an accident on the stairs leading to rooftop happened."
 show akasaka_v001 sinken at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide akasaka_v001
 hide fade onlayer curtain
 show akasaka_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show akasaka_v001 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'When I learned about that... my body shook with fear. Every day, my wife would take those stairs to get to the rooftop, where she would wish for my safety and swift return.'
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'And then, whether it was done by human hands or whether it was simply by natural degradation, I have no idea... but the none-slip adhesive for the tiles wore off, and someone thoughtlessly stepped on them, losing their balance.'
 show akasaka_v001 fuan_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "I feel horrible for the person who was gravely injured in the accident... but if it was my wife who used those stairs, I don't know if she would have been able to recover from that."
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "The fact that my wife and my daughter in her belly were safe... is all thanks to you, Rika-chan. That's why, from the bottom of my heart, I feel as though I'm indebted to you."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide akasaka_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v002 normal at mei_right
 show akasaka_v001 normal at mei_left
 with Dissolve(0.5)
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Akasaka...'
 show rika_v002 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "With that in mind, I want you to hear me out. ...As long as it's with you, I'll convey the full truth. So, please, I want you to hear me out on this."
 show rika_v002 normal at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "And in return, please judge whether or not I'll be able to lend you my aid... as you listen to my answer."
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide akasaka_v001
 hide rika_v002
 hide fade onlayer curtain
 show rika_v002 sinken_close at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v002 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Understood, Akasaka. I believe in you too.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show akasaka_v001 smile at mei_left
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Thank you, Rika-chan.'
 show rika_v002 smile at inactive
 show akasaka_v001 normal_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ah... The introduction ended up being pretty long. I'll have to share the details with you another day, but I'll convey just this to you for now."
 show rika_v002 smile at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'The grotesque lifeforms that are showing up in Hinamizawa... you kids call them {b}Tsukuyami{/b} and fight them. "They" were involved with the earlier case.'
 show rika_v002 smile at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Some government agencies are clearly aware of their existence. ...Just like they are about the {b}Role Cards{/b} you kids have too.'
 show rika_v002 smile at inactive
 show akasaka_v001 sinken_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "On top of that, those people are planning something... I've been dispatched to this village by my higher ups to determine exactly what."
 show akasaka_v001 sinken_close at inactive
 show rika_v002 odoroki at active
 show rika_v002 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Wha-...? Th-that would mean via the Irie Institute, the {b}Tokyo{/b} organization is doing something that's impacting Hinamizawa?!"
 show rika_v002 odoroki at inactive
 show akasaka_v001 sinken at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "...I see. So, you really do know about {b}Tokyo{/b}, then? As well as the Irie Clinic's true form hidden underneath..."
 show akasaka_v001 sinken at inactive
 show rika_v002 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Yes, of course. If what you want to hear is how I'm cooperating with the Irie Institute, then I'll tell you everything I know."
 show rika_v002 sinken at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Yeah, I would be insanely grateful if you did that. Putting it frankly, there were a bunch of factors that I was having difficulty comprehending regarding the relationship between you, Mr. Irie, and Mrs. Takano.'
 show rika_v002 sinken at inactive
 show akasaka_v001 normal_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "The only thing is... the conspiracy this time is stirring much differently from the way these people move. That's why public security has been letting up on them for the time being, but..."
 show akasaka_v001 normal_close at inactive
 show rika_v002 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What would this other organization be called?'
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide akasaka_v001
 hide fade onlayer curtain
 show akasaka_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'That would be __ __.'
 call chapter_end
 jump chara142002_03