label event01_34_01:
 show black_background onlayer black
 $ event_store.current_event='umi2'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_34_01'
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
 show expression 'images/bg/AdvBg_261.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator '--On a certain holiday.'
 play audio 'audio/sfx/SE_343_ls_engine1.wav'
 narrator 'Kasai-san was driving us to that place.'
 narrator "Relatively speaking, it wasn't that far away. We just agreed to go there by car because it is across a steep hill."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1851.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rena_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Mii-chan! Congrats on finishing the Hinamizawa hot spring resort!'
 show rena_v002 smile at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ahaha, thank you, thank you... but I'm not really in a position where I can power pose with a triumphant face. All we did was sell the leftover land."
 hide rena_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "But the area all around here is the Sonozaki family's, right? I think that's awesome on it's own..."
 hide mion_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "And to think Mion-san's grandma gave the word to start this massive project... that itself is surprising too."
 hide kazuho_v002
 show rika_v002 normal at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. I heard that a Tokyo resort construction company took the chance to propose their plans to her.'
 hide satoko_v002
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show mion_v002 smile at active
 show mion_v002 smile at nod_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Yep, yep. That company came and was like, "Can we build a hot spring district here if we finance it?"'
 hide rika_v002
 hide mion_v002
 with Dissolve(0.2)
 show hanyuu_v002 smile at mei_left
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au. I think I remember that there was a community hot spring settlement around this area.'
 show hanyuu_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'The people in the village would use it from time to time. I only got to use it a few times myself, but when I did use it, it felt so nice that it became one of my favorite things ever~♪'
 hide miyuki_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "The district's around about the same spot where that hot spring is. When the specialist came by recently to survey it, he confirmed that the quality of the water was incredibly good."
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'But since there was the political dispute over the dam being built, the village council had a mixed reception on whether they should let contractors get involved.'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '"Screw that! I say for the village to grow, we must also focus on tourism!!"'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...With that one phrase, Granny persuaded the entire village to be in support of it.'
 hide mion_v002
 with Dissolve(0.2)
 show keiichi_v002 fuan at mei_left
 with Dissolve(0.5)
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Just one phrase making it so a whole hot spring district gets built... your grandma is the real deal, Mion.'
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'And when that one area was finished, they started the pre-opening for it.'
 show keiichi_v002 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Hot spriiing~! It's gonna be so much fun~! It's been hard trying to travel these days, so I'm gonna kick my feet back and relax~!"
 hide keiichi_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, we'll have lots of fun relaxing~!"
 hide miyuki_v002
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... but from hearing that conversation earlier, this was super fast compared to the whole year they said it would take to finally open.'
 hide hanyuu_v002
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Since the area around the hot spring facility used to be a settlement, it seems they were able to repurpose the electricity and water supply there.'
 hide rena_v002
 hide rika_v002
 with Dissolve(0.2)
 show mion_v002 fuan at mei_center
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Well, in any event, we need to start developing highways since we plan to set up tour buses to get tourists here.'
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "For the time being, we're just focusing on families and relatives of the Hinamizawa and Okinomiya inhabitants..."
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'The plan of operation will depend on that from here on out. The people from the management company are pretty chill too. They mentioned how they wanted people who live here using it freely.'
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's where we come in as reviewers. They're going to want the opinions of the youngest generation..."
 show nao_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "So, that's why the lodging expenses are free of charge...\nI-It's a huge responsibility, huh?"
 show nao_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(But was there actually a conversation about a land development plan up until recently? More specifically, a hot spring district being built in Hinamizawa is...)'
 show nao_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(...Was there something I missed...?)'
 show kazuho_v002 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "There aren't really any responsibilities; we don't have to pay much mind to that. All we're doing is having fun staying overnight and taking notes whenever we find something we like... That's it."
 hide kazuho_v002
 show keiichi_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Geh. I didn't even think we'd have to take memos... \nMaaan, I'm actually gonna have to put some work in."
 hide nao_v002
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau, yeah. It'd be nice if Shii-chan came too, wouldn't it?"
 hide keiichi_v002
 hide rena_v002
 with Dissolve(0.2)
 show mion_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show mion_v002 fuan_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "She said she had some errands to do.\n...It'll will be way more relaxing without Shion. She'd never shut up if she were here."
 hide mion_v002
 with Dissolve(0.2)
 show rika_v002 smile at mei_left
 show mion_v002 fuan_close at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan_close at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. I think she could say the same about you.'
 show rika_v002 smile at inactive
 show mion_v002 odoroki at active
 show mion_v002 odoroki at jump_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Whaa-?!'
 hide mion_v002
 hide rika_v002
 with Dissolve(0.2)
 show kasai_v001 normal at mei_center
 with Dissolve(0.5)
 show kasai_v001 normal at active
 Character('Tatsuyoshi Kasai',ctc="ctcArrow", ctc_position="fixed") '...Mion-san, we should be reaching the destination very soon.'
 hide kasai_v001
 with Dissolve(0.2)
 show keiichi_v002 smile at mei_left
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Oh, it's surprisingly close, huh?"
 show keiichi_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... my heart's pounding from the excitement."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide rena_v002
 hide keiichi_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_261.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'As we had that conversation, the car made it out of the forest, arriving at our destination.'
 narrator 'And so, what spread out in front of us was...!'
 window hide None
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_2461.png' as bg
 call wipein_routine
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_577_ls_sanriokirakira.wav'
 pause 2.0
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show rena_v002 smile_blush at mei_left
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show rena_v002 smile_blush at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Wooaaah~!! Coool~!'
 show rena_v002 smile_blush at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Yeah, the hot spring district is better than I imagined...!'
 hide miyuki_v002
 hide rena_v002
 with Dissolve(0.2)
 narrator 'Everyone cheered as they got out of the car one by one, eyes darting around in every direction.'
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Th-this is amazing...! To think Hinamizawa could make a hot spring district as impressive as this...!'
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au au! It's almost gives off the appearance of a famous sightseeing area~!"
 hide satoko_v002
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "From here on out, it's {i}going{/i} to be a famous sightseeing area. This is the fruit of our labor!"
 hide hanyuu_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Wow... my dreams probably couldn't even top this..."
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator 'The scenery was so stunning that even Nao-chan was spouting words like that.'
 narrator 'Judging from a glance, the buildings lined up together looked a bit old-fashioned... but that was just the outwards appearance.'
 narrator 'Taking a peek inside, you could see how clean and brand-new it looked... It was brimming with class.'
 show keiichi_v002 smile_close at mei_left
 with Dissolve(0.5)
 show keiichi_v002 smile_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Oh...? I smell something good.'
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show keiichi_v002 smile_close at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'That might be the hot spring manjuu? Looks like one of the dedicated stands made it.'
 hide keiichi_v002
 show kazuho_v002 smile_blush at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show mion_v002 smile at inactive
 show kazuho_v002 smile_blush at active
 show kazuho_v002 smile_blush at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'M-Manjuu...!'
 hide mion_v002
 show keiichi_v002 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 smile_blush at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Hell yeah! Piping hot, fluffy manjuu steamed in a hot spring! C'mon, Kazuho-chan, let's eat some!"
 show keiichi_v002 smile at inactive
 show kazuho_v002 smile_blush at active
 show kazuho_v002 smile_blush at nod_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'O-...Okay!!'
 hide kazuho_v002
 hide keiichi_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But where could that stand be?'
 show nao_v002 normal at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'I can smell it, but the stand is nowhere in sight...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide miyuki_v002
 hide nao_v002
 hide fade onlayer curtain
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I'll look right now!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "We couldn't see it in our field of view, but surely it has to be down this road somewhere."
 narrator 'Since the hot spring district already started its pre-opening, this road definitely has to be paved in a straight line. If we run, we should be able to find it...'
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Here we gooo!'
 play audio 'audio/sfx/SE_408_run.wav'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'H-Huh...?'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'I ran ahead of everyone, but the hot spring smell started deepening...? The presense of the manjuu in the air began to fade gradually.'
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Where are they selling the manjuu...?'
 hide kazuho_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator 'While I was walking, I was looking left and right when...'
 stop music fadeout 0.5
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5013_down.wav'
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Kya?!'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'In that moment, I collided with something sort of both soft and hard.'
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB3.ogg"
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...Oof.'
 narrator "What I run into starts talking, so I realize I hit a person... \nI gasp as I come to understand the situation I'm in."
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I-I'm sorry...!"
 hide kazuho_v002
 with Dissolve(0.2)
 show miyuki_v002 odoroki at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Kazuho, are you okay?!\nI'm sorry; our friend caused you trouble!"
 show miyuki_v002 odoroki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "You shouldn't look away from where you're running, you know...\nMy apologies; are you okay?"
 hide nao_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator 'Miyuki-chan and Nao-chan rush up from behind and start apologizing.'
 narrator 'The person reacted blankly... but quickly gave a calm smile and waved.'
 show battler_v001 smile at mei_center
 with Dissolve(0.5)
 show battler_v001 smile at active
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Nah, don't worry about it. I wasn't looking straight ahead either. My bad."
 hide battler_v001
 with Dissolve(0.2)
 narrator 'This person I carelessly bumped into was probably... high school age.'
 narrator "He was tall... and looked too old to be called a boy, yet too young to be called a man at the same time. That's what he looked like."
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.5)
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "You okay, Kazuho-chan? ...Wait, who's this guy?"
 hide keiichi_v002
 with Dissolve(0.2)
 show miyuki_v002 fuan at mei_left
 show battler_v001 smile at mei_right
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Kazuho-chan bumped into him...\nUm, I haven't seen your face around these parts, so are you actually a sightseer?"
 show miyuki_v002 fuan at inactive
 show battler_v001 smile at active
 Character('????',ctc="ctcArrow", ctc_position="fixed") "So that means you guys are from this area?\nHahah, of course I'd get pumped to go when this place popped up so suddenly!"
 show miyuki_v002 fuan at inactive
 show battler_v001 normal at active
 Character('????',ctc="ctcArrow", ctc_position="fixed") "I didn't really answer your question, though.\nSightseeing... nah, it's a bit different, I think?"
 hide miyuki_v002
 show kazuho_v002 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...?'
 show kazuho_v002 normal at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But this is perfect timing if you guys are from around here. \nI'm Battler Ushiromiya. Nice to meet you."
 show kazuho_v002 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'll be straightforward. Have you guys heard anything interesting about this hot spring?"
 show kazuho_v002 normal at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I didn't think the inhabitants here would build this place so readily... and stuff..."
 hide kazuho_v002
 show keiichi_v002 odoroki at mei_left
 with Dissolve(0.5)
 show battler_v001 normal_close at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide battler_v001
 hide keiichi_v002
 with Dissolve(0.2)
 narrator 'We exchanged glances as this person named Battler-san inquired about something wildly beyond our expectations.'
 narrator "I had a bit of doubt after hearing Mion-san's story... but I don't think the village would be hesitant in welcoming it."
 show miyuki_v002 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "No, I don't think that's the case..."
 show keiichi_v002 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "The landlord's daughter... Mion, is okay with it. She was so eager about it, she called over a bunch of tourists and livened up the village."
 hide miyuki_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show keiichi_v002 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The other kids have been taking it pretty normally too, you know?'
 hide keiichi_v002
 show battler_v001 smile_close at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show battler_v001 smile_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...I see. If they're open to it, then that’s cool."
 hide nao_v002
 hide battler_v001
 with Dissolve(0.2)
 narrator 'Battler-san let out what could be assumed to be a breath of relief, which caused Miyuki-chan to smile cheerily; a question coming to her mind.'
 narrator '...She spent a while having nosy thoughts after making this face. She may have gotten a bit curious about his background.'
 show miyuki_v002 smile at mei_left
 show battler_v001 smile_close at mei_right
 with Dissolve(0.5)
 show battler_v001 smile_close at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'If you have anything going on, would you mind telling us?\nWe might be able to lend you a hand.'
 show miyuki_v002 smile at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...I actually came here with my cousin, but she's the daughter of the sponsor of this hot spring facility."
 hide miyuki_v002
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The daughter of... the sponsor...? So she came to Hinamizawa for an inspection?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide battler_v001
 hide nao_v002
 hide fade onlayer curtain
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'D-Does this mean that depending on the result of the inspection, this hot spring district might have to close down?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show keiichi_v002 odoroki at mei_left
 show battler_v001 normal at mei_right
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Wha-...?!'
 show keiichi_v002 odoroki at inactive
 show battler_v001 odoroki at active
 show battler_v001 odoroki at jump_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'N-Nonono! That would be an overstatement!'
 show keiichi_v002 odoroki at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Just, well, I feel like we came due to a family issue... but the fact that this place is much nicer than I thought honestly puts me at ease!'
 hide keiichi_v002
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Th-that's relieving..."
 hide battler_v001
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "Battler-san's words let us loosen up."
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(Ah... but an inspection due to family issues... what's that about...?)"
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Just as I thought how weird that was, Nao-chan asked another question.'
 show nao_v002 smile at mei_left
 show battler_v001 smile at mei_right
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Where is that cousin you mentioned?'
 show nao_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Oh, she went to the main hot spring area earlier. After that, I thought I’d take a look around, y'know?"
 show nao_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'She was nervous at first, but if she knew that the villagers are open to it, she would probably feel relieved too.'
 show nao_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So, thanks. That was reassuring.\nI'll head out now. <See you again. Have a nice day.>"
 hide battler_v001
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator 'With a wave of his hand, Battler-san disappeared off into the back of the hot spring district. We absentmindedly watched him go.'
 stop music fadeout 0.5
 show keiichi_v002 smile at mei_center
 with Dissolve(0.5)
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") '...Battler-san was... kind of a cool dude, huh?'
 hide keiichi_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_right
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show kazuho_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'You want to be like him, Maebara-san? He was kinda eh, though.'
 show nao_v002 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide kazuho_v002
 show keiichi_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yeah, I do kinda... wait, so you didn't like him that much then, Nao-chan?"
 show keiichi_v002 smile at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I don't care if you {i}want{/i} to be like him, but it'd be better if you didn't try becoming like that type of person."
 show keiichi_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Not that I dislike it, but it's that type that naturally has women flocking to them... and incidentally, a type that gets tied up in women problems."
 show nao_v002 normal at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'How could you figure something like that in such a short amount of time?'
 show keiichi_v002 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "The reason behind it would be troubling to have to explain... but I'll say it's a rule of thumb."
 hide keiichi_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I-Isn't that a bit rude to someone you just met...?"
 hide nao_v002
 show miyuki_v002 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm... even if that guy is that way, he looks unaware that he's a lady killer type though, doesn't he?"
 show kazuho_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "I don't think he's a bad guy, but being unconscious of your popularity with the other sex is just asking for trouble."
 show kazuho_v002 fuan at inactive
 show miyuki_v002 normal_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "But it's hard for him to realize, so it's not his fault, y'know?"
 hide kazuho_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show keiichi_v002 fuan at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "I had no idea, but I guess it's just women's instinct. \n...What do you think, Kazuho-chan?"
 show keiichi_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I-I don't really know, but..."
 hide kazuho_v002
 hide keiichi_v002
 with Dissolve(0.2)
 narrator 'If Nao-chan and Miyuki-chan have the same view on it, then that sort of person might actually exist... even if I know nothing about it.'
 show keiichi_v002 smile at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show keiichi_v002 smile at active
 show keiichi_v002 smile at jump_transform
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Still, I aspire to be a man popular with the ladies! A few years down the line, I wanna be cool without even trying like he does!'
 hide keiichi_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_right
 show keiichi_v002 smile at mei_left
 with Dissolve(0.5)
 show keiichi_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...So, you'd take the double edge of being resented by women too, then?"
 show nao_v002 normal at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Th-that's... no thanks."
 hide nao_v002
 show miyuki_v002 normal at mei_right
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Living a popular life having your every action on spotlight, or living a normal life in obscurity... I wonder which is better?'
 hide keiichi_v002
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'D-Do popular people really have that sort of lifestyle?'
 hide miyuki_v002
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Even if you don't want that, if you fit the bill, you'll end up there anyway."
 hide kazuho_v002
 show keiichi_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "That's pretty philosophical of you, Nao-chan..."
 show keiichi_v002 fuan at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Well, this does happen a lot in the world of fashion too.'
 hide nao_v002
 hide keiichi_v002
 with Dissolve(0.2)
 narrator "Everyone is getting pretty philosophical aside from Maebara-kun... although I understand Miyuki-chan's point best."
 narrator "I feel like I'm the only person who isn't with the times, and it makes me feel pathetic..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show mion_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hey, hey, don't run off without me like that!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator 'At that moment, Mion-san approached us from behind.'
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Sorry, sorry! But you took a while to catch up to us, y'know?"
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Rena and Hanyuu kept looking around everywhere, so it took us a while to catch up.'
 hide miyuki_v002
 hide rika_v002
 with Dissolve(0.2)
 show rena_v002 smile at mei_left
 show hanyuu_v002 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ha-... hau~. There were lots and lots of kyute souvenirs everywhere...'
 show rena_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au! Rika was looking around a lot too~!'
 hide hanyuu_v002
 hide rena_v002
 with Dissolve(0.2)
 show satoko_v002 normal at mei_right
 show kazuho_v002 normal at mei_left
 with Dissolve(0.5)
 show kazuho_v002 normal at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Anyway, what's the matter with Kazuho-san and everyone? You look like you've been having a troubling conversation."
 show satoko_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'U-Um...'
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Kazuho bumped into a tourist.'
 show nao_v002 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'So, the conversation took off from there... about men that are popular with ladies.'
 hide nao_v002
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I don't see how that's related at all."
 hide miyuki_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au. The conversation literally took off.'
 hide satoko_v002
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "We just feel that way because we missed the bulk of it, but surely we'll understand as the flow of it goes on."
 hide hanyuu_v002
 hide rika_v002
 with Dissolve(0.2)
 show mion_v002 fuan at mei_center
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'I-I guess...?'
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But regardless, something that'd make a man popular with the ladies, huh? The most obvious thing is being tall, right...?"
 hide mion_v002
 with Dissolve(0.2)
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... If Rena fell in love, I think height wouldn't matter much, though."
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "That might be true if you fell in love, but we're talking about the {i}prerequisites{/i} to falling in love, y'know?"
 hide rena_v002
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'In that case, I believe someone kind really is the way to go.'
 hide miyuki_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, I think so too. I think no matter the gender, a kind person would be the most loveable.'
 hide satoko_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.5)
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'A kind, tall man, huh...? Setting the mental part aside, what can you do about height?'
 hide keiichi_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. I think it would be difficult to change who you are on the inside.'
 show rika_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Yeah, it {i}would{/i} be pretty difficult to change around your insides.'
 hide nao_v002
 hide rika_v002
 with Dissolve(0.2)
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.5)
 show keiichi_v002 fuan at active
 show keiichi_v002 fuan at chara_shake_transform
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Uuuh...?! Y-You can do that...?'
 hide keiichi_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show kazuho_v002 smile at inactive
 show mion_v002 smile at active
 show mion_v002 smile at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ahaha! Good luck, Kei-chan! Kill some ladies!'
 show mion_v002 smile at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ahaha. If it's Maebara-kun, I think he'll be fine."
 hide kazuho_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator 'And just as we laugh to that...'
 stop music fadeout 0.5
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'U-Uuuuuoooooooohhhhh?!\nWh-what are you guuuyyyssss?!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show nao_v002 sinken at mei_right
 show keiichi_v002 odoroki at mei_left
 with Dissolve(0.5)
 show keiichi_v002 odoroki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'That voice just now was...'
 show nao_v002 sinken at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Was that Battler-san?'
 hide keiichi_v002
 hide nao_v002
 with Dissolve(0.2)
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'N-No way...!'
 hide kazuho_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator 'With a bad feeling stirring in the air, we dashed towards the direction his voice came from.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2491.png' as bg
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB3.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'The voice came from a branch off of the main road.'
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'I think it came from there... ah?!'
 hide kazuho_v002
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 camera at screenshake_transform
 pause 0.0
 Character('Tsukuyami',ctc="ctcArrow", ctc_position="fixed") '{b}Giiiiiiiiiiiiiiiiii!!{/b}'
 show battler_v001 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan at active
 show battler_v001 fuan at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hiiih, hiiiiiiiiiihhhh!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "The {b}Tsukuyamis'{/b} joints creaked and rattled as they creeped towards someone fallen over on the ground..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show battler_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 fuan at active
 show battler_v001 fuan at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Wh-what is this?! No, seriously, what is going on?!?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ba-Battler-san!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide fade onlayer curtain
 show battler_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Uooh?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'When I called out to Battler-san, he turned his head to find me, yelling out with tears in his eyes.'
 show battler_v001 sinken at mei_right
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 show kazuho_v002 sinken at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Y-You're the one from before...?! D-Don't come any closer!! Run! Noooow!!!!"
 show battler_v001 sinken at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(Even when he's about to get attacked, he's worried about my wellbeing...?)"
 show battler_v001 sinken at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(He... He's a great person. He's actually a great person! I absolutely cannot sit here and let someone like that die!)"
 show battler_v001 sinken at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "It's alright! Just leave it to us!"
 show kazuho_v002 sinken at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'L-Leave it to you...? What could you possibly do against that?!'
 hide kazuho_v002
 hide battler_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator 'The very second after he cried out those words, I hear the sound of numerous footsteps coming from behind.'
 show keiichi_v002 odoroki at mei_left
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Woah, they're coming in hordes?!"
 show keiichi_v002 odoroki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Guess he's pretty popular with {b}Tsukuyami{/b}... never mind ladies."
 hide keiichi_v002
 show satoko_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Are you really joking around at a time like this?!'
 hide nao_v002
 show rika_v002 sinken at mei_right
 with Dissolve(0.5)
 show satoko_v002 sinken at inactive
 show rika_v002 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'You over there, get out of there, now!'
 hide satoko_v002
 hide rika_v002
 with Dissolve(0.2)
 show battler_v001 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Wh-... what is this?! What is thiiis?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide battler_v001
 hide fade onlayer curtain
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Battle positions, everyone!\nWe're saving this guy!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 Character('Everyone',ctc="ctcArrow", ctc_position="fixed") 'Yeaaaahhhhhh!!!'
 show battler_v001 odoroki at mei_center
 with Dissolve(0.5)
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Wh-... huh?'
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show battler_v001 odoroki at active
 show battler_v001 odoroki at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'HHHUUUUUUUUUUUUUUHHHHH?!?!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide battler_v001
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
 show ange_v001 odoroki at mei_center
 with Dissolve(0.5)
 show ange_v001 odoroki at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'W-Wait a sec...!'
 show ange_v001 odoroki at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'This comes nowhere close to the kind of fantasy with witches and goats...!'
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'What is happening in this world...?'
 call chapter_end
 jump event01_34_02