label chara072016_02:
 show black_background onlayer black
 $ event_store.current_event='chara072016'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072016_02'
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
 show expression 'images/bg/AdvBg_741.png' as bg
 play music "<loop 0>audio/bgm/BGM_BATTLE1_hiru.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v023 sinken at mei_center
 with Dissolve(0.5)
 show rika_v023 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '--Haaah!'
 hide rika_v023
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_117_hit_heavystrike.wav'
 camera at screenshake_transform
 pause 0.0
 Character('Tsukuyami',ctc="ctcArrow", ctc_position="fixed") '{b}Giiiiiiiiiiiiiiii!!{/b}'
 stop music fadeout 1.0
 show rika_v023 fuan at mei_center
 with Dissolve(0.5)
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'W-We barely defeated them...'
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide rika_v023
 with Dissolve(0.2)
 show miyuki_v002 odoroki at mei_left
 show keiichi_v002 normal at mei_right
 with Dissolve(0.5)
 show keiichi_v002 normal at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'To think that Rika-chan, Kazuho, Nao, Maebara-kun, and Battler-san could have... only just barely destroyed them...'
 show miyuki_v002 odoroki at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "I'm glad I split off from Mion and helped you guys out.\n...Guess I'll have to apologize later."
 hide miyuki_v002
 with Dissolve(0.3)
 show battler_v001 fuan at mei_left
 with Dissolve(0.5)
 show keiichi_v002 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Worst case, we could have gotten surrounded with that many of em. ...If we get back, I'm sure the workload for us is gonna be far worse, though."
 hide keiichi_v002
 hide battler_v001
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_right
 show rika_v023 fuan at mei_left
 with Dissolve(0.5)
 show rika_v023 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'By the way, Rika-chan... I think we had this conversation earlier too, but why are you in that getup?'
 show kazuho_v002 fuan at inactive
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...I don\'t really know either. I found myself dressed like this even though I used what should be my usual "Card"...'
 show kazuho_v002 fuan at inactive
 show rika_v023 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It doesn't give me any issues while fighting though, so I don't think it's anything bad..."
 hide kazuho_v002
 with Dissolve(0.3)
 show miyuki_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v023 normal at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "You got like that with your usual {b}Role Card{/b}, huh? And like, what's up with that eyepatch...?"
 play audio 'audio/sfx/SE_5037_getup.wav'
 show miyuki_v002 normal at inactive
 show rika_v023 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. My right eye is still there. This eyepatch seems to be part of the outfit itself.'
 hide miyuki_v002
 with Dissolve(0.3)
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show rika_v023 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Has something like this happened at any point up to now?'
 show nao_v002 normal at inactive
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "This is the first time I've paid this much attention to it, so I'm stuck wondering about that too!"
 hide nao_v002
 with Dissolve(0.3)
 show battler_v001 normal at mei_right
 with Dissolve(0.5)
 show rika_v023 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "That said, there's gotta be some sort of reason this happens. Anything you can remember?"
 show battler_v001 normal at inactive
 show rika_v023 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Nothing at all...'
 hide battler_v001
 with Dissolve(0.3)
 show keiichi_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v023 fuan_close at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Even if we do try to find out that reason, this fit's way too skimpy for her."
 hide keiichi_v002
 with Dissolve(0.3)
 show battler_v001 normal at mei_right
 with Dissolve(0.5)
 show rika_v023 fuan_close at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Maybe the direct reason isn't actually Rika-chan?"
 show battler_v001 normal at inactive
 show rika_v023 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'What do you mean, Battler?'
 show rika_v023 normal at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'For example, some other person could be causing this indirectly through other means... stuff like that.'
 hide rika_v023
 with Dissolve(0.3)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 normal_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So you're saying that Rika just got caught in the middle?"
 show nao_v002 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Yeah. I can only speculate without knowing the main cause, though.'
 hide battler_v001
 hide nao_v002
 with Dissolve(0.2)
 show miyuki_v002 normal at mei_right
 show rika_v023 normal at mei_left
 with Dissolve(0.5)
 show rika_v023 normal at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "But we also know Rika-chan herself doesn't even remember.\n...So with that in mind, have you been staying in shape?"
 show miyuki_v002 normal at inactive
 show rika_v023 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. I'm fine there too."
 hide miyuki_v002
 with Dissolve(0.3)
 show nao_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v023 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's probably okay to assume nothing will become of it at this very moment, then."
 hide nao_v002
 with Dissolve(0.3)
 show keiichi_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v023 normal at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'But if something does happen, let us know right away, alright?'
 show keiichi_v002 fuan at inactive
 show rika_v023 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Thank you, Keiichi. Everyone and Battler, too, I'm so glad you all keep me in your thoughts."
 hide keiichi_v002
 with Dissolve(0.2)
 show battler_v001 futeki at mei_right
 with Dissolve(0.5)
 show rika_v023 smile at inactive
 show battler_v001 futeki at active
 show battler_v001 futeki at updown_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yeah! As thanks, promise me that you'll let me ruuuub thooose boobies when you grow up! Ihihihi~!"
 show battler_v001 futeki at inactive
 show rika_v023 fuan at active
 show rika_v023 fuan:
  yanchor 1.0
  linear 0.5 pos (470,1200)
 pause 0.5
 show rika_v023 fuan:
  yanchor 1.0
  pos (470,1200)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Me-meep...'
 hide battler_v001
 with Dissolve(0.2)
 show nao_v002 fuan_close at mei_right
 with Dissolve(0.5)
 show rika_v023 fuan at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "He'd be great if he didn't say  stuff like that..."
 hide rika_v023
 with Dissolve(0.2)
 show kazuho_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan_close at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wait, wait... ah-, huh?'
 stop music fadeout 1.0
 hide nao_v002
 with Dissolve(0.2)
 show miyuki_v002 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v002 normal at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "What's wrong, Kazuho?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide miyuki_v002
 hide fade onlayer curtain
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play music "<loop 0>audio/bgm/BGM_BATTLE2_hiru.ogg"
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jump_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "There's a Tsukuyami over there! ...Ah, it ran off, it's running!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show battler_v001 odoroki at mei_center
 with Dissolve(0.5)
 show battler_v001 odoroki at active
 show battler_v001 odoroki at jumping_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Whaaat?!'
 hide battler_v001
 with Dissolve(0.2)
 show keiichi_v002 sinken at mei_center
 with Dissolve(0.5)
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "L-Let's follow iiiiit!!"
 hide keiichi_v002
 with Dissolve(0.2)
 show rika_v023 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v023 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's just one thing after another..."
 window hide None
 call wipeout_routine
 play audio 'audio/sfx/SE_408_run.wav'
 hide rika_v023
 with Dissolve(0.2)
 pause 1.0
 stop sound
 show expression 'images/bg/AdvBg_511.png' as bg
 call wipein_routine
 show rika_v023 sinken at mei_center
 with Dissolve(0.5)
 show rika_v023 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Yaaaaaaahhhh!!'
 hide rika_v023
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_117_hit_heavystrike.wav'
 camera at screenshake_transform
 pause 0.0
 Character('Tsukuyami',ctc="ctcArrow", ctc_position="fixed") '{b}Giiiiiiiiiiiiiiii!!{/b}'
 stop music fadeout 0.5
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Haaah, haaah... looks like we made it back to Hinamizawa following this last one.'
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide kazuho_v002
 show battler_v001 fuan_close at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan_close at active
 show battler_v001 fuan_close at chara_shake_transform
 show battler_v001 fuan_close:
  yanchor 1.0
  linear 0.5 pos (960,1300)
 pause 0.5
 show battler_v001 fuan_close:
  yanchor 1.0
  pos (960,1300)
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hiih, hiih, hiiih... am I really that slow?'
 hide battler_v001
 with Dissolve(0.2)
 show keiichi_v002 normal at mei_right
 show battler_v001 fuan_close at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Nah, I think it's just the difference in how accustomed you are to these roads."
 hide keiichi_v002
 with Dissolve(0.3)
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "And besides... Battler-san, you're really tall, so don't you have to find your way around twigs and stuff on these mountain roads?"
 show miyuki_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I did my best to grow up big and strong, but to think there were pitfalls like that... oof.'
 hide battler_v001
 hide miyuki_v002
 with Dissolve(0.2)
 show rika_v023 normal at mei_center
 with Dissolve(0.5)
 show rika_v023 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "My house is a bit this way, so I'll get some tea. Let's rest up so we can return to the inn after."
 window hide None
 play audio 'audio/sfx/SE_408_run.wav'
 pause 0.5
 show rika_v023 normal
 show rika_v023 normal:
  yanchor 1.0
  linear 0.5 pos (2400,1200)
 pause 0.5
 show rika_v023 normal:
  yanchor 1.0
  pos (2400,1200)
 hide rika_v023
 with Dissolve(0.2)
 show battler_v001 normal at mei_center
 with Dissolve(0.5)
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Thanks, Rika-chan... wh-... she dipped.'
 hide battler_v001
 with Dissolve(0.2)
 show nao_v002 normal_close at mei_right
 show battler_v001 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'That girl is super tough.'
 show nao_v002 normal_close at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hiih, hiih... exhausted... can't... walk..."
 hide battler_v001
 with Dissolve(0.3)
 show keiichi_v002 normal at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5037_getup.wav'
 show nao_v002 normal_close at inactive
 show keiichi_v002 normal at active
 show keiichi_v002 normal:
  yanchor 1.0
  linear 0.5 pos (480,1300)
 pause 0.5
 show keiichi_v002 normal:
  yanchor 1.0
  pos (480,1300)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Let's rest here a bit.\nAh, there we go..."
 stop music fadeout 1.0
 hide keiichi_v002
 with Dissolve(0.3)
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...Nn......?'
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 show kazuho_v002 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "What's wrong, Kazuho?"
 show nao_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Eh, ah, mm... I kind of got chills...'
 hide nao_v002
 with Dissolve(0.3)
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Huh... do you have a cold?'
 show miyuki_v002 fuan at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "No, that's not what I meant..."
 window hide None
 call wipeout_routine
 stop music fadeout 0.5
 hide kazuho_v002
 hide miyuki_v002
 with Dissolve(0.2)
 call wipein_routine
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 play music "<loop 5.836>audio/bgm/BGM_EVENT5.ogg"
 show erika_v001 futeki at active
 show erika_v001 futeki at jumping_transform
 Character('????',ctc="ctcArrow", ctc_position="fixed") "I-I've found yooooooooooouuuu!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'What...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide fade onlayer curtain
 show erika_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 futeki at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") "Here you are, here you are, HERE YOU AREEEE...!! I've finally found yooooouuuuuu!!!"
 play audio 'audio/sfx/SE_304_ls_run.wav'
 pause 0.5
 show erika_v001 futeki
 show erika_v001 futeki:
  yanchor 1.0
  linear 0.5 pos (-480,1200)
 pause 0.5
 show erika_v001 futeki:
  yanchor 1.0
  pos (-480,1200)
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show nao_v002 fuan:
  yanchor 1.0
  linear 0.5 pos (940,1200)
 pause 0.5
 show nao_v002 fuan:
  yanchor 1.0
  pos (940,1200)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "W-What's with that person with this flowy, frilly dress...?! Is she coming this way?!"
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 show erika_v001 futeki at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") "I've finally found you, Nao Houtani!"
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show nao_v002 fuan at active
 show nao_v002 fuan at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Hiiiih?!'
 show nao_v002 fuan at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Umm... uh, do you need something from Nao?'
 hide miyuki_v002
 with Dissolve(0.3)
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Nao-chan, do you know this person?'
 show kazuho_v002 fuan at inactive
 show nao_v002 fuan_close at active
 show nao_v002 fuan_close at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'No, not at all... how could I know her?!'
 hide nao_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show erika_v001 fuan at mei_center
 with Dissolve(0.5)
 show erika_v001 fuan at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") 'Hahh, what are you saying, you little midget? ...Aah, has your memory been wiped? Or is it that this is a different world, or a whole different persooon...?!'
 show erika_v001 normal_close at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") 'Well, you are without a doubt the exact same existence... \nSo it changes nothing for me.'
 hide erika_v001
 with Dissolve(0.2)
 show miyuki_v002 odoroki at mei_center
 with Dissolve(0.5)
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'T-The... same... what?'
 hide miyuki_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") "I didn't want to bother my master, so I went out of my way to use a separate route made through the help of another fine individual in order to meet you here."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show erika_v001 fuan at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") "So, this means you'll accept my revenge match... won't yooouuu?!"
 window hide None
 hide erika_v001
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show kazuho_v002 fuan at mei_left
 show erika_v001 fuan at mei_right
 with Dissolve(0.5)
 show erika_v001 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'W-... What is this person... on about...?!'
 show erika_v001 fuan at inactive
 show kazuho_v002 sinken_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(I can't let this person get to Nao-chan...! I don't know why, but it absolutely can't happen!)"
 show erika_v001 fuan at inactive
 show kazuho_v002 sinken at active
 show kazuho_v002 sinken at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "N-... No way...! We don't know you, so please leave."
 show kazuho_v002 sinken at inactive
 show erika_v001 sinken at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") "Huuh? ...You, what's your deal? Don't get in my way. Don't you know this doesn't involve you?"
 show erika_v001 sinken at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "That's not the point...! You look like you have bad intentions!"
 window hide None
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 show kazuho_v002 sinken at inactive
 show erika_v001 sinken at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") 'What an unreasonable person...\nWho cares about that? Do please get out of my way.'
 show erika_v001 sinken at inactive
 show kazuho_v002 sinken_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...Maybe if you were to leave.'
 window hide None
 hide erika_v001
 hide kazuho_v002
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'K-Kazuho...?'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 fuan at mei_center
 with Dissolve(0.5)
 show erika_v001 fuan at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") "...And if I don't, then what? Don't tell me you intend to fight me?"
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Keep saying disrespectful things, and I'll have to put you in your--"
 hide erika_v001
 with Dissolve(0.2)
 show rika_v023 normal at mei_center
 with Dissolve(0.5)
 show rika_v023 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep? What's going on?"
 stop music fadeout 1.0
 hide rika_v023
 with Dissolve(0.2)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 Character('Mysterious Woman',ctc="ctcArrow", ctc_position="fixed") 'What, really? Another one to get in my wa-... huh?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide fade onlayer curtain
 show rika_v023 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v023 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep?'
 call chapter_end
 jump chara072016_03