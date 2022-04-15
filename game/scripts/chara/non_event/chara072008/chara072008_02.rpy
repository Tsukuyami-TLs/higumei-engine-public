label chara072008_02:
 show black_background onlayer black
 $ event_store.current_event='chara072008'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072008_02'
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
 show rika_v001 sinken at mei_left
 show satoko_v001 sinken at mei_right
 with Dissolve(0.5)
 show satoko_v001 sinken at inactive
 show rika_v001 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep...'
 show rika_v001 sinken at inactive
 show satoko_v001 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Hmph!'
 hide satoko_v001
 hide rika_v001
 with Dissolve(0.2)
 show mion_v001 fuan at mei_left
 with Dissolve(0.5)
 show mion_v001 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Hey, what happened with you two? You've been looking like you're in a super bad mood since you arrived, and you've been facing away from each other..."
 show hanyuu_v001 fuan at mei_right
 with Dissolve(0.5)
 show mion_v001 fuan at inactive
 show hanyuu_v001 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au... it's not just super bad, it's super duper bad.\nThey've been like this since last night."
 hide mion_v001
 show rena_v001 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v001 fuan at inactive
 show rena_v001 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... this is so unusual; they're always getting along. I wonder what the cause could have been, have been?"
 show rena_v001 fuan at inactive
 show hanyuu_v001 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'U-Um... last night, Satoko was on cooking duty, and Rika went out to shop for the ingredients, but...'
 show rena_v001 fuan at inactive
 show hanyuu_v001 fuan_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'The brand of soy sauce was different from the one she usually gets... and so...'
 hide rena_v001
 show miyuki_v001 odoroki at mei_left
 with Dissolve(0.5)
 show hanyuu_v001 fuan_close at inactive
 show miyuki_v001 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Huuuh...? They're fighting over something like that?\nWho cares whether the soy sauce is different?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide hanyuu_v001
 hide miyuki_v001
 hide fade onlayer curtain
 show satoko_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_537_move_desk.wav'
 show satoko_v001 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's not good at all! What she brought was all wrong; the only soy sauce I'll buy is Tanisa and Tanisa alone! Its flavor fits perfectly with meat and potato stew!"
 hide satoko_v001
 show rika_v001 fuan at mei_center
 with Dissolve(0.5)
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep, but I bought the Anfeya soy sauce thinking it was good at times too. But Satoko still snapped with...'
 show rika_v001 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '"Rika has no understanding of flavor, so she can\'t tell the difference", incredibly agitated-like.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show miyuki_v001 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v001 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ah, so it's Satoko's fault. Everyone has their own tastes, so it's impolite for her to scold you for having no understanding of flavor."
 show satoko_v001 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v001 normal at inactive
 show satoko_v001 fuan at active
 show satoko_v001 fuan at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'O-Of course I slipped up and said something ill-mannered... but I apologized right away!'
 show miyuki_v001 normal at inactive
 show satoko_v001 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'But even so... even considering that, Rika told me, "I don\'t want to hear that from the girl who still can\'t eat broccoli to this day. Nipah ♪"...!'
 show satoko_v001 sinken at inactive
 show miyuki_v001 normal_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ah, Rika's at fault there. Everyone has things they dislike, so she's playing a foul to poke at you for something like that."
 hide satoko_v001
 show nao_v001 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v001 normal_close at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Miyuki... whose side are you on?'
 show nao_v001 fuan at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, neither. The origin of the fight is so trivial, it wouldn't even get you on a tiger's bad side."
 hide nao_v001
 show kazuho_v001 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v001 smile at inactive
 show kazuho_v001 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "But it still made these two good friends hostile towards each other, so wouldn't it be best for someone to intervene?"
 show kazuho_v001 fuan at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Naahh, they probably don't need it.\nJust take a good look at where they're sitting."
 hide kazuho_v001
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v001 smile at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I see. Their faces may be looking away, but they're still sitting in those same desks right next to each other as always."
 hide miyuki_v001
 hide nao_v001
 with Dissolve(0.2)
 show rika_v001 odoroki at mei_left
 show satoko_v001 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show satoko_v001 odoroki at active
 show rika_v001 odoroki at active
 Character('Rika and Satoko',ctc="ctcArrow", ctc_position="fixed") '...gkh...?!'
 show rika_v001 odoroki at inactive
 show satoko_v001 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I-It's just bothersome to move the desk, so I left it as is!"
 show satoko_v001 sinken at inactive
 show rika_v001 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's the same for me.\nPlease have some more faith in me, meep...!"
 hide satoko_v001
 show mion_v001 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v001 sinken at inactive
 show mion_v001 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Rika-chan, you're already going home?"
 show mion_v001 odoroki at inactive
 show rika_v001 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "If I have to stay here any longer, it'll only make me upset.\n...We're going home, Hanyuu!"
 hide mion_v001
 show hanyuu_v001 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v001 sinken at inactive
 show hanyuu_v001 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Huh...? B-But we're going to be doing club activities afterwards..."
 show hanyuu_v001 odoroki at inactive
 show rika_v001 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...If you don't go home with me, today's dinner is going to be very disgusting."
 show rika_v001 sinken_close at inactive
 show hanyuu_v001 fuan at active
 show hanyuu_v001 fuan at chara_shake_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Hiiih... hiiiiiiihh? U-Understood!\nI guess this is bye for now, everyone?!'
 play audio 'audio/sfx/SE_530_walk_one.wav'
 hide rika_v001
 hide hanyuu_v001
 with Dissolve(0.2)
 pause 1.0
 show satoko_v001 normal at mei_left
 with Dissolve(0.5)
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'm going home too. ...Um, Mion-san, would it be okay if I contacted Shion-san right now?"
 show mion_v001 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v001 normal at inactive
 show mion_v001 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Wha-? Well, that girl is at her job in Angel Mort about now, so I think you can get her if you call the shop... but why?'
 show mion_v001 odoroki at inactive
 show satoko_v001 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I apologize, but I'm not up to seeing Rika's face during my meals right now. ...Please help me out, Mion-san."
 show satoko_v001 fuan_close at inactive
 show mion_v001 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If you'll go so far as to say that... then okay. I'll get the phone in the staff room, so you can go head there now."
 show mion_v001 normal at inactive
 show satoko_v001 normal at active
 show satoko_v001 normal at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Understood.\n...Okay, everyone, see you tomorrow.'
 play audio 'audio/sfx/SE_530_walk_one.wav'
 hide satoko_v001
 hide mion_v001
 with Dissolve(0.2)
 pause 1.0
 show rena_v001 fuan at mei_left
 with Dissolve(0.5)
 show rena_v001 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... she gave off an unusually serious aura. I wonder what should be done, be done...?'
 show nao_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show rena_v001 fuan at inactive
 show nao_v001 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "This sure isn't looking pretty...\nIf we let them separate like this, it looks like it'll get drawn out."
 hide rena_v001
 show miyuki_v001 fuan_close at mei_left
 with Dissolve(0.5)
 show nao_v001 fuan_close at inactive
 show miyuki_v001 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Even if you say that, it looks like us intervening will only pull them further apart here... hm.'
 hide miyuki_v001
 show kazuho_v001 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v001 fuan_close at inactive
 show kazuho_v001 normal_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 show kazuho_v001 normal_close at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "What's the matter, Kazuho? You got all silent.\nIs there something on your mind?"
 show nao_v001 normal at inactive
 show kazuho_v001 normal at active
 show kazuho_v001 normal at nod_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah, yeah. It's probably nothing important, though."
 show nao_v001 normal at inactive
 show kazuho_v001 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'I was just wondering why Rika-chan went out of her way to buy a different soy sauce last night...'
 hide nao_v001
 show miyuki_v001 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v001 normal at inactive
 show miyuki_v001 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Couldn't it have been sold out, so she went and bought a different one...? It can't be anything more than that."
 hide kazuho_v001
 show rena_v001 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v001 normal at inactive
 show rena_v001 normal at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Actually, at times like that, Rika-chan asks Mii-chan to share some of her own soy sauce with them.'
 show miyuki_v001 normal at inactive
 show rena_v001 normal at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'And just like Satoko-chan said, using different seasonings in your cooking can make quite the impact on flavor...'
 show miyuki_v001 normal at inactive
 show rena_v001 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "So it's probably a bit unlikely for Rika-chan not to pay attention to that... to that."
 hide rena_v001
 show kazuho_v001 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v001 normal at inactive
 show kazuho_v001 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Uh... are Tanisa soy sauce and Anfeya soy sauce that different...?'
 hide miyuki_v001
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I've taste tested them before, and I felt like the sweetness and saltiness ratios were slightly different. Whichever is better depends on the person, though..."
 show kazuho_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But Anfeya does periodic campaigns to advertise their products, so they leave a strong impression while standing out from shop entrances... ah.'
 hide kazuho_v001
 show rena_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 normal at inactive
 show rena_v001 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "What's up, Nao-chan?\nI wonder if you've realized something, realized something?"
 show rena_v001 smile at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I might have realized the true reason behind their fight... maybe.\nBut I wonder if it's in my place to point this out as another person."
 show rena_v001 smile at inactive
 show nao_v001 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm lost on whether I should just wait for those two to make up instead, you know...?"
 show nao_v001 fuan_close at inactive
 show rena_v001 normal_close at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") '...Those two might definitely make up at some point, even if they do separate themselves.'
 show nao_v001 fuan_close at inactive
 show rena_v001 normal at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "But make up or not, if they still won't be able to say what they want to each other... I think it'll surely leave a bad aftertaste."
 show nao_v001 fuan_close at inactive
 show rena_v001 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "So, as an answer, I'll ask... will you maybe help us figure the cause out together, out together?"
 show rena_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Rena-chan... thank you.'
 show rena_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Alright, let's go to Sevens Mart. It might still be possible if we go now--"
 call chapter_end
 jump chara072008_03