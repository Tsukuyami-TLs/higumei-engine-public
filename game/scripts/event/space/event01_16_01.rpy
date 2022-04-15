label event01_16_01:
 show black_background onlayer black
 $ event_store.current_event='space'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_16_01'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_1390.png' as bg
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "So you're saying we died a thousand years ago... and came back to life...?"
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'That premise sounded so cliché and absurd that it made me want to laugh... so taking it seriously was beyond reasoning.'
 narrator "However, amidst the detached and composed nature of Maebara-kun and Rika-chan's (?) expressions... I couldn't detect any sense of them intending to joke around."
 narrator 'So then... maybe they really... are telling the truth...?!'
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Qu-...quit the jokes! Did you really think I'd believe it if you suddenly told me I died and came back?!"
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'N-Nao-chan...'
 hide nao_v002
 hide rena_v002
 with Dissolve(0.2)
 narrator "Nao-chan's small body was trembling and quivering in fear, so {i}squeeze{/i}, Rena-san hugged her from behind."
 narrator "I think it's amazing that Nao-chan was able to respond with her true feelings like that. ...Meanwhile, I was too stunned to speak."
 show keiichi_v007 normal at mei_right
 with Dissolve(0.5)
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Ah... I understand what you guys are feeling, but this isn't a matter of believing or not. Every last detail really is the truth."
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show keiichi_v007 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Wha-...?!'
 hide keiichi_v007
 show rika_v012 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show rika_v012 normal at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep. There were approximately two-thousand cases in which the DNA of the former living species was put to trial in attempt to resurrect humans into the present. Of those cases, only six were successful....'
 show nao_v002 sinken at inactive
 show rika_v012 normal at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'That is to say, you six.'
 hide nao_v002
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v012 normal at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Two-thousand... wait a minute, you mean every person in Hinamizawa died in that great disaster?'
 hide rika_v012
 show keiichi_v007 normal at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "...No, not just you guys. It's likely safe to say most of humanity went extinct during that great disaster on Earth back then."
 show shion_v002 fuan at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "And we're the descendants of those who narrowly escaped."
 show shion_v002 fuan at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'By the way, you all said "Keiichi Maebara" just now... right?\nHe\'s a complete stranger to us. I\'m counting on you to understand.'
 hide shion_v002
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show keiichi_v007 smile at inactive
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...ack...!'
 hide keiichi_v007
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'That cruel truth hits me like a sharp blow to the head... and I start feeling faint.'
 narrator "I wanted to believe it was some kind of a joke.\nI'd probably feel much better if I was told it was all a bad dream..."
 show miyuki_v002 sinken at mei_left
 with Dissolve(0.5)
 show miyuki_v002 sinken at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "You... definitely can't be Maebara-kun.\nHe would never treat women violently, no matter the reason."
 show miyuki_v002 sinken_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "I'll believe you for now. But... unlike Maebara-kun, you seem like someone I'll come to dislike, honestly."
 show keiichi_v007 futeki at mei_right
 with Dissolve(0.5)
 show miyuki_v002 sinken_close at inactive
 show keiichi_v007 futeki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Heh, when you put it like that, it makes me feel a little lonely... well, do as you like.'
 show miyuki_v002 sinken_close at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'By the way, Lady Meep, did you find any trace of this "Keiichi Maebara"?'
 hide miyuki_v002
 show rika_v012 fuan at mei_left
 with Dissolve(0.5)
 show keiichi_v007 normal at inactive
 show rika_v012 fuan at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") "Meep. I seem to have discovered that person's DNA; however, it is much too damaged."
 hide keiichi_v007
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v012 fuan at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Keiichi-kun, no...'
 hide rika_v012
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'So then, was it also impossible to revive Rika, um... "Rika Furude"?'
 hide rena_v002
 show keiichi_v007 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show keiichi_v007 odoroki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Mm... "Rika Furude"?\nThat name wasn\'t on the list...'
 show satoko_v002 fuan at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "And the fact of whether or not we have a specimen here isn't something we would mistake."
 hide satoko_v002
 show rika_v012 normal_close at mei_left
 with Dissolve(0.5)
 show keiichi_v007 normal at inactive
 show rika_v012 normal_close at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep. Thousands of DNA samples were collected, but around 70%% of them were unidentifiable... and most of what remained could not be resurrected.'
 show keiichi_v007 normal at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Nonetheless, being able to revive six people after one-thousand years have passed is such a miraculous feat that it makes me want to rejoice.'
 hide keiichi_v007
 hide rika_v012
 with Dissolve(0.2)
 narrator 'Rika-chan — I mean, "Lady Meep" — says that while proudly sticking out her chest.'
 narrator "We didn't feel very joyful, however...\nI did my best to keep my dark thoughts and discomfort bordering on frustration sealed off within my heart."
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'H-Hau... but those two seriously do look so similar to Keiichi-kun and Rika-chan...'
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Definitely. It's a bit difficult to think of them as different people, isn't it?"
 hide rena_v002
 show keiichi_v007 normal at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Mmm, well, maybe I do have an ancestor from the distant past that I resemble... and their phenotypic genes could've taken over by coincidence."
 show shion_v002 fuan at inactive
 show keiichi_v007 sinken at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "But as I said a bunch of times, I don't know you guys at all, and I don't remember us being friends. That alone should be crystal clear."
 show keiichi_v007 sinken at inactive
 show shion_v002 fuan at inactive
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") '...nn...'
 hide shion_v002
 hide keiichi_v007
 with Dissolve(0.2)
 narrator 'Maebara-kun — or rather, "K-1" — has an unpleasantly stern look as he asserts that.'
 narrator "Apparently, this person has no intention of befriending us. ...I can't help but feel lonely since that face looks so much like his."
 show mion_v002 sinken at mei_center
 show mion_v002 sinken at chara_shake_transform:
  yanchor 1.0
  linear 0.5 pos (960,1200)
 with Dissolve(0.5)
 show mion_v002 sinken:
  yanchor 1.0
  pos (960,1200)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ngh... I more or less understand the situation, but I still don't exactly feel like I have enough information."
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "It's just, could you go into some more detail about this great disaster thing...?"
 show shion_v002 odoroki at mei_right
 show mion_v002 sinken
 show mion_v002 sinken:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 with Dissolve(0.5)
 show mion_v002 sinken:
  yanchor 1.0
  pos (480,1200)
 show mion_v002 sinken at inactive
 show shion_v002 odoroki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah-... Sis.\nWow, you're already standing up?"
 hide shion_v002
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Mi-Mii-chan... I wonder if you're okay standing up like that, like that?"
 show rena_v002 fuan at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yup, it was no problem.\n...And besides, you can't lay down the whole time you're in the middle of a crisis, y'know?"
 hide mion_v002
 hide rena_v002
 with Dissolve(0.2)
 narrator '...Despite her hearty reply, Mion-san grimaced painfully.'
 narrator 'Even so, she stepped forward to protect us... standing before K-1 and Lady Meep.'
 show rika_v012 smile at mei_right
 with Dissolve(0.5)
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'So then, Mion Sonozaki, what would you like us to explain for you?'
 show mion_v002 sinken at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Of course, the time period we were alive was... 1983.\nI want to know what happened not just in Hinamizawa, but with the entire world.'
 show rika_v012 smile at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "You revived us to your own convenience, so no matter how you explain yourselves, isn't this way too selfish of an action?"
 hide mion_v002
 show miyuki_v002 sinken at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show miyuki_v002 sinken at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "What Mion said.\nIf I'm going to listen to you guys from now on, I'm for sure gonna need some follow-up."
 show miyuki_v002 sinken at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") "Meep, that is a valid request.\n...K-1, if we are to obtain these girls' cooperation, we must educate them properly."
 hide rika_v012
 show keiichi_v007 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v002 sinken at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Alright, got it.\nCould everyone turn their attention here?'
 hide miyuki_v002
 hide keiichi_v007
 with Dissolve(0.2)
 narrator 'As K-1 said that, {i}fwip{/i}, he raised his hand, and a 3D screen appeared in the air.'
 narrator "However this thing was constructed, I had no idea. But within the screen, there was a vividly-projected bird's-eye view of the Hinamizawa that I was familiar with."
 show keiichi_v007 normal at mei_right
 with Dissolve(0.5)
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'First of all... I was told that a poisonous gas disaster happened at this location a thousand years ago... but do any of you know what happened?'
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show keiichi_v007 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A... a volcanic... gas disaster...?!'
 show kazuho_v002 odoroki at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Hoh...? The records are so old that {i}I{/i} don't even know the full details... but if you have memories of the event, that makes the explanation faster."
 show kazuho_v002 odoroki at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'So, that seeped through the entire area...\nAnd the people who lived in the vicinity died without knowing it was happening...'
 show kazuho_v002 odoroki at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Some of those victims happened to be you guys.'
 show keiichi_v007 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...gh...?!'
 show kazuho_v002 fuan at inactive
 show keiichi_v007 normal_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'After that, the volcanic gas flow spread to outside towns and cities, and then overseas to foreign lands...'
 show kazuho_v002 fuan at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "As a result, Earth's population plummeted to just tens of thousands in two to three years."
 hide kazuho_v002
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show keiichi_v007 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Wait... no way; something like that can't...?! No matter how much poisonous gas there is, it couldn't possibly have spread that much, could it?!"
 show nao_v002 sinken at inactive
 show keiichi_v007 normal_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "You can ask all you want, but I wasn't there, you know?\nI'm just retelling the facts we have recorded."
 show keiichi_v007 normal_close at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...nnh...!!'
 show nao_v002 sinken at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'So, the people who survived abandoned Earth since it was a dead planet, and sailed off into space to find a new home.'
 show nao_v002 sinken at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "I'm a descendant of those Earthlings."
 hide keiichi_v007
 show rika_v012 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep. And I am an android created to support K-1. Nipah~♪'
 hide nao_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'S-Sure...'
 hide rika_v012
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "Even if she calls herself an android... she doesn't look much different than a human, so I don't know how to respond."
 narrator "But I felt that if I asked any more questions, I'd be interrupting the explanation, so I chose to keep quiet and let it slide."
 show rika_v012 smile at mei_right
 with Dissolve(0.5)
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") '...Well then, everyone. Have the details been made more clear with this new explanation?'
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...It's too big in scale, or rather, too far beyond my imagination, so I feel like it's hard to understand..."
 hide rika_v012
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Well, I guess that's a given.\nSo you don't have to understand, or even agree."
 show kazuho_v002 fuan at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "But... this is the truth.\nWith that in mind, it'd save us trouble if you listened to what we told you from now on."
 hide kazuho_v002
 show mion_v002 normal_close at mei_left
 with Dissolve(0.5)
 show keiichi_v007 normal at inactive
 show mion_v002 normal_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Yeah, yeah, I got it.\nI'd prefer not to get zapped again."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide keiichi_v007
 hide mion_v002
 hide fade onlayer curtain
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But still... why were we brought back to life again ultimately?\nI won't let you do anything else until that gets explained."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Well, it's simple. The Environment Protection Coalition's job is to restore environmental ruins and bring back extinct animals."
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "And this time, we're working on a big project: bringing humanity back to life. That's where you guys come in."
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show keiichi_v007 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "U-Uuum... so you're saying we're being treated like an extinct species...?"
 show satoko_v002 fuan at inactive
 show keiichi_v007 smile at active
 show keiichi_v007 smile at nod_transform
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "In layman's terms, yeah.\nJust enjoy your second life to the fullest as if you won the lottery."
 hide satoko_v002
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show keiichi_v007 smile at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'H-Hau... when you get told that you and everyone you knew died, parting with your former live feels... very...'
 hide keiichi_v007
 show rika_v012 smile at mei_right
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep, none of you have the right to complain. When we resurrected you, we implanted microcomputers inside of you all to ensure complete obedience.'
 hide rena_v002
 show miyuki_v002 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'M-Microcomputers?\nWhat do you mean by—unyuu?!'
 show miyuki_v002 odoroki at jumping_transform
 hide rika_v012
 hide miyuki_v002
 with Dissolve(0.2)
 narrator 'When Lady Meep raised her hand, Miyuki-chan started speaking in a strange way. And then...'
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Mi-...Miyuki, are you okay? Get a hold of—unyuu?'
 show nao_v002 odoroki at jumping_transform
 hide nao_v002
 with Dissolve(0.2)
 narrator 'When Nao-chan tried to rush over to Lady Meep, Lady Meep pointed her finger towards Nao, who started speaking in a strange voice.'
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Mi-Miyuki-chan... Nao-chan...?!'
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show miyuki_v002 fuan at active
 show miyuki_v002 fuan at leftright_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Unyu...? Ukyukyukyu, kyukyuu?!'
 hide miyuki_v002
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show nao_v002 fuan at active
 show nao_v002 fuan at leftright_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ukkyuu! Kyukyukyu, kyuuuuuu?'
 show nao_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Wh-what's happening to you...?"
 show kazuho_v002 fuan at inactive
 show nao_v002 fuan at active
 show nao_v002 fuan at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Kyukyu! Kyukyukyu~!'
 hide nao_v002
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show miyuki_v002 fuan at active
 show miyuki_v002 fuan at chara_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Kyuuuuu, ukyukyuu!'
 hide kazuho_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator '...No matter what I try asking, the only replies are strange cries and sounds. The expressions on their faces are too real to think it was a prank.'
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Hol-... stop! Change them back!'
 show rika_v012 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep, there is no need to worry.\nI have temporarily changed their language from Japanese to Rabbitese.'
 hide kazuho_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Did rabbits ever make this sound?'
 show shion_v002 normal at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'We also have Turtlese, Crocoese, and Water-striderese.\n...Would you like to try one?'
 hide shion_v002
 show satoko_v002 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Water strider noises?\nI kinda want to hear what that sounds like...'
 hide rika_v012
 show miyuki_v002 sinken at mei_right
 with Dissolve(0.5)
 show satoko_v002 odoroki at inactive
 show miyuki_v002 sinken at active
 show miyuki_v002 sinken at jumping_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'KyuKYUUUUUU!!'
 show miyuki_v002 sinken at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I-It's just a joke, Miyuki-san!\n...Wait, she's even moving like a rabbit, isn't she?!"
 hide miyuki_v002
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Oh, don't worry. This is just an emergency measure; it isn't meant to cause them harm."
 hide satoko_v002
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 show keiichi_v007 smile at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 hide keiichi_v007
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "K-1 says that while smiling, but I certainly can't take it at face value."
 narrator 'It felt like a declaration that they could fix it whenever they wanted, but only if they felt like it...'
 show keiichi_v007 smile_close at mei_right
 with Dissolve(0.5)
 show keiichi_v007 smile_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Well, not much point thinking about it negatively.\nDon't you feel like crying tears of joy now that you can resume your life right from when it suddenly ended?"
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 show keiichi_v007 smile_close at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 hide keiichi_v007
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "...I wonder why. But I couldn't help but feel frustrated, or rather, disgusted at this K-1, who was nothing like Maebara-kun..."
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Anyways, we'll be informing you some more soon.\nGet some rest for now."
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Let's go, Meep."
 show rika_v012 smile at mei_left
 with Dissolve(0.5)
 show keiichi_v007 smile at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Yes, understood.\nWell then, everyone, we shall meet again.'
 play audio 'audio/sfx/SE_540_footstep.wav'
 hide keiichi_v007
 hide rika_v012
 with Dissolve(0.2)
 narrator 'After saying that, K-1 and Lady Meep turned around... and vanished through the wall.'
 narrator "Even after they were gone, we were stunned and couldn't move an inch..."
 call chapter_end
 jump event01_16_02