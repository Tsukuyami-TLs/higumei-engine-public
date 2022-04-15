label chara472001_01:
 show black_background onlayer black
 $ event_store.current_event='chara472001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara472001_01'
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
 show expression 'images/bg/AdvBg_2190.png' as bg
 play music "<loop 0>audio/bgm/BGM_EVENT_TOP_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v001 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v001 odoroki at active
 show nao_v001 odoroki at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh...? ...Th-this place is...?!'
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 odoroki at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...It's been a while, Nao."
 show beatrice_v001 smile at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Y-You're... the Golden Witch, Beatrice...?"
 show nao_v001 normal at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "*cackle*...So your memory has returned. I'm glad to see that."
 show beatrice_v001 smile_close at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...If anything, I'm curious as to how I forgot about all this."
 show nao_v001 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Oh, please, it's nothing particularly strange; your memory was simply erased by magic."
 show beatrice_v001 smile at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I forgot because... of magic...?'
 show nao_v001 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Yes, magic. Me inviting you here has gotten a little out of hand, so please forgive me.'
 show beatrice_v001 normal_close at inactive
 show nao_v001 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'You invited... what the... huh?'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 odoroki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Long time no SEE.'
 show dlanor_v001 normal at inactive
 show nao_v001 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "You're... Dlanor-san? Which means that pervert girl is also here...?!"
 show nao_v001 sinken at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'RELAX. Erika is not HERE. Since it would be a hassle if thou were to meet, we brought thou HERE.'
 show dlanor_v001 normal_close at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Um... what do you mean by that?'
 hide dlanor_v001
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show nao_v001 fuan at inactive
 show beatrice_v001 smile at active
 show beatrice_v001 smile at jumping_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Let's put such trivialities aside! Look here, we have black tea from my teacher and cookies from Ronove! "
 show nao_v001 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Everything will be fine if you just sit and have some tea.'
 show nao_v001 fuan at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'After that, I promise to return you to where you came from. '
 show beatrice_v001 smile_close at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...In other words, I am supposed to quietly drink tea with you until then?'
 show nao_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Exactly. Are you displeased?'
 show beatrice_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Absolutely not; I love tea parties. So I'll take your offer and drink with you at ease."
 hide beatrice_v001
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "These cookies are extremely TASTY. I'm sure thou shalt enjoy THEM..."
 show dlanor_v001 normal_close at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh? What do you mean?'
 hide dlanor_v001
 show beatrice_v001 smile_close at mei_left
 with Dissolve(0.5)
 show nao_v001 normal at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...Hm. It seems Lady Dlanor is unsure of what to refer to you as.'
 show nao_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'She typically will use the title of "Miss", but due to your age, that may come off as insulting.'
 show beatrice_v001 normal at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I don't particularly mind... but for now, just Nao is fine. ...Can I also just call you Dlanor?"
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Yes, that is FINE. ...Then, NAO. Do you trust Lady BEATRICE?'
 show dlanor_v001 normal at inactive
 show nao_v001 smile at active
 show nao_v001 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yes. She saved me when I was in danger, and I have no reason to doubt somebody who has saved my life.'
 show dlanor_v001 normal at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, these cookies are really delicious. May I have another?'
 hide nao_v001
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_center
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Mhm, you don't need to worry about that. Just eat them."
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...This is a rare SIGHT. Lady Beatrice is being quite GENEROUS. Are you still held up over what happened EARLIER?'
 show dlanor_v001 normal at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...What an arrogant question, Lady Dlanor. That is irrelevant to our current situation.'
 show beatrice_v001 smile_close at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'That was... clearly an impolite REMARK. My APOLOGIES.'
 hide beatrice_v001
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal_close at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...?'
 show nao_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'I will change my QUESTION. Nao, do you like MYSTERIES?'
 show dlanor_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Mysteries... you mean like mystery novels?'
 show nao_v001 normal at inactive
 show dlanor_v001 normal at active
 show dlanor_v001 normal at nod_transform
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'YES. I would like to hear your honest THOUGHTS.'
 show dlanor_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Hm... I don't have a particular favorite. I've read the famous ones, like the great British detective and the Armchair detective."
 show dlanor_v001 normal at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Is what I'd say, but it's all from the elementary school library, so it's edited so that kids can read it."
 show nao_v001 fuan at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Then, would you like to know the origin... of the Knox DECALOGUE?'
 show dlanor_v001 normal at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The origin... of the Knox Decalogue...?'
 show dlanor_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'You and Erika used the Knox Decalogue during the last logic battle. \nIn the end, what purpose did that serve?'
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'What purpose it served... hmm... this is a basic question, but if you wish to enjoy mysteries, you should be aware of how significant it is. '
 show nao_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "So rejoice. Lady Dlanor is an expert in Knox's Decalogue. "
 show nao_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'We have the time, so granting you this knowledge alone will be fine.'
 hide nao_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal_close at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'I do not MIND. Now THEN...'
 call chapter_end
 jump chara472001_02