label chara482001_01:
 show black_background onlayer black
 $ event_store.current_event='chara482001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara482001_01'
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
 show expression 'images/bg/AdvBg_171.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_141.png' as bg
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB3.ogg"
 call wipein_routine
 show jessica_v001 smile at mei_right
 show battler_v001 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Oooh...! The night sky was great, but so is the view by daylight! Not sure if it's because the air is so clean, but I can see really far."
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 show battler_v001 smile at nod_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yeah, you said it! After this, I'm going back over to that hot spring to relax..."
 show jessica_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...But the problem is what we do after that.\nJessica, how much you have on hand?'
 show battler_v001 fuan at inactive
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Huh...? Wait, Battler, you're tight on cash too?"
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Um... what's the matter? The two of you look like you've seen a ghost."
 hide kazuho_v002
 with Dissolve(0.2)
 show battler_v001 fuan_close at mei_left
 show jessica_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show jessica_v001 fuan_close at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well... we couldn't imagine the lodging facility'd get burnt down like that, y'know? While we were looking for Jessica, my wallet, uh... yeah."
 show battler_v001 fuan_close at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I-I thought it would be bad if I lost my wallet in a place I wasn't familiar with... so I put it in with my luggage..."
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...In other words, you left them behind at the inn that burnt down, so you're both penniless."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade onlayer curtain
 show battler_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I-I'm not broke! Here, look at all these credit cards! I didn't forget them when I headed out today! "
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v002 fuan at mei_right
 show battler_v001 sinken at mei_left
 with Dissolve(0.5)
 show battler_v001 sinken at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Uh, sorry, Battler-san. Hinamizawa's only banking institution is the post office. And today is Sunday..."
 show mion_v002 fuan at inactive
 show battler_v001 fuan_close at active
 show battler_v001 fuan_close at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Y-You're joking...! Where are we gonna stay tonight then?"
 hide mion_v002
 show jessica_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Mmm... we'd need to hail a taxi to take us to Gogura if it comes down to it. That kind of town will probably have an ATM too. "
 show battler_v001 fuan_close at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Nah, but then it would be a pain to get back to Hinamizawa.'
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 show miyuki_v002 normal at mei_right
 show keiichi_v002 normal at mei_left
 with Dissolve(0.5)
 show keiichi_v002 normal at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Hey, Maebara-kun, could I ask for your opinion on something?'
 show miyuki_v002 normal at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Oh... Miyuki-chan, were you maybe thinking the same thing I was? You saved me the effort of asking you about it if so.'
 hide keiichi_v002
 show battler_v001 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...? What's up, Keiichi and Miyuki-chan? What are you talking about?"
 show battler_v001 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Well, actually, I have a suggestion here for the two of you.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide miyuki_v002
 hide battler_v001
 with Dissolve(0.2)
 pause 1.0
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show battler_v001 odoroki at mei_center
 with Dissolve(0.5)
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Keiichi's house is a homestay...?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show keiichi_v002 smile at mei_center
 with Dissolve(0.5)
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yeah. My family's currently living at their second house in Okinomiya for a bit due to some stuff. So, at our house in Hinamizawa, I have these three here..."
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "...Kazuho-chan, Miyuki-chan, and Nao-chan all sleeping over... I say that, but it's more like they dorm there."
 hide keiichi_v002
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_right
 show keiichi_v002 smile at mei_left
 with Dissolve(0.5)
 show keiichi_v002 smile at inactive
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So, what you're saying is... two more people can stay there?"
 show keiichi_v002 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "We have a guesthouse too, but it's on the same island as the main one. I'd love to have a place away from the island all to myself."
 hide keiichi_v002
 show battler_v001 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...You live in that stupid big mansion and still want a house? I think that's a bit excessive."
 show battler_v001 fuan at inactive
 show jessica_v001 sinken at active
 show jessica_v001 sinken at chara_shake_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "S-Shut up! The size of the place doesn't matter when you have Gramps being moody and Mom giving her constant lectures. Every day there feels suffocating."
 show battler_v001 fuan at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Even if it's cramped, I still want to try living a life where I can stretch my wings every so often."
 show jessica_v001 fuan_close at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Mmm, well... I think that you living on your own depends on the situation, though. Could you imagine life without the servants?'
 show battler_v001 fuan at inactive
 show jessica_v001 sinken at active
 show jessica_v001 sinken at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Shut up, for real! ...If I wanted to get back at you, I could have said the same thing about you.'
 play audio 'audio/sfx/SE_374_ls_question.wav'
 show jessica_v001 sinken at inactive
 show battler_v001 futeki at active
 show battler_v001 futeki at updown_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Ihihihihi~, okaay, okay. I didn't mean it, so why don't you let me rub those boobs of yours as an apology?"
 camera at screenshake_transform
 pause 0.0
 show battler_v001 futeki at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hey, don't get cocky!"
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(...Battler-san said he was born to a rich family, but I wonder if something bad happened at home...?)'
 hide kazuho_v002
 with Dissolve(0.2)
 show battler_v001 normal at mei_left
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So that means that me and Jessica will be staying at Keiichi's house while we're in Hinamizawa, and we'll get looked after by these three...?"
 show battler_v001 normal at inactive
 show kazuho_v002 smile at active
 show kazuho_v002 smile at nod_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah... y-yes. I'll do my best to be hospitable in place of Maebara-kun!"
 show kazuho_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "You're already accommodating for me, so you don't have to fuss about it that much. As long as Jessica's with me, that's all I can ask for! "
 hide kazuho_v002
 hide battler_v001
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Would it be ok if Jessica-san stays upstairs with us while Battler-san stays on the first floor then?'
 show nao_v002 smile at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Of course! Hehe, it'll be just like a school trip!"
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 show rena_v002 smile at mei_center
 with Dissolve(0.5)
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau~, then maybe Rena will help out with dinner, with dinner!\nI'll make a ton of tasty food!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rena_v002
 hide fade onlayer curtain
 show nao_v002 smile_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show nao_v002 smile_blush at active
 show nao_v002 smile_blush at jumping_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "W-Waah... Rena-chan's home cooking...! Now I might have a bunch of fun... maybe...!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v002 fuan at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah, is staying here alright, though? If you go back after we finish work rather than go now, wouldn't it be bad for you...?"
 show mion_v002 fuan at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Nah, I'm fine with that. Apparently, the root of our current situation is because the contractor my dad hired's been cutting corners to pocket more cash. "
 show mion_v002 fuan at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Saying this sucks, but the house is getting chaotic thanks to that... so if we go back now, it'll just be a massive pain."
 hide mion_v002
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 fuan_close at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I see. In that case, please take it easy here as long as you're able to."
 hide jessica_v001
 hide kazuho_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "By the way, if you're considering sneaking up to the second floor while we're sleeping... don't."
 show nao_v002 normal at inactive
 show miyuki_v002 smile_close at active
 show miyuki_v002 smile_close at nod_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Yup, yup. Kazuho would kick your ass instinctively.'
 hide miyuki_v002
 hide nao_v002
 with Dissolve(0.2)
 show battler_v001 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "No, no, I'm not planning on doing anything as thoughtless as that when you're being so generous to me."
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...I mean, this one is Kazuho-chan, right? This cute, well-behaved looking girl would do that...?'
 hide battler_v001
 with Dissolve(0.2)
 show rena_v002 smile at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... Battler-san, Kazuho-chan is pretty strong. She's kyute and super reliable too♪"
 show rena_v002 smile at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'C-Compared to me, Rena is way stronger, though...'
 hide kazuho_v002
 hide rena_v002
 with Dissolve(0.2)
 show keiichi_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show keiichi_v002 fuan_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "...From my point of view, you're both pretty powerful."
 hide keiichi_v002
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_left
 show hanyuu_v002 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'That would become quite the meaningless battle.'
 show satoko_v002 fuan at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au. Rena is super powerful, but when Kazuho gets prepared for the worst, their power is neck to neck!'
 hide satoko_v002
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. It doesn't matter who they're facing; they'll mow the enemy down. "
 hide hanyuu_v002
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "The strength to face anything runs in the Kimiyoshi blood. That reminds me; that's just like Grandpa Kimiyoshi. "
 hide rika_v002
 hide mion_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'R-Really...?'
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(W-What should I do... I don't remember anything about my grandpa!)"
 hide kazuho_v002
 with Dissolve(0.2)
 show battler_v001 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Heh, so Kazuho-chan takes after her grandpa? People tell me I take after my grandfather too. We might be kindred spirits.'
 show battler_v001 smile at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'By grandfather... you mean {i}our{/i} grandfather? Never heard that before. Who told you that?'
 show jessica_v001 normal at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Not sure? But I do remember it happened at some point.'
 show battler_v001 smile at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "This isn't a joke...! If that's true, you're gonna be just like Grandfather in the future."
 show battler_v001 smile at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "He's the only person who'd be so preoccupied with studying black magic and alchemy that he'd seclude himself in the study spraying mysterious chemicals everywhere."
 show jessica_v001 fuan_close at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Nah, I don't think I'd go {i}that{/i} far..."
 hide battler_v001
 show miyuki_v002 normal at mei_left
 with Dissolve(0.5)
 show jessica_v001 fuan_close at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Alchemy... I think that was the foundation that modern science is based on. Wasn't its ultimate goal to create gold?"
 show miyuki_v002 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Oh, you're familiar with it. Um..."
 show jessica_v001 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'You can call me Miyuki. I remember reading about alchemy in some sort of book a while back.'
 hide miyuki_v002
 show satoko_v002 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "But... he sounds like an interesting grandfather. I'd love to meet him sometime~!"
 show satoko_v002 smile at inactive
 show jessica_v001 fuan_close at active
 show jessica_v001 fuan_close at deepbreath_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Nah... You probably wouldn't be saying that if you actually saw him... Like I don't know what he's thinking even as his grandkid."
 hide jessica_v001
 hide satoko_v002
 with Dissolve(0.2)
 show mion_v002 fuan at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Maybe Jessica-san's granddad is the same type of person as Granny?"
 show mion_v002 fuan at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'That hag would probably take a liking to him.\n...You wanna try introducing her to Battler-san?'
 show shion_v002 smile at inactive
 show mion_v002 fuan_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'd love to, but it's been pretty chaotic at the house since we've been dealing with the aftermath too..."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show rika_v002 smile at mei_right
 show battler_v001 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. I'm excited to see what the future holds for Battler. Does anybody want to place bets on it?"
 show rika_v002 smile at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hey, hey, starting a betting pool based on somebody else's life... the people of Hinamizawa really don't hold back, do they?"
 hide rika_v002
 show keiichi_v002 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 odoroki at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Our club members are something special... \nBut... when that's coming from someone already in the group, it probably doesn't hold much weight, does it...?"
 hide battler_v001
 hide keiichi_v002
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-Ahahaha......'
 hide kazuho_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show battler_v001 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'By the way, you play a bunch of different games with each other in your club activities, right...?'
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Just going off of what I've heard, it seems interesting.\nGiven this cast of characters, though, it definitely gets weird."
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 show keiichi_v002 smile at mei_left
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "...This is getting off topic. Well, since we solved the problem of where you're going to stay, why don't we take you two around Hinamizawa?"
 show keiichi_v002 smile at inactive
 show rena_v002 smile at active
 show rena_v002 smile at nod_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Yeah, yeah, Rena has nooo objections♪ Where do you two want to go?'
 hide rena_v002
 hide keiichi_v002
 with Dissolve(0.2)
 show battler_v001 normal at mei_center
 with Dissolve(0.5)
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Oh, yeah, for the meantime...'
 show battler_v001 fuan_close at active
 show battler_v001 fuan_close at chara_shake_transform
 show battler_v001 fuan_close at chara_shake_transform:
  yanchor 1.0
  linear 0.5 pos (960,1250)
 pause 0.5
 show battler_v001 fuan_close:
  yanchor 1.0
  pos (960,1250)
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...I'm hungry."
 hide battler_v001
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_right
 show battler_v001 fuan_close at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "You're... really saying that? And saying it now?! It was only a little while ago that Rena-chan brought us a mountain of onigiri!"
 show jessica_v001 odoroki at inactive
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Yeah, and that was delicious! The entire mountain was gone before I realized it!'
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 show rena_v002 fuan at mei_center
 with Dissolve(0.5)
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... I'm sorry, was it not enough?"
 hide rena_v002
 with Dissolve(0.2)
 show jessica_v001 fuan at mei_right
 show battler_v001 sinken at mei_left
 with Dissolve(0.5)
 show battler_v001 sinken at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'This one eats like a pig... like he takes up {i}way{/i} too much fuel. How many calories do you even need to support that body of yours?'
 show jessica_v001 fuan at inactive
 show battler_v001 sinken at active
 show battler_v001 sinken at jump_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "S-Shut up! It's a growth spurt!"
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 show shion_v002 odoroki at mei_center
 with Dissolve(0.5)
 show shion_v002 odoroki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If that's true, it means you're still growing... that's scary."
 hide shion_v002
 with Dissolve(0.2)
 show miyuki_v002 normal at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Mmm, if eating lots of onigiri is supposed to make you taller, does that mean Kazuho is trying to get taller?'
 show miyuki_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'W-Who knows...?'
 hide miyuki_v002
 show nao_v002 fuan_close at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "This girl's just a glutton."
 show nao_v002 fuan_close at inactive
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Gh?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide nao_v002
 hide fade onlayer curtain
 show keiichi_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'So the move is getting some tasty food then? I know a good place if so!'
 play audio 'audio/sfx/SE_226_shine.wav'
 show keiichi_v002 futeki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Which means there's absolutely no chance we're {i}not{/i} bringing Battler over there!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show battler_v001 fuan at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Y-You sound pretty confident...'
 hide battler_v001
 with Dissolve(0.2)
 show rika_v002 smile at mei_left
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. I know where Keiichi wants to go.'
 show rika_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Yeah, me too.'
 hide rika_v002
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Can't think of anywhere else."
 hide miyuki_v002
 hide mion_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show battler_v001 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Woah, wait, wait, all of you can already tell? This place has to be the best in town, huh?'
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Ah~, I'm looking forward to it!!"
 call chapter_end
 jump chara482001_02