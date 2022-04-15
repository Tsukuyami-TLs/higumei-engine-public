label chara062008_01:
 show black_background onlayer black
 $ event_store.current_event='chara062008'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara062008_01'
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
 show expression 'images/bg/AdvBg_1751.png' as bg
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show satoko_v016 fuan_close at mei_center
 with Dissolve(0.08333333333333333)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v016 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "*sigh*... I'm exhausted. I've finally been released from supplementary lesson hell."
 show satoko_v016 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'm fed up with this teacher constantly having her eyes glued on me and giving me extra work at every opportunity she can for no reason."
 show satoko_v016 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'll be free from the failing grade range with 10 more... no, it's 20 more points, isn't it? ...Good grief."
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...It sure is nostalgic thinking back to life at the Hinamizawa branch school. Even apart from my grades, I was held in high regard in so many... mm?'
 play audio 'audio/sfx/SE_530_walk_one.wav'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v016
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v017 smile at mei_right
 show satoko_v016 normal at mei_left
 with Dissolve(0.5)
 show satoko_v016 normal at inactive
 show rika_v017 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah... Satoko. How was your supplementary class?'
 show rika_v017 smile at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Oh, I somehow made it through. It got pushed on a little longer because of that same issue with the pop quiz before, though.'
 show rika_v017 smile at inactive
 show satoko_v016 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Wait... Rika, have you been waiting for my supplementary class to end to meet up with me?'
 show satoko_v016 odoroki at inactive
 show rika_v017 smile at active
 show rika_v017 smile at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Yeah. I was invited to a tea party, but meeting with you is much more important to me, Satoko.'
 show rika_v017 smile at inactive
 show satoko_v016 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I'm sorry. I ended up being a burden to you. And after all of that trouble you went through to meet up with me to study..."
 show satoko_v016 fuan at inactive
 show rika_v017 smile_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Oh no, that's not the case at all. You were really trying your best this time on one of your worst subjects. To the point that you were actually losing sleep over it..."
 show rika_v017 smile_close at inactive
 show satoko_v016 sinken at active
 show satoko_v016 sinken at deepbreath_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...But grades are everything here. Even if I do a little more or a little less, I'll still be subjected to supplementary classes... and it'll be the same mess just as always."
 show satoko_v016 sinken at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v017 fuan at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Please don't make that face, okay, Rika?\nI'm grateful for your help at the very least."
 show rika_v017 fuan at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "You gave up your own study time to lend me a hand with my studies... and I'm thankful for that."
 show satoko_v016 smile at inactive
 show rika_v017 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But... I'm sorry, Satoko. If only I had properly anticipated a pop quiz at this point... then this wouldn't have..."
 show rika_v017 fuan_close at inactive
 show satoko_v016 smile at active
 show satoko_v016 smile at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ohohoho! You aren't God, so having perfect foresight would actually be pretty creepy~!"
 show rika_v017 fuan_close at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "But seriously, Rika... don't feel so responsible for it. I'll try to prepare much more effectively next time."
 show satoko_v016 smile at inactive
 show rika_v017 smile at active
 show rika_v017 smile at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Okay, understood. I won't say those things anymore then.\nAnd I'll be helping with your studies this time too."
 show rika_v017 smile at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Of course. Your help is indispensible to me at Lucia!\nIt might as well be my lifeline... right?'
 show satoko_v016 smile at inactive
 show rika_v017 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '*giggle*... Ah, that reminds me, we practiced making cookies in home economics class today. Would you like to have some with me?'
 show rika_v017 smile at inactive
 show satoko_v016 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'My, is that okay? Giving them to all of those groupies you constantly have would make it much more lively.'
 show satoko_v016 odoroki at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Oh, don't talk like that. Haven't I told you a bunch of times how important spending time with you is to me?"
 show rika_v017 fuan at inactive
 show satoko_v016 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '......Sorry. Somehow my views have gotten pretty warped since coming to this academy... so it makes it hard to take what you say at face value.'
 show satoko_v016 normal_close at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "The truth is I'd prefer if you joined that group too, though. Those girls aren't so bad on the inside, but... um..."
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 show satoko_v016 normal at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yeah, well... for some reason, they have a tendency for wanting to enforce a caste system or something so that they can distinguish right off the bat whether someone is above or below them.'
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Mion-san and Rena-san never exhibited that kind of behavior even though they were older...'
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'That\'s also the reason that I could find mutual trust and understanding with "those kids"; they were good company.'
 show satoko_v016 normal at inactive
 show rika_v017 smile_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Club activities after school in Hinamizawa sure were fun, weren't they...? Even now I still have dreams about it from time to time."
 show rika_v017 smile_close at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I have them almost every day. Well, on the flipside, it probably means I'm accumulating more and more reasons for me to be dissatisfied by the lifestyle at Lucia, though."
 show satoko_v016 smile at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Satoko...'
 show rika_v017 fuan at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Jeez, like I said, stop making that face already. I chose to go to St. Lucia together with you too. You hold no responsibility for that.'
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...That said, if I were to get thrown into one of the cells at the infamous reflection room, I'd probably feel a bit of regret then..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide satoko_v016
 hide rika_v017
 hide fade onlayer curtain
 show satoko_v016 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v016 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "(It's alright... I'm still doing fine for the time being. It's just at this rate, my heart is going to wear away or burn up... whatever it does, it's clear it's on the brink of collapse.)"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v016
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v017 fuan at mei_right
 show satoko_v016 normal at mei_left
 with Dissolve(0.5)
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I have to find a way to break out of this situation, or else.\nWell, it'd be nice if I had any ideas to boot, though..."
 show satoko_v016 normal at inactive
 show rika_v017 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Then how about we start up club activities here at Lucia just like we did in Hinamizawa?'
 show satoko_v016 normal at inactive
 show rika_v017 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It'll be tough forming a club right away, but if we get permission from a teacher, we might be able to find like-minded people."
 show rika_v017 smile at inactive
 show satoko_v016 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "About that... I actually already put in a similar request once to see if it would work. So it's..."
 show satoko_v016 fuan at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What was their reply?'
 show rika_v017 fuan at inactive
 show satoko_v016 fuan at active
 show satoko_v016 fuan at deepbreath_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'She was so closed-minded about it that she kept saying they don\'t accept extracurricular activities that aren\'t involved with studies. She basically shut it down with, "If you have grades like that, you\'d better study using your free time..."'
 show satoko_v016 fuan at inactive
 show rika_v017 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But they're extracurricular {i}because{/i} you do things outside of studying... I'm completely lost on how the teachers here at the academy want us to grow."
 show rika_v017 fuan_close at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Probably into that so-called "good wife and wise mother" archetype. Does what the husband says, earns the favor of the in-laws, gives birth to and raises an excellent child...'
 show rika_v017 fuan_close at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "In short, it's evident that their stance makes light of developing an individual personality, even to the extent of deeming it as unnecessary. At that point, you're already their slave."
 show satoko_v016 normal at inactive
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'None of our classmates feel as if they have to question it at all either, so they submissively obey... Sometimes I worry for them.'
 show rika_v017 normal at inactive
 show satoko_v016 normal at active
 show satoko_v016 normal at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "You said it. What kind of future do these stuck-up masses even have in their heads if they can't do anything without someone controlling them...?"
 show rika_v017 normal at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Well, these {i}are{/i} complaints coming from the likes of a dropout loser like me.'
 show satoko_v016 normal at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show rika_v017 fuan at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ah, but... "those kids" that we studied with in Hinamizawa had their heads screwed on better than them. They\'d be different from the bunches of people at this academy.'
 show satoko_v016 smile at inactive
 show rika_v017 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...? Hey, Satoko, you\'ve been saying "those kids" a few times. Do you mean like Mion, Rena, and Keiichi?'
 show rika_v017 odoroki at inactive
 show satoko_v016 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Not at all. I'm talking about those two with amazing study skills, Miyuki-san and Nao-san."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide satoko_v016
 hide rika_v017
 hide fade onlayer curtain
 show rika_v017 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Miyuki... Nao...'
 call chapter_end
 jump chara062008_02