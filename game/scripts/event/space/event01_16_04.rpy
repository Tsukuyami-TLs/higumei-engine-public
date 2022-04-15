label event01_16_04:
 show black_background onlayer black
 $ event_store.current_event='space'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_16_04'
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
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'K-1 gradually closes the distance between us while ostentatiously holding his gun up in the air.'
 narrator "Did he help me by shooting Rena-san...?\nBut if that's the case, I don't understand at all why he thought it was necessary to intimidate me."
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'M-...Maebara-kun, was it... you who saved me...?'
 show keiichi_v007 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") '............'
 show keiichi_v007 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I... I didn't do anything, okay?\nEveryone started acting weird and turned violent... with each other... uh!"
 show keiichi_v007 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "So... so I didn't do anything! Please... believe me, Maebara-kun!"
 show kazuho_v002 fuan at inactive
 show keiichi_v007 sinken at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "You know... I told you this before, but my name is K-1. And while it's true I did help you... I came here for a different reason."
 show keiichi_v007 sinken at inactive
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah? Wh-what do you mean...?!'
 hide keiichi_v007
 show rika_v012 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep, confirmed. The only one alive in this location is this {b}Kazuho Kimiyoshi{/b}.'
 hide rika_v012
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show keiichi_v007 futeki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Wow, so you {i}are{/i} a "Carrier" of the virus\' antibodies.\nHeheh, I didn\'t think it\'d turn out as good as this...'
 show keiichi_v007 futeki at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Virus antibodies...?'
 hide kazuho_v002
 hide keiichi_v007
 with Dissolve(0.2)
 narrator "K-1 and Lady Meep's laughs and smirks make me shudder in fear."
 narrator 'Did they maybe... know... that this would happen all along...?!'
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Y-...you said it yourselves, didn't you?!\nThat you resurrected us and let us spend a day in Hinamizawa... just to collect... data..."
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Yup, pretty much. None of that stuff we talked about was a lie.'
 show kazuho_v002 fuan at inactive
 show keiichi_v007 futeki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'But... I left out all of the important points.'
 show keiichi_v007 futeki at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Im-...important points...?'
 play audio 'audio/sfx/SE_022_WaveStart.wav'
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 show kazuho_v002 fuan at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "The mysterious natural disaster that happened wasn't the spread of noxious gas. What really destroyed humanity was... a virus outbreak."
 show keiichi_v007 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-A virus...?!'
 show kazuho_v002 odoroki at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Yup. Those infected with the virus would have their sense of reason collapse in the blink of an eye... to the point they would awaken to violent impulses.'
 show kazuho_v002 odoroki at inactive
 show keiichi_v007 normal_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Until you squeeze the life out of every person besides yourself, those impulses won't go away. And at the very end, you yourself will become your own target..."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 show kazuho_v002 odoroki at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "...It's a peculiar virus. If something like that were to spread, it wouldn't be surprising if an entire planet died, right~?"
 hide keiichi_v007
 show rika_v012 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'You experienced it firsthand, so I believe you were given the chance to understand that aspect. Nipah~'
 show rika_v012 smile at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...gh...!'
 hide rika_v012
 show keiichi_v007 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Oh, and I haven't mentioned this to you guys... but right now, that same virus is re-emerging all throughout the galaxy. Only thing is, it's so old that almost nobody has the antibodies."
 show kazuho_v002 fuan at inactive
 show keiichi_v007 fuan_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Neither a vaccine nor a cure are being developed.\nThat's why we all live in fear every day."
 show kazuho_v002 fuan at inactive
 show keiichi_v007 futeki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "But so, I thought about it...\nIf I went to the place where the virus originated and collected antibody samples... get where I'm going with this?"
 show kazuho_v002 fuan at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'I figured out the location where the virus likely originated, collected DNA, brought it to my spaceship, and made clones...'
 show kazuho_v002 fuan at inactive
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "—That's what you guys are."
 show keiichi_v007 smile at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...And then you lied to us, sent us to Hinamizawa, and observed us...?'
 show kazuho_v002 sinken at inactive
 show keiichi_v007 smile at active
 show keiichi_v007 smile at nod_transform
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Yup. The virus outbreak happened much earlier than I thought, but it turned out alright in the end.'
 show kazuho_v002 sinken at inactive
 show keiichi_v007 smile_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Honestly, it was a miracle of God that we fortunately found an antibody carrier... no, really, I was so grateful I wanted to cry~!'
 show keiichi_v007 smile_close at inactive
 show kazuho_v002 sinken_close at active
 show kazuho_v002 sinken_close at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...O-Oh...'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 hide keiichi_v007
 with Dissolve(0.2)
 play music "<loop 1.5>audio/bgm/BGM_EVENT4.ogg"
 show black_cover as bg
 narrator 'Ah... I see now.\nI finally understand why I harbored such dislike towards these people.'
 narrator 'They didn\'t think of us as "humans" like themselves from the start.'
 narrator 'And instead of seeing us as extinct animals... they thought they could treat us like guinea pigs just to collect... virus antibody samples...'
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...gh...'
 narrator '...I was frustrated. Sad. And above all else, the fact that I was deceived by people whose faces I knew all too well... helplessly made me even more angry.'
 stop sound
 show expression 'images/bg/AdvBg_142.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kazuho_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(...But...)'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'If that\'s what it actually takes to rescue the troubled people in this "World"... then acceptance was my only option.'
 narrator 'I tried to suppress the dark thoughts swirling around in my chest through that mindframe, and took several deep breaths... then I finally raised my head.'
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 show kazuho_v002 sinken at deepbreath_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...I understand now. I'll cooperate if what you said is true.\nBut..."
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Why didn't you say so from the beginning?\nIf I knew this was to save everyone in this world... something like this wouldn't have...!"
 stop music fadeout 0.5
 show keiichi_v007 odoroki at mei_right
 with Dissolve(0.5)
 show kazuho_v002 sinken at inactive
 show keiichi_v007 odoroki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Wha? I\'m not trying to save everyone. This is limited to those who compensate us appropriately for the "cost" of their lives.'
 show keiichi_v007 odoroki at inactive
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Eh... wh-...why...? Weren\'t you going to use us to save this "World"?!'
 show kazuho_v002 odoroki at inactive
 show keiichi_v007 fuan at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Huh? Oy oy, what are you talking about? Do you know how much time and money we poured into resurrecting you guys?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide kazuho_v002
 hide keiichi_v007
 hide fade onlayer curtain
 show keiichi_v007 futeki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_022_WaveStart.wav'
 show keiichi_v007 futeki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "I'll cut you up and collect the antibodies alone... I'll create vaccines and cures in high quantities, and then I'll sell them all across the galaxy for a high price ― that's my plan."
 show keiichi_v007 futeki_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "And then, I'll be the richest man in the galaxy!\nIt's my one-way ticket to getting out of this low-paying Environment Protection Coalition job!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Th-then... you're telling me that you intend to sacrifice us all purely out of self-interest...?!"
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'So all that stuff you kept saying about the archaeology and the environmental protection... in the end, all of that is...!'
 show keiichi_v007 futeki at mei_right
 with Dissolve(0.5)
 show kazuho_v002 sinken at inactive
 show keiichi_v007 futeki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Heh... you really {i}are{/i} an idiot to believe all of that!'
 show kazuho_v002 sinken at inactive
 show keiichi_v007 futeki at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "I don't care what happens to anyone else!\nI'm gonna celebrate my life to the fullest! Hyaaaahhahahahahaha...!!"
 show keiichi_v007 futeki at inactive
 show kazuho_v002 sinken at active
 show keiichi_v007 futeki at updown_shake_transform
 show kazuho_v002 sinken at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...-ivable...!'
 hide kazuho_v002
 hide keiichi_v007
 with Dissolve(0.2)
 narrator 'Unforgivable, unforgivable, unforgivable...!'
 narrator 'Absolutely... UNFORGIVABLE!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play music "<loop 5.836>audio/bgm/BGM_EVENT5.ogg"
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "How... dare you trample on people's lives and everyone's feelings... how dare you!!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "I'm so overcome with all of the anger, frustration, and hatred rising up from the bottom of my heart...  that I leap towards K-1 in a fit of rage."
 narrator 'However... the fist that I raised up in front of him suddenly stops...'
 play audio 'audio/sfx/SE_218_down.wav'
 narrator 'And in the next moment, I get wrestled onto the ground by Lady Meep, who was standing right by him.'
 show keiichi_v007 smile at mei_right
 with Dissolve(0.5)
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "...Didn't I tell you?\nYou can't possibly go up against us."
 show rika_v012 smile at mei_left
 with Dissolve(0.5)
 show keiichi_v007 smile at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") "Nipah, please don't think poorly of me.\nMy master's orders are absolute."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide keiichi_v007
 hide rika_v012
 hide fade onlayer curtain
 show rika_v012 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v012 futeki at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") "...Well, it doesn't matter if I receive orders or not. I'm an android, so I wouldn't particularly be interested in your welfare if it were my say anyway!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v012
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 sinken_close at mei_center
 show rika_v012 futeki behind kazuho_v002
 show rika_v012 futeki:
  yanchor 1.0
  pos (1110, 1200)
 with Dissolve(0.5)
 show rika_v012 futeki at inactive behind kazuho_v002
 show kazuho_v002 sinken_close at active
 show kazuho_v002 sinken_close at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Gh...rrrrghhh...!'
 show kazuho_v002 sinken_close at inactive behind rika_v012
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Specimen name: Kazuho Kimiyoshi. You will become the savior of the Great Galactic Cluster and live on inside a cultivation pod, where your body will be connected to tubes.'
 show kazuho_v002 sinken_close at inactive
 show rika_v012 smile_close at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Or, well, to put it simply... I do wonder if this means you will forever lose your ability to die, so long as you are a seedbed for the creation of cures...?'
 show rika_v012 smile_close at inactive behind kazuho_v002
 show kazuho_v002 sinken at active
 show kazuho_v002 sinken at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Nn-...no, stop...!!'
 show kazuho_v002 sinken at inactive behind rika_v012
 show rika_v012 futeki at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") "I said it earlier, hadn't I? You have no right to complain. Do your best in becoming a tool to use for the sake of foolish humans. Kuhuhuhuhu... ahahahahahaha...!"
 hide rika_v012
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Lady Meep says that while holding me down and taking out a syringe, waving it in front of me.'
 narrator 'She pushes down on the plunger... and a tiny drop lifts out from the tip of the needle.'
 narrator 'Then, as I saw the pointed end coming towards my arm, I instinctively close my eyes in despair...'
 narrator 'But just then.'
 play music "<loop 0>audio/bgm/BGM_BATTLE1_hiru.ogg"
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Surrender, evildoers!'
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Huh...? That voice, it couldn't be―"
 hide kazuho_v002
 show keiichi_v007 sinken at mei_center
 with Dissolve(0.5)
 show keiichi_v007 sinken at active
 show keiichi_v007 sinken at jumping_transform
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Geh! Y-You're...!"
 hide keiichi_v007
 show hanyuu_v009 sinken at mei_center
 with Dissolve(0.5)
 show hanyuu_v009 sinken at inactive
 narrator 'Who appeared was someone in a miko uniform... an outfit just like what Hanyuu-chan would wear.'
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 show hanyuu_v009 sinken at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Haaaaaah!!'
 hide hanyuu_v009
 show rika_v012 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v012 odoroki at active
 show rika_v012 odoroki at jumping_transform
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") '...Wha-...?!'
 hide rika_v012
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 narrator 'Hanyuu-chan brandishes a sword swirling with a pale blue energy, and then slashes at us.'
 play audio 'audio/sfx/SE_405_swing_high.wav'
 narrator 'When Lady Meep noticed that, she immediately jumped backwards a long distance, separating herself from me.'
 show hanyuu_v009 sinken at mei_left
 with Dissolve(0.5)
 show hanyuu_v009 sinken at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "—You're mine!!"
 show hanyuu_v009 sinken at active
 show hanyuu_v009 sinken:
  yanchor 1.0
  linear 0.16666666666666666 pos (960,1200)
 pause 0.16666666666666666
 show hanyuu_v009 sinken:
  yanchor 1.0
  pos (960,1200)
 narrator "Without a moment's delay, Hanyuu-chan steps forward and delivers two, then three slashes; both vertical and horizontal beams of light mow Lady Meep's body down instantaneously."
 show rika_v012 fuan_close behind hanyuu_v009
 show rika_v012 fuan_close:
  yanchor 1.0
  pos (1110, 1200)
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_103_hit_slash.wav'
 show hanyuu_v009 sinken at inactive behind rika_v012
 show rika_v012 fuan_close at active
 show rika_v012 fuan_close at chara_shake_transform
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") '...G-Guh...?!'
 hide hanyuu_v009
 hide rika_v012
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_218_down.wav'
 narrator 'Lady Meep groans in a low voice after taking the full-blown attack. She fell to one knee while wearing an anguished expression.'
 show rika_v012 fuan_close at mei_right
 with Dissolve(0.5)
 show rika_v012 fuan_close at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'I have f-...failed.\nDamage LEVEL... CRITICAL...'
 show hanyuu_v009 sinken at mei_left
 with Dissolve(0.5)
 show rika_v012 fuan_close at inactive
 show hanyuu_v009 sinken at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Now, come to me before it's too late!"
 hide rika_v012
 hide hanyuu_v009
 with Dissolve(0.2)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'O-...Okay...!'
 hide kazuho_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator 'I attempted to regain my balance, awkwardly getting my feet tangled up as I sprinted to get behind Hanyuu-chan.'
 show keiichi_v007 sinken at mei_right
 with Dissolve(0.5)
 show keiichi_v007 sinken at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'Tch... I heard about you!\nTo think a Star Cluster Investigator would show up...!'
 show hanyuu_v009 sinken_close at mei_left
 with Dissolve(0.5)
 show keiichi_v007 sinken at inactive
 show hanyuu_v009 sinken_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'We have looked into all of your plans.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide keiichi_v007
 hide hanyuu_v009
 hide fade onlayer curtain
 show hanyuu_v009 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_358_ls_firestart.wav'
 show hanyuu_v009 sinken at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'For you to take advantage of a virus terrorizing the entire galaxy solely to line your own pockets... we will absolutely never allow this!!'
 call chapter_end
 jump event01_16_99