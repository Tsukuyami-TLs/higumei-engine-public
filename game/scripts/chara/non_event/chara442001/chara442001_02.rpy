label chara442001_02:
 show black_background onlayer black
 $ event_store.current_event='chara442001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara442001_02'
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
 show expression 'images/bg/AdvBg_220.png' as bg
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v001 fuan at mei_right
 show eua_v001 smile at mei_left
 with Dissolve(0.5)
 show eua_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'U-Uh... u-um...'
 show eua_v001 smile at inactive
 show satoko_v001 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '(I know this person’s name... and I’ve met her somewhere before...)'
 show eua_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '(But I can’t remember anything other than that...\nWhy? Just who is this person...?)'
 show satoko_v001 fuan at inactive
 show eua_v001 smile_close at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") '*chuckle*... at rest, child of man. Do not force yourself to resurface your memories, as this will not matter at all.'
 show satoko_v001 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") "Since I discovered the “Fragment” to this “World” drifting along, I decided I'd simply drop by out of boredom."
 show eua_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...wh-...?'
 show satoko_v001 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'I simply got excited and called out to you since you were here.'
 show satoko_v001 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'I did not have much confidence that I could connect our minds... but how pleasant. So such derivations can exist once the “Link” has been established.'
 show eua_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I... I don’t really understand what you’re saying.\nJust what business do you have with me?'
 show satoko_v001 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Oh, loosen up. I do not intend to alter your "World" as it is now.'
 show satoko_v001 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Until now, I have been spectating various fragments to distract me from my boredom.'
 show satoko_v001 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Nonetheless, hearing your conversation has slightly piqued my interest.'
 show eua_v001 smile at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...I don’t really get the meaning of this conversation. What do you mean?'
 show satoko_v001 normal at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Had you not said it yourself earlier? How eating something while spectating could be fun?'
 show satoko_v001 normal at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") "What gets eaten while spectating clearly holds the same level of importance as one's enjoyment of its plot events."
 show satoko_v001 normal at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'I have snacked on sweets in between sips of tea, but of course, I have tired of that. Therefore, child of man, it would be grand if you could fetch me something.'
 show eua_v001 smile at inactive
 show satoko_v001 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Something... like, you want something to eat?\nWell, that’s... sort of no problem, but...'
 show eua_v001 smile at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Anyway, E-... Eua-san, what kind of food would you like? Although what I bring likely won't meet up to your standards."
 show satoko_v001 normal at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'As for me, the concept of pickiness has long disappeared in the past; ergo, what I ask is that you surprise me with an exciting product.'
 show eua_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'It feels like something is off when you ask me to get some food to surprise you... but okay.'
 show eua_v001 smile at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Just... in the case that what I think of bringing isn’t the correct choice, please do not complain.'
 show satoko_v001 normal at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'I am not so sure about that.\nCuring me of my illness of boredom is your role.'
 show satoko_v001 normal at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'In the event that my task for you is carried out well, you will be praised. Otherwise, you will receive a fitting punishment.\nAs such, I encourage you to do your best, child of man--'
 show eua_v001 smile at inactive
 show satoko_v001 odoroki at active
 show satoko_v001 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ah, ple-... please wait just a moment...!'
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_81.png' as bg
 hide eua_v001
 with Dissolve(0.2)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v001 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '*sigh*... I have an impossible challenge on my hands, don’t I?'
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '(But for some reason, I can’t go against that person’s orders...\nWhy could that be...?)'
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show rika_v001 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v001 fuan at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...? What happened, Satoko? You got quiet all of a sudden, so I've been worried about you."
 show rika_v001 fuan at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...It's nothing. I was just sorting out a few thoughts that came to mind, so please don't get worked up over it."
 show rika_v001 fuan at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'By the way, Rika... I would like everyone to lend me their ears now.'
 show rika_v001 fuan at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'If you could eat or drink anything while appreciating a movie, what would it be?'
 hide rika_v001
 show kazuho_v001 odoroki at mei_left
 with Dissolve(0.5)
 show satoko_v001 normal at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wh-... what is this all of a sudden?'
 show kazuho_v001 odoroki at inactive
 show satoko_v001 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Just as I've stated before, it was just something that crossed my mind. Please do answer if you can."
 hide kazuho_v001
 show miyuki_v001 smile at mei_left
 with Dissolve(0.5)
 show satoko_v001 normal_close at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, good question. ...Popcorn is a safe answer. It doesn't make noise while you're chewing it, so it doesn't hinder your appreciation of the movie at all."
 show miyuki_v001 smile at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "(Popcorn... is too conventional, so I feel like she won't accept that from me.)"
 hide miyuki_v001
 show kazuho_v001 smile at mei_left
 with Dissolve(0.5)
 show satoko_v001 normal at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I'll say... how does onigiri or something sound?"
 hide satoko_v001
 show nao_v001 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v001 smile at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's just something you like, Kazuho."
 show nao_v001 fuan at inactive
 show kazuho_v001 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "B-But that doesn't make any noise when you eat it either, right?!"
 hide nao_v001
 show rena_v001 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v001 sinken at inactive
 show rena_v001 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... I think the sound of someone eating onigiri is pretty easy to recognize.'
 show rena_v001 fuan at inactive
 show kazuho_v001 fuan at active
 show kazuho_v001 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah-... really...?'
 hide rena_v001
 show mion_v001 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v001 fuan at inactive
 show mion_v001 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "What about potato chips?\nThose make noise though, so you'd get restricted to watching at home."
 hide kazuho_v001
 show rika_v001 smile at mei_left
 with Dissolve(0.5)
 show mion_v001 smile at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. It's a staple for home film appreciation."
 hide mion_v001
 hide rika_v001
 with Dissolve(0.2)
 show miyuki_v001 smile at mei_left
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v001 normal at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ah, what about dried squid flakes or fried stingray?\nThey don't make noise {i}and{/i} they have long-lasting flavor!"
 show miyuki_v001 smile at inactive
 show nao_v001 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...You sound like a grandpa, Miyuki.'
 show nao_v001 fuan_close at inactive
 show miyuki_v001 fuan at active
 show miyuki_v001 fuan at chara_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Gaah...?!'
 hide nao_v001
 hide miyuki_v001
 with Dissolve(0.2)
 show hanyuu_v001 smile at mei_left
 show satoko_v001 normal at mei_right
 with Dissolve(0.5)
 show satoko_v001 normal at inactive
 show hanyuu_v001 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, I think sweets would be nice~!'
 show hanyuu_v001 smile at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Sweets... like juice?'
 show satoko_v001 normal at inactive
 show hanyuu_v001 fuan_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Umm, juice is good too, but something with more volume, like... aha!'
 show satoko_v001 normal at inactive
 show hanyuu_v001 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Cream puffs...? Wouldn't cream puffs fit perfectly for watching a movie?!"
 hide satoko_v001
 show nao_v001 fuan at mei_right
 with Dissolve(0.5)
 show hanyuu_v001 odoroki at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Again, that's just what you like, Hanyuu."
 show nao_v001 fuan at inactive
 show hanyuu_v001 sinken at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au au~! Then what do you think would be good, Nao?'
 show hanyuu_v001 sinken at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Right... how about churros, I wonder?'
 hide hanyuu_v001
 show satoko_v001 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show satoko_v001 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Chew rows...?'
 hide satoko_v001
 show miyuki_v001 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show miyuki_v001 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Churros, like those churros?'
 hide nao_v001
 show rena_v001 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v001 odoroki at inactive
 show rena_v001 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Miyuki-chan, you know about them?'
 show rena_v001 smile at inactive
 show miyuki_v001 smile at active
 show miyuki_v001 smile at nod_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Yeah. I bought them at a donut shop in Tokyo once.'
 hide miyuki_v001
 hide rena_v001
 with Dissolve(0.2)
 show satoko_v001 normal at mei_left
 show nao_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show satoko_v001 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'What kind of food is that?'
 show satoko_v001 normal at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "A variety of donut. If I'm correct, they insert the batter into a piping bag, squeeze the batter out, and then deep fry it like that."
 hide satoko_v001
 show miyuki_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "They're long, narrow, crispy, and overall delicious! The ones I had were circular-shaped, but it looks like there are ones that are rod-shaped too?"
 show miyuki_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I had some when I went to an amusement park.\nThat reminds me, I've heard from some friends that they're selling them at movie theaters now too."
 hide miyuki_v001
 show mion_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show mion_v001 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Really? Mm, I don't remember seeing them in all the times I went to the movie theater in Gogura, though... so they are different from the ones in Tokyo, I'm guessing?"
 show mion_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I have no idea if those are limited to Tokyo... but the sound it makes while you eat it won't be bothersome, and it seems like it's a popular snack in its own right."
 hide mion_v001
 show hanyuu_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show hanyuu_v001 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, it sounds tasty!\nI also want to try, um... those churros as a snack sometime~!'
 hide hanyuu_v001
 show satoko_v001 fuan at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Can you make those easily...?'
 show satoko_v001 fuan at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh...? Well, I feel it wouldn’t take too long to make, but as for a detailed recipe...'
 hide nao_v001
 show miyuki_v001 smile at mei_right
 with Dissolve(0.5)
 show satoko_v001 fuan at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Maybe you can make them using a recipe for donuts. Wanna eat some?'
 show miyuki_v001 smile at inactive
 show satoko_v001 smile at active
 show satoko_v001 smile at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Y-... yes! I'd absolutely love to try it!"
 show satoko_v001 smile at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Why don't we try making some after school then?\nSorry, Rena, but would you mind helping?"
 hide satoko_v001
 show rena_v001 smile_blush at mei_left
 with Dissolve(0.5)
 show miyuki_v001 smile at inactive
 show rena_v001 smile_blush at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Not at all! Hau~, I wonder if these churros are cute, are cute?'
 hide miyuki_v001
 hide rena_v001
 with Dissolve(0.2)
 show satoko_v001 smile_close at mei_center
 with Dissolve(0.5)
 show satoko_v001 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '(Hoh...)'
 hide satoko_v001
 with Dissolve(0.2)
 show rika_v001 smile at mei_right
 show satoko_v001 smile_close at mei_left
 with Dissolve(0.5)
 show satoko_v001 smile_close at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. It's rare to see Satoko wanting to eat something sweet this much."
 show rika_v001 smile at inactive
 show satoko_v001 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Th-that's... um..."
 show rika_v001 smile at inactive
 show satoko_v001 smile at active
 show satoko_v001 smile at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Of course I'd want to! There's no way I could ever dislike sweet things as a girl! Ohohoho!"
 show satoko_v001 smile at inactive
 show rika_v001 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Meep...?'
 call chapter_end
 jump chara442001_03