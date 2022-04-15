label chara072017_03:
 show black_background onlayer black
 $ event_store.current_event='chara072017'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072017_03'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 show black_cover as bg
 narrator 'December 24th, nighttime.'
 window hide None
 stop sound
 show expression 'images/bg/AdvBg_1769.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 0.5
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Okay, my fellow new student council members!\nThank you so much for joining us tonight!'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Please release any pent up inhibitions you've had towards the Mass preachings sponsored by the higher-ups at this academy."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "...However, if we get caught, it'd be one terrible development, so I ask of you to quietly have fun."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "That said, I'll give out these crackers now!"
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") "President~! There's no way we can keep silent with crackers, though~?"
 Character('Freshman A',ctc="ctcArrow", ctc_position="fixed") "Um... can I just say, President's voice is way too loud."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Ahh, my bad! Well then, I'll shut my mouth for a while... nom!"
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") "Still... what wonderful decorations! Who did it? It couldn't have been you, President?"
 Character('Sophomore B',ctc="ctcArrow", ctc_position="fixed") '...Of course not. Do you really think a person like her could do such an intricate job?'
 Character('President',ctc="ctcArrow", ctc_position="fixed") '...(Om, nom, nom.)'
 Character('Sophomore B',ctc="ctcArrow", ctc_position="fixed") 'Hey, President! Stop twiddling your thumbs while chewing and just properly explain it to us already.'
 Character('Freshman B',ctc="ctcArrow", ctc_position="fixed") "Right, she stated she'd keep her mouth shut for a while.\n...Will you pantomime for us?"
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'U-Um...'
 hide rika_v021
 with Dissolve(0.2)
 Character('Sophomore B',ctc="ctcArrow", ctc_position="fixed") "Ah, sorry. If I'm not wrong, you two are the pair of first years the president is trying to drag into the student council... Houjou-san and Furude-san... was it?"
 show satoko_v021 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v021 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Y-Yes... so you know us?'
 hide satoko_v021
 with Dissolve(0.2)
 Character('Sophomore B',ctc="ctcArrow", ctc_position="fixed") "Yes. I've heard of you quite a long time ago, Houjou-san, and I've heard of Furude-san's reputation from the girls at the salon."
 Character('Freshman A',ctc="ctcArrow", ctc_position="fixed") "Please do be careful... the president has a habit of never letting the people she likes go, so if you don't want that, you'll have to reject her upfront. It'll be all sorts of trouble otherwise."
 show satoko_v021 fuan_close at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "W-Well, I'm already well aware of that..."
 hide satoko_v021
 with Dissolve(0.2)
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") "You two must have it hard being involved with someone so troublesome. ...Well, we're all in this together, though."
 Character('Sophomore B',ctc="ctcArrow", ctc_position="fixed") "Still, those Santa outfits... they're cute, but don't they expose too much?"
 Character('Freshman B',ctc="ctcArrow", ctc_position="fixed") "Aren't you guys cold exposing so much skin? Are you okay?"
 Character('Sophomore B',ctc="ctcArrow", ctc_position="fixed") "Hey, President. I understand the feeling of wanting them to wear something cute, but you could've at least picked some warmer clothes."
 Character('Freshman A',ctc="ctcArrow", ctc_position="fixed") "She's right; this is almost like a punishment game. What will you do if they catch a cold?"
 Character('President',ctc="ctcArrow", ctc_position="fixed") '...(Chomp, munch, munch).'
 show satoko_v021 sinken at mei_center
 with Dissolve(0.5)
 show satoko_v021 sinken at active
 show satoko_v021 sinken at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I-It's okay, really! We've had the heater on since the time we were getting the room ready, so we're doing fine!"
 hide satoko_v021
 with Dissolve(0.2)
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") 'Huh... then you two are the ones who decorated this room?'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Y-Yes...'
 hide rika_v021
 with Dissolve(0.2)
 Character('Freshman A',ctc="ctcArrow", ctc_position="fixed") 'Ahaha, thank you! Seeing this kind of scenario really makes you get in the Christmas mood~.'
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") "Frantically praying at the chapel just feels more like a religious activity than actually celebrating Christmas after all. It's no different than a funeral."
 Character('Sophomore B',ctc="ctcArrow", ctc_position="fixed") 'Calling the day a saint was born a "funeral"... you really have a foul mouth.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") '...(Omn, mmh, mmm.)'
 Character('Sophomore B',ctc="ctcArrow", ctc_position="fixed") "Yeah, yeah. You don't have to keep yourself from talking any longer. Just keep the volume of your voice in check."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "...Thank you. My mouth was getting so full with words that my cheeks were on the verge of swelling into the shape of a squirrel's."
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") "Still, Houjou-san has such nice style. I definitely wouldn't look good in an outfit like that. The top part would simply fall off from my chest."
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") 'How does this outfit work anyway? Is there some sort of invisible strap holding it up over here...?'
 show satoko_v021 odoroki_blush at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show satoko_v021 odoroki_blush at active
 show satoko_v021 odoroki_blush at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Hyaah! Please don't stroke my back!"
 hide satoko_v021
 with Dissolve(0.2)
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") '............'
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") 'Oh gosh, her scream is so cute...'
 show satoko_v021 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan at active
 show satoko_v021 fuan:
  yanchor 1.0
  linear 0.3333333333333333 pos (970,1200)
 pause 0.3333333333333333
 show satoko_v021 fuan:
  yanchor 1.0
  pos (970,1200)
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Wh-what's with those weird hands coming towards me...!"
 hide satoko_v021
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 Character('Sophomore A',ctc="ctcArrow", ctc_position="fixed") "Hehehe... won't you let your Onee-san hear more of your wonderful screams...?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show satoko_v021 odoroki_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show satoko_v021 odoroki_blush at active
 show satoko_v021 odoroki_blush at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ah... creep! There's a creep over hereeeee!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('Sophomore B',ctc="ctcArrow", ctc_position="fixed") "Hey-... quit it, won't you!"
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v021 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...I didn't know there were people like this at Lucia."
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Didn't expect this?"
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I... thought that everyone at this academy was all quiet and rich and dainty.'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Well, everyone is behaving so they don't stand out too much... but given the opportunity to show who they truly are, they get like this."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "If you two had never gotten involved with the student council, you probably would've never found out about this at all, though."
 stop music fadeout 0.5
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '…………'
 hide rika_v021
 with Dissolve(0.2)
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 Character('President',ctc="ctcArrow", ctc_position="fixed") '...Each human is multifaceted.\nThis includes the built-in parts that cannot be corrected in any way.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Acting out the role of a typical Lucia student, is, in a way, a survival strategy for these girls. To blend in and to behave, to hold your tongue and to hide your fangs.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "But also never letting go of your individual personality and ego. Someone who loses that and becomes a human who can only act according to a manual... they are not an elite or a fine lady... they're merely a robot."
 show rika_v021 sinken_close at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Then does that mean your self-righteous behavior is also a survival strategy...?'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'I just do what I want. I make plenty of contributions at this academy through my grades alone.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "So, wouldn't you think it not unusual for me to demand these privileges and freedoms?"
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'But... what if this Christmas Party becomes an object of criticism?\nNot only will you be held responsible, but these people here will be too...'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I will never let that happen. If there's someone out there trying to hurt what's important to me, I'll be ready to answer with just as much retaliation as you can imagine."
 show rika_v021 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...ah...'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Once you flip the umbrella called "authority" over, you\'ll see the people abusing that umbrella have nothing else to protect themselves.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "...Because they're aware of that, all they can do is stomp their feet in frustration as they watch in silence."
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...President. I now fully understand why I don't like you."
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Yeah...?'
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "No matter what difficulties you face, you're convinced you're supposed to bear all of the sin yourself. In the worst case, you think things will get solved as long as you disappear."
 show rika_v021 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Is it self-sacrificing...? Devotion? No, that's not what it is. You simply don't value yourself as much as you cherish others..."
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "You put on an egotistical front, but you're far from an egotist in reality. To me, that's something that I just can't..."
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") '...I see. So there was someone important to you that bore all sin and disappeared, then...?'
 show rika_v021 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 show rika_v021 fuan at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Please do not try prying into people's lives like that."
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Oh, sorry. I see, though...\nIt's Christmas, and yet I made you remember something sad. ...My fault."
 show rika_v021 fuan_close at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...And the way you admit your sins so easily too...\nI just can't come to like it."
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Sorry about that... but, yeah. I don't think I can speak for the person that's important to you, but..."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Rather than believing that this person you lost is only thinking about themselves and suffering... know that they likely wish for you to life your life fruitfully.'
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I also have someone who's important to me. ...If I'm being honest with my heart, I'd rather return to them than be at such a closed-off academy."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "But if I just returned now, they'd be worried for me. So I just make it so I have stories to deliver to them. This party is also one of those."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Also... Houjou-san is a very faithful girl. No matter how much she's fawned over by people around her, she'll always come back to your side."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I understand that you feel lonely when she's away from you... but I feel as though you should wait and watch her grow."
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What in the world are you? Why do you care so much about--...'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "That's..."
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "If you say it's because you and Satoko are alike... I'll genuinely get angry even if it's a joke, you understand me?"
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "No, I won't say that. I don't want our Christmas to become a bloodbath, after all."
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "You make it sound like I'm evil..."
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Oh, an ornament is falling... I'll go fix the Christmas tree."
 hide rika_v021
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/card/Card_072017.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'There you go...... ah...'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's snowing... we're having a White Christmas."
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(It's so pretty... but...)"
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(Every time the snow started falling, Satoko was always by my side...)'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(I feel a little bit lonely...)'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1769.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show satoko_v021 smile at mei_center
 with Dissolve(0.5)
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Oh my... it's snowing!"
 hide satoko_v021
 with Dissolve(0.2)
 show rika_v021 odoroki at mei_left
 show satoko_v021 smile at mei_right
 with Dissolve(0.5)
 show satoko_v021 smile at inactive
 show rika_v021 odoroki at active
 show rika_v021 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah? S-Satoko...?'
 show rika_v021 odoroki at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Why are you so startled? I brought the juice for the cheers.'
 show satoko_v021 normal at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Th-thank you...'
 show satoko_v021 normal at inactive
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Hey, Satoko.'
 show satoko_v021 normal at active
 show rika_v021 sinken at inactive
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "What is it? If it's about the Christmas present, I'll bring it later."
 show satoko_v021 normal at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Yes, thank you. ...By the way, I have a present for you too.'
 show satoko_v021 normal at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'So... why don’t we sneak out of the party later and secretly exchange presents, just the two of us?'
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That sounds great. Let's do that."
 show satoko_v021 smile at inactive
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But... is it okay? The student council's upperclassmen seemed to be doting on you, so I thought they'd want you to stay here until the end."
 show rika_v021 odoroki at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If we exchange presents here, everyone will see the present you have for me, and they'd start messing around again."
 show rika_v021 odoroki at inactive
 show satoko_v021 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "And... I want to be the only one who opens and enjoys the present you're giving me... ♪"
 show satoko_v021 smile_close at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "*giggle*... you're right. We can't have a mood or anything else going on if there's people toying with us."
 show rika_v021 smile at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Right? Those upperclassmen aren't thoughtful at all!"
 show satoko_v021 sinken at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "*chuckle*... Ah, Satoko, your hair is messy.\nI'll fix it for you, so crouch down a little."
 play audio 'audio/sfx/SE_5037_getup.wav'
 show rika_v021 smile at inactive
 show satoko_v021 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...It's been a while since you've last caressed my head like this."
 show satoko_v021 smile_close at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Sure has...'
 hide satoko_v021
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Alright, alright, lovebirds. Don't get stuck in your own little world of two over by that window and come cheer with us again."
 show satoko_v021 smile at mei_center
 with Dissolve(0.5)
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yes, be there soon~!'
 hide satoko_v021
 with Dissolve(0.2)
 show rika_v021 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Does that person enjoy interrupting us right at the good part?'
 hide rika_v021
 with Dissolve(0.2)
 show satoko_v021 odoroki at mei_right
 show rika_v021 normal_close at mei_left
 with Dissolve(0.5)
 show rika_v021 normal_close at inactive
 show satoko_v021 odoroki at active
 show satoko_v021 odoroki at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show satoko_v021 odoroki at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's nothing. Let's go, Satoko."
 hide rika_v021
 hide satoko_v021
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 pause 0.5
 show black_cover as bg
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Well then, everyone...'
 play audio 'audio/sfx/SE_305_ls_cracker.wav'
 Character('Rika and Satoko',ctc="ctcArrow", ctc_position="fixed") 'Merry Christmas!'
 call chapter_end
 
 $ persistent.chara072017_done = True
 return