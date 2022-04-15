label chara072017_02:
 show black_background onlayer black
 $ event_store.current_event='chara072017'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072017_02'
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
 show expression 'images/bg/AdvBg_1763.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v021 normal at mei_right
 show rika_v021 normal at mei_left
 with Dissolve(0.5)
 show rika_v021 normal at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'By the way, Rika. When did you first meet the student council president?'
 show satoko_v021 normal at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...The first time I met her was a little while after we enrolled here.'
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Oh my. Then you've known her even longer than I have."
 show satoko_v021 smile at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I would only hear rumors about her at first. Like how there's a terrible delinquent among the second years. And then how..."
 show satoko_v021 smile at inactive
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '…………'
 show rika_v021 fuan_close at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Rika. What are you hiding from me?'
 show satoko_v021 sinken at inactive
 show rika_v021 odoroki at active
 show rika_v021 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Huh?'
 show rika_v021 odoroki at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'No keeping secrets, okay? Tell me what happened.'
 show satoko_v021 sinken at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I don't know if she remembers it, but it was around the middle of June... \nI believe. Back then, I..."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide rika_v021
 hide satoko_v021
 with Dissolve(0.2)
 camera at sepia_shader
 pause 0.0
 stop sound
 show expression 'images/bg/AdvBg_1751.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Oh...?'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'A student was sitting alone on the bench that I had believed was my special seat... no, actually...'
 narrator 'She was sprawled all over it, so much that it looked disgraceful.'
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...She looks like a drunk old man.'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'I carelessly thought out loud...'
 narrator 'Moreover, it seems it reached "her" ears...\nShe blinked a few times before fully opening her eyes.'
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...nh... Nnnnn~...?'
 show rika_v017 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Um, are you okay...?'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'She might be feeling sick, so I call out to the girl while checking up on her.'
 narrator 'But just then, she let out a big yawn while stretching.'
 play audio 'audio/sfx/SE_5037_getup.wav'
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Man, I slept so well. I'm glad Lucia is good at keeping a steady influx of books at the very least. No matter how many of them I read, they never run out of new ones; it's great."
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Well then, time to go to class. ...Excuse me, what time is it now?'
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...School is over already, though.'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'I remember that I was so surprised, I ended up replying very awkwardly.'
 narrator "Once you're found skipping classes at Lucia, you get sent to the reflection room right away, no questions asked."
 narrator "And yet there's someone slacking off out in the open like this.\nCould this person be... an idiot? She is, isn't she?"
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Um... I'll pretend I didn't see anything. I think it's best if you rush to the infirmary or to your room and leave a report with the teachers that you were absent due to sickness."
 hide rika_v017
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Dear me... you're worrying for my sake? What a kind person. What grade are you in?"
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...I'm a first year."
 hide rika_v017
 with Dissolve(0.2)
 narrator 'Her answer felt strangely like she believed she wasn\'t even in a crisis, so with a hint of regret, I thought, "I shouldn\'t have talked to her".'
 narrator "No matter how you look at it, she's either a delinquent or a problem child. If I get too close to her, they might even think I'm the same as her...!"
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(No way...! If they lower my grades for this, I'll lose study time with Satoko...!)"
 hide rika_v017
 with Dissolve(0.2)
 narrator 'I let out a forced laugh with these thoughts in mind, lowering my head and immediately turning on my heel... when...'
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Ah, there's no need to run away. I'm not supposed to be here today."
 show rika_v017 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v017 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide rika_v017
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "I'm not supposed to be present at the academy until this evening."
 Character('????',ctc="ctcArrow", ctc_position="fixed") "It's a clear fact that someone who isn't at the academy isn't supposed to be in class... right?"
 show rika_v017 sinken at mei_center
 with Dissolve(0.5)
 show rika_v017 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What do you mean?'
 hide rika_v017
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "I'm attending an intensive course at a cram school.\n...Well, due to several reasons, someone else went in my place today."
 Character('????',ctc="ctcArrow", ctc_position="fixed") "But well, even if they do find out, as long as I get a reasonable score on tomorrow's competency test... I suppose they'll let it pass."
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "You're telling me as long as you get good grades, they won't care about anything you do...?"
 hide rika_v017
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Yes. If they drop me out, this school's average top score will lower...\nSo, they carefully hold onto those with good grades."
 show rika_v017 sinken_close at mei_center
 with Dissolve(0.5)
 show rika_v017 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '…………'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'Is she being sarcastic? Or is she just a natural airhead with no malicious intent? Whatever it is, she sure gives me the creeps.'
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'By the way, Rika Furude-san.'
 show rika_v017 odoroki at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show rika_v017 odoroki at active
 show rika_v017 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Y-Yes?!'
 hide rika_v017
 with Dissolve(0.2)
 narrator "I inadvertently realigned my posture in response to her saying my name. And wait, I don't even remember mentioning my name to this person...?"
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'It seems you landed the highest score on your midterm. Congratulations.'
 Character('????',ctc="ctcArrow", ctc_position="fixed") "If you'd be up to it, could we have a little talk?"
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I... I refuse!'
 play audio 'audio/sfx/SE_408_run.wav'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'After spitting that out, this time I made sure to run away from her as quickly as I could...'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 camera at reset_shader
 pause 0.0
 stop sound
 show expression 'images/bg/AdvBg_1763.png' as bg
 show rika_v021 normal_close at mei_left
 show satoko_v021 normal at mei_right
 with Dissolve(0.5)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v021 normal at inactive
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...And that\'s how it went. Because of that, my first impression of her was "I don\'t like her", and that\'s all there is to it.'
 show rika_v021 normal_close at inactive
 show satoko_v021 smile at active
 show satoko_v021 smile at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ohohoho! That's just like the president!"
 show satoko_v021 smile at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Ugh, don't laugh. I was really scared back then."
 show rika_v021 fuan at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...? But what about her scares you?'
 show satoko_v021 normal at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "So many things about her are scary. I don't know anything about that person, but she oddly knows way too much about us."
 show satoko_v021 normal at inactive
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Where did that person even get information on this year's grade list in the first place...?"
 show rika_v021 fuan_close at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I guess where she got it from is irrelevant to her.'
 show satoko_v021 smile at active
 show rika_v021 fuan_close at inactive
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'She understands the importance and significance of collecting information. I believe her use of it was appropriate.'
 show satoko_v021 smile at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...You see her positively. Even though she's having us set up for a private Christmas party in outfits like these."
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's a mystery where she got these outfits from, but it was me who originally told her that we wore outfits like these in our club's punishment games."
 show rika_v021 normal at inactive
 show satoko_v021 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "And... it might be a bother to you, Rika, but I'm having fun right now."
 show rika_v021 normal at inactive
 show satoko_v021 smile_blush at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's all thanks to you sticking with me while I study."
 show satoko_v021 smile_blush at active
 show rika_v021 normal at inactive
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Had it not been for you, I would've spent Christmas at remedial classes... I can't thank you enough!"
 stop music fadeout 1.0
 show satoko_v021 smile_blush at inactive
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v021 fuan_close at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Um... Rika?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide satoko_v021
 hide rika_v021
 hide fade onlayer curtain
 show rika_v021 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Listen, Satoko. I believe you're capable of being liked by many."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show satoko_v021 odoroki at mei_right
 show rika_v021 sinken at mei_left
 with Dissolve(0.5)
 show rika_v021 sinken at inactive
 show satoko_v021 odoroki at active
 show satoko_v021 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Wh-what's wrong, all of a sudden?"
 show satoko_v021 odoroki at inactive
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I had a dream recently. In it you became really popular at Lucia, and you were surrounded by so many people... that you stopped talking to me.'
 show rika_v021 fuan_close at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...That's one odd dream. It's weird saying it myself, but I get avoided by people here, remember?"
 show satoko_v021 fuan at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'But a future like that could have existed.'
 show rika_v021 normal at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Well... the president told me something. Dreams that take misleading directions like that may be connected to your heart's desires."
 show satoko_v021 normal at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...What are you saying? Not once have I wished for a future where I'd get separated from you."
 show rika_v021 fuan at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Like I said, it's misleading."
 show rika_v021 fuan at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Dreams of what you don't want to come true, and dreams of what you want to come true are like two sides to the same coin."
 show rika_v021 fuan at inactive
 show satoko_v021 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "And... I've also had dreams where you abandoned me and went somewhere else."
 show rika_v021 fuan at inactive
 show satoko_v021 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "You got tired of me because I couldn't study, and went somewhere far away... that kind of dream."
 show satoko_v021 fuan_close at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "You think I'm the type of girl to do such a thing? ...I'm terribly upset."
 show rika_v021 fuan at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Like I said, this is the type of dream you don't want to see come true. Because I focused too much on how I don't want that kind of future, it led to me having that nightmare..."
 show rika_v021 fuan at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "But you and I both can acknowledge that they're just bad dreams and toss them away."
 show rika_v021 fuan at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Except that all depends on how hard I work from now on.\nI'll do my best not to cause you any trouble!"
 show satoko_v021 sinken at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I don't really think of it as trouble..."
 show rika_v021 fuan at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Oh, the origami are all ready.'
 show satoko_v021 normal at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "My part is done as well. I guess we're finished with decorating then."
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'For sure. We just need to put these up... and after that, we wait for the Christmas party!'
 show satoko_v021 smile at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Yeah.'
 call chapter_end
 jump chara072017_03