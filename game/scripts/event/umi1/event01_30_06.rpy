label event01_30_06:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=4
 $ event_store.current_chapter='event01_30_06'
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
 show expression 'images/bg/AdvBg_2341.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Even if try to frame Shannon-san, it's over for you. Erika-san, you're the culprit of that prank."
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "That feels good, doesn't it?"
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Excuse me?'
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '"You\'re the culprit.". ...The moment you get to speak those words is the ultimate pleasure for a detective!'
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Of course, the culprit won't give in to that phrase so easily."
 show nao_v002 fuan at inactive
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "As a cornered rat will bite a cat, the culprit will also surely object with all their might. But for me, I'll {i}enjoy{/i} tearing it down once more!"
 show erika_v001 futeki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...So, essentially, you'll play the part of an exemplary culprit. Is that what you're saying?"
 show nao_v002 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Can you obtain the ultimate pleasure as a detective...?'
 show nao_v002 normal at inactive
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Or, just before the solution is unveiled, will you assume the role of Inspector So-and-so with your incompetent reasoning? *cackle*cackle*cackle*!'
 show erika_v001 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Then, Erika-san, let's hear your objection. Why do you say you aren't the culprit?"
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It's an exceedingly simple reason. Because I have an alibi."
 show erika_v001 normal at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Alibi...?'
 show nao_v002 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Oh, did you forget? Along with you and the others, didn't I sample Gohda-san's superb rendition on Spanish cuisine?"
 show nao_v002 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Then, immediately after finishing the meal, I participated in Jessica-san's board game."
 show nao_v002 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'After we played late into the night, I surely went upstairs with everyone else.'
 show nao_v002 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "In that time, was there even the briefest moment when I disappeared from everyone's sight?"
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...........................'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "Certainly, it's a rock-solid alibi. Since she was nowhere other than with me..."
 show nao_v002 normal_close at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'No... you did have a chance to commit a crime.'
 show nao_v002 normal_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Oh? At which time would that be?'
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "At the very beginning. You were late coming to dinner, saying your hair wasn't ready."
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Also, you knew our room's window was broken and couldn't be locked."
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'The magic circle on the sheets took time to prepare, but there was plenty of time to prepare it in advance.'
 narrator 'After confirming that we went downstairs to dinner ahead of her, she left through the window, walked on top of the first floor overhang, and entered through the window of our room!'
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '<Good>. Not bad at all.'
 show nao_v002 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'However... not great either.'
 show erika_v001 normal_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'You have an objection?'
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 show erika_v001 normal at nod_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "But of course. If I did that magic circle prank the way you've said, then it would have happened during the early stage of dinner."
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'In other words... Shannon-san would be entering the room shortly afterward.'
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "If she found your bed in that wonderfully {i}sublime{/i} state, do you really think she'd return uneventfully?"
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '.................................'
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Do you not remember when I jokingly asked Shannon-san, "Has a robber broken into the window or anything?", when she came back?'
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I guess... you did say that...'
 show nao_v002 fuan at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'And then, she said word for word, "No. Please be at ease.".'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Since Mion-san and Shion-san have super tough minds, they viewed the prank as a trivial matter.'
 narrator 'But... if they were guests with normal taste, we would all have screamed, running away from the room in fear of the prank.'
 narrator 'Seeing that, could someone really say, "No. Please be at ease."?'
 show nao_v002 fuan at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Th-, surely that's... when you think of it, you and Shannon-san are..."
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '{umi_red}Shannon-san and I are not conspiring together in any way.{/umi_red}'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "Huh? ...The color of Erika-san's voice was... somehow... different... just now."
 narrator 'They were words that I knew spoke the truth even without it being shown...'
 show erika_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Therefore, me being involved with Shannon-san prior to it, like telling her to pretend not to see the magic circle, or any extension of that scenario, is impossible.'
 show erika_v001 normal at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '......Nn.........'
 show nao_v002 fuan_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'And furthermore, if I were the culprit, my only opportunity to commit the crime would be after Shannon-san had already left the room.'
 show nao_v002 fuan_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Nonetheless, during that whole time period, I was together playing games with you people, so I have a perfect alibi.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide erika_v001
 hide fade onlayer curtain
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 show nao_v002 sinken at active
 show nao_v002 sinken at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I... I would like to hear that directly from Shannon-san.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'By the way, Shannon-san seems to be off work today.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Because the Ushiromiya family seems to consider the rights and privacy of their servants deeply, even if you were able to put in a message for Shannon-san while she was out, that message obviously still wouldn't reach her."
 hide erika_v001
 with Dissolve(0.2)
 narrator "Which means... I can't confirm with her whether or not the magic circle last night was a prank...?"
 show erika_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Seems like she's going to be out today and tomorrow, so little Nao-chama returning home on Sunday no longer has a chance to hear her side."
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Gh......'
 stop music fadeout 2.0
 window hide None
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 pause 1.0
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 show mion_v015 smile at mei_right
 show shion_v008 smile at mei_left
 with Dissolve(0.5)
 show shion_v008 smile at inactive
 show mion_v015 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Haah-, I'm tireeddd! Let's take a break, yeah?"
 show mion_v015 smile at inactive
 show shion_v008 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Huh? Nao-chan, you aren't doing your embroidery?"
 hide shion_v008
 hide mion_v015
 with Dissolve(0.2)
 show nao_v002 normal_close at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '......I got psyched up chatting with Erika-san.'
 show nao_v002 normal_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Psyched {i}down{/i} would be a bit more fitting here.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 smile_blush at mei_right
 show shion_v008 smile at mei_left
 with Dissolve(0.5)
 show shion_v008 smile at inactive
 show jessica_v001 smile_blush at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I might be starting to get interested in cosplay too now... I wonder what kind of outfit Kanon-kun would like on me... '
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show jessica_v001 smile_blush at inactive
 show shion_v008 smile at active
 show shion_v008 smile at jumping_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'A motive like that is highly welcome here! With beauty, the thought of that one person looking at you feeds into your confidence!♪'
 show shion_v008 smile at inactive
 show jessica_v001 odoroki_blush at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "N-Nonono, we, Kanon-kun and I aren't actually toge-..."
 show shion_v008 smile at inactive
 show jessica_v001 smile_blush at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I-I-I'm, oh, look, it's lunch time!"
 play audio 'audio/sfx/SE_332_ls_fall.wav'
 show jessica_v001 smile_blush
 show jessica_v001 smile_blush:
  yanchor 1.0
  linear 0.16666666666666666 pos (2400,1200)
 pause 0.16666666666666666
 show jessica_v001 smile_blush:
  yanchor 1.0
  pos (2400,1200)
 pause 1.0
 hide shion_v008
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'While clearly trying to hide her embarrassment, Jessica-san turned away and tried to run off.'
 narrator "It's still around 11 o'clock. It's kind of a little early to worry about getting lunch..."
 narrator "At that moment, a lightbulb appeared above Erika-san's head as she appeared to have remembered something."
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Ah, that won't do. ...To me, the incident with the lock on Mion-san's window is no laughing matter."
 hide erika_v001
 with Dissolve(0.2)
 show mion_v015 odoroki at mei_right
 show shion_v008 smile at mei_left
 with Dissolve(0.5)
 show shion_v008 smile at inactive
 show mion_v015 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "What do you mean? Wait, did Erika-san's break too?!"
 show mion_v015 odoroki at inactive
 show shion_v008 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Obviously not, Sis. What happened?'
 hide shion_v008
 hide mion_v015
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It's a bit of a silly story. I actually forgot to lock my own room."
 hide erika_v001
 with Dissolve(0.2)
 show mion_v015 smile at mei_right
 show shion_v008 fuan at mei_left
 with Dissolve(0.5)
 show shion_v008 fuan at inactive
 show mion_v015 smile at active
 show mion_v015 smile at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'How horrible!! The windows are, well, who cares about those, but the door! Oh no, not the door!!'
 show mion_v015 smile at inactive
 show shion_v008 fuan_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'I feel like forgetting to lock your room and breaking something because you underestimated your strength are two incredibly different things, though?'
 hide shion_v008
 hide mion_v015
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator '"Heeeeyy!", Jessica-san called out as she ran back over here.'
 show jessica_v001 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "L-Lunch is actually at 12 o'clock! Haah, haah..."
 show jessica_v001 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Well, that's what I thought in the first place, but thank you very much for that information."
 hide erika_v001
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v015 smile at mei_right
 show shion_v008 smile at mei_left
 with Dissolve(0.5)
 show shion_v008 smile at inactive
 show mion_v015 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Shion~. For our next photo shoot, though, can we really not replace this prop?'
 show mion_v015 smile at inactive
 show shion_v008 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah-, you finally realized, huh? I've been thinking it didn't fit well."
 camera at screenshake_transform
 pause 0.0
 show shion_v008 smile at inactive
 show mion_v015 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Huuh?! If you've been thinking that, then say something!"
 hide shion_v008
 hide mion_v015
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "My, my. How lively it's getting."
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Um, Jessica-san. Do you have a moment?'
 show nao_v002 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hm? What?'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2221.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator 'Jessica-san and I walked away from the arbor for a little.'
 narrator 'On the other hand, Erika-san appeared as though she was pretending to read, constantly observing each move people made. '
 narrator "Going too far away would make it suspicious. I'll move away just enough so that our voices can't be heard."
 show nao_v002 normal at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Um, Jessica-san... Is Shannon-san going to be off work from today?'
 show nao_v002 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Huh? Yeah, that's right! She'll be back on... Monday, I think it was?"
 show jessica_v001 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Um, truth is I've been wanting to ask Shannon-san something as quick as possible."
 show nao_v002 fuan at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "What? What's wrong?"
 show jessica_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "That's something I can only speak about with Shannon-san... \nAt the very least, can I get on a phone to contact her?"
 show nao_v002 fuan at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Uhh. My folks are, y'know, pretty strict..."
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'It seriously is just like Erika-san said.'
 narrator "Shannon-san is on leave until tomorrow. And since the Ushiromiya family highly values the privacy of their servants, it's looking like I won't be able to get one call in."
 show jessica_v001 fuan_close at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Even if they knew where she was, they wouldn't let you talk with her. They have rules like that... Sorry about it."
 show jessica_v001 fuan_close at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Ah... no. I'm sorry for asking..."
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator "I can't come up with a lie on the spot to make her want to let me get in contact. ...It seemed like it was impossible to call her."
 stop music fadeout 0.5
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Even if they knew, they wouldn't let you speak. ......Ah."
 play music "<loop 0>audio/bgm/BGM_QUEST3_COLLAB2.ogg"
 hide nao_v002
 with Dissolve(0.2)
 narrator "...Whether a servant sees something or doesn't see something is a duty of theirs... isn't that right?"
 show nao_v002 normal at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Jessica-san. ...This might be obvious, but...'
 show jessica_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'For example, right? Suppose a servant enters a guest room to make the bed or something.'
 show jessica_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...In that moment, in the case they were to accidentally see something... private, I guess, would there be some sort of confidentiality rule with that?'
 show nao_v002 normal at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Something like that, yeah! According to Genji-san, the servants are like furniture.'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Furniture does not start conversation. It silently performs its task. It does not needlessly make its presence known.'
 narrator 'So, even if they were to bare witness to something private while performing their task... they would never disclose that information.'
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'A-Another example, okay? Um... okay, Halloween! Suppose some guests who are staying in a hotel room overnight do some Halloween costume shoots in their room.'
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The Halloween costume is, like, it can be zombie makeup, right? Something pretty bloody and scary. '
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Suppose that bloody monster costume simply gets laid there on top of the bed.'
 narrator 'But then, an unaware servant comes in while on the job, mistakes it for something else, screams in horror, and goes to call the police...'
 show jessica_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...If there really was some sort of criminal activity, they would report it right away, I think? They have their duty as citizens before their duty as servants. '
 show nao_v002 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "And in case they couldn't get a grasp on the situation... I think the servants would check it out themselves to make a proper conclusion."
 show jessica_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Even with a bloody massacre on top of the bed, if they got their permission to look the other way...'
 show nao_v002 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I think it's a matter of whether or not they decide to consider the guest's privacy."
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'I suspect that Erika-san is the culprit. But Erika-san has a perfect alibi after the point Shannon-san entered the room.'
 narrator "The timeframe the magic circle sheets were prepared in was before Shannon-san entered the room. It can't be any time other than right after we went downstairs for dinner."
 narrator "Even though Shannon-san entered the room after that and saw the bed torn up with the magic circle sheets there, she didn't judge it as ill-willed."
 narrator 'Setting the blanket being disorderly aside... she saw that disgusting magic circle and saw no ill-will behind it.'
 narrator "Seeing that... could you really think to keep that private? There's no way you would...!"
 show jessica_v001 odoroki at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 normal at inactive
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'If there was a drawing written in blood all over the sheeets?! Shannon would definitely get horrified by that, I think?!'
 show nao_v002 normal at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Shannon is fine when she's calm, but she's the type to completely lose it at times like that..."
 show nao_v002 normal at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "If she did see something that strange... I don't think I can say that she would see nothing wrong..."
 show jessica_v001 fuan_close at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Yeah, right?'
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'Since the Sonozaki sisters had an excessively blank reaction to that, my confidence seeped out of me, though...'
 narrator "That magic circle prank clearly crossed the line. That prank wasn't even in the realm of hilarity!"
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Even so... Shannon-san... calmly said... "No. Please be at ease."...'
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "And then they say she isn't conspiring with Erika-san at all..."
 hide nao_v002
 with Dissolve(0.2)
 camera at screenshake_transform
 pause 0.0
 narrator 'Wait, wait, wait. Mion-san told me before. Read through the text thoroughly! Erika-san said this:'
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 narrator '{umi_red}Shannon-san and I are not conspiring together in any way.{/umi_red}'
 narrator "This... isn't this a stupid little trick?! There better be something between the lines!"
 narrator 'Erika-san is conspiring with someone. And that "someone" she\'s conspiring with has been giving instructions to Shannon-san somehow.'
 narrator 'Like for example... yeah! Cosplay photography!'
 narrator "If you're cosplaying as something scary, you'd want to tell your photographer in advance so that he doesn't get shocked..."
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...This same thought applies to the magic circle sheets, which Shannon-san thought was a normal, harmless thing!'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'The thing is... Shannon-san is the type to listen to orders.'
 narrator "I'm led to believe the whole family is like that. You could probably give orders to the servant head and the older servants as well."
 narrator "But... that's just it. Even if Shannon-san did see the magic circle, I can see her acting as if nothing had happened...!"
 show jessica_v001 fuan at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Did one of our servants mess up somehow......?'
 show jessica_v001 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'No, not at all. It might be the opposite in fact.'
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'Shannon-san simply carried out her orders as she was told.'
 show jessica_v001 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Th-then, I'll head out for now...!"
 show jessica_v001 smile at inactive
 show nao_v002 smile at active
 show nao_v002 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Thank you very much for that. Nothing really happened, so please don't worry."
 stop music fadeout 2.0
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'After making sure Jessica-san was gone, I turned around... and made eye contact with Erika-san by the arbor...'
 play music "<loop 0>audio/bgm/BGM_QUEST5_COLLAB2.ogg"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '............*giggle*.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'That face probably wants to say that she eavesdropped fully on whatever I was talking about with Jessica-san.'
 narrator 'While Erika-san was having a friendly chat with Mion-san, she observed me the whole time without so much as a hint of effort.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2341.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 normal at mei_left
 show mion_v015 smile at mei_right
 with Dissolve(0.5)
 show mion_v015 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Huh? Where'd Shion-san go?"
 show nao_v002 normal at inactive
 show mion_v015 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "She went back to the guesthouse to check for a different prop. She'll be back soon."
 hide nao_v002
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show mion_v015 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "...At any rate, Mion-san... you can be pretty shrewd, can't you?"
 show mion_v015 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Saying this is a smidge rude, but I thought you would be like a caveman afraid of fire... You're pretty good, though."
 show erika_v001 normal at inactive
 show mion_v015 smile at active
 show mion_v015 smile at updown_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ahaha! If you say that much, I'll start blushing!!"
 show erika_v001 normal at inactive
 show mion_v015 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But you're pretty good too, y'know, Erika-san? There's one thing you might have wrong, though~."
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 normal at inactive
 show mion_v015 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "The truth isn't something you reveal, it's a fabrication of reality. Or maybe it's a mixture of the two? Either way, don't mess with the next head of the Sonozaki family, you hear?"
 hide mion_v015
 hide erika_v001
 with Dissolve(0.2)
 narrator "...I don't know what those two were having a conversation about while I was talking to Jessica-san... but it feels like it was kind of fiery."
 narrator 'Even if that did happen though, Mion-san would probably just be like, "You ain\'t half bad!", and walk it off.'
 show erika_v001 normal at mei_left
 show mion_v015 futeki at mei_right
 with Dissolve(0.5)
 show mion_v015 futeki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Mion-san, let's make a promise. One of these days, I'll definitely visit Hinamizawa as a detective."
 show erika_v001 normal at inactive
 show mion_v015 smile at active
 show mion_v015 smile at nod_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Yeah, for sure! All of the club members will give you a warm welcome when you do~!'
 hide mion_v015
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Those fiery, murderous sparks that I felt in between them as their gazes met suddenly seemed like the kind in a friendly playfight.'
 narrator 'Mion-san either has more experience than me, or she just has way more guts than I do. ...She really is no joke.'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah... Shion-san came back.'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v008 sinken at mei_left
 show mion_v015 smile at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show mion_v015 smile at inactive
 show shion_v008 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Sis! I think I might have put it in a totally different place? Please forgive meee!'
 show shion_v008 sinken at inactive
 show mion_v015 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Huuuh?! Weren't you the one who went and put it someplace else before we left?!"
 hide mion_v015
 hide shion_v008
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "My, my. It's getting lively again..."
 show kanon_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal_close at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '...Please do forgive me for intruding on your conversation. Lunch has been prepared.'
 show kanon_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Isn't that right, everyone? Shall we go now, Nao-chama?"
 hide kanon_v001
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Erika-san, I've torn your alibi to pieces."
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Oh? Would that have been after dessert was served to us?'
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "No, during appetizers. It's clear to me now."
 show nao_v002 normal at inactive
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Wouldn't the full-course meals have already come out if that were the case? It would have been embarrassing for me if I made it after appetizers were already over, don't you knooow?!"
 show erika_v001 fuan at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'You had Shannon-san look the other way from the point you committed the crime onward.'
 show erika_v001 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Moreover, you carefully asserted to me that you weren't conspiring with Shannon-san up until now. But--"
 stop music fadeout 0.5
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '{umi_red}Shannon-san and I are not conspiring together in any way.{/umi_red}'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '{umi_red}Through another person or by any other means possible, it is in no way true that Shannon-san was involved behind the scenes.{/umi_red}'
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Eh......?'
 show nao_v002 fuan at inactive
 show erika_v001 fuan at active
 show erika_v001 fuan at chara_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '*sigh*. Regrettably, you missed the mark by a longshot. ...See? It would have been better for me to do it during dessert.'
 show nao_v002 fuan at inactive
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Since I wasn't directly conspiring with someone, I must have been getting someone involved indirectly. You really thought you could weasel yourself through the red truth like that... huuuuh?!"
 show erika_v001 fuan at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Nn...... uh......'
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB2.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I... I wasn't thinking like that. I don't want to be treated like a child with some... silly wordplay like that."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show nao_v002 sinken at inactive
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*cackle*... <Good>.'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'As the detective or as the culprit ...quickly losing heart is for second-rates. The only person who would keel over crying is Battler.'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'First-rates must be tough, and they {i}must{/i} be daring.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "She really is a hateable person; however, she's a bit strange. Rather than just being a hateable person... how can I put it... she's more like a rival."
 narrator "She puts me below her and gets under my skin. She's aggravating, but as an enemy, I feel like she's deserving of praise in that aspect."
 show mion_v015 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show mion_v015 smile at active
 show mion_v015 smile at jumping_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "C'mon, c'mooon, let's go get luuunch~! Huuuuuuh? You hittin' on my little Nao-chaaaan?!"
 show mion_v015 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Yes, absolutely. This sweet {i}darling{/i} of a girl must be protected at all costs before she becomes victim to a murder incident.'
 show erika_v001 normal at inactive
 show mion_v015 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ooohhh, don't you know touching her is forbidden~? If you wanna schedule with my Nao-chan, you're gonna have to get through her manager fiiirst!♪"
 show mion_v015 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'And so? Will that be your move?'
 play audio 'audio/sfx/SE_211_electric.wav'
 show erika_v001 normal at inactive
 show mion_v015 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Of course. Round over. Your next move better be promising, yeah~?'
 hide erika_v001
 hide mion_v015
 with Dissolve(0.2)
 narrator "Yeah, there are definitely sparks flying between those two. But even though there's supposed to be enmity between them, it's almost like they've combined that with the coolness of a movie scene."
 narrator "...This must be what it's like to be tough like a first-rate......"
 show shion_v008 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show shion_v008 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Nao-san, last night, didn't you get super shocked from that prank?"
 show shion_v008 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Eh? Ah, yeah...'
 show nao_v002 fuan at inactive
 show shion_v008 normal_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'If that was the work of a witch...'
 show nao_v002 fuan at inactive
 show shion_v008 futeki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Oyashiro-sama's curse might be able to exist too, right?"
 hide nao_v002
 hide shion_v008
 with Dissolve(0.2)
 narrator 'Uh... what? What does that mean......?'
 narrator "Shion-san's smile was about 90%% reliable... and 10%% daring, with a bit of creepiness mixed in..."
 call chapter_end
 jump event01_30_07