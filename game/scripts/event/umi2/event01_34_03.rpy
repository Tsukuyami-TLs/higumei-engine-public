label event01_34_03:
 show black_background onlayer black
 $ event_store.current_event='umi2'
 $ event_store.current_progress=1
 $ event_store.current_chapter='event01_34_03'
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
 show expression 'images/bg/AdvBg_2461.png' as bg
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Wait, Miyuki, Kazuho... wh-, huh?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Nao-chan, who had been trailing us, stopped when she saw the face of the person opposite us.'
 show miyuki_v002 normal at mei_center
 with Dissolve(0.5)
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '............'
 hide miyuki_v002
 with Dissolve(0.2)
 narrator "Miyuki-chan was so surprised, she couldn't even let out a sound... \nShe just stood there, dumbfounded."
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show akasaka_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yo, it's been a while. Are you doing well?"
 show akasaka_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Y-Yes... but why are you here, Akasaka-san...?'
 show nao_v002 normal at inactive
 show akasaka_v001 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'A-Ah, well...'
 hide nao_v002
 hide akasaka_v001
 with Dissolve(0.2)
 narrator 'Akasaka-san scratched his head in embarrassment when Nao-chan asked that question instead of Miyuki-chan.'
 narrator 'Then, with an awkward shrug, he smiled.'
 show akasaka_v001 smile at mei_center
 with Dissolve(0.5)
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "To tell the truth, Ooishi-san told me that there was a new hot spring in Hinamizawa, and I thought I'd go see what it was like."
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'I was in the area on official business, so I decided to drop by for a visit.'
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'I planned to take my family along the next time I visited, so I wanted to scout it out first.'
 hide akasaka_v001
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_left
 show akasaka_v001 smile at mei_right
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah, so it was like that...'
 show kazuho_v002 smile at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '...By the way, you two.\nYou were arguing or something a bit ago, so did something happen?'
 hide kazuho_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show akasaka_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, the truth is...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide akasaka_v001
 hide nao_v002
 hide fade onlayer curtain
 show keiichi_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") '...Huh, Akasaka-san?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "At the sound of Maebara-kun's voice, I turned around to see everybody giving off puzzled looks. It seems like they'd found us while we were talking."
 show akasaka_v001 smile at mei_right
 show battler_v001 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Yo, it's been a while. I don't recognize some of you kids... \nAre they new friends?"
 show akasaka_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ah, no, not me anyway...'
 hide battler_v001
 show rika_v002 fuan at mei_left
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep, Akasaka. To tell the truth, there's been some big trouble going on."
 show rika_v002 fuan at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Hm, some trouble...?'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide akasaka_v001
 hide rika_v002
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v002 fuan at mei_left
 show battler_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...That's what happened."
 show mion_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "To be honest, I don't want Jessica to be troubled by it... in various senses of the word."
 hide battler_v001
 hide mion_v002
 with Dissolve(0.2)
 show akasaka_v001 normal at mei_center
 with Dissolve(0.5)
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "I see... if I understand correctly, it's looking like we'll need to respond immediately."
 hide akasaka_v001
 with Dissolve(0.2)
 narrator 'After our explanation, Akasaka-san nodded in understanding while uncomfortably shifting his attention to Battler-san.'
 narrator 'Seeing that, a slightly lost expression rose to his face, and with a timid voice, he asked:'
 show battler_v001 normal at mei_left
 show akasaka_v001 normal at mei_right
 with Dissolve(0.5)
 show akasaka_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'd like to ask for reference... but from an adult's point of view, what do you make of this problem?"
 show battler_v001 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Mmm... if we purposefully conceal information that could lead to an accident, we'll most definitely risk a contract breach."
 show battler_v001 normal at inactive
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Also, if that was determined to have an impact on the customers, there would almost certainly be an indemnity claim.'
 hide battler_v001
 show mion_v002 fuan at mei_left
 with Dissolve(0.5)
 show akasaka_v001 normal at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "It's as I thought... Damn it."
 show mion_v002 fuan at inactive
 show akasaka_v001 normal_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") '............'
 hide akasaka_v001
 hide mion_v002
 with Dissolve(0.2)
 narrator 'As he fixed his gaze on Mion-san, who was clutching her head, Akasaka-san touched his mouth as if pondering something.'
 narrator 'Then, after a light nod, he turned to all of us.'
 show akasaka_v001 normal at mei_center
 with Dissolve(0.5)
 show akasaka_v001 normal at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Personally, there are various things about this that have my interest... but I need some time to figure out how to approach it. Even if we could thin them out temporarily, the issue wouldn't get resolved."
 show akasaka_v001 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "If you like, I can lend you all a hand. Working up a sweat before relaxing in the hot springs doesn't sound bad."
 hide akasaka_v001
 with Dissolve(0.2)
 show rena_v002 odoroki at mei_left
 show akasaka_v001 smile at mei_right
 with Dissolve(0.5)
 show akasaka_v001 smile at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Huh... i-is that really okay?'
 show rena_v002 odoroki at inactive
 show akasaka_v001 smile at active
 show akasaka_v001 smile at nod_transform
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Haha, of course. After all, it's my duty as a police officer to uphold public safety."
 hide rena_v002
 show miyuki_v002 smile_blush at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show akasaka_v001 smile at inactive
 show miyuki_v002 smile_blush at active
 show miyuki_v002 smile_blush at jump_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "For sure! \nI'll be here to support you, so please come this way!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide akasaka_v001
 hide miyuki_v002
 hide fade onlayer curtain
 show nao_v002 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '......-eh?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show miyuki_v002 smile_blush at mei_center
 with Dissolve(0.5)
 show miyuki_v002 smile_blush at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "A-Akasaka-san. Using your bare hands won't be effective against {b}Tsukuyami{/b}, so please use this {b}Role Card{/b}♪"
 hide miyuki_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5028_pull_card.wav'
 narrator 'After saying that, Miyuki-chan handed Akasaka-san a {b}Role Card{/b} with a cheerful expression on her face.'
 narrator "...Umm, what's up with that sudden change?\nShe was all down in the dumps a second ago, but now she's glowing as if that was all a lie...?"
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.5)
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Uh, Miyuki-chan, didn't you say earlier that you were going to leave because of a headache... mmph?!"
 hide keiichi_v002
 with Dissolve(0.2)
 narrator 'Miyuki-chan nimbly took a step to get behind Maebara-kun and quickly covered his mouth.'
 narrator "...The look on her face was exactly as if she was an assassin, slitting her target's throat from behind them. I unconciously felt a chill run down my spine..."
 show miyuki_v002 smile
 show miyuki_v002 smile:
  yanchor 1.0
  pos (860, 1200)
 show keiichi_v002 fuan
 show keiichi_v002 fuan:
  yanchor 1.0
  pos (1060, 1200)
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "The busy detective {i}will{/i} heal himself through fun and relaxation... and I will {i}not{/i} forgive anyone who tries to disturb him as he's taking this time away from that to help someone else."
 show keiichi_v002 fuan at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...So don't say anything unnecessary. OK?"
 show miyuki_v002 normal at inactive
 show keiichi_v002 fuan at active
 show keiichi_v002 fuan at jumping_transform
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Mmmph! Mmmph!'
 hide keiichi_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator 'With every few words, Maebara-kun would fearfully respond with a nod and a groan as if he were a convulsing, teary-eyed animal.'
 narrator '...She was so forceful with him, it looked like he was about to cry.\nI was incredibly relieved that I had stopped myself from saying that a split second before he did.'
 show miyuki_v002 smile at mei_left
 show keiichi_v002 fuan at mei_right
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "That's a good boy, Maebara-kun.\n...Ah, do you wanna eat the manjuu you bought earlier at the hot spring?"
 show miyuki_v002 smile at inactive
 show keiichi_v002 fuan_close at active
 show keiichi_v002 fuan_close at chara_shake_transform
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'O-Oooh... ooooohhh......'
 hide keiichi_v002
 hide miyuki_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(Is Maebara-kun... trembling all over...? He is...!)'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator '...Oh yeah. Miyuki-chan always gets like this whenever her father is involved.'
 narrator 'Everyone else sensing this... gave the impression they were absolutely not going to speak out of turn.'
 stop music fadeout 0.5
 show battler_v001 fuan at mei_right
 show satoko_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'H-Hey... you girls...?'
 show battler_v001 fuan at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'My, what is it?'
 play music "<loop 0>audio/bgm/BGM_QUEST2_COLLAB3.ogg"
 show satoko_v002 smile at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Tell me... is there something going on in this village? Or maybe I've just completely lost all traces of common sense?"
 hide satoko_v002
 hide battler_v001
 with Dissolve(0.2)
 show hanyuu_v002 fuan at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, your face is pale...'
 show hanyuu_v002 fuan at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep, are you okay?'
 hide rika_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show battler_v001 fuan_close at mei_center
 with Dissolve(0.5)
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Th-the truth is... up until a bit before, I thought I was absolutely right in the head.'
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I had the idea what happened earlier was all a dream, and I was actually just nodding off while on a train to Okinomiya...'
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I was hoping from the bottom of my heart that Jessica would wake me up in the midst of it... so she could bring me back to reality...!'
 camera:
  parallel:
   linear 0.5 pos (960, 550)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But now there's this detective from Tokyo?\nEven a policeman is confirming it now?"
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "There's no way a person like that would just accept the existence of something as out of this world as {b}Tsukuyami{/b}...?!"
 camera:
  parallel:
   linear 0.5 pos (960, 570)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Aaah, I just don't get it! Even if it is a dream, a bunch of things are consistent!"
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Is this place actually reality?! Am I going crazy?! Is it just me?!'
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'GWAAAAHHHHHHHHHHH!!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v002 normal at mei_center
 with Dissolve(0.5)
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Meep. He's literally cowering with his face in his hands."
 hide rika_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show battler_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Please rest assured.\nBattler-san, you're certainly not crazy."
 show nao_v002 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'H-... R-Really?'
 show battler_v001 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Yes. And besides, there's no need to consider every little thing as real."
 show battler_v001 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...For now, if your eyes can't handle it, why not think of them as something like a boar or a bear?"
 show nao_v002 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Like when you're on stage and picture everybody in the audience as pumpkins?"
 hide battler_v001
 hide nao_v002
 with Dissolve(0.2)
 show rika_v002 smile at mei_right
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. I think that's what Nao was saying."
 show rika_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Of all things he could have used as an example, though, pumpkins are comparitively the worst...'
 show rika_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I\'ve heard of the phrase "When in Rome, do as the Romans do.". Why not tell yourself that this situation is only temporary to help you come to terms with it all?'
 hide rika_v002
 show battler_v001 normal_close at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Temporary......'
 hide satoko_v002
 show hanyuu_v002 normal at mei_left
 with Dissolve(0.5)
 show battler_v001 normal_close at inactive
 show hanyuu_v002 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au... it can be hard to accept new things when they're outside the limits of what you understand."
 show battler_v001 normal_close at inactive
 show hanyuu_v002 normal_close at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "But trying to reject them can also be painful. \nEven if you can't understand these things yourself... I think telling yourself that they exist tackles that issue well alone."
 show battler_v001 normal_close at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Perhaps someday, a single small occasion will help you understand.'
 stop music fadeout 0.5
 show hanyuu_v002 smile at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "O-Okay... That's pretty true..."
 hide battler_v001
 hide hanyuu_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5029_slap_back.wav'
 narrator 'One by one, Battler-san checked the faces of the girls surrounding him, and then let out a heavy sigh. Then, he slapped his cheeks.'
 show battler_v001 normal at mei_center
 with Dissolve(0.5)
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Aah~... It's kinda pathetic being lectured by kids the same age as Maria. \nLetting stuff like that get to my head isn't like me."
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Alright... time to screw my head on straight!'
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I still don't get the situation at all.\nIf I look into it enough, maybe I'll be able to spin the chessboard around!"
 hide battler_v001
 with Dissolve(0.2)
 show rika_v002 smile at mei_left
 show battler_v001 smile at mei_right
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. That's the spirit, nipah~."
 show rika_v002 smile at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Now that that's settled, let me go with you. Am I able to use these {b}Role Card{/b} things too? I'd like to help if possible."
 show battler_v001 normal at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I think that you would probably be fine using them.'
 hide rika_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, let me give you a spare card.'
 hide battler_v001
 hide hanyuu_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator 'With that, Battler-san took a card from Hanyuu-chan... and issued a loud declaration.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show battler_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 sinken at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm gonna find the solution during this inspection!\nFor Jessica's... For Jessica and a sense of familial peace!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "I'm interested in Miyuki-chan's feeling that this person might unknowingly bring trouble wherever he goes. I have my doubts about it, though..."
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(He's undeniably a good person...\nAnyways, let's do our best to return home safely...!)"
 hide kazuho_v002
 with Dissolve(0.2)
 show keiichi_v002 smile at mei_left
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Yeah! We got another reliable friend!'
 show keiichi_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Still, he saw the {b}Tsukuyami{/b} and was as flustered as can be at first... so calling him flexible wouldn't cut it. He's more plucky than anything."
 hide keiichi_v002
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. He's a friend with a plenty {i}eccentric{/i} personality."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide satoko_v002
 hide rika_v002
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show ange_v001 fuan at mei_center
 with Dissolve(0.5)
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '*sigh*... Onii-chan, why are you accepting this...?'
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'None of the forgeries had anything about these monsters or {b}Role Cards{/b}, did they?'
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Or is there something? \nCould I even find something that would give a reason for needing to accept it...?'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide ange_v001
 with Dissolve(0.2)
 pause 1.0
 stop sound
 show expression 'images/bg/AdvBg_2501.png' as bg
 stop music fadeout 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator '--Meanwhile, at the hot spring resort.'
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Ah, what a nice place! Both the hot spring and its facilities were great, but getting here sure was a problem, huh?'
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well, they said they'd have a shuttle bus from the nearest station once it opened up for business... so Mom doesn't really need to worry!"
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Even so, where did Battler run off to? He wasn't in his room, so maybe he went in one of the springs too?"
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'That Battler...\nWill he remember the promise we made for tonight...?'
 call chapter_end
 jump event01_34_04