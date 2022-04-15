label chara072016_01:
 show black_background onlayer black
 $ event_store.current_event='chara072016'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara072016_01'
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
 show expression 'images/bg/AdvBg_141.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v002 normal at mei_center
 with Dissolve(0.5)
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "You'll be reopening some of the hot spring facilities?"
 hide rika_v002
 with Dissolve(0.2)
 show mion_v002 normal at mei_right
 show rika_v002 normal at mei_left
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Open up for the first time is more accurate. The hot spring district was pretty much completely wiped out just as we finished building it, y'know?"
 show rika_v002 normal at inactive
 show mion_v002 normal_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'So thanks to that, we urgently need to continue with the cleanup work... since the cleanup workers will need a place to stay and eat at and stuff.'
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 normal_close at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Was opening the hot spring inn... safe?'
 hide mion_v002
 with Dissolve(0.2)
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 normal at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Mmm... I wonder if "safe" is the right word here?'
 hide kazuho_v002
 with Dissolve(0.2)
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au, at least it sort of maintained its form... kind of?'
 hide miyuki_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show jessica_v001 normal at mei_center
 with Dissolve(0.5)
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well, our clothes and stuff ended up fine more or less, so there are some parts that were safe. ...Our valuables we left at the front didn't make it, though."
 hide jessica_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_right
 show battler_v001 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'It seems the fire took an awful turn...'
 show nao_v002 fuan at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Even so, for the hot spring inn to turn into a pile of rubble overnight... I get the meaning behind "all things must pass" now.'
 hide nao_v002
 with Dissolve(0.2)
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'My, what knowledgeable words just left your mouth.'
 show satoko_v002 smile at inactive
 show battler_v001 smile at active
 show battler_v001 smile at updown_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Ihihi. You'd be amazed at how many expressions you can find in books... So then, what happened in that consultation?"
 hide satoko_v002
 with Dissolve(0.2)
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Just like I said before, they're contractors, but they're also not from here. We'd be in a rut if we didn't assign housing and other resources to them. It's just..."
 hide battler_v001
 with Dissolve(0.2)
 show rika_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Meep? What is it, Mii?'
 show rika_v002 normal at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "We recruited people for part time with that in mind, but the timing of this was so awful, so not a lot of people applied, and, well, y'know, uh..."
 hide rika_v002
 with Dissolve(0.2)
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... are you maybe suggesting that we start working part time for this hot spring inn, spring inn?'
 show rena_v002 fuan at inactive
 show mion_v002 normal at active
 show mion_v002 normal at nod_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Pretty much. This time it got real bad, so if possible, it would be great if everyone jumped in on this for me.'
 hide rena_v002
 with Dissolve(0.2)
 show keiichi_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "But if we do that, Battler and Jessica will lose out on their opportunity to get shown around Hinamizawa, won't they?"
 hide mion_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_right
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'm sorry... the removal company had plans to come a little bit after actually, but they ended up skipping their destination before ours to come right away."
 hide keiichi_v002
 hide shion_v002
 with Dissolve(0.2)
 show battler_v001 normal at mei_left
 show jessica_v001 normal at mei_right
 with Dissolve(0.5)
 show jessica_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...What the, so that's what it was? I thought something was up since you had that serious look on your face."
 show battler_v001 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "We wanted you to show us around the village at first, but it was just a random thing we asked, y'know? It's really no big deal!"
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show rika_v002 smile at mei_center
 with Dissolve(0.5)
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Thank you, Battler and Jessica.'
 hide rika_v002
 with Dissolve(0.2)
 show battler_v001 smile at mei_center
 with Dissolve(0.5)
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yeah, it's fine, no worries!\n...But what's this part time job at the inn looking like?"
 hide battler_v001
 with Dissolve(0.2)
 show mion_v002 normal at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Cleaning, preparing food... and I think some other stuff would be like switching out futons.'
 show mion_v002 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's more like a dorm manager than a part time worker at an inn."
 hide mion_v002
 with Dissolve(0.3)
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yeah, definitely. I think that's closer."
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show battler_v001 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well isn't that right... Jessica?"
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hehe, you had the same thought too, Battler? Guess you really are my cousin, huh?'
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show rika_v002 normal at mei_center
 with Dissolve(0.5)
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep...?'
 hide rika_v002
 with Dissolve(0.2)
 show battler_v001 normal at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hey, Mion-chan. Mind if we helped with that work too?'
 show battler_v001 normal at inactive
 show mion_v002 odoroki at active
 show mion_v002 odoroki at jump_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Huuh?! W-Well, that would save my skin, but... are you sure?'
 hide mion_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yeah! I've been wanting to try part time out at least once!"
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm not super used to it, but leave it to me! Physical labor is what hands are for anyways!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide battler_v001
 hide jessica_v001
 hide fade onlayer curtain
 show mion_v002 fuan_blush at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 fuan_blush at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Uuu... thank you! Reaaally, thank you sooooo much!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show miyuki_v002 odoroki at mei_left
 show rena_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rena_v002 odoroki at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Woah, Mion's getting teary-eyed..."
 show miyuki_v002 odoroki at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... Mii-chan's really in a tight spot, huh?"
 hide miyuki_v002
 with Dissolve(0.3)
 show kazuho_v002 normal at mei_left
 with Dissolve(0.5)
 show rena_v002 odoroki at inactive
 show kazuho_v002 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I-I'll do my best! I don't know what my limits are, though..."
 hide rena_v002
 with Dissolve(0.3)
 show hanyuu_v002 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 normal at inactive
 show hanyuu_v002 smile at active
 show hanyuu_v002 smile at jump_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au! If we put our hands together, I'm sure it'll be fine!"
 hide kazuho_v002
 with Dissolve(0.3)
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Fight oooon!'
 hide hanyuu_v002
 with Dissolve(0.3)
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 show battler_v001 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Battler...? Is there something on my face?'
 show rika_v002 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ah, no. Just feel like I heard that line somewhere before.'
 hide rika_v002
 show satoko_v002 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "My, really? I don't think it's all that rare of a phrase, though."
 show satoko_v002 normal at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "No, not that... well, guess it's all in my head."
 show battler_v001 normal_close at inactive
 show satoko_v002 smile at active
 show satoko_v002 smile at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rikaa, you and I will do our best too!'
 hide battler_v001
 hide satoko_v002
 with Dissolve(0.2)
 show rika_v002 smile at mei_center
 with Dissolve(0.5)
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Okaaayy, nipah!'
 hide rika_v002
 with Dissolve(0.2)
 stop music fadeout 1.0
 narrator '............'
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 show rika_v002 normal at mei_center
 with Dissolve(0.5)
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(Has this man... met another me?)'
 show rika_v002 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(No, this has to be the first Fragment where this man came here...)'
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(And it doesn't look like I've forgotten about anything either.)"
 show rika_v002 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(...He doesn't seem like an enemy or anything, so I'll have to wait and see for now.)"
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 hide rika_v002
 with Dissolve(0.2)
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(...I haven't gotten the chance to get a close look at him until this part time started.)"
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2471.png' as bg
 play music "<loop 0>audio/bgm/BGM_BATTLE1_hiru.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I-I heard them say that we don't have enough hands on the job...!"
 window hide None
 call wipeout_routine
 hide rika_v002
 with Dissolve(0.2)
 call wipein_routine
 show shion_v002 normal at mei_center
 with Dissolve(0.5)
 show shion_v002 normal at active
 show shion_v002 normal at updown_shake_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Bed lady, bringing in the sheeets!'
 window hide None
 call wipeout_routine
 hide shion_v002
 with Dissolve(0.2)
 call wipein_routine
 show mion_v002 normal at mei_center
 with Dissolve(0.5)
 show mion_v002 normal at active
 show mion_v002 normal at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Cook, about to start making dinner! Who's gonna bring it to the disaster site?"
 hide mion_v002
 with Dissolve(0.2)
 show satoko_v002 odoroki at mei_right
 show mion_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Huh...? Didn't I just clean the lunch silverware a bit ago?!"
 show satoko_v002 odoroki at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "This ol' cooking grandma says the food won't make it in time unless she starts cooking right now!"
 hide mion_v002
 hide satoko_v002
 with Dissolve(0.2)
 show miyuki_v002 fuan at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'I totally get why housewives lose their head over making side dishes... just thinking about making three meals a day is way too much.'
 show miyuki_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "In their case, they can push through making bread if they're lost for a second... but you are aware we don't have that option at this inn, correct?"
 show nao_v002 fuan at inactive
 show miyuki_v002 odoroki at active
 show miyuki_v002 odoroki at jump_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'I-I know...!'
 hide nao_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "*sigh*... But it's phenomenal that this much rice is getting eaten here!"
 hide kazuho_v002
 show rika_v002 normal at mei_center
 with Dissolve(0.5)
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Kazuho could work forever as long as there's rice. But..."
 window hide None
 call wipeout_routine
 hide rika_v002
 with Dissolve(0.2)
 call wipein_routine
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
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hiiih, hiiiih... t-... tired...'
 hide battler_v001
 with Dissolve(0.2)
 show keiichi_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show keiichi_v002 fuan_close at active
 show keiichi_v002 fuan_close at chara_shake_transform
 show keiichi_v002 fuan_close:
  yanchor 1.0
  linear 0.5 pos (960,1300)
 pause 0.5
 show keiichi_v002 fuan_close:
  yanchor 1.0
  pos (960,1300)
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "I... I can't move... anymore..."
 hide keiichi_v002
 with Dissolve(0.2)
 show rena_v002 fuan at mei_center
 with Dissolve(0.5)
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... a-are you okay, Battler-san and Keiichi-Kun?'
 hide rena_v002
 with Dissolve(0.2)
 show mion_v002 sinken at mei_center
 with Dissolve(0.5)
 show mion_v002 sinken at active
 show mion_v002 sinken at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "We got no time to laze around, manslaves! There's still a boatload of physical labor out there to do!"
 hide mion_v002
 with Dissolve(0.2)
 show keiichi_v002 odoroki at mei_right
 show battler_v001 fuan at mei_left
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'H-How can there be...?'
 show keiichi_v002 odoroki at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm about to say hi to my mother in heaven..."
 hide battler_v001
 hide keiichi_v002
 with Dissolve(0.2)
 window hide None
 play audio 'audio/sfx/SE_304_ls_run.wav'
 pause 0.6666666666666666
 show hanyuu_v002 fuan at mei_outerleft
 with Dissolve(0.5)
 show hanyuu_v002 fuan at active
 show hanyuu_v002 fuan:
  yanchor 1.0
  linear 0.5 pos (960,1200)
 pause 0.5
 show hanyuu_v002 fuan:
  yanchor 1.0
  pos (960,1200)
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'S-Something bad, something bad! Something bad happened!'
 hide hanyuu_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "What's wrong, Hanyuu-chan? Weren't you carrying out the food just now...?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide fade onlayer curtain
 show hanyuu_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show hanyuu_v002 sinken at active
 show hanyuu_v002 sinken at jump_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '{b}Tsukuyami{/b} are coming out again!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide hanyuu_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 Character('Everyone',ctc="ctcArrow", ctc_position="fixed") 'What?!'
 call chapter_end
 jump chara072016_02