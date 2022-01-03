label chara472001_01:
 show black_background onlayer black
 $ event_store.current_event='chara472001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara472001_01'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 play music 'audio/bgm/BGM_EVENT_TOP_COLLAB2.ogg'
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v001 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v001 odoroki at jump_transform,active
 nao 'Huh...? ...Th-this place is...?!'
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v001 odoroki at inactive
 beatrice "...It's been a while, Nao."
 show nao_v001 normal at active
 show beatrice_v001 smile at inactive
 nao "Y-you're... the Golden Witch Beatrice...?"
 show beatrice_v001 smile_close at active
 show nao_v001 normal at inactive
 beatrice "*cackle*... so your memory has returned. I'm glad to see that."
 show nao_v001 fuan at active
 show beatrice_v001 smile_close at inactive
 nao "...If anything, I'm curious as to how I forgot about all this."
 show beatrice_v001 smile at active
 show nao_v001 fuan at inactive
 beatrice "Oh, please, it's nothing particularly strange; your memory was simply erased by magic."
 show nao_v001 normal at active
 show beatrice_v001 smile at inactive
 nao 'I forgot because... of magic...?'
 show beatrice_v001 normal_close at active
 show nao_v001 normal at inactive
 beatrice 'Yes, magic. Me inviting you here has gotten a little out of hand, so please forgive me.'
 show nao_v001 odoroki at active
 show beatrice_v001 normal_close at inactive
 nao 'You invited... what the... huh?'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 odoroki at inactive
 dlanor '...Long time no SEE.'
 show nao_v001 sinken at active
 show dlanor_v001 normal at inactive
 nao "You're... Dlanor? Which means that pervert girl is also here...?!"
 show dlanor_v001 normal_close at active
 show nao_v001 sinken at inactive
 dlanor 'RELAX. Erika is not HERE. Since it would be a hassle if you were to meet, we brought you HERE.'
 show nao_v001 fuan at active
 show dlanor_v001 normal_close at inactive
 nao 'Um... what do you mean by that?'
 hide dlanor_v001
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show beatrice_v001 smile at jumping_transform,active
 show nao_v001 fuan at inactive
 beatrice "Let's put such trivialities aside! Look here, we have black tea from the Master and cookies from Ronove! "
 show beatrice_v001 smile at active
 show nao_v001 fuan at inactive
 beatrice 'Everything will be fine if you just sit and have some tea.'
 show beatrice_v001 smile_close at active
 show nao_v001 fuan at inactive
 beatrice 'After that, I promise to return you to where you came from. '
 show nao_v001 normal at active
 show beatrice_v001 smile_close at inactive
 nao '...In other words, I am supposed to quietly drink tea with you until then?'
 show beatrice_v001 smile at active
 show nao_v001 normal at inactive
 beatrice 'Exactly. Are you displeased?'
 show nao_v001 smile at active
 show beatrice_v001 smile at inactive
 nao "Absolutely not; I love tea parties. So I'll take your offer and leisurely drink with you."
 hide beatrice_v001
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show nao_v001 smile at inactive
 dlanor "These cookies are extremely TASTY. I'm sure thou will enjoy THEM..."
 show nao_v001 normal at active
 show dlanor_v001 normal_close at inactive
 nao 'Huh? What do you mean?'
 hide dlanor_v001
 show beatrice_v001 smile_close at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile_close at active
 show nao_v001 normal at inactive
 beatrice '...Hm. It seems Lady Dlanor is unsure of which title to call you.'
 show beatrice_v001 normal at active
 show nao_v001 normal at inactive
 beatrice 'She typically will use the title of "miss", but due to your age, that may come off as insulting.'
 show nao_v001 smile at active
 show beatrice_v001 normal at inactive
 nao "I don't particuarly mind... for now, just Nao is fine. ...Can I also just call you Dlanor?"
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 smile at inactive
 dlanor 'Yes, that is FINE. ...Then, NAO. Do you trust Lady BEATRICE?'
 show nao_v001 smile at nod_transform,active
 show dlanor_v001 normal at inactive
 nao 'Yes. She saved me when I was in danger, and I have no reason to doubt somebody who has saved my life.'
 show nao_v001 smile at active
 show dlanor_v001 normal at inactive
 nao 'Ah, these cookies are really delicious. May I have another?'
 hide nao_v001
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_center
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 beatrice "Mhm, you don't need to worry about that. Just eat them."
 hide beatrice_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor '...This is a rare SIGHT. Lady Beatrice is being quite GENEROUS. Are you still held up over what happened EARLIER?'
 show beatrice_v001 smile_close at active
 show dlanor_v001 normal at inactive
 beatrice '...What an arrogant question, Lady Dlanor. That is irrelevant to our current situation.'
 show dlanor_v001 normal_close at active
 show beatrice_v001 smile_close at inactive
 dlanor 'That was... clearly an impolite REMARK. I APOLOGIZE.'
 hide beatrice_v001
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v001 normal at active
 show dlanor_v001 normal_close at inactive
 nao '...?'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'I will change my QUESTION. Nao, do you like MYSTERIES?'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao 'Mysteries... you mean like mystery novels?'
 show dlanor_v001 normal at nod_transform,active
 show nao_v001 normal at inactive
 dlanor 'YES. I would like to hear your honest THOUGHTS.'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao "Hm... I don't have a particular favorite. I've read the famous ones, like the great British detective and armchair detective."
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao "...Is what I'd say, but it's all from the elementary school library, so it's edited so that kids can read it."
 show dlanor_v001 normal at active
 show nao_v001 fuan at inactive
 dlanor 'Then, would you like to know the origin... of the Knox DECALOGUE?'
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao 'The origin... of the Knox Decalogue...?'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao 'You and Erika used the Knox Decalogue during the last logic battle. In the end, what purpose did that serve?'
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v001 normal at inactive
 beatrice 'What purpose it served... hmm... this is a basic question, but if you wish to enjoy mysteries, you should know its reason for existing. '
 show beatrice_v001 smile at active
 show nao_v001 normal at inactive
 beatrice "You should be pleased. Lady Dlanor is an expert in Knox's Decalogue. "
 show beatrice_v001 smile at active
 show nao_v001 normal at inactive
 beatrice 'We have the time, so granting her this knowledge alone will be fine.'
 hide nao_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal_close at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 dlanor 'I do not MIND. Now THEN...'
 call chapter_end
 jump chara472001_02