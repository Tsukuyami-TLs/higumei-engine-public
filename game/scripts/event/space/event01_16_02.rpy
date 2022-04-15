label event01_16_02:
 show black_background onlayer black
 $ event_store.current_event='space'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_16_02'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 show black_cover as bg
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") '...We have arrived. Now, please wake up.'
 stop sound
 show expression 'images/bg/AdvBg_204.png' as bg
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...Eh...? Wh-where is this...?'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'We stand in place with our mouths agape at the view in front of us.'
 narrator 'The interior of the spaceship as well as the view of space from earlier were now nowhere to be seen. In its place—'
 show rena_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hauuu... we're back in Hinamizawa~!\nI wonder how this happened, this happened?"
 hide rena_v002
 with Dissolve(0.2)
 narrator 'All of us are bewildered, looking at our surroundings up and down in a light panic.'
 narrator "This nostalgic environment... there was no mistaking it.\nBut if the story told by K-1's group was true, then this village was..."
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "O-...ohohoho! I see, so it's like that, huh?"
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wh-what do you mean, Satoko-chan? What do you understand?'
 show kazuho_v002 odoroki at inactive
 show satoko_v002 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "But of course! It just turns out the Earth wasn't really destroyed after all!"
 show kazuho_v002 odoroki at inactive
 show satoko_v002 futeki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'All of that revival stuff was just a lie!\nThis was a total facade! One of those so-called practical jokes~!'
 show satoko_v002 futeki at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 hide satoko_v002
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Satoko-chan declares that with a hearty laugh, but...\nWe all exchange glances with indescribable thoughts.'
 narrator 'Honestly, there was still a lot to doubt.\nBut at the very least, there were certain things we couldn\'t ignore and had to accept as "fact"...'
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ummm... Satoko. If this really all was a practical joke, how do you think I got knocked out after getting zapped earlier?'
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yeah... I agree. Besides, didn't you see what happened, Satoko?\nMiyuki-san and Nao-san just started to..."
 hide mion_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at inactive
 show satoko_v002 fuan at active
 show satoko_v002 fuan at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Th-th-...that's...!"
 hide shion_v002
 hide satoko_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_right
 show miyuki_v002 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at active
 show nao_v002 fuan at active
 Character('Miyuki and Nao',ctc="ctcArrow", ctc_position="fixed") '............'
 hide miyuki_v002
 hide nao_v002
 with Dissolve(0.2)
 show keiichi_v007 normal at mei_center
 with Dissolve(0.5)
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Unfortunately, this is anything but a practical joke.\nThat is the one and only certain truth.'
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Your DNA was collected from this village.\nAlso, there are records saying a bunch of natural disasters originated here.'
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'That volcanic toxic gas...? How it spread across the Earth remains unknown. But well, all of it will likely be made clear after our investigation.'
 show kazuho_v002 normal at mei_left
 show keiichi_v007 normal
 show keiichi_v007 normal:
  yanchor 1.0
  linear 0.5 pos (1440,1200)
 with Dissolve(0.5)
 show keiichi_v007 normal:
  yanchor 1.0
  pos (1440,1200)
 show keiichi_v007 normal at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "But... didn't you say the Earth was destroyed and only few survived?"
 show keiichi_v007 normal at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'With that in mind, this Hinamizawa is practically identical to the one we remember...'
 show kazuho_v002 normal at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "I told you, didn't I? Our job at the Environment Protection Coalition is to restore nature and resurrect extinct species."
 show kazuho_v002 normal at inactive
 show keiichi_v007 normal_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") '...However, this was the only area that could be restored at present.\nIf you take even one step away from this area, there would be no water or oxygen there for you.'
 show kazuho_v002 normal at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "The vast outer majority is scorching hot and has raging sandstorms, and I don't think you'd last a minute in conditions like that."
 hide kazuho_v002
 show miyuki_v002 fuan at mei_left
 with Dissolve(0.5)
 show keiichi_v007 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Incredible. To think that this Hinamizawa scenery laid out before me was {i}aaall{/i} recreated artifically...'
 hide keiichi_v007
 hide miyuki_v002
 with Dissolve(0.2)
 narrator "I feel the same way as Miyuki-chan... but I don't have the heart to confirm how true it is."
 narrator 'Besides, if K-1 really was telling the truth, then this hopeless feeling weighing down my body would surely become even heavier and more painful...'
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...So, what are we supposed to do?\nAre you going to make us imitate bug noises or something this time?'
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Hahah, I'm not necessarily going to ask you to do anything difficult.\nYou can just live as you do normally for one whole day."
 show nao_v002 sinken at inactive
 show keiichi_v007 smile_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Then after collecting data on both you guys and the environment, we're going to determine how much nature we want to restore and by what process."
 show nao_v002 sinken at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Of course, once that's done, you'll be transported back to our home planet... where we'll arrange for you to be given minimum living accommodations."
 hide nao_v002
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show keiichi_v007 smile at inactive
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...*gasp*...!'
 hide keiichi_v007
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'We collectively gasp at what K-1 says to us and stare at him wide-eyed.'
 narrator 'He just used the word "transported ".\nSo that means we\'ll...?'
 play music "<loop 1.5>audio/bgm/BGM_EVENT4.ogg"
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... we won't be able to live here in Hinamizawa anymore?"
 show rika_v012 normal at mei_right
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show rika_v012 normal at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep. It would take a lot of time and resources to restore the entire Earth into the form it was in previously.'
 show rena_v002 fuan at inactive
 show rika_v012 smile_close at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'We understand how you feel, but we hope you will enjoy yourselves in this brief period.'
 hide rena_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v012 smile_close at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v012
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "So... feel free to enjoy your time here instead of feeling bad.\nPlease enjoy the last memories you'll make in this land to the fullest."
 show kazuho_v002 fuan at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "I'll also give you some food and weapons for self-defense, just to be safe. ...Well, see you tomorrow."
 hide kazuho_v002
 hide keiichi_v007
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 narrator 'Right as he said that, he somehow produced a knapsack-looking bag and set it on the ground... then the two of them transformed into light particles and vanished without a trace.'
 show miyuki_v002 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "They disappeared, huh...? Well, they probably used some superscience technology or power we don't understand to teleport back to the spaceship."
 show satoko_v002 normal_close at mei_right
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show satoko_v002 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...They might have good intentions, but I can't say I appreciate their condescending attitude."
 show miyuki_v002 normal at inactive
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Their faces alone look similar, but there's a great difference between them and our Keiichi-san and Rika."
 hide miyuki_v002
 hide satoko_v002
 with Dissolve(0.2)
 narrator "We all nod at each other in agreement in response to Satoko-chan's take on the situation. ...It was apparent that everyone felt uncomfortable."
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...To think we only have one day to spend here in Hinamizawa...'
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 hide nao_v002
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'I feel angry, bitter, and sad at our powerlessness.\nThere are far too many emotions to be able to sort through... so I just sigh and shake my head over and over.'
 narrator "I can't accept that this is my final day here... there's no way I could with that information just laid on me suddenly."
 narrator 'Those gloomy feelings caused my gaze to fall, and I was on the verge of sobbing... but at that moment...'
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show mion_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Well... in times like these, you just need to change your state of mind. Alright everyone, let's get back to the stargazing we did last night... no, a thousand years ago, tonight!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show shion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show shion_v002 odoroki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Eh...?'
 show rena_v002 odoroki at mei_right
 with Dissolve(0.5)
 show shion_v002 odoroki at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Mii-chan...?'
 hide shion_v002
 hide rena_v002
 with Dissolve(0.2)
 narrator 'We all simultaneously look at Mion-san with puzzled thoughts after her cheerful declaration.'
 narrator 'Then she shrugged her shoulders with a wry smile... and raised her voice to cheer us up.'
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Moping around won't get anything done!\nIt's much better for our last memory here to be a happy one! ―Right?"
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Tomorrow, we'll be taken away to some world we know nothing about. ...But today, we can create special memories together to be able to look back on them fondly... y'know?"
 show mion_v002 smile at inactive
 Character('Everyone',ctc="ctcArrow", ctc_position="fixed") '...ah...'
 hide mion_v002
 with Dissolve(0.2)
 show shion_v002 futeki at mei_left
 with Dissolve(0.5)
 show shion_v002 futeki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '*cackle*, I see...\nWe need to try replacing all of our sad thoughts with happier ones instead of sitting on them, right?'
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 futeki at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Ahahaha, that's the Mii-chan we know!\nRena has no objections♪"
 hide shion_v002
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Mmm, well, it is pretty aggravating being brought back to life against our will. Like talk about sucky treatment...'
 show rena_v002 smile at inactive
 show miyuki_v002 odoroki at active
 show miyuki_v002 odoroki at jumping_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...Wait, they didn't hear that... right?"
 hide rena_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator 'Miyuki-chan panics and suddenly covers her mouth.\nWe also instinctively braced ourselves... but after seeing that nothing was wrong, {i}pffft{/i}, we all started laughing.'
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'It seems fine to say bad stuff. ...I was a little scared, though. How are you, Miyuki? Anything strange happening to you?'
 show miyuki_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...No. I'm okay, I guess...?"
 show nao_v002 normal at inactive
 show miyuki_v002 smile at active
 show miyuki_v002 smile at updown_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "—You know what, actually, I'm totally fine!\nI'm super lively, as you can see!"
 hide nao_v002
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Alright! C'mon, everyone, let's go!"
 hide miyuki_v002
 show satoko_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ohohohohoho! Now I'm all fired up!"
 hide mion_v002
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahahaha, Rena will keep at it too~!'
 hide satoko_v002
 hide rena_v002
 with Dissolve(0.2)
 narrator 'Our moods in much better shape, we all walked towards the Furude Shrine.'
 call chapter_end
 jump event01_16_03