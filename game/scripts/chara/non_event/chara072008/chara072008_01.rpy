label chara072008_01:
 show black_background onlayer black
 $ event_store.current_event='chara072008'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072008_01'
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
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v017 fuan_close at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '*sigh*... so I wonder what now?\nGetting handed something like this is honestly more trouble than not...'
 show satoko_v016 smile at mei_outerright
 show rika_v017 fuan_close
 show rika_v017 fuan_close:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 with Dissolve(0.5)
 show rika_v017 fuan_close:
  yanchor 1.0
  pos (480,1200)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 show satoko_v016 smile at walk_transform
 show satoko_v016 smile at walk_transform:
  yanchor 1.0
  linear 0.5 pos (1440,1200)
 pause 0.5
 show satoko_v016 smile:
  yanchor 1.0
  pos (1440,1200)
 show rika_v017 fuan_close at inactive
 show satoko_v016 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "My... if it isn't Rika. What could you be doing at a place like this?"
 show satoko_v016 smile at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Satoko...? Um, I might want some advice from you... is that okay?'
 show rika_v017 fuan at inactive
 show satoko_v016 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Advice? That's no big deal at all; I'm sure I can help out somehow."
 show satoko_v016 odoroki at inactive
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's nothing particularly serious.\nI just kind of thought I'd like to hear your opinion on it."
 show rika_v017 normal at inactive
 show satoko_v016 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I can\'t really trust an "It\'s nothing serious" when it\'s coming from you... but understood.'
 show rika_v017 normal at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'So what could have happened?'
 show satoko_v016 normal at inactive
 show rika_v017 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'The truth is earlier... I was handed a love letter.'
 show rika_v017 fuan_close at inactive
 show satoko_v016 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ooooh, my, my,\nCongratulations to y-... huh?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v017
 hide satoko_v016
 hide fade onlayer curtain
 show satoko_v016 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show satoko_v016 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rika, you got a looove letteeeeer?!\nAnd it’s actually real and not a joke?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v016
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v017 fuan_close at mei_left
 show satoko_v016 fuan_close at mei_right
 with Dissolve(0.5)
 show satoko_v016 fuan_close at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...You don't have to be that surprised.\nIs it really that unexpected for me to get something like this?"
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "No, not in the slightest... and, well, you do always have groupies swarming around you and idolizing you on a daily basis, so it's not even close to strange."
 show satoko_v016 normal at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "What an unfair way of speaking...\nHaven't I been telling you they're just school friends gathering to exchange information within the academy?"
 show rika_v017 fuan at inactive
 show satoko_v016 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "You don't have to take it so seriously. I was half joking."
 show satoko_v016 normal_close at inactive
 show rika_v017 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Which means you were half serious.'
 show rika_v017 sinken at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Please don't get it mixed up.\nIf you're hearing me speaking passive-aggressively, then that's you overthinking it."
 show rika_v017 sinken at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Oh? So what you were talking about earlier was a "love letter", right? Isn\'t Lucia an all girls\' school...?'
 show satoko_v016 normal at inactive
 show rika_v017 normal at active
 show rika_v017 normal at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Yeah, that's right. And what about it?"
 show rika_v017 normal at inactive
 show satoko_v016 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Was the letter written and handed to you by some gentleman?'
 show satoko_v016 fuan at inactive
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's an all girls' school, so it was a girl. She's the same grade as us, but I've never heard of her name or seen her face before, so she must be from a different class."
 show rika_v017 normal at inactive
 show satoko_v016 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'And that girl was... confessing her love to you, Rika?'
 show satoko_v016 fuan at inactive
 show rika_v017 normal_close at active
 show rika_v017 normal_close at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Yes. That's why I'm stuck on how to respond to her."
 show satoko_v016 fuan at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Hey, Satoko. How should I handle this situation so she doesn't get hurt from me rejecting her...?"
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I feel like a straightforward "I have no feelings for you" response would be fine here. Answering in a more roundabout way would probably just lead to misunderstandings anyway.'
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Or... that\'s right. How about trying, "I already have eyes for someone"?'
 show satoko_v016 normal at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...That's even more bothersome. If that were to spread, I'd probably get barraged by questions during class in attempt to find out the truth."
 show rika_v017 fuan at inactive
 show satoko_v016 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That's an exaggeration... eh, no, you're probably right.\nContrary to their outward appearance, everyone at this academy loves to gossip..."
 show satoko_v016 fuan at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "There aren't many fun things to do here, so it can't be helped.\nWould you be completely uninterested if there was gossip about someone?"
 show rika_v017 fuan at inactive
 show satoko_v016 sinken_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I can't say completely... but unfortunately, I have no room to worry about that sort of thing unlike some people."
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide satoko_v016
 hide rika_v017
 hide fade onlayer curtain
 show rika_v017 normal at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v017
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 show rika_v017 normal at mei_left
 show satoko_v016 fuan_close at mei_right
 with Dissolve(0.5)
 show rika_v017 normal at inactive
 show satoko_v016 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "......I said too much, Rika.\nYou're not the one at fault for my own struggles with studying..."
 show satoko_v016 fuan_close at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Do you... regret coming to Lucia?'
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I can't entirely say that I don't... but at the end of the day, the one who chose was me. Therefore, I'll solve the current situation myself."
 show satoko_v016 normal at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Is it okay if... I interpret those words at face value?'
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 show satoko_v016 normal at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Yeah. This is no lie, nor show of courage. This is how I truly feel.\nIt's just..."
 show satoko_v016 normal at inactive
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's just... what?"
 show rika_v017 fuan at inactive
 show satoko_v016 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Well... I suddenly remembered.\nBack then, I could have heart-to-hearts with you without worrying about anything...'
 show rika_v017 fuan at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'So I thought... why is it that as soon as we got into this academy, we started sounding each other out overcritically in every conversation?'
 show satoko_v016 normal at inactive
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...I've always intended to speak openly with you, then and now."
 show rika_v017 normal at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Oh, really...? But there have been numerous instances up until now where you wouldn't share important or even vital information with me."
 show satoko_v016 normal at inactive
 show rika_v017 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...And when would that have been?'
 show rika_v017 sinken at inactive
 show satoko_v016 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "My, have you been forgetting?\nI'm certain that sort of thing has happened in however many of our fights we've had."
 show satoko_v016 normal at inactive
 show rika_v017 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...You couldn\'t be talking about "that"...?'
 show rika_v017 sinken at inactive
 show satoko_v016 normal_close at active
 show satoko_v016 normal_close at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I am. It might be insignificant, but I remember it clear as day.'
 call chapter_end
 jump chara072008_02