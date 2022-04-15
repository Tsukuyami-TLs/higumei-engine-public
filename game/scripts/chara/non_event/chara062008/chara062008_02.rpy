label chara062008_02:
 show black_background onlayer black
 $ event_store.current_event='chara062008'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara062008_02'
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
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show satoko_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_537_move_desk.wav'
 camera at screenshake_transform
 pause 0.0
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Oh, come ooon!\nNo matter how many times I do this, I still can't understand it!\nHow do you even get an answer like that on this question?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v001 fuan at mei_right
 show satoko_v001 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v001 fuan at inactive
 show mion_v001 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Uh, Satoko... we might be self-studying right now, but we're still in the middle of class. Chie-sensei might get angry at us if you don't quiet down."
 show mion_v001 fuan at inactive
 show satoko_v001 sinken at active
 show satoko_v001 sinken at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'But still! This question written in gibberish is going to make me scream! How is this supposed to be useful to learn in the first place?'
 show satoko_v001 sinken at inactive
 show mion_v001 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That's, well... remembering these formulas and calculation methods will help raise your grades as well as help you on high school and college entrance exams. And then that'll net you an academic background, which can get you into a nice job..."
 show satoko_v001 sinken at inactive
 show mion_v001 normal_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...hopefully anyways, since that's just what I hear."
 hide satoko_v001
 show kazuho_v001 odoroki at mei_left
 with Dissolve(0.5)
 show mion_v001 normal_close at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "On top of it being wishful thinking, it's hearsay...? Uh, Mion-san, saying it that way isn't too convincing, and I also doubt you've convinced Satoko-chan..."
 hide kazuho_v001
 show satoko_v001 sinken at mei_left
 with Dissolve(0.5)
 show mion_v001 normal_close at inactive
 show satoko_v001 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "You said it! Be it on TV or in magazines, they're always saying that if you study, you'll get into a good company, get paid well, and become happy, but..."
 show mion_v001 normal_close at inactive
 show satoko_v001 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If so, does every single rich person on Earth have good study skills?\nNo way; plenty without those skills also exist, don't they?!"
 hide mion_v001
 show miyuki_v001 smile at mei_right
 with Dissolve(0.5)
 show satoko_v001 sinken at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, yeah, true. The world is full of idols, TV personalities, athletes, and much more who didn't go to a good school but are bursting with talent."
 hide miyuki_v001
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show satoko_v001 sinken at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yet even without going to a good school, these people who are rich with intelligence and experience give off a reliable and outstanding impression. So there might not be such a strict rule behind it... maybe.'
 show nao_v001 normal at inactive
 show satoko_v001 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "See, those two agree with me! So isn't there no need at all to push yourself to study past your limits?"
 hide nao_v001
 show rena_v001 smile at mei_right
 with Dissolve(0.5)
 show satoko_v001 smile at inactive
 show rena_v001 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... but Miyuki-chan and Nao-chan can study extremely well.\nThey get great scores on tests, and they never miss out on homework either...'
 show satoko_v001 smile at inactive
 show rena_v001 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "But if you go and decide that it's all useless regardless of that, they probably won't feel great about it either... it either."
 show rena_v001 fuan at inactive
 show satoko_v001 fuan at active
 show satoko_v001 fuan at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ah... th-that's..."
 hide rena_v001
 show miyuki_v001 smile at mei_right
 with Dissolve(0.5)
 show satoko_v001 fuan at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ahahaha, you're too kind, Rena. I'll get embarrassed if you worry about me like that."
 show satoko_v001 fuan at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "But the thought of my studies being useful for the future hasn't crossed my mind that much. Maybe I'll use it for something someday."
 hide satoko_v001
 show rika_v001 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v001 smile at inactive
 show rika_v001 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Then why do you study, Miyuki?'
 show rika_v001 normal at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, good question... I have a lot of reasons, but the biggest one is probably the feeling of exhilaration once you figure something out.\nIt's almost the same feeling as clearing a game."
 hide rika_v001
 show satoko_v001 fuan at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_122_status_piyopiyo.wav'
 show miyuki_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Writing down math equations and kanji is a {i}game{/i} to you...?\nYour sensibility with that is so unique, I can't sympathize at all, Miyuki-san."
 show satoko_v001 fuan at inactive
 show miyuki_v001 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Huh, really? But just like how puzzles can't be completed without putting the pieces in the right place... you need knowledge to answer a quiz, right?"
 show satoko_v001 fuan at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "And besides, even video games require you to memorize your opponent's attack patterns and where hidden items are and stuff.\nIt's just a matter of training your reflexes, y'know?"
 show miyuki_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'That, well... you are right there.'
 hide miyuki_v001
 show nao_v001 smile at mei_right
 with Dissolve(0.5)
 show satoko_v001 fuan at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I have the same view as Miyuki here.\nAnd plus, contrary to what we were talking about earlier, I actually do want to get high grades to compete with the other kids...'
 show satoko_v001 fuan at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Pair me up against a difficult question, my heart races.\nI want to solve things better and faster than the other kids.'
 hide satoko_v001
 show mion_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show mion_v001 smile at active
 show mion_v001 smile at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ahahahaha, I see! Be it video games or studies, Nao-chan is a true gamer at heart~!'
 hide mion_v001
 show miyuki_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "For sure...! I also regularly compete with my childhood friend over test grades and stuff, and then the winner gets treated with coffee.\nStuff like that is fun, y'know~?"
 show miyuki_v001 smile at inactive
 show nao_v001 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...It's forbidden to gamble as a student.\nYou aspire to be a police officer, so you’d better start having some respect for the law."
 show nao_v001 sinken at inactive
 show miyuki_v001 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Woahh, we're not betting money or anything, so keep that strict stuff to yourself. Hmph."
 hide nao_v001
 hide miyuki_v001
 with Dissolve(0.2)
 show satoko_v001 normal at mei_center
 with Dissolve(0.5)
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 show hanyuu_v001 fuan at mei_right
 show satoko_v001 normal
 show satoko_v001 normal:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 with Dissolve(0.5)
 show satoko_v001 normal:
  yanchor 1.0
  pos (480,1200)
 show satoko_v001 normal at inactive
 show hanyuu_v001 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, what's the matter, Satoko? You got quiet all of a sudden..."
 show hanyuu_v001 fuan at inactive
 show satoko_v001 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ah, no... it's just incredibly hard for me to think of studying in a fun way like that..."
 show hanyuu_v001 fuan at inactive
 show satoko_v001 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Our abilities really are different. I'm jealous of Miyuki-san and Nao-san..."
 hide hanyuu_v001
 show miyuki_v001 normal at mei_right
 with Dissolve(0.5)
 show satoko_v001 fuan_close at inactive
 show miyuki_v001 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...Hey, Satoko, is that actually true? Isn't that just an assumption?"
 show miyuki_v001 normal at inactive
 show satoko_v001 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh...? Wh-what do you mean?'
 show satoko_v001 odoroki at inactive
 show miyuki_v001 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'The games I mentioned before have both an answer and a way to solve them. And incidentally, those two things also exist in school studies... alongside getting high scores.'
 show satoko_v001 odoroki at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'But... can you explain the difference between the two to me?'
 show miyuki_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That's..."
 hide miyuki_v001
 show nao_v001 smile at mei_right
 with Dissolve(0.5)
 show satoko_v001 fuan at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "If they are different, then it's clear how.\nIt's whether or not you enjoy the game... right?"
 show satoko_v001 fuan at inactive
 show nao_v001 smile_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Whether or not you can enjoy studying is just like how every person has their own preferences on vegetables. So...'
 show satoko_v001 fuan at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I've never had points where I hated studying.\nIt's not a matter of good or bad in my head, it just is what it is."
 show nao_v001 smile at inactive
 show satoko_v001 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Nao-san...'
 show satoko_v001 odoroki at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "But, you know, Satoko? When I don't want to put up with a boring game, I can just toss it aside and pick up a different game..."
 show satoko_v001 odoroki at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Though unfortunately, the options we have now are slim and few, so we'll have to make do with what we have without another round of allowances."
 show satoko_v001 odoroki at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So, it'd be a waste not to play them with your all.\nAnd of course, you can always find out how to enjoy them in your own way too... right?"
 show nao_v001 smile at inactive
 show satoko_v001 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 hide nao_v001
 show miyuki_v001 normal at mei_right
 with Dissolve(0.5)
 show satoko_v001 normal_close at inactive
 show miyuki_v001 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Also... this has been on my mind for a while now... but why don't you try looking at each part of this question individually?"
 show satoko_v001 normal_close at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "It can't be fun picking up a game you don't know how to find an answer or solution to while playing. So, I think looking at those first and working backwards on the problem would be much more efficient."
 show miyuki_v001 smile at inactive
 show satoko_v001 odoroki at active
 show satoko_v001 odoroki at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Huuuh? But wouldn't looking at the answer first be cheating?"
 hide miyuki_v001
 show nao_v001 smile at mei_right
 with Dissolve(0.5)
 show satoko_v001 odoroki at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'You think? Like even with a plastic model of something, trying to recreate it just by seeing the end product would be hard... so people usually put those together while looking at the instructions, right?'
 show satoko_v001 odoroki at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So, rather than being disappointed that your answer is wrong, you have to contemplate how you'd reach the correct answer..."
 show satoko_v001 odoroki at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I believe rinsing and repeating that process is the road to getting the correct answer through polishing up your skills.'
 hide satoko_v001
 show kazuho_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'The way you two look at it... is definitely game-like.\nSolving something by remembering the answer is kind of twisted, though.'
 hide nao_v001
 show miyuki_v001 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v001 smile at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ahahahaha! Please denounce it as twisted!\nIf you find the games you have on hand boring to play normally, then there's no other way but to change how you play!"
 show kazuho_v001 smile at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "So, you should try changing your viewpoint on it, Satoko.\nStudying isn't a race to see who can put up with it the longest, so why not trying to find ways you can enjoy doing it... y'know?"
 hide kazuho_v001
 hide miyuki_v001
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1751.png' as bg
 pause 1.0
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v017 odoroki at mei_right
 show satoko_v016 smile at mei_left
 with Dissolve(0.5)
 show rika_v017 odoroki at inactive
 show satoko_v016 smile at active
 show satoko_v016 smile at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...*chuckle*, ahahaha...'
 show satoko_v016 smile at inactive
 show rika_v017 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Ah-... wh-what's wrong, Satoko? You suddenly started laughing..."
 show rika_v017 odoroki at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'No... *chuckle*, I was just remembering what Miyuki-san and them were saying to me back then.'
 show rika_v017 odoroki at inactive
 show satoko_v016 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "When played normally, it's just a dumb old game, so all you have to do is change the way you play it... huh?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide satoko_v016
 hide rika_v017
 hide fade onlayer curtain
 show satoko_v016 futeki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_226_shine.wav'
 show satoko_v016 futeki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...How interesting.\nNever mind studying; this Satoko Houjou doesn't intend to lose to anyone while playing a game!"
 call chapter_end
 jump chara062008_03