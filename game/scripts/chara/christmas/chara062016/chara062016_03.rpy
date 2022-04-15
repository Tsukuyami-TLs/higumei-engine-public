label chara062016_03:
 show black_background onlayer black
 $ event_store.current_event='chara062016'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara062016_03'
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
 show expression 'images/bg/AdvBg_1769.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v021 smile_close at mei_left
 show rika_v021 normal at mei_right
 with Dissolve(0.5)
 show rika_v021 normal at inactive
 show satoko_v021 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...The president taught me that you can use scientific knowledge on traps, and that knowledge on traps can be used in science.'
 show rika_v021 normal at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I... had never thought about that until that point. Making traps was just a hobby for me, so I considered it unrelated to studies...'
 show satoko_v021 sinken at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'But... your traps can definitely be explained through physics.\nIt has a mechanical structure, and it has connections to psychology too.'
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Yes... the definition of science is reproducibility. If anyone gets caught by my traps, that's already the indication of science at work... is what I was told."
 show rika_v021 normal at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'And as our conversation flowed, I showed her the test I had just received back then.'
 show rika_v021 normal at active
 show satoko_v021 normal at inactive
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What did she say?'
 show rika_v021 normal at inactive
 show satoko_v021 sinken_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'She told me... "You\'re aware of the basics and you\'re able to apply them. However, you don\'t have an understanding of those basics...\nIt\'s like you\'re using the wrong parts and tools."'
 show rika_v021 normal at inactive
 show satoko_v021 sinken_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '"And because you continued to receive low grades due to this trivial oversight, you gradually lost sight of how to apply those basics."'
 show rika_v021 normal at inactive
 show satoko_v021 sinken_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '"What separates you from the rest is your quick wit and your skill in problem solving. Without being aware of that, you tend towards over-prudency, and this tacks onto your misconceptions instead."'
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Because she pointed out all these things I couldn't realize on my own one after another, it was almost like I was awakened to the truth."
 show satoko_v021 smile at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "For sure... it's the same as when you fully understand your own health condition and don't find a doctor necessary."
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'My my, Coach will end up unemployed like that.'
 show rika_v021 smile at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "But... the way I've been mastering physics isn't through theory; it's through hands-on experience. The president claimed that I would be able to get higher grades if I changed that approach."
 show rika_v021 smile at inactive
 show satoko_v021 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Math problems are just another stepping stone to perfecting my traps...'
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'She was the first ever person to tell me that traps have an affinity with mathematics.'
 show satoko_v021 smile at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "So that's why your grades in math went up lately..."
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Bettering myself in other subjects... I'll be doing that from now on. \nThe president recommended me a bunch of helpful books."
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I thought difficult books would only make me sleepy... but when I think about how the knowledge in them can be applied to my traps too, I can actually have fun while reading them.'
 stop music fadeout 1.0
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v021
 hide satoko_v021
 hide fade onlayer curtain
 show rika_v021 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...I'm sorry."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 show satoko_v021 odoroki at mei_left
 show rika_v021 fuan at mei_right
 with Dissolve(0.5)
 show rika_v021 fuan at inactive
 show satoko_v021 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show satoko_v021 odoroki at inactive
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Satoko... you know, up until a bit ago... I've been regretting having invited you to come to Lucia."
 show satoko_v021 odoroki at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ever since you came here, Satoko, you seemed piled up with studies and bored out of your mind...'
 show rika_v021 fuan at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Rika, shouldn't it be about time for us to start decorating the tree?"
 show satoko_v021 sinken at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Y-Yes...'
 hide rika_v021
 hide satoko_v021
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/card/Card_062016.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rika, you know... I felt relieved when the president praised me, telling me that I understand the basics.'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I thought, "So I was properly cultivating all the things Rika taught me..."'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'And that, "...The effort and time Rika spent teaching me wasn\'t all in vain..."'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Satoko...'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Personally, I felt so much like a burden that every time the tests returned to me, I felt tears well up in my eyes.'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '"I can\'t get good grades at all. At this rate, Rika\'s efforts will all be for nothing", I thought.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1769.png' as bg
 show rika_v021 fuan_close at mei_right
 show satoko_v021 sinken at mei_left
 with Dissolve(0.5)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v021 sinken at inactive
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'But that was all thanks to the president, not me...'
 show rika_v021 fuan_close at inactive
 show satoko_v021 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I\'ll reiterate what she said. "You understand the basics".\n ...The only reason I know those basics... is because of you.'
 show rika_v021 fuan_close at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Well, the fact that I couldn't put what I learned from you to good use and made a series of mistakes was my own fault, though..."
 show satoko_v021 smile at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '…………。'
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rika... life at school is fun to me now.'
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I can assure you that if you had never invited me to Lucia, the day that I'd think that studying is fun would have never arrived."
 show satoko_v021 smile at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But studying made you suffer, didn't it? ...If you never came to Lucia, you wouldn't have had to go through all of that suffering. Things just happened to work out because you met the president..."
 show rika_v021 fuan at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If you're under the impression that that person changed my life, then that's a huge misunderstanding."
 show rika_v021 fuan at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'If I never came to Lucia, I would have never met that weirdo.'
 show satoko_v021 smile at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Thank you for being considerate.'
 show rika_v021 smile at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That's not it... Jeez, Rika, you don't know anything about yourself either, do you?"
 show satoko_v021 sinken at active
 show rika_v021 smile at inactive
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'The one who saved me before anyone else at Hinamizawa was you.\nThat is an undeniable fact.'
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'And... do you remember? When Keiichi-san moved in, you said, "I feel something might change".'
 show satoko_v021 smile at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Y-Yeah... that did also happen...'
 show rika_v021 smile at inactive
 show satoko_v021 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Keiichi-san arrived, and the village changed.'
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'And with that person becoming the student council president at Lucia... changes are again happening little by little.'
 show rika_v021 smile at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I also want to change. I want to be someone who can proudly walk by your side, Rika.'
 show rika_v021 smile at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'm not as shrewd as you are, and I may trip over and fall back at times... but I'll absolutely, absolutely catch up to you one day."
 show satoko_v021 sinken at inactive
 show rika_v021 smile_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...If that's what you'll do, then I can't lose to you either."
 show rika_v021 smile_close at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Yeah! On the next test, I'll get a high score and strike those teachers dumb..."
 show rika_v021 smile_close at inactive
 show satoko_v021 smile at active
 show satoko_v021 smile at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "And then I'll jeopardize your ranking on the test after that!"
 show satoko_v021 smile at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "*giggle*...I'm excited. I'll also do my best so that I don't lose."
 show rika_v021 smile at inactive
 show satoko_v021 futeki at active
 show satoko_v021 futeki at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yes, do very much look forward to it! Ohohoho!!!'
 call chapter_end
 
 $ persistent.chara062016_done = True
 return