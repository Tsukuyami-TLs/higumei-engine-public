label chara492001_02:
 show black_background onlayer black
 $ event_store.current_event='chara492001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara492001_02'
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
 show expression 'images/bg/AdvBg_373.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST2_COLLAB3.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show ange_v001 normal at mei_left
 show miyuki_v002 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...I see. I more or less understand the details behind you three getting sent to this village. So that's why you told me not to pry too deep, huh...?"
 show ange_v001 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Nooo, I misspoke, I misspoke. If you weren't in the same position as us, that might have been a pretty reckless thing to say."
 hide ange_v001
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Not just "might have". Are you seriously light-lipped or are you just careless...?'
 show nao_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yeah, yeah, I'll listen nice and carefully to your complaints after.\n...So, what do you plan on doing next?"
 hide nao_v002
 show ange_v001 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'You\'re asking me...\nMeanwhile, my goal is figuring out how to get back to my original "World", and fast.'
 show ange_v001 normal at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, that would clearly be your best option... but while you're stuck not knowing how you got here, it doesn't look like there are many clues either, y'know?"
 show miyuki_v002 normal at inactive
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...That's........."
 show miyuki_v002 normal at inactive
 show ange_v001 sinken at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'But like I said, I can\'t just sit here all willy nilly. I have things I need to do back in my original "World".'
 hide miyuki_v002
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show ange_v001 sinken at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Things you should do? What would that--'
 stop music fadeout 0.5
 hide ange_v001
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_526_door_open.wav'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show battler_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hm? Wow, so you guys were over here. I've been wondering where you went."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah, Battler-san. Good morning.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide fade onlayer curtain
 show ange_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show ange_v001 odoroki at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...gh......?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide ange_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB3.ogg"
 show battler_v001 smile at mei_right
 show ange_v001 odoroki at mei_left
 with Dissolve(0.5)
 show ange_v001 odoroki at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yeah, morning. ...Hm?\nYou're a new face. You a friend of Kazuho-chan's?"
 show battler_v001 smile at inactive
 show ange_v001 fuan_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Um... I-I'm..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide ange_v001
 hide battler_v001
 hide fade onlayer curtain
 show jessica_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Haah... haahh... haaahhh...! Don't screw around with me, Battleeerr! Don't just run off to the clinic on your own!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide jessica_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show battler_v001 smile at mei_right
 show jessica_v001 sinken at mei_left
 with Dissolve(0.5)
 show jessica_v001 sinken at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yeah, my bad, my bad. But now we're all here. Isn't this perfect?"
 show battler_v001 smile at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well... I guess.\nHuh? Who's that girl? She's wearing our armband too..."
 show jessica_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Now that you say it, the armband on her outfit...\nAlso if you look closely, that ring she's wearing does have the {b}one-winged eagle{/b} on it too. It's the same as the one Grandfather designated as the symbol of the family head, right?"
 show battler_v001 normal at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I have no idea, but does her having the one-winged eagle mean our grandfather recognized her as a relative? Hmm.'
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show ange_v001 normal_close at mei_center
 with Dissolve(0.5)
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'This is...'
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...a prototype design for a souvenir manufacturing line from the Ushiromiya family resort... I guess you could say.'
 hide ange_v001
 with Dissolve(0.2)
 show battler_v001 smile at mei_center
 with Dissolve(0.5)
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Oh, so that's what it was. I figured no one would know much about that design in this rural village, though. I don't think Grandfather permits it off the island."
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Ah! It's not like I'm saying Hinamizawa is in a hard to reach, remote countryside! It was just an example..."
 hide battler_v001
 with Dissolve(0.2)
 show miyuki_v002 fuan at mei_left
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'No, no, I get it. ...But I feel like purposefully uttering an excuse like that is much more rude.'
 show miyuki_v002 fuan at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Ah-, true. I messed up and said something unwarranted. I didn't mean to be insensitive. I apologize."
 show battler_v001 fuan_close at inactive
 show miyuki_v002 smile at active
 show miyuki_v002 smile at updown_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ahahaha, it's fine! Battler-san, you're a great guy. I knew that very well even at the time we met."
 show battler_v001 fuan_close at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'But anyway, why are you two at the clinic? Did you get hurt amidst the chaos last night?'
 show miyuki_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "No, no, nothing like that. Nothing in particular is in pain, and I've been healthy all morning."
 hide miyuki_v002
 show jessica_v001 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'No, like... we had the doctor driving us back and forth all night to the hot spring district, and he helped us with a bunch of other stuff, but we never got to thank him up front for all of it.'
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So, we came to formally thank him and say hello, y'know? Do you guys know where he is now?"
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah, if it's Dr. Irie, he's out buying breakfast for us in Okinomiya. I think he should be back any time now, though..."
 hide kazuho_v002
 with Dissolve(0.2)
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "That's a shame. Guess we didn't consider the time all too much."
 show ange_v001 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 show ange_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Huh, you're spacing out. Did the armband talk shock you that much?"
 show battler_v001 normal at inactive
 show ange_v001 sinken at active
 show ange_v001 sinken at jump_transform
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'N-... No!'
 hide ange_v001
 show jessica_v001 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Ah-, sorry. Our grandfather said that crest is a family symbol, so he doesn't allow it being worn out casually, y'know?"
 show jessica_v001 fuan at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Regardless, I think it'd be nice for Hinamizawa to have some sort of famous product like the Ushiromiya family crest. The hot spring can sport it too."
 show jessica_v001 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But that ring... might be the same one that designates the head of the Ushiromiya family... and I feel like I've seen you somewhere before."
 show jessica_v001 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Could I get your name in the meantime?'
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show battler_v001 normal at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Battleeeeer, you've got some nerve spouting some old ass cliche pickup line in front of me like that. I'm telling on you to your dad."
 camera at screenshake_transform
 pause 0.0
 show jessica_v001 sinken at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...W-Wait, wait, Jessica. You're gonna tell that old geezer?! I wasn't flirting with her either! I just felt like I remembered her from somewhere!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide jessica_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show ange_v001 normal_close at mei_center
 with Dissolve(0.5)
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm sorry. I will be leaving."
 play audio 'audio/sfx/SE_530_walk_one.wav'
 hide ange_v001
 with Dissolve(0.6)
 show miyuki_v002 odoroki at mei_left
 with Dissolve(0.5)
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ah, wait... wh-, she left.'
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v002 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Battler-san, you're the worst."
 show nao_v002 normal at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yeah... you're awful today."
 hide nao_v002
 show battler_v001 odoroki at mei_right
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show battler_v001 odoroki at active
 show battler_v001 odoroki at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '......H-...Hey...! Hey, hey, hey, it was a misunderstandiiiiiiiiiiiinggggggg!!!'
 hide miyuki_v002
 show jessica_v001 sinken at mei_left
 with Dissolve(0.5)
 show battler_v001 odoroki at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Shut up, Battler! Did you forget you're at the doctor's office?"
 show battler_v001 odoroki at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Anyways, Battler, if you actually weren't trying to flirt, then you really have seen her before?"
 show jessica_v001 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "No, that's impossible. She should still be 6 years old, it was just a feeling I had because of the similarity."
 show jessica_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'But damn, that girl had a crazy sad look on her face towards the end. Is she okay? We just let her go.'
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 show kazuho_v002 normal at mei_center
 with Dissolve(0.5)
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Um, I'll... be going. Battler-san and Jessica-san, please wait here and catch up with me a bit afterwards."
 play audio 'audio/sfx/SE_408_run.wav'
 hide kazuho_v002
 with Dissolve(0.6)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Wh-, Kazuho...?'
 call chapter_end
 jump chara492001_03