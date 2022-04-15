label chara442001_01:
 show black_background onlayer black
 $ event_store.current_event='chara442001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara442001_01'
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
 show expression 'images/bg/AdvBg_81.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v001 smile at mei_center
 with Dissolve(0.5)
 show mion_v001 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Alright, everyone, I'm gonna hand out the pre-screening questionnaire forms for the movies we're watching next month in the community center, so make sure to fill them out before the school day is over!"
 hide mion_v001
 with Dissolve(0.2)
 show kazuho_v001 normal at mei_left
 with Dissolve(0.5)
 show kazuho_v001 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Huh? Hey, Mion-san, didn't we do this outside last time?"
 show rika_v001 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v001 normal at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. There were a lot of complaints that it was muggy out and that there were a lot of bugs, so we'll be doing it inside this time."
 hide kazuho_v001
 show miyuki_v001 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v001 smile at inactive
 show miyuki_v001 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Oh yeah, that's right. I like the free feeling you get when watching a movie outside, though."
 hide rika_v001
 show satoko_v001 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v001 odoroki at inactive
 show satoko_v001 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "On the other hand, you can hear the movie much better when you're inside, and it helps you immerse yourself too."
 hide miyuki_v001
 show hanyuu_v001 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v001 smile at inactive
 show hanyuu_v001 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, it was hard to hear some of the lines during the climax of the movie last time too, so it was a bit of a letdown.'
 hide satoko_v001
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show hanyuu_v001 fuan at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Now that you say it, yeah. Inside would have been better at that point.'
 show hanyuu_v001 fuan at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Also, it's nice that we'll be able to choose which movie we'll screen on the questionnaire. It'll be far less likely that we'll watch an uninteresting movie that way."
 hide hanyuu_v001
 show rena_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show rena_v001 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... was that maybe not how it worked at the place Nao-chan lived at before, at before?'
 show rena_v001 smile at inactive
 show nao_v001 fuan at active
 show nao_v001 fuan at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yeah. The screenings at my school in particular were old works chosen by the teachers, and we were forced to watch them and stuff.'
 hide rena_v001
 show miyuki_v001 fuan_close at mei_left
 with Dissolve(0.5)
 show nao_v001 fuan at inactive
 show miyuki_v001 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Oh, I get it, I get it. Like when they have you appreciate an anti-war film since summer's approaching, so they make you write a report on that over break."
 show nao_v001 fuan at inactive
 show miyuki_v001 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "It's fine watching it that way the first time, but when every single year they make you watch what might as well be the same movie over and over again, it gets pretty tough..."
 show miyuki_v001 fuan at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'If the movie is interesting, I can watch it however many times, though. You can find something new every time you watch.'
 show nao_v001 normal at inactive
 show miyuki_v001 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Hm, for me, it's probably enough seeing the same thing once no matter what movie it is."
 show nao_v001 normal at inactive
 show miyuki_v001 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "My childhood friend never gets sick of shark movies even if she watches them hundreds of times. So many times that the tapes would get worn out and she'd have to buy new ones to watch them again..."
 hide nao_v001
 show kazuho_v001 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v001 fuan_close at inactive
 show kazuho_v001 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wh-what an intense friend...'
 hide miyuki_v001
 show rika_v001 smile at mei_left
 with Dissolve(0.5)
 show kazuho_v001 fuan at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Anyway, what movie do you guys plan to suggest on the questionnaire?'
 hide kazuho_v001
 show nao_v001 smile at mei_right
 with Dissolve(0.5)
 show rika_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'A safe choice would be... a Hollywood movie, right?\nIt can be a learning experience to see one where a lot of budget went into fine tuning the production and the clothing.'
 hide rika_v001
 show miyuki_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Of course it's gonna be a detective one for me!\nA cop going on to take down his foes with a huge-barreled magnum is the best!"
 hide nao_v001
 show satoko_v001 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Um... Miyuki-san?\nYou couldn't be thinking of using that as a reference for your future like Nao-san is, right...?"
 show satoko_v001 fuan at inactive
 show miyuki_v001 sinken at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Absolutely not!\nAnd who the hell do you think I am? I'm the daughter of a police officer!"
 show miyuki_v001 sinken at inactive
 show satoko_v001 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "But the people who get guns easiest are policemen...\nI'm a bit worried that you'll get influenced by this movie."
 show satoko_v001 fuan_close at inactive
 show miyuki_v001 sinken at active
 show miyuki_v001 sinken at chara_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Gh...! C-Clearly, the only ones who carry in this country are policemen or members of the JSDF...!'
 show satoko_v001 fuan_close at inactive
 show miyuki_v001 sinken at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "But I comprehend the difference between fiction and reality, and no matter how much stuff gets to my head, I won't commit crimes or anything! You wound this Miyuki-chan!"
 hide satoko_v001
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v001 sinken at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Look at yourself in the mirror. Do you really think an impulsive type like yourself wouldn't haphazardly fire off a gun while in an emergency?"
 show nao_v001 normal at inactive
 show miyuki_v001 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Waaaah! Satoko and Nao are bullying meee!'
 show rika_v001 smile
 show rika_v001 smile:
  yanchor 1.0
  pos (860, 1200)
 with Dissolve(0.5)
 show nao_v001 normal at inactive
 show miyuki_v001 fuan at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'There, there. Nipah!'
 hide miyuki_v001
 hide rika_v001
 with Dissolve(0.2)
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'By the way, Rena-chan, which movie would you want to see?'
 show rena_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show rena_v001 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... I wonder if Rena will want to watch the animal documentary they showed on that commercial, that commercial.\nThose kitties were so kyuuute~♪'
 show rena_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's true. My vote goes in for Rena-chan's pick then!"
 hide rena_v001
 show miyuki_v001 fuan at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show miyuki_v001 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Hellooo, Nao? What happened to earlier when you were passionately talking about how you'd want to learn from a Hollywood movie?"
 show miyuki_v001 fuan at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's okay. The content of the movie is important, but having {i}fun{/i} while watching is of utmost importance."
 hide miyuki_v001
 show rika_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. So in Nao's case, watching together with Rena is very important."
 hide nao_v001
 show hanyuu_v001 smile at mei_right
 with Dissolve(0.5)
 show rika_v001 smile at inactive
 show hanyuu_v001 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, I want to see a movie with a happy end. And if there's something tasty there too, it would be the best time ever!"
 hide rika_v001
 show satoko_v001 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That'd be bad manners, Hanyuu-san. Well, it might be kind of fun to eat something while watching a movie, though... wh-?"
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_539_warp.wav'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 hide hanyuu_v001
 hide satoko_v001
 with Dissolve(0.2)
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '“What is this sensation...?!”'
 stop sound
 show expression 'images/bg/AdvBg_220.png' as bg
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 620)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show eua_v001 smile at mei_center
 with Dissolve(0.5)
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") '...How glad I am to see you, child of man.'
 hide eua_v001
 with Dissolve(0.2)
 show satoko_v001 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Eua...san...?'
 call chapter_end
 jump chara442001_02