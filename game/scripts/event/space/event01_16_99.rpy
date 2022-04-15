label event01_16_99:
 show black_background onlayer black
 $ event_store.current_event='space'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_16_99'
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
 show expression 'images/bg/AdvBg_142.png' as bg
 play music "<loop 0>audio/bgm/BGM_BATTLE2_hiru.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show hanyuu_v009 sinken at mei_left
 with Dissolve(0.5)
 show hanyuu_v009 sinken at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Class-A Criminal K-1!\nPeacefully lay your weapons down and surrender now!'
 show keiichi_v007 sinken at mei_right
 with Dissolve(0.5)
 show hanyuu_v009 sinken at inactive
 show keiichi_v007 sinken at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "D-...dammit, I'm not getting caught now!\nOy, Lady Meep, do something about her, quickly!"
 hide hanyuu_v009
 show rika_v012 fuan at mei_left
 with Dissolve(0.5)
 show keiichi_v007 sinken at inactive
 show rika_v012 fuan at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep. I am very SORRY. Damage LEVELS exceeding functionable THRESHOLD; RECOVERY function REBOOT FAILED...'
 show keiichi_v007 sinken at inactive
 show rika_v012 fuan_close at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'OPERATING SYSTEM, SHUTTING DOWN...\nGOOD... NIGHT... *gachunk*.'
 hide rika_v012
 with Dissolve(0.2)
 show keiichi_v007 odoroki at active
 show keiichi_v007 sinken at jumping_transform
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "H-Hey, you're the android that's supposed to protect me!\nWake up, dammit!"
 show hanyuu_v009 sinken at mei_left
 with Dissolve(0.5)
 show keiichi_v007 odoroki at inactive
 show hanyuu_v009 sinken at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Now you're as good as naked...\nTime to face the consequences!"
 show hanyuu_v009 sinken at inactive
 show keiichi_v007 sinken at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Tch, looks like I have no choice...!'
 hide keiichi_v007
 hide hanyuu_v009
 with Dissolve(0.2)
 narrator "Realizing that he's backed into a corner... K-1 readies his gun and aims it at Hanyuu-chan."
 narrator 'His eyes glinted with malice...\nThat murderous intent reflected in his gaze caused fear to well up within me.'
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Hanyuu-chan... be careful!\nThat guy really plans on shooting you!'
 show hanyuu_v009 odoroki at mei_right
 with Dissolve(0.5)
 show kazuho_v002 sinken at inactive
 show hanyuu_v009 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...Huh? How do you know my name...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide hanyuu_v009
 hide fade onlayer curtain
 show keiichi_v007 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v007 sinken at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Oraah!'
 play audio 'audio/sfx/SE_112_hit_thunder.wav'
 camera at screenshake_transform
 pause 0.0
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "When Hanyuu-chan curiously turns her head towards me, K-1's gun roars to life, and a pale light shoots towards us."
 narrator '...However, she noticed it and effortlessly sliced it apart with a single strike of her sword, then quickly closed the distance between her and K-1, and aimed the tip of her sword at his throat.'
 show hanyuu_v009 sinken at mei_center
 show keiichi_v007 odoroki behind hanyuu_v009
 show keiichi_v007 odoroki:
  yanchor 1.0
  pos (1160, 1200)
 with Dissolve(0.5)
 show hanyuu_v009 sinken at inactive behind keiichi_v007
 show keiichi_v007 odoroki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Wh-wha...?!'
 show keiichi_v007 odoroki at inactive behind hanyuu_v009
 show hanyuu_v009 sinken at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "...Fired your gun, did you?\nI won't spare you any mercy either then!"
 play audio 'audio/sfx/SE_126_hit_strike3.wav'
 show hanyuu_v009 sinken at inactive behind keiichi_v007
 show keiichi_v007 fuan_close at active
 show keiichi_v007 odoroki at chara_shake_transform
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Gagh..?!'
 hide keiichi_v007
 hide hanyuu_v009
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_218_down.wav'
 narrator 'Struck in the stomach with the hilt of her sword, K-1 collapsed to the ground with a cry of anguish... and remained motionless.'
 stop music fadeout 0.5
 show hanyuu_v009 sinken_close at mei_center
 with Dissolve(0.5)
 show hanyuu_v009 sinken_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...I will not take your life.\nIn turn, please accept the verdict of the law and atone for your crimes.'
 hide hanyuu_v009
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 show hanyuu_v009 smile at mei_right
 show kazuho_v002 odoroki
 show kazuho_v002 odoroki:
  yanchor 1.0
  linear 0.5 pos (480,1200)
 with Dissolve(0.5)
 show kazuho_v002 odoroki:
  yanchor 1.0
  pos (480,1200)
 show kazuho_v002 odoroki at inactive
 show hanyuu_v009 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Are you okay?\nI'm glad I could rescue someone, even if it was just one person..."
 show hanyuu_v009 smile at inactive
 show kazuho_v002 smile at active
 show kazuho_v002 smile at nod_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Y-...yeah. Thank you, Hanyuu-chan. You saved me by a hair's breadth."
 show hanyuu_v009 smile at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah... but I'm also sorry.\nYou aren't the same Hanyuu-chan that I'm familiar with... are you?"
 show kazuho_v002 fuan at inactive
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...I will clarify some of those details for you very soon.\nThat said...'
 show kazuho_v002 fuan at inactive
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "We only know about you through the data from this recent investigation. ...I believe this is the first time we've met face to face."
 show hanyuu_v009 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 show kazuho_v002 fuan at inactive
 show hanyuu_v009 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'In the meantime, do you mind informing me of what happened?\nI have some knowledge of your circumstances, but I would like to hear about it directly from you, if at all possible...'
 show hanyuu_v009 smile at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Um, b-before that... uh...!'
 hide kazuho_v002
 hide hanyuu_v009
 with Dissolve(0.2)
 narrator 'There was only one thing I wanted to ask. With that in mind, I felt encouraged enough to turn towards Hanyuu-chan.'
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'About what K-1 and Lady Meep told me... \nWas our world really destroyed by a virus a thousand years ago?'
 show hanyuu_v009 odoroki at mei_right
 with Dissolve(0.5)
 show kazuho_v002 sinken at inactive
 show hanyuu_v009 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide hanyuu_v009
 hide fade onlayer curtain
 show hanyuu_v009 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 play music "<loop 1.5>audio/bgm/BGM_EVENT4.ogg"
 show hanyuu_v009 normal_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'It was.\nAlso, since this space is just a temporary construct... it will disappear in ten hours without a trace.'
 hide hanyuu_v009
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...nnh...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'She delivers that message in an indifferent tone, as if stepping all over my emotions... I was so heartbroken from it that my shoulders sink.'
 narrator "...Honestly, I wanted to deny it.\nI wanted her to reassure me that everything K-1's group said was a lie."
 narrator 'But... that was the truth.\nI had no choice but to accept my current situation...'
 show hanyuu_v009 fuan at mei_center
 with Dissolve(0.5)
 show hanyuu_v009 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...Allow me to conduct an inquiry.\nSo... as for the "medical treatment" for those people...'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide hanyuu_v009
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show hanyuu_v009 normal at mei_right
 with Dissolve(0.5)
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "...I see. In other words, you're a rare human carrying antibodies to the killer virus raging across the galaxy."
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v009 normal at inactive
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at nod_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...Yeah. I think that's what K-1 said..."
 show kazuho_v002 fuan at inactive
 show hanyuu_v009 normal_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Interesting... I don't have any medical tech, so I'll have to do a detailed analysis when we return to my home planet... "
 show kazuho_v002 fuan at inactive
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...Kazuho Kimiyoshi-san, this is just my personal opinion, but please listen...'
 show kazuho_v002 fuan at inactive
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Assuming that this is all true... your DNA may become a great weapon in eradicating the virus plaguing the Great Galactic Cluster.'
 show kazuho_v002 fuan at inactive
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "However, I don't have the authority to force you to do it... so I will ask.\nPlease, we implore you to cooperate with us."
 show hanyuu_v009 normal at inactive
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...You don't really need my permission. Just... do as you like."
 hide hanyuu_v009
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'I spit that out, feeling half-desperate.'
 narrator "I'm a walking corpse who died long ago.\nAnd everyone else is already... gone..."
 narrator 'There is nothing for me to protect anymore...\nI had no hopes... no will to live... nothing...'
 show kazuho_v002 sinken_close at mei_left
 with Dissolve(0.5)
 show kazuho_v002 sinken_close at active
 show kazuho_v002 sinken_close at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Whatever it is, just... kill me...!\nI don't want to know anything else, I don't want to feel anything else... so just...!"
 show hanyuu_v009 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 sinken_close at inactive
 show hanyuu_v009 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...I sincerely apologize that you were woken up from your precious slumber for our own one-sided desires...'
 show kazuho_v002 sinken_close at inactive
 show hanyuu_v009 fuan_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'You witnessed such a gruesome sight unfold before your eyes...\nI believe this day was far too horrible for you. There is nothing that can be done to atone for this tragedy, let alone heal you from it.'
 show hanyuu_v009 fuan_close at inactive
 show kazuho_v002 sinken_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...nnh...'
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide hanyuu_v009
 hide fade onlayer curtain
 show hanyuu_v009 normal at mei_center
 with Dissolve(0.08333333333333333)
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Now... Kazuho Kimiyoshi-san.\nWhich would you rather dream about?'
 hide hanyuu_v009
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Dream... about...?'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 camera:
  pos (960, 540)
  zoom 1.0
 play music "<loop 6.86>audio/bgm/BGM_OYASHIRO.ogg"
 stop sound
 show expression 'images/bg/AdvBg_220.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'The scenery around us suddenly changes.\nThis space around us is different from Hinamizawa, and even different from outer space.'
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Th-...this is...?'
 show hanyuu_v009 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show hanyuu_v009 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Please be at ease. Using the power vested in me, I have broken the {b}Karmic Law{/b} binding you to the "World" you were just in.'
 show kazuho_v002 odoroki at inactive
 show hanyuu_v009 normal_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'My being a Star Cluster Investigator was just a temporary form...\nIn actuality, I am an {b}Overseer{/b}, with the mission of repairing irregularities and contradictions in parallel worlds...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide hanyuu_v009
 hide fade onlayer curtain
 show hanyuu_v009 normal at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_022_WaveStart.wav'
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Indeed... I am an existence that you humans might refer to as a {b}god{/b}.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide hanyuu_v009
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 show hanyuu_v009 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'The deeds of those criminals aside... there are people suffering from disease all throughout the galaxy. Tens or hundreds of billions of them.'
 show kazuho_v002 odoroki at inactive
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Thus, if you supply us with your genetic information, we may be able to save these many lives from death. ...However, it requires your sacrifice.'
 show kazuho_v002 odoroki at inactive
 show hanyuu_v009 normal_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Nonetheless, forcing you into doing such a thing would be cruel. \nSo... I would like for you to make a decision.'
 show kazuho_v002 odoroki at inactive
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Will you choose for this world to be merely a "Dream"?\nOr will you accept reality and become a saviour...?'
 show kazuho_v002 odoroki at inactive
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Whichever one you choose, we will accept it. It is up to your will.'
 show hanyuu_v009 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 hide kazuho_v002
 hide hanyuu_v009
 with Dissolve(0.2)
 narrator "...These options are too extreme, so I can't bring myself to answer right away."
 narrator 'What I want is obvious.\n...But others would see it as incredibly egotistical and selfish.'
 narrator "Even so... no matter what anyone says... I'll..."
 show hanyuu_v009 normal at mei_center
 with Dissolve(0.5)
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...Kazuho Kimiyoshi. Will you tell me your choice?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide hanyuu_v009
 hide fade onlayer curtain
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............I...will...'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 camera:
  pos (960, 540)
  zoom 1.0
 pause 2.0
 stop sound
 show expression 'images/bg/AdvBg_81.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show miyuki_v001 odoroki at mei_center
 with Dissolve(0.5)
 show miyuki_v001 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...ey, Kazuho! Kazuhooooo!'
 show kazuho_v001 odoroki at mei_left
 show miyuki_v001 odoroki
 show miyuki_v001 odoroki:
  yanchor 1.0
  linear 0.5 pos (1440,1200)
 with Dissolve(0.5)
 show miyuki_v001 odoroki:
  yanchor 1.0
  pos (1440,1200)
 show miyuki_v001 odoroki at inactive
 show kazuho_v001 odoroki at active
 show kazuho_v001 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '—Huh?! Wh-what? Wh-where am I?'
 hide miyuki_v001
 show nao_v001 sinken at mei_right
 with Dissolve(0.5)
 show kazuho_v001 odoroki at inactive
 show nao_v001 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Jeez, are you still half-asleep? Just look around you.'
 hide kazuho_v001
 hide nao_v001
 with Dissolve(0.2)
 narrator "At Nao's insistence, I check my surroundings."
 narrator '...This was without a doubt the classroom at the branch school.\nAnd right next to me, Rena-san and the others were looking at me in wonder.'
 show kazuho_v001 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Th-then... what I was experiencing just now was...'
 show mion_v001 odoroki at mei_right
 with Dissolve(0.5)
 show kazuho_v001 odoroki at inactive
 show mion_v001 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Uh, experiencing...?\nYou've been here the whole time. You're seriously still half-asleep, huh?"
 show mion_v001 odoroki at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'I... I was here the whole time?'
 show kazuho_v001 odoroki at inactive
 show mion_v001 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Honestly... you can't doze off while we're in the middle of an important discussion. We're trying to decide the cast for this play—"
 show mion_v001 fuan at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I-I'm sorry! ...Wait, a play? Wh-what do you mean...?"
 hide mion_v001
 show keiichi_v001 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v001 odoroki at inactive
 show keiichi_v001 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Oy, oy, Kazuho-chan. Did you forget how fired up everyone was to make a play like that show with the superhero we saw earlier?'
 hide keiichi_v001
 show shion_v001 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v001 odoroki at inactive
 show shion_v001 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I heard that's why Kei-chan and I were called here... but am I wrong?"
 show shion_v001 fuan at inactive
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Play...? A stage play...?'
 hide shion_v001
 show rena_v001 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v001 odoroki at inactive
 show rena_v001 smile at active
 show rena_v001 smile at nod_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Yes, that's right. Here, look."
 hide kazuho_v001
 hide rena_v001
 with Dissolve(0.2)
 narrator 'Seeing my confusion and bewilderment, Rena-san handed me a copy of a script. I check the content by skimming through the pages.'
 play audio 'audio/sfx/SE_005_WindowPopup.wav'
 show kazuho_v001 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v001 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(Wh-...what is this..?!)'
 hide kazuho_v001
 with Dissolve(0.2)
 narrator 'I become even more confused as I look through.\nIs this plot exactly like what I went through just now......?'
 show keiichi_v001 sinken at mei_right
 with Dissolve(0.5)
 show keiichi_v001 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "I gotta say, this villain character sucks.\nIf this guy were real, I'd beat his ass right then and there."
 show shion_v001 sinken at mei_left
 with Dissolve(0.5)
 show keiichi_v001 sinken at inactive
 show shion_v001 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'I know, right? This story was pulled from a collection of sci-fi theater scripts, but when I read it I got pretty pissed.'
 hide shion_v001
 show mion_v001 futeki at mei_left
 with Dissolve(0.5)
 show keiichi_v001 sinken at inactive
 show mion_v001 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Well, if this guy were Kei-chan, he definitely couldn't be that cold-hearted. He'd be all clumsy and get taken advantage of at the very most... *cackle*cackle*!"
 show mion_v001 futeki at inactive
 show keiichi_v001 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "The hell are you saying? ...Heheh, if it's gonna be that way, I'll show you I'm an ultra-cool character, even if it's just for a play!"
 hide mion_v001
 show miyuki_v001 smile at mei_left
 with Dissolve(0.5)
 show keiichi_v001 smile at inactive
 show miyuki_v001 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yeah, yeaaah, we're looking forward to it~.\nWelp, guys, let's pull ourselves together and do some script reading!"
 hide keiichi_v001
 show rika_v001 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v001 smile at inactive
 show rika_v001 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. It's a beautiful day; I think we should read together outside."
 hide miyuki_v001
 show satoko_v001 smile at mei_left
 with Dissolve(0.5)
 show rika_v001 smile at inactive
 show satoko_v001 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'That sounds like a splendid idea!\nWhat does everyone else think?'
 hide rika_v001
 show shion_v001 smile at mei_right
 with Dissolve(0.5)
 show satoko_v001 smile at inactive
 show shion_v001 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '*giggle*... that sounds fun.\nShall we go then?'
 hide satoko_v001
 show keiichi_v001 smile at mei_left
 with Dissolve(0.5)
 show shion_v001 smile at inactive
 show keiichi_v001 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yeah! While we're at it, why don't we practice swordfighting together? There should be wooden swords in the storehouse behind the school!"
 hide shion_v001
 hide keiichi_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_537_move_desk.wav'
 narrator 'Everyone voices words of approval and heads into the hallway, scripts in hand.'
 narrator 'As I stare at them absentmindedly, I feel a light poke at my back. \n...When I turned my head, Nao-chan was standing there.'
 show nao_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Come on, Kazuho, what are you hesitating for?\nWe don't want to keep everyone waiting, so let's get going."
 show kazuho_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show kazuho_v001 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah... s-sorry.\nI'll start getting ready right away...!"
 hide nao_v001
 hide kazuho_v001
 with Dissolve(0.2)
 narrator 'I answered her with that and chased after everyone, quickly running through the classroom door...'
 narrator '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show hanyuu_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show hanyuu_v001 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "So, what was Kazuho's choice in the end...?\nI'll leave that up to your imagination. Au au."
 $ persistent.space_done = True
 call chapter_end
 return