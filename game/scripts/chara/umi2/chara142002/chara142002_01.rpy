label chara142002_01:
 show black_background onlayer black
 $ event_store.current_event='chara142002'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara142002_01'
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
 show expression 'images/bg/AdvBg_2461.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show akasaka_v001 smile at mei_center
 with Dissolve(0.5)
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Hey, Rika-chan. You alone today?'
 hide akasaka_v001
 with Dissolve(0.2)
 show rika_v002 normal at mei_right
 show akasaka_v001 smile at mei_left
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Hello, Akasaka. Are you leaving town today?'
 show rika_v002 normal at inactive
 show akasaka_v001 smile at active
 show akasaka_v001 smile at nod_transform
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yeah. We already know what caused the fire at the hot spring inn, so all that's left is leaving it to Ooishi-san's jurisdiction. Outsiders getting involved will just be a hindrance for them."
 show rika_v002 normal at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "So, with that, since I've been needing some rest, I thought it wouldn't be bad to try taking a relaxing stroll through this area."
 show akasaka_v001 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. If you want to sightsee, we can give you a tour around here.'
 show rika_v002 smile at inactive
 show akasaka_v001 smile at active
 show akasaka_v001 smile at updown_shake_transform
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Haha, thanks. Instead of me, though, give Battler-kun and Jessica-san a tour since they've come a long way."
 show rika_v002 smile at inactive
 show akasaka_v001 smile_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Besides, I love aimlessly walking around an unknown area by myself.'
 show akasaka_v001 smile_close at inactive
 show rika_v002 smile at active
 show rika_v002 smile at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Understood. It gets dangerous after dark, so if the sky starts getting cloudy, please do come back safely!'
 show rika_v002 smile at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Aah, I'll take you up on that offer. Do you still want help with the lodging facility, Rika-chan? It's hard work at such an early hour, isn't it?"
 show akasaka_v001 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'No, thanks. Mion called and said she finally found some part time workers, so were dismissed from our jobs yesterday.'
 show akasaka_v001 smile at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'So we started patrolling around in shifts instead since "they" might come around here again.'
 show rika_v002 fuan at inactive
 show akasaka_v001 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '...I see. In my position as an officer, I think leaving such a dangerous task up to you kids is absolutely wrong to do, but...'
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "...unfortunately, with those monsters, only the power you kids have stands a chance against them. It's inexcusable, but I'm going to have to depend on you."
 show akasaka_v001 normal at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Leave it to us, okay? Nipah~.'
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Also, Akasaka. I have something strange I want to ask you, but can you answer it anyway?'
 show rika_v002 normal at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Of course I can. So, what's the question?"
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide akasaka_v001
 hide rika_v002
 hide fade onlayer curtain
 show rika_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Why... did you come here?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 show akasaka_v001 odoroki at mei_left
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show akasaka_v001 odoroki at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show akasaka_v001 odoroki at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'In my memory, Mamoru Akasaka has never come to inspect Hinamizawa on a business trip like this. ...He was always busy working as a public security detective.'
 show akasaka_v001 odoroki at inactive
 show rika_v002 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "No matter the time, due to your personal circumstances, you held priority over your responsibility and dignity in being a public servant. Of course, I don't dislike that you came here because of the hot spring, but..."
 show akasaka_v001 odoroki at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "At the very least, forgetting your job to spend your time leisurely is... something I couldn't imagine."
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Rika-chan.'
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I think there are things you'll be unable to say in your position. ...But please answer as much as you can."
 show akasaka_v001 normal at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Haven't you realized it too? How there are way too many unknown things happening lately?"
 show akasaka_v001 normal at inactive
 show rika_v002 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I've been thinking I could reach for the truth on my own, but since I'm on my own, my hand doesn't reach that far... and..."
 show rika_v002 fuan_close at inactive
 show akasaka_v001 normal_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v002 fuan_close at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Rika-chan. When does your patrol shift end?'
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...? Umm, at noon, I was planning to switch with Mion, but...'
 show rika_v002 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "I'll tell you the rest when we're in a better area. Once it hits noon, let's meet up together somewhere else. Where do you prefer?"
 show akasaka_v001 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...How's the hill at the Furude shrine? Not many people go there, and if someone did come, we'd be able to realize right away."
 show rika_v002 normal at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Got it. Alright. Until I get there I'll be focusing on making a few arrangements. See ya."
 play audio 'audio/sfx/SE_530_walk_one.wav'
 hide akasaka_v001
 with Dissolve(0.6)
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah...?'
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What does he mean by arrangements...?'
 call chapter_end
 jump chara142002_02