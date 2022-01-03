label event01_30_05:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=3
 $ event_store.current_chapter='event01_30_05'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 play music 'audio/bgm/BGM_QUEST2_COLLAB2.ogg'
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 pause 1.0
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '.........Huh...? ...Morning already......?'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Nnnnn~... zzzzzz~... The Sonozaki sisters snored on. It was amazing that even their sleeping postures were the same.'
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao 'I had a very... odd dream.'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'It was obviously a dream, but...\nIt was so lucid that I can still recall the details even after waking up.'
 narrator 'In my dream, the witch in the portrait, Beatrice, invited me to a battle of wits... over whether or not that magic circle prank was possible for a human.'
 narrator "Let's recap what happened last night.\nWhen we returned to our guest room, I found my bed ravaged... and a magic circle was painted onto the sheets."
 narrator "It was a prank that Beatrice plays on those who don't believe in witches."
 narrator 'In my dream I suspected Shannon-san, who went up to our room to check the lock of the window.'
 narrator "Thinking about it now, I feel sorry for so diligently suspecting someone who's always helping us."
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '......That red truth Beatrice said...'
 hide nao_v002
 with Dissolve(0.2)
 narrator "If I were to talk about what happened in my dream with someone else, they'd look at me like I had three heads. Even so, I still believe that it happened."
 narrator 'I accept that a witch came to me in my dream.\nHowever, I refuse to believe that a witch came inside my room and pulled off a magic circle prank on my bed.'
 narrator "Last night, after we found that magic circle, we contacted the servant room and had them change the sheets. I'm not bold enough to sleep on sheets like that..."
 narrator 'After the call, the head of the servants, an older man named Genji-san, brought new sheets for us.'
 narrator 'I gave him the sheets rolled-up in a ball and said they were dirty.\nI wonder what he thought when he unraveled it...?'
 play audio 'audio/sfx/SE_5037_getup.wav'
 Character('Sonozaki Sisters',ctc="ctcArrow", ctc_position="fixed") 'Mmmmm, *yawn*~...'
 narrator 'At that moment, both Sonozaki sisters woke up together. Their synchronized awakening amazed me so much, I wanted to record a video of them.'
 show shion_v002 fuan_close at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 fuan_close at inactive
 mion "Oh, Nao-chan, you're up early. Morning~..."
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion "*Yawn*... I feel like I didn't sleep enough, even though we have a photo session today..."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao "Thanks for giving me sleeping pills yesterday, Shion-san. I don't think I could've slept without them due to the shock."
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "I usually have a hard time sleeping on a different pillow while on vacation, so I brought those just in case. I'm glad you found them useful."
 show mion_v002 smile at jump_transform,active
 show shion_v002 smile at inactive
 mion 'Yeeaaah!! We have great weather today! The best kind for a photo shoot!!'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'Nao-san, you were going easy today and just doing embroidery, right? Please feel free to relax on your own, okay?'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal_close at mei_center
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 nao '......Okay.'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Us three were... very surprised... last night when we saw that ominous magic circle painted on my bedsheet.'
 narrator '...However, what surprised me even more was that it was only me who was shocked the entire time.'
 narrator 'A few moments after we saw the magic circle, Mion-san started to roar with laughter. It was so sudden, I was speechless and feared that the witch had possessed her.'
 narrator '....But thinking about it again, Mion-san probably understood in an instant that it was just a prank mimicking a curse from the witch.'
 narrator "...But of course, there is no such thing as witches or magic. There's no way to think of it other than a prank being done by a human."
 narrator 'I thought it was a magic circle drawn with blood at first glance.\nBut Mion-san immediately saw it was just paint.'
 narrator 'The suspect had prepared a sheet with a magic circle drawn on it, and when they found the right time, they snuck into our room and replaced the sheet on my bed.'
 narrator "The real question is... who did it?\nLast night, both Mion-san and Shion-san didn't give any ideas."
 narrator 'In any case... whoever the culprit was, there was no doubt it was the work of a human.'
 narrator 'That\'s why Mion-san can casually grin and say, "They\'ve done it".'
 narrator 'Her laughter reminded me of a schoolchild seeing a well-executed prank.'
 narrator 'And when Shion-san heard that, she also started laughing. Both Sonozaki sisters relished in the timing of the prank.'
 narrator 'Meanwhile, I was frightened at the thought that it was really done by a witch...'
 narrator '...Although, I think anyone would be at a loss for words if they were subject to a prank like this.'
 narrator '......Yeaaaah...'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '......Maybe I should learn to be as stoic like those two...'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Because of that fear, I let the witch impose on my dreams...'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'Hey... did you two... have any dreams?'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion 'I was expecting to have some good dreams, but none last night. What about you, Sis?'
 show mion_v002 smile_close at active
 show shion_v002 fuan at inactive
 mion "Nope. I slept so well last night that I didn't have any dreams."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_526_door_open.wav'
 narrator 'Mion-san carefully unlocked the window and opened it, taking in the spectacular views of the ocean and the rose garden.'
 narrator "...I think that window is the key to solving this mystery. Shannon-san has a master key to our room, but she wasn't involved with the magic circle at all."
 narrator "It's quite obvious that the window is suspicious, which was left unlocked until Shannon-san fixed it."
 narrator 'But whether by stairs or the window... it was stated in red that nobody went up to the second floor.'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at jump_transform,active
 show shion_v002 smile at inactive
 mion "C'mon, let's go eat breakfast! What we're doing at noon today was our biggest reason for coming to this island!"
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "That's right! We don't often have the chance to take photos in such an amazing place."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao 'The two of you came to this island to do a photo session, right?'
 hide nao_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at updown_shake_transform,active
 show nao_v002 smile at inactive
 mion "Wanna join us, Nao-chaaan? We'll make some great memories, won't weee? Ihihihi~"
 show nao_v002 fuan at active
 show mion_v002 smile at inactive
 nao "...I'm worried about that laugh, so no thanks."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 hide mion_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show shion_v002 normal at mei_center
 with Dissolve(0.5)
 show shion_v002 normal at active
 shion 'Erika-san is... oh, still sleeping, I guess?'
 hide shion_v002
 with Dissolve(0.2)
 narrator 'On the doorknob of Erika-san\'s room hung the typical "Do Not Disturb" tag seen in hotels.'
 show shion_v002 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 normal at inactive
 mion 'Hmmm~? But in reality, we end up finding her dead body inside...'
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion "You really don't know how to choose your words, Sis."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2331.png' as bg
 play music 'audio/bgm/BGM_GACHA_COLLAB2.ogg'
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_515_tableware.wav'
 narrator 'On the first floor, Gohda-san and Kanon-san were preparing our morning dishes.'
 show kanon_v001 normal at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal at active
 kanon '...Good morning. Have you slept well last night?'
 hide kanon_v001
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'Now, please be seated. Is Furudo-sama still sleeping?'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'She had a tag hanging on a doorknob saying "Do Not Disturb".'
 hide nao_v002
 with Dissolve(0.2)
 show kanon_v001 normal_close at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show shion_v002 smile at jump_transform,active
 show kanon_v001 normal_close at inactive
 shion 'Wow~, these poached eggs are soooo cute!'
 show kanon_v001 normal at active
 show shion_v002 smile at inactive
 kanon 'Our head chef, Gohda, has prepared for you his finest.'
 hide shion_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show kanon_v001 normal at inactive
 nao 'He really has an eye for aesthetics, huh?'
 hide kanon_v001
 hide nao_v002
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") "Oh, no, it's nothing special. Nahhahhahaha..."
 narrator "Gohda-san blushed with embarrassment as the young girls praised him.\n...He's a loveable guy."
 narrator 'After serving our food, the servants left, telling us to ring the bell if we needed anything else.'
 narrator "I'm still in a daze... reeling from the shock of last night's magic circle and the logic battle with the witch in my dream."
 narrator 'Meanwhile, the Sonozaki sisters were at full throttle as if yesterday had never happened. They ate as much as they could, even if it was just breakfast.'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Well, last night's board game session was a lot of fun!"
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion "Sis. About that tactic you used, I'm sure they'll have an errata in the next rule revision. There's no way they'll allow that."
 show mion_v002 normal at active
 show shion_v002 fuan at inactive
 mion "Oh, really? Whether it's a game or real life, just read the text carefully. You never know where you'll find a trap!"
 show mion_v002 smile at active
 show shion_v002 fuan at inactive
 mion "On the other hand, if you're the only one who sees a loophole, it's a great weapon! It worked perfectly on you all yesterday!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '........................'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao "...... Um, Mion-san. I'm not sure what to say, but can I get your thoughts on something?"
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion 'Hmm? Go on.'
 stop music fadeout 2.0
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator "I'm going to try talking about... that logic battle with the witch in my dream."
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.ogg'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'I had this dream last night. I remember it very vividly and...'
 hide nao_v002
 with Dissolve(0.2)
 narrator "At first, she made fun of me a little, saying that I was too scared from last night's magic circle incident when I told them that I had dreamed about witches."
 narrator '...No, Mion-san. That magic circle was something that would astonish any person with an ordinary mind.'
 narrator "But when we talked about the game with the witch and the battle with the two truths, blue and red, Mion-san's eyes sharpened, and she started to listen to me more carefully."
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'It went like that. ...So, you guys {i}are{/i} suspicious of Shannon-san?'
 show nao_v002 normal at active
 nao 'I thought I was on the right track. However, the witch in my dream stated in red that Shannon-san was not involved in the prank in any way.'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 normal at inactive
 mion "Hmmm. I see, I see... Even in your dream, I'm sure you were thinking hard, Nao-chan!"
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 show shion_v002 normal at active
 show mion_v002 normal at inactive
 shion 'I wrote down all the red truths that Beatrice said in your dream. Could you double-check them?'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator 'Shion-san had written down the red truths, the pivotal factor of the game, on a paper napkin.'
 narrator "I checked it out. ...Yeah. I think it's word for word the same as what Beatrice said."
 show shion_v002 normal at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 normal at inactive
 mion 'Well, yeah, if we think about it normally, it probably was Shannon-san.'
 show shion_v002 normal at active
 show mion_v002 normal at inactive
 shion "{umi_red}Shannon was not involved in any way, directly or indirectly, in the act of laying the sheet with a magic circle on Nao's bed.{/umi_red}"
 show shion_v002 fuan at active
 show mion_v002 normal at inactive
 shion "...this one is quite a pain for us. Don't you think so too, Sis?"
 show mion_v002 fuan at active
 show shion_v002 fuan at inactive
 mion 'The definition of "indirectly" is pretty huge. If you include Shannon-san entering the room as part of the trick, you violate the indirect part, right?'
 show mion_v002 smile at active
 show shion_v002 fuan at inactive
 mion "I mean, this ol' man never suspected Shannon-san in the first place."
 hide shion_v002
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 show mion_v002 smile at inactive
 nao 'What? Do you have any evidence for that?'
 play audio 'audio/sfx/SE_326_ls_spacestop.wav'
 show mion_v002 smile at active
 show nao_v002 odoroki at inactive
 mion "I don't think she'd do it."
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator "Bam. If it were Mion-san's place, she could say it in red without any basis."
 show nao_v002 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion 'Last night, right before Nao-chan mentioned the window lock, she said "I\'ll take my leave for today."'
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion 'That meant she was going to finish her work for the day. In other words, she was going to go back to her quarters or something.'
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao "She only went upstairs because... I told her about the window, which wasn't on her schedule..."
 show mion_v002 smile_close at nod_transform,active
 show nao_v002 normal at inactive
 mion 'Yup. And she only had a few minutes to go in and out of our room.'
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion "An unscheduled request and a small amount of time. Logically, Shannon-san wouldn't have any time for playing that prank."
 hide nao_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 smile at inactive
 shion "Furthermore, in the red truth, it is clearly stated that Shannon-san didn't even touch the sheets, with or without the magic circle."
 show mion_v002 smile at updown_shake_transform,active
 show shion_v002 normal at inactive
 mion "And besides, it's hard for this ol' man to believe that such a fragile, pretty girl would play such a naughty prank!"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '...........................'
 hide nao_v002
 with Dissolve(0.2)
 narrator "Amazing. ...There was no red truth to any of this, but it's incredibly convincing."
 narrator 'It is true that last night I was shocked and lost my composure.\n...However, if you think calmly like Mion-san, you can remove your suspicion of Shannon-san at first glance.'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'If it was impossible for Shannon-san... then who could have played that prank?'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "*giggle*. The red truth where no one but Shannon-san went upstairs is in our way, isn't it?"
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 show shion_v002 smile at inactive
 mion "That's what this ol' man said earlier. You have to read the text very carefully."
 show shion_v002 normal at active
 show mion_v002 futeki at inactive
 shion '{umi_red}No one visited the second floor of the guesthouse from the time you locked the door until you opened it again, except for Shannon.{/umi_red}'
 show shion_v002 smile at active
 show mion_v002 futeki at inactive
 shion "...was what the witch said, wasn't it?"
 show mion_v002 futeki at active
 show shion_v002 smile at inactive
 mion 'Maybe no one went up, but someone could have been waiting in the room, right?'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao 'Huh, waiting...?'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 futeki at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 futeki at inactive
 shion "From the time the room was locked until it was unlocked, the red doesn't allow going upstairs, right?"
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'But someone could have gone upstairs before then.'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Meaning, if you're already upstairs between the time the door is locked and the time it's unlocked, there's no problem at all!"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao 'Ah... oh......'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'They got me on this. What a silly play on words...!\nThe culprit had been lurking upstairs all along, waiting for the opportunity to play the prank...!'
 show mion_v002 smile at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show mion_v002 smile at inactive
 nao "B-but Shannon-san isn't involved in this at all, even indirectly, right?"
 show nao_v002 fuan at active
 show mion_v002 smile at inactive
 nao 'In other words, if the culprit takes advantage of the opportunity when Shannon-san opens and closes the door, that counts as indirectly cooperating with the culprit...'
 show mion_v002 smile at active
 show nao_v002 fuan at inactive
 mion "Or... they could've gotten in through the window?"
 show nao_v002 odoroki at active
 show mion_v002 smile at inactive
 nao 'So... the culprit climbed up the wall outside... broke in through the window, and hid in another room on the second floor...?!'
 show mion_v002 smile at active
 show nao_v002 odoroki at inactive
 mion "I couldn't tell last night because it was dark. But in the morning, this ol' man opened the window and checked the outer wall."
 show mion_v002 smile at active
 show nao_v002 odoroki at inactive
 mion 'There were no obvious traces, but the overhang on the lower floor made for a nice foothold.'
 hide nao_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'Well, if this were a club activity, not only Sis, but any member of the club could use it as a foothold.'
 show mion_v002 futeki at updown_shake_transform,active
 show shion_v002 smile at inactive
 mion "The culprit isn't bad at all. *cackle*cackle*. I'd even say I want to invite them to our club activities."
 hide shion_v002
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show mion_v002 futeki at inactive
 nao 'So, then, who is the culprit...?'
 show mion_v002 futeki at active
 show nao_v002 sinken at inactive
 mion 'It would be someone who was staying on the second floor of the guesthouse last night, besides us...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide nao_v002
 hide fade onlayer curtain
 show erika_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at active
 erika 'Good morning. I had the pleasure of sleeping in.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'At that moment, Erika-san came down the stairs. She smiled at us with a refreshing face.'
 narrator 'When Erika-san rang the bell, Kanon-san arrived a little later.'
 play audio 'audio/sfx/SE_515_tableware.wav'
 narrator 'When Erika-san asked Kanon-san to prepare her breakfast, Erika-san brushed aside her knife and fork, and took out her prided chopsticks.'
 show erika_v001 normal at mei_right
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at active
 show erika_v001 normal at inactive
 mion 'Good morning, Erika-san! Your hair looks great again today!'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika 'Thank you very much. What a fine day today is.'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika "I'm thinking of relaxing and reading my books at the arbor in the rose garden."
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika 'I remember Nao-chama saying she was going to do embroidery while looking at the rose garden?'
 hide erika_v001
 hide mion_v002
 with Dissolve(0.2)
 narrator 'A refreshing smile? ...No, it wasn\'t like that.\nIt was a smile that asked, "Did you enjoy what you saw yesterday?"'
 narrator "...Erika-san, you were the one who played that nasty prank, weren't you..."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop music fadeout 0.5
 pause 2.0
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 play music 'audio/bgm/BGM_GACHA_COLLAB2.ogg'
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'After finishing breakfast, we went back to our rooms for a bit.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Then, with each of our belongings for the day in hand, we came back downstairs.'
 narrator 'I had my embroidery tools and a book I was reading in my bag, while the Sonozaki sisters were carrying that giant trunk.'
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 mion "Ah, here's a good luck charm."
 hide mion_v002
 with Dissolve(0.2)
 narrator 'Mion-san hung a tag on the doorknob that said "Bedmaking Not Necessary".\n...I\'m not sure what she called it a charm for.'
 play audio 'audio/sfx/SE_5056_toy.wav'
 narrator "She was messing around with the doorknob for a while... but I couldn't quite figure out what she was doing."
 show shion_v002 smile at mei_center
 with Dissolve(0.5)
 show shion_v002 smile at active
 shion "*giggle*. You can forget about it for now. It looks like Sis finished. Let's go downstairs!"
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide shion_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2331.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'The three of us descended the stairs and returned to the first floor hall, where Erika-san had just finished her breakfast.'
 show erika_v001 normal at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion "We'll be taking a lot of pictures here and there in the rose garden today."
 show erika_v001 normal at active
 show shion_v002 smile at inactive
 erika "Please spend your time as you wish. As long as you don't take pictures of me, I don't mind anything."
 hide shion_v002
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at active
 show erika_v001 normal at inactive
 mion "What'll you spend your time doing, Erika-san?"
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika "I've brought a special mystery book with me today, so I'm planning to relax and read in the rose garden."
 show mion_v002 smile at active
 show erika_v001 normal at inactive
 mion 'Woah! What kind of book?'
 show erika_v001 normal_close at active
 show mion_v002 smile at inactive
 erika "Well, you see, it would typically be classified under the romance genre... yet it's very much a mystery to me."
 show erika_v001 smile at active
 show mion_v002 smile at inactive
 erika 'What is the motivation to fall in love? Or, why step into the minefield of love without hedging your risks? And so on.'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika 'To me, the behavioral philosophy of love supremacists is a much juicier read than an ordinary mystery.'
 show mion_v002 smile at updown_shake_transform,active
 show erika_v001 normal at inactive
 mion "Hahahaha. This ol' man understands that a little bit too. A woman's mind may be more mysterious than a mystery novel."
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika 'As a detective, there is no harm in learning about the "emotion of romantic love": one of the most common motives for murder since ancient times.'
 hide mion_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion "Erika-san? Love isn't a matter of logic. When you feel the spark, you go zap and then boom♪"
 hide erika_v001
 hide shion_v002
 with Dissolve(0.2)
 narrator 'Zap and boom...? I guess romance {i}can{/i} be a motive for murder...'
 narrator 'It seemed that Erika-san had already brought a book she wanted to read and was planning to leave without going back to her room.'
 narrator 'The four of us left the guesthouse in a group...'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2221.png' as bg
 play music 'audio/bgm/BGM_HOME_COLLAB2.ogg'
 hide fade onlayer curtain
 with Dissolve(1.0)
 show shion_v004 smile at mei_left
 show mion_v005 smile at mei_right
 with Dissolve(0.5)
 show mion_v005 smile at active
 show shion_v004 smile at inactive
 mion "Well, let's just pose as we see fit!"
 play audio 'audio/sfx/SE_562_ls_mahouball1.wav'
 show shion_v004 smile at jumping_transform,active
 show mion_v005 smile at inactive
 shion 'Suuure♪. Can you fully capture my cuteness, Sis?'
 play audio 'audio/sfx/SE_201_shutter.wav'
 pause 0.3333333333333333
 play audio 'audio/sfx/SE_201_shutter.wav'
 pause 0.3333333333333333
 play audio 'audio/sfx/SE_201_shutter.wav'
 pause 0.3333333333333333
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide shion_v004
 hide mion_v005
 hide fade onlayer curtain
 show jessica_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show jessica_v001 odoroki at active
 jessica '...Woah! What are you people doing?! Are you really doing a cosplay photo session?!'
 show jessica_v001 fuan_blush at chara_shake_transform,active
 jessica "Woah, woah, woaaah, isn't this showing your skin t-too much? Isn't this too sexy?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide jessica_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "While saying that, Jessica-san couldn't resist showing her interest in it."
 show jessica_v001 fuan_blush at mei_right
 show shion_v004 smile at mei_left
 with Dissolve(0.5)
 show shion_v004 smile at active
 show jessica_v001 fuan_blush at inactive
 shion "Why don't you come and join, Jessica-san? It can get pretty addictive～♪"
 show jessica_v001 smile at active
 show shion_v004 smile at inactive
 jessica "N-No, No! I'm fine with just looking! Oh, actually, do you want me to hold the camera? I can capture both of you then!"
 hide shion_v004
 show mion_v005 odoroki at mei_left
 with Dissolve(0.5)
 show mion_v005 odoroki at active
 show jessica_v001 smile at inactive
 mion 'What? Really? That would be great! Can you handle an SLR camera?'
 show jessica_v001 smile at nod_transform,active
 show mion_v005 odoroki at inactive
 jessica "Leave it to me! In the past, I messed around a bit with my dad's camera and used it a lot, more than him even."
 hide jessica_v001
 hide mion_v005
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '...I thought you were going to take pictures of roses. I had no idea it was a cosplay shoot.'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v005 smile at mei_right
 show shion_v004 smile at mei_left
 with Dissolve(0.5)
 show shion_v004 smile at active
 show mion_v005 smile at inactive
 shion "Location is also quite important, you know? There's a big difference between shooting in front of a white backdrop and shooting here."
 show mion_v005 smile at active
 show shion_v004 smile at inactive
 mion "This is another job that my uncle asked me to do. He's going to use it for Angel Mort's next campaign!"
 show shion_v004 smile at active
 show mion_v005 smile at inactive
 shion 'If you order certain menu items on a campaign, you will randomly receive a picture of an enchanting Angel Mort waitress.'
 hide mion_v005
 hide shion_v004
 with Dissolve(0.2)
 show jessica_v001 smile_blush at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile_blush at active
 jessica "Let's take a shoot then! Give me your best pose! W-wow, so bold... so sexy..."
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'For Jessica-san, who has been living in solitude on Rokkenjima, the world of the Sonozaki sisters must be completely different.'
 narrator "If you asked me to name the person who's having the most fun on this vacation, I would have to say it's Jessica-san."
 narrator '...Well, girls will be girls. I should spend some time on my own too.'
 narrator 'Where can I relax and immerse myself in embroidery, surrounded by roses-- oh...?'
 stop music fadeout 2.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2341.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao 'It seems we had the same idea...'
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.ogg'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 fuan_close at inactive
 erika "Ah, Nao-chama. ...Would you like to sit here too? It's wonderful here."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator 'The perfect location was surrounded by a spectacular view of the rose garden... the arbor.'
 narrator 'A fancy table and chairs are set there, but the {i}worst{/i} guest made it there before me...'
 show nao_v002 fuan_close at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 fuan_close at inactive
 erika "I'm not going to talk to you or anything. Why not just sit here?"
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao "...I might disturb you, so I'll find a different spot."
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika "I've been observing your every move since you entered this rose garden.\n"
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika "You already know that there is no better place to embroider than here, don't you?"
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "How creepy... She wasn't reading, but instead, she was watching me the whole time...?"
 narrator "After all, I can't get along with this person. I mean, I can clearly sense her hostility."
 narrator "When you think about it, turning your back on this place feels like admitting defeat. There's no way I'm running away..."
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao "...Thank you very much. ...I'll sit across from you, then."
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '<Good>.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'I guess she means "You\'ve got some guts." ...or something like that.'
 narrator "*Sigh*. ......Even though I'm on vacation in this beautiful rose garden, I feel like I've been forced to make a group with annoying classmates."
 narrator "No. I've already got a choice on my hands. It's one of two things: take the challenge or run."
 narrator 'Besides, she played such a terrible prank on my bed...!'
 show erika_v001 normal at mei_right
 show nao_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao '...You really did it last night.'
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika 'I beg your pardon? What are you talking about?'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'She acted innocent, but her grin meant an obvious yes.'
 show nao_v002 normal_close at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika 'I see that you wish to have a debate with me about something that happened last night.'
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika 'But sadly, I am not aware of what happened.'
 show nao_v002 sinken at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao 'W-what a blatant lie....'
 show erika_v001 smile at active
 show nao_v002 sinken at inactive
 erika "Then, would you care to describe what's on your mind in detail, so I can understand too? Eheheheheh!"
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "Deal. As Nao Houtani, I'm not going to take an easy compromise..."
 call chapter_end
 call event01_30_06