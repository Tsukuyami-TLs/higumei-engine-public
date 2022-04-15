label chara072017_01:
 show black_background onlayer black
 $ event_store.current_event='chara072017'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072017_01'
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
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...*sigh*, I'm finally done with one box worth of origami flowers.\nYou end up doing a lot of them when you concentrate on it."
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'But if we want to fill the whole party venue with these, then I still have to do about one... no, two more boxes of them.'
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(I'm glad that the teachers didn't find out Satoko snuck out of school to go shopping, though...)"
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(But seriously, who would have guessed that we'd be forced to prepare the decorations for the student council Christmas party in exchange for keeping it quiet... and let's not even get started on the outfits...)"
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(What on earth could that student council president with that strange laugh be planning...?)'
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Still... I'm making more and more of these and there's just no end in sight."
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I feel like a stay-at-home housewife from one of those soap operas. Will I really make it in time like this...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v021
 hide fade onlayer curtain
 show satoko_v021 normal at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...What are you muttering about over there, Rika?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v021 odoroki at mei_left
 show satoko_v021 normal at mei_right
 with Dissolve(0.5)
 show satoko_v021 normal at inactive
 show rika_v021 odoroki at active
 show rika_v021 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Hyaaaah!? ...Oh, it's you, Satoko. When did you get here?"
 show rika_v021 odoroki at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I knocked so many times.You're to blame for leaving the door completely unlocked and open like that... jeez."
 show satoko_v021 fuan at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Huh, really? I'm sorry. I was concentrating, so I guess I didn't realize."
 show rika_v021 fuan at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Thought so. ...Here, Rika.'
 show satoko_v021 smile at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Why are you offering me your hand...? Is this a handshake?'
 show rika_v021 fuan at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Not at all. Can you give me half of those origami? I'll help too."
 show satoko_v021 smile at inactive
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Eh? B-But you're in charge of the Christmas tree, aren't you?"
 show rika_v021 odoroki at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Don't worry. I'm already done with everything I was in charge of."
 show rika_v021 odoroki at inactive
 show satoko_v021 futeki at active
 show satoko_v021 futeki at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Studies aside,I won't lose when it comes to moving around these fingers~! Ohohoho!"
 show satoko_v021 futeki at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...You're oddly proud about that. But... *giggle*.\nHearing your laugh is reassuring."
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Oh, is that so? Anyway, Rika, if you don't finish things up soon, you won't have any energy for tomorrow."
 show satoko_v021 smile at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Thank you, Satoko...\nWell then, I'm counting on you."
 hide satoko_v021
 hide rika_v021
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v021 fuan at mei_right
 show rika_v021 normal at mei_left
 with Dissolve(0.5)
 show rika_v021 normal at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Still, the student council president really did give us an odd request. Decorating for a Christmas party like this...'
 show satoko_v021 fuan at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Well, she did find a bunch of ways to get us by our tails, so we ended up indebted to her... Now we have no choice but to do as she says.'
 show rika_v021 fuan at inactive
 show satoko_v021 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I feel like I did something bad to you. I didn't think you'd notice that I snuck out right away."
 show satoko_v021 fuan_close at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Of course I would. Ever since we came to this school, not a moment has passed where I'm not thinking about you."
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show rika_v021 smile at inactive
 show satoko_v021 odoroki_blush at active
 show satoko_v021 odoroki_blush at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Y-You don't have to be so direct about it... It's still embarrassing even if it's just the two of us here right now."
 show satoko_v021 odoroki_blush at inactive
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...You may not like Lucia that much, but I want to learn new things together, graduate together.'
 show satoko_v021 odoroki_blush at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "This is the school life we've attained by doing our best together after all... I want it to lead us to a brighter future, even if only by a little."
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Yes, I know that. That's why I'll also keep doing my very best."
 show rika_v021 smile at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Even now, saying that I genuinely like studying would be a bit of an exaggeration, but...'
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Recently, I've been feeling like it's a bit gratifying."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v021
 hide satoko_v021
 hide fade onlayer curtain
 show rika_v021 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Really?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show satoko_v021 fuan at mei_right
 show rika_v021 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v021 odoroki at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...You're being too loud, Rika. We've been given permission to use this room, yes, but don't forget it's the middle of the night right now."
 show rika_v021 odoroki at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If a teacher that doesn't know of our situation sees us, we'll end up owing even more to the student council president."
 show satoko_v021 fuan at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'S-Sorry... I just got startled.'
 show rika_v021 fuan at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's a bit disheartening that you're so surprised, Rika...\nDid it really sound that surprising to you?"
 show satoko_v021 fuan at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I, um... yeah. To tell you the truth, it's so unbelievable that I feel like I'm dreaming."
 show satoko_v021 fuan at inactive
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Like, even when we were preparing for exams, you looked like you were in so much pain...'
 show rika_v021 fuan_close at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'That is true... Despite the fact that you were so busy dedicating your time to me, I would still continuously worry you by looking depressed. That much I was aware of.'
 show rika_v021 fuan_close at inactive
 show satoko_v021 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'But at the time, I was so preoccupied with myself that I had no room to be more considerate towards you.'
 show rika_v021 fuan_close at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '"It\'s suffocating, I can\'t see what the future holds, I want to run...", even though I felt sorry for you, these thoughts were always on my mind.'
 show satoko_v021 fuan at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Did that change because you met the student council president?'
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'd say it was the trigger. I was shocked when I first met her...\nWho would've thought there was someone like this at Lucia."
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rather, I was impressed someone with that attitude was able to keep up with the life at St. Lucia. ...It seems that person has been enrolled since middle school.'
 show satoko_v021 smile at inactive
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "So... if she's been enrolled since middle school, that would make this her fifth year? She managed to live at this academy with a personality like that for so long?"
 show rika_v021 odoroki at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'It really is surprising... so I listened to everything she had to say.'
 show rika_v021 odoroki at inactive
 show satoko_v021 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "After hearing her out, I thought for a bit.\n...The roots between geniuses and dropouts aren't all that dissimilar."
 show rika_v021 odoroki at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's whether you notice that difference or not...\nThat's all there is to it."
 show satoko_v021 normal at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...That sounds so vague, I'm not sure I understand."
 show rika_v021 fuan at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "*giggle*, thought so. I actually don't understand it that well myself, so I just have a general idea of it."
 show rika_v021 fuan at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "But... once I was made aware of that, I began to see studying in a different light rather than something that's painful."
 stop music fadeout 0.5
 show satoko_v021 normal at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v021
 hide satoko_v021
 with Dissolve(0.2)
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 show rika_v021 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(I don't quite understand what Satoko means.)"
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(I almost feel nervous hearing that; it's as if she's been enlightened in an unusual way by a vicious religion or a seminar...)"
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(But...)'
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(The present Satoko is different from the one not too long ago. She's reminiscent to how she was having fun back in Hinamizawa...)"
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(The reason why Satoko had fun back then was because Keiichi, Rena, and the others were there... but now, it's thanks to the student council president.)"
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(............)'
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(...I'm pathetic. I can't make her smile like this on my own...)"
 call chapter_end
 jump chara072017_02