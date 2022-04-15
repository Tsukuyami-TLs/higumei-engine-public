label chara492001_01:
 show black_background onlayer black
 $ event_store.current_event='chara492001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara492001_01'
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
 show expression 'images/bg/AdvBg_663.png' as bg
 play music "<loop 0>audio/bgm/BGM_BOSS1_COLLAB3.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show ange_v001 sinken at mei_center
 with Dissolve(0.5)
 show ange_v001 sinken at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'So damn... persistent!! Just hurry up and drop deeaad!!!'
 play audio 'audio/sfx/SE_101_hit_strike1.wav'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide ange_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 Character('Tsukuyami',ctc="ctcArrow", ctc_position="fixed") '{b}Gyooooooooooohhhhhh!!!{/b}'
 play audio 'audio/sfx/SE_5013_down.wav'
 stop music fadeout 0.5
 pause 1.0
 show ange_v001 sinken at mei_center
 with Dissolve(0.5)
 show ange_v001 sinken at active
 show ange_v001 sinken at updown_shake_transform
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Haaah, haaah, haahh... This should be all of them...'
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB3.ogg"
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Those outlandish creatures put up a fight, but it seems I was able to take them all down... ah?'
 play audio 'audio/sfx/SE_057_gacha_allFlash.wav'
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'The "Card" went back to normal... so is this also magic? What could this power even be?'
 show ange_v001 sinken at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Honestly, suddenly getting burdened with being dumped into this "World" I\'ve never seen before... leave the jokes for that hot spring district...... gh!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide ange_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/card/Card_492001.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'W-Why... am I getting lightheaded all of a sudden... my strength is...'
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'L-Look outtt!!'
 play audio 'audio/sfx/SE_229_grap.wav'
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Eh... kya...?!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_663.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show miyuki_v002 smile at mei_right
 show ange_v001 fuan at mei_left
 with Dissolve(0.5)
 show ange_v001 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Phew... we're good. Just a little more and you would have been tumbling down to the bottom of a gorge. You okay?"
 show miyuki_v002 smile at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Th-thank you. Without you reaching your hand out for me, I would be a goner.'
 show ange_v001 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "You're welcome. ...But walking around alone in the middle of the mountains at this time of night is way too dangerous."
 show ange_v001 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Where are you from? I haven't seen your face around Hinamizawa... so could you be a customer for the lodging facility?"
 show miyuki_v002 smile at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Yeah, let's say that. And who are you guys?"
 show ange_v001 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "As you can tell, I'm a resident of Hinamizawa. ...Well, the details in how I got to this village are complicated though, so don't pry too deeply into it and we'll be fine."
 hide miyuki_v002
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show ange_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "You don't need to tell her that, Miyuki. But more importantly, are you hurt at all?"
 show nao_v002 normal at inactive
 show ange_v001 normal at active
 show ange_v001 normal at nod_transform
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "No, I'll survive. ...But anyway, why are you two even here?"
 hide nao_v002
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show ange_v001 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'We came from the high ground on the shrine you can see over there, and we were heading towards the hot spring district, but Kazuho... ah, this girl here.'
 show ange_v001 normal at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'She said she felt a presense and then heard some noises from the shrine grounds, so the three of us came to investigate just in case.'
 show miyuki_v002 smile at inactive
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...I see. Even though there shouldn't have been people nearby, you saved my life."
 hide miyuki_v002
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 show ange_v001 normal_close at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Eh? Ah, um... I'm sorry."
 show kazuho_v002 fuan at inactive
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...? Why are you apologizing? I was just expressing my thanks, but if you heard it as ill-willed I'll apolo...gize..."
 show ange_v001 fuan_close at chara_shake_transform
 show ange_v001 fuan_close at chara_shake_transform:
  yanchor 1.0
  linear 0.5 pos (480,1250)
 pause 0.5
 show ange_v001 fuan_close:
  yanchor 1.0
  pos (480,1250)
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 pause 1.0
 show ange_v001 fuan_close at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "W-wh-... what's the matter? Your legs are trembling... wait, you're drenched in sweat!"
 show kazuho_v002 odoroki at inactive
 show ange_v001 fuan_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "It's not actually a huge deal... I was just kind of... swarmed by an absurd amount of monsters and outdid... my...self."
 play audio 'audio/sfx/SE_5013_down.wav'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide ange_v001
 hide kazuho_v002
 hide fade onlayer curtain
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ple-... please keep it together! Miyuki-chan, get Dr. Irie, now!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...an......'
 stop music fadeout 0.5
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Onii...cha...n......'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_373.png' as bg
 pause 1.0
 play music "<loop 0>audio/bgm/BGM_QUEST2_COLLAB3.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show ange_v001 fuan at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5037_getup.wav'
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...n......ah...?'
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Where... am I? Why am I in a bed...?'
 hide ange_v001
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_right
 show ange_v001 fuan at mei_left
 with Dissolve(0.5)
 show ange_v001 fuan at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah... looks like you've finally came to? Thank goodness..."
 show kazuho_v002 smile at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'You guys just said we were behind the shrine in the mountains...'
 show kazuho_v002 smile at inactive
 show ange_v001 odoroki at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "You're telling me... the sun... has already risen...?"
 show ange_v001 odoroki at inactive
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at nod_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Yeah. You've been asleep the whole night."
 hide ange_v001
 hide kazuho_v002
 with Dissolve(0.2)
 show miyuki_v002 fuan at mei_center
 with Dissolve(0.5)
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Yeahhh, you gave us quite a shock. Right in the middle of us talking, you suddenly lost consciousness or something and fell over on the spot.'
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'So, we called up the doctor from this clinic to rush over with his car, and we carried you in.'
 hide miyuki_v002
 with Dissolve(0.2)
 show ange_v001 fuan_close at mei_left
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show ange_v001 fuan_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm sorry. I must have caused a lot of trouble."
 show ange_v001 fuan_close at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Mmm, the feeling is mutual. We were forcing you past your limits chatting, but the fact that you woke up is relieving.'
 show kazuho_v002 smile at inactive
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Huh... so you guys... stayed up the whole night?'
 hide kazuho_v002
 show miyuki_v002 smile at mei_right
 with Dissolve(0.5)
 show ange_v001 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'No, no. Staying up all night would be crazy. We napped on the beds and sofas in the other room and just woke up a bit before you did.'
 show ange_v001 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "But no, this really was good timing. It wouldn't have been strange at all if we found that you left without a word while we were asleep."
 show miyuki_v002 smile at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Forgive me. You saved me, so I would at least express my gratitude before leaving. I'd feel bad otherwise."
 show miyuki_v002 smile at inactive
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Well, if someone who just woke up told me that they felt {i}good{/i}, I would think they were lying anyway.'
 show ange_v001 normal_close at inactive
 show miyuki_v002 smile at active
 show miyuki_v002 smile at updown_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ahahaha, good one! I'm gonna write that down in my joke book after."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show ange_v001 normal_close at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'So... this is the real question at hand. Last night... what did you see on the shrine grounds?'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show miyuki_v002 normal at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'What did I see? What about it do you want to hear?'
 hide miyuki_v002
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show ange_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm not sure if I understood properly, so it'll be hard to explain... but before you lost consciousness, you mentioned that you fought against monsters."
 show ange_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'After Dr. Irie examined you, he said you overworked yourself past your limits. What were you doing in the back mountains fighting those monsters?'
 show nao_v002 normal at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "What I was... obviously I was killing monsters. Don't you guys fight those unidentifable creatures too?"
 hide ange_v001
 hide nao_v002
 with Dissolve(0.2)
 show kazuho_v002 normal at mei_left
 show miyuki_v002 normal at mei_center
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at active
 show miyuki_v002 normal at active
 show kazuho_v002 normal at active
 Character('The Three',ctc="ctcArrow", ctc_position="fixed") '............'
 hide nao_v002
 hide miyuki_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show ange_v001 normal at mei_left
 show miyuki_v002 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v002 normal at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "What's so odd about that? You guys are making awfully meek faces."
 show ange_v001 normal at inactive
 show miyuki_v002 normal_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm, no, it's definitely just like you say... but I, like, wonder if we can get you to forget somehow..."
 show miyuki_v002 normal_close at inactive
 show ange_v001 sinken at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...What do you mean?'
 hide miyuki_v002
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show ange_v001 sinken at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'It would be really bad if the existence of "those things" that you witnessed became well-known outside of the village. You... can see why, right?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide ange_v001
 hide nao_v002
 hide fade onlayer curtain
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "U-Um... I'm fully aware that what we're asking is an impossible demand!"
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "But...! After Hinamizawa had gone through so much to have an atmosphere that can now be considered nice, we don't want... a troublesome rumor to spread about and ruin that...!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show ange_v001 normal_close at mei_center
 with Dissolve(0.5)
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Relax. Nothing I know has meaning regarding this "World", let alone how little my own existence matters here.'
 hide ange_v001
 with Dissolve(0.2)
 show miyuki_v002 fuan at mei_right
 show ange_v001 normal at mei_left
 with Dissolve(0.5)
 show ange_v001 normal at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...? What does that mean?'
 show miyuki_v002 fuan at inactive
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Exactly as I\'m saying. Because I\'m not a person from this "World"...'
 hide miyuki_v002
 show kazuho_v002 odoroki at mei_right
 with Dissolve(0.5)
 show ange_v001 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh... Y-You too, then?'
 show kazuho_v002 odoroki at inactive
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Wh-?'
 call chapter_end
 jump chara492001_02