label event01_34_99:
 show black_background onlayer black
 $ event_store.current_event='umi2'
 $ event_store.current_progress=1
 $ event_store.current_chapter='event01_34_99'
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
 show expression 'images/bg/AdvBg_253.png' as bg
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_405_swing_high.wav'
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Hnn, taaaahhhh!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_5013_down.wav'
 narrator 'We finished them off so easily that it was uneventful.'
 narrator "With the bunch of us already here in the first place, losing wasn't even a thought that crossed our minds."
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(But rather than that, the problem now is...)'
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB3.ogg"
 hide kazuho_v002
 with Dissolve(0.2)
 show jessica_v001 normal at mei_center
 with Dissolve(0.5)
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'Jessica-san was frozen like she was astonished.'
 narrator 'Physically, she was unhurt, so that was a relief, but...'
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(...The air! It's so heavy!)"
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Battler-san went through all those lengths to keep Jessica-san from finding out about the {b}Tsukuyami{/b}, but now it was too late.'
 narrator 'She took in the entire scene, from their arrival to their disappearance.'
 show mion_v002 fuan_close at mei_right
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show mion_v002 fuan_close at active
 show mion_v002 fuan_close:
  yanchor 1.0
  linear 0.5 pos (1440,1250)
 pause 0.5
 show mion_v002 fuan_close:
  yanchor 1.0
  pos (1440,1250)
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Finished... Hinamizawa... is finished...'
 show mion_v002 fuan_close at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Mi-Mii-chan, pull yourself together!'
 hide rena_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator 'Rena-san ran over to support Mion-san, who was now lurched over with her hands on her head.'
 show keiichi_v002 fuan at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'So this is what it means when winning a match feels like a loss...'
 show keiichi_v002 fuan at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep...'
 hide keiichi_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'A-Au au.'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'W-What should we do...?'
 hide hanyuu_v002
 show nao_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...There's... nothing we can do."
 hide satoko_v002
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan_close at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "There's no way to worm ourselves out of this... huh?"
 hide nao_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator "Amidst the suffocating atmosphere the club members were enshrouded in, Shion-san alone felt weirded out as she didn't have a grasp on the situation."
 show shion_v002 fuan at mei_center
 with Dissolve(0.5)
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Um... guys, what's going on?"
 hide shion_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 narrator 'With that... Battler-san put on a resolute face and stepped forward as if to cover for us.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show battler_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...It's alright. I'll pay you back my debt for saving me. I'll handle it."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh?'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'In saying that, he faced Jessica-san, calmly let out a huge breath, and followed up with what he wanted to say.'
 show battler_v001 normal at mei_right
 show jessica_v001 normal at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'U-Uh, Jessica... I have a long explanation for all the uncontrollable events tonight...'
 show jessica_v001 normal at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "No one here had bad intentions. \nWe obviously just didn't realize how necessary it was to inform you since it was so... uh..."
 stop music fadeout 0.5
 show battler_v001 normal_close at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...? What are you talking about, Battler?'
 show jessica_v001 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Huh...? What am I talking about... What are {i}you{/i} talking about?'
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB3.ogg"
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show rika_v002 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep... Jessica doesn't look very surprised."
 show rika_v002 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Don't tell me... Jessica-san was already long aware of the {b}Tsukuyami{/b}?"
 hide rika_v002
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Those dudes just earlier?\nYeah, of course, since there was a report about them.'
 hide nao_v002
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A what...?!'
 show kazuho_v002 odoroki at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But this is the first time I've heard them being given a name like {b}Tsukuyami{/b}, y'know?"
 show kazuho_v002 odoroki at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Damn, okay. \nSo, the rumor was about {i}those{/i}... huh? They really did exist.\nSo Dad wasn't actually trying to mess with me!"
 hide kazuho_v002
 show mion_v002 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Huh? Huh...?'
 hide jessica_v001
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'H-Hau... um, what do you mean?'
 hide mion_v002
 hide rena_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well, it's been a concept for the development project my dad invested in."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_348_ls_suddunshow.wav'
 show jessica_v001 futeki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'They called it...\n "The Demon Parade Runs Rampant: Monster Hot Spring"!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide jessica_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 normal at mei_center
 with Dissolve(0.5)
 pause 1.0
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jump_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...wh-......?!'
 hide kazuho_v002
 with Dissolve(0.2)
 show battler_v001 fuan at mei_right
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So essentially, you were told they did exist... but you thought they actually didn't and that he was pulling your leg?"
 show battler_v001 fuan at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yeah. I didn't know what you'd think if I mentioned it, so I kept quiet.\n'Cuz back in the day you were a big scaredy cat, y'know?"
 show battler_v001 fuan at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well, Dad was saying that the Demon Parade was its best selling point. If you took that out, it would just be your everyday nice hot spring, so it's a plus for it."
 show jessica_v001 smile at inactive
 show battler_v001 sinken at active
 show battler_v001 sinken at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Nahhh, the Demon Parade being a selling point?!\nHe thought that would bring in customeeeeeeeerrsss?!'
 $ event_store.current_progress = 2
 show battler_v001 sinken at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Dad is predicting that there\'s gonna be a horror boom coming soon. \n"I could receive blessings if I visit an inn with a {note_green}Zashiki-warushi{/note_green} in it!", that sort of idea!'
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Zashiki-warushi are like gods of fortune, but doesn't Hinamizawa's {b}Oyashiro-sama{/b} go against that premise as a {b}god of disaster{/b} that curses people...?"
 show nao_v002 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Nao, your mouth zipper is undone.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide nao_v002
 hide fade onlayer curtain
 show jessica_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'That was pretty sick! Mom was skeptical about them too, but now I can puff out my chest and report back to her with, "The monsters do exist."!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide jessica_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.5)
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'I-Is that... actually okay...?'
 hide keiichi_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_left
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Well, I was surprised when we were getting attacked.\nBut the fact that you were able to defeat all of them without getting hurt made it even more cool.'
 show battler_v001 fuan at inactive
 show jessica_v001 smile_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Those things just look like boars!'
 show battler_v001 fuan at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I see them on my island from time to time. If you get close to them, it could get dangerous... but if you kill them it's no issue, right?"
 show jessica_v001 smile at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Huh? Boars are on that island too?!'
 camera at screenshake_transform
 pause 0.0
 show jessica_v001 smile at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Is that okay?!\nIs it really okay to handle those things just like boars?!'
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_left
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'U-Um...'
 show satoko_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, where is this situation going...?'
 hide satoko_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I-I don't know at all either, but..."
 hide hanyuu_v002
 show akasaka_v001 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "I don't think there would be a breach of contract issue if they knew what they were getting into."
 show akasaka_v001 smile at inactive
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Well, Akasaka-san...\nThe contract issue has been long over by now......'
 hide akasaka_v001
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan_close at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'So then... if Jessica-san had already known about them from the beginning, does that maybe mean there was never really a problem... a problem?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide rena_v002
 hide fade onlayer curtain
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Wh-wha-...'
 play audio 'audio/sfx/SE_347_ls_fall.wav'
 camera at screenshake_transform
 pause 0.0
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'What in the hell?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show shion_v002 smile at mei_center
 with Dissolve(0.5)
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'My, you all fell over simultaneously like you were in a skit.'
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_left
 show battler_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ahahaha! Just like Shion-san said, this village is hilarious!'
 show jessica_v001 smile at inactive
 show battler_v001 fuan_close at active
 show battler_v001 fuan_close at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'G-Grrrrr...'
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'While everyone was still carelessly rolling around on the ground, with a stagger, Battler-san was the very first one to stand back up.'
 show battler_v001 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I thought Uncle Krauss was the king of crazy tastes for a long while now, but...'
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...to think you and Aunt Natsuhi are no different...'
 hide battler_v001
 with Dissolve(0.2)
 show miyuki_v002 smile at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Really? I think haunted inns as an idea is a pretty sharp move, though.'
 show miyuki_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Miyuki, we're in the Showa era."
 hide miyuki_v002
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Showa, huh... but... thank goodness. Nothing was actually wrong.'
 hide nao_v002
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Right? ...I guess my senses have gotten dull.\nMy bad feeling earlier really was completely baseless after all.'
 hide kazuho_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator 'As she said that, Miyuki-chan sighed apologetically. And in attempt to encourage her, {i}pat{/i}, Akasaka-san tapped her shoulder.'
 show akasaka_v001 smile at mei_right
 show miyuki_v002 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "An officer's duty is to prevent a worst case scenario.\nWhether it was needless worry or a fruitless effort, I believe that we should take pleasure in the fact that nothing went wrong."
 show akasaka_v001 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...You're right. I'll think of it the way you do, Akasaka-san."
 hide miyuki_v002
 hide akasaka_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Oh, yeah. Now that we're all gathered here, let's view the nightscape together."
 show shion_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'The scenery from the shrine grounds is very lovely.'
 hide rika_v002
 hide shion_v002
 with Dissolve(0.2)
 show battler_v001 smile at mei_center
 with Dissolve(0.5)
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Then, I'll just..."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide battler_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_293.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'W-...Woaaaah!'
 narrator 'As Battler-san yelled out in amazement, we all walked up from behind him and looked down on Hinamizawa.'
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "The lights aren't as bright as the ones in the city... but thanks to that, the moon is so big and beautiful looking."
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. This is Hinamizawa's prided night view."
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'The mountains give it an awesome touch too.'
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Yeah... Man, sometimes stuff like this is great.'
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Although I think this scenery would be the utmost perfect sight to see with that one boy~.'
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Yeah. I'd love to bring him here one day."
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... Jessica-san, do you have someone you like?'
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Nnnn-nono, um... uhhhh, I probably wasn't thinking about what I said very well... uh... yeah."
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'My, is it okay to chat about such a thing?'
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au! We'll pray for you afterwards! Hinamizawa has a god of marriage anyway~!"
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Huh...? The god here is the type of god to hitch people together?'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Akasaka, your punishment game will be later.'
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Whaaaa-?!'
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hahahahaha! Even though this beautiful night scene is so peaceful, it's bound to be lively with this many people."
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Do you not like it when it's lively?"
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Nah, I love it! A bunch of people getting together having a blast on a trip is the best!'
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yep, yep, it's great to have fun!"
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ooo, we see eye to eye. I think your name was Miyuki-chan, right? ...Uh?'
 stop music fadeout 0.5
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "What's the matter?"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'That... glowing over there, what is that?'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_253.png' as bg
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Battler-san pointed out in a direction behind Hinamizawa.'
 narrator 'There was clearly something huge shining over there.'
 show battler_v001 normal at mei_center
 with Dissolve(0.5)
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Huh, what's going on? Are they doing an event or something?"
 hide battler_v001
 with Dissolve(0.2)
 show kasai_v001 normal at mei_center
 with Dissolve(0.5)
 show kasai_v001 normal at active
 Character('Tatsuyoshi Kasai',ctc="ctcArrow", ctc_position="fixed") "I haven't heard of any plans for anything like that, though..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kasai_v001
 hide fade onlayer curtain
 show mion_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yeah, I haven't eith-... AAAAAAAAAAAAAAHHHH?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show akasaka_v001 fuan at mei_left
 show mion_v002 odoroki at mei_right
 with Dissolve(0.5)
 show mion_v002 odoroki at inactive
 show akasaka_v001 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "W-What's wrong, Mion-san? Your expression changed. What is it?"
 show akasaka_v001 fuan at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Th-, isn't that a fire?!"
 hide akasaka_v001
 show keiichi_v002 odoroki at mei_left
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Huh... ah, it is! Red flames are dancing back and forth!!'
 hide mion_v002
 show battler_v001 odoroki at mei_right
 with Dissolve(0.5)
 show keiichi_v002 odoroki at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "And plus, isn't that in the direction of the hot spring district?!"
 hide keiichi_v002
 show rena_v002 odoroki at mei_left
 with Dissolve(0.5)
 show battler_v001 odoroki at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Huh, so what's burning is..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide battler_v001
 hide rena_v002
 hide fade onlayer curtain
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Th-... the hot spring district?!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_261.png' as bg
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 narrator 'And so, the next morning--'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1361.png' as bg
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show battler_v001 fuan at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '*sigh*... So all of that happened overnight, huh...?'
 show battler_v001 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 hide kazuho_v002
 hide battler_v001
 with Dissolve(0.2)
 narrator 'Dejected... we looked over the ash and debris that the "hot spring district" now was.'
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.5)
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "After all that's happened, it just goes up in flames...?"
 hide keiichi_v002
 with Dissolve(0.2)
 show jessica_v001 fuan_close at mei_right
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I-I can't believe it...*cough*, *cough*cough*!!"
 show jessica_v001 fuan_close at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... you might be inhaling smoke. I think it'd be better if we get away from the scene for a bit."
 show rena_v002 fuan at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'S-Sorry... *cough*.'
 hide rena_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator "Rena-san pats Jessica-san's back as she has a coughing fit."
 narrator '...Because of the raging flames overnight, the hot spring district was wiped out in the blink of an eye.'
 narrator 'Since the surrounding area was blocked by "No Trespassing" tape, we didn\'t know the details, but it looks like the inn is partially gone.'
 narrator "...This might be disdainful to say, but business couldn't be done in those conditions."
 show mion_v002 fuan at mei_right
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Fire is... scary, huh?'
 show mion_v002 fuan at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'You said it...'
 hide mion_v002
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep... What should we do now?'
 hide shion_v002
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "No matter what we do, isn't it already too late...?"
 hide rika_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, this is so...'
 hide satoko_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 narrator 'While everyone was whispering to each other separately, Miyuki-chan next to me was murmuring to herself.'
 show miyuki_v002 fuan at mei_left
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "My bad feeling wasn't actually... this, was it...?"
 show miyuki_v002 fuan at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Nice intuition. If you were actually capable of predicting this fire, shouldn't you become a soothsayer instead of a detective?"
 show nao_v002 fuan_close at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Are you saying I can become Nostradamus?\nWasn't he a doctor before a soothsayer, though?"
 show miyuki_v002 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'That has nothing to do with what I said...'
 hide nao_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator 'Right then, we saw a figure coming towards us from the tape barricade, and we all waved at him.'
 show kazuho_v002 normal at mei_center
 with Dissolve(0.5)
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-...Akasaka-san!'
 hide kazuho_v002
 with Dissolve(0.2)
 show akasaka_v001 smile at mei_left
 with Dissolve(0.5)
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Hey, everyone's here, huh?"
 show battler_v001 normal at mei_right
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'So, what did the firemen say?'
 show battler_v001 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "This is outside of my jurisdiction so I didn't hear the details, but while it's still being confirmed... the cause is likely to have been a circuit breaker failure."
 show battler_v001 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "The firefighters didn't make it in time for the early stages, so it appears the hot spring equipment caught fire."
 show akasaka_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'So, with the circuit breaker... it was an electric fire?'
 hide akasaka_v001
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Even though it's electricity... it turned into a fire?"
 hide battler_v001
 show satoko_v002 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Kazuho-san, don't make light of electricity. It can make a regular fire look pathetic."
 hide kazuho_v002
 show keiichi_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 normal at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "But wasn't this hot spring facility just finished?! How could this happen...?"
 hide satoko_v002
 hide keiichi_v002
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "It couldn't have been from degradation or anything... so it must have been an error on the contractor's end?"
 show shion_v002 normal at inactive
 show mion_v002 sinken at active
 show mion_v002 sinken at chara_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...So you're saying they did half-ass work?! All of that for the hot spring district to go to waste... I'm gonna make these contractors pay!!"
 show mion_v002 sinken at inactive
 show shion_v002 odoroki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "H-Hold on, Sis! We're jumping to conclusions. Please calm down!"
 show shion_v002 odoroki at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'But Shion!\nAll that hard work with the hot spring district... and it was meant to be the one huge project to develop the village for-...!!'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Mion-san.'
 show satoko_v002 fuan at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Mii...'
 hide rika_v002
 hide satoko_v002
 with Dissolve(0.2)
 show akasaka_v001 fuan at mei_center
 with Dissolve(0.5)
 show akasaka_v001 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "...I'm sorry. It's my fault for mentioning that...\nEveryone, please calm down. I shouldn't have been so irresponsible as to mention the details of an investigation still in progress."
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "The source of the fire is still being investigated by the firefighters. We still don't know whether or not the circuit breaker is what actually caused it. As it is currently, we can't judge it as a mistake on the contractor's part."
 hide akasaka_v001
 with Dissolve(0.2)
 show keiichi_v002 normal at mei_left
 show shion_v002 normal at mei_right
 with Dissolve(0.5)
 show shion_v002 normal at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yeah... making their construction work out to be faulty on your own isn't that great, especially when it could be multiple unfortunate accidents comboed into one."
 show keiichi_v002 normal at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...But even if we consider that the contractors didn't do this out of ill will, isn't it the truth that this was a man-caused accident?"
 hide shion_v002
 hide keiichi_v002
 with Dissolve(0.2)
 show akasaka_v001 normal at mei_center
 with Dissolve(0.5)
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "That's bias speaking, Sonozaki-san. Assuming that there was ill will on the other end can muddle out the truth."
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'As youth, I want you kids to see this situation in an unbiased light, at the very least.'
 hide akasaka_v001
 with Dissolve(0.2)
 show battler_v001 normal at mei_right
 show jessica_v001 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'For sure... by seeing it from a one-sided viewpoint while depending on incomplete information, the truth gets that much harder to see.'
 show battler_v001 normal at inactive
 show jessica_v001 fuan at active
 show jessica_v001 fuan at chara_shake_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Monsters are scary, but human bias is just as bad.\n...But seriously, never mind monsters, Mom is gonna be {i}terrifying{/i}...\nWhat should I do, Battler~?'
 stop music fadeout 0.5
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show rena_v002 normal at mei_left
 show akasaka_v001 normal at mei_right
 with Dissolve(0.5)
 show akasaka_v001 normal at inactive
 show rena_v002 normal at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... but no one died, right? And no one was injured?'
 show rena_v002 normal at inactive
 show akasaka_v001 odoroki at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Huh? Ah, well... this is all I've heard at present, but a few people fell and sustained minor injuries... but it seems like none are gravely wounded."
 show rena_v002 normal at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'We were able to guide the evacuees to safety, seemingly thanks to our training and knowledge of emergency procedures. Even the firemen were commending us for how well it went.'
 show akasaka_v001 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Oh, wow... thank goodness. I think a big congratulations is in order, then!'
 hide akasaka_v001
 hide rena_v002
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Rena-san...'
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB3.ogg"
 hide kazuho_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show rika_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "She's right. There's always the bright side, like how a fire can guarantee an insurance payout. We can't think of it as a complete loss."
 show nao_v002 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. You can't substitute human lives with money. \nThe damage might be too great to say there's a silver lining, though..."
 hide rika_v002
 hide nao_v002
 with Dissolve(0.2)
 show battler_v001 normal at mei_right
 show jessica_v001 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...True. They say, "While there\'s life, there\'s hope.".'
 show battler_v001 normal at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'For sure. Considering the issues that would arise if people did die, this outcome is {i}miles{/i} better.'
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show kazuho_v002 normal at mei_center
 with Dissolve(0.5)
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Jessica-san...'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Behind that laughing face, a show of courage appeared.'
 narrator 'But in this time of us trying to quell our anxiousness... while it might be rude, I thought that was very admirable of her.'
 narrator "That Jessica-san is well brought up. I'm sure her mother and father are both wonderful people too..."
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well, setting the contractor issue aside, I now know that Hinamizawa is a great village. The people here are loveable, it's fun here; {i}so{/i} much to like."
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "If the conversation about whether they'll rebuild the hot spring district comes up and my mom gets worried, I'll pump my chest out and persuade the hell out of her!"
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Sorry for giving you unpleasant memories.\n...If you'd like, next time you come we can play around like normal."
 show battler_v001 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Oh, hell yeah! Can I bring my little sister too next time?'
 hide mion_v002
 show rena_v002 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau~, Battler-san has a little sister?'
 show rena_v002 smile at inactive
 show battler_v001 smile at active
 show battler_v001 smile at nod_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yup. She's far from us in age though, so she's still tiny.\nI'll get her to get along with you guys if you want!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide battler_v001
 hide rena_v002
 hide fade onlayer curtain
 show rena_v002 smile_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show rena_v002 smile_blush at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'A tiny little sister... Hauuuu...!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rena_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show shion_v002 fuan at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Rena-san, you're drooling."
 show shion_v002 fuan at inactive
 show nao_v002 smile_blush at active
 show nao_v002 smile_blush at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I-I'd love to baby her too!"
 hide shion_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 smile_blush at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep, please do bring her at all costs.'
 show nao_v002 smile_blush at inactive
 show rika_v002 smile_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'No one will want to deal with a place that they can make unpleasant memories... but just ending it with that is really lonely.'
 hide nao_v002
 show akasaka_v001 smile at mei_left
 with Dissolve(0.5)
 show rika_v002 smile_close at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Yeah, just like Rika-chan says.'
 show rika_v002 smile_close at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Trying to avoid unpleasant memories is such a waste, in my opinion, because then you miss out on the pleasant ones too.'
 show akasaka_v001 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Does Akasaka have any good memories of Hinamizawa?'
 show rika_v002 smile at inactive
 show akasaka_v001 smile at active
 show akasaka_v001 smile at nod_transform
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Of course, I have a bunch...\nIt's all because Rika-chan and everyone have been so sweet to me."
 show rika_v002 smile at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "I'll bring my daughter next time. I anticipate she'll really love it here too."
 hide rika_v002
 hide akasaka_v001
 with Dissolve(0.2)
 show miyuki_v002 smile_close at mei_center
 with Dissolve(0.5)
 show miyuki_v002 smile_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '............'
 hide miyuki_v002
 with Dissolve(0.2)
 show battler_v001 smile at mei_center
 with Dissolve(0.5)
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Alright... if the detective is gonna say all that, now I gotta do everything in my power to come here with my lil' sis!"
 hide battler_v001
 with Dissolve(0.2)
 show hanyuu_v002 smile at mei_left
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, everyone will welcome her with open arms!'
 show hanyuu_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'll be waiting patiently! I'm going to offer her the pampering of a lifetime~!"
 hide hanyuu_v002
 show keiichi_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") '...When Satoko says it, it makes me kind of worried.'
 show keiichi_v002 fuan at inactive
 show satoko_v002 odoroki at active
 show satoko_v002 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Keiichi-san?! We just had a conversation earlier about not jumping to biased conclusions!!'
 hide keiichi_v002
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 odoroki at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-Ahahaha...'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide satoko_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show black_cover as bg
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 narrator 'As I stealthily eavesdrop on them, I have clear vision of Onii-chan raising his voice and laughing.'
 narrator 'Is this... a dream... or an illusion...?'
 narrator 'In this past world that may or may not have ever existed, the scene of Onii-chan and his friends seemingly having a great time together plays out right before my eyes. Without thinking, I start running towards--'
 narrator '............'
 stop sound
 show expression 'images/bg/AdvBg_601.png' as bg
 stop music fadeout 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") '...Lady, hey, Lady...'
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") 'Get a grip, Lady...!'
 play audio 'audio/sfx/SE_5037_getup.wav'
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '......nn... uh...'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_481.png' as bg
 play music "<loop 0>audio/bgm/BGM_EVENT_TOP_COLLAB3.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") 'Ah, you came to! When I saw you slumped over on these stone steps, I thought I was gonna have a heart attack...!'
 show ange_v001 fuan at mei_center
 with Dissolve(0.5)
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Where... am I...?'
 hide ange_v001
 with Dissolve(0.2)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "Where? ...Did you hit your head? We're at the dam, where Hinamizawa was flooded. Look for yourself."
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 hide ange_v001
 with Dissolve(0.2)
 narrator 'Looking down, I saw we had stopped midway going up some stone steps. They continue much farther up the mountain... stretching all the way to the dam.'
 narrator 'The landscape that used to be visible from the high ground was nowhere to be seen... vanishing as though all it had ever been was a mirage.'
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "What's the matter, Lady? You dream about something by chance?"
 show ange_v001 normal_close at mei_center
 with Dissolve(0.5)
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'A dream...\nYeah, surely that was a dream...'
 hide ange_v001
 with Dissolve(0.2)
 narrator 'But to brush it off as all a wild fantasy is difficult, given how vivid it was.'
 show ange_v001 normal_close at mei_center
 with Dissolve(0.5)
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '(...And plus......)'
 hide ange_v001
 with Dissolve(0.2)
 narrator 'While I barely remembered Onii-chan and Jessica Onee-chan... I was completely unable to recognize the faces of the village girls.'
 narrator 'Their existence clearly differs from the kind in my imagination, like Maria Onee-chan and the Seven Stakes. No, rather than them being imaginary, it was more like...'
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...I may have come into contact with ghosts.'
 hide ange_v001
 with Dissolve(0.2)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") 'Huh? Sorry, Lady, you wanna say that again? I missed what you said. Just one more time...'
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Ignore it. ...Let's head back to the car right away. I want to go to the hotel and sleep."
 hide ange_v001
 with Dissolve(0.2)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") 'Uhh, Ange-san...?'
 narrator 'While complaining about still having leftover regrets or something, my escort faithfully attended to his duty and followed behind me.'
 narrator 'Looking back at him over my shoulder, I let out a stifled laugh. For some reason, I felt refreshed as we continued walking to where the car was parked.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_261.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hinamizawa... huh...?'
 narrator "I'll try to find some primary sources the next time I'm back in Tokyo. This might not exactly be what I'm looking for right now, but it should be a good distraction."
 narrator 'As I think that, I look up at the sky.'
 play audio 'audio/sfx/SE_402_higurashi1.wav'
 narrator 'The surrounding noise of the Higurashi chirping felt incredibly shrill--'
 call chapter_end
 
 $ persistent.umi2_done = True
 return