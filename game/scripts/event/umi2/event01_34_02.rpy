label event01_34_02:
 show black_background onlayer black
 $ event_store.current_event='umi2'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_34_02'
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
 show expression 'images/bg/AdvBg_2491.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v002 smile at mei_left
 show hanyuu_v002 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Hmph, that takes care of that. There were quite a bit of them, but they didn't put up much of a fight."
 show satoko_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'They were a lot easier to deal with than usual~.\n...That said......'
 show hanyuu_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yeah, aside from that... Rika is...'
 hide hanyuu_v002
 hide satoko_v002
 with Dissolve(0.2)
 window hide None
 camera:
  parallel:
   linear 0.5 pos (960, 490)
  parallel:
   linear 0.5 zoom 1.5
 pause 0.5
 show rika_v023 fuan at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_378_ls_cutepose.wav'
 pause 1.0
 camera:
  parallel:
   linear 1.0 pos (960, 590)
  parallel:
   linear 1.0 zoom 1.5
 pause 1.0
 pause 1.0
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Meep.'
 hide rika_v023
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_left
 show rika_v023 fuan at mei_right
 with Dissolve(0.5)
 show rika_v023 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ri-...... Rika-chan, what is that outfit?'
 show kazuho_v002 fuan at inactive
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I don't know either. I used my {b}Role Card{/b} as usual, and then this happened."
 hide rika_v023
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'As Rika-chan said this, bobbing up and down on her head were... rabbit ears.'
 narrator "Even I thought they looked pretty cute. \nThat's when--"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rena_v002 smile_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show rena_v002 smile_blush at active
 show rena_v002 smile_blush at chara_shake_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") '...H-Hauuu~~♪♪'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rena_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "Yep, there's no way Rena-san wouldn't react to it!"
 show mion_v002 odoroki at mei_right
 show miyuki_v002 sinken at mei_left
 with Dissolve(0.5)
 show miyuki_v002 sinken at inactive
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'H-Hey, Rena, calm down!!'
 show mion_v002 odoroki at inactive
 show miyuki_v002 sinken at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Break it up, time out! Your face is practically melting!!'
 hide miyuki_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator "Drool seeped from Rena-san's mouth as she approached Rika-chan... \nMion-san and Miyuki-chan tried to stop her."
 narrator 'Maebara-kun also ran over to help, but Rena-san sent him rolling to the ground with a flurry of punches... How unfortunate.'
 show kazuho_v002 fuan at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "W-What is going on? ...Nao-chan, what's with the serious look?"
 show kazuho_v002 fuan at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Oh, it's nothing. Somehow I feel like I've seen Rika's clothes before."
 show kazuho_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Anyway, is {i}he{/i} alright?'
 show nao_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah, that's right. Battler-san, are you okay?"
 stop music fadeout 0.5
 hide nao_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show battler_v001 normal at mei_center
 with Dissolve(0.5)
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 hide battler_v001
 with Dissolve(0.2)
 narrator 'I turned to look at Battler-san, but he was staring at me with a dumbfounded look on his face.'
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Um, hello...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide fade onlayer curtain
 show battler_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "H-Hey, hey, what's going on here? What are those cards? Did you just... transform and fight?"
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'W-What the hell was all that...?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show keiichi_v002 fuan at mei_left
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Uh... are you okay?'
 show keiichi_v002 fuan at inactive
 show battler_v001 odoroki at active
 show battler_v001 odoroki at jump_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Uoooh?!'
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide battler_v001
 hide keiichi_v002
 with Dissolve(0.2)
 narrator 'When Maebara-kun called out to him again, Battler-san finally stood up and shook his body, as if he had come to his senses.'
 show battler_v001 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Y-Yeah... thank you. Thanks to you... I'm... safe...?"
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'No, what was that earlier?!'
 show battler_v001 sinken at active
 show battler_v001 sinken at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I've never seen those animals before... wait, were they animals or monsters?! No, are those even {i}living creatures{/i} in the first place?!"
 show battler_v001 sinken_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm not dreaming right now, am I?! I just came to inspect the resort with Jessica... but the bus never came at all..."
 camera at screenshake_transform
 pause 0.0
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'This is all real, right? Right?!'
 hide battler_v001
 with Dissolve(0.2)
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.5)
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'W-Well... maybe you should listen to me for a bit...'
 hide keiichi_v002
 with Dissolve(0.2)
 narrator 'Battler-san originally seemed like a composed young man.'
 narrator 'But that guy kept trying to press Maebara-kun for answers with a perplexed face.'
 show nao_v002 normal at mei_right
 show kazuho_v002 normal at mei_left
 with Dissolve(0.5)
 show kazuho_v002 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Something about his reaction seems familiar.'
 show nao_v002 normal at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Yeah. \nWe felt that in the beginning too...'
 hide kazuho_v002
 hide nao_v002
 with Dissolve(0.2)
 show battler_v001 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan at active
 show battler_v001 fuan at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Wh-what the hell?! You're telling me those things are so common that even little girls find them normal?!"
 show battler_v001 sinken_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Never in my life have I ever seen these... whatever they are...!'
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Even assuming they were imaginary since they disappeared without a trace, that fight looked like it would cause some serious damage... \nBut then...?'
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show battler_v001 sinken at active
 show battler_v001 sinken at jump_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'What about Jessica?! Is Jessica alright?!! She must be all alone now!!'
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Seriously, thank you all so much for rescuing me! But now I need to go find my cousin...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rena_v002 fuan at mei_center
 with Dissolve(0.5)
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "H-Hau... please calm down! Every time this has happened up until now, they've only popped up in one place, so I think it'll be fine, okay?"
 hide rena_v002
 with Dissolve(0.2)
 narrator 'In the heat of the situation, even Rena-san was so worried about Battler-san that she shut off her Kyute Mode.'
 narrator "I could tell he grasped the situation somehow, but maybe he's just a little impatient...?"
 show nao_v002 fuan at mei_right
 show miyuki_v002 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Well, that is a natural reaction for someone with regular common sense and values.'
 show nao_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, in any case, we've culled them all for now.\nI'm sure they'll contact us if anything happens in the hot springs, so why not relax?"
 show nao_v002 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "And besides, this place is pretty deep in the mountains. If any bears, boars, or other wild animals appeared, it wouldn't be that strange, right?"
 hide nao_v002
 show battler_v001 odoroki at mei_right
 with Dissolve(0.5)
 $ event_store.current_progress = 1
 show miyuki_v002 smile at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Don't tell me you're treating them like you would a bear or a boar?! Seriously... they felt like monsters out of the {note_green}Demon Parade{/note_green} to me..."
 hide miyuki_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 odoroki at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...kh...'
 hide battler_v001
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'I felt a pain in my chest, and I accidentally let out a pained noise as I tried to catch my breath.'
 narrator "But Demon Parade... that is pretty accurate. Any regular person who saw {b}Tsukuyami{/b} wouldn't consider them normal."
 show battler_v001 odoroki at mei_right
 with Dissolve(0.5)
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "What the hell happened in this village that made kids start fighting like it's a sport?!"
 show satoko_v002 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 odoroki at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's a wonderful activity once you get used to it! If it's fine with you, would you like to join in?"
 show satoko_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'That actually sounds kinda tempting. To be honest, that transformation scene awakened the male instincts inside me! Transforming is pretty epic, huh?'
 show satoko_v002 smile at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Wait, I don't have time for that!! I gotta see if Jessica is okay!!"
 hide battler_v001
 hide satoko_v002
 with Dissolve(0.2)
 show rika_v002 smile at mei_left
 show hanyuu_v002 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Meep. He's certainly a lively person, bustling around in a sweat like that."
 show rika_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, he's very hot blooded~!"
 stop music fadeout 0.5
 hide hanyuu_v002
 hide rika_v002
 with Dissolve(0.2)
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show battler_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Woaaah! ...You girls, too... ah, sorry for losing my cool...!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Just as Battler-san quickly turned to his right, he realized that Hanyuu-chan and Rika-chan, who were standing behind him, had returned back to their original clothes at some point, so he jumped back in surprise.'
 narrator 'He then took a deep breath to regain his composure and explained the situation to those of us that were still unaware.'
 play music "<loop 0>audio/bgm/BGM_QUEST2_COLLAB3.ogg"
 show battler_v001 normal_close at mei_center
 with Dissolve(0.5)
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Like I said to the other kids over there, my cousin who came with me is the daughter of the sponsor who funded this place, and...'
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Aah, to be honest, the sponsor's wife doubts that investing into the hot spring district was the right thing to do! So we came to do a secret investigation!"
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But if they found out about those monsters... it's possible they could discontinue development or demand indemnities if we're not careful."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide battler_v001
 hide fade onlayer curtain
 show mion_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Aaah, th-... that'd be troublesome!!"
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "This project has made a lot of progress, and if it stopped now, it'd be a huge loss for the village!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v002 normal at mei_right
 show miyuki_v002 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. All of Hinamizawa would be in debt, and it'd be up to our necks."
 show rika_v002 normal at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "It'd be up to our necks? You mean {i}we'd{/i} be up to our necks? ...That sounds more like we'd hang ourselves."
 show miyuki_v002 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Group hanging, swoooosh-swoosh... meep!'
 hide miyuki_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show hanyuu_v002 fuan at active
 show hanyuu_v002 fuan at chara_shake_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au, au au au~?! Just imagining that is too horrible!!'
 hide rika_v002
 show satoko_v002 sinken at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Hey, Rika! Please don't go saying such ridiculous things! I won't be able to use the bathroom at night otherwise!!"
 hide hanyuu_v002
 hide satoko_v002
 with Dissolve(0.2)
 show battler_v001 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'The way I see it, the monsters in this village are scarier than the money...'
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Anyways, those monsters... you called them {b}Tsukuyami{/b}? That isn't normal! We gotta do something about them!"
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I don\'t wanna put a damper on the project when it\'s made this much progress... When you say "cull", does that mean you plan to exterminate them all?'
 hide battler_v001
 with Dissolve(0.2)
 show keiichi_v002 fuan at mei_left
 show battler_v001 normal at mei_right
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Even if I could say yes... how would we do that?'
 show keiichi_v002 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "We can save formulating a strategy for that later! Can we do some stuff so that Jessica won't see anything during our stay?"
 show keiichi_v002 fuan at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ah, but afterwards, please take care of all the monsters completely. Otherwise, we could have an awful murder incident on our hands...'
 hide keiichi_v002
 show rena_v002 odoroki at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'H-Hau...? Why would a murder incident occur if the hot spring development project got cancelled, got cancelled...?'
 show rena_v002 odoroki at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I also thought, "No way", while it was getting explained to me, but there\'s a possibility the worst case scenario can happen!'
 show rena_v002 odoroki at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'It\'s in a bunch of mystery novels, y\'know? \n"I loved them and didn\'t want them to suffer anymore, so I killed them." ...that\'s the kind of motive I\'m talking about.'
 show rena_v002 odoroki at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Something like that is totally possible here.'
 hide rena_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'H-Huhhhh...??'
 hide battler_v001
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "I didn't understand the meaning of that, and I didn't know what his circumstances were... but his manner of speaking was so persuasive that I wanted to believe his words."
 show mion_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show mion_v002 fuan_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "*sigh*... That's just how it is."
 hide mion_v002
 with Dissolve(0.2)
 narrator 'Mion-san gave a big sigh and shrugged her shoulders as she said that. She then turned to us with a very apologetic look, putting her hands together.'
 show mion_v002 normal at mei_center
 with Dissolve(0.5)
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Sorry, everyone, but I'm gonna need a hand with this. For the time being, we're gonna rid this village of all {b}Tsukuyami{/b}, even if it's just temporary."
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide fade onlayer curtain
 show miyuki_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ehhhhhh?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide miyuki_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v002 fuan at mei_center
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Is it really that bad, Miyuki?'
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide mion_v002
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_left
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Well... I do understand Miyuki-san's feelings. Recently, she's been having a hard time keeping up with Mion-san's many ridiculous demands."
 show satoko_v002 fuan at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Th-that isn't true... is it, Miyuki-chan?"
 hide satoko_v002
 show rika_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. I'm not so sure I can say it isn't true."
 show rika_v002 normal at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Well, is it or isn't it, Rika-chan?"
 hide rika_v002
 show miyuki_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show miyuki_v002 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...Sorry, I'm getting a bit of a headache. I'm gonna go back if it's okay."
 hide mion_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'W-Wait, Miyuki-chan...!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator 'Seemingly hurt from not being able to fully enjoy the hot spring, Miyuki-chan turned away and headed back towards the resort.'
 narrator 'I followed her and hurriedly ran around to get in front of her.'
 show kazuho_v002 fuan at mei_left
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "What's wrong, Miyuki-chan...? I know Mion-san said some dumb things, but it's just like what she always does..."
 show kazuho_v002 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "There's another reason I'm not too happy about it... I think we'd better not get involved."
 hide miyuki_v002
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "Miyuki-chan's pace slowed down, and she replied in a mumbling, barely audible voice. "
 show miyuki_v002 normal at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Like I said before, where I predicted that Battler-san was the type to attract trouble... I feel like it's worse than I imagined."
 show kazuho_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "I got a bad feeling, so I just wanna go home. I want to take Nao with me too, but Rena's here..."
 show kazuho_v002 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "So, Kazuho, just let me go back alone. It'd probably be better if I watched over from the sidelines. And if there's an emergency, I can come in at your flank..."
 show miyuki_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Miyuki-chan...?'
 hide kazuho_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator "I don't get what her problem is."
 narrator "The Miyuki-chan I know would jump in to help those in need... Somehow she doesn't seem like her usual self."
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(Is her hunch so bad that she's willing to bend her ideals...?)"
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'If Miyuki-chan is being this vigilant, I wonder if I should actually go home like she says?'
 narrator "But if something bad is bound to happen... I can't leave Nao-chan and the rest behind all the more."
 narrator "And I can't let the hot spring project get cancelled, otherwise all of Hinamizawa will suffer..."
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(Wh-what do I do... what do I do...?)'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Without an answer to any of those questions, the hot spring district came into view...'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2461.png' as bg
 stop music fadeout 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...Wha-?'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'I looked up at the familiar voice and saw a man looking at me from the middle of the road in the hot spring district.'
 narrator "He seems familiar. That's... that's...!!"
 show akasaka_v001 normal at mei_center
 with Dissolve(0.5)
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'You two are... if I remember correctly...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide akasaka_v001
 hide fade onlayer curtain
 show miyuki_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'D-Da-... Akasaka-san?'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide miyuki_v002
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '{b}Mamoru Akasaka{/b}, a detective from Tokyo who died in 1983, as well as the father of that girl, Miyuki Akasaka...'
 show ange_v001 odoroki at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Wait, why do I know his name? And how did I know that's her father...?!"
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'And I also know... the secret behind {i}those three{/i}...? They came from the year 1993 to this Hinamizawa 10 years earlier...?'
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Why...? Was it because I went through an experience similar to theirs?'
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 show ange_v001 fuan_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Battler Onii-chan...'
 call chapter_end
 jump event01_34_03