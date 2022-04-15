label event01_33_02:
 show black_background onlayer black
 $ event_store.current_event='christmas'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_33_02'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2421.png' as bg
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Out from the train window, the form of the mountains gradually lower with the passage of time, the number of houses increasing as the scenery of a residential area blends into view.'
 narrator '"If you use the bullet train, Tokyo won\'t be much farther".\nI should be there in about 10 minutes or so.'
 show rika_v024 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v024 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'But what should I do once I arrive there...?'
 hide rika_v024
 with Dissolve(0.2)
 narrator 'Satoko left St. Lucia Academy and headed to Tokyo.... that much is clear. However----'
 show rika_v024 fuan at mei_center
 with Dissolve(0.5)
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Even if I know she's in Tokyo, where should I look for her...?"
 hide rika_v024
 with Dissolve(0.2)
 narrator 'Tokyo is a huge, jam-packed city with countless people hustling and bustling around every corner. Searching for someone here will prove far more difficult than it would be in Hinamizawa.'
 narrator "The Tokyo Metropolis area has a steadily growing population, which is said to be around 10 million as of today. ...Even doing it out with simple math, that's 5,000 times that of Hinamizawa."
 narrator 'Furthermore, if you were to factor in all of the people that commute there from the surrounding prefectures, that number would swell up even more.'
 narrator "And amidst all of that, I'm going to seek out one single girl...?\nIf I really think about it, this mission is going to be just as hard as it is reckless."
 narrator "I don't even know where Satoko could be in the first place... out of all of these places in Tokyo I could set off to."
 narrator '(I have no idea what her goal in leaving even was. I have no leads either...)'
 narrator "When I was talking to Satoko last night... she didn't show the slightest hint of wanting to go to Tokyo."
 narrator "We were just having our silly conversations like we usually did.\nI don't even remember a single name of a place or town getting brought up..."
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 narrator 'I wade back into my memories, attempting to fish out the contents of the conversation Satoko and I had last night.'
 narrator "Recalling how she's appeared recently, I can't imagine why that girl would be so short-tempered that she'd run away on impulse. There must have been a sign at some point."
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(Remember... remember...!)'
 narrator 'I tried sifting through the entirety of yesterday rather than just last night.'
 stop sound
 show expression 'images/bg/AdvBg_1760.png' as bg
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Yesterday... we received a notice that a fashion magazine from Shion was delivered for Satoko.'
 narrator 'I believe there was a letter attached reading... "You can\'t get your hands on reads like this at Lucia, so check this out in between your studies, okay?".'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '"If the teachers were to find out about this, I would surely get chastised and have this confiscated. ...Shion-san has sent me yet another thing I\'ll have to burden myself with."'
 narrator 'As exasperated as Satoko was then, her and I are essentially in the same boat with being curious about current fashion trends.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 narrator 'So, we hid in the recesses of the library and read it in secret... getting all sorts of excited while checking out the latest accessories and Western styles.'
 narrator 'Afterwards, we went off on a tangent about movies listed in the magazine... and then went into our studies for a bit too.'
 stop sound
 show expression 'images/bg/AdvBg_2421.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v024 fuan_close at mei_center
 with Dissolve(0.5)
 show rika_v024 fuan_close at active
 show rika_v024 fuan_close at deepbreath_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...It's no use. I can't remember anything else..."
 hide rika_v024
 with Dissolve(0.2)
 narrator 'And... I still had lingering suspicions.\nFor one, did Satoko actually head for Tokyo?'
 narrator 'The president only claimed that Satoko had gone to Tokyo.\nThere was no definite idea of where she had gone.'
 show rika_v024 normal at mei_center
 with Dissolve(0.5)
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Could it also be possible that she went someplace else... or even returned to Hinamizawa?'
 hide rika_v024
 with Dissolve(0.2)
 narrator "Those options can't be refuted either, but if I consider those, then the search range increases drastically."
 narrator '...With that in mind, finding Satoko and bringing her back in time today had likely already been near hopeless.'
 show rika_v024 fuan at mei_center
 with Dissolve(0.5)
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Satoko...'
 hide rika_v024
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'While feeling sentimental, I take the picture I have stored in my bag out again.'
 narrator 'Satoko and I are smiling alongside each other in the picture. At the time this was photographed, we entertained a bright outlook on our future together.'
 narrator 'And yet... why is it that I have to get assaulted by such dark thoughts while on this train...?'
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 Character('????',ctc="ctcArrow", ctc_position="fixed") '--Huh?'
 narrator 'And just then...\nI hear an unexpected voice come from the aisle. And when I turn my face over to look in surprise...?'
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'No way. Rika...chan...?'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '......ah...?!'
 narrator 'A nostalgic voice. \nA nostalgic smile.'
 narrator "But it couldn't be...! Her and I meeting at such a place is...!"
 narrator 'As I sat there frozen in disbelief, she placed her hand on the headrest next to me and struck up conversation.'
 stop sound
 show expression 'images/bg/AdvBg_2421.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v018 smile at mei_center
 with Dissolve(0.5)
 show mion_v018 smile at active
 show mion_v018 smile at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ahaha! You really are Rika-chan! It's been a while; you doing good?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v018
 hide fade onlayer curtain
 show rika_v024 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v024 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Mi-... Mion, is that... you?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v024
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v024 odoroki at mei_left
 show mion_v018 smile at mei_right
 with Dissolve(0.5)
 show rika_v024 odoroki at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Man, what a coincidence for us to meet here! I'm surprised too!"
 show mion_v018 smile at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v024 normal at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'This seat is open. Can I sit here?'
 show mion_v018 smile at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah...'
 show rika_v024 fuan at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ahhh, there we go.'
 hide mion_v018
 hide rika_v024
 with Dissolve(0.2)
 narrator 'Before I could even manage a response, Mion flings herself onto the open seat and slouches over.'
 narrator "Since I expected Mion to mellow out more in college, I couldn't help but smile at her nostalgic behavior. Reassurance began to set in throughout my body."
 show mion_v018 smile at mei_right
 show rika_v024 fuan at mei_left
 with Dissolve(0.5)
 show rika_v024 fuan at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "No, but seriously, what a surprise! To think we'd run into each other on the exact same train at the exact same time like this!"
 show mion_v018 smile at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Um... why are you here, Mion...?'
 show rika_v024 fuan at inactive
 show mion_v018 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I was just in the cabin up ahead until now. There were a bunch of smokers puffin' and heavin' right near this ol' man, y'know~?"
 show rika_v024 fuan at inactive
 show mion_v018 fuan_close at active
 show mion_v018 fuan_close at chara_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Gaaah, too smoky, too smoky! So that's why I escaped over here."
 show rika_v024 fuan at inactive
 show mion_v018 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I wish they'd at least prohibit smoking when inside a train, y'know? There's no place to run in a closed room, so give me a break, will ya? Sheesh."
 show mion_v018 sinken at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...No, not that. I meant why are you riding this bullet train...?'
 show rika_v024 fuan at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah, that? Hmm, well, just on a little trip. Thought I'd go to Tokyo to run some errands."
 show mion_v018 smile at inactive
 show rika_v024 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'A trip... but what about college?'
 show rika_v024 odoroki at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'm on break 'cuz exams are over~.\nUnlike high school, you get long breaks at college."
 show rika_v024 odoroki at inactive
 show mion_v018 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But when winter vacation hits, the trains get stuffy since people are all trying to get home, y'know?"
 show rika_v024 odoroki at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'So, I thought, "Hell, going out on a little excursion might not be so bad for now~".'
 show mion_v018 smile at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I see...'
 show rika_v024 normal at inactive
 show mion_v018 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'What about you?'
 show mion_v018 normal at inactive
 show rika_v024 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Eh?'
 show rika_v024 odoroki at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "High schools are out right now too, but Lucia makes it so you can't leave campus grounds, right? ...Waaaitt. Are you skipping school?"
 show rika_v024 odoroki at inactive
 show mion_v018 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "*cackle*cackle*, Rika-chan ain't half bad either~! You get sent off to live your dream school life as a rich girl and you still turn to delinquency~?"
 show mion_v018 futeki at inactive
 show rika_v024 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "N-... No. It's not that."
 hide rika_v024
 hide mion_v018
 with Dissolve(0.2)
 narrator 'My replies to her were getting weaker by the second... \nI unconsciously bit my lip and looked down.'
 narrator 'Noticing something was up, Mion stopped her cheerful laughter and put a more serious look on her face.'
 show mion_v018 fuan at mei_right
 show rika_v024 fuan_close at mei_left
 with Dissolve(0.5)
 show rika_v024 fuan_close at inactive
 show mion_v018 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah... Sorry, sorry, it's a joke. Don't look so sad."
 show rika_v024 fuan_close at inactive
 show mion_v018 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'But is it that? You got tired of studying and ran away... or something?'
 show rika_v024 fuan_close at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Haha, just kidding! You're not Satoko after all, so for you that'd... be......"
 show mion_v018 smile at inactive
 show rika_v024 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v024 normal_close at inactive
 show mion_v018 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '......Well?'
 show mion_v018 normal at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show rika_v024 fuan at inactive
 show mion_v018 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "The reason why you're taking the bullet train. Is something going on?"
 show rika_v024 fuan at inactive
 show mion_v018 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Don't feel afraid to tell me. I might be able to help you out."
 show mion_v018 normal at inactive
 show rika_v024 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v024
 hide mion_v018
 with Dissolve(0.2)
 narrator 'Should I tell her the truth...? My thoughts and emotions swirl together in a vortex, causing me to hesitate.'
 narrator 'If Mion found out Satoko fled from Lucia, how would she react? \nNo, not even just that...'
 show rika_v024 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v024 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(If Mion finds out, sooner or later Shion will know about it too...)'
 show rika_v024 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(If Shion was made aware of it, what would I do? Even if I convince Satoko and bring her back to Lucia with me...)'
 hide rika_v024
 with Dissolve(0.2)
 narrator "...When Satoko decided to go to Lucia, Shion was strongly opposed to the idea. Even after hearing the news that we got in, she wasn't as happy as everyone else."
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '"...Satoko. If you really feel like you won\'t fit in there, just quit and come back to Hinamizawa right away".'
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '"They\'ll say you\'re a coward or a drop-out... but let them say all they want about you. It\'s just a fact that some places you\'ll fit in, and others not".'
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '"There\'s no sense in pushing your limits if it\'ll cause you to break; you can develop your abilities anywhere else..."'
 narrator "Shion told that to Satoko right before we left. \nSo, if she finds out that Satoko ran away, she'll definitely take Satoko under her protection, even if everyone is opposed to it."
 narrator '"As if I\'ll let her go back to Lucia. I\'ll protect Satoko no matter what anyone says" ...Shion\'s voice echoes in my mind as I picture the scene mentally.'
 show rika_v024 fuan_close at mei_center
 with Dissolve(0.5)
 show rika_v024 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(That's another possible scenario for Satoko. But if it came to that, what would all of her efforts have been for...?)"
 hide rika_v024
 with Dissolve(0.2)
 narrator 'As I sat there silently, lost in thought about how I should convey all of this to her... Mion suddenly shifted her eyes to what I had in my hands.'
 show mion_v018 normal at mei_right
 show rika_v024 fuan_close at mei_left
 with Dissolve(0.5)
 show rika_v024 fuan_close at inactive
 show mion_v018 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Huh... what's that? A framed picture?"
 show mion_v018 normal at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah, this is...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v024
 hide mion_v018
 hide fade onlayer curtain
 show mion_v018 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v018 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ah... could it be a picture of a boy? You got a penpal or something?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v018
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v024 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v024 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah...?'
 hide rika_v024
 with Dissolve(0.2)
 narrator '{i}Swoop{/i}, Mion slides the framed picture out of my hands and flips it right side up. And then...'
 show mion_v018 odoroki at mei_right
 show rika_v024 fuan at mei_left
 with Dissolve(0.5)
 show rika_v024 fuan at inactive
 show mion_v018 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Huh? It's a picture of you and... Satoko?"
 show mion_v018 odoroki at inactive
 show rika_v024 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...I was about to tell you you were wrong. You're hasty as always, Mion."
 show rika_v024 fuan_close at inactive
 show mion_v018 smile at active
 show mion_v018 smile at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ahaha, sorry, sorry. It's because you were holding it like it was your precious treasure."
 hide rika_v024
 hide mion_v018
 with Dissolve(0.2)
 narrator 'While apologizing, Mion fixes her eyes on the picture without so much as a blink.'
 show mion_v018 smile at mei_right
 show rika_v024 fuan_close at mei_left
 with Dissolve(0.5)
 show rika_v024 fuan_close at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'This picture is pretty recent, huh?'
 show mion_v018 smile at inactive
 show rika_v024 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Yeah. This was taken... our last winter before we left Hinamizawa.'
 show rika_v024 smile at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ohhh~? Then did Satoko pull "that" out this year yet? ...Ah, but today\'s too warm, maybe even a little hot.'
 show mion_v018 smile at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'And what would... "that" be?'
 show rika_v024 normal at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "What? Don't you remember the scarf? That fox-like one?"
 hide rika_v024
 hide mion_v018
 with Dissolve(0.2)
 narrator 'As she says that, she points to the Satoko in the picture.'
 show mion_v018 smile at mei_right
 show rika_v024 normal at mei_left
 with Dissolve(0.5)
 show rika_v024 normal at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'That has to be the Christmas present you traded to her, right?'
 show rika_v024 normal at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Damn, how long ago was that again?\n3 years... no, wait, 4 years ago?'
 show rika_v024 normal at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Regardless, Satoko always had that scarf on. She really took a liking to that thing.'
 show rika_v024 normal at inactive
 show mion_v018 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Even putting Satoko and winter in the same sentence, I instantly remembered it. She always had that scarf wrapped around her neck.'
 show rika_v024 normal at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But 4 years, huh... Shouldn't it be about time to replace it with a newer one?"
 show mion_v018 smile at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '......Scarf...'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide rika_v024
 hide mion_v018
 with Dissolve(0.2)
 show black_cover as bg
 narrator 'The moment those words dropped into the depths of my heart, the haze clouding my mind began to clear up.'
 narrator 'Intense elation drove through me as I came to a sudden realization.'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(Yes, that's right... that's right! If that's the case, then Satoko is..!)"
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Mm? Rika-chan, what's wrong?"
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I know what her goal is now! And that girl's destination too!"
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Huh, goal? And destination... which one?'
 call chapter_end
 jump event01_33_03